---
content_hash: 1d44826f81c7d06bd58705a1c113f2ef82b722931cc1fe481b4e6696d5dd3be3
fetched_at: '2026-06-29T00:09:20.986088+00:00'
page_id: '422545759'
product: rm
source: tdn-rm
title: Apuração PIS/COFINS Não Cumulativo (Outras Informações)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545759
version: 8
---

## **Conteúdo**

**Conteúdo**

## **01. Introdução**

Ao selecionar o Tributo do Período, se o Tributo associado for do Tipo PIS/COFINS o sistema irá carregar para a Pasta Detalhamento / Campo Alíquota de Apuração o campo Alíquota do Cadastro de Tributos.

## **02. Como o sistema identificará a regra que deverá utilizar no momento do Encerramento do Período**

Ele buscará o Evento Tributário informado no Vigência Eventos Tributários, verificará em qual vigência o Período está associado, levando em consideração o Tributo e a Data Inicial e Final do Período.  
No cadastro de Vigência se define o período de utilização de uma determinada regra de cálculo.   
O sistema considerará para efeito do Cálculo apenas Lançamentos Contábeis já integrados ao Lote Zero.

## **03. Como se define o Evento Tributário**

Deverá ser definido em função da forma como o usuário define seu Plano de Contas.  
Caso a empresa precise definir as regrar por filial, deverá habilitar o campo Define Regra por Filial, no cadastro de Evento Tributário. Fazendo isso, a seleção de Contas Contábeis deverá ser feita Filial a Filial.  
Deverá definir quais as Contas Contábeis deverão ser utilizadas no cálculo do imposto.  
Além de restringir por Filial, o usuário poderá restringir a seleção da Conta em função do Departamento, Centro de Custo, Contas Gerencias, Tipo (Débito / Crédito).  
O usuário terá a opção de Selecionar contas sintéticas.  
Este recurso só estará disponível se o cliente possuir o TOTVS Gestão Contábil.

## **04. Fórmula de Cálculo do Imposto**

Base de Cálculo (Receita Tributada  Receita Não Tributada  Exclusões  Isenções) ¹ Alíquota Apuração = **PIS/COFINS Devido**

**PIS/COFINS a pagar** : PIS/COFINS Devido – Créditos (Crédito Período Anterior  Credito Período Atual)  Compensações

**Onde¹** = Sinal de divisão"/"

## **05. Como é determinado o Crédito do Período Atual**

Cálculo do Crédito Integral: Busca os valores das Contas Contábeis.  
Cálculo da Base Crédito Proporcional : Busca os valores das Contas Contábeis e multiplica pelo % Receita Tributada.  
% Receita Tributada = Receita Tributada/ (Receita Tributada + Receita Não Tributada)  
Cálculo do Crédito Proporcional: Busca o valor da Base Crédito Proporcional e multiplica pelo percentual informado no campo Percentual (%).

Atenção

No encerramento dos períodos de apuração dos tributos **PIS** e **COFINS** o sistema verificará se existe algum evento tributário vinculado a estes tributos (modelo antigo em Delphi), caso positivo realizará a apuração normalmente, caso contrário o período será encerrado sem mensagem de inconsistência porém, com os valores zerados ou desatualizados.
