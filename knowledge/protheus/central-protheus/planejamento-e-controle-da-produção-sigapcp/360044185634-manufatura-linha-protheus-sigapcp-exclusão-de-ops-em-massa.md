---
article_id: 360044185634
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 6d024c53645ca7f5c107f8dfbede4184fef318453fcbace81812608eedf07ee1
fetched_at: '2026-06-28T22:42:42.333550+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Exclusão de OPs em massa
type: support-article
updated_at: '2021-09-24T12:28:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044185634-Manufatura-Linha-Protheus-SIGAPCP-Exclus%C3%A3o-de-OPs-em-massa
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:30****min****Dúvida**Existe alguma forma de cancelar um lote de **OPs - Ordens de Produção**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Utilize a rotina **MATA740 - Cancelamento OPs**, informe o número da **OP** inicial e final. As **OPs** que não tiveram movimentos de requisição ou apontamento serão excluídas, as demais serão listadas no relatório **MATR895 - Relação de OPs Não Canceladas** que será gerado ao final do processo.
