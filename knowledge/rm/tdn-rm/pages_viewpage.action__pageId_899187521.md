---
content_hash: a15413b414bcdf0ceb549146a1270d89856d0cdb3ade96fb5981c03b921d5948
fetched_at: '2026-06-29T00:12:02.093113+00:00'
page_id: '899187521'
product: rm
source: tdn-rm
title: 'Função de Fórmula: FAPCHAPADATA'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=899187521
version: 8
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Função de fórmula que retorna a alíquota FAP por estabelecimento empresarial, conforme a seção centralizadora da estrutura que o colaborador está alocado. Caso não exista alíquota cadastrada na seção centralizadora, será verificado na tabela de valores fixos registro com a finalidade Alíquota FAP dentro da vigência.   
Sintaxe: FAPCHAPADATA(CHAPA,DATA) 

## **02. EXEMPLO DE UTILIZAÇÃO**

FAPCHAPADATA(CHAPA,MTDATA(01,MES,ANO))

FAPCHAPADATA('00001','01/12/2020')

falseAtenção

O resultado desta fórmula será:

* 0 (Zero) se a seção centralizadora de CNPJ não tem cadastrado vigência de FAP por estabelecimento empresarial e não tem alíquota FAP com vigência no cadastro de Valores Fixos
* -1 quando possui vigência para o FAP por estabelecimento empresarial, mas não possui alíquota na data informada, mesmo se possui tabela de valores fixo com vigência.
* Valor da alíquota referente ao FAP dentro da vigência conforme a data informada, verificando primeiro o cadastro de FAP por estabelecimento empresarial e caso não encontre, a tabela de valores fixos.
Fap por estabelecimento e Tabela com Valor Fixo com vigência

Cadastro de FAP Estabelecimento Empresarial com vigência de 01/01/2021 a 30/04/2023:

Tabela com Valor fixo com vigência de 01/01/2010 a 31/12/2023:

Executando a Fórmula informando a data 30/04/2023 retornou 0,5 conforme a alíquota FAP do cadastro de FAP por estabelecimento empresarial:

Executando a fórmula informando a data 01/05/2024 retornou 1 conforme o cadastro da tabela de valores fixos:

Sem FAP por estabelecimento empresarial e Tabela de Valor Fixo

Seção centralizadora sem FAP por estabelecimento empresarial cadastrado:

Tabela de Valores fixos com finalidade Alíquota FAP com vigência de 01/01/2020 a 31/12/2022:

Informando a data 01/05/2023, a fórmula retornou 0:

Com FAP por estabelecimento, mas sem Alíquota

FAP por estabelecimento empresarial cadastrado com vigência de 01/01/2023 a 31/12/2023, mas sem alíquota cadastrada:

Informando a data 01/05/2023 na fórmula, retornou  -1:

Executando na data de admissão

Colaborador admitido dia 16/02/2022:

FAP por estabelecimento com Vigência de 01/01/2021 a 31/12/2024 com alíquota com vigência de 01/01/2021 a 31/12/2023:

Executando a Fórmula e passando a data 16/02/2022, retornou 0,5, conforme a alíquota acima:

## **03. TABELAS UTILIZADAS**

PSECAOFAPESTABELECIMENTO

PSECAOFAPALIQUOTA

PVALFIX

GFORMULA
