---
article_id: 360062163014
category: Escrita Fiscal - Impostos - IR
content_hash: 5d18a2645dc8e541eafe8ac2a2ee844c1c59ade2e8c25955642eebe232df481b
fetched_at: '2026-06-28T22:39:31.943086+00:00'
product: protheus
section_id: 1500001549802
source: central-protheus
title: MP - FIS - Como fazer o Cálculo de IRRF - Tabela Progressiva
type: support-article
updated_at: '2024-09-19T19:24:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062163014-MP-FIS-Como-fazer-o-C%C3%A1lculo-de-IRRF-Tabela-Progressiva
---

**Dúvida**

Como fazer o Cálculo de IRRF - Tabela Progressiva?

**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

**Processo a ser executado:**

No **Configurador,** acesse **AMBIENTE\ CADASTROS\ TABELA IRRF**e preencha a Tabela conforme abaixo:

Tabela IRRF 2021

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003738422)

***Obs.: Acima de 4664,68 informe 999999999.99.***

**No cadastro de Natureza, preencha os campos:**

**Calcula IRRF (ED\_CALCIRRF)** = Sim

**Perc. IRRF (ED\_PERCIRRF)** = informar %

A natureza deve ser amarrada ao cadastro do cliente **(A1\_NATUREZ)** e ao cadastro do Fornecedor **(A2\_NATUREZ)**ou ser informada direto no pedido de venda/compra.

**No cadastro de Cliente preencha os campos:**

**Natureza (A1\_NATUREZ)** - Opcional;

**CNPJ/CPF (A1\_CGC)** - Verifique se está preenchido. O Sistema não calcula se o CNPJ ou CPF do responsável não estiver preenchido;

**Modo Abatimento do Imposto (A1\_ABATIMP)** = Calculado pelo Sistema;

**Vlr. Min. IR (A1\_MINIRF)** = Considera ou não o parâmetro **MV\_VLRETIR**, que limita um valor mínimo de retenção de IRRF. Se informado **1 = Sim,** o Sistema não considera o parâmetro. Se informado **2 = Não**,esse parâmetro será considerado, permanecendo o valor mínimo nele definido.

**No cadastro de Fornecedor preencha os campos:**

**Natureza (A2\_NATUREZ)** – Opcional;

**CNPJ/CPF (A2\_CGC)** - Verifique se está preenchido. O Sistema não calcula se o CNPJ ou CPF do responsável não estiver preenchido;

**Vlr. Min. IR (A2\_MINIRF)** - Considera ou não o parâmetro **MV\_VLRETIR**, que limita um valor mínimo de retenção de IRRF. Se informado **1 = Sim**, o Sistema não considera o parâmetro. Se informado **2 = Não,** o Sistema considera esse parâmetro, permanecendo o valor mínimo nele definido.

**Cálculo IRRF (A2\_CALCIRF)** = Normal

**IRRF Prog (A2\_IRPROG)** = SIM (Pessoa Física)

Obs.: caso seja necessário incluir dependentes, só será possível incluir por meio do **Financeiro**. Neste módulo, informe o cadastro de fornecedores e será apresentada a aba **TMS**. Nesta, o campo **dependente**deve ser preenchido somente com o número de dependentes, para que o Sistema efetue o cálculo deduzindo a quantidade.

**No cadastro de Produtos preencha os campos:**

**Calcula IRRF (B1\_IRRF)** = Sim;

**Redução de IRRF (B1\_REDIRRF)** - preencha caso haja redução de IR;

Assuntos relacionados:

[MP - FIS - Como efetuar a retenção do IRRF no Contas a Pagar do Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003545201-MP-FIS-Como-efetuar-a-reten%C3%A7%C3%A3o-do-IRRF-no-Contas-a-Pagar-do-Protheus-)
