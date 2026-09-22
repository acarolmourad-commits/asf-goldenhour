# -*- coding: utf-8 -*-
"""ASF SEO fix: substitui o H1 dinamico (contagem regressiva) por <div>, preservando id/JS. Idempotente."""
p = 'index.html'
s = open(p, encoding='utf-8').read()
old = '<h1 id="cd" style="color:var(--rosa);font-size:2.2rem"></h1>'
new = '<div id="cd" style="color:var(--rosa);font-size:2.2rem;font-weight:bold"></div>'
if old in s:
    open(p, 'w', encoding='utf-8').write(s.replace(old, new))
    print('H1 dinamico corrigido')
else:
    print('Nada a corrigir.')