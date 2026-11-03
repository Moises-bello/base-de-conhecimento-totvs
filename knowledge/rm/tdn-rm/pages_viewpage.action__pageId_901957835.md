---
content_hash: 536c8792e94814161de57c95d0f441f3810480ceee0fc846f228bf49af22e866
fetched_at: '2026-06-29T00:12:02.541439+00:00'
page_id: '901957835'
product: rm
source: tdn-rm
title: Informações do Responsável Técnico pela emissão do DF-e (NFCom)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=901957835
version: 6
---

# gRespTec - Informações do Responsável Técnico pela emissão do DF-e

Para gerar este grupo é necessário ter executado o processo

LayoutCampos

| Campo | Grupo Pai | Ocorrência | Ele | Descrição |
| --- | --- | --- | --- | --- |
| **gRespTec** | **[infNFCom](https://tdn.totvs.com/pages/viewpage.action?pageId=900451399)** | **0-1** | **Grupo** | **Informações do Responsável Técnico pela emissão do DF-e** |
| CNPJ | gRespTec | 1-1 | Elemento | DRESPONSAVELTECNICONFE.CNPJ |
| xContato | gRespTec | 1-1 | Elemento | DRESPONSAVELTECNICONFE.NOME |
| email | gRespTec | 1-1 | Elemento | DRESPONSAVELTECNICONFE.EMAIL |
| fone | gRespTec | 1-1 | Elemento | DRESPONSAVELTECNICONFE.TELEFONE |
| **--- x — Sequência opcional do XML: Será gerado quando a informação estiver preenchida para a UF Emitente** | | | | |
| idCSRT | gRespTec | 1-1 | Elemento da Sequencia | DRESPONSAVELTECNICONFE.IDCSRT |
| hashCSRT | gRespTec | 1-1 | Elemento da Sequencia | Calculado |

Exemploxml

14113791001285
Eduardo XXX
resp\_tecnico\_dfe\_rm@totvs.com.br
1128593911
XXXXXXXX
XXXXXXXXXXXXXXXX
]]>
