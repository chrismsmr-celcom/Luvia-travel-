from pathlib import Path
import base64, html

logo_path = Path("/mnt/data/EB16F50A-0BAF-4C76-98AB-7034BBF34CBC.png")
photo_path = Path("/mnt/data/E1BE32E3-29DF-416F-BBF5-359D3A6EF298.jpeg")

logo_b64 = base64.b64encode(logo_path.read_bytes()).decode()
photo_b64 = base64.b64encode(photo_path.read_bytes()).decode()

page = r'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#111111">
  <meta name="description" content="Luvia Travel LLC — making travel more accessible and affordable, everywhere in the world.">
  <title>Luvia Travel LLC — Travel without barriers</title>

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@600;700;800&display=swap" rel="stylesheet">

  <style>
    :root{
      --ink:#101010;
      --muted:#686868;
      --paper:#f7f7f4;
      --white:#fff;
      --line:rgba(16,16,16,.10);
      --accent:#d9252a;
      --accent-dark:#b91f24;
      --radius:28px;
      --shadow:0 20px 70px rgba(0,0,0,.10);
    }
    *{box-sizing:border-box}
    html{scroll-behavior:smooth}
    body{
      margin:0;
      color:var(--ink);
      background:var(--paper);
      font-family:"DM Sans",system-ui,sans-serif;
      overflow-x:hidden;
    }
    a{color:inherit;text-decoration:none}
    img{display:block;max-width:100%}
    .wrap{width:min(1180px,calc(100% - 40px));margin:auto}
    .nav{
      position:fixed;z-index:50;top:18px;left:50%;transform:translateX(-50%);
      width:min(1040px,calc(100% - 28px));
      display:flex;align-items:center;justify-content:space-between;
      padding:9px 10px 9px 15px;
      border:1px solid rgba(255,255,255,.62);
      background:rgba(255,255,255,.72);
      backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);
      box-shadow:0 10px 35px rgba(0,0,0,.08);
      border-radius:999px;
      transition:.35s ease;
    }
    .nav.scrolled{background:rgba(255,255,255,.90);box-shadow:0 15px 45px rgba(0,0,0,.12)}
    .brand img{width:112px;height:auto}
    .links{display:flex;gap:28px;align-items:center;font-size:13px;font-weight:600}
    .links a{opacity:.72;transition:.2s}
    .links a:hover{opacity:1}
    .nav-cta{
      padding:12px 17px;border-radius:999px;background:var(--ink);color:#fff;
      font-size:13px;font-weight:700;transition:.25s;
    }
    .nav-cta:hover{transform:translateY(-2px);background:#272727}
    .menu{display:none;border:0;background:#111;color:#fff;width:42px;height:42px;border-radius:50%;font-size:19px}
    .mobile-panel{
      display:none;position:fixed;z-index:49;top:72px;left:14px;right:14px;
      padding:16px;background:rgba(255,255,255,.94);backdrop-filter:blur(18px);
      border:1px solid var(--line);border-radius:24px;box-shadow:var(--shadow)
    }
    .mobile-panel.open{display:grid}
    .mobile-panel a{padding:13px 10px;border-bottom:1px solid var(--line);font-weight:600}
    .mobile-panel a:last-child{border:0}

    .hero{position:relative;min-height:900px;padding:175px 0 80px;overflow:hidden;background:#fff}
    .hero:before{
      content:"";position:absolute;width:700px;height:700px;border-radius:50%;
      right:-270px;top:-300px;background:radial-gradient(circle,rgba(217,37,42,.14),transparent 65%);
      pointer-events:none;
    }
    .hero-grid{display:grid;grid-template-columns:1.02fr .98fr;gap:55px;align-items:center}
    .eyebrow{
      display:inline-flex;align-items:center;gap:8px;font-size:11px;font-weight:800;
      letter-spacing:.13em;text-transform:uppercase;color:var(--accent);margin-bottom:20px;
    }
    .dot{width:7px;height:7px;background:var(--accent);border-radius:50%;box-shadow:0 0 0 7px rgba(217,37,42,.10)}
    h1{
      margin:0;font-family:"Manrope",sans-serif;font-size:clamp(52px,7vw,92px);
      line-height:.93;letter-spacing:-.065em;max-width:760px;
    }
    h1 em{font-style:normal;color:var(--accent)}
    .hero-copy{
      max-width:575px;margin:28px 0 31px;color:#5e5e5e;font-size:18px;line-height:1.65
    }
    .actions{display:flex;gap:12px;align-items:center;flex-wrap:wrap}
    .btn{
      display:inline-flex;align-items:center;justify-content:center;gap:9px;
      min-height:52px;padding:0 20px;border-radius:999px;font-size:14px;font-weight:700;
      transition:.25s;
    }
    .btn-primary{background:var(--accent);color:#fff;box-shadow:0 12px 30px rgba(217,37,42,.22)}
    .btn-primary:hover{background:var(--accent-dark);transform:translateY(-3px)}
    .btn-secondary{background:#f1f1ef;border:1px solid var(--line)}
    .btn-secondary:hover{background:#e9e9e6;transform:translateY(-3px)}
    .proof{display:flex;gap:26px;margin-top:34px;align-items:center}
    .proof-item{font-size:12px;color:#777}
    .proof-item strong{display:block;color:#111;font-size:15px;margin-bottom:3px}
    .hero-art{position:relative;height:600px}
    .hero-card{
      position:absolute;inset:20px 0 20px 30px;border-radius:42px;overflow:hidden;
      background:#ddd;box-shadow:var(--shadow);transform:rotate(2.2deg)
    }
    .hero-card img{width:100%;height:100%;object-fit:cover}
    .hero-card:after{
      content:"";position:absolute;inset:0;
      background:linear-gradient(180deg,rgba(0,0,0,.02),rgba(0,0,0,.28));
    }
    .float-card{
      position:absolute;z-index:2;left:-2px;bottom:48px;background:rgba(255,255,255,.90);
      backdrop-filter:blur(16px);padding:16px 18px;border-radius:20px;
      box-shadow:0 18px 50px rgba(0,0,0,.15);display:flex;gap:12px;align-items:center;
      animation:float 4s ease-in-out infinite;
    }
    .float-icon{width:42px;height:42px;border-radius:14px;background:#111;color:#fff;display:grid;place-items:center;font-size:19px}
    .float-card strong{font-size:13px}.float-card span{display:block;color:#777;font-size:11px;margin-top:2px}
    @keyframes float{50%{transform:translateY(-9px)}}
    .scroll-note{position:absolute;bottom:25px;left:50%;transform:translateX(-50%);font-size:10px;letter-spacing:.15em;text-transform:uppercase;color:#999}

    .marquee-section{padding:80px 0 105px;background:var(--paper);overflow:hidden}
    .section-head{display:flex;justify-content:space-between;gap:30px;align-items:end;margin-bottom:30px}
    .kicker{font-size:11px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:#999}
    h2{font-family:"Manrope";font-size:clamp(34px,4.5vw,58px);line-height:1;letter-spacing:-.055em;margin:10px 0 0;max-width:700px}
    .section-head p{max-width:350px;color:#777;line-height:1.6;font-size:14px}
    .rail{display:flex;width:max-content;animation:rail 42s linear infinite}
    .rail.reverse{animation:railReverse 48s linear infinite}
    .rail:hover{animation-play-state:paused}
    .photo{width:310px;height:390px;margin-right:16px;border-radius:28px;overflow:hidden;position:relative;flex:none}
    .photo.wide{width:430px}
    .photo img{width:100%;height:100%;object-fit:cover;transition:transform .8s}
    .photo:hover img{transform:scale(1.06)}
    .photo span{
      position:absolute;left:15px;bottom:15px;padding:8px 11px;border-radius:999px;
      background:rgba(0,0,0,.55);backdrop-filter:blur(10px);color:#fff;font-size:11px
    }
    @keyframes rail{to{transform:translateX(-50%)}}
    @keyframes railReverse{to{transform:translateX(0)}}

    .mission{background:#111;color:#fff;padding:120px 0}
    .mission-grid{display:grid;grid-template-columns:.85fr 1.15fr;gap:80px}
    .mission .kicker{color:#aaa}
    .mission h2{font-size:clamp(42px,5.5vw,72px)}
    .mission-copy{font-size:21px;line-height:1.65;color:#c7c7c7;margin:0 0 34px}
    .redline{width:100%;height:1px;background:rgba(255,255,255,.15);margin:35px 0}
    .principles{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
    .principle{padding-top:20px;border-top:1px solid rgba(255,255,255,.22)}
    .principle b{display:block;font-size:15px;margin-bottom:8px}.principle p{margin:0;color:#8f8f8f;font-size:13px;line-height:1.6}

    .leadership{padding:120px 0;background:#fff}
    .leader-grid{display:grid;grid-template-columns:.85fr 1.15fr;gap:90px;align-items:center}
    .portrait{height:650px;border-radius:35px;overflow:hidden;background:#eee;position:relative}
    .portrait img{width:100%;height:100%;object-fit:cover;object-position:center top}
    .portrait-tag{position:absolute;left:18px;bottom:18px;padding:11px 14px;border-radius:999px;background:rgba(255,255,255,.86);backdrop-filter:blur(12px);font-size:11px;font-weight:700}
    .leader-copy h2{font-size:clamp(42px,5vw,68px)}
    .leader-copy .role{color:var(--accent);font-weight:800;font-size:12px;letter-spacing:.12em;text-transform:uppercase;margin:26px 0 17px}
    .leader-copy p{font-size:17px;line-height:1.75;color:#666;max-width:590px}
    .quote{margin-top:34px;padding:25px 0 0;border-top:1px solid var(--line);font-family:"Manrope";font-size:22px;line-height:1.4;letter-spacing:-.02em}

    .cta{padding:105px 0;background:var(--accent);color:#fff;text-align:center;position:relative;overflow:hidden}
    .cta:before,.cta:after{content:"";position:absolute;border:1px solid rgba(255,255,255,.17);border-radius:50%}
    .cta:before{width:580px;height:580px;left:-260px;top:-250px}.cta:after{width:430px;height:430px;right:-190px;bottom:-260px}
    .cta h2{margin:0 auto 22px;max-width:800px;font-size:clamp(45px,6vw,76px)}
    .cta p{color:rgba(255,255,255,.78);font-size:16px;margin:0 auto 30px;max-width:570px;line-height:1.6}
    .cta .btn-primary{background:#fff;color:#111;box-shadow:none}.cta .btn-primary:hover{background:#f1f1f1}
    .cta .btn-secondary{background:transparent;border-color:rgba(255,255,255,.4);color:#fff}

    footer{background:#0b0b0b;color:#fff;padding:42px 0}
    .footer-row{display:flex;justify-content:space-between;gap:30px;align-items:center}
    .footer-brand img{width:100px;filter:brightness(0) invert(1)}
    .footer-meta{color:#777;font-size:11px;line-height:1.7;text-align:right}
    .footer-meta a{color:#bbb}

    .reveal{opacity:0;transform:translateY(24px);transition:opacity .8s ease,transform .8s ease}
    .reveal.show{opacity:1;transform:none}
    @media(max-width:850px){
      .links,.nav-cta{display:none}.menu{display:block}
      .hero{padding-top:130px;min-height:auto}.hero-grid,.mission-grid,.leader-grid{grid-template-columns:1fr}
      .hero-art{height:470px;margin-top:35px}.hero-card{inset:0 5px 0 5px}.float-card{left:5px;bottom:25px}
      .section-head{display:block}.section-head p{margin-top:18px}
      .principles{grid-template-columns:1fr}.mission{padding:85px 0}.leadership{padding:85px 0}
      .portrait{height:520px}.leader-grid{gap:45px}.cta{padding:85px 0}
      .footer-row{align-items:flex-start;flex-direction:column}.footer-meta{text-align:left}
    }
    @media(max-width:520px){
      .wrap{width:min(100% - 28px,1180px)}.nav{top:10px}.brand img{width:98px}
      h1{font-size:52px}.hero-copy{font-size:16px}.hero-art{height:390px}
      .proof{gap:15px}.photo{width:250px;height:320px}.photo.wide{width:330px}
    }
    @media(prefers-reduced-motion:reduce){
      *,*:before,*:after{scroll-behavior:auto!important;animation:none!important;transition:none!important}
    }
  </style>
</head>

<body>
  <header class="nav" id="nav">
    <a class="brand" href="#top" aria-label="Luvia Travel home">
      <img src="data:image/png;base64,''' + logo_b64 + r'''" alt="Luvia Travel LLC">
    </a>
    <nav class="links">
      <a href="#mission">Mission</a>
      <a href="#leadership">Leadership</a>
      <a href="#world">The world</a>
    </nav>
    <a class="nav-cta" href="https://luviaplace.com" target="_blank" rel="noopener">Explore LuviaPlace ↗</a>
    <button class="menu" id="menuBtn" aria-label="Open menu">☰</button>
  </header>

  <div class="mobile-panel" id="mobilePanel">
    <a href="#mission">Mission</a>
    <a href="#leadership">Leadership</a>
    <a href="#world">The world</a>
    <a href="https://luviaplace.com" target="_blank" rel="noopener">Explore LuviaPlace ↗</a>
  </div>

  <main id="top">
    <section class="hero">
      <div class="wrap hero-grid">
        <div class="reveal">
          <div class="eyebrow"><span class="dot"></span> Luvia Travel LLC · Global travel</div>
          <h1>Travel should be <em>open</em> to everyone.</h1>
          <p class="hero-copy">
            Luvia Travel LLC is the parent company behind LuviaPlace.com.
            We build simpler, more accessible ways to discover and book travel —
            including for people who don't have a bank card.
          </p>
          <div class="actions">
            <a class="btn btn-primary" href="https://luviaplace.com" target="_blank" rel="noopener">Discover LuviaPlace <span>↗</span></a>
            <a class="btn btn-secondary" href="#mission">Our mission ↓</a>
          </div>
          <div class="proof">
            <div class="proof-item"><strong>Global</strong>Accessible worldwide</div>
            <div class="proof-item"><strong>Human-first</strong>Built around real constraints</div>
            <div class="proof-item"><strong>Affordable</strong>Focused on lower barriers</div>
          </div>
        </div>

        <div class="hero-art reveal">
          <div class="hero-card">
            <img src="https://images.unsplash.com/photo-1469474968028-56623f02e42e?auto=format&fit=crop&w=1300&q=88" alt="Mountain landscape">
          </div>
          <div class="float-card">
            <div class="float-icon">✦</div>
            <div><strong>One world. Fewer barriers.</strong><span>Travel, made more accessible.</span></div>
          </div>
        </div>
      </div>
      <div class="scroll-note">Scroll to explore · ↓</div>
    </section>

    <section class="marquee-section" id="world">
      <div class="wrap">
        <div class="section-head reveal">
          <div>
            <div class="kicker">01 · The world is the product</div>
            <h2>From Kinshasa to everywhere.</h2>
          </div>
          <p>We believe geography should inspire people — not become a barrier to access, discovery or booking.</p>
        </div>
      </div>

      <div class="rail" aria-hidden="true">
        <div class="photo"><img src="https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=900&q=82"><span>Explore</span></div>
        <div class="photo wide"><img src="https://images.unsplash.com/photo-1526772662000-3f88f10405ff?auto=format&fit=crop&w=1100&q=82"><span>Discover</span></div>
        <div class="photo"><img src="https://images.unsplash.com/photo-1530789253388-582c481c54b0?auto=format&fit=crop&w=900&q=82"><span>Move</span></div>
        <div class="photo wide"><img src="https://images.unsplash.com/photo-1488646953014-85cb44e25828?auto=format&fit=crop&w=1100&q=82"><span>Experience</span></div>
        <div class="photo"><img src="https://images.unsplash.com/photo-1469474968028-56623f02e42e?auto=format&fit=crop&w=900&q=82"><span>Escape</span></div>

        <div class="photo"><img src="https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=900&q=82"><span>Explore</span></div>
        <div class="photo wide"><img src="https://images.unsplash.com/photo-1526772662000-3f88f10405ff?auto=format&fit=crop&w=1100&q=82"><span>Discover</span></div>
        <div class="photo"><img src="https://images.unsplash.com/photo-1530789253388-582c481c54b0?auto=format&fit=crop&w=900&q=82"><span>Move</span></div>
        <div class="photo wide"><img src="https://images.unsplash.com/photo-1488646953014-85cb44e25828?auto=format&fit=crop&w=1100&q=82"><span>Experience</span></div>
        <div class="photo"><img src="https://images.unsplash.com/photo-1469474968028-56623f02e42e?auto=format&fit=crop&w=900&q=82"><span>Escape</span></div>
      </div>
    </section>

    <section class="mission" id="mission">
      <div class="wrap mission-grid">
        <div class="reveal">
          <div class="kicker">02 · Why we exist</div>
          <h2>Access first. Always.</h2>
        </div>
        <div class="reveal">
          <p class="mission-copy">
            For millions of travelers, the problem isn't the desire to travel.
            It's the barrier between them and the booking: cards, payment methods,
            complicated journeys and prices that don't fit.
          </p>
          <p class="mission-copy">
            Luvia Travel exists to reduce those barriers and make travel more
            reachable for Africans and for anyone underserved by traditional travel platforms.
          </p>
          <div class="redline"></div>
          <div class="principles">
            <div class="principle"><b>Accessible</b><p>Design around the traveler, not around a payment card.</p></div>
            <div class="principle"><b>Affordable</b><p>Search for better value and remove unnecessary friction.</p></div>
            <div class="principle"><b>Global</b><p>Built to serve travelers wherever they are in the world.</p></div>
          </div>
        </div>
      </div>
    </section>

    <section class="leadership" id="leadership">
      <div class="wrap leader-grid">
        <div class="portrait reveal">
          <img src="data:image/jpeg;base64,''' + photo_b64 + r'''" alt="Christopher Dikesa">
          <div class="portrait-tag">Founder · Luvia Travel LLC</div>
        </div>
        <div class="leader-copy reveal">
          <div class="kicker">03 · Leadership</div>
          <h2>Built from a simple observation.</h2>
          <div class="role">Christopher Dikesa · Founder</div>
          <p>
            Luvia Travel LLC was created by Christopher Dikesa with a clear idea:
            access to travel should not depend on where you live, which passport
            you hold, or whether you have a traditional bank card.
          </p>
          <p>
            The company is building the infrastructure and products around that
            belief, starting with <strong>LuviaPlace.com</strong>.
          </p>
          <div class="quote">“The goal isn't to make travel look easier. It's to actually make it easier to access.”</div>
        </div>
      </div>
    </section>

    <section class="cta">
      <div class="wrap reveal">
        <div class="kicker" style="color:rgba(255,255,255,.7)">04 · Start somewhere</div>
        <h2>The world is closer than you think.</h2>
        <p>Discover LuviaPlace and start planning your next stay, destination or journey.</p>
        <div class="actions" style="justify-content:center">
          <a class="btn btn-primary" href="https://luviaplace.com" target="_blank" rel="noopener">Visit LuviaPlace ↗</a>
          <a class="btn btn-secondary" href="#top">Back to top ↑</a>
        </div>
      </div>
    </section>
  </main>

  <footer>
    <div class="wrap footer-row">
      <a class="footer-brand" href="#top"><img src="data:image/png;base64,''' + logo_b64 + r'''" alt="Luvia Travel LLC"></a>
      <div class="footer-meta">
        © 2026 Luvia Travel LLC · Parent company of LuviaPlace.com<br>
        Founded by Christopher Dikesa · <a href="https://luviaplace.com" target="_blank" rel="noopener">luviaplace.com</a>
      </div>
    </div>
  </footer>

  <script>
    const nav = document.getElementById('nav');
    const menuBtn = document.getElementById('menuBtn');
    const mobilePanel = document.getElementById('mobilePanel');

    window.addEventListener('scroll', () => nav.classList.toggle('scrolled', window.scrollY > 30), {passive:true});

    menuBtn.addEventListener('click', () => mobilePanel.classList.toggle('open'));
    mobilePanel.querySelectorAll('a').forEach(a => a.addEventListener('click', () => mobilePanel.classList.remove('open')));

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if(entry.isIntersecting) {
          entry.target.classList.add('show');
          observer.unobserve(entry.target);
        }
      });
    }, {threshold:.12});

    document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
  </script>
</body>
</html>'''

out = Path("/mnt/data/luvia-travel-landing-page.html")
out.write_text(page, encoding="utf-8")
print(f"Landing page créée : {out}")
print(f"Taille : {out.stat().st_size / 1024:.1f} KB")
