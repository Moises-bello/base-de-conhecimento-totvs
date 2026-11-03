---
content_hash: a71b48a1410521343ed5e978ec8fdf01ee795b156f00c6fafdafa9607f34d42f
fetched_at: '2026-07-02T19:24:18.864654+00:00'
page_id: '221551824'
product: protheus
source: tdn-tec
title: Lentidão na navegação dos itens do Browse usando SmartClient HTML em tablet
  (Android / IOS)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=221551824
version: 1
---

<Resumo do que foi contemplado na alteração associada a essa nota de release> 

|  |  |
| --- | --- |
| Situação | Lentidão na navegação dos itens do Browse usando SmartClient HTML em tablet (Android / IOS) |
| Ocorrência | Ao navegar para cima ou para baixo, demorava ate 2 segundos para repintar o Browse. |
| Correção | Na TCBrowse: - Implementada MS\_TCBROWSEDOSCROLL - Não limpar sempre a tcbrowse e sim verifica se a linha já existe e atualizar seus valores. - Atualizar a altura de linha para o calculo ao receber CSS.  Na TGetDados:  - Correcoes de celula selecionada se perdendo.  Na TGrid:  - Atualizar a altura de linha para o calculo ao receber CSS. |
| Informações adicionais | * Referente ao chamado: TTBRH5 * Referente à ocorrência: SSIM-211 * Disponível em builds superiores a  7.00.131227A - 3.0.11 |
