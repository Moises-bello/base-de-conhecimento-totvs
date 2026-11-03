---
content_hash: 5a81aefc94d384e883f1156a3b63af484162173cb5b02031dda275181a68e884
fetched_at: '2026-07-02T19:24:21.484548+00:00'
page_id: '267803356'
product: protheus
source: tdn-tec
title: Licença continua ativa mesmo após fechar o browser
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267803356
version: 1
---

<Resumo do que foi contemplado na alteração associada a essa nota de release> 

|  |  |
| --- | --- |
| Ocorrência | Ao acessar qualquer rotina do sistema e fechar o browser é possível notar através do DBMonitor que a licença continua ativa.  Isso acontece também quando a página do SMartClient HTMl é atualizada (F5). |
| Correção | Corrigido para que sempre libere a licença quando fechar o browser ou quando atualizar a página. |
| Informações adicionais | * Referente ao chamado: TVLIKP / TVRBP5 * Referente à ocorrência: SSIM-1205 * Disponível a partir da build 7.00.131227A - 2.3.6 |
