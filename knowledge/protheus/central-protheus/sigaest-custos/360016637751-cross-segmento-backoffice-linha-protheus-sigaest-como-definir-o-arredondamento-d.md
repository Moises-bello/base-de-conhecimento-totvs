---
article_id: 360016637751
category: SIGAEST - CUSTOS
content_hash: e56917b29e472359e0c6031e8150e9e6071cf2eeefee2a708cac0cea064e8996
fetched_at: '2026-06-28T22:39:00.691576+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como definir o arredondamento
  do Custo unitário no movimento do produto?
type: support-article
updated_at: '2023-09-19T19:24:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016637751-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-definir-o-arredondamento-do-Custo-unit%C3%A1rio-no-movimento-do-produto
---

**Dúvida**

Como definir o arredondamento do Custo unitário no movimento do produto? Valor de saída e entrada esta diferente nas transferências entre armazéns, aparentemente diferença de arredondamento de decimais, como ajustar?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17658329738519)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
  
**Solução**

Através do parâmetro **MV\_CMROUND**, poderá definir qual a forma de **arredondamento** do custo unitário da movimentação, ou seja, poderá escolher se a gravação do custo será com **Arredondamento** ou **Truncado (Noround)**.

***Importante:*** O parâmetro só funcionará caso o registro ainda não tenha sido gravado, ou seja, após a alteração do parâmetro é necessário refazer as movimentações.

**Parâmetro** : **CMROUND**

Descrição conteúdo: O custo da movimentação será . T. arredondamento .F. Truncado

Tipo: Lógico

**.T.** - Arredondamento

**.F.** - Truncado(Noround)

**Saiba Mais**

*[Clique aqui e veja mais artigos sobre CUSTOS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*

*[MV\_CMROUND - Parâmetro para realizar o Arrendondamento ou Truncate na gravação do campo B2\_CM](http://tdn.totvs.com/pages/viewpage.action?pageId=327330694)*
