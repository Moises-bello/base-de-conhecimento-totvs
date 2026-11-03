---
article_id: 35706892794135
category: Financeiro - Contas a Receber
content_hash: d9c0361d51116a2b442c7f15a74fb0d1ec9412dd3f862fa10a5f64200d51e00b
fetched_at: '2026-06-28T22:38:13.913856+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Baixa de títulos em
  contas de outras filiais
type: support-article
updated_at: '2025-10-17T19:15:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35706892794135-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Baixa-de-t%C3%ADtulos-em-contas-de-outras-filiais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35706892776983) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
É possível realizar a baixa de um título utilizando uma conta bancária cadastrada em outra filial?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.

**Solução**  
O sistema permite essa operação **somente quando a tabela SA6 (Cadastro de Bancos)** estiver configurada **de forma compartilhada.**

Essa configuração possibilita que os bancos cadastrados sejam **visualizados e utilizados por mais de uma filial**, de acordo com o nível de compartilhamento adotado no ambiente.

**Importante**

Caso o modo de compartilhamento da tabela SA6 (ou de qualquer outra tabela) seja alterado durante o uso do sistema, a nova configuração **passará a valer apenas para os registros criados após a mudança**.  
Os cadastros existentes anteriormente **permanecem com o nível de compartilhamento anterior**.
