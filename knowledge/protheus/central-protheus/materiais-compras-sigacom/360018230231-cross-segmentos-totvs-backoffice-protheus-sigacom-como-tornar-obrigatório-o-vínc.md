---
article_id: 360018230231
category: Materiais - Compras (SIGACOM)
content_hash: 9539c9133ae0f534db0f1389ca48bcc5d8e64d926e75703c5086596c8207dd65
fetched_at: '2026-06-28T22:41:10.480816+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM: Como tornar obrigatório
  o vínculo do Pedido de Compras no Documento de Entrada?'
type: support-article
updated_at: '2024-06-20T18:04:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018230231-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-tornar-obrigat%C3%B3rio-o-v%C3%ADnculo-do-Pedido-de-Compras-no-Documento-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24318223684759) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**

Como tornar obrigatório o vínculo do Pedido de Compras no Documento de Entrada?

Ambiente

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - A partir da versão 11.80   
  
  
**Solução**

É possível tornar obrigatória o vínculo do Pedido de Compras no documento de entrada com uso do parâmetro **MV\_PCNFE**

Exceções a esta restrição pode ser informadas através do parâmetro **MV\_TESPCNF** cujas inforamções estão no artigo:

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como permitir Inclusão de Documento de Entrada sem Pedido vinculado, com o MV\_PCNFE ativado (MV\_TESPCNF) ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019760331-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-permitir-Inclus%C3%A3o-de-Documento-de-Entrada-sem-Pedido-vinculado-com-o-MV-PCNFE-ativado-MV-TESPCNF)

Com o parâmetro **MV\_PCNFE** habilitado, todos lançamentos da rotina **MATA103** e **MATA140** necessitarão de pedido de compra.

Caso necessite incluir uma nota fiscal, onde esta for inserida com TES de exceção cadastrada (**MV\_TESPCNF)**, ela deverá incluir diretamente pelo documento de entrada (**MATA103**), para que o sistema faça a exeção corretamente.

Por padrão do Protheus na rotina **MATA140** não há o campo de Tipo de TES, sendo assim, a exceção do parâmetro **MV\_TESPCNF** valerá apenas para a rotina de Documento de Entrada (**MATA103**), ou seja, verificará a exceção cadastrada.

Caso não atenda à sua necessidade, verifique a utilização do ponto de entrada :  [**MT140PC**](http://tdn.totvs.com/pages/releaseview.action?pageId=6085510).

**Obs.1:**

O Parâmetro MV\_TESPCNF possui funcionalidade apenas para a rotina de Documento de Entrada MATA103.

**Obs.2:** ***MV\_TESPCNF no Totvs Colaboração / Importador XML:***

O Colaboração/Importador XML é um facilitador para a inclusão do Documento e no caso ele segue as mesmas regras do rotina de inclusão manual.  
No caso da inclusão de Pré-Nota de Entrada, não se informa TES na rotina e dessa forma o parâmetro MV\_TESPCNF não possui funcionalidade tanto na rotina manual (MATA140), quanto na geração de Pré-Nota pelo Totvs Colaboração / Importador XML.

Este é o funcionamento padrão da rotina de Pré-Nota de Entrada (o parâmetro MV\_TESPENF não tem funcionalidade nesta rotina), e o Importador XML trabalha com o mesmo conceito, necessitando a informação do Pedido de Compras se o parâmetro MV\_PCNFE estiver habilitado.

Para a Exceção ao uso do **MV\_PCNFE** quando gerada Pré-Nota, pode ser tratada através da utilização do Ponto de Entrada [**MT140PC**](http://tdn.totvs.com/pages/releaseview.action?pageId=6085510).

***Saiba Mais :***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como permitir Inclusão de Documento de Entrada sem Pedido vinculado, com o MV\_PCNFE ativado (MV\_TESPCNF) ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019760331-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-permitir-Inclus%C3%A3o-de-Documento-de-Entrada-sem-Pedido-vinculado-com-o-MV-PCNFE-ativado-MV-TESPCNF)

[Pontos de Entrada](https://tdn.totvs.com/display/public/PROT/IX02+-+Pontos+de+Entrada)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
