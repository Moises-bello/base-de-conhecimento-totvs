---
content_hash: 0994429838217f407552be88293df84380241bc959f6f4396b64a42270337cf7
fetched_at: '2026-06-29T00:10:21.650752+00:00'
page_id: '490986834'
product: rm
source: tdn-rm
title: 5698431 FINANCEIRO01-11814 Retorno pagamento padrão SIACC
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=490986834
version: 2
---

# **RETORNO DE PAGAMENTO**

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Retorno de Pagamento |
| **Situação/Requisito:** | O campo FLAN.SEQSIACC é utilizado para identificação dos pagamentos no padrão SIACC da CEF. Tal Campo é um sequencial controlado por convenio, ou seja, cada convenio tem o seu sequencial. Caso o cliente possua mais de 1 convenio na coligada com essa integração está gerando conflito de preenchimento do campo FLAN.SEQSIACC com isso não finaliza a importação do retorno corretamente. |
| **Solução/Implementação:** | Otimizado o processo de retorno de pagamento ao utilizar o padrão SIACC para considerar o código do convenio (posição 33 a 38 do header do arquivo retorno) na busca do lançamento devido a sequencial SIACC repetidos. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A |
| **Documento de Referência:** | N/A. |
| **Pacote:** | N/A. |
