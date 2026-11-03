---
content_hash: 93c6a66bd5c2093b8406bff0d88516a3b07de848fd96d74ec0797a91192f6505
fetched_at: '2026-06-29T00:10:12.260986+00:00'
page_id: '454427409'
product: rm
source: tdn-rm
title: FISCAL01-7763 DT Alterar geração da NFS-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=454427409
version: 2
---

# Tags de Descrição, Discriminação e Observação sejam geradas conforme parametrizado

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Envio da NFS-e |
| **Situação/Requisito:** | Alterar a geração da NFS-e para que as tags de Descrição, Discriminação e Observação sejam geradas conforme parametrizado |
| **Solução/Implementação:** | Durante a emissão da NFS-e, os seguintes campos podem ser parametrizados para serem compostos por outros campos:  Discriminação do Serviço Descrição do Serviço Observação do Serviço  Para cada um desses campos, o sistema irá apresentar as seguintes opções para seleção, respeitando-se a ordem:  Histórico do Movimento Histórico do Lançamento Descrição do Produto Número do Contrato  Para a composição dos Históricos (do Movimento e do Lançamento): O sistema recuperará o histórico curto ou longo a depender do parâmetro do Estoque - Parâmetros Gerais - 04.01.04.07 Produtos 2/3 - Tipo Histórico  Para a composição da Descrição do Produto: O sistema recuperará a descrição do Produto como a descrição do produto, descrição auxiliar ou nome fantasia a depender do parâmetro do Estoque - Parâmetros Gerais - 04.01.04.07 Produtos - 1/3 Descrição do Produto  Além disso, para as tags que acumulam mais de um item, o conteúdo será composto pelos campos parametrizados, respeitando-se a ordem, do primeiro item, para depois ser inserido os campos do segundo item e assim consecutivamente. Caso algum conteúdo seja repetido, o mesmo não será concatenado novamente. |
