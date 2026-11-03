---
content_hash: 24b2051ed3a3b3e7e8563da413c6e736bd5a75d56096f670191b12c0754b6428
fetched_at: '2026-06-29T00:11:06.325268+00:00'
page_id: '634028249'
product: rm
source: tdn-rm
title: LGPD-Webservice Ponto
type: documentation
url: https://tdn.totvs.com/display/LRM/LGPD-Webservice+Ponto
version: 19
---

## **01. VISÃO GERAL**

Com base na [Lei Nº 13.709/18](http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709.htm) , implementamos algumas regras de restrição a dados consumidos através de dataservers por meio dos serviços SOAP e Rest. 

Estas restrições se aplicam aos registros retornados (restrição de linha) ao consultar dados através destes serviços e implicam que um usuário só poderá ter acesso as informações de cadastro que possua permissão e/ou que lhe pertencem, ou seja, informações que fazem referência a sua pessoa.

Para os serviços via SOAP as restrições de aplicam aos métodos "ReadView" , "ReadRecord" , SaveRecord.

## **02. Permissão de acesso**

Criada no cadastro de serviços Globais em Perfil-Automação de Ponto-Configurações  a permissão de acesso 07.03-*"**Desconsiderar Filtro de Produto em WebService**"* .

O sistema fará a validação do filtro de segurança nos Dataservers ao realizar acesso via Webservice.

Caso o usuário não tenha permissão no parâmetro ***"Desconsiderar Filtro de Produto em WebService",***os DataSevers retornarão apenas os dados das coligadas que o usuário tenha permissão de acesso ao cadastro correspondente no produto.

## **03. Exemplo1**

**Confirmada a opção "Proibir Acesso"**

Criado um usuário com o nome WEB com acesso as coligadas 1,8 e 9

O Dataservers retornou apenas as coligadas no qual  o usuário tem acesso, neste caso, coligadas 1 ,8 e 9.

## **04. Exemplo2**

**Cnfirmada a opção "Permitir Acesso"**

Os dataservers retornaram o resultado da coligada do usuário e das demais.

No caso de o usuário estar vinculado a um perfil que não contenha permissão, os DataSevers retornarão os registros filtrados conforme regra de negócio do produto, caso contrário, o sistema continua com o comportamento padrão retornando todos os registros conforme filtro informado pelo usuário.

## **LISTA DE DATASERVERS COM RESTRIÇÕES:**

| Funcionalidade | Dataserver | Status |
| --- | --- | --- |
| Cadastro de funcionarios-Utiliza cartão de ponto | Ptodatafuncionarioutilizaponto | Ativo |
| Cadastro de funcionários-Histórico de Utilização do cartão de Ponto | PtoDataHistoricoCartaoPonto | Ativo |
