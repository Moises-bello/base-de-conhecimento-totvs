---
content_hash: 070826504c1f2d39c75229e54b360d5294239eb42f741ae774f22d1815c1d4ae
fetched_at: '2026-07-02T19:24:25.010209+00:00'
page_id: '494976198'
product: protheus
source: tdn-tec
title: tMultiGet não respeita cores atribuídas ao componente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=494976198
version: 1
---

|  |  |
| --- | --- |
| Situação | Ao utilizat um tMultiGet, não é possível trocar a cor do texto ou de fundo do componente – é usado sempre preto sobre branco – mesmo especificando explicitamente os valores no construtor, ou usando  o método SetColor(). Somente foi possível trocar a cor de fundo usando um SetCSS() no componente, mas a cor de frente permanece sempre preta. |
| Correção | Correção para aplicação correta da cor do texto e do fundo do componente TMultiGet. |
| Informações adicionais | * Referente ao chamado:  Não há chamado associado * Referente à ocorrência: SCHTML-938 * Disponível a partir da build 7.00.131227A - 4.3.0 |
