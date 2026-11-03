---
article_id: 4404567650711
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 511bbfb52cb71a2fabc27e6fb1004049ea978c60d0f3cf606fae56c633199214
fetched_at: '2026-06-28T22:38:45.078187+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Lock de Tabelas
  na rotina de Preparação do Documento de Saída
type: support-article
updated_at: '2021-07-19T18:24:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404567650711-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Lock-de-Tabelas-na-rotina-de-Prepara%C3%A7%C3%A3o-do-Documento-de-Sa%C3%ADda
---

**Dúvida**Como funciona o Lock de Tabelas na rotina de Preparação do Documento de Saída?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Todas as versões.  
  
**Solução**Ao realizar a emissão de um Documento de Saída, o sistema inicia um processo de gravação das tabelas que chamamos de “***Transação***”, nesta transação o sistema precisa realizar a alteração/inclusão de informações nas tabelas, para isso ele realiza um “***Lock***”, que seria uma reserva do registro na tabela para que não seja possível que dois usuários alterem o mesmo registro ao mesmo tempo, pois isso causaria inconsistências nas informações.

Ao iniciar a emissão do documento de saída, suponha que esse documento possui várias linhas com o mesmo produto, o sistema realizará o Lock de acordo com as informações da nota, a tabela SC5 (Cabeçalho do Pedido de Vendas) possui apenas um Lock, pois o cabeçalho é um só para vários itens, já para a tabela SC6 (Itens do pedido de venda), o sistema realiza vários Locks, por serem vários itens.

O sistema inicia a gravação das informações do Documento de Saída dentro da mesma transação e apenas **libera os Locks**ao concluir a gravação de **todas as tabelas envolvidas**, isso é um conceito geral do Protheus e ocorre para que, caso, por qualquer motivo, a transação seja interrompida, não ocorra de o sistema atualizar algumas tabelas e outras não.

Isso significa que, caso possua uma nota com dez itens diferentes, o sistema realizará o Lock dos dez itens na tabela SB2 e só liberará esse Lock ao concluir a gravação da nota.

Esse conceito de programação é utilizado para todas as rotinas/tabelas do Protheus, alterações no funcionamento padrão do sistema devem ser customizadas ou sugeridas através da **[Central Colaborativa](https://youtu.be/hi7XgZSt6JI)**.

Para informações a respeito dos **parâmetros** e **pontos de entrada** para tratamento do Lock de tabelas, verifique o Link: **<https://tdn.totvs.com/x/_IKcEw>**

**Saiba Mais: <https://tdn.totvs.com/x/z6SSJQ>**
