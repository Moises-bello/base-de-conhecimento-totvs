---
content_hash: 90e45d989affb50f29c2c35dabe287b40cf522a7f1b7853285346e47a78e85be
fetched_at: '2026-06-29T00:12:16.231339+00:00'
page_id: '982928635'
product: rm
source: tdn-rm
title: Grupo de Informações do Crédito Presumido - IBS - CT-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=982928635
version: 5
---

# gIBSCredPres - Grupo de Informações do Crédito Presumido, quando aproveitado pelo emitente do documento

Revogado

Revogado pela NT 2025.001 v1.10

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| ~~**gIBSCredPres**~~ | ~~**[gIBSCBS](https://tdn.totvs.com/pages/viewpage.action?pageId=981794544)**~~ | ~~**0-1**~~ | ~~**Grupo**~~ | ~~**Grupo de Informações do Crédito Presumido, quando aproveitado pelo emitente do documento**~~  ~~Este grupo será gerado sempre que o código do Credito presumido estiver preenchido no tributo do Movimento~~ |
| ~~cCredPres~~ | ~~gIBSCredPres~~ | ~~1-1~~ | ~~Elemento~~ | ~~TTRBMOV.CODCREDPRESUMIDO~~  ~~Busca do IBS definido no Movimento~~ |
| ~~pCredPres~~ | ~~gIBSCredPres~~ | ~~1-1~~ | ~~Elemento~~ | ~~TTRBMOV.PCCREDPRESUMIDO~~  ~~Busca do IBS definido no Movimento~~ |
| ~~vCredPres~~ | ~~gIBSCredPres~~ | ~~1-1~~ | ~~Elemento de Escolha~~ | ~~TTRBMOV.VALORCREDPRESUMIDO~~  ~~Busca do IBS definido no Movimento~~ |
| ~~vCredPresCondSus~~ | ~~gIBSCredPres~~ | ~~1-1~~ | ~~Não será gerado~~ |
