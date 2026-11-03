---
content_hash: 7c63b4e12dbd398dca32ce44b0d811d4b83f3af8d546648e9d9567fc517a3694
fetched_at: '2026-06-29T00:10:56.771569+00:00'
page_id: '593040273'
product: rm
source: tdn-rm
title: Serviços Via WebService
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=593040273
version: 2
---

## **01. VISÃO GERAL**

Foi implementado algumas regras de restrição ao acesso de dados através de DataServers por meio dos serviços SOAP e Rest.

Essas restrições se aplicam ao consultar registros de funcionários de coligadas diferentes, foi implementado um filtro para verificar se o funcionário tem permissão para acessar aquelas informações.

## **02. EXEMPLO DE UTILIZAÇÃO**

Foi criada uma nova permissão de acesso **"Desconsiderar Filtro de Produto em WebService",** com o objetivo de que o sistema passe a fazer filtro de segurança nos DataServers ao realizar acesso via WebService.

O novo parâmetro esta localizado em **Serviços Globais - Segurança - Perfis**

No caso de o usuário estar vinculado a um perfil que não contenha permissão, os DataServers retornarão os registros filtrados conforme regra de negócio do produto, caso contrário o sistema continua com o comportamento padrão retornando todos os registros conforme filtro informado pelo usuário.

## **02.01. Filtro por Coligada**

Caso o usuário não tenha permissão no parâmetro ***"Desconsiderar Filtro de Produto em WebService",*** os DataSevers retornarão apenas os dados das coligadas que o usuário tenha permissão de acesso ao cadastro correspondente no produto.

A funcionalidade até então foi implementada no DataServer **PtoHorarioData**

**OBS: Para que o usuário tenha acesso aos demais DataServers que não receberam a implementação do filtro de segurança do produto, mantendo o comportamento que o sistema já possuía, deverá dar permissão a esse novo parâmetro.**

## **02.02 Configurar Ambiente SOAPUI**

Ao abrir o soap, selecionar novo projeto.

Novo projeto: <http://localhost:8051/wsDataServer/MEX?wsdl>

Com o nome que desejar:

**1 - Configurar o host, com as tags, caso não as tenham, segue abaixo :**

<add key="DefaultDB" value="CorporeRM" />

<add key="HTTPPORT" value="8051" />

**Host.Exe.config**

**Host.Service.exe.config**

**Após incluir as tags, iniciar o host como administrador.**

**2 - Configurar o READVIEW**

Selecionar a aba Auth - Basic, preencher os campos de Username e password

.

**OBS: O USUÁRIO QUE SERÁ VALIDADO É O USUÁRIO PREENCHIDO NA AUTHORIZATION, O USUÁRIO PREENCHIDO NO CONTEXTO NÃO FAZ DIFERENÇA, MAS A CODCOLIGADA SERÁ VALIDADA A QUE ESTIVER NO CONTEXTO.**

## **Exemplo:**

Usando o usuário "mestre2" que possui permissão para acesso na coligada 6 e não possui permissão para acesso na coligada 1.

**Observação:**

Em caso da flag " **Desconsiderar filtro de produto em Webservice"** estar sem permissão **(Permissão vinculada ao usuário em serviços globais - segurança - usuário/perfil),** deve retornar registros conforme permissão de segurança cadastrada no perfil.

**Acesso em todas as coligadas**

**Retorno SOAPUI**

**Sem acesso a coligada 1**

**Retorno SOAPUI**
