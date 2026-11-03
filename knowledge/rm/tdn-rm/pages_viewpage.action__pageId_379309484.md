---
content_hash: a0db3b341bf776dd5dc5d5eaafe5d1f7f5abd4d4e66de10c2045d6cb028b52dc
fetched_at: '2026-06-29T00:09:02.437113+00:00'
page_id: '379309484'
product: rm
source: tdn-rm
title: 1871434 FOPCALCULO01-2340 Relatório Comparativo SEFIP x Folha Analítica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=379309484
version: 1
---

# Comparativo SEFIP x Folha Analítica

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Comparativo SEFIP x Folha Analítica |
| **Situação/Requisito:** | Ao gerar a folha analítica para comparativo da SEFIP x Folha Analítica referente ao 13º salário, o arquivo "\_Net.txt" utilizado na rotina de comparativo não traz todos os campos conforme os valores dos eventos no envelope de pagamento do funcionário, gerando inconsistência indevida no relatório de comparativo SEFIP x Folha Analítica. |
| **Solução/Implementação:** | No Totvs Folha de Pagamento foi identificado que o comparativo SEFIP x Folha Analítica, o arquivo da folha analítica referente ao 13º salário não traz todos os campos, gerando divergência no relatório de comparação. Foi identificado e ajustado que o INSS sobre o 13º salário não era retornado no arquivo folha analítica causando assim a divergência. |
| **Tickets relacionados:** | 1871434 |
