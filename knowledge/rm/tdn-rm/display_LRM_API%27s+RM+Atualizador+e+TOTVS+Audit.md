---
content_hash: d631df6b53f678f090dc2f3b91eeb391bae86321d67c52b8acbb6a912f9a7e28
fetched_at: '2026-06-29T00:11:55.780331+00:00'
page_id: '864324607'
product: rm
source: tdn-rm
title: API's RM Atualizador e TOTVS Audit
type: documentation
url: https://tdn.totvs.com/display/LRM/API%27s+RM+Atualizador+e+TOTVS+Audit
version: 2
---

Este documento tem como objetivo explicar como utilizar as APIs do RM Atualizador e TOTVS Audit.

Para executá-las, é necessário que o programa RM.Host.exe esteja em execução e o alias a ser utilizado esteja configurado no RM.

### **Utilizando um alias diferente do definido como padrão**

**RM Atualizador:** Nas rotas do atualizador é necessário informar o nome do alias;

**TOTVS Audit:** As rotas do TOTVS Audit utilizam o alias definido como padrão. Para utilizar um alias diferente o ambiente precisa ser configurado como Multi-Tenancy  ([Configurando o RM Multi Tenancy (Multi Alias)](https://tdn.totvs.com/x/9XwcEQ)). O TOTVS Audit possui uma rota para verificar qual alias está sendo utilizado.

### **Descrição das Rotas**

Existe uma *colletion*do Postman com uma chamada padrão para todas as rotas do RM Atualizador e TOTVS Audit, disponível internamente para membros da Engenharia no repositório de [Colletions do TestFlow da Engenharia](https://dev.azure.com/totvstfs/Engenharia-BH/_git/CSharpTesteFlowGCAD?path=/Postman/RMAtualizador_ColletionCompleta.json&version=GBmain).

As APIs do RM Atualizador possuem diferentes tipos de autenticação: as que utilizam a *tag* "UseRMUser" que utilizam as credenciais do RM para se conectar, e as demais que usam as credenciais do banco de dados.

##### **RM Atualizador**

**Executar a Atualização - /UpgUpgradeWebServer/atualizador/ExecuteUpgrade/{alias}/1**ou**/UpgUpgradeWebServer/atualizador/ExecuteUpgradeUseRMUser/{alias}/1:**

* Resultado esperado: Se houver atualizações a serem executadas, a API retorna um JSON com informações sobre o que será atualizado. Se não houver atualizações, a API informa que não há atualizações disponíveis.

**Executar a Atualização (*noJSON*) - /UpgUpgradeWebServer/atualizador/ExecuteUpgrade/{alias}/1/noJSON:**

* Resultado esperado: A API retorna a quantidade de erros que ocorreram durante a execução da atualização. Se não houver atualizações disponíveis, ela retorna "0".

**Obter o Progresso da Atualização - /UpgUpgradeWebServer/atualizador/GetUpgradeProgressCloud/{alias} ou /UpgUpgradeWebServer/atualizador/GetUpgradeProgressCloudUseRMUser/{alias}:**

* Resultado esperado: Se houver uma atualização em execução, a API retorna um JSON com informações sobre as etapas da atualização, incluindo progresso, tempo de execução e nome da etapa. Se não houver atualizações em andamento, a API informa que não foram encontradas atualizações.

**Obter se a base possui scripts pendentes - /UpgUpgradeWebServer/atualizador/HasPendingScript/{alias}:**

* Resultado esperado: Se houver scripts pendentes, a API retorna *true*, caso não haja scripts pendentes, *false*.

**Verificar os Pré-Requisitos - /UpgUpgradeWebServer/atualizador/CheckRequirements/{alias} ou /UpgUpgradeWebServer/atualizador/CheckRequirementsUseRMUser/{alias}:**

* Resultado esperado: A API retorna um JSON com as validações dos pré-requisitos do RM Atualizador.

**Obter os Impactos em Objetos Gerenciais (relatórios, cubos, planilhas) - /UpgUpgradeWebServer/atualizador/GetUpgradeImpacts/{alias} ou /UpgUpgradeWebServer/atualizador/GetUpgradeImpactsUseRMUser/{alias}:**

* Resultado esperado: A API executa a análise de impacto da versão na base de dados e retorna os resultados em um JSON. Se não houver impactos, o JSON será vazio.

##### **TOTVS Audit**

**Ativar o TOTVS Audit - /api/totvs-audit/v1/totvs-audit-config:**

* Resultado esperado: Retorna um json com os passos que foram realizados para ativação do TOTVS Audit.

**Visualizar o alias utilizado pela API - /api/totvs-audit/v1/totvs-audit-config/alias:**

* Resultado esperado: A API retorna o nome do alias para qual a API está apontando.

O TOTVS Audit possui rotas para alterar a configuração de tabelas auditadas, as quais podem ser encontradas na documentação específica das [Rotas do TOTVS Audit](https://tdn.totvs.com/x/ZIyEMw).
