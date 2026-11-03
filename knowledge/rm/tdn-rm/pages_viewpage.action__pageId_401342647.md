---
content_hash: bf0c522457474632dedd84588d419956fdec738ce02b5f5232a5b82a59dbc4e2
fetched_at: '2026-06-29T00:09:10.586351+00:00'
page_id: '401342647'
product: rm
source: tdn-rm
title: 2886948 FISCAL01-4766 DT NFS-e Totvs Colaboração 2.0 - Geração da tag cresponsavelretencao
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=401342647
version: 3
---

# Geração da tag cresponsavelretencao

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Totvs Gestão Fiscal |
| **Função:** | Envio de NFS-e |
| **Situação/Requisito:** | NFS-e Totvs Colaboração 2.0 - Geração da tag cresponsavelretencao |
| **Solução/Implementação:** | Foi adicionado a TAG **cResponsavelRetencao** no grupo **identificacao** do XML da NFS-e de integração com o **TOTVS Colaboração** **2.0**.  A TAG será gerada somente em NFS-e cujo tipo de recolhimento esteja preenchido como "Retido na Fonte"  O valores aceitos para a TAG são:  1 – Tomador 2 – Intermediário  Nos casos em que a TAG for gerada será levado o valor fixo 1 - Tomador, pois no RM não temos o contexto de intermediário da NFS-e. |
