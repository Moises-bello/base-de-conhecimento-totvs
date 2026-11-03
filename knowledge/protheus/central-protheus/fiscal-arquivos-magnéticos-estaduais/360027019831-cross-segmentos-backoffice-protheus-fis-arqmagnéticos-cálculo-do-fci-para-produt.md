---
article_id: 360027019831
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: e31896ecc0f9b7273c6748e2f22620322b290a24e72b312df72c9bde7bf6cf3d
fetched_at: '2026-06-28T22:42:10.267683+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Cálculo do FCI
  para Produtos Novos
type: support-article
updated_at: '2022-09-19T12:16:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027019831-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-C%C3%A1lculo-do-FCI-para-Produtos-Novos
---

**Dúvida**  
Como o sistema trata o código do FCI na primeira venda de um produto novo onde ainda não ocorreu movimentações?  
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Caso não exista documento fiscal de saída, o sistema irá verificar se o produto é novo e para isso irá utilizar os parâmetros abaixo:

- **MV\_FCINWPR** precisa estar com o conteúdo igual ao parâmetro **MV\_ESTADO**  
- Se o parâmetro **MV\_FCIPRV** estiver igual a 1, você deve preencher o campo **B1\_PRV1**  
- Se o parâmetro **MV\_FCIPRV** estiver igual a 2, você deve preencher o campo **B5\_FCIPRV**  
- Se o parâmetro **MV\_FCIPRV** estiver igual a 3, você deve preencher o campo **BZ\_FCIPRV**.

Informar a **UF** no **MV\_FCINWPR**

Para o parâmetro **MV\_FCINWPR**   
  
**Observação:** Caso tenha varias filiais em unidade federativas diferentes é necessário criar um parâmetro para cada filial.

Para mais informações, acesse o *link* abaixo:  
  
**Ficha de Conteúdo de Importação e Valor de Importação**  
  
<http://tdn.totvs.com/pages/releaseview.action?pageId=185758724>
