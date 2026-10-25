# Builds index.html (the home-screen app) from app.html (the same page the claude.ai preview shows).
import pathlib

d = pathlib.Path(__file__).parent
head, body = (d / 'app.html').read_text().split('</style>', 1)
(d / 'index.html').write_text(f'''<!doctype html>
<html lang="lt">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Vizitavimas">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="theme-color" content="#F2F2F7" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#000000" media="(prefers-color-scheme: dark)">
<link rel="apple-touch-icon" href="icon-180.png">
<link rel="manifest" href="manifest.webmanifest">
<style>:root{{color-scheme:light;padding-top:env(safe-area-inset-top);padding-bottom:env(safe-area-inset-bottom)}}img{{max-width:100%}}</style>
{head}</style>
</head>
<body>{body}</body>
</html>
''')
