---
content_hash: d6a299b5aad43a5a9307fc5f88fd03222e81f7ce4934623a917abdcac70b812f
fetched_at: '2026-06-29T00:09:54.833902+00:00'
page_id: '445648471'
product: rm
source: tdn-rm
title: 4577297 FISCAL01-7431 DT - NF-e - Zerar a Base de Cálculo do ICMS para operação
  Complementar e com CST 90
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=445648471
version: 2
---

# NF-e - Zerar a Base de Cálculo do ICMS para operação Complementar e com CST 90

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Envio de NF-e |
| **Situação/Requisito:** | Autorizar NF-e Complementar com Base de Cálculo e Alíquota de ICMS Zeradas e CST 90. |
| **Solução/Implementação:** | O Envio de NF-e foi alterado para manter a compatibilidade com o envio na versão 3.10 e Layout TSS: Caso o CST seja 90, a Natureza Complementar e a Alíquota Zerada, a TAG de Base de Cálculo será enviada com 0 (zero) caso não esteja preenchida, ao invés de não não ser gerada no XML. |
