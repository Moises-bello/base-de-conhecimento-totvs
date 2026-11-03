---
content_hash: 3bb2cc2b4460e8e995a7bf8211faee94a471eaf432d64be1b66ee27eb7f50c98
fetched_at: '2026-06-29T00:09:01.599180+00:00'
page_id: '374310303'
product: rm
source: tdn-rm
title: 3091022 FINANCEIRO01-7597 DT Valores tributos contabilização borderô
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=374310303
version: 1
---

# Valores dos tributos não carregados na contabilização quando emite borderô.

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Baixa Contábil |
| **Situação/Requisito:** | Ao realizar a baixa contábil de um lançamento que possui borderô remetido e o lançamento possui valores de INSS, IRRF e SEST/SENAT, o sistema não carrega os valores com as funções de fórmula.  Exemplo: TABLANBAIXA('VALORIRRF','V') |
| **Solução/Implementação:** | Ajuste realizado na geração de item de baixa para carregar os valores dos tributos para a contabilização da baixa enquanto o processo de baixa está sendo realizado manualmente. |
| **Requisito:** | FIN000040 |
