---
content_hash: 1533933fd1284ff0988ce789241dcd10134d03abee6c94970f3852ae03c828e5
fetched_at: '2026-06-29T00:06:02.198356+00:00'
page_id: '198944370'
product: rm
source: tdn-rm
title: TSVTF5_DT_Seguro_Desemprego
type: documentation
url: https://tdn.totvs.com/display/LRM/TSVTF5_DT_Seguro_Desemprego
version: 1
---

# SEGURO DESEMPREGO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *Relatório de seguro desemprego* |
| **Situação/Requisito:** | Ao gerar o relatório de "Seguro Desemprego" para funcionários que possuem a rescisão cadastrada para uma competência futura, o sistema retorna o valor do SALARIO do funcionário sem o cálculo das verbas rescisórias. |
| **Solução/Implementação:** | Otimizado relatório de seguro desemprego, alterada regra para calcular as verbas rescisórias de demissão próximo mês, verificando se o funcionário está ativo ou se a rescisão está calculada |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TSVTF5 |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.40* |
