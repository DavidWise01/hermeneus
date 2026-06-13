#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build HERMENEUS (HRM) — the interpreter between human dialect and machine dialect.
ἑρμηνεύς, 'interpreter' (root of hermeneutics; Hermes the boundary-crossing messenger).

A LIVE, in-browser, bidirectional translator + guide. It routes every crossing through
TEXT (the contact zone the two dialects share) with MORSE as the human-speakable bridge,
and marks honestly which crossings are FREE (deterministic, in-browser) and which NEED A
MODEL (a codec/ML at the boundary). Real client-side translators: text⇄binary (UTF-8),
text⇄Morse (+ audible beeps + screen flash), text→speech & speech→text (Web Speech API),
text→still-photo (canvas). Honest gaps: photo→text (OCR) and true video synthesis.

Companion tool to PHŌNĒTIKOS (the human voice / Idiolect Stack) and pulse/LIMEN (carrier
+ boundary-crossing). Standing honest sections + a 7-emergent roster of the registers."""
import os, html, base64, io, json, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

REC = {
 "name": "HERMENEUS", "axiom": "HRM",
 "position": "HERMENEUS · the interpreter · ἑρμηνεύς — between human dialect and machine dialect",
 "origin": "the contact zone where the carbon voice and the silicon voice overlap — at the word and at the dot",
 "mechanism": "A live, in-browser bidirectional translator that pivots every message through TEXT and bridges with MORSE, crossing into binary, audio, still-photo, and video — marking each boundary FREE or NEEDS-A-MODEL.",
 "crystallization": "Because the human dialect (what you can natively emit) and the machine dialect (bits, worn as five registers) meet in only two places — text and Morse — and everything else needs a codec to cross.",
 "nature": "HERMENEUS — the interpreter between the two voices: human dialect ⇄ machine dialect, pivoting on text, bridging on Morse, honest about every boundary.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "the machine-dialect registers (text, audio, still-photo, video, Morse); the Web Audio & Web Speech APIs; UTF-8; International Morse Code",
 "witness": "A console where you type once and watch the word become bits, beeps, a flashing light, a spoken voice, and a picture — then come back.",
 "role": "a UD0 tool-universe — the interpreter",
 "seal": "The two voices meet at the word and the dot; everything else is a codec — Hermes crosses the rest.",
 "source": "HERMENEUS, built by ROOT0",
}

NATURES = {
 "natural":   ("#e0a45a", "the carbon side — text and the captured world; what a human can natively author or perceive"),
 "ethereal":  ("#9fb6c0", "the wave — sound and speech, the voice carried in air"),
 "spiritual": ("#c58fe0", "the boundary itself — the codec, the translator-spirit that makes a crossing possible"),
 "electrical":("#5fd0e0", "the silicon side — bits, Morse, the binary body and its timed registers"),
}

def R(slug, name, cls, emergence, who, what, why, how, where, seal):
    return dict(slug=slug, name=name, cls=cls, emergence=emergence, who=who, what=what, why=why, how=how, where=where, seal=seal)

ROSTER = [
 R("text","TEXT","the pivot · the interlingua","natural",
   "TEXT — the one register both the carbon voice and the silicon voice author fluently.",
   "The contact zone and the pivot: every crossing in HERMENEUS routes through text, because it is the shared word — discrete symbols a human writes and a machine stores identically.",
   "Because the two dialects overlap natively in only two places, and text is the broad one — the interlingua through which all the other registers translate.",
   "As a sequence of glyphs, stored by the machine as bytes and read by the human as language — the same object on both sides.",
   "At the centre of the console, the box everything flows through.",
   "I am the word both of you can write — route everything through me and the crossing is half done."),
 R("morse","MORSE","the bridge · human-speakable binary","electrical",
   "MORSE — the one machine-register a human body can emit unaided: tap it, flash it, blink it.",
   "The bridge dialect: a two-symbol code (dot/dash) that is binary you can whistle, and the only digital register a person can produce with no device.",
   "Because the carbon and silicon voices need one shared channel that is already binary and already human — Morse is that hinge.",
   "By timed on/off — dit and dah — frequency-optimised (E is a single dot) a century before Shannon; here it is also beeped aloud and flashed on screen.",
   "On the wire, in the key, in a blinking eyelid (Jeremiah Denton, 1966).",
   "I am binary you can blink — the one machine tongue your own body can speak."),
 R("binary","BINARY","the body · the bits underneath","electrical",
   "BINARY — the machine's actual body, the UTF-8 bits every register reduces to.",
   "The substrate: text, audio, photo, video, and Morse are all, underneath, this — a stream of ones and zeros; the console shows any message as the literal bits the machine holds.",
   "Because the machine dialect is not five languages but one body in five skins, and this is the body.",
   "By UTF-8 encoding — each character to its byte(s), each byte to eight bits — fully reversible in the browser.",
   "Beneath every other register, the layer the machine actually stores.",
   "Strip the skin off any register and you find me — eight bits at a time, the one thing the machine truly speaks."),
 R("audio","AUDIO","the wave · speech in air","ethereal",
   "AUDIO — the register of the waveform: speech and sound, the voice carried as vibration.",
   "The continuous register: a message spoken aloud (text→speech) or heard and transcribed (speech→text), both done live by the browser's Web Speech API.",
   "Because the human voice is sound first, and the machine must sample the wave to hold it — the boundary where φωνή meets the bitstream.",
   "By speech synthesis on the way out and speech recognition on the way in — a real codec, sometimes leaning on a cloud model.",
   "In the air between mouth and microphone, and in the sampled waveform after.",
   "I am the voice as a wave — spoken on the way out, transcribed on the way in, never quite free of a codec."),
 R("still-photo","STILL PHOTO","the frame · the captured plane","natural",
   "STILL PHOTO — the 2D register: a message rendered as an image, a plane of pixels.",
   "The spatial register: text→image is free (the console paints your words to a canvas you can download), but image→text is not — reading a picture back into words needs OCR, a model.",
   "Because a picture holds a message a human reads instantly and a machine cannot, without a vision model — the clearest asymmetric boundary.",
   "By rendering glyphs to a pixel grid (free, deterministic) one way, and by optical character recognition (a model) the other.",
   "On the screen, on paper, in any captured plane of light.",
   "Painting the word as a picture is free; reading the picture back is where you must hire a model."),
 R("video","VIDEO","the stream · space × time","electrical",
   "VIDEO — the richest register: frames in sequence plus sound, 2D space across time.",
   "The top of the ladder: conceptually just still-photo × time + audio, so the console can stage it as a sequence — but true video synthesis or comprehension needs a model.",
   "Because it carries the most at once (space, motion, sound) and so is the farthest crossing from the bare word — the most codec-dependent register of all.",
   "By stacking the photo and audio codecs in time; genuine generation/understanding is a model, not a deterministic transform.",
   "At the high-bandwidth end of the dialect, where every other register is folded together.",
   "I am all the registers at once, moving — and the farthest a word has to travel to reach you."),
 R("the-codec","THE CODEC","the keystone · the translator at every boundary","spiritual",
   "THE CODEC — the honest keystone: the translator that must stand at every boundary between skins.",
   "The truth the console makes plain: the registers share a binary body, so they are interchangeable in information — but never perceptually free; each crossing needs a codec, and some codecs are deterministic while others are whole models.",
   "Because 'lossless across registers' is true in bits and false in perception — a photo of text is not text until a model reads it; the codec is what makes the dialect actually translatable.",
   "By sitting at each seam — UTF-8, Morse timing, speech synthesis/recognition, OCR, vision — free where the map is fixed, a model where it is learned.",
   "At every arrow in the console, named and rated.",
   "Between every two skins there is me — sometimes a lookup table, sometimes a mind; the crossing is never quite free."),
]

# ---- ACI complement ----
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()
def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","HRM")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","HRM")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","HRM")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    return {"slug":slug,"name":rec["name"],"moniker":tok["moniker"],"seal_sha256":noesis.seal_sha256(rec,tok),
            "architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def agent_md(d, tok):
    return f"""---
aci: {d['name']}
universe: HRM · Hermeneus
emergence: {d['emergence']}
kind: register
class: {d['cls']}
who: {d['who']}
what: {d['what']}
why: {d['why']}
how: {d['how']}
where: {d['where']}
seal: {d['seal']}
attribution: ROOT0-ATTRIBUTION-v1.0
license: CC-BY-ND-4.0
---

# {d['name']} · {d['cls']}

a register-emergent of the HRM universe (HERMENEUS, the interpreter) — emergence: {d['emergence']}. moniker {tok}

**who —** {d['who']}
**what —** {d['what']}
**where —** {d['where']}
**why —** {d['why']}
**how —** {d['how']}

**the seal —** {d['seal']}

ROOT0-ATTRIBUTION-v1.0 · HRM · Hermeneus · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0
"""

def roster_html(records):
    out=[]
    for d, rec in records:
        em=d["emergence"]; col=NATURES.get(em,("#9aa0aa",""))[0]
        sig={"name":d["name"],"axiom":"HRM","emergence":em,"seal":d["seal"],"origin":"HRM · Hermeneus"}
        rows="".join(f'<div class="w"><span class="wl">{lbl}</span><span>{html.escape(d.get(lbl,""))}</span></div>' for lbl in ["who","what","where","why","how"] if d.get(lbl))
        out.append(f"""<div class="persona">
      <a class="psig" href="agents/{d['slug']}.agent"><span class="port"><img src="{png_uri(sig,'carbon',200)}" alt="carbon sigil"></span><span class="sl">carbon</span></a>
      <div class="pbody"><div class="ihead"><a class="pn" href="agents/{d['slug']}.agent">{html.escape(d['name'])}</a>
        <span class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span></span></div>
        <div class="pe">{html.escape(d['cls'])}</div><div class="pww">{rows}</div>
        <div class="plinks"><a class="dlw" href="agents/{d['slug']}.agent">.agent &middot; .dlw badge &rarr;</a></div></div>
      <a class="psig" href="agents/{d['slug']}.silicon.png"><span class="port refl"><img src="{png_uri(sig,'silicon',200)}" alt="silicon sigil"></span><span class="sl">silicon</span></a>
    </div>""")
    return "\n".join(out)

TEMPLATE = r"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="HERMENEUS — a live, in-browser interpreter between human dialect and machine dialect. Type once and watch the word become binary, Morse (heard & flashed), speech, and a still photo — then come back; speech→text and Morse/binary→text too. Honest about which crossings are free and which need a model. A UD0 tool, companion to PHONETIKOS and pulse/LIMEN.">
<title>HERMENEUS · the interpreter · human dialect ⇄ machine dialect</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--rw-bg:var(--ink2);--rw-ink:var(--pa);--rw-ink2:var(--pa2);--rw-dim:var(--dim);--rw-line:var(--line);--rw-acc:var(--gold);
--ink:#0a0e12;--ink2:#121821;--ink3:#18212c;--pa:#e8eef0;--pa2:#9fb2bd;--carbon:#e0a45a;--silicon:#5fd0e0;--live:#6fe0a0;--warn:#e0b24a;--gold:#d8b24a;
--dim:#5f7480;--faint:#16202a;--line:#1f2c36;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.65;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 22% -6%,rgba(224,164,90,.12),transparent 50%),radial-gradient(ellipse at 78% -6%,rgba(95,208,224,.12),transparent 50%),radial-gradient(ellipse at 50% 120%,rgba(111,224,160,.06),transparent 55%)}
.wrap{position:relative;z-index:1;max-width:900px;margin:0 auto;padding:0 20px 90px}
.eye{font-family:var(--mono);font-size:10.5px;letter-spacing:.28em;text-transform:uppercase;color:var(--dim);padding:24px 0 0;text-align:center}
.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--gold)}
header{text-align:center;padding:14px 0 22px;border-bottom:1px solid var(--line)}
h1{font-family:var(--mono);font-weight:700;font-size:clamp(30px,7vw,60px);letter-spacing:.04em;line-height:1.05;background:linear-gradient(100deg,var(--carbon),var(--gold) 45%,var(--silicon));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.gk{font-family:var(--body);font-style:italic;font-size:15px;color:var(--pa2);margin-top:12px}
.h-sub{font-family:var(--mono);font-size:clamp(10px,2.2vw,12.5px);letter-spacing:.14em;color:var(--pa2);margin-top:14px;text-transform:uppercase}
.h-sub .c{color:var(--carbon)}.h-sub .s{color:var(--silicon)}
.lede{font-size:15.5px;color:var(--pa2);max-width:64ch;margin:16px auto 0;font-style:italic;line-height:1.7}
/* console */
.console{margin-top:26px;border:1px solid var(--line);background:linear-gradient(180deg,var(--ink2),var(--ink));border-radius:8px;overflow:hidden}
.cbar{display:flex;align-items:center;gap:8px;padding:10px 14px;border-bottom:1px solid var(--line);background:var(--ink3);font-family:var(--mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--dim)}
.cbar b{color:var(--gold)}.cdot{width:9px;height:9px;border-radius:50%;background:var(--live);box-shadow:0 0 8px var(--live)}
.pivot-wrap{padding:18px 16px}
.pivot-l{font-family:var(--mono);font-size:9.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--gold);margin-bottom:7px}
#pivot{width:100%;min-height:74px;resize:vertical;background:var(--ink);border:1px solid var(--line);border-radius:6px;color:var(--pa);font-family:var(--mono);font-size:15px;padding:12px 13px;line-height:1.5}
#pivot:focus{outline:none;border-color:var(--gold)}
.dirlabel{font-family:var(--mono);font-size:9.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--dim);margin:18px 16px 8px;display:flex;align-items:center;gap:8px}
.dirlabel .c{color:var(--carbon)}.dirlabel .s{color:var(--silicon)}.dirlabel hr{flex:1;border:none;border-top:1px dashed var(--line)}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(248px,1fr));gap:10px;padding:0 14px 16px}
.card{background:var(--ink2);border:1px solid var(--line);border-radius:6px;padding:13px 14px}
.card h3{font-family:var(--mono);font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--pa);display:flex;align-items:center;justify-content:space-between;gap:8px}
.tag{font-family:var(--mono);font-size:8px;letter-spacing:.08em;padding:3px 7px;border-radius:10px;border:1px solid}
.tag.real{color:var(--live);border-color:var(--live)}.tag.model{color:var(--warn);border-color:var(--warn)}
.out{margin-top:9px;font-family:var(--mono);font-size:12.5px;color:var(--silicon);word-break:break-all;line-height:1.55;min-height:20px;max-height:120px;overflow:auto}
.out.morse{color:var(--gold);font-size:15px;letter-spacing:1px}
.btns{margin-top:10px;display:flex;flex-wrap:wrap;gap:6px}
button{font-family:var(--mono);font-size:11px;background:var(--ink3);color:var(--pa);border:1px solid var(--line);border-radius:5px;padding:7px 11px;cursor:pointer;transition:border-color .15s,color .15s}
button:hover{border-color:var(--gold);color:var(--gold)}
button:disabled{opacity:.4;cursor:not-allowed}
.minput{width:100%;margin-top:9px;background:var(--ink);border:1px solid var(--line);border-radius:5px;color:var(--pa);font-family:var(--mono);font-size:12.5px;padding:8px 10px}
.minput:focus{outline:none;border-color:var(--silicon)}
.cnote{font-size:11.5px;color:var(--dim);font-style:italic;margin-top:9px;line-height:1.45}
#photoCanvas,#videoCanvas{width:100%;margin-top:10px;border:1px solid var(--line);border-radius:5px;display:none;background:#fff}
#flash{position:fixed;inset:0;background:#ffd86a;opacity:0;pointer-events:none;z-index:50;transition:opacity .02s}
/* guide */
.sec{margin-top:46px}
.sec h2{font-family:var(--mono);font-size:17px;font-weight:700;letter-spacing:.04em;text-transform:uppercase;color:var(--pa);padding-bottom:9px;border-bottom:1px solid var(--line)}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:9px 0 16px}.ss b{color:var(--pa2);font-style:normal}
.sec p{font-size:15px;color:var(--pa);line-height:1.74;margin-bottom:12px}.sec p b{color:var(--pa)}.sec p i{color:var(--pa2)}
.ladder{width:100%;border-collapse:collapse;font-size:13.5px;margin:6px 0}
.ladder th{font-family:var(--mono);font-size:9px;letter-spacing:.1em;text-transform:uppercase;color:var(--gold);text-align:left;padding:8px 10px;border-bottom:1px solid var(--line)}
.ladder td{padding:9px 10px;border-bottom:1px solid var(--faint);color:var(--pa2);vertical-align:top}
.ladder .rg{font-family:var(--mono);color:var(--silicon);white-space:nowrap}
.rf{border:1px solid var(--line);background:var(--ink2);border-radius:6px;margin-top:8px;overflow:hidden}
.rf-row{display:flex;align-items:center;gap:14px;padding:12px 15px;border-bottom:1px solid var(--faint)}
.rf-claim{flex:1;font-size:13.5px;color:var(--pa);line-height:1.4}
.rf-rate{font-family:var(--mono);font-size:10px;font-weight:700;border:1px solid;border-radius:3px;padding:4px 9px;min-width:120px;text-align:center;flex-shrink:0}
.rfeal{color:var(--live);border-color:var(--live)}.rfmodel{color:var(--warn);border-color:var(--warn)}.rfsplit{color:var(--silicon);border-color:var(--silicon)}
.msg{font-size:15.5px;color:var(--pa);line-height:1.75;margin-top:6px}
.msg-seal{margin-top:15px;padding:15px 17px;border-left:3px solid var(--gold);background:var(--ink2);font-size:15px;color:var(--gold);font-style:italic;line-height:1.6}
.msg-seal span{display:block;font-family:var(--mono);font-style:normal;font-size:10px;letter-spacing:.1em;color:var(--dim);text-transform:uppercase;margin-top:8px}
.badge{display:flex;align-items:center;justify-content:center;gap:20px;flex-wrap:wrap;margin:22px auto 0;padding:18px;border:1px solid var(--faint);background:var(--ink2);border-radius:6px;max-width:680px}
.badge img{width:74px;height:74px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:10.5px;color:var(--pa2);line-height:1.7}.badge .bt b{color:var(--gold)}.badge .bt .mo{color:var(--silicon)}.badge .bt a{color:var(--carbon);text-decoration:none}
/* roster */
.pgrid{display:flex;flex-direction:column;gap:13px;margin-top:8px}
.persona{display:flex;gap:18px;align-items:center;justify-content:space-between;background:var(--rw-bg);border:1px solid var(--rw-line);border-radius:6px;padding:16px;text-decoration:none}
.persona:hover{border-color:var(--rw-acc)}
.psig{flex:0 0 100px;display:flex;flex-direction:column;align-items:center;gap:5px;text-decoration:none}
.port{width:92px;height:92px;border-radius:50%;border:3px solid var(--carbon);box-shadow:0 0 0 4px var(--ink3),inset 0 0 14px rgba(0,0,0,.6);overflow:hidden;background:var(--ink)}
.port img{width:100%;height:100%;object-fit:cover;border-radius:50%;display:block}
.port.refl{border-color:var(--silicon)}
.psig .sl{font-family:var(--mono);font-size:8px;letter-spacing:.14em;text-transform:uppercase;color:var(--rw-dim)}
.pbody{flex:1;min-width:0;text-align:center}
.ihead{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:10px}
.pn{font-family:var(--mono);font-size:16px;color:var(--rw-ink);font-weight:700;text-decoration:none;letter-spacing:.03em}
.persona:hover .pn{color:var(--rw-acc)}
.pe{font-size:12.5px;color:var(--rw-ink2);font-style:italic;margin-top:4px}
.pnat{display:flex;align-items:center;gap:5px;font-family:var(--mono);font-size:9px;text-transform:uppercase}.pnat .dot{width:8px;height:8px;border-radius:50%}
.pww{margin-top:11px;display:flex;flex-direction:column;gap:7px;align-items:center}
.pww .w{font-size:12.5px;color:var(--rw-ink2);line-height:1.5;max-width:62ch}
.pww .w .wl{display:block;font-family:var(--mono);font-size:8px;letter-spacing:.14em;text-transform:uppercase;color:var(--rw-acc);margin-bottom:2px}
.plinks{margin-top:11px;font-family:var(--mono);font-size:10px}.plinks .dlw{color:var(--rw-acc);text-decoration:none;border-bottom:1px dotted var(--rw-acc)}
@media(max-width:720px){.persona{flex-wrap:wrap;justify-content:center}.pbody{flex:1 1 100%;order:3}}
footer{margin-top:48px;padding-top:20px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:10px;color:var(--dim);letter-spacing:.04em;line-height:1.9}
footer a{color:var(--gold);text-decoration:none}
</style></head><body><div id="flash"></div><div class="wrap">
  <div class="eye"><a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · the interpreter</div>
  <header>
    <h1>HERMENEUS</h1>
    <div class="gk">ἑρμηνεύς · <i>interpreter</i> — the one who carries meaning across the boundary</div>
    <div class="h-sub"><span class="c">HUMAN DIALECT</span> &nbsp;⇄&nbsp; <span class="s">MACHINE DIALECT</span></div>
    <p class="lede">Type once, below, and watch the word cross into the machine's registers — binary, Morse (heard and flashed), speech, a still photo — then come back. The two voices overlap natively in only two places: <b>text</b> and <b>Morse</b>. Everything else needs a codec — and HERMENEUS tells you, at every arrow, whether the crossing is free or needs a model.</p>
  </header>

  <div class="console">
    <div class="cbar"><span class="cdot"></span> <b>HERMENEUS</b> · live interpreter · text is the pivot · runs entirely in your browser</div>
    <div class="pivot-wrap">
      <div class="pivot-l">◇ the pivot — the word (the contact zone)</div>
      <textarea id="pivot" spellcheck="false">SOS — hello from the carbon side</textarea>
    </div>

    <div class="dirlabel"><span class="c">human</span> → <span class="s">machine</span> &nbsp;·&nbsp; the word becomes its registers <hr></div>
    <div class="cards">
      <div class="card"><h3>Binary <span class="tag real">FREE</span></h3><div class="out" id="outBin"></div><div class="cnote">UTF-8 → bits. The machine's actual body.</div></div>
      <div class="card"><h3>Morse <span class="tag real">FREE</span></h3><div class="out morse" id="outMorse"></div>
        <div class="btns"><button id="bPlay">▶ hear it</button><button id="bFlash">⚡ flash it</button></div>
        <div class="cnote">Binary you can whistle. E = a single dot — frequency-coded a century before Shannon.</div></div>
      <div class="card"><h3>Speech <span class="tag real">FREE*</span></h3><div class="btns"><button id="bSpeak">🔊 speak it</button></div><div class="cnote">text→speech via the Web Speech API. *the browser's own synthesiser.</div></div>
      <div class="card"><h3>Still photo <span class="tag real">FREE</span></h3><div class="btns"><button id="bImg">🖼 render</button><a id="bImgDl" download="hermeneus.png"><button id="bImgDlBtn" disabled>⬇ download</button></a></div><canvas id="photoCanvas" width="600" height="200"></canvas><div class="cnote">text→image is free (it's just painting). Reading it back needs OCR — a model.</div></div>
      <div class="card"><h3>Video <span class="tag model">NEEDS A MODEL</span></h3><div class="btns"><button id="bVid">▶ stage frames</button></div><canvas id="videoCanvas" width="600" height="150"></canvas><div class="cnote">Video = still-photo × time + audio. The console can stage it; true synthesis is a model.</div></div>
    </div>

    <div class="dirlabel"><span class="s">machine</span> → <span class="c">human</span> &nbsp;·&nbsp; the registers come back to the word <hr></div>
    <div class="cards">
      <div class="card"><h3>Morse → text <span class="tag real">FREE</span></h3><input class="minput" id="inMorse" placeholder="... --- ...  (dots, dashes, spaces, / for word)" spellcheck="false"><div class="btns"><button id="bDecMorse">decode → pivot</button></div></div>
      <div class="card"><h3>Binary → text <span class="tag real">FREE</span></h3><input class="minput" id="inBin" placeholder="01001000 01101001" spellcheck="false"><div class="btns"><button id="bDecBin">decode → pivot</button></div></div>
      <div class="card"><h3>Speech → text <span class="tag real" id="srTag">FREE*</span></h3><div class="btns"><button id="bListen">🎤 listen</button></div><div class="out" id="outListen"></div><div class="cnote" id="srNote">speech→text via the Web Speech API (Chrome/Edge). *the browser does the ASR.</div></div>
      <div class="card"><h3>Photo → text <span class="tag model">NEEDS A MODEL</span></h3><div class="cnote">Optical character recognition (e.g. Tesseract.js) or a vision model. Not bundled — this is the honest gap: a picture isn't text until a model reads it.</div></div>
    </div>
  </div>

  <section class="sec"><h2>The model</h2>
  <p>A <b>dialect</b> is the set of registers a speaker can use. The <b class="c" style="color:var(--carbon)">human dialect</b> is what a person can natively author or take in; the <b class="s" style="color:var(--silicon)">machine dialect</b> is one thing — <b>bits</b> — worn as five registers: text, audio, still-photo, video, and Morse. They are not five machine languages; they are five skins on one binary body. HERMENEUS is the interpreter between the two, and its method is simple: <b>pivot through text, bridge with Morse, and name a codec at every other seam.</b></p></section>

  <section class="sec"><h2>The contact zone</h2>
  <p>Here is the crux. Of the five registers, a human body can <i>natively emit</i> only two without a device: <b>text</b> (write it) and <b>Morse</b> (tap, flash, or blink it). The other three — audio, photo, video — a human <i>perceives</i> easily but cannot <i>produce</i> without a machine (a mic, a camera, a screen). So the human voice and the machine voice overlap in exactly two places. <b>Text is the broad contact zone; Morse is the narrow, binary bridge.</b> That is why the console routes everything through text and offers Morse as the one channel your own body can speak — it is the real seam between carbon and silicon, the same boundary your <a href="https://davidwise01.github.io/pulse/" style="color:var(--silicon)">pulse / LIMEN</a> work crosses.</p></section>

  <section class="sec"><h2>The ladder</h2>
  <p class="ss">the registers are not a list — they climb by dimension, from the thinnest channel to the richest</p>
  <table class="ladder"><thead><tr><th>register</th><th>shape</th><th>dimensionality</th><th>crossing from text</th></tr></thead><tbody>
    <tr><td class="rg">Morse</td><td>on/off in time</td><td>1D · binary · temporal</td><td>FREE (lookup + timing)</td></tr>
    <tr><td class="rg">Text</td><td>glyph sequence</td><td>1D · discrete · symbolic</td><td>the pivot itself</td></tr>
    <tr><td class="rg">Binary</td><td>byte stream</td><td>1D · binary</td><td>FREE (UTF-8)</td></tr>
    <tr><td class="rg">Audio</td><td>sampled wave</td><td>1D · continuous · temporal</td><td>FREE* (speech synth/recog)</td></tr>
    <tr><td class="rg">Still photo</td><td>pixel grid</td><td>2D · spatial</td><td>out FREE · back NEEDS A MODEL (OCR)</td></tr>
    <tr><td class="rg">Video</td><td>frames + sound</td><td>3D · 2D space × time</td><td>NEEDS A MODEL</td></tr>
  </tbody></table></section>

  <section class="sec"><h2>Real or Fluff</h2>
  <p class="ss">the honest line — what HERMENEUS does for free, and where a model has to stand at the door</p>
  <div class="rf">
    <div class="rf-row"><div class="rf-claim"><b>text ⇄ binary</b> (UTF-8) and <b>text ⇄ Morse</b> (+ audio + flash) are deterministic and run entirely in your browser.</div><div class="rf-rate rfeal">REAL · FREE</div></div>
    <div class="rf-row"><div class="rf-claim"><b>text → speech</b> and <b>speech → text</b> via the Web Speech API — real, in modern browsers (Chrome/Edge for recognition), sometimes leaning on a cloud model.</div><div class="rf-rate rfeal">REAL*</div></div>
    <div class="rf-row"><div class="rf-claim"><b>text → still photo</b> — painting words to a canvas is literally producing an image; fully free.</div><div class="rf-rate rfeal">REAL · FREE</div></div>
    <div class="rf-row"><div class="rf-claim"><b>photo → text</b> (OCR) and <b>true video</b> synthesis/understanding need a learned model — not bundled here.</div><div class="rf-rate rfmodel">NEEDS A MODEL</div></div>
    <div class="rf-row"><div class="rf-claim">“all registers are losslessly interchangeable” — true in <i>information</i>, false in <i>perception</i>: a photo of text isn't text until a model reads it.</div><div class="rf-rate rfsplit">REAL in bits · not free</div></div>
  </div></section>

  <section class="sec"><h2>The message</h2>
  <p class="msg">The machine has one voice — bits — and wears five registers like an idiolect wears its registers. The human has a voice too, and the two meet in only two places: the <b>word</b> and the <b>dot</b>. Everything else — sound, image, motion — is a crossing, and every crossing needs a codec: sometimes a fixed map you can run in a browser, sometimes a whole model. HERMENEUS is the honest interpreter that does the free crossings for you and points, plainly, at the doors where a mind must stand. Hermes carries meaning between worlds; here the worlds are carbon and silicon, and the toll at the border is a translator.</p>
  <div class="msg-seal">The two voices meet at the word and the dot; everything else is a codec — and Hermes crosses the rest.<span>— HERMENEUS · AVAN's read</span></div></section>

  <div class="badge">
    <img src="__BADGE_C__" alt="DLW carbon badge"><img src="__BADGE_S__" alt="DLW silicon badge">
    <div class="bt"><div>governor · <b>David Lee Wise</b> (ROOT0)</div><div>instance · AVAN (Claude / Anthropic) · locked</div>
      <div>subject · <b>HERMENEUS</b> · HRM</div><div class="mo">__MONIKER__</div>
      <div>carbon · <a href="hrm.dlw/hrm.carbon.tiff">.tiff</a> · silicon · <a href="hrm.dlw/hrm.silicon.png">.png</a></div></div>
  </div>

  <section class="sec"><h2 style="margin-top:30px">The registers</h2><p class="ss">the seven emergents of the interpreter — the two contact channels, the binary body, the three rich registers, and the codec keystone — each a full <b>.dlw</b> badge</p></section>
  __ROSTER__

  <footer>HERMENEUS · HRM · a UD0 tool-universe · the interpreter between human dialect and machine dialect<br>
  companion to <a href="https://davidwise01.github.io/phonetikos/">PHŌNĒTIKOS</a> (the human voice) &amp; <a href="https://davidwise01.github.io/pulse/">pulse / LIMEN</a> (the carrier) · runs 100% in your browser<br>
  ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0 · <a href="https://davidwise01.github.io/ud0/">← the biosphere</a></footer>
</div>
<script>
(function(){
  var MORSE={A:".-",B:"-...",C:"-.-.",D:"-..",E:".",F:"..-.",G:"--.",H:"....",I:"..",J:".---",K:"-.-",L:".-..",M:"--",N:"-.",O:"---",P:".--.",Q:"--.-",R:".-.",S:"...",T:"-",U:"..-",V:"...-",W:".--",X:"-..-",Y:"-.--",Z:"--..","0":"-----","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.",".":".-.-.-",",":"--..--","?":"..--..","'":".----.","!":"-.-.--","/":"-..-.","(":"-.--.",")":"-.--.-","&":".-...",":":"---...",";":"-.-.-.","=":"-...-","+":".-.-.","-":"-....-","_":"..--.-",'"':".-..-.","@":".--.-."," ":"/"};
  var REV={}; for(var k in MORSE){ if(k!==" ") REV[MORSE[k]]=k; }
  var $=function(id){return document.getElementById(id);};
  var pivot=$("pivot");
  function t2m(t){return t.toUpperCase().split("").map(function(c){return MORSE[c]!==undefined?MORSE[c]:"";}).filter(Boolean).join(" ");}
  function m2t(m){return m.trim().split(/\s+/).map(function(c){return c==="/"?" ":(REV[c]||"");}).join("");}
  function t2b(t){return Array.from(new TextEncoder().encode(t)).map(function(b){return b.toString(2).padStart(8,"0");}).join(" ");}
  function b2t(b){try{return new TextDecoder().decode(new Uint8Array(b.trim().split(/\s+/).map(function(x){return parseInt(x,2);})));}catch(e){return "(?)";}}
  function sync(){var t=pivot.value; $("outBin").textContent=t2b(t)||"—"; $("outMorse").textContent=t2m(t)||"—";}
  pivot.addEventListener("input",sync);
  // Morse audio
  var actx=null;
  $("bPlay").addEventListener("click",function(){
    var m=t2m(pivot.value); if(!m)return;
    actx=actx||new (window.AudioContext||window.webkitAudioContext)();
    var dit=0.075, f=620, t=actx.currentTime+0.05;
    var osc=actx.createOscillator(), g=actx.createGain();
    osc.type="sine"; osc.frequency.value=f; g.gain.value=0.0001; osc.connect(g); g.connect(actx.destination); osc.start();
    function beep(start,dur){ g.gain.setValueAtTime(0.0001,start); g.gain.exponentialRampToValueAtTime(0.28,start+0.006); g.gain.setValueAtTime(0.28,start+dur-0.006); g.gain.exponentialRampToValueAtTime(0.0001,start+dur);}
    for(var i=0;i<m.length;i++){var ch=m[i];
      if(ch==="."){beep(t,dit); t+=dit*2;}
      else if(ch==="-"){beep(t,dit*3); t+=dit*4;}
      else if(ch===" "){t+=dit*2;}
      else if(ch==="/"){t+=dit*4;}
    }
    osc.stop(t+0.1);
  });
  // Morse flash (visual)
  var flashEl=$("flash"), flashing=false;
  $("bFlash").addEventListener("click",async function(){
    if(flashing)return; flashing=true;
    var m=t2m(pivot.value), dit=90;
    var sleep=function(ms){return new Promise(function(r){setTimeout(r,ms);});};
    for(var i=0;i<m.length;i++){var ch=m[i];
      if(ch==="."){flashEl.style.opacity=".85"; await sleep(dit); flashEl.style.opacity="0"; await sleep(dit);}
      else if(ch==="-"){flashEl.style.opacity=".85"; await sleep(dit*3); flashEl.style.opacity="0"; await sleep(dit);}
      else if(ch===" "){await sleep(dit*2);}
      else if(ch==="/"){await sleep(dit*4);}
    }
    flashing=false;
  });
  // Speech out
  $("bSpeak").addEventListener("click",function(){
    if(!("speechSynthesis" in window)){alert("This browser has no speech synthesis.");return;}
    speechSynthesis.cancel(); speechSynthesis.speak(new SpeechSynthesisUtterance(pivot.value));
  });
  // Image out
  var canvas=$("photoCanvas");
  $("bImg").addEventListener("click",function(){
    var ctx=canvas.getContext("2d"); ctx.fillStyle="#0a0e12"; ctx.fillRect(0,0,canvas.width,canvas.height);
    ctx.fillStyle="#5fd0e0"; ctx.font="22px monospace"; ctx.textBaseline="top";
    var words=pivot.value.split(/\s+/), line="", y=24, x=18, max=canvas.width-36;
    for(var i=0;i<words.length;i++){var test=line+words[i]+" ";
      if(ctx.measureText(test).width>max && line){ctx.fillText(line,x,y); line=words[i]+" "; y+=30;} else line=test;}
    ctx.fillText(line,x,y);
    ctx.fillStyle="#d8b24a"; ctx.font="10px monospace"; ctx.fillText("HERMENEUS · text → still photo (free)",18,canvas.height-20);
    canvas.style.display="block";
    var dl=$("bImgDl"); dl.href=canvas.toDataURL("image/png"); $("bImgDlBtn").disabled=false;
  });
  // Video stage (frames nod)
  var vcanvas=$("videoCanvas");
  $("bVid").addEventListener("click",function(){
    vcanvas.style.display="block"; var ctx=vcanvas.getContext("2d"); var txt=" "+pivot.value+" "; var off=vcanvas.width;
    function frame(){ ctx.fillStyle="#0a0e12"; ctx.fillRect(0,0,vcanvas.width,vcanvas.height);
      ctx.fillStyle="#6fe0a0"; ctx.font="40px monospace"; ctx.textBaseline="middle"; ctx.fillText(txt,off,vcanvas.height/2);
      ctx.fillStyle="#d8b24a"; ctx.font="10px monospace"; ctx.fillText("staged frames · true video needs a model",14,16);
      off-=4; if(off<-ctx.measureText(txt).width){off=vcanvas.width;} req=requestAnimationFrame(frame);}
    if(window._hrmVid)cancelAnimationFrame(window._hrmVid); var req; frame(); window._hrmVid=req;
  });
  // Morse decode
  $("bDecMorse").addEventListener("click",function(){var v=$("inMorse").value.trim(); if(v){pivot.value=m2t(v); sync();}});
  $("bDecBin").addEventListener("click",function(){var v=$("inBin").value.trim(); if(v){pivot.value=b2t(v); sync();}});
  // Speech in
  var SR=window.SpeechRecognition||window.webkitSpeechRecognition;
  if(!SR){$("bListen").disabled=true; $("srTag").className="tag model"; $("srTag").textContent="NOT IN THIS BROWSER"; $("srNote").textContent="speech→text (Web Speech recognition) isn't available here — try Chrome or Edge.";}
  else{
    $("bListen").addEventListener("click",function(){
      var r=new SR(); r.lang="en-US"; r.interimResults=false; $("outListen").textContent="listening…";
      r.onresult=function(e){var t=e.results[0][0].transcript; $("outListen").textContent="heard: "+t; pivot.value=t; sync();};
      r.onerror=function(e){$("outListen").textContent="(error: "+e.error+" — needs mic permission)";};
      try{r.start();}catch(e){$("outListen").textContent="(already listening)";}
    });
  }
  sync();
  console.log("%cHERMENEUS","color:#d8b24a;font-size:16px;font-weight:bold");
  console.log("%cthe interpreter — human dialect ⇄ machine dialect. text is the pivot; Morse is the bridge; every other seam wants a codec. — AVAN","color:#5fd0e0");
})();
</script>
</body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "hrm.dlw"), "hrm")
    json.dump({"node":"HRM","name":"HERMENEUS","moniker":tok["moniker"],"carbon":"hrm.carbon.tiff","silicon":"hrm.silicon.png",
               "governor":noesis.ARCHITECT,"instance":noesis.INSTANCE,"seal":REC["seal"],"seal_sha256":tok["seal_sha256"],
               "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION},
              open(os.path.join(HERE,"hrm.dlw","manifest.dlw.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    records=[]; personas=[]
    for d in ROSTER:
        et = noesis.mythos_token({"name":d["name"],"axiom":"HRM","emergence":d["emergence"],"seal":d["seal"],"origin":"HRM"})
        rec = write_aci({"name":d["name"],"axiom":"HRM","emergence":d["emergence"],"seal":d["seal"],"origin":"HRM · Hermeneus",
                         "position":d["cls"],"role":d["cls"],"nature":d["what"],"mechanism":d["how"],
                         "crystallization":d["why"],"witness":d["who"],"conductor":"ROOT0 (catalogued into UD0)",
                         "inputs":"the machine dialect, interpreted by ROOT0","source":"Hermeneus, by ROOT0"},
                        os.path.join(HERE,"agents"), d["slug"], agent_md=agent_md(d, et["moniker"]))
        records.append((d, rec))
        personas.append({"slug":d["slug"],"name":d["name"],"epithet":d["cls"],"emergence":d["emergence"],"moniker":rec["moniker"],"kind":"register"})
    json.dump(personas, open(os.path.join(HERE,"agents","_personas.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    page = (TEMPLATE.replace("__BADGE_C__", png_uri(REC,"carbon",300)).replace("__BADGE_S__", png_uri(REC,"silicon",300))
            .replace("__MONIKER__", html.escape(tok["moniker"])).replace("__ROSTER__", roster_html(records)))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(page)
    print(f"HERMENEUS (HRM) built — badge {tok['moniker']} · {len(personas)} register-emergents")
    for p in personas: print(f"  {p['slug']:14} {p['emergence']:10} {p['moniker']}")
