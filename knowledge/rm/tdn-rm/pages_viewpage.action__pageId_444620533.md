---
content_hash: 30f0cc9bff855d0db56c3a76bda6232a9d42df25393d580a8e03c6aa27ac546e
fetched_at: '2026-06-29T00:09:54.444269+00:00'
page_id: '444620533'
product: rm
source: tdn-rm
title: 4447447 FISCAL01-7300 DT - EFD Contribuições - Chave NF-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=444620533
version: 2
---

# EFD Contribuições

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Geração de Arquivos EFD Contribuições |
| **Situação/Requisito:** | Não está sendo gerado no arquivo txt da rotina EFD, a informação no campo 9 CHV\_NFSE (Chave/Código de Verificação da nota fiscal de serviço eletrônica), do registro A100, rotina EFD Contribuições. |
| **Solução/Implementação:** | Na geração da EFD contribuições o lançamento fiscal de serviço quando não possuir informação de chave de acesso, será verificado se o movimento de pedido está vinculado a NFS-e para buscar os dados necessários no registro A100.  Quando não são encontradas informações de chave de acesso através dos cadastros de documentos eletrônicos, será considerado o valor presente no Lançamento Fiscal na Aba Outros\Chave Acesso (NF-e, NFS-e, NFC-e, CT-e). |
