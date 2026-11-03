---
content_hash: cb85cd30d33a0138e8e669b26c033ad48334afe06e1d35ecc67d91f3abecea5e
fetched_at: '2026-06-29T00:09:45.856782+00:00'
page_id: '435097072'
product: rm
source: tdn-rm
title: 2647812  FISCAL01-5380 DT - NFS-e - Implementação do município de Cascavel-PR
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435097072
version: 1
---

# Implementação do município de Cascavel-PR

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Municípios Homologados |
| **Situação/Requisito:** | Solicitação da implementação do município de Cascavel - PR  No método cfgambnfse001 o RM está enviando o CNPJ que não é da filial (Aparentemente vinculado ao certificado) com isso a NFS-e é rejeitada pela Prefeitura com a seguinte mensagem:  Inscrição Municipal do prestador especificada no lote não confere com o prestador informado no RPS.  Realizando o teste via SoapUi, ao informar corretamente o cnpj da filial neste método a NFS-e foi autorizada com sucesso. |
| **Solução/Implementação:** | Implementação do envio, consulta e cancelamento para o município de Cascavel-PR.  Foi feita uma alteração para que o CNPJ do certificado digital seja enviado somente para municípios que são DSFNET. |
