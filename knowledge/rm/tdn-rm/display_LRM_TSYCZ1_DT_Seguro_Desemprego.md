---
content_hash: 6ef94cd84b7d43a792bfb644666f38b1d1d60d0e1a16c098759c4526631aad20
fetched_at: '2026-06-29T00:06:02.219080+00:00'
page_id: '198944786'
product: rm
source: tdn-rm
title: TSYCZ1_DT_Seguro_Desemprego
type: documentation
url: https://tdn.totvs.com/display/LRM/TSYCZ1_DT_Seguro_Desemprego
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
| **Chamados relacionados:** | TSYCZ1 |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.7* |
