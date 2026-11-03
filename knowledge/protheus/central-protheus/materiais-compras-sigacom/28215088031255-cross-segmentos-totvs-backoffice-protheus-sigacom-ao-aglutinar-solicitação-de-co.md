---
article_id: 28215088031255
category: Materiais - Compras (SIGACOM)
content_hash: 77ea99cce98c6aa659db6c7efd9fc561ce875b33d241b8c8be71be7fb9f1ee45
fetched_at: '2026-06-28T22:41:14.108088+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Protheus - SIGACOM - Ao aglutinar Solicitação
  de Compras gera o help RECNO
type: support-article
updated_at: '2024-12-02T19:20:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28215088031255-Cross-Segmentos-TOTVS-Backoffice-Protheus-SIGACOM-Ao-aglutinar-Solicita%C3%A7%C3%A3o-de-Compras-gera-o-help-RECNO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28215087987991) Tempo aproximado para leitura: **00:02:SS min** **Dúvida**

Ao aglutinar Solicitação de Compras gera a mensagem de Recno

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Versão 12

**Solução**

A rotina aglutina solicitação de compras avalia o tipo da solicitação.  
Um apossibilidade da mensagem de "recno" ser apresentada é quando o conteúdo de alguns campos estão conforme a seguir :  
C1\_APROV <> 'B' AND C1\_APROV <> 'R'", essa condição valida se a solicitação está diferente de bloqueada (ou seja liberada), e se existe vestigio de rejeição da aprovação (SC rejeitada).

Essa liberação é executada a partir da rotina Liberação de Documento (MATA094).  
Dessa forma existe a possibilidade de um item da solicitação de compras bloquear pela rotina MATA110 e o outro item bloquear para liberar no MATA094 porque se enquadrou na configuração do grupo de aprovação.

Para não gerar o bloqueio, é necessário efetuar a liberação da solicitação de compras.

***Saiba Mais:***  
[SIGACOM - Alçada de Solicitação de Compras por Entidade Contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017527952-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Al%C3%A7ada-de-Solicita%C3%A7%C3%A3o-de-Compras-por-Entidade-Cont%C3%A1bil)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
