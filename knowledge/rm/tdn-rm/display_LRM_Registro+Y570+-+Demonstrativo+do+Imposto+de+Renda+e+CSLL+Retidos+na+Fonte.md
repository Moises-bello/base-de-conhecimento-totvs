---
content_hash: a8574ae9b2418027529905d7c7226c8e73839fae3885b388f8fa52507251b2cb
fetched_at: '2026-06-29T00:09:23.831588+00:00'
page_id: '422546142'
product: rm
source: tdn-rm
title: Registro Y570 - Demonstrativo do Imposto de Renda e CSLL Retidos na Fonte
type: documentation
url: https://tdn.totvs.com/display/LRM/Registro+Y570+-+Demonstrativo+do+Imposto+de+Renda+e+CSLL+Retidos+na+Fonte
version: 9
---

#### **1.****Origem Fiscal**

#### **2. Origem Fluxus x Nucleus**

#### **3. Origem Aplicação Financeira**

Para a geração deste registro serão selecionados lançamentos de todas as Filiais que possuam CNPJ com a mesma raiz da Filial Matriz. Lançamentos das SCP não serão selecionados.

#### **1. Origem Fiscal** **Para lançamentos originados no TOTVS Gestão Fiscal devem ser observados os seguintes pontos:**

* Lançamentos Fiscais de Saída
* Data do Lançamento Fiscal (DATA.DATALF) esteja compreendida no período de geração da ECF
* Lançamentos Cancelados ou Estornados não serão carregados no processo.
* Os Tributos IRRF-PJ, IRRF e CSLL-RF devem estar gravados na pasta Outros Tributos do Lançamento Fiscal.

#### **2. Origem Fluxus x Nucleus** **Para Lançamentos originados no TOTVS Gestão Financeira devem ser observados os seguintes pontos:**

* Nos parâmetros da ECF deve-se marcar a opção **"Carregar Retenções do Fluxus - Registro Y570"**
* Lançamentos Fiscais de Saída que possuem o Tributo IRRF-PJ continuaram sendo carregados do TOTVS Gestão Fiscal
* As retenções de IRRF e CSLL serão carregadas de:  
                  a) Lançamentos Fiscais  de Saída que estejam vinculados a Lançamento Financeiro e a data de baixa deste esteja dentro do período de geração da ECF.  
                  b) Lançamentos Fiscais de Saída proveniente do TOTVS Gestão de Compras, cujo movimento tenha gerado Lançamento Financeiro e este último tenha data de baixa dentro do período de geração da ECF.  
                  c) Neste caso o valor das retenções serão carregados do TOTVS Gestão Financeira. A CSLL da tabela FTRBLAN e o IRRF da tabela FLAN.  
  ***Atenção!***A CSLL retida constante na  COSIRF (Contribuições Sociais e Imposto de Renda Retidos na Fonte) não é carregada para este registro.
* Lançamentos Fiscais de Saída que possuem o Tributo CSLLRF continuarão serão carregados do TOTVS Gestão Financeira.

#### **3. Origem Aplicação Financeira** **Para Lançamentos originados de Aplicação financeira devem ser observados os seguintes pontos:**

* + Nos parâmetros da ECF deve-se marcar a opção **"Carregar Retenções do Fluxus - Registro Y570"**
  + A aplicação financeira deve possuir valor de IR retido no período de geração da ECF (Valor de IR Retido é gerado no processo de regaste na aplicação financeira).
  + A aplicação financeira deve possuir código de receita vinculado.
  + A Conta Caixa vinculada a aplicação financeira deve possuir os dados do Banco com o preenchimento do CNPJ.
