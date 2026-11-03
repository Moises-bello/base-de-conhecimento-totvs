---
content_hash: 369a9dad507339712b604d4c50725b139e9e748bb2a16cdf17800858f6e3b95a
fetched_at: '2026-06-29T00:12:03.520069+00:00'
page_id: '910682104'
product: rm
source: tdn-rm
title: Tabela de Preço - openAPI
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=910682104
version: 91
---

Disponibilização da Funcionalidade 

A funcionalidade da Tabela de Preço estará disponível a partir de Fevereiro de 2026 - **Em breve as versões e Patchs onde o recurso estará disponível serão publicados nestes documento.**

# Sumário

---

Sumário

# Objetivo

---

Esse documento tem o objetivo de exemplificar o uso da API da  utilizando todos os métodos implementados. E as api's complementares referente às matrizes aplicadas e aos períodos letivos de ingresso associados à tabela de preço. Para a utilização das api's é importante observar a responsabilidade e o papel de cada uma no cadastro e manutenção das informações da tabela de preços.

A API da tabela de preço tem a responsabilidade de realizar a manutenção das informações da própria tabela de preço e das suas matrizes aplicadas e dos seus períodos letivos de ingressos associados à ela. Não sendo possível inserir, alterar ou remover os dados das disciplinas associadas às matrizes aplicadas. Essa manipulação será de responsabilidade da api da matriz aplicada.

A API da matriz aplicada tem a responsabilidade de realizar a manutenção das informações da matriz aplicada e das disciplinas vinculadas à ela. Nessa api será possível alterar e remover a matriz aplicada. E inserir, alterar e remover os dados das disciplinas vinculadas à matriz aplicada. Nessa api não será possível inserir uma nova matriz aplicada na tabela de preço, essa responsabilidade está na api da tabela de preço.

A API do período letivo de ingresso tem a responsabilidade de realizar somente a remoção do período letivo de ingresso na tabela de preço. A responsabilidade a inclusão e alteração do período letivo de ingresso na tabela de preço está na própria api da tabela de preço.

# 1 - Tabela de Preço

---

      Serão apresentados 5 métodos, os quais foram implementados na API da Tabela de Preço, são eles:

* GET
* POST
* PUT
* DELETE

## 1.1 - GET

---

### 1.1.1 - Get All (Recuperar todas as tabelas de preços)

falseGetAll

Recupera todas as tabelas de preços sem retornar as listagens das matrizes aplicadas, dos períodos letivos de ingresso por questão de performance. Essas informações serão retornadas com a utilização do GetOne para tabela de preço informada.

**Máscara de Url:** http://{domínio}:{porta}/api/educational/financial/v1/pricetable

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Url Utilizada:** [http://localhost:8051/api/educational/financial/v1/pricetable](http://localhost:8051/api/educational/v1/prospection/prospections)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

### 1.1.2 - Filter (Resultado filtrado)

falseFilter

**Máscara de Url:** http://{domínio}:{porta}/api/educational/financial/v1/pricetable?{campo}={valor}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** code

**Valor:** 00001

**Url Utilizada:** [http://localhost:8051/api/educational/financial/v1/pricetable?code=00001](http://localhost:8051/api/educational/v1/prospection/prospections)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)trueFiltros Complexos - OData

Para realizar filtros complexos na API da Tabela de Preço é possível adotar o padrão OData. Para entender melhor sobre a utilização desse padrão, acesse o link da documentação [Utilizando filtros complexos - Exemplos do guia de API - ODATA](https://tdn.totvs.com/display/LRM/Utilizando+Filtros+Complexos+-+Exemplos+do+guia+de+API+-+ODATA).

### 1.1.3 - Paginação

Parâmetros

**Page:** Página que será apresentada.

**PageSize**: Quantidade máxima de registros por página que serão apresentados.

**Exemplo:** ?page=1&pageSize=1

**Valores padrão:** Caso não sejam preenchidos os parâmetros evidenciados acima serão preenchidos com valores padrão.

**Page:** 1

**PageSize:** 20

falsePaginação

**Máscara de Url:** http://{domínio}:{porta}/api/educational/financial/v1/pricetable?page={valor1}&pageSize={valor2}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Valor1:** 1

**Valor2:** 5

**Url Utilizada:** [http://localhost:8051/api/educational/financial/v1/pricetable?](http://localhost:8051/api/educational/v1/prospection/prospections)[page=1&pageSize=5](http://localhost:8051/api/educational/v1/prospection/prospections?page=1&pageSize=1)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

### 1.1.4 - Fields (Retorno de campos específicos no resultado)

Parâmetros

**Fields:** parâmetro responsável pela especialização de campos em um resultado, ou seja, o usuário define quais campos serão apresentados no resultado.

**Exemplo:** ?fields=campo1

**Múltiplos campos de ordenação:** ?fields=campo1, campo2, campo3 ...

falseFields

**Máscara de Url:** http://{domínio}:{porta}/api/educational/financial/v1/pricetable?fields={campos}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo 1:** code

**Campo 2:** name

**Url Utilizada:** [http://localhost:8051/api/educational/financial/v1/pricetable](http://localhost:8051/api/educational/v1/prospection/prospections)?[fields=code,name](http://localhost:8051/api/educational/v1/prospection/prospections?fields=prospectionCode,description)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

### 1.1.5 - GetOne (Recuperar tabela de preço pelo identificador)

falseGetOne

Nessa requisição serão retornadas as listagens das matrizes aplicadas, dos períodos letivos de ingresso da tabela de preço informada

**Máscara de Url:** http://{domínio}:{porta}/api/educational/financial/v1/pricetable/{internalId}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**internalId:** 1|1|3

**Url Utilizada:** [http://localhost:8051/api/educational/financial/v1/pricetable/1|1|3](http://localhost:8051/api/educational/v1/prospection/prospections/1)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.2 - POST

---

### 1.2.1 - Post (Inserir uma tabela de preço)

falsePost

A inclusão de uma nova tabela de preço será feita contendo os seus dados, e os dados das suas matrizes aplicadas vinculadas. Não sendo possível inserir a tabela de preço com suas matrizes aplicadas contendo suas disciplinas, e os períodos letivos de ingresso dessa tabela de preço. Essas informações serão inseridas em outras api's com essa responsabilidade.

**Máscara de Url:** http://{domínio}:{porta}/api/educational/financial/v1/pricetable

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Url Utilizada:** [http://localhost:8051/api/educational/financial/v1/pricetable](http://localhost:8051/api/educational/v1/prospection/prospections)

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true

## 1.3 - PUT

---

### 1.3.1 - Put (Atualização de uma tabela de preço)

falsePatch

A atualização da tabela de preço será feita contendo os seus dados e os dados das suas matrizes aplicadas, e os dados dos seus períodos letivos de ingresso.  E a inclusão de novos períodos letivos de ingresso. Não sendo possível inserir a tabela de preço com suas matrizes aplicadas contendo suas disciplinas. Essas informações serão inseridas em outras api's com essa responsabilidade.

**Máscara de Url:** http://{domínio}:{porta}/api/educational/financial/v1/pricetable/{internalId}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**internalId:** 1|1|14

**Url Utilizada:** [http://localhost:8051/api/educational/financial/v1/pricetable/1|1|14](http://localhost:8051/api/educational/v1/prospection/prospections/3)

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true

## 1.4 - DELETE

---

### 1.4.1 - Delete (Excluir uma tabela de preço)

falseDelete

**Máscara de Url:** http://{domínio}:{porta}/api/educational/financial/v1/pricetable/{internalId}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**internalId:** 1|1|20

**Url Utilizada:** [http://localhost:8051/api/educational/financial/v1/pricetable/1|1|20](http://localhost:8051/api/educational/v1/prospection/prospections/5)

falseExemplo de Resultado Positivo Postman

Obs.: Em caso de sucesso, será retornado o respondeCode = 204 e a resposta em branco.

falseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true

# 2 - Matriz Aplicada

---

      Serão apresentados 3 métodos, os quais foram implementados na API da Matriz Aplicada vinculada à Tabela de Preço, são eles:

* GET
* PUT
* DELETE

## 2.1 - GET

---

### 2.1.1 - Get All (Recuperar todas as matrizes aplicadas)

falseGetAll

Recupera todas as matrizes aplicadas sem retornar a listagem das disciplinas vinculadas por questão de performance. Essas informações serão retornadas com a utilização do GetOne para a matriz aplicada informada.

**Máscara de Url:** http://{domínio}:{porta}/api/educational/financial/v1/pricetableappliedmatrixes

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Url Utilizada:** [http://localhost:8051/api/educational/financial/v1/pricetableappliedmatrixes](http://localhost:8051/api/educational/v1/prospection/prospections)

falseExemplo de ResultadoVer resultado JSON...

{  
    "hasNext": false,  
    "items": [  
        {  
            "companyCode": 1,  
            "branchCode": 1,  
            "levelEducationCode": 1,  
            "appliedMatrixCode": 132,  
            "priceTableCode": 3,  
            "branchName": "Filial Belo Horizonte - Fantasia",  
            "courseCode": "1-1",  
            "courseName": "Curso Tabela de Preço",  
            "curriculumGridCode": "1",  
            "curriculumGridName": "Matriz Tabela de Preço",  
            "majorCode": "1",  
            "majorName": "Habilitação  Tabela de Preço",  
            "classShiftCode": 11,  
            "classShiftName": "INTEGRAL",  
            "status": 0,  
            "disciplines": [],  
            "actionState": 0  
        }  
    ]  
}

### 2.1.2 - Filter (Resultado filtrado)

falseFilter

**Máscara de Url:** http://{domínio}:{porta}/api/educational/financial/v1/pricetableappliedmatrixes?{campo}={valor}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** courseCode

**Valor:** 1-1

**Url Utilizada:**  [http://localhost:8051/api/educational/financial/v1/pricetableappliedmatrixes?courseCode=1-1](http://localhost:8051/api/educational/v1/prospection/prospections)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)trueFiltros Complexos - OData

Para realizar filtros complexos na API da Matriz Aplicada é possível adotar o padrão OData. Para entender melhor sobre a utilização desse padrão, acesse o link da documentação [Utilizando filtros complexos - Exemplos do guia de API - ODATA](https://tdn.totvs.com/display/LRM/Utilizando+Filtros+Complexos+-+Exemplos+do+guia+de+API+-+ODATA).

### 2.1.3 - Paginação

Parâmetros

**Page:** Página que será apresentada.

**PageSize**: Quantidade máxima de registros por página que serão apresentados.

**Exemplo:** ?page=1&pageSize=1

**Valores padrão:** Caso não sejam preenchidos os parâmetros evidenciados acima serão preenchidos com valores padrão.

**Page:** 1

**PageSize:** 20

falsePaginação

**Máscara de Url:** http://{domínio}:{porta}/api/educational/financial/v1/pricetableappliedmatrixes?page={valor1}&pageSize={valor2}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Valor1:** 1

**Valor2:** 5

**Url Utilizada:** [http://localhost:8051/api/educational/financial/v1/pricetableappliedmatrixes?page=1&pageSize=5](http://localhost:8051/api/educational/v1/prospection/prospections)

falseExemplo de ResultadoVer resultado JSON...

{  
    "hasNext": true,  
    "items": [  
        {  
            "companyCode": 1,  
            "branchCode": 1,  
            "levelEducationCode": 1,  
            "appliedMatrixCode": 7,  
            "priceTableCode": 3,  
            "branchName": "Filial Belo Horizonte - Fantasia",  
            "courseCode": "3-1",  
            "courseName": "ADMINISTRAÇÃO",  
            "curriculumGridCode": "4",  
            "curriculumGridName": "2004/1",  
            "majorCode": "1",  
            "majorName": "COMÉRCIO EXTERIOR",  
            "classShiftCode": 1,  
            "classShiftName": "MANHÃ",  
            "status": 0,  
            "disciplines": [],  
            "actionState": 0  
        },  
        {  
            "companyCode": 1,  
            "branchCode": 1,  
            "levelEducationCode": 1,  
            "appliedMatrixCode": 8,  
            "priceTableCode": 3,  
            "branchName": "Filial Belo Horizonte - Fantasia",  
            "courseCode": "3-1",  
            "courseName": "ADMINISTRAÇÃO",  
            "curriculumGridCode": "4",  
            "curriculumGridName": "2004/1",  
            "majorCode": "1",  
            "majorName": "COMÉRCIO EXTERIOR",  
            "classShiftCode": 2,  
            "classShiftName": "TARDE",  
            "status": 0,  
            "disciplines": [],  
            "actionState": 0  
        },  
        {  
            "companyCode": 1,  
            "branchCode": 1,  
            "levelEducationCode": 1,  
            "appliedMatrixCode": 9,  
            "priceTableCode": 3,  
            "branchName": "Filial Belo Horizonte - Fantasia",  
            "courseCode": "3-1",  
            "courseName": "ADMINISTRAÇÃO",  
            "curriculumGridCode": "4",  
            "curriculumGridName": "2004/1",  
            "majorCode": "1",  
            "majorName": "COMÉRCIO EXTERIOR",  
            "classShiftCode": 3,  
            "classShiftName": "NOITE",  
            "status": 0,  
            "disciplines": [],  
            "actionState": 0  
        },  
        {  
            "companyCode": 1,  
            "branchCode": 1,  
            "levelEducationCode": 1,  
            "appliedMatrixCode": 10,  
            "priceTableCode": 3,  
            "branchName": "Filial Belo Horizonte - Fantasia",  
            "courseCode": "3-1",  
            "courseName": "ADMINISTRAÇÃO",  
            "curriculumGridCode": "4",  
            "curriculumGridName": "2004/1",  
            "majorCode": "4",  
            "majorName": "RECURSOS HUMANOS",  
            "classShiftCode": 1,  
            "classShiftName": "MANHÃ",  
            "status": 0,  
            "disciplines": [],  
            "actionState": 0  
        },  
        {  
            "companyCode": 1,  
            "branchCode": 1,  
            "levelEducationCode": 1,  
            "appliedMatrixCode": 11,  
            "priceTableCode": 3,  
            "branchName": "Filial Belo Horizonte - Fantasia",  
            "courseCode": "3-1",  
            "courseName": "ADMINISTRAÇÃO",  
            "curriculumGridCode": "4",  
            "curriculumGridName": "2004/1",  
            "majorCode": "4",  
            "majorName": "RECURSOS HUMANOS",  
            "classShiftCode": 2,  
            "classShiftName": "TARDE",  
            "status": 0,  
            "disciplines": [],  
            "actionState": 0  
        },  
        {  
            "companyCode": 1,  
            "branchCode": 1,  
            "levelEducationCode": 1,  
            "appliedMatrixCode": 12,  
            "priceTableCode": 3,  
            "branchName": "Filial Belo Horizonte - Fantasia",  
            "courseCode": "3-1",  
            "courseName": "ADMINISTRAÇÃO",  
            "curriculumGridCode": "4",  
            "curriculumGridName": "2004/1",  
            "majorCode": "4",  
            "majorName": "RECURSOS HUMANOS",  
            "classShiftCode": 3,  
            "classShiftName": "NOITE",  
            "status": 0,  
            "disciplines": [],  
            "actionState": 0  
        }  
    ]  
}

### 2.1.4 - Fields (Retorno de campos específicos no resultado)

Parâmetros

**Fields:** parâmetro responsável pela especialização de campos em um resultado, ou seja, o usuário define quais campos serão apresentados no resultado.

**Exemplo:** ?fields=campo1

**Múltiplos campos de ordenação:** ?fields=campo1, campo2, campo3 ...

falseFields

**Máscara de Url:** http://{domínio}:{porta}/api/educational/financial/v1/pricetableappliedmatrixes?fields={campos}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo 1:** code

**Campo 2:** name

**Url Utilizada:** [http://localhost:8051/api/educational/financial/v1/pricetableappliedmatrixes?fields=courseName,courseCode](http://localhost:8051/api/educational/v1/prospection/prospections)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

### 2.1.5 - GetOne (Recuperar matriz aplicada pelo identificador)

falseGetOne

Nessa requisição será retornada a matriz aplicada e suas das disciplinas vinculadas.

**Máscara de Url:** http://{domínio}:{porta}/api/educational/financial/v1/pricetableappliedmatrixes/{internalId}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**internalId:** 1|1|3|132

**Url Utilizada:** [http://localhost:8051/api/educational/financial/v1/pricetableappliedmatrixes/1|1|3|132](http://localhost:8051/api/educational/v1/prospection/prospections)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 2.2 - PUT

---

### 2.2.1 - Put (Atualização de uma matriz aplicada)

falsePatch

A atualização da matriz aplicada é realizada somente para atualizar as disciplinas vinculadas à matriz aplicada. E importante no corpo da requisição informar a propriedade "actionState" na tag "disciplines"  a ação que deseja conforme descrito na seção "Descrição dos campos JSON de entrada/retorno"

**Máscara de Url:** http://{domínio}:{porta}/api/educational/financial/v1/pricetableappliedmatrixes/{internalId}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**internalId:** 1|1|3|132

**Url Utilizada:** [http://localhost:8051/api/educational/financial/v1/pricetableappliedmatrixes/1|1|3|132](http://localhost:8051/api/educational/v1/prospection/prospections)

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado NegativoVer resultado JSON...

{  
    "code": null,  
    "message": "Não foi possível incluir/editar a tabela de preço. Existe(m) matriz(es) aplicada(s) com id da matriz aplicada inválido.",  
    "detailedMessage": null,  
    "helpUrl": null,  
    "details": null  
}

## 2.3 - DELETE

---

### 2.3.1 - Delete (Excluir uma matriz aplicada)

falseDelete

**Máscara de Url:** http://{domínio}:{porta}/api/educational/financial/v1/pricetableappliedmatrixes/{internalId}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**internalId:** 1|1|3|132

**Url Utilizada:** [http://localhost:8051/api/educational/financial/v1/pricetableappliedmatrixes/1|1|3|132](http://localhost:8051/api/educational/v1/prospection/prospections)

falseExemplo de Resultado Positivo Postman

Obs.: Em caso de sucesso, será retornado o respondeCode = 204 e a resposta em branco.

falseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true

# 3 - Período Letivo de Ingresso

---

      Serão apresentados 2 métodos, os quais foram implementados na API do Período de Letivo de Ingresso vinculada à Tabela de Preço, são eles:

* GET
* DELETE

## 3.1 - GET

---

### 3.1.1 - Get All (Recuperar todos períodos de letivo de ingresso)

falseGetAll

**Máscara de Url:** http://{domínio}:{porta}/api/educational/financial/v1/pricetableterms

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Url Utilizada:** [http://localhost:8051/api/educational/financial/v1/pricetableterms](http://localhost:8051/api/educational/v1/prospection/prospections)

falseExemplo de Resultado

{  
    "hasNext": false,  
    "items": [  
        {  
            "internalId": "1|1|3|73",  
            "companyCode": 1,  
            "priceTableCode": 3,  
            "termId": 73,  
            "levelEducationCode": 1,  
            "termCode": "2024/1",  
            "branchCode": 1,  
            "branchName": "Filial Belo Horizonte - Fantasia"  
        },  
        {  
            "internalId": "1|1|3|74",  
            "companyCode": 1,  
            "priceTableCode": 3,  
            "termId": 74,  
            "levelEducationCode": 1,  
            "termCode": "2024/2",  
            "branchCode": 1,  
            "branchName": "Filial Belo Horizonte - Fantasia"  
        },  
        {  
            "internalId": "1|1|3|75",  
            "companyCode": 1,  
            "priceTableCode": 3,  
            "termId": 75,  
            "levelEducationCode": 1,  
            "termCode": "2025/1",  
            "branchCode": 1,  
            "branchName": "Filial Belo Horizonte - Fantasia"  
        }  
    ]  
}

### 3.1.2 - Filter (Resultado filtrado)

falseFilter

**Máscara de Url:** http://{domínio}:{porta}/api/educational/financial/v1/pricetableterms?{campo}={valor}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** termId

**Valor:** 74

**Url Utilizada:**  [http://localhost:8051/api/educational/financial/v1/pricetableterms?termId=74](http://localhost:8051/api/educational/v1/prospection/prospections)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)trueFiltros Complexos - OData

Para realizar filtros complexos na API do Período Letivo de Ingresso é possível adotar o padrão OData. Para entender melhor sobre a utilização desse padrão, acesse o link da documentação [Utilizando filtros complexos - Exemplos do guia de API - ODATA](https://tdn.totvs.com/display/LRM/Utilizando+Filtros+Complexos+-+Exemplos+do+guia+de+API+-+ODATA).

### 3.1.3 - Paginação

Parâmetros

**Page:** Página que será apresentada.

**PageSize**: Quantidade máxima de registros por página que serão apresentados.

**Exemplo:** ?page=1&pageSize=1

**Valores padrão:** Caso não sejam preenchidos os parâmetros evidenciados acima serão preenchidos com valores padrão.

**Page:** 1

**PageSize:** 20

falsePaginação

**Máscara de Url:** http://{domínio}:{porta}/api/educational/financial/v1/pricetableterms?page={valor1}&pageSize={valor2}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Valor1:** 1

**Valor2:** 5

**Url Utilizada:** [http://localhost:8051/api/educational/financial/v1/pricetableterms?page=1&pageSize=5](http://localhost:8051/api/educational/v1/prospection/prospections)

falseExemplo de ResultadoVer resultado JSON...

{  
    "hasNext": false,  
    "items": [  
        {  
            "internalId": "1|1|3|73",  
            "companyCode": 1,  
            "priceTableCode": 3,  
            "termId": 73,  
            "levelEducationCode": 1,  
            "termCode": "2024/1",  
            "branchCode": 1,  
            "branchName": "Filial Belo Horizonte - Fantasia"  
        },  
        {  
            "internalId": "1|1|3|74",  
            "companyCode": 1,  
            "priceTableCode": 3,  
            "termId": 74,  
            "levelEducationCode": 1,  
            "termCode": "2024/2",  
            "branchCode": 1,  
            "branchName": "Filial Belo Horizonte - Fantasia"  
        },  
        {  
            "internalId": "1|1|3|75",  
            "companyCode": 1,  
            "priceTableCode": 3,  
            "termId": 75,  
            "levelEducationCode": 1,  
            "termCode": "2025/1",  
            "branchCode": 1,  
            "branchName": "Filial Belo Horizonte - Fantasia"  
        }  
    ]  
}

### 3.1.4 - Fields (Retorno de campos específicos no resultado)

Parâmetros

**Fields:** parâmetro responsável pela especialização de campos em um resultado, ou seja, o usuário define quais campos serão apresentados no resultado.

**Exemplo:** ?fields=campo1

**Múltiplos campos de ordenação:** ?fields=campo1, campo2, campo3 ...

falseFields

**Máscara de Url:** http://{domínio}:{porta}/api/educational/financial/v1/pricetableterms?fields={campos}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo 1:** termCode

**Campo 2:** branchName

**Url Utilizada:** [http://localhost:8051/api/educational/financial/v1/pricetableterms?fields=termCode,branchName](http://localhost:8051/api/educational/v1/prospection/prospections)

falseExemplo de ResultadoVer resultado JSON...

{  
    "hasNext": false,  
    "items": [  
        {  
            "termCode": "2024/1",  
            "branchName": "Filial Belo Horizonte - Fantasia"  
        },  
        {  
            "termCode": "2024/2",  
            "branchName": "Filial Belo Horizonte - Fantasia"  
        },  
        {  
            "termCode": "2025/1",  
            "branchName": "Filial Belo Horizonte - Fantasia"  
        }  
    ]  
}

### 3.1.5 - GetOne (Recuperar período letivo de ingresso pelo identificador)

falseGetOne

**Máscara de Url:** http://{domínio}:{porta}/api/educational/financial/v1/pricetableterms/{internalId}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**internalId:** 1|1|3|73

**Url Utilizada:** [http://localhost:8051/api/educational/financial/v1/pricetableterms/1|1|3|73](http://localhost:8051/api/educational/v1/prospection/prospections)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 3.2 - DELETE

---

### 3.2.1 - Delete (Excluir um período letivo de ingresso)

falseDelete

**Máscara de Url:** http://{domínio}:{porta}/api/educational/financial/v1/pricetableterms/{internalId}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**internalId:** 1|1|3|73

**Url Utilizada:** [http://localhost:8051/api/educational/financial/v1/pricetableterms/1|1|3|73](http://localhost:8051/api/educational/v1/prospection/prospections)

falseExemplo de Resultado Positivo Postman

Obs.: Em caso de sucesso, será retornado o respondeCode = 204 e a resposta em branco.

falseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true

# 4 - Reajuste de valores

---

      Nesta sessão serão apresentadas as três APIs principais usadas no reajuste de valores.

* GET - http://{domínio}:{porta}/api/educational/v1/financial/pricetablebranchesandterms (Responsável por retornar lista de filiais e os períodos letivos disponíveis para seleção por filial)
* POST - http://{domínio}:{porta}/api/educational/v1/financial/simulation/pricetablereadjustment (Responsável pela simulação do reajuste de valores)
* POST - http://{domínio}:{porta}/api/educational/v1/financial/pricetableadjustment (Processa o reajuste de valores)

## 4.1 - Obter filiais e períodos letivos

---

### 4.1.1 - Get All (Recuperar todas filiais e todos períodos disponíveis para uso no reajuste)

falseGetAll

**Máscara de Url:** http://{domínio}:{porta}/api/educational/v1/financial/pricetablebranchesandterms/{tabelaDePrecoInternalId};{tabelaDePrecoInternalId};{tabelaDePrecoInternalId};

**Obs**: Para execução é obrigatório informar pelos menos 1 internalId de tabela de preço e no máximo 20 internalId de tabela de preço. Cada internalId deve ser separado por ';'.

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**internalId:** 1|1|23

**internalId:** 1|1|24

**Url Utilizada:** [http://localhost:8051/api/educational/v1/financial/pricetablebranchesandterms?1|1|23;1|1|24](http://bhn050104662.bh01.local:8052/api/educational/v1/financial/pricetablebranchesandterms?1|1|23;1|1|24)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 4.2 - Simular reajuste de valores

---

### 4.2.1 - POST (Executa simulação do reajuste por matriz aplicada)

falsePOST

A simulação é realizada por matriz aplicada da tabela de preço, seu retorno é como os valores devem ficar após o reajuste.

**Máscara de Url:** http://{domínio}:{porta}/api/educational/v1/financial/simulation/pricetablereadjustment

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Url Utilizada:** [http://localhost:8051/api/educational/v1/financial/simulation/pricetablereadjustment/](http://bhn050104662.bh01.local:8052/api/educational/v1/financial/pricetablebranchesandterms?1|1|23;1|1|24)

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado com sucesso (201 - Created)Ver resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado com falha - (500 Internal server error)Ver resultado JSON...js1Resultado (JSON)true

## 4.3 - Processar reajuste de valores

---

### 4.3.1 - POST (Processa reajuste de valores)

falsePOST

Efetua o reajuste dos valores da tabela de preço.

**Máscara de Url:** http://{domínio}:{porta}/api/educational/v1/financial/pricetableadjustment/

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Url Utilizada:** [http://localhost:8051/api/educational/v1/financial/pricetableadjustment/](http://bhn050104662.bh01.local:8052/api/educational/v1/financial/pricetablebranchesandterms?1|1|23;1|1|24)

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado com sucesso (201 - Created)Ver resultado JSON...js1Resultado (JSON)true

# 5 - Processo vínculo Matriz Aplicada e Campus/Polo da Matriz Aplicada

---

O vínculo da tabela de preço como default para a matriz aplicada e/ou campus/polo da matriz aplicada, pode ser realizada pelo método POST da API de [JobScheduler](https://tdn.totvs.com/display/public/LRM/API+de+JobScheduler#APIdeJobScheduler-1.2.1-Post(Inserirumagendamentodejob)).

falsePost

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/jobscheduler

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Url Utilizada:** <http://localhost:8051/api/framework/v1/jobscheduler>

falseExemplo de entrada 3 camadas

Caso a propriedade recurrent seja igual a true, obrigatoriamente deve-se informar o [Tipo de Recorrência](https://tdn.totvs.com/display/public/LRM/API+de+JobScheduler#APIdeJobScheduler-recurrencyType).

**Propriedades obrigatórias:**

processID, firstExecution, recurrent, executionParameter

executionParameter: Context, ProcessName, UserName, PrimaryKeyList, PrimaryKeyNames

Ver resultado JSON...js1Resultado (JSON)truefalseExemplo de entrada ambiente local

Se o Host estiver executando local (3camadas = false) não é possível criar um agendamento de job. Neste cenário, para executar o job imediatamente, é preciso que no Body da requisição a recorrência esteja como 'false' e não sejam enviadas as propriedades "ScheduleDateTime" e [Tipo de Recorrência](https://tdn.totvs.com/display/public/LRM/API+de+JobScheduler#APIdeJobScheduler-recurrencyType).

**Propriedades obrigatórias:**

processID, recurrent, executionParameter

executionParameter: Context, ProcessName, UserName, PrimaryKeyList, PrimaryKeyNames

Ver resultado JSON...js1Resultado (JSON)truefalseExemplo de resultado positivoVer resultado JSON...js1Resultado (JSON)truefalseExemplo de resultado negativoVer resultado JSON...js1Resultado (JSON)true

# 6 - Descrição dos campos JSON de entrada/retorno

---

Descrição dos campos JSON de entrada/retorno

**Tabela de Preço**

* companyCode: Código da coligada
* levelEducationCode: Código do nível de ensino/tipo de curso
* id: Identificador único da tabela de preço
* internalId: Identificador da tabela de preço no formato:
  + "Código da Coligada | Código do Nível de Ensino | Identificador da Tabela de Preço"
* code: Código da tabela de preço definido pelo usuário no sistema
* name: Nome da tabela de preço
* reccreatedon: Data de criação da tabela de preço
* active: Informa se a tabela de preço está ativa
* pricetableinuse: Informa se a tabela de preço está em uso
* appliedMatrixes: Listagem das matrizes aplicadas vinculadas à tabela de preço
* terms: Listagem dos período letivos de ingresso vinculados à tabela de preço

**Matriz Aplicada vinculada à Tabela de Preço**

* companyCode: Código da coligada
* branchCode: Código da filial
* levelEducationCode: Código do nível de ensino/tipo de curso
* appliedMatrixCode: Identificador da matriz aplicada
* priceTableCode: Identificador da tabela de preço
* branchName: Nome da filial
* courseCode: Código do curso
* courseName: Nome do curso
* curriculumGridCode: Código da grade/matriz curricular
* curriculumGridName: Nome da grade/matriz curricular
* majorCode: Código da habilitação
* majorName: Nome da habilitação
* classShiftCode: Código do turno
* classShiftName: Nome do turno
* Status: Informar o status do preenchimento do valor de créditos da disciplinas, valores possíveis
  + 0: Informa que todas as disciplinas não tem o valor de créditos preenchido
  + 1: Informa que têm algumas disciplinas sem ter o valor de créditos preenchido
  + 2: Informa que todas as disciplinas já tem o valor de créditos preenchido
* disciplines: Listagem das disciplinas vinculadas a matriz aplicada
* actionState: Informar o controle de modificação
  + 1: Informa a inclusão da matriz aplicada na tabela de preço
  + 2: Informa a remoção da matriz aplicada na tabela de preço

**Disciplina vinculada à Matriz Aplicada**

* companyCode: Código da coligada
* priceTableCode: Identificador da tabela de preço
* appliedMatrixCode: Identificador da matriz aplicada
* levelEducationCode: Código do nível de ensino/tipo de curso
* internalId: Identificador da disciplina no formato:
  + "Código da Coligada | Identificador da Tabela de Preço | Identificador da Matriz Aplicada | Código do Nível de Ensino | Código da Disciplina"
* disciplineCode: Código da disciplina
* creditsValue: Valor de créditos
* periodCode: Código do período
* periodDescription: Descrição do período
* disciplineName: Nome da disciplina
* workload: Número da carga horária da disciplina
* actionState: Informar o controle de modificação
  + 1: Informa a inclusão da disciplina da matriz aplicada
  + 2: Informa a remoção da disciplina da matriz aplicada
  + 3: Informa a modificação da disciplina da matriz aplicada
* recCreatedBy: Usuário de criação
* recCreatedOn: Data de criação
* recModifiedBy: Usuário de alteração
* recModifiedOn: Data de alteração

**Período Letivo de Ingresso vinculado à Matriz Aplicada**

* companyCode: Código da coligada
* priceTableCode: Identificador da tabela de preço
* levelEducationCode: Código do nível de ensino/tipo de curso
* termId: identidicador do período letivo de ingresso
* internalId: Identificador da disciplina no formato:
  + "Código da Coligada|Identificador da Tabela de Preço|Identificador do Período Letivo de Ingresso|Código do Nível de Ensino"
* termCode: Código do período letivo de ingresso definido pelo usuário no sistema
* branchName: Nome da filial
* branchCode: Código da filial
* actionState: Informar o controle de modificação
  + 1: Informa a inclusão do período letivo de ingresso na tabela de preço
  + 2: Informa a remoção do período letivo de ingresso na tabela de preço
* recCreatedBy: Usuário de criação
* recCreatedOn: Data de criação
* recModifiedBy: Usuário de alteração
* recModifiedOn: Data de alteração

**Processo vínculo Matriz Aplicada e/ou Campus/Polo da Matriz Aplicada**

* processID: Indentificador do processo no RM
  + Informar "EduVinculaTabelaPrecoMatrizAplicadaData"
* firstExecution: Data da primeira execução do processo agendado
* recurrent: Indica se a execução do processo é recorrente
* executionParameter: Parâmetros de execução
  + Context: Contexto
    - \_params
      * $CODCOLIGADA: Código da coligada
      * $CODFILIAL: Código da filial
      * $CODTIPOCURSO: Código do nível de ensino
      * $CODUSUARIO: Código do usuário
      * $CODSISTEMA: Código do sistema
        + Informar "S"
  + ProcessName: Nome do processo
    - Informar "Vinculo Matriz Aplicada e Campus/Polo"
  + UserName: Nome do usuário
  + PrimaryKeyList: Chave primária da tabela de preço
    - "Código da Coligada | Código do Nível de Ensino | Identificador da Tabela de Preço"
  + PrimaryKeyNames: Nome da chave primária da tabela de preço
    - Informar "internalId"
  + HostName: Nome do host
  + appliedMatrixCodeList: Lista de códigos da matriz aplicada
  + appliedMatrixCampusCodeList: Lista de códigos do campus/polo da matriz aplicada
    - "Identificador da matriz aplicada | Código do campus/polo"
* daily: Utilizar somente se recurrent = true e o tipo de recorrência for diária. Consultar [Tipo de Recorrência](https://tdn.totvs.com/display/public/LRM/API+de+JobScheduler#APIdeJobScheduler-recurrencyType).
  + year: Ano
  + month: Mês
  + day: Dia
  + hour: Hora
  + minute: minuto
* weekly: Utilizar somente se recurrent = true e o tipo de recorrência for semanal. Consultar [Tipo de Recorrência](https://tdn.totvs.com/display/public/LRM/API+de+JobScheduler#APIdeJobScheduler-recurrencyType).
  + daysOfWeek: Lista de dias da semana
  + hour: Hora
  + minute: Minutos
* monthly: Utilizar somente se recurrent = true e o tipo de recorrência for mensal. Consultar [Tipo de Recorrência](https://tdn.totvs.com/display/public/LRM/API+de+JobScheduler#APIdeJobScheduler-recurrencyType).
  + day: Dia
  + hour: Hora
  + minute: minuto
