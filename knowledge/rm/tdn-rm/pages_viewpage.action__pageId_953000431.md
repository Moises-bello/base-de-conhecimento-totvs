---
content_hash: a90b4c2e6428ba5db3d6f8bbe7512b7765f0357a376dc1e5c2ffe0e3dcb5a08e
fetched_at: '2026-06-29T00:12:10.231356+00:00'
page_id: '953000431'
product: rm
source: tdn-rm
title: Grupo GA – Autorização para Obter XML
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=953000431
version: 2
---

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Grupo GA – Autorização para Obter XML** | | | | | | | |
| **#** | **ID** | **Campo** | **Descrição** | **Observação** | **Campo de Origem** | **Campo na Aplicação** | **Mais Informações** |
| 97a.1 | G01 | autXML | Pessoas autorizadas a acessar o XML da NF-e |  |  |  |  |
| 97a.2 | G02 | CNPJ | CNPJ Autorizado | Informar CNPJ ou CPF. Preencher os zeros não significativos. | FCFO.CGCFO e TTRA.CGC | CNPJ/CPF da Filial ou Transportadora. | Serão levados os dados da transportadora, quando a mesma não for igual ao Cliente/Fornecedor. Para que seja possível enviar mais 5 CPF/CNPJ nesta tag, deve ser criado os campos complementares abaixo no movimento: CNPJCPF1, CNPJCPF2, CNPJCPF3, CNPJCPF4 e CNPJCPF5. |
| 97a.3 | G03 | CPF | CPF Autorizado | FCFO.CGCFO e TTRA.CGC |
