---
content_hash: 02b175d94c3739659025b72523513c94b702cb3e0812967b2299190ff31e2804
fetched_at: '2026-06-29T00:10:14.661272+00:00'
page_id: '461920526'
product: rm
source: tdn-rm
title: FISCAL01-8007 DT Valor de Dedução ISS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=461920526
version: 3
---

# NFS-e Valor de Dedução ISS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | NFS-e \ Envio |
| **Situação/Requisito:** | Ao realizar a emissão de uma NFS-e, com 3 itens e um valor de dedução, o sistema está realizando o rateio da dedução para os 3 itens, gerando uma dízima periódica.  É apresentado a seguinte mensagem de erro:  ***Element 'valdedu': '574.69392257953239507385653146' is not a valid value of the atomic type '*** |
| **Solução/Implementação:** | O processo da NFS-e foi ajustado para que o valor da dedução seja corretamente arredondado quando o município não solicita o agrupamento dos serviços quando existir mais na mesma Nota. |
| **Documento relacionado:** | -- |
