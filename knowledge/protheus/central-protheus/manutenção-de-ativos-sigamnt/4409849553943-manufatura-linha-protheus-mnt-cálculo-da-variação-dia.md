---
article_id: 4409849553943
category: Manutenção de Ativos (SIGAMNT)
content_hash: adac9c2da6f615a4029d5d9b16a302bc0b0c7945408d5998195db28e949ef8c1
fetched_at: '2026-06-28T22:42:32.844683+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Cálculo da Variação dia
type: support-article
updated_at: '2021-10-04T12:35:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409849553943-Manufatura-Linha-Protheus-MNT-C%C3%A1lculo-da-Varia%C3%A7%C3%A3o-dia
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como é calculada a **T9\_VARDIA - Variação Dia** no **SIGAMNT -** **Manutenção de Ativos**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**A **Variação Dia** que está cadastrada no **Bem**, é calculada a **cada reporte de contador**, seja **O.S. - Ordem de serviço**, abastecimento, pneus ou finalização de **O.S.** Sempre que o contador é informado, o Sistema recalcula a variação dia e atualiza o campo **Variação Dia** no cadastro do **Bem**.  
**Dois parâmetros** são **fundamentais** para o cálculo da variação dia:

* **MV\_NGPRVDI - Percentual de variação da variação dia**: que define o percentual de modificação da **Variação dia** atual em relação à anterior, para apresentar a mensagem de alerta ao usuário. Normalmente este parâmetro está com o conteúdo igual a 10, o que significa que pode haver uma variação de até **10%** entre a variação anteriormente cadastrada e a que está sendo calculado no reporte do contador.
* **MV\_VARDIA** - **Define quantos registros para trás será obtido no histórico de contador para servir de base para o cálculo da variação dia**. Normalmente este parâmetro está com 10, o que significa que o programa irá buscar o **décimo registro anterior** ao que está sendo calculado. Digamos que o décimo registro refere-se a um apontamento de **contador do dia 01/05/2021** e cujo contador nesta data estava com **10.000**.  
  O apontamento que está sendo realizado no dia **31/05/2021** com a informação do contador como **12.000**.

Para o cálculo da variação dia, o Sistema irá calcular primeiramente o número de dias decorrido entre **31/05/2021** e **01/05/2021** que são **30 dias.**Em seguida será calculada a **quilometragem percorrida (12.000 – 10000) = 2.000**, com os cálculos necessários em mãos, basta fazer o cálculo abaixo:

|  |  |
| --- | --- |
| **1 - Km Percorrido** | 2.000 |
| **2 - Dias Corridos** | 30 |
| **Variação Dia** | 1 / 2 = 67 K |
