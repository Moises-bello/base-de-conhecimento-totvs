---
content_hash: 1e02f6c880e0920bc0a91a2c7ca60d1aa4b490b134ee56ab128460113ddc729b
fetched_at: '2026-06-29T00:09:21.390482+00:00'
page_id: '422545878'
product: rm
source: tdn-rm
title: Controle de Créditos Fiscais de Tributos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545878
version: 23
---

# Conteúdo

Conteúdonone

# 1**.**Visão Geral

O cadastro será usado para armazenar os registros de crédito fiscal de tributo, onde devem ser informados:

* **Período do Crédito** (mês e ano);
* **Origem do Crédito**;
* **Tipo de Crédito**;
* **Valores do Crédito** (Normal e Extemporâneo);
* **Forma de Geração** (Manual ou Automática), indica se o registro foi inserido **manualmente** pelo usuário ou **automaticamente** pela integração com os lançamentos fiscais do sistema. Isso permite que o cliente identifique quais créditos foram gerados manualmente e quais foram gerados pelos processos internos de controle de crédito.

Exemplo da tela de cadastro

O campo **Saldo Remanescente** indica o valor restante do crédito após as compensações realizadas. As compensações do crédito (em anexo) podem ser feitas em período igual ou posterior ao do crédito e exigem a informação do **Tipo da Compensação**.

Exemplo do campo Saldo Remanescente

# 2. Regras

**Cadastro de Crédito Fiscal**

* Não serão permitidos valores negativos para os campos de Crédito.
* O **Valor Total do Crédito Apurado** (Normal + Extemporâneo) não pode ser menor que o total das compensações do crédito já incluídas.
* O **Saldo Remanescente do Crédito** será a soma dos valores do crédito apurado (Normal + Extemporâneo), subtraído do total já compensado.

**Cadastro de Compensações do Crédito Fiscal**

* Não serão permitidos valores negativos para o campo **Valor da Compensação**.
* O período da compensação não pode ser menor que o do crédito.
* O valor total dos registros de compensação não pode ultrapassar o total do crédito fiscal.
* Ao incluir/alterar uma compensação, o valor será subtraído do **Valor Total do Crédito Apurado** do crédito vinculado, refletindo no campo **Saldo Remanescente do Crédito**.
* Ao excluir uma compensação, o valor da mesma será retornado ao saldo remanescente.

# 3**.** Processos
