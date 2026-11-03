---
content_hash: 934fcf8d685b131a0013c1244cbb5bffbec6dcf4acf76fb317621a652f4ec613
fetched_at: '2026-06-29T00:09:58.189016+00:00'
page_id: '451268432'
product: rm
source: tdn-rm
title: 4190537 - FISCAL01-7125 - DT NFS-e São Paulo - CPF estrangeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=451268432
version: 1
---

# Cancelamento da NFS-e

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Envio NFS-e |
| **Situação/Requisito:** | O processo de NFS-e deverá considerar como estrangeiro qualquer cliente/fornecedor (pessoa física) que esteja com o campo Nacionalidade do cadastro do cliente fornecedor definido como Estrangeira. |
| **Solução/Implementação:** | Incluída condição onde vai ser verificado se o Cli\for é estrangeiro. Atualmente o sistema já verifica se o Estado é Nacional, agora vão ser feitas as duas verificações. |
| **Requisito:** | FIS000251 |
