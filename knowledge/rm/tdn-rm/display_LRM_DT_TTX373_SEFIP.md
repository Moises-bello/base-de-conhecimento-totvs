---
content_hash: 6c4fbd96eafda5625284fd25193d57acc0f36c9e84348839daf6b686230efbde
fetched_at: '2026-06-29T00:06:22.552274+00:00'
page_id: '223921427'
product: rm
source: tdn-rm
title: DT_TTX373_SEFIP
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_TTX373_SEFIP
version: 123
---

# SEFIP

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | Construção e projetos |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *SEFIP* |
| **Situação/Requisito:** | Ao gerar SEFIP da competência de Dezembro/2015 com código de recolhimento 115, 150, 155 (SEFIP da folha) para funcionários demitidos que já receberam o 13º salário, sistema está levando valor de dedução do 13º salário maternidade para o funcionário sendo que o mesmo que já teve a dedução na SEFIP de 13º.  Esta dedução é levada na parte de INSS do funcionário |
| **Solução/Implementação:** | Otimizado cálculo de dedução de 13 licença maternidade, adicionando validação do tipo de geração do SEFIP( sefip de 13 ou não), pois o cálculo de dedução estava sendo realizado sem considerar o tipo de geração, levando dedução do código de cálculo 322 (Segunda parcela 13 licença maternidade)  para o funcionário sendo que o mesmo que já teve a dedução na SEFIP de 13º |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTX373, TTZPIR |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.42 - 12.1.9* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** |  |

divs
