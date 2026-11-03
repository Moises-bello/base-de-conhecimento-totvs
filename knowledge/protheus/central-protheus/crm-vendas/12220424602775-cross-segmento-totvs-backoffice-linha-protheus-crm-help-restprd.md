---
article_id: 12220424602775
category: CRM - Vendas
content_hash: d529ce8f3b8d03e8d5f7c8d58500cc1665d64bbea02d5b39d87d9497a2605d09
fetched_at: '2026-06-28T22:40:25.854411+00:00'
product: protheus
section_id: 1500001549102
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - CRM - Help : RESTPRD'
type: support-article
updated_at: '2023-03-31T19:17:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12220424602775-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-CRM-Help-RESTPRD
---

**Dúvida**

Ao incluir o produto na linha da Prosposta Comercial  é apresentado o Help : RESTPRD.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

Este problema é decorrente da configuração do parâmetro MV\_RESTARM, onde o mesmo tem por objetivo de **indicar se utiliza o controle de permissão de uso de armazéns e em qual nível, sendo:**

**(0=Não utiliza;1=Por usuário;2=Por produto;3=Por usuário e produto).**

A primeira possibilidade é deixar o Parâmetro **MV\_RESTARM = 0**. Desta forma ele não utiliza o controle de permissão de uso de armazéns.

A segunda é quando parâmetro está com conteúdo 1, 2 ou 3 **e deseja mantê-lo dessa forma** , deve-se fazer o cadastro das permissões no Armazém. Veja abaixo:

 1. Na tela de cadastro de Locais de estoque (AGRA045) , selecione um armazém e clique em alterar.  
 2. Nesta nova tela será apresentada duas abas sendo "Permissões por Armazéns E "Permissões por Produto";  
 3. Selecione uma das duas opções;  
 4. Preencha os dados de acordo com a opção selecionada;  
 5. Clique em Confirmar.

Quando um usuário que não estiver cadastrado nesta permissão para o armazém tentar realizar uma movimentação, o sistema irá apresentar o Help : RESTPRD informado esta restrição.

Para maiores informações sobre uso do parâmetro ou cadastro de locais de armazém entre em contato com a equipe de suporte Estoque/Custos.
