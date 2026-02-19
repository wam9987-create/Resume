from pathlib import Path
from datetime import datetime

# "어떤 폴더의 HTML들을 목록화할지" 설정
TARGET_DIR = Path(".")  # 너는 Resume/ 안에 index.html이 있으니까
OUTPUT = Path("contents.html")

def main():
    if not TARGET_DIR.exists():
        raise SystemExit(f"Target dir not found: {TARGET_DIR.resolve()}")

    html_files = sorted([p for p in TARGET_DIR.rglob("*.html") if p.is_file()])

    # 링크는 Pages 기준 상대경로로 생성 (contents.html이 루트에 있다고 가정)
    lines = []
    lines.append("<!doctype html>")
    lines.append("<html lang='ko'>")
    lines.append("<head>")
    lines.append("  <meta charset='utf-8'/>")
    lines.append("  <meta name='viewport' content='width=device-width, initial-scale=1'/>")
    lines.append("  <title>Contents</title>")
    lines.append("  <style>")
    lines.append("    body{font-family:system-ui,-apple-system,Segoe UI,Roboto,'Noto Sans KR',sans-serif;max-width:900px;margin:40px auto;padding:0 16px;line-height:1.6;}")
    lines.append("    h1{margin:0 0 10px 0;font-size:24px;}")
    lines.append("    .muted{color:#6b7280;font-size:13px;}")
    lines.append("    ul{padding-left:18px;}")
    lines.append("    a{text-decoration:none;border-bottom:1px solid rgba(0,0,0,0.12);color:#111;}")
    lines.append("    a:hover{border-bottom-color:rgba(0,0,0,0.3);}")
    lines.append("  </style>")
    lines.append("</head>")
    lines.append("<body>")
    lines.append("  <h1>Contents</h1>")
    lines.append(f"  <div class='muted'>Generated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}</div>")
    lines.append("  <ul>")

    if not html_files:
        lines.append("    <li>(No HTML files found.)</li>")
    else:
        for p in html_files:
            rel = p.as_posix()  # ex) Resume/index.html
            lines.append(f"    <li><a href='{rel}'>{rel}</a></li>")

    lines.append("  </ul>")
    lines.append("</body></html>")

    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"✅ Wrote {OUTPUT} with {len(html_files)} link(s).")

if __name__ == "__main__":
    main()

