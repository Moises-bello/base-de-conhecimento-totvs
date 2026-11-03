---
article_id: 17901694726423
category: TAF - REINF
content_hash: c3ed3b312dcb407c9421cd581c3aefccf7381d1142f40df163512f1c9e51607c
fetched_at: '2026-06-28T22:41:34.819740+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Rejeição MS0038 ao transmitir
  em ambiente de Produção da Reinf 2.1.2
type: support-article
updated_at: '2023-09-29T12:02:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17901694726423-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Rejei%C3%A7%C3%A3o-MS0038-ao-transmitir-em-ambiente-de-Produ%C3%A7%C3%A3o-da-Reinf-2-1-2
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17901679277847) Tempo aproximado para leitura: **00:03:50min****Ocorrência**

Ao efetuar a transmissão dos eventos da Reinf no layout 2.1.2 em Produção, é apresentada a rejeição **MS0038 -** **Para envio de eventos em Produção, o ambiente deve ser igual a 1. Para o envio de eventos em pré-produção, o ambiente deve ser igual a 2.**Essa rejeição pode estar sozinha ou acompanhada de outros códigos de rejeições.  
**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Automação Fiscal - a partir da 12.1.33  
  
**Causa**

Esse incidente ocorre devido ao repositório do **TSS** não estar adequado para transmitir em produção.

É necessário que o fonte TSSPROCREINF esteja com data superior a 08/2023.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Atualizar o repositório do TSS pelo link: [MP - TSS - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-MP-TSS-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS)

2. Acessar o menu: **Atualizações > Eventos Reinf > Tabelas** (caso a rejeição se der em um evento de tabela) ou **Periódicos** (caso se tratar de um evento periódico. Acessar o **menu correspondente** ao nome do **evento** nesse caminho e excluir o evento inconsistente (que estará com a legenda **vermelha**)

3. Acessar o **Painel Reinf**, apurar e transmitir novamente o evento.

É obrigatório que o evento rejeitado seja excluído antes da retransmissão após atualizar o TSS, caso contrário a rejeição irá permanecer.
