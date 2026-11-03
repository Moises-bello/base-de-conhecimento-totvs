---
article_id: 41425343755287
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: a72ad82d44a4c56abd3d32a7c0e2755e75d036f3cf8a0d522c85c20717b14df0
fetched_at: '2026-06-28T22:39:58.694819+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - TSS Transmissão de Documentos Eletrônicos - NFSE São Paulo-SP:
  XML não compatível com Schema.The element ''RPS'' has invalid child element ''cLocPrestacao''.
  List of possible elements expected: ''NCM, NBS''.'
type: support-article
updated_at: '2026-06-23T13:35:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41425343755287-Cross-Segmentos-TSS-Transmiss%C3%A3o-de-Documentos-Eletr%C3%B4nicos-NFSE-S%C3%A3o-Paulo-SP-XML-n%C3%A3o-compat%C3%ADvel-com-Schema-The-element-RPS-has-invalid-child-element-cLocPrestacao-List-of-possible-elements-expected-NCM-NBS
---

**Dúvida**  
Como solucionar a falha de schema abaixo para a prefeitura de São Paulo-SP?  
**XML não compatível com Schema.The element 'RPS' has invalid child element 'cLocPrestacao'. List of possible elements expected: 'NCM, NBS'.**

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões

**Solução**  
Essa falha de schema ocorre quando a nota fiscal é transmitida **com mais de um item** de serviço e os itens possuem **informações tributárias divergentes.**

Notas fiscais que contenham **itens com NBS e/ou CODISS (Tributação Municipal) distintos** **não devem ser aglutinadas**. Nesses casos, cada serviço deverá ser emitido em uma nota fiscal individual, respeitando suas respectivas classificações tributárias.

Caso todos os itens possuam o mesmo NBS e o mesmo CODISS/TRIBMUN, a aglutinação poderá ser realizada por meio da configuração do parâmetro **MV\_ITEMAGL = "S"**.

**Importante:**  
A utilização de um código **NBS genérico** apenas para possibilitar a aglutinação dos itens pode **não estar em conformidade com a legislação aplicável**. Recomenda-se validar o correto enquadramento dos serviços antes da emissão.

Para mais informações, consulte o material: [Preenchimento da NBS em Notas Fiscais](https://tdn.totvs.com/pages/releaseview.action?pageId=1024330275)
