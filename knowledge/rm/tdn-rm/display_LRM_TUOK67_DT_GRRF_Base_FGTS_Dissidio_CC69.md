---
content_hash: 4c33fbf2b48343de65f919621dfc3b68c8aca9e89cb0a518e62dba12588f4d46
fetched_at: '2026-06-29T00:08:03.914536+00:00'
page_id: '235329172'
product: rm
source: tdn-rm
title: TUOK67_DT_GRRF_Base_FGTS_Dissidio_CC69
type: documentation
url: https://tdn.totvs.com/display/LRM/TUOK67_DT_GRRF_Base_FGTS_Dissidio_CC69
version: 2
---

# BASE FGTS DISSIDIO DA GRRF NÃO ESTÁ LEVANDO VALOR DO CC69

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *GRRF* |
| **Situação/Requisito:** | *Ao gerar a GRRF por dissidio, no campo de Base FGTS Dissídio não está levando para sua composição o valor do evento de CC 69 - Base de FGTS de Diferença Salarial.*  *Desta forma ao gerar a guia da GRRF o valor fica incorreto.*  *O problema só ocorre quando o evento de Aviso Prévio indenizado, CC 62, não incide INSS.* |
| **Solução/Implementação:** | *Ajuste na geração da GRRF por dissídio, para abater o valor do CC 99 (Diferença de Aviso Prévio) no campo de Base FGTS Dissídio, somente se o evento de Aviso Prévio indenizado, CC 62, incidir INSS.* |
| **Chamados   relacionados:** | *TUOK67, TUPMQM* |
| **Versões/Release:** | *11.82.43, 12.1.11* |
