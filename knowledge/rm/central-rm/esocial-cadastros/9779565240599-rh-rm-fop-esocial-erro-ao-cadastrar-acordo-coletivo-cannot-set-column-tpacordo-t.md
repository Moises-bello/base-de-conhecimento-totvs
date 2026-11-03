---
article_id: 9779565240599
category: eSocial - Cadastros
content_hash: 9c938aff82acc88a301651b931a80b19535ac634bb50639686c4b5c6d5183109
fetched_at: '2026-06-28T22:47:14.500707+00:00'
product: rm
section_id: 1500000834341
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao cadastrar acordo coletivo: Cannot set Column
  ''TPACORDO'' to be null'
type: support-article
updated_at: '2024-06-19T15:03:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9779565240599-RH-RM-FOP-eSocial-Erro-ao-cadastrar-acordo-coletivo-Cannot-set-Column-TPACORDO-to-be-null
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min****Ocorrência**Ao tentar cadastrar um novo acordo coletivo através do menu **eSocial | Acordo Coletivo / Reajuste por Lei** ocorre o erro: **Cannot set Column 'TPACORDO' to be null. Please use DBNull instead.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9777835814039)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**Este incidente geralmente ocorre quando o Windows .NET Framework não está  atualizado.  
  
**Solução**Conforme documento de Portabilidade, a partir da versão 12.1.34 a atualização do .NET Framework 4.8 passa a ser obrigatória e deve estar atualizada com a última Release que pode ser realizada através do Windows Update, pacote cumulativo KB a depender da versão do Windows.

**Saiba mais**  
Para mais informações, acesse:  
     - [Portabilidade](https://tdn.totvs.com/display/public/LRM/Portabilidade)
