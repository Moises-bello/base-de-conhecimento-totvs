---
content_hash: 3f058edea63c651cfd512137259418eb28277922c2f466ce905c71bcf064696c
fetched_at: '2026-06-29T00:09:26.770766+00:00'
page_id: '423938417'
product: rm
source: tdn-rm
title: Associação de Cenários de Cálculo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938417
version: 5
---

O objetivo do processo é criar cenários de cálculo nos patrimônios no sistema.  
A criação de um novo cenário de cálculo nos patrimônios possibilita ao usuário a utilização de taxas de depreciação diferentes dos cenários já existentes e, também, a caracterização dos novos cenários como fiscais, para que tenham informações diferentes do(s) cenário(s) que seja(m) contábil(eis). Ou seja, o sistema possibilitará ao usuário ter mais de uma visão sobre o controle do imobilizado de suas empresas, sendo esta visão contábil ou fiscal, como taxas de depreciação diferentes ou não das ditas pela legislação de imposto de renda, dando assim um horizonte diferenciado sobre a vida de seu imobilizado A parametrização do processo é feita acessando o menu  Utilitários\ Associação de Cenários Neste, devem ser preenchidos obrigatoriamente os campos:

**Grupo de Patrimônio:** Grupo ao qual o cenário a ser criado será vinculado.

**Cenário:** Cenário ainda não vinculado ao Grupo de Patrimônio informado. Este campo só será habilitado quando o Grupo de patrimônio for preenchido. No filtro, só serão apresentados cenários ainda não vinculados ao grupo.

**Taxa Default:** Qual será a taxa de depreciação padrão para o cenário a ser criado.

**Cenário de Cálculo base para cálculos:** Qual será o cenário de cálculo que o sistema irá basear para criar os saldos patrimoniais do novo cenário informado.

O usuário ainda poderá marcar as opções abaixo:

Replicar estrutura contábil do Grupo de Patrimônio: Ao marcar esta opção, todos os eventos e defaults contábeis do cenário de Cálculo Base serão replicados para este novo cenário.

Apenas converter valores para nova moeda: Ao criar um cenário com esta opção, o sistema apenas converterá os valores base, depreciações acumuladas e valores de testes de impairment de acordo com a moeda do novo cenário e sua cotação em relação à moeda do cenário base informado. Não efetuará cálculos dos saldos de acordo com a nova taxa default informada.

Realizando a parametrização conforme desejado, o processo poderá ser executado. O sistema irá realizar as validações abaixo para concluir com sucesso. Deve ser realizado o fechamento do período de cálculo anterior. Caso contrário, o sistema irá apresentar a mensagem: É necessário o Fechamento de Período para execução do processo.

Não poderá existir operações patrimoniais no período de cálculo atual. Caso contrário, o sistema irá apresentar a mensagem: Existem operações patrimoniais no período de cálculo atual que impossibilitam a execução do processo.

Não poderá existir contabilizações no período de cálculo atual. Caso contrário, o sistema irá apresentar a mensagem: Existem contabilizações no período de cálculo atual que impossibilitam a execução do processo.

Existir cotação. Se a moeda do cenário escolhido utilizar índice, verificar a existência das cotações para o período de cálculo atual e primeiro dia posterior ao período.

Se for parametrizado para somente converter valores para nova moeda, o sistema irá criar a estrutura de saldos dos patrimônios de acordo com a cotação da nova moeda, em relação à moeda do cenário base para cálculos que foi informado. Caso contrário, o cálculo será criado da seguinte forma:

Valor base novo: Se cenário for fiscal, será igual ao (Valor Base do cenário base + Valor de Impairment do cenário base) convertido pela cotação da nova moeda em relação à moeda do cenário base; Se não for fiscal, o cálculo será feito sem adição do Valor de Impairment ao Valor Base do cenário base;

Depreciação mensal nova: Taxa default mensal aplicada ao Valor base novo;

Depreciação acumulada: Depreciação mensal nova multiplicada pelo número de meses entre a data de início de vigência do cálculo do patrimônio até o período de cálculo atual. Se início de vigência for posterior ao período de cálculo atual, a depreciação acumulada será igual a 0;

Valores em índices serão calculados de acordo com a cotação atual do índice se a moeda no cenário em questão usar índice;
