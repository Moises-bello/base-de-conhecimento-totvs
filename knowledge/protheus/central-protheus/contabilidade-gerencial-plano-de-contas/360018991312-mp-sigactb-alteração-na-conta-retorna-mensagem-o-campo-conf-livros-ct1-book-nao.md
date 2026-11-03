---
article_id: 360018991312
category: Contabilidade Gerencial - Plano de Contas
content_hash: 1bc79ccdb08aac8658f5b52e666c4db1e50607908e8a1d1949335cc33b3c01ce
fetched_at: '2026-06-28T22:40:33.405269+00:00'
product: protheus
section_id: 1500001549022
source: central-protheus
title: MP - SIGACTB - ALTERAÇÃO NA CONTA RETORNA MENSAGEM "O campo Conf. Livros (CT1_BOOK)
  nao foi preenchido"
type: support-article
updated_at: '2021-04-28T15:26:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018991312-MP-SIGACTB-ALTERA%C3%87%C3%83O-NA-CONTA-RETORNA-MENSAGEM-O-campo-Conf-Livros-CT1-BOOK-nao-foi-preenchido
---

**Ocorrência**

Na alteração de uma conta contabil em ambiente configurado para integração via EAI, retorna mensagem "O campo Conf. Livros (CT1\_BOOK) nao foi preenchido"

**Ambiente**

PROTHEUS – Contabilidade Gerencial – A partir da versão 11.80  
   
 **Causa**

Campo esta configurado para ser obrigatório  
 **Solução**

No Protheus , Acesse o configurador em dicionário de dados, na tabela CT1 e desmarque a opção "Obrigatório" e "Browse", salve, e realize procedimento novamente.
