---
content_hash: 0a70e3b641903f825769f759d6596a81aaa37faba9cd5d61d1c7d5ce30f171da
fetched_at: '2026-06-29T00:09:48.456635+00:00'
page_id: '435105160'
product: rm
source: tdn-rm
title: Identificação - Regra de Vencimento - Data de vencimento em dia útil ou fixo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105160
version: 4
---

A criação desta funcionalidade foi para atender a necessidade de definir se o intervalo de 1 a 31 de dia de vencimento será fixo ou útil.  
Abaixo estão as mudanças ocorridas no módulo de aluguel.

# **Regra Vencimento**

---

Através deste cadastro é possível informar um conjunto de parâmetros para um determinado vencimento.

Farão parte deste conjunto de parâmetros os seguinte campos:

* **Código do Vencimento:** Código numérico auto incrementado que compõe a chave primária da entidade;
* **Código da Coligada do Vencimento:** Código numérico que representa a coligada do vencimento e compõe a chave primária da entidade;
* **Descrição do Vencimento:** Descrição resumida da regra de vencimento;
* **Dia do Vencimento:** Número inteiro no intervalo de 1 a 31 que determina o dia do vencimento;
* **Contagem:** Bit que determinará o tipo de contagem para o dia vencimento 0 para dia fixo e 1 para dia útil. Sendo o padrão deste campo "1" dia útil;
* **Dias Fixos:** Baseado no "Dia do Vencimento" as datas serão exatamente iguais.
  + Exemplo: Se o "dia do Vencimento" informado for dia 01, os vencimentos serão todo dia 01 dos meses subsequentes. Não será tratado se o dia do vencimento é útil ou não e se o vencimento deve ser prorrogado ou antecipado.
* **Dias Úteis:** com base no "Dia do Vencimento" o sistema contará o dia para o vencimento.
  + Exemplo: Se o "dia do Vencimento" informado for dia 05, o sistema contará cinco dias úteis para gerar o vencimento. O calendário base será o informado no módulo financeiro da linha RM.
  + Para integração com o BackOffice Protheus deverá haver uma réplica manual dos calendários e parametrização.
* **Ação divergência vencimento:** Campo que será utilizado na geração de lançamentos financeiros quando houver divergência entre a data de "1º vencimento" do contrato de locação em relação a "regra de Vencimento". As opções são:
  + Fraciona;
  + Acumula;
  + Considera valor do contrato.

O campo "Ação divergência vencimento" será utilizado para gerar o lançamento financeiro de aluguel nos casos em que a data de vencimento diverge do período real de aluguel. Exemplo:

Período do contrato de 16/03/14 a 15/03/15;  
A data de vencimento padrão é 15/04/14;

Para o cliente que solicita que a data de vencimento seja todo dia 20, com este novo campo, teríamos os seguintes comportamentos:

* Fraciona: Cria um lançamento no dia 20/03, com o número de dias proporcional; Os próximos vencimentos serão nos dias 20 subsequentes, relativos a um mês de aluguel;
* Acumula: Cria um lançamento no dia 20/04, com o número de dias proporcional (45 dias); Os próximos vencimentos serão nos dias 20 subsequentes, relativos a um mês de aluguel;
* Considera valor do contrato: Cria o lançamento com o valor original, considerando apenas uma espécie de prazo ou carência para o pagamento.

O default deste campo é a opção: "Considera valor do contrato"

# **Campo Código da Regra de Vencimento**

---

O campo denominado Código da regra do vencimento na tela de cadastro de contrato de locação, mapeia o conjunto dos parâmetros da entidade Regra de Vencimento.

Será apresentando em tela além do campo com o código a descrição da Regra de Vencimento.
