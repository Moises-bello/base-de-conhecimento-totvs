---
content_hash: 7e60955b6989f41da8ced99d11250b8ff6e4ad86b534e7f4a03a852a3de167e9
fetched_at: '2026-06-29T00:12:03.303591+00:00'
page_id: '905613075'
product: rm
source: tdn-rm
title: DT - Utilização do WebService PtoDataSolicitarAbonoFuncionario por chefes e
  supervisores externos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=905613075
version: 19
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | RM |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Função: | Solicitar abono via WebService |
| País: | Brasil |
| Requisito/Story/Issue: | [DRHJORNRM-7307](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-7307) |

## **02. SITUAÇÃO/REQUISITO**

Permitir o uso do WebService **PtoDataSolicitarAbonoFuncionario** por chefes e supervisores externos.

## **03. SOLUÇÃO**

Adequação do WebService **PtoDataSolicitarAbonoFuncionario** para permitir que chefes e supervisores externos consultem, cadastrem, editem e excluam abonos.

## **04. VERSÕES**

Disponível a partir das versões:

* 12.1.2410.150
* 12.1.2502 e superiores

## **05. CONFIGURAÇÃO**

### **RM:**

* É necessário editar o arquivo **RM.Host.Service.exe.config** e **RM.Host.exe.config** e inserir as seguintes tags:

*<add key="HTTPPORT" value="**porta\_desejada**" />  
 <add key="DefaultDB" value="**alias\_desejado**" />  
  
**Exemplo:***

***Arquivos a serem alterados:***

***Tags:***

### **Postman:**

* **Authorization**

É necessário informar o tipo de autenticação, usuário e senha.

**Auth Type:** Basic Auth;

**Username:** usuário (chefe ou supervisor externo);

**Password:** senha (chefe ou supervisor externo);

* **Headers**

É necessário informar o código da coligada do usuário que está realizando o processo.

**Key:** CODCOLIGADA;

**Value**: códigocoligada;

## **06. UTILIZAÇÃO**

Importante

* Chefes e supervisores externos só podem cadastrar, alterar e excluir abonos de seus subordinados. Caso contrário, a operação não será realizada e uma mensagem de erro será retornada.
11Método GET

1- Informar o método: **GET**e o **Endpoint:** "http://servidor:porta/RMSRestDataServer/rest/PtoDataSolicitarAbonoFuncionario".

2- Enviar a requisição clicando em **Send**.

3- Será retornado uma lista com todos os abonos da coligada.

Caso queria visualizar um abono específico é necessário informar o **CodColigada$\_$IdAbono** no **Endpoint:** "http://servidor:porta/RMSRestDataServer/rest/PtoDataSolicitarAbonoFuncionario/CodColigada$\_$idAbono".

2Método POST

1- Informar o método: "**POST"** e o "**Endpoint"**: "http://servidor:porta/RMSRestDataServer/rest/PtoDataSolicitarAbonoFuncionario".

olicitarAbonoFuncionariohttp://localhost:8051/RMSRestDataServer/rest/PtoDataSolicitarAbonoFuncionario

2- Preencha o "**Body"** da requisição com os dados desejados.

3- Enviar a requisição clicando em "**Send"**.

4- O abono será cadastrado com sucesso.

Se o usuário autenticado não for chefe ou supervisor externo do funcionário relacionado ao abono informado, o abono não será cadastrado.

3Método PUT

1- Informar o método: "**PUT"** e o "**Endpoint"**: "http://servidor:porta/RMSRestDataServer/rest/PtoDataSolicitarAbonoFuncionario/CodColigada$\_$idAbono".

2- Preencha o "**Body"** da requisição alterando os dados que deseja atualizar.

3- Enviar a requisição clicando em "**Send"**.

4- O abono será atualizado.

Se o usuário autenticado não for chefe ou supervisor externo do funcionário relacionado ao abono informado, o abono não será alterado.

4Método DELETE 

1- Informar o método: "**DELETE"** e o "**Endpoint"**: "http://servidor:porta/RMSRestDataServer/rest/PtoDataSolicitarAbonoFuncionario/CodColigada$\_$idAbono".

2- Enviar a requisição clicando em "**Send"**.

3- O abono será deletado.

Se o usuário autenticado não for chefe ou supervisor externo do funcionário relacionado ao abono informado, o abono não será excluído.
