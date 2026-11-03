---
content_hash: 7bd0fff67004d924759558f3d026d086ef5291229193d684ef032e5f5f21a24e
fetched_at: '2026-06-29T00:06:06.065926+00:00'
page_id: '201728099'
product: rm
source: tdn-rm
title: RMFIS00005_12.005 - Registro Y540 - Discriminação da Receita de Vendas dos
  Estabelecimentos por Atividade Econômica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201728099
version: 2
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                      **Versão: 11.82.40 e superiores** |
| **Processo** | **:** | ECF - Escrituração Contábil Fiscal |
| **Subprocesso** | **:** | ECF - Escrituração Contábil Fiscal |
| **Data da publicação** | **:** | 10/09/2015 |

Este registro será gerado para todas as pessoas jurídicas, para discriminação da receita de vendas dos estabelecimentos por atividade econômica, quando for o caso.

A saída deste registro irá ocorrer de forma automática e conforme as parametrizações da ECF do módulo TOTVS Gestão Fiscal as quais passamos a detalhar. Será gerado um registro Y540 para cada Filial que não seja SCP.

**Regra de preenchimento dos campos do Registro:**

**Campo 2 - CNPJ\_ESTAB**

Informação proveniente do módulo TOTVS Gestão Fiscal do cadastro de Filial

**Campo 3 - VL\_REC\_ESTAB**

Para processar o valor da receita, será aplicada a regra definida no Manual da ECF, que é baseada nas contas do Plano de Contas Referencial (Plano de Contas Paralelo). O sistema irá processar o valor da movimentação (conforme a Filial) da conta contábil associada a conta paralela que faz parte da regra, que passamos a detalhar.

Observações:

* As contas que irão fazer parte da regra abaixo sempre serão contas paralelas, para efeito de validação deverão ser analisadas as movimentações das contas contábeis associadas à conta paralela destacada na regra.
* Serão processadas as movimentações correspondentes ao período da regra (Trimestre ou Ano)

|  |  |  |
| --- | --- | --- |
| **#** | **Quando?** | **Qual expressão e conta paralela deve ser aplicada?**  ***Considera a movimentação das contas contábeis associadas a conta paralela destacada abaixo*** |
| **1** | Quando a Qualificação da PJ for “**PJ em Geral**” E a Forma de Tributação for “**Lucro Real**” E a Forma de Apuração for “**Trimestral**” | 3.01.01.01.01 – 3.01.01.01.02.01 – 3.01.01.01.02.02 +   3.11.01.01.01 – 3.11.01.01.02.01 –     3.11.01.01.02.02 |
| **2** | Quando a Qualificação da PJ for “**PJ em Geral**” E a Forma de Tributação for “**Lucro Real**” E a Forma de Apuração for “**Anual**” | 3.01.01.01.01 – 3.01.01.01.02.01 – 3.01.01.01.02.02 + 3.11.01.01.01 – 3.11.01.01.02.01 –   3.11.01.01.02.02 |
| **3** | Quando a Forma de Tributação for “**Lucro Presumido**” E a empresa possuir Isenção e Redução do Imposto (0020.IND\_RED\_ISEN = S) | De acordo com o Manual, essas informações devem vir da apuração do tributo. Como a apuração do tributo é realizada de forma centralizada pela Matriz, quando ocorrer esta combinação, será apresentada a seguinte mensagem no Log da ECF:  *“Não foi possível gerar o registro Y540 porque toda a receita da empresa foi armazenada agrupada na Matriz no momento do encerramento do período e as informações devem ser prestadas por Estabelecimento. Esse registro deve ser informado diretamente no PVA.”* |
| **4** | Forma de Tributação for “**Lucro Presumido**” E a empresa NÃO possuir Isenção e Redução do Imposto (0020.IND\_RED\_ISEN = N) | 3.01.01.01.01 – 3.01.01.01.02.01 – 3.01.01.01.02.02 +  3.11.01.01.01  – 3.11.01.01.02.01 – 3.11.01.01.02.02 |
| **5** | Quando a Forma de Tributação for “**Lucro Arbitrado**” | De acordo com o Manual, essas informações devem vir da apuração do tributo. Como a apuração do tributo é realizada de forma centralizada pela Matriz, quando ocorrer esta combinação será apresentada a seguinte mensagem no Log da ECF:  *“Não foi possível gerar o registro Y540 porque toda a receita da empresa foi armazenada agrupada na Matriz no momento do encerramento do período e as informações devem ser prestadas por Estabelecimento. Esse registro deve ser informado diretamente no PVA.”* |
| **6** | Quando a Qualificação da PJ for “**PJ Componente do Sistema Financeiro**” E a Forma de Tributação for “**Lucro Real**” E a Forma de Apuração for “**Trimestral**” | 3.1.7.1.0.00.00 |
| **7** | Quando a Qualificação da PJ for “**PJ Componente do Sistema Financeiro**” E a Forma de Tributação for “**Lucro Real**” E a Forma de Apuração for “**Anual**” | 3.1.7.1.0.00.00 |
| **8** | Quando a Qualificação da PJ for “**Sociedades Seguradoras, de Capitalização ou Entidade Aberta de Previdência Complementar**” E a Forma de Tributação for “**Lucro Real**” E a Forma de Apuração for “**Trimestral**” | 3.01.01.01.01.01 + 3.01.01.01.01.02 |
| **9** | Quando a Qualificação da PJ for “**Sociedades Seguradoras, de Capitalização ou Entidade Aberta de Previdência Complementar**” E a Forma de Tributação for “**Lucro Real**” E a Forma de Apuração for “**Anual**” | 3.01.01.01.01.01 + 3.01.01.01.01.02 |

**Como a movimentação da conta contábil associada a conta paralela será processada?**

Exemplo:

Vamos considerar que estamos aplicando a regra 6 acima, que deverá considerar os valores das contas contábeis associada a conta paralela 3.1.7.1.0.00.00.

|  |  |  |  |
| --- | --- | --- | --- |
| **Conta Contábil Associada** | **Total Crédito** | **Total Débito** | **Movimento** |
| 3.1.01.01 | 1.000.00 (C) | 500,00 (D) | 500,00 (C) |
| 3.1.01.02 | 800,00 (C) | 400,00 (D) | 400,00 (C) |
| 3.1.01.03 | 100,00 (C) | 600,00 (D) | 500,00 (D) |
| **Movimentação Total** | | | **400,00 (C)** |

Será considerado para o campo “VL\_REC\_ESTAB” o valor de **400,00**.

Se o valor processado for “**devedor**” (menor que zero), será considerado para o campo “VL\_REC\_ESTAB” o valor de “0,00”, pois entendemos que as regras são baseadas em contas de receita que possuem a natureza “**credora**”.

**Campo 4 – CNAE**

Informação proveniente do módulo TOTVS Gestão Fiscal do cadastro de Filial.
