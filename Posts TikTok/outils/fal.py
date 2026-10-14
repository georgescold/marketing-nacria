import base64, json, os, sys, time, requests

KEY = os.environ["FAL_KEY"]
H = {"Authorization": f"Key {KEY}", "Content-Type": "application/json"}


def run(model, args, out, timeout=300):
    """Submit to the fal queue, wait, and save the first image to `out`."""
    r = requests.post(f"https://queue.fal.run/{model}", headers=H, json=args, timeout=60)
    r.raise_for_status()
    sub = r.json()
    status_url, resp_url = sub["status_url"], sub["response_url"]
    t0 = time.time()
    while True:
        s = requests.get(status_url, headers=H, timeout=60).json()
        if s.get("status") == "COMPLETED":
            break
        if time.time() - t0 > timeout:
            raise TimeoutError(model)
        time.sleep(2)
    res = requests.get(resp_url, headers=H, timeout=60).json()
    imgs = res.get("images") or ([res["image"]] if res.get("image") else [])
    if not imgs:
        raise RuntimeError(json.dumps(res)[:500])
    url = imgs[0]["url"]
    data = base64.b64decode(url.split(",", 1)[1]) if url.startswith("data:") else requests.get(url, timeout=120).content
    open(out, "wb").write(data)
    return url


def upload(path):
    """Return a data URI usable as image_url input."""
    ext = os.path.splitext(path)[1].lstrip(".").replace("jpg", "jpeg")
    return f"data:image/{ext};base64," + base64.b64encode(open(path, "rb").read()).decode()


if __name__ == "__main__":
    model, out = sys.argv[1], sys.argv[2]
    args = json.loads(sys.argv[3])
    print(run(model, args, out))
