---
content_hash: f1b126ae7bc77c58205156e8c3078693626fc97326383ee810b7d353b38e9620
fetched_at: '2026-06-29T00:09:21.178282+00:00'
page_id: '422545852'
product: rm
source: tdn-rm
title: Contas Paralelas (Lalur parte B)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545852
version: 5
---

A parte B do LALUR foi implementada na Gestão Fiscal a partir do Plano de Contas Paralelo do [TOTVS Gestão Contábil](http://tdn.totvs.com.br/pages/viewpage.action?pageId=198948832), onde serão registradas todas as movimento da conta. Deve ser criado na TOTVS Gestão Fiscal um plano de Contas Paralelo contendo todas as contas que serão controladas na Parte B.   
 O cadastro das Contas do LALUR Parte B pode ser acessado através do menu Obrigações Principais | LALUR Parte B | Contas.  
 O novo cadastro, onde serão controlados os saldos, deve ter os seguintes campos:   
 **Código** (obrigatório) - Serão apresentadas todas as contas do Plano de Contas Paralelo parametrizado para a Parte B de último nível (analítica).

**Descrição** - Informe a descrição da Conta Paralela

**Natureza** - Quando a conta for da natureza do tipo débito os valores serão reduzidos do Lucro Real ou no valor do imposto. Caso a natureza da Conta Contábil for do tipo crédito, os valores irão aumentar o Lucro Real. Abaixo a regra de cada Natureza selecionada na criação da parte B do LALUR:  
I-    Adição (C) - afeta a Parte A  
 II-   Exclusão (D) - afeta a Parte A  
 III-  Dedução (D) - NÃO afeta a Parte A  
 IV-  Compensação (D) - NÃO afeta a Parte A

**Data de Início da Vigência** - Obrigatório  
***Atenção!*** Deve ser informada a data final do período de apuração em que a conta foi criada.

**Data de Término da Vigência** - Informar a data final  
 Na aba Informações Fiscais deve ser preenchido os seguintes campos:

**Tributo** (obrigatório) - Selecionar um dos tributos listados que são IRPJ e CSLL

**Saldo Inicial** -  Este campos deve ser editável apenas na inclusão da conta. Após ser salvo e vinculado lançamentos a conta em hipótese alguma o registro poderá ser alterado.

**Saldo Atual** - Campo calculado pelo sistema a partira das movimentações da conta, não editável. O Saldo Atual e calculado da seguinte forma: o sistema soma todos os lançamentos a débito e todos a crédito, o saldo será = débito - crédito.  
***Observação:*** Campo memo.

As consta da parte B possuem natureza de adição, exclusão, compensação e de dedução. As natureza de adição, exclusão e compensação afetam a apuração do Lucro Real, portanto são demonstradas na Parte A do LALUR. Já as contas com natureza de dedução, afetam o valor do imposto a pagar.
