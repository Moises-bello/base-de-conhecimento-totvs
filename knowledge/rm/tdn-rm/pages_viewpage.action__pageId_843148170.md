---
content_hash: 3e547b0db26b3387b4500b5557ea6ce45999b07103f2155dda2c3b26c9d4aa50
fetched_at: '2026-06-29T00:11:50.609454+00:00'
page_id: '843148170'
product: rm
source: tdn-rm
title: Prospecção (openAPI)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=843148170
version: 9
---

# Sumário

---

Sumário

# Objetivo

---

      Esse documento tem o objetivo de exemplificar o uso da API de Prospecção utilizando todos os métodos implementados.

# 1 - Métodos

---

      Serão apresentados 5 métodos, os quais foram implementados na API de Prospecção, são eles:

* GET
* POST
* PUT
* DELETE

# 1.1 - GET

---

## 1.1.1 - Get All (Recuperar todas as Prospecções)

falseGetAll

**Máscara de Url:** http://{domínio}:{porta}/api/educational/v1/prospection/prospections

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Url Utilizada:** <http://localhost:8051/api/educational/v1/prospection/prospections>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.2 - Order (Retorna os dados ordenados)

Parâmetros

**Order:** parâmetro responsável pela ordenação do resultado, podendo ser ascendente ou descendente. O resultado com a ordem descendente deve ser precedida do caractere "-" (menos).

**Exemplo 1:** ?order=campo1 (Ascendente)

**Exemplo 2:** ?order=-campo1 (Descendente)

**Múltiplos campos de ordenação:** ?order=[-]campo1, [-]campo2, [-]campo3 ...

falseOrder (Asc)

**Máscara de Url:** http://{domínio}:{porta}/api/educational/v1/prospection/prospections?order={campo}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** description

**Tipo de Ordenação:** Ascendente

**Url Utilizada:** <http://localhost:8051/api/educational/v1/prospection/prospections?order=description>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)truefalseOrder (Desc)

**Máscara de Url:** http://{domínio}:{porta}/api/educational/v1/prospection/prospections?order=[-]{campo}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** description

**Tipo de Ordenação:** Descendente

**Url Utilizada:** <http://localhost:8051/api/educational/v1/prospection/prospections?order=-description>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.3 - Filter (Resultado filtrado)

---

falseFilter

**Máscara de Url:** http://{domínio}:{porta}/api/educational/v1/prospection/prospections?{campo}={valor}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** bankNumber

**Valor:** 005

**Url Utilizada:** <http://localhost:8051/api/educational/v1/prospection/prospections?prospectionCode=2>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)trueFiltros Complexos - OData

Para realizar filtros complexos na API de Prospecção é possível adotar o padrão OData. Para entender melhor sobre a utilização desse padrão, acesse o link da documentação [Utilizando filtros complexos - Exemplos do guia de API - ODATA](https://tdn.totvs.com/display/LRM/Utilizando+Filtros+Complexos+-+Exemplos+do+guia+de+API+-+ODATA).

## 1.1.4 - Paginação

---

Parâmetros

**Page:** Página que será apresentada.

**PageSize**: Quantidade máxima de registros por página que serão apresentados.

**Exemplo:** ?page=1&pageSize=1

**Valores padrão:** Caso não sejam preenchidos os parâmetros evidenciados acima serão preenchidos com valores padrão.

**Page:** 1

**PageSize:** 20

falsePaginação

**Máscara de Url:** http://{domínio}:{porta}/api/educational/v1/prospection/prospections?page={valor1}&pageSize={valor2}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Valor1:** 1

**Valor2:** 2

**Url Utilizada:** <http://localhost:8051/api/educational/v1/prospection/prospections?page=1&pageSize=1>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.5 - Fields (Retorno de campos específicos no resultado)

---

Parâmetros

**Fields:** parâmetro responsável pela especialização de campos em um resultado, ou seja, o usuário define quais campos serão apresentados no resultado.

**Exemplo:** ?fields=campo1

**Múltiplos campos de ordenação:** ?fields=campo1, campo2, campo3 ...

falseFields

**Máscara de Url:** http://{domínio}:{porta}/api/educational/v1/prospection/prospections?fields={campos}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo 1:** prospectionCode

**Campo 2:** description

**Url Utilizada:** <http://localhost:8051/api/educational/v1/prospection/prospections?fields=prospectionCode,description>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.6 - GetOne (Recuperar prospecção pelo identificador)

---

falseGetOne

**Máscara de Url:** http://{domínio}:{porta}/api/educational/v1/prospection/prospections/{prospectionCode}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**prospectionCode:** 1

**Url Utilizada:** <http://localhost:8051/api/educational/v1/prospection/prospections/1>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

# 1.2 - POST

---

## 1.2.1 - Post (Inserir uma Prospecção)

---

falsePost

**Máscara de Url:** http://{domínio}:{porta}/api/educational/v1/prospection/prospections

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Url Utilizada:** <http://localhost:8051/api/educational/v1/prospection/prospections>

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true

# 1.3 - PUT

---

## 1.3.1 - Put (Atualização de uma Prospecção)

---

falsePatch

**Máscara de Url:** http://{domínio}:{porta}/api/educational/v1/prospection/prospections/{prospectionCode}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**prospectionCode:** 3

**Url Utilizada:** <http://localhost:8051/api/educational/v1/prospection/prospections/3>

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true

# 1.4 - DELETE

---

## 1.4.1 - Delete (Exclui uma Prospecção)

---

falseDelete

**Máscara de Url:** http://{domínio}:{porta}/api/educational/v1/prospection/prospections/{prospectionCode}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**prospectionCode:** 5

**Url Utilizada:** <http://localhost:8051/api/educational/v1/prospection/prospections/5>

falseExemplo de Resultado Positivo Postman

Obs.: Em caso de sucesso, será retornado o respondeCode = 204 e a resposta em branco.

falseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true

## 1.4.2 - Delete (Exclui um Prospect da Prospecção)

---

falseDelete

**Máscara de Url:** http://{domínio}:{porta}/api/educational/v1/prospection/prospect/{prospectionCode}|{prospectCode}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**prospectionCode:** 3

**prospectCode:** 141

**Url Utilizada:** <http://localhost:8051/api/educational/v1/prospection/prospect/3|141>

falseExemplo de Resultado Positivo Postman

Obs.: Em caso de sucesso, será retornado o respondeCode = 204 e a resposta em branco.

falseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true

## 1.4.3 - Delete (Exclui um Plano de Pagamento do Prospect da Prospecção)

---

falseDelete

**Máscara de Url:** http://{domínio}:{porta}/api/educational/v1/prospect/paymentplan/{prospectionCode}|{prospectCode}|{prospectPaymentPlanCode}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**prospectionCode:** 3

**prospectCode:** 133

**prospectPaymentPlanCode**: 101

**Url Utilizada:** <http://localhost:8051/api/educational/v1/prospect/paymentplan/3|133|101>

falseExemplo de Resultado Positivo Postman

Obs.: Em caso de sucesso, será retornado o respondeCode = 204 e a resposta em branco.

falseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true

## 1.4.4 - Delete (Exclui uma Bolsa do Prospect da Prospecção)

---

falseDelete

**Máscara de Url:** http://{domínio}:{porta}/api/educational/v1/prospect/scholarship/{prospectionCode}|{prospectCode}|{prospectSchoolshipCode}

falseExemplo de Configuração

**Domínio:**localhost

**prospectionCode:** 3

**prospectCode:** 128

**prospectSchoolshipCode**: 80

**Url Utilizada:** <http://localhost:8051/api/educational/v1/prospect/scholarship/3|128|80>

falseExemplo de Resultado Positivo Postman

Obs.: Em caso de sucesso, será retornado o respondeCode = 204 e a resposta em branco.

falseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true

# 2 - Descrição dos campos JSON de entrada/retorno

---

**Prospeção**

* prospectionCode: Código da prospecção
* description: Descrição da prospecção
* prospects: Lista de prospects da prospecção

**Prospects**

* prospectionCode: Código da prospecção
* prospectCode: Código do prospect
* prospectName: Nome do prospect
* prospectType: Tipo do prospect (A = "aluno", C = "candidato" ou P = "pessoa")
* companyCode: Código da coligada
* studentCode: Registro acadêmico do aluno
* prospectPaymentPlans: Lista de planos de pagamento do prospect
* prospectScholarShips: Lista bolsas do prospect

**Planos de pagamento do prospect**

* prospectionCode: Código da prospecção
* prospectCode: Código do prospect
* prospectPaymentPlanCode: Código do plano de pagamento do prospect
* companyCode: Código da coligada
* termCode: Código do período letivo
* paymentPlanCode: Código do plano de pagamento
* levelEducationCode: Código do nível de ensino
* branchCode: Código da filial

**Bolsas do prospect**

* prospectionCode: Código da prospecção
* prospectCode: Código do prospect
* prospectSchoolshipCode: Código da bolsa do prospect
* companyCode: Código da coligada
* scholarShipCode: Código da bolsa
* levelEducationCode: Código do nível de ensino
* serviceCode: Código do serviço
* termCode: Código do período letivo
* discountType: Tipo de desconto (P = Percentual, V = Valor)
* discountValue: Valor do desconto
* startDate: Data inicial da vigência
* endDate: Data final da vigência
* validityType: Tipo de validade (T = Todo o período, P = Somente o período letivo)
* branchCode: Código da filial
