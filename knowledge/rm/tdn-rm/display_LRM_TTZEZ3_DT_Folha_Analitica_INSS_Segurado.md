---
content_hash: 9170ac985f8f537f6422f95fa18cabc3c4d7ee09f9aad9997a759449a3b40b3a
fetched_at: '2026-06-29T00:08:03.904038+00:00'
page_id: '235328913'
product: rm
source: tdn-rm
title: TTZEZ3_DT_Folha_Analitica_INSS_Segurado
type: documentation
url: https://tdn.totvs.com/display/LRM/TTZEZ3_DT_Folha_Analitica_INSS_Segurado
version: 115
---

# Folha Analítica

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projeto* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Calculo do valor do INSS Segurado* |
| **Situação/Requisito:** | O valor de INSS Segurado está sendo impresso com valor negativo quanto o valor de restituição de inss fica maior que os valores dedutíveis de INSS  a baixo um caso que esta condição pode vir a ocorrer:  Um funcionário recebeu Restituição de INSS na rescisão, e o valor da restituição é maior que o valor do CC3 do mês. Desta forma quando gera a Folha Analítica (Delphi) o campo INSS SEGURADO fica negativo.  O motivo para ter uma restituição de INSS, é pelo fato de no período 30 o funcionário ter recebido ter recebido 13º salario, e no período 75 ter sido demitido por Justa Causa (perdendo o direito ao 13º). O sistema desconta o decimo terceiro pago, e restitui INSS descontado. Como a demissão é no dia 9/12/15 o INSS do mês é baixo e a restituição fica superior. |
| **Solução/Implementação:** | O Valor de INSS Segurado na Folha Analítica será zerado automaticamente sempre que ficar negativo. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTZEZ3* |
| **Requisito (ISSUE):** |  |

divs
