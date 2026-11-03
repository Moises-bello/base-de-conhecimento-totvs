---
article_id: 360021745172
category: Financeiro
content_hash: 78e3c61797566f728a605484cc1452db1dfbde35f63b99d2beaaaf4e823abf6e
fetched_at: '2026-06-28T22:38:02.995819+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA271 - Como faz
  para criar uma visão gerencial financeira
type: support-article
updated_at: '2022-06-15T02:03:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021745172-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA271-Como-faz-para-criar-uma-vis%C3%A3o-gerencial-financeira
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como faz para criar uma visão gerencial financeira para as rotinas;

* **FINC021 – Fluxo de Caixa;**
* **FINC022 – Fluxo por Natureza;**
* **FINR770 – Fluxo de Caixa Realizado;**
* **FINR140 – Fluxo de Caixa Analítico.**

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA271 - Todas as versões  
  
  
**Solução**1- Incluir uma **Visão Gerencial Financeira** (FINA271) Simples dar um código e um nome.  
2- Inserir uma conta de resultado **Sintética**/**Total** e abaixo dela criar duas Contas **Gerenciais Financeiras** de despesa **Analítica**/**Subtrai** e outra **Analítica**/**Soma** amarrando a conta Pai de resultado.  
3- Amarrar as **naturezas** e considerar o valor do movimento, caso a **natureza** esteja entre a faixa definida no cadastro da conta **gerencial financeira** (**FJ3\_SEDINI e FJ3\_SEDFIM**).  
Colocar no campo **FJ3\_IDENT**, as definições abaixo:

**. Soma:** Apresentar a soma dos valores de acordo com as naturezas definidas na faixa. **. Subtrai:** Apresentar a subtração dos valores de acordo com as naturezas definidas na faixa. **. Negrito:** Define que a impressão da linha dos dados daquela entidade será em negrito. **.Total Geral e Negrito:** Define que a impressão da linha dos dados daquela entidade será em negrito e que haverá um destaque naquele totalizador. **.Linha sem Valor:** Imprimir uma linha tracejada caso a descrição for igual a hífen, caso contrário, imprimir somente o código sem valores. **.Linha sem Valor e Negrito:** Define que não serão impressos valores, mesmo zerados, para linha de dados daquela entidade e a linha dos dados será em negrito. **. Separador:** Define que os dados daquela linha serão ignorados e na impressão do relatório será impresso um traço “-“ substituindo as mesmas.

4 –Criar duas **naturezas estruturadas.**

 - 11111 Sintética despesa  
1111 -  Analítica despesa amarrando a pai 11111

 -  22222 Sintética despesa  
2222 -  Analítica despesa amarrando a pai 22222

5 – Criar orçamento e amarrar a **natureza** de **despesa.**6 – Ao efetuar alguma consulta procurar esta visão através da **LUPA.**

**Importante:  
MV\_NATSINT = 1 e Tabelas FJ1, FJ2 e FJ3**
