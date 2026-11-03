---
content_hash: 040955dc139e51f719a3757595966bbba56b6aac237512f4c118923dd8962708
fetched_at: '2026-06-29T00:10:58.220255+00:00'
page_id: '604520959'
product: rm
source: tdn-rm
title: Totvs Folha de Pagamento RM x TOTVS Moda - Cadastros e processos contábeis
  e financeiros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=604520959
version: 7
---

**Cadastros e processos contábeis**

**1 - Contábil - Período Contábil (recebimento)**

**Mensagem: ACCOUNTINGCALENDAR**

**Versão: 1.000**

Recebimento no RM do período contábil. Pode ser consultado o resultado com consulta SQL (SELECT \* FROM CPARAM WHERE ID IN (24,25) AND CODCOLIGADA = 1).

**Exemplo de Json de Envio da mensagem:**

**2 - Contábil - Centro de Custo (recebimento)**

**Mensagem: COSTCENTER**

**Versão: 2.003**

Recebimento no RM do Centro de Custo. Pode ser consultado o resultado com consulta SQL (SELECT \* FROM GCCUSTO). Após a carga inicial, todo centro de custo criado, deverá ser feito o cadastro do De/Para em ambos os sistemas, antes de enviar qualquer mensagem que conste a informação de centro de custo. Exemplo: Lançamento Contábil (ACCOUNTINPAYABLEDOCUMENT) e Lançamento Financeiro (ACCOUNTINGENTRY).

**Exemplo de Json de Envio da mensagem:**

**3 - Contábil - Histórico Padrão (recebimento)**

**Mensagem: ACCOUNTANTDEFAULTHISTORY**

**Versão: 1.000**

Recebimento no RM do Histórico Padrão. Pode ser consultado o resultado com consulta SQL (SELECT \* FROM CHISTP). Após a carga inicial, todo Histórico Padrão criado, deverá ser feito o cadastro do De/Para em ambos os sistemas, antes de enviar qualquer mensagem que conste a informação de Histórico Padrão. Exemplo: Lançamento Contábil (ACCOUNTINPAYABLEDOCUMENT).

**Exemplo de Json de Envio da mensagem:**

**4 - Contábil - Plano Contas (recebimento)**

**Mensagem: ACCOUNTANTACCOUNT**

**Versão: 2.001**

Recebimento do RM do Plano de Contas. Pode ser consultado o resultado com consulta SQL (SELECT \* FROM CCONTA). Após a carga inicial, toda Conta contábil criada, deverá ser feito o cadastro do De/Para em ambos os sistemas, antes de enviar qualquer mensagem que conste a informação de Conta Contábil. Exemplo: Lançamento Contábil (ACCOUNTINPAYABLEDOCUMENT).

**Exemplo de Json de Envio da mensagem:**

**5 - Contábil - Lançamento Contábil (envio)**

**Mensagem: ACCOUNTINGENTRY**

**Versão: 2.002**

Envio do RM  dos lançamentos contábeis. Após a carga inicial, toda Conta contábil criada, deverá ser feito o cadastro do De/Para em ambos os sistemas, antes de enviar qualquer mensagem que conste a informação de Conta Contábil.

**Observações:**

* Pode consultar o processamento da mensagem no EAI em RM | Integrações | EAI 2.0 | Mensagens | Gerenciamento de Mensagens;
* Para executar o envio deverá ser gerado o Lançamento Contábil em RM | RH | Encargos | Contabilização | Geração dos Lançamentos;
* Após gerar o lançamento contábil, em RM | RH | Encargos | Contabilização | Lançamento | Lançamentos (Folha de Pagamento) | Processos | Integração contábil com outros BackOffices.

**Exemplo de Json de Envio da mensagem:**

**Lançamentos Financeiros**

**1 - Financeiro - Cadastro de Clientes/Fornecedores**

**Mensagem: CUSTOMERVENDOR**

**Versão: 2.003**

O cadastro de Clientes/Fornecedores serão encaminhados na mesma mensagem com todos os campos disponíveis. No TOTVS Moda tais cadastros não são independentes e, portanto, serão recebidos na mesma mensagem. Esses dados serão recebidos no RM para uso nos processos necessários ao TOTVS Moda.

**Exemplo de Json de Envio da mensagem:**

**2 - Financeiro - Banco e Agência**

**Mensagem: BANK**

**Versão: 2.002**

O cadastro de banco, agência, conta caixa, conta corrente serão encaminhados na mesma mensagem. No TOTVS Moda tais cadastros não são independentes e, portanto, serão recebidos na mesma mensagem. Esses dados serão recebidos no RM para uso nos processos necessários ao TOTVS Moda.

**Exemplo de Json de Envio da mensagem:**

**3 - Financeiro - Lançamento Financeiro (envio)**

**Mensagem: ACCOUNTINPAYABLEDOCUMENT**

**Versão: 2.002**

A geração de lançamentos financeiros deverá ser executada normalmente no sistema RM utilizando dados oriundos do TOTVS Moda. Após a geração deverá executar o processo de "Integração financeira com outros BackOffice". As informações de financeiro geradas pela folha serão enviadas automaticamente para o BackOffice conforme configuração da mensagem única.

**Observações:**

* Pode consultar o processamento da mensagem no EAI em RM | Integrações | EAI 2.0 | Mensagens | Gerenciamento de Mensagens;
* Para executar o envio deverá ser gerado o Lançamento Financeiro em RM | RH | Encargos | Financeiro | Geração dos Lançamentos;
* Após gerar o lançamento financeiro, em RM | RH | Encargos | Financeiro | Lançamentos | Lançamentos (Folha de Pagamento) | Processos | Integração financeira com outros BackOffices.

**Exemplo de Json de Envio da mensagem:**
