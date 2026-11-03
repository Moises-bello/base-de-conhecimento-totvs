---
content_hash: edc41153eb7d79cb9dc186255ef36a7055d46e40ae9e57bfbf3e65ff5b7d02fe
fetched_at: '2026-07-02T19:24:19.679346+00:00'
page_id: '243650592'
product: protheus
source: tdn-tec
title: Correção - Sensação de travamento do sistema Totvs PDV devido a perda de foco
  dos componentes da tela
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243650592
version: 1
---

|  |  |
| --- | --- |
| Situação | Ao utilizar teclas de atalho no Totvs PDV ocorre "travamento" da interface do usuário |
| Ocorrência | Neste caso, ao utilizar teclas de atalho que removem um componente que está em foco, o Smartclient "trava" e impede a interação do usuário |
| Correção | As mensagens de tratamento de teclas de atalho agora são tratadas pela janela (Dialog) e não pelo componente em foco, para evitar esse tipo de situação. |
| Informações adicionais | * Referente ao chamado: TVIPRX * Referente à ocorrência: SSIM-1139 * Disponível em builds superiores a 131227A-20160714 |
