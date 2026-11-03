---
article_id: 360062599353
category: Materiais - Compras (SIGACOM)
content_hash: d4dc5b6f82b4785aa484f01737da016c9fabb2ee84f6b258e565acb63de422ad
fetched_at: '2026-06-28T22:41:20.155298+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - MATA121 - Relatório
  pedido de compra (MATR110), usuário de impressão marcado como alteração
type: support-article
updated_at: '2022-05-16T21:11:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062599353-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-MATA121-Relat%C3%B3rio-pedido-de-compra-MATR110-usu%C3%A1rio-de-impress%C3%A3o-marcado-como-altera%C3%A7%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:57s**  
**Dúvida**Utilizando os campos 'log de inclusão' e 'log de alteração' no Pedido de Compras (SC7), ao efetuar a impressão do relatório (MATR110) com usuários diversos, o sistema interpreta a emissão como uma alteração, atualizando o usuário no log de alterações.

**Ambiente**

Microsiga protheus - Compras - Versão 12

**Solução** A altualização do usuário no Log de alteração se dá conforme conceito implementado a tabela SC7.  
Ao imprimir o pedido, o registro (SC7) é alterado, atualizando os campos Quantidade de Reemissoes  (C7\_QTDREEM) e Já emitiu (C7\_EMITIDO). Sendo alterado, a função de controle de log do framework registra a alteração, atualizando o campo com usuário que efetuou a impressão.

Caso não queira que o sistema efetue as validações, sugiro que via portal do cliente, baixe o fonte do relatório MATR110 e customize-o, retirando a atualização dos campos de impressão.
