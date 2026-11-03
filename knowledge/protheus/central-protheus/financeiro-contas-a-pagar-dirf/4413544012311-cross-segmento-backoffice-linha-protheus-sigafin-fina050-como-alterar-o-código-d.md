---
article_id: 4413544012311
category: Financeiro - Contas a Pagar - Dirf
content_hash: 4d925cc20bba0de5bd62f5b311b2f9c9ac79c3a82f3815106cbcde1b19337ecc
fetched_at: '2026-06-28T22:38:10.694020+00:00'
product: protheus
section_id: 1500001550482
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA050 - Como alterar
  o código de retenção após envio das informações para a DIRF
type: support-article
updated_at: '2023-01-25T21:05:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413544012311-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA050-Como-alterar-o-c%C3%B3digo-de-reten%C3%A7%C3%A3o-ap%C3%B3s-envio-das-informa%C3%A7%C3%B5es-para-a-DIRF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como alterar o código de retenção no Financeiro após envio das informações para a DIRF?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Solução**.  
No financeiro, é possível alterar o campo **Cd. Retenção (E2\_CODRET)**, se o titulo estiver em aberto, se o titulo estiver baixado será necessário excluir a baixa e alterar o campo.  
Se não for possível cancelar a baixa, será necessário realizar uma manutenção pontual no registro via banco de dados corrigindo a informação do campo E2\_CODRET.   
  
**Saiba mais**[Geração de Dados para DIRF (FINA401)](https://tdn.totvs.com/pages/releaseview.action?pageId=224126168)
