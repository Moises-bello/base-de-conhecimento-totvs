---
article_id: 235078308
category: Gestão de Armazenagem (WMS)
content_hash: e7fc6013712122d374618222963abb20b6d4d9aac1313f2160092574ad9d4d08
fetched_at: '2026-06-28T22:45:48.105015+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: Logística - Linha Protheus - WMS - Processo e simplificação da leitura das
  informações nos coletores
type: support-article
updated_at: '2024-10-01T19:34:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/235078308-Log%C3%ADstica-Linha-Protheus-WMS-Processo-e-simplifica%C3%A7%C3%A3o-da-leitura-das-informa%C3%A7%C3%B5es-nos-coletores
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26762609194391)***Tempo aproximado para leitura: **00:03:30 min  
  
Dúvida**Como funciona o processo e a simplificação da leitura das informações nos coletores?  
  
**Ambiente**TOTVS Logística - TOTVS WMS (Linha Protheus) - Gestão de Armazenagem (WMS) - Versão 12  
  
**Solução**A leitura das informações nos coletores de dados, na parte de produtos, na grande maioria dos casos é composta pelos seguintes passos:

1. Leitura do produto
2. Leitura do rastro
3. Leitura da quantidade

Na leitura do produto é possível informar qualquer uma destas informações:

* Código do produto
* Código de barras do produto - **SB1 - Descrição Genérica do Produto**
* Código de barras **EAN8** ou **EAN13**
* Código de barras **EAN14**
* Código de barras **EAN128**
* Código de barras complementar - **SLK - Código de Barra Por Produto**
* Etiqueta **CB0 - ID de Etiquetas**

Em algumas rotinas é possível suprimir a informação do rastro. Para isto deve ser habilitado o parâmetro **MV\_WMSLOTE - Solicita a confirmação do lote nas operações com RF?**Em algumas situações a quantidade poderá ser determinada também em função do tipo de informação que é bipado no campo **produto**. Entretanto, esta informação de quantidade só é considerada pelo **WMS - *Warehouse Management System*** quando o ponto de entrada **CBRETEAN**estiver presente no **RPO**. Basta este ponto de entrada existir, independente do seu retorno. Essa quantidade será determinada da seguinte forma:

* Quando informado o código do produto é olhado o campo **Tipo Unit -** **B5\_TIPUNIT** e caso esteja como **1 - Sim**, retorna o valor do campo **Qtd.Emb.Lei -** **B5\_QEL.** Do contrário, retorna 1.
* Nas situações onde é informado o **EAN14** será verificada a unidade de despacho, posição 1 do código, e a quantidade será retornada de acordo com o campo **Qtd X EAN14  -****B5\_EAN14X** que pode ter até 8 combinações.
* Nas situações onde é informado o **EAN128** as informações serão retornadas de acordo com o configurado no código de barras.
* Quando informado um código complementar - **SLK - Código de Barra Por Produto**, será retornada a quantidade parametrizada no cadastro **Códigos de Barras - LOJA210**.

Apenas no caso de **EAN128** é que poderá ser retornada a informação válida de lote para o produto. A quantidade retornada será zerada no **WMS**, obrigando ser informada, caso não exista o ponto de entrada **CBRETEAN**, exceto etiqueta **CB0**.  
  
Caso não seja encontrado o produto em nenhuma das informações acima, será ainda verificado se o código informado representa uma etiqueta de produto **CB0**. Nesta situação serão sempre retornadas as informações de produto, rastro e quantidade a serem consideradas no **WMS**, não permitindo alterar nenhuma desta informações.  
  
Então, como simplificar a leitura?

* Utilizar código de barras **EAN128**.
* Utilizar etiquetas de produto **CB0**.
* Utilizar o ponto de entrada **CBRETEAN**.

Em algumas telas do coletor, após informar o produto, o Sistema apresenta a informação da descrição do produto para o usuário confirmar. Nestas telas também é possível desativar esta informação simplificando ainda mais o processo de leitura.

* Nos processos de separação e de reabastecimento pode ser utilizado o parâmetro: **MV\_WMSVSTE - Apresenta descrição do produto no coletor RF para os processos de movimentação**.
* Nos processos de conferência de expedição, via convocação, e de conferência do recebimento, sem convocação, pode ser utilizado o parâmetro: **MV\_WMSVSTC - Apresenta descrição do produto no coletor RF para os processos de conferência**.
