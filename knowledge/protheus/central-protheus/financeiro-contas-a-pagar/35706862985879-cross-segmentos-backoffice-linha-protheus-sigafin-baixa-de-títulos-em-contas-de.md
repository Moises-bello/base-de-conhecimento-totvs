---
article_id: 35706862985879
category: Financeiro - Contas a Pagar
content_hash: 851f9c66388748f8f8cd3a55a872ab306e4d35bef3cb2faaa2c9dcb320bb2852
fetched_at: '2026-06-28T22:38:08.481464+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Baixa de títulos em
  contas de outras filiais
type: support-article
updated_at: '2025-10-17T19:15:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35706862985879-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Baixa-de-t%C3%ADtulos-em-contas-de-outras-filiais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35706862974871) Tempo aproximado para leitura: **00:05 min**  
  
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
