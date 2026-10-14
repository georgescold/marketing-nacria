"""Nacria app mock shared by the three accounts' CTA slides: a large, legible "today" screen that shows the benefits at a glance
(12-week plan, 3-step evening routine, weekly skin photo in the same light, cycle noted next to the skin). It is drawn in HTML with
the Nacria tokens and does not have to match the real app screen by screen.

phone(name, face_uri, left, top, scale=1, height=1250) returns a self-contained block (its own <style>), designed at 566 px wide.
"""
import html

CSS = '''
.nx-ph{position:absolute;width:566px;background:#1d1b20;border-radius:78px;padding:14px;font-family:"DM Sans",sans-serif;color:#2E2A33;
 box-shadow:0 34px 70px rgba(46,42,51,.30),0 0 0 2px #3a363d inset}
.nx-ph .notch{position:absolute;left:50%;top:28px;width:150px;height:40px;margin-left:-75px;background:#1d1b20;border-radius:20px;z-index:2}
.nx-ph .scr{width:100%;height:100%;border-radius:64px;background:#FBF7F2;overflow:hidden;padding:0 30px}
.nx-ph .status{display:flex;justify-content:space-between;padding:26px 14px 0;font-size:24px;font-weight:700}
.nx-ph .hello{display:flex;justify-content:space-between;align-items:center;margin-top:34px}
.nx-ph .brand{font-family:Fraunces,serif;font-size:28px;color:#A95A3E;font-weight:500;letter-spacing:.5px}
.nx-ph .hi{font-family:Fraunces,serif;font-size:50px;font-weight:450;letter-spacing:-.5px;line-height:1.1}
.nx-ph .av{width:82px;height:82px;border-radius:50%;background-position:center;background-size:cover;border:4px solid #F1DCD5}
.nx-ph .prog{margin-top:24px}.nx-ph .lab{display:flex;justify-content:space-between;font-size:29px;font-weight:700}
.nx-ph .lab span{color:#A95A3E}
.nx-ph .bar{display:flex;gap:6px;margin-top:12px}.nx-ph .bar i{flex:1;height:16px;border-radius:8px;background:#F1DCD5}
.nx-ph .bar i.on{background:#A95A3E}
.nx-ph .card{background:#fff;border-radius:28px;padding:24px 26px;margin-top:24px;box-shadow:0 8px 22px rgba(46,42,51,.08)}
.nx-ph .ct{font-size:32px;font-weight:700;display:flex;justify-content:space-between;align-items:center}
.nx-ph .ct small{font-size:24px;font-weight:600;color:#496557;background:#E4ECE7;border-radius:20px;padding:6px 14px}
.nx-ph .row{display:flex;align-items:center;gap:20px;margin-top:20px;font-size:32px;font-weight:500}
.nx-ph .ck{width:48px;height:48px;border-radius:50%;flex:none;display:flex;align-items:center;justify-content:center;font-size:28px;
 font-weight:800;color:#fff;background:#8FA89A}
.nx-ph .ck.todo{background:none;border:4px solid #DCCFC6}
.nx-ph .row.done span{color:#70666E}
.nx-ph .pp{display:flex;gap:22px;align-items:center}
.nx-ph .ph{width:150px;height:150px;border-radius:22px;background-position:center;background-size:cover;flex:none;position:relative}
.nx-ph .ph b{position:absolute;right:-10px;bottom:-10px;width:46px;height:46px;border-radius:50%;background:#8FA89A;color:#fff;font-size:26px;
 display:flex;align-items:center;justify-content:center;border:4px solid #fff}
.nx-ph .pp h4{font-size:32px}.nx-ph .pp p{font-size:26px;color:#496557;font-weight:600;margin-top:6px}
.nx-ph .pp p.m{color:#70666E;font-weight:500}
.nx-ph .chips{display:flex;gap:12px;margin-top:22px}
.nx-ph .chip{border-radius:30px;padding:12px 22px;font-size:28px;font-weight:700;background:#F1DCD5;color:#A95A3E}
.nx-ph .chip.s{background:#E4ECE7;color:#496557}
'''


def phone(name, face_uri, left, top, scale=1.0, height=1250):
    bar = "".join(f'<i class="{"on" if k < 6 else ""}"></i>' for k in range(12))
    rows = "".join(f'<div class="row {c}"><div class="ck {"" if c else "todo"}">{"✓" if c else ""}</div><span>{t}</span></div>'
                   for t, c in [("Nettoyant doux", "done"), ("Sérum apaisant", "done"), ("Crème légère", "")])
    face = f'background-image:url("{face_uri}")'
    screen = (f'<div class="status"><span>9:41</span><span>●●● ▮</span></div>'
              f'<div class="hello"><div><div class="brand">nacria</div><div class="hi">Bonjour {html.escape(name)}</div></div>'
              f'<div class="av" style=\'{face}\'></div></div>'
              f'<div class="prog"><div class="lab">Semaine 6 sur 12<span>50 %</span></div><div class="bar">{bar}</div></div>'
              f'<div class="card"><div class="ct">Ce soir<small>3 gestes</small></div>{rows}</div>'
              f'<div class="card pp"><div class="ph" style=\'{face}\'><b>✓</b></div><div><h4>Point peau</h4><p>Faite ce matin</p>'
              f'<p class="m">Même lumière que la sem. 5</p></div></div>'
              f'<div class="chips"><div class="chip">● Règles · jour 2</div><div class="chip s">Peau notée</div></div>')
    return (f'<style>{CSS}</style><div style="position:absolute;left:{left}px;top:{top}px;zoom:{scale}">'
            f'<div class="nx-ph" style="position:relative;height:{height}px"><div class="notch"></div><div class="scr">{screen}</div></div></div>')


def face_crop(src, box, dst):
    """Square crop (x0, y0, x1 as fractions of the width/height) saved as a 300 px thumbnail; returns its file URI."""
    from PIL import Image
    x0, y0, x1 = box
    im = Image.open(src).convert("RGB")
    side = (x1 - x0) * im.width
    im.crop((round(x0 * im.width), round(y0 * im.height), round(x0 * im.width + side), round(y0 * im.height + side))) \
      .resize((300, 300), Image.LANCZOS).save(dst)
    return dst.as_uri()


def follow_badge(avatar_uri, label="appuie sur le +", sub=None, color="#2E2A33", size=132):
    """TikTok-like profile picture with the red follow "+", and the instruction next to it (follow CTA, no app)."""
    plus = round(size * .36)
    sub_html = f'<div style="font-size:30px;font-weight:600;opacity:.75;margin-top:6px">{html.escape(sub)}</div>' if sub else ""
    return (f'<div style="display:flex;align-items:center;gap:30px;font-family:\'DM Sans\',sans-serif;color:{color}">'
            f'<div style="position:relative;width:{size}px;height:{size}px;flex:none">'
            f'<div style="width:{size}px;height:{size}px;border-radius:50%;background:url(\'{avatar_uri}\') center/cover;border:5px solid #fff;'
            f'box-shadow:0 10px 26px rgba(0,0,0,.25)"></div>'
            f'<div style="position:absolute;left:50%;bottom:-{plus // 2}px;margin-left:-{plus // 2}px;width:{plus}px;height:{plus}px;'
            f'border-radius:50%;background:#FE2C55;color:#fff;font-size:{round(plus * .8)}px;font-weight:800;line-height:{plus - 6}px;'
            f'text-align:center;border:4px solid #fff">+</div></div>'
            f'<div style="font-size:42px;font-weight:800;line-height:1.1">← {html.escape(label)}{sub_html}</div></div>')
