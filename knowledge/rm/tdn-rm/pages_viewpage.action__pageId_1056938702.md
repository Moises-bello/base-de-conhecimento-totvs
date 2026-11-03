---
content_hash: 38247b292743e81443fc02534538ea505a5db4969e58e318672e1509466c80b9
fetched_at: '2026-06-29T00:05:52.163636+00:00'
page_id: '1056938702'
product: rm
source: tdn-rm
title: Informações complementares do documento (TPF)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1056938702
version: 2
---

### Voltar para [Layout único de integração da NFS-e com o TPF](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143731)

| Nome | Pai | Tipo Elemento | Ocorrência | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| infcompl | **[rps](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143860)** | G | 0-1 | Tag raiz que agrupará as informações complementares do documento. |  |  |
| descricao | infcompl | E | 1-1 | Descrição/Dados complementares do documento. |  |  |
| observacao | infcompl | E | 0-1 | Observações referentes ao documento. | infcompl.descricao |  |
| servprestviapublica | constrciv | E | 1-1 | Serviço prestado em vias públicas. |  | Não será gerado |
| obraInscImobFis | constrciv | E | 0-1 | Inscrição imobiliária fiscal da obra |  | Não será gerado |
