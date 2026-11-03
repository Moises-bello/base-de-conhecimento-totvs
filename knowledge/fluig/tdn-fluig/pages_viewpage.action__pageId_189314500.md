---
content_hash: e964473aabb57f998da2dfae8d72a9379775b922d72511c619fa3f3d4ffe1489
fetched_at: '2026-06-28T21:35:19.079135+00:00'
page_id: '189314500'
product: fluig
source: tdn-fluig
title: BPM 103 - Problema na Configuração de Processos no Chrome com Windows 8 e telas
  não-sensíveis ao toque
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=189314500
version: 5
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**Fluig

# Ocorrência

Tela de Configuração de Processos não funciona corretamente com Google Chrome no Windows 8 em computadores que **não possuem** touchscreen (telas sensíveis).

# Causa

Por padrão, o modo touchscreen do Chrome é configurado para "Automático". Porém, em computadores com Windows 8 que não possuem touchscreen, esta configuração pode interferir no funcionamento da tela de Configuração de Processos.

# Solução

- Digite na barra de endereços do Chrome > chrome://flags/#touch-events.

- Altere a opção "Ativar eventos de toque" para Desativado.

- Reinicie o Chrome.

# Observações

Lembrando que na  é informado que computadores que **possuam telas sensíveis ao toque** e rodam Windows 8 **não são compatíveis** com Google Chrome.
