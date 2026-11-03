---
content_hash: 96d12844447041b315d7289292801e4480dc506df81e1ad20566e27dfbca31f5
fetched_at: '2026-06-29T00:05:52.135339+00:00'
page_id: '1056934994'
product: rm
source: tdn-rm
title: Deduções legais da base de cálculo (TPF)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1056934994
version: 2
---

### Voltar para [Layout único de integração da NFS-e com o TPF](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143731)

| Nome | Pai | Tipo Elemento | Ocorrência | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| deducoes | **[rps](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143860)** | G | 0-1 | Tag raiz que agrupará as deduções do documento. |  |  |
| desccond | deducoes | E | 1-1 | Valor do desconto condicional do documento. | TMOV.VALORDESCCONDICIONAL |  |
| descincond | deducoes | E | 1-1 | Valor do desconto incondicional do documento. | TMOV.VALORDESC |  |
| deducao | deducoes | G | 0-N | Tag raiz que conterá as informações sobre uma dedução do documento. |  | Será gerado se o tipo de Movimento estiver parametrizado para utilizar Dedução por item e se o valor estiver preenchido no movimento ou se percentual estiver preenchido no item de movimento |
| totalnf | deducao | E | 1-1 | Valor total da nota fiscal de referência. |  | Não será gerado |

Campo Dedução por Material ou Sub Empreitada
