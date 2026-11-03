---
article_id: 4402310087575
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 1b780ce382fff7b22021429f5c257d935d5f7da49d2b6bafb9fae106b1b09d10
fetched_at: '2026-06-28T22:39:57.446285+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Forma de
  Recolhimento - Araxá-MG
type: support-article
updated_at: '2025-06-25T13:25:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402310087575-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Forma-de-Recolhimento-Arax%C3%A1-MG
---

**Dúvida**Regra de preenchimento da Forma de Recolhimento para NFSE de Araxá-MG.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Documentos Eletrônicos - Todas as versões.  
  
**Solução**

O manual webservice de Araxá-MG sugere os conteúdos abaixo para a tag <FrmRec> com a Forma de Recolhimento no xml do RPS:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402310312599)  
Link: <http://201.62.57.11:9090/esiatAraxa/Setup/Integra%C3%A7%C3%A3o%20Web%20Service.pdf>  
  
No Protheus, para gerar a **Forma de Recolhimento** usamos a regra abaixo:

**FormaRecolhimento=00**  
A1\_RECISS/C5\_RECISS=2 e MV\_REGIESP diferente de 3.

**FormaRecolhimento=01**  
A1\_RECISS/C5\_RECISS=1

**FormaRecolhimento=03**  
MV\_OPTSIMP=1

**FormaRecolhimento=04**  
B1\_ORIGEM=0 + F4\_SITTRIB=5 ou F4\_CSTISS=05

**FormaRecolhimento=05**  
F4\_ISSST= 03 ou 04

**FormaRecolhimento=06**  
F4\_ISSST=14 (Criar essa opção no campo)

**FormaRecolhimento=07**  
MV\_REGIESP=7
