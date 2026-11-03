---
article_id: 4414392856343
category: Financeiro - Contas a Pagar
content_hash: 9f7c40757e943cb0899c359b1e364181d2f79a96e7bc7e1327e310dfb685f7aa
fetched_at: '2026-06-28T22:38:08.367278+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus- SIGAFIN - FINA677 - HELP F677ACESSO:
  Usuario não possui acesso para liberar financeiro'
type: support-article
updated_at: '2024-06-19T18:09:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414392856343-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA677-HELP-F677ACESSO-Usuario-n%C3%A3o-possui-acesso-para-liberar-financeiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:20 min****Ocorrência**No módulo Financeiro, ao tentar realizar a liberação/estorno para o financeiro via prestação de contas, apresenta a mensagem F677ACESSO - Usuário não possui acesso para liberar financeiro  
**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) - Financeiro - FINA677 - Todas as versões  
  
**Causa**Esse incidente ocorre, pois somente **Aprovadores** e **Aprovadores Substitutos** podem realizar a liberação para o financeiro.   
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse a rotina **APDA020 - Cadastro de Pessoas** e altere o cadastro do participante da viagem.  
2. No cadastro do participante na aba "**Viagens**", adicione no campo "**Aprovador Substituto** - **RD0\_APSUBS**" o código do usuário que realizará a liberação para não apresentar mais o HELP.

**Saiba mais:**  
[Cross Segmento - BackOffice Linha Protheus - SIGAFIN - FINA677 - HELP: RECNO - Aprovação da Prestação de Contas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407080924439-Cross-Segmento-BackOffice-Linha-Protheus-SIGAFIN-FINA677-HELP-RECNO-Aprova%C3%A7%C3%A3o-da-Presta%C3%A7%C3%A3o-de-Contas)  
<https://tdn.totvs.com/display/public/PROT/Viagens+-+Financeiro+-+P12>
