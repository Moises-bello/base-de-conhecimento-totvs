---
content_hash: 19e163f8e2aad66df344228f8d92e364a9f2ffd834943010cf5a7e5e8418870a
fetched_at: '2026-06-29T00:12:15.235993+00:00'
page_id: '973055853'
product: rm
source: tdn-rm
title: DT - Inclusão de Usuário para o Acesso ao RM Portal - Adequação na execução
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=973055853
version: 20
---

## **01. DADOS GERAIS**

| Produto: | TOTVS - Folha de Pagamento |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Inclusão de Usuário para o Acesso ao RM Portal - Adequação na execução |
| Issue: | [DRHROTRM-14395](https://jiraproducao.totvs.com.br/browse/DRHROTRM-14395 "View this issue") |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2410.281
* 12.1.2502.183
* 12.1.2506.125 e superiores

## **03. SITUAÇÃO/REQUISITO**

Solicitamos que, na execução do processo **"Inclusão de Usuário para Acesso ao RM Portal"** em lote, o sistema permita a continuidade do processamento mesmo que algum funcionário da lista já possua um usuário criado.

Atualmente, essa situação faz com que nenhum usuário da lista seja criado, mesmo quando os demais registros estão válidos.

## **04. SOLUÇÃO**

Foi adequado o processo de **"Inclusão de Usuário para Acesso ao RM Portal"**, que passa a seguir a seguinte regra:

Ao executar o processo, o sistema **associa o usuário já existente** e **atualiza as permissões** do usuário conforme os parâmetros abaixo:

  

Importante:

* Caso o "Código do Usuário" não exista na base de dados, o processo irá criar um novo usuário e associá-lo ao funcionário. Esse código será criado de acordo com a seleção dos parâmetro.
* É importante ressaltar que desvincular um usuário de um funcionário não implica na exclusão do "Código do Usuário" da base de dados, o usuário permanece ativo no sistema.

### Exemplo l:

No cadastro do funcionário o campo "Código do Usuário" está em branco:

Ao executar a rotina com os parâmetros **desmarcados**, o sistema criará o "Código do Usuário" utilizando o mesmo código da chapa do funcionário e preencherá automaticamente o campo no cadastro do funcionário.

### Exemplo ll:

Caso o parâmetro **"Utiliza CPF para código de acesso"** esteja marcado, o sistema criará o "Código do Usuário" utilizando o número do CPF do funcionário e preencherá automaticamente esse valor no campo  no cadastro do funcionário.

### Exemplo lll:

Ao marcar o parâmetro **"Utiliza número da coligada e chapa para código de acesso"**, o sistema criará o"Código do Usuário" concatenando o código da coligada com a chapa do funcionário, preenchendo automaticamente esse valor no campo no cadastro do funcionário.

### Exemplo lV:

Ao executar a rotina com os parâmetros **desmarcados** e com o **Código de Usuário** já vinculado a um funcionário cadastrado, o sistema exibirá a mensagem abaixo. Isso ocorre porque, mesmo sem alteração ou inclusão do **Código de Usuário**, a senha é sempre resetada a cada execução do processo.

## **05. DEMAIS INFORMAÇÕES**

[Inclusão de Usuário para Acesso ao RM Portal](https://tdn.totvs.com/pages/releaseview.action?pageId=452719492)
