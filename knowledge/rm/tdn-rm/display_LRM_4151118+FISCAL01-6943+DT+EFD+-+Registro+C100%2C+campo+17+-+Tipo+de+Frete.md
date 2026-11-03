---
content_hash: cdae9b68737a38c8aec72d306383e69c9cb8aca5e6c27df9a082a3f814824ea1
fetched_at: '2026-06-29T00:09:39.453326+00:00'
page_id: '431666457'
product: rm
source: tdn-rm
title: 4151118 FISCAL01-6943 DT EFD - Registro C100, campo 17 - Tipo de Frete
type: documentation
url: https://tdn.totvs.com/display/LRM/4151118+FISCAL01-6943+DT+EFD+-+Registro+C100%2C+campo+17+-+Tipo+de+Frete
version: 1
---

Tempo aproximado para leitura:**01 min**

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | Gestão Fiscal |
| Função: | EFD - Contribuições |

**02. SITUAÇÃO/REQUISITO**

Ao gerar a EFD Contribuições no registro C100 o campo 17 - Tipo de Frete está sendo gerado vazio para os tipos 3 - Por conta do Próprio Remetente e 4 - Por conta do Próprio Destinatário.

**03. SOLUÇÃO**

Ajustado o layout de geração da rotina para que os dois tipos passem a ser considerados na geração do campo 17 do registro C100.
