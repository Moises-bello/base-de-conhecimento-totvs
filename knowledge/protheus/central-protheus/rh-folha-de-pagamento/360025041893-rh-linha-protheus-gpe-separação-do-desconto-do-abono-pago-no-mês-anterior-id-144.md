---
article_id: 360025041893
category: RH - Folha de Pagamento
content_hash: 8ae2179c7a530077f552c18d29b74537e0e11f6b9fdb06531601cabd859fd0ff
fetched_at: '2026-06-28T22:44:16.326766+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Separação do Desconto do Abono Pago no Mês Anterior
  (ID 1449)
type: support-article
updated_at: '2024-09-10T19:03:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025041893-RH-Linha-Protheus-GPE-Separa%C3%A7%C3%A3o-do-Desconto-do-Abono-Pago-no-M%C3%AAs-Anterior-ID-1449
---

![relogio_tempo_leitura_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26278418766487) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Separação do Desconto do Abono Pago no Mês Anterior (ID 1449)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

Ajuste para efetuar separação do desconto do abono que foi pago no mês anterior:

Dessa forma, os valores de desconto de férias e abono serão gerados em dois Ids:

- ID de cálculo **0164 - Ferias Pagas Mes Anterior**: irá conter o desconto dos valores de férias que foram pagas no mês anterior, obtido pelas verbas configuradas com o campo **RV\_REFFER** preenchido com **S** **(Sim)** e que não sejam referente aos Id's **0205, 0206, 0207, 0208, 0633, 0634, 0635, 1313, 1315, 1317, 1319, 1321, 1323, 1325, 1327, 1409, 1410, 1418 e 1419**;

- ID de cálculo **1449 - Abonos Pagos Mes Anterior**: irá conter o desconto dos valores de abono que foram pagos no mês anterior, obtido através das verbas configuradas com o campo **RV\_REFFER** preenchido **S** **(Sim)** e referentes aos Ids de cálculo **0205, 0206, 0207, 0208, 0633, 0634, 0635, 1313, 1315, 1317, 1319, 1321, 1323, 1325, 1327, 1409, 1410, 1418 e 1419** ou das verbas com o campo **RV\_REFFER** preenchido com **S** **(Sim)** e **RV\_REFABON** preenchido com **1** **(Sim)**. Para facilitar o cadastro, copiar a configuração da verba de ID de cálculo **0164**, mas **retirar a incidência para tributação (INSS, IR e FGTS).**  
  
**Importante**Será obrigatório efetuar o cadastro da verba do ID 1449 para efetuar o fechamento do período, pois o valor do desconto do abono deverá ser gerado para o próximo período.  
Para explicar a diferença do conceito do sistema após a criação do ID 1449, **verificar o exemplo abaixo:**

Funcionário com salário de R$ 2.400,00, com férias de 20 dias e 10 de abono iniciados em 16/04/2018 e as verbas de provento e desconto abaixo:

| Verba | Descrição | Valor |
| --- | --- | --- |
| 129 (Id 0072) | Férias Mês | R$ 1.200,00 |
| 130 (Id 0073) | Férias Mês Seguinte | R$ 400,00 |
| 134 (Id 0077) | 1/3 Sobre Férias Mês | R$ 400,00 |
| 135 (Id 0078) | 1/3 Sobre Férias Mês Seguinte | R$ 133,33 |
| 186 (Id 0205) | Abono Pecuniário Mês Seguinte | R$ 800.00 |
| 187 (Id 0206) | 1/3 Sobre Abono Pecuniário Mês Seguinte | R$ 266,67 |
| 418 (Id 0065) | INSS Férias Mês | R$ 128,00 |
| 501 (Id 0232) | INSS Férias Mês Seguinte | R$ 128,00 |

Ao realizar o fechamento do período, o sistema irá transportar as verbas de férias e abono do mês seguinte para o próximo período como verbas de férias e abono do mês e irá gerar verba de desconto para zerar o líquido dessas verbas.

As verbas de férias e abono que foram geradas para o próximo período são:

| Verba | Descrição | Valor |
| --- | --- | --- |
| 129 (Id 0072) | Férias Mês Seguinte | R$ 400,00 |
| 134 (Id 0077) | 1/3 Sobre Férias Mês | R$ 133,33 |
| 184 (Id 0074) | Abono Pecuniário Mês | R$ 800,00 |
| 185 (Id 0079) | 1/3 Sobre Abono Pecuniário Mês | R$ 266,67 |
| 418 (Id 0065) | INSS Férias Mês | R$ 128,00 |

Antes da criação do Id 1449, o sistema iria efetuar a geração do desconto de férias e abono aglutinados na mesma verba:

| Verba | Descrição | Valor |
| --- | --- | --- |
| 433 (Id 0164) | Férias Pagas Mês Anterior | R$ 1.472,00 |

Após a criação do Id 1449, o sistema irá separar o desconto de férias e o desconto do abono em duas verbas:

| Verba | Descrição | Valor |
| --- | --- | --- |
| 433 (Id 0164) | Férias Pagas Mês Anterior | R$ 405,33 |
| 434 (Id 1449) | Abonos Pagos Mês Anterior | R$ 1.066,67 |

**Saiba mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
