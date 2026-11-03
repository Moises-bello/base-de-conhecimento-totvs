---
article_id: 36625470206615
category: Materiais - Compras (SIGACOM)
content_hash: 20c8f30fb822092794609ea76c9475f62d13e107d8c216a03d3cd19d4f65c045
fetched_at: '2026-06-28T22:41:18.723348+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Gravação do campo DKD_VALBRU
type: support-article
updated_at: '2025-11-27T17:18:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36625470206615-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Grava%C3%A7%C3%A3o-do-campo-DKD-VALBRU
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36625453994391) Tempo aproximado para leitura: **HH:MM:SS min**  
  
**Dúvida**  
Como criar e efetuar a gravação do campo DKD\_VALBRU ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus)  – Compras – A partir da versão 12.24  
  
**Solução :**

A tabela DKD é uma tabela padrão do Protheus e auxiliar à SD1 ( itens da nota de entrada ), inicialmente foi criada para que os clientes pudessem criar os campos customizados, que não poderiam mais ser criados na SD1, em virtude da quantidade de campos padrão que há na tabela hoje. Porém fez-se necessário, a Totvs começar a utilizá-la também para criar campos padrão também e, dentro eles temos o **DKD\_VALBRU**, **o qual é gravado quando uma nota de entrada possui formulário próprio = Sim,** e há a necessidade da sua transmissão para a SEFAZ.

Para criar o campo DKD\_VALBRU  e atualizar o fonte do compras que o grava, MATA103COM, será necessário aplicar o pacote de expedição contínua abaixo, conforme o release do Protheus em uso em seu ambiente, bem como aplicar o também o dicionário que consta nesse pacote e, na sequência executar o uppdistr.

**Release 2410 -** [**https://tdn.totvs.com/pages/releaseview.action?pageId=522011099#issues-17**](https://tdn.totvs.com/pages/releaseview.action?pageId=522011099#issues-17)

**Release 2510 -**[**https://tdn.totvs.com/pages/releaseview.action?pageId=522011099**](https://tdn.totvs.com/pages/releaseview.action?pageId=522011099)

**OBSERVAÇÃO :**

Caso mesmo após a atualização do sistema e criação do campo, o sistema apresente rejeição no momento da transmissão da nota de entrada, será necessário acionar a equipe do SPED/TSS mediante ticket, para que possam avaliar o motivo da rejeição.

***Saiba Mais: :***

[**tabela DKD**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15673083408279-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-utilizar-mais-de-350-campos-na-tabela-SD1-do-Documento-de-de-Entrada)

[**Rejeição 610**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042423234-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Rejei%C3%A7%C3%A3o-610-Total-da-NF-difere-do-somat%C3%B3rio-dos-Valores-comp%C3%B5e-o-valor-Total-da-NF-para-nota-de-Suframa)

[**DKD\_VALBRU**](https://tdn.totvs.com/pages/releaseview.action?pageId=1002496677)

[**Rejeição 029**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049488234--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-029-Falha-no-schema-do-XML-com-schema-v%C3%A1lido)

[**PÁGINA CENTRALIZADORA DO COMPRAS**](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[**Artigos Materiais - Compras (SIGACOM)**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
