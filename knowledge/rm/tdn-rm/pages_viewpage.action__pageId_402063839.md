---
content_hash: e7fbb2cd92138389f3174de4fe6ebb54fabb966d80f03b3b2509d7a43a830bd7
fetched_at: '2026-06-29T00:09:10.602084+00:00'
page_id: '402063839'
product: rm
source: tdn-rm
title: 3148376 FISCAL01-6176 DT NF-e - Gerar TAG nFCI número da FCI para operações
  internas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=402063839
version: 3
---

# NF-e - Gerar TAG nFCI número da FCI para operações internas

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Emissão de NF-e |
| **Situação/Requisito:** | a Sefaz de São Paulo exige a geração da tag relacionada ao número da FCI para operações dentro do próprio estado. Atualmente o ERP RM realiza a seguinte validação para gerar tal tag: "*O Número da FCI passará a ser obrigatória nas operações interestaduais (CFOP iniciadas por 2 ou 6), conforme a Origem da Mercadoria (3, 5 ou 8), a partir de 01/10/2013. Será selecionado o número da última FCI cadastra para o produto na filial e coligada que o processo estiver sendo executado.*" |
| **Solução/Implementação:** | Foi alterado o processo de montagem do XML da NF-e para gerar a TAG nFCI independente se a operação é interestadual |
