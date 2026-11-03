---
article_id: 37508801432727
category: Folha Mensal
content_hash: 45d8e6821f16dc30664f61af97253f7509bc132ca5f17ebd4797ea64e8d8a7a5
fetched_at: '2026-06-28T22:46:58.008001+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Crédito do Trabalhador: Quais verbas não são consideradas
  na Base Remuneração?'
type: support-article
updated_at: '2026-01-07T18:28:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37508801432727-RH-RM-FOP-Cr%C3%A9dito-do-Trabalhador-Quais-verbas-n%C3%A3o-s%C3%A3o-consideradas-na-Base-Remunera%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37508801399319) Tempo aproximado para leitura: 00:01:16 min

**Dúvida**  
No módulo RM Folha, ao tentar realizar o cálculo da margem consignável, o sistema não considera o evento de código de cálculo 35 - Adiantamentos 13º Salário para a base de cálculo do empréstimo. Quais são os eventos que não não considerados na Base Remuneração conforme manual do governo? 

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos patches:

12.1.2406.277

12.1.2410.229

12.1.2502.145

12.1.2506 e superiores

**Causa**  
Esse incidente ocorre, pois o evento de adiantamento de 13º salário não deve ser considerado no cálculo da margem consignável, assim como outros verbas listadas, segundo as diretrizes do manual governamental, que orienta que tais eventos não devem ser inclusos na remuneração para o empréstimo. 

**Solução**  
Esse comportamento está correto e ocorre de forma intencional, conforme as diretrizes do Manual de Consignações do Governo Federal.

Determinadas rubricas não devem compor a Base de Remuneração utilizada para o cálculo da margem consignável, pois não possuem caráter permanente, representam adiantamentos, verbas indenizatórias, benefícios ou descontos que não integram a remuneração base para fins de empréstimo consignado.

Dessa forma, o evento 35 – Adiantamento de 13º Salário não é considerado no cálculo da margem consignável, assim como as demais rubricas listadas abaixo:

| Nome da rubrica | Natureza – Tabela 03 eSocial |
| --- | --- |
| Luvas e premiações | 1007 |
| Férias – Abono ou gratificação de férias não excedente a 20 dias (art. 144 da CLT) | 1022 |
| Férias – Abono pecuniário | 1023 |
| Férias – Dobro na vigência do contrato | 1024 |
| PLR – Participação nos Lucros ou Resultados | 1300 |
| Abono | 1401 |
| Auxílio babá | 1404 |
| Assistência médica | 1405 |
| Auxílio-creche | 1406 |
| Salário-família | 1409 |
| Ajuda de custo de transferência | 1602 |
| Ajuda de custo | 1603 |
| Ressarcimento de provisão | 1623 |
| Ressarcimento de outras despesas | 1629 |
| Diárias de viagem | 1650 |
| Moradia | 1805 |
| Alimentação em ticket ou cartão, vinculada ao PAT | 1806 |
| Alimentação em ticket ou cartão, não vinculada ao PAT | 1807 |
| Cesta básica ou refeição, vinculada ao PAT | 1808 |
| Cesta básica ou refeição, não vinculada ao PAT | 1809 |
| Transporte | 1810 |
| Prêmios | 2501 |
| Direitos autorais e intelectuais | 2510 |
| Complementação salarial de auxílio-doença (desde que extensivo a todos os funcionários) | 4010 |
| Salário-maternidade – 13º salário (lançado na folha anual) | 4051 |
| 13º salário (lançado na folha anual) | 5001 |
| 13º salário – Adiantamento | 5504 |
| Indenização compensatória do aviso prévio (API) | 6003 |
| Férias – Dobro na rescisão | 6004 |
| Férias proporcionais (na rescisão) | 6006 |
| Férias vencidas na rescisão | 6007 |
| Indenização do art. 9º da Lei 7.238/1984 | 6102 |
| Indenização do art. 14 da Lei 5.889/1973 | 6103 |
| Indenização do art. 479 da CLT | 6104 |
| Indenização recebida a título de incentivo à demissão | 6105 |
| Multa do art. 477 da CLT | 6106 |
| Desconto de adiantamentos | 9200 |
| Provisão de contribuição previdenciária | 9205 |
| 13º salário – Desconto de adiantamento (lançado na folha anual) | 9214 |
| Desconto de vale-transporte | 9216 |
| Desconto de assistência médica ou odontológica | 9219 |
| Desconto de férias | 9221 |
| Previdência complementar – Parte do empregado | 9223 |
| Alimentação em ticket ou cartão, vinculada ao PAT – Desconto | 9241 |
| Alimentação em ticket ou cartão, não vinculada ao PAT – Desconto | 9242 |
| Cesta básica ou refeição, vinculada ao PAT – Desconto | 9243 |
| Cesta básica ou refeição, não vinculada ao PAT – Desconto | 9244 |
| Seguro de vida – Desconto | 9250 |
| Empréstimos consignados – Desconto | 9254 |
| Convênios | 9258 |
| Salário-maternidade pago pela Previdência Social | 9930 |
| Salário-maternidade pago pela Previdência Social – 13º salário | 9931 |
| Auxílio-doença acidentário | 9932 |

**SAIBA MAIS:**  
  
[MANUAL DE ORIENTAÇÃO DO EMPREGADOR](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica-old/manual-operacional-do-empregador-programa-credito-do-trabalhador-v2-16-05-25.pdf)  
[RH - RM - FOP - Dúvidas frequentes: Crédito do Trabalhador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33227187529495-RH-RM-FOP-D%C3%BAvidas-frequentes-Cr%C3%A9dito-do-Trabalhador)
