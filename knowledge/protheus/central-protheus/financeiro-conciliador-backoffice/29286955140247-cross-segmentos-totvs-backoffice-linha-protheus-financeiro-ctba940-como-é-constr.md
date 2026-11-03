---
article_id: 29286955140247
category: Financeiro - Conciliador Backoffice
content_hash: a7c4f8440dcb2811c7bc74dedbcfb60f74673cb9cc9615a0e69974a5e9fea751
fetched_at: '2026-06-28T22:37:47.268306+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: Cross Segmentos - TOTVS BackOffice (Linha Protheus) - Financeiro - CTBA940
  - Como é construído o saldo bancário no Novo Conciliador BackOffice
type: support-article
updated_at: '2026-04-10T18:27:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29286955140247-Cross-Segmentos-TOTVS-BackOffice-Linha-Protheus-Financeiro-CTBA940-Como-%C3%A9-constru%C3%ADdo-o-saldo-banc%C3%A1rio-no-Novo-Conciliador-BackOffice
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29286931957655) Tempo aproximado para leitura: **00:10:00 min**  
  
**Dúvida**  
Como é construído o saldo bancário no Novo Conciliador BackOffice?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.33.

**Solução**

**SALDOS BANCÁRIOS**

Exibe tela para consulta da evolução dos saldos bancários durante o processo de conciliação, totalizando todos os registros com match para conciliação (todos os registros contidos em "Dados da Conciliação").

![](https://tdn.totvs.com/download/attachments/754621064/image-2024-12-9_14-16-54.png?version=1&modificationDate=1733764614763&api=v2)

* + Conciliador Backoffice e Reconciliação Bancária - FINA380**:**

    - Os totalizadores apresentados no **Conciliador Backoffice** são **análogos** aos totalizadoresapresentados na antiga rotina de **Reconciliação Bancária - FINA380**.

      | Saldo anterior (Bancário) | Saldo anterior (Bancário) |
      | Saldo anterior (Conciliação) | Saldo anterior (Conciliado) |
      | Valor Recebido | Total de entradas |
      | Valor Pago | Total de saídas |
      | Saldo Atual (Bancário) | Saldo atual (Bancário) |
      | Saldo Atual (Conciliação) | Saldo atual (Conciliado) |
      | Total Recebido | Valor Total Entradas-Geral (Este totalizador está presente no **rodapé** da tabela de conciliação na aba de **Dados não Encontrados**). |
      | Total Pago | Valor Total Saídas-Geral (Este totalizador está presente no **rodapé** da tabela de conciliação na aba de **Dados não Encontrados**). |
* + Definições dos totalizadores:
    - **Saldo anterior (Bancário)**: Refere-se ao **total geral** da conta bancária no **final do período imediatamente anterior** ao intervalo de conciliação atual. Este saldo inclui tanto as transações **conciliadas quanto as não conciliadas** até o final do período anterior, representando o valor total da conta bancária nesse período.
  + - **Saldo anterior (Conciliado)**: Refere-se ao valor total das transações que **foram reconciliadas** até o final do período anterior (antes do início do intervalo de conciliação atual). Esse saldo representa o valor das transações **conciliadas** no sistema ERP até o último dia do período anterior, sem incluir as transações **não conciliadas**.
  + - **Total de entradas: representa** o valor total das transações de **entradas de dinheiro** que o usuário **selecionou para conciliação** (efetuou a operação de pré-conciliação do registro migrando o mesmo para aba de Dados da Conciliação) durante o processo. Esse totalizador corresponde aos **valores recebidos** registrados no ERP e que o usuário efetuou a pré-conciliação.
  + - **Total de saídas: representa** o valor total das transações de **saídas de dinheiro** que o usuário **selecionou para conciliação** (efetuou a operação de pré-conciliação do registro migrando o mesmo para aba de Dados da Conciliação) durante o processo. Esse totalizador corresponde aos**pagamentos efetuados** que foram registrados no ERP e que o usuário efetuou a pré-conciliação.
  + - **Saldo atual (Bancário)**: Representa o **total geral** da conta bancária, incluindo tanto as transações **conciliadas** quanto as **não conciliadas**. Este saldo é uma **somatória do Saldo anterior (Bancário)** com o **Total de entradas**e**Total de saídas**.
  + - **Saldo atual (Conciliado)**: Refere-se ao valor total das transações que já foram **efetivamente reconciliadas** entre o sistema ERP e o extrato bancário até o final do período selecionado. Este saldo **considera apenas as transações conciliadas** pelo sistema, ou seja, as entradas e saídas que já foram verificadas e associadas corretamente com os dados do banco.

**Exemplo de aplicação dos conceitos**:

Exemplo considerando os períodos de novembro e dezembro de 2024

**Saiba mais**

[Conciliador BackOffice - Conciliação Bancária Manual](https://tdn.totvs.com/pages/releaseview.action?pageId=754621064)  
[Conciliadores Bancários Manual e Automático (FINA380 e FINA473)](https://tdn.totvs.com/pages/releaseview.action?pageId=754946735)  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Como é mostrado o saldos no novo conciliador financeiro na opção processo 0024](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28647651562519-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Como-%C3%A9-mostrado-o-saldos-no-novo-conciliador-financeiro-na-op%C3%A7%C3%A3o-processo-0024)
