---
article_id: 4402820079767
category: Financeiro - Contas a Pagar
content_hash: 80c36783b7cc470fe7dc39246ff4b1678805d410a806dae9c70556e7ed740b6f
fetched_at: '2026-06-28T22:38:08.328903+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA666 - HELP: VLDPARTIC
  -  Usuário não é aprovador da solicitação'
type: support-article
updated_at: '2021-06-18T17:37:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402820079767-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA666-HELP-VLDPARTIC-Usu%C3%A1rio-n%C3%A3o-%C3%A9-aprovador-da-solicita%C3%A7%C3%A3o
---

**Ocorrência**No módulo Viagens, ao tentar realizar (Aprovação de Viagens como aprovador substituto ) apresenta o **HELP VLDPARTIC   
  
![HELP_VIAGENS.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402889509527/HELP_VIAGENS.png)**  
**Ambiente**Cross Segmento - BackOffice Linha Protheus – Financeiro – FINA666 - A partir da versão 12.1.17  
  
**Causa**Esse incidente ocorre, pois o aprovador substituto não está no cadastro do participante - **Rotina APDA020 - Cadastro de Pessoas.**

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

Para que o aprovador substituto possa efetivar aprovação da solicitação de viagem, é necessário que no **Cadastro** **do viajante** seja configurado como **Aprovador substituto**.

Preencher os campos: **(** **Aprovador ) - RD0\_APROPC o aprovador padrão** e no campo **( Substituto ) RD0\_APSUBS o aprovador substituto**

Nessa configuração, tanto o aprovador quanto o substituto podem aprovar as solicitações do viajante.
