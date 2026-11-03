---
content_hash: d04511a8e945f0032ca705ea8df30e6c71f06732b8a0392d6df3316a9c254a58
fetched_at: '2026-06-29T00:06:05.625657+00:00'
page_id: '201725915'
product: rm
source: tdn-rm
title: TSZFI5_DT_Lancamento_Financeiro_Pensao_Ferias_Rescisao
type: documentation
url: https://tdn.totvs.com/display/LRM/TSZFI5_DT_Lancamento_Financeiro_Pensao_Ferias_Rescisao
version: 1
---

# LANÇAMENTO FINANCEIRO DE PENSÃO DE FÉRIAS NA RESCISÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Lançamento Financeiro* |
| **Situação/Requisito:** | *Ao gerar lançamento financeiro do tipo 14 – Total de pensão, não está sendo considerando o evento de código de cálculo 319 - Pensão alimentícia férias na rescisão, para o cálculo do valor do lançamento.* |
| **Solução/Implementação:** | *Existem 2 códigos de cálculo de Pensão nas Férias. Um para o cálculo de férias normais, e outro para as férias na rescisão. No lançamento financeiro está considerando somente o CC de pensão nas férias normais.*  *Deverá ser tratado no processo de Lançamento Financeiro para considerar o CC 319 - Pensão alimentícia férias na rescisão, no lançamentos de "Total de Pensão" e "Pensão de Férias".* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TSZFI5* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.7* |
