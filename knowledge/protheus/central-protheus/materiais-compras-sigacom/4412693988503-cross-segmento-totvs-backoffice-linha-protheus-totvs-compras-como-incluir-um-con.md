---
article_id: 4412693988503
category: Materiais - Compras (SIGACOM)
content_hash: 31337d8787d7b81599b9c245f679d0863e06b503a12f1e9e2f56fc32e5acb6bf
fetched_at: '2026-06-28T22:41:11.771507+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - Como incluir
  um contrato de parceria até chegar no documento de entrada?
type: support-article
updated_at: '2025-12-26T17:08:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412693988503-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Compras-Como-incluir-um-contrato-de-parceria-at%C3%A9-chegar-no-documento-de-entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16532636704663) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**

Qual é o processo a ser realizado para incluir um contrato de parceria, passando pela autorização de entrega, até chegar no documento de entrada?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - Versão 12

**Solução**

Esta rotina destina-se às empresas que possuem contrato de fornecimento de produtos por um determinado período, eliminando a necessidade da inclusão de diversas **Solicitações de Compras** e de realização de **Cotações**, agilizando o processo de compra.

No **Contrato de Parceria,** define-se a cada sequência de item, o produto e a quantidade a ser adquirida para o período. Assim pode-se definir, por exemplo, todos os itens a serem adquiridos durante o ano.

As informações do contrato de parceria são gravadas na **Tabela SC3**

**Quais os requisitos para incluir um Contrato Parceria?**

Para utilizar um produto em um **Contrato de Parceria** preencha com **SIM** o campo "**Contrato" (*****B1\_CONTRAT*****)** do cadastro de [Produtos](https://tdn.totvs.com.br/pages/viewpage.action?pageId=306856486).

![Screenshot_3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412686150295)

***IMPORTANTE:*** Caso utilize o campo como **S - Sim,** o produto será bloqueado para incluir em **Solicitação de Compras** e **Pedido de Compras.**

Caso queira utilizar em ambas as rotinas, precisa informar o campo como **A - Ambos**

**Passo 1 - Incluir um contrato de parceira**

No módulo de compras, acesse a rotina MATA125 Contrato de Parceria -> Incluir -> Preencher o contrato e selecionar um produto B1\_CONTRAT = Sim

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16531983807895)

Preencher os campos no Grid com as informações de produto

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21132377985943)

***Obs:***

No processo de inclusão de Contrato de Parceria não é gerado Título Financeiro.

**Passo 2 - Incluir uma autorização de entrega**

Acessar a rotina MATA122 -> Incluir

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16532348801175)

Preencher o cabeçalho -> Posicionar no grid do item -> Outras Ações -> Contrato

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16532425915415)

Selecionar o Contrato desejado -> Salvar -> Salvar a autorização de entrega

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16532462628503)

**Passo 3- Incluir um documento de entrada**

Acesse a MATA103 -> Incluir -> Preencha o cabeçalho da nota -> Posicione no grid do item -> Outras Ações -> Pedido

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16532543231383)

Selecione a autorização de entrega desejada -> Salvar

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16532567863191)

Note que são apresentados tanto os pedidos de compra quanto as autorizações de entrega. Para diferenciá-los basta analisar o campo Origem. PC = pedido de compras e AE = autorização de entrega

***Saiba Mais:***

[Contrato Parceria](https://tdn.totvs.com/x/VYjyE%20)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - É possível configurar controle de alçada com entidade contábil para contrato de parceria?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414194738711-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-%C3%89-poss%C3%ADvel-configurar-controle-de-al%C3%A7ada-com-entidade-cont%C3%A1bil-para-contrato-de-parceria-?source=search)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
