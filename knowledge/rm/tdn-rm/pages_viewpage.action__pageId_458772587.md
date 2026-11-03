---
content_hash: d24aa6c28694c6599f74269b7800a0010b4609f8ddd6ef77820818f23137e920
fetched_at: '2026-06-29T00:10:13.962087+00:00'
page_id: '458772587'
product: rm
source: tdn-rm
title: 4841021 FISCAL01-8065 DT NFS-e - Itajaí-SC - Não autoriza NF com cliente do
  exterior
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=458772587
version: 3
---

# Envio de NFS-e

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Envio da NFS-e |
| **Situação/Requisito:** | A NFS-e está sendo rejeitada quando o cliente é do exterior, ocorre a rejeição abaixo:  Identificador do Movimento: 5093 RETRANSMITA O ID :'999984907' E284 - Pais da prestação do serviço invalido. Informe o código do pais onde foi prestado o serviço conforme consta da Tabela de Paises do BACEN. |
| **Solução/Implementação:** | Efetuado o ajuste para o município de Itajaí no grupo PRESTAÇÃO para enviar a tag CODPAIS e preencher a tag CODMUNIBGE no grupo do TOMADOR com o valor 9999999. |
