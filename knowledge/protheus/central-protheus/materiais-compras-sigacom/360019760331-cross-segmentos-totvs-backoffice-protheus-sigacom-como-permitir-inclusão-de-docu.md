---
article_id: 360019760331
category: Materiais - Compras (SIGACOM)
content_hash: 26357f81b0c42fc44237d1f6a08188dddc2391a2a45b5e44b4f153a7348f6d95
fetched_at: '2026-06-28T22:41:12.812041+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus  -  SIGACOM - Como permitir Inclusão
  de Documento de Entrada sem Pedido vinculado, com o MV_PCNFE ativado (MV_TESPCNF)
  ?
type: support-article
updated_at: '2024-10-09T21:02:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019760331-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-permitir-Inclus%C3%A3o-de-Documento-de-Entrada-sem-Pedido-vinculado-com-o-MV-PCNFE-ativado-MV-TESPCNF
---

**Dúvida**

Como permitir Inclusão de Documento de Entrada sem Pedido vinculado, com o MV\_PCNFE ativado (MV\_TESPCNF) ?

**Ambiente**A partir da Versão 11.  
  
  
**Solução**

|  |
| --- |
| Para que o sistema obrigue a amarração de um pedido de compras à nota fiscal de entrada, deve-se configurar os parâmetros MV\_PCNFE e MV\_TESPCNF.  Ao informar no parâmetro MV\_TESPCNF os Tipos Entrada e Saída (TES), o sistema não exigirá a amarração com pedido de compras para os itens da nota fiscal que possuírem algum dos TES informados neste parâmetro.  Ao deixar o conteúdo do parâmetro vazio, o sistema não permitirá a confirmação da digitação de um item da nota fiscal sem que exista amarração com um pedido de compras, independente da TES utilizada na entrada da nota fiscal. |

**Obs.1:**

O Parâmetro MV\_TESPCNF possui funcionalidade apenas para a rotina de Documento de Entrada MATA103.

**Obs.2:**  ***MV\_TESPCNF no Totvs Colaboração / Importador XML:***

O Colaboração/Importador XML é um facilitador para a inclusão do Documento e no caso ele segue as mesmas regras do rotina de inclusão manual.  
No caso da inclusão de Pré-Nota de Entrada, não se informa TES na rotina e dessa forma o parâmetro MV\_TESPCNF não possui funcionalidade tanto na rotina manual (MATA140), quanto na geração de Pré-Nota pelo Totvs Colaboração / Importador XML.

Este é o funcionamento padrão da rotina de Pré-Nota de Entrada (o parâmetro MV\_TESPENF não tem funcionalidade nesta rotina), e o Importador XML trabalha com o mesmo conceito, necessitando a informação do Pedido de Compras se o parâmetro MV\_PCNFE estiver habilitado.

Para a Exceção ao uso do **MV\_PCNFE** quando gerada Pré-Nota, pode ser tratada através da utilização do Ponto de Entrada [**MT140PC**](http://tdn.totvs.com/pages/releaseview.action?pageId=6085510)

***Saiba Mais :***

[Pontos de Entrada](https://tdn.totvs.com/display/public/PROT/IX02+-+Pontos+de+Entrada)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
