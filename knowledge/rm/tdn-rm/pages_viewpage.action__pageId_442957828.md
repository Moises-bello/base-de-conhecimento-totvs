---
content_hash: d05448218c4f4de489fcab4de505d5cc7b2800233dbbe9a54d975627c0915fd3
fetched_at: '2026-06-29T00:09:53.864848+00:00'
page_id: '442957828'
product: rm
source: tdn-rm
title: Simulação de parcelas de contratos utilizando plano de pagamento - via REST
  (openAPI)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=442957828
version: 18
---

### Visão geral

O objetivo desse serviço é simular valores de parcelas de contratos de alunos através da configuração de parcelas de planos de pagamentos e concessão de bolsas futuras, informando o plano de pagamento, período letivo, matriz aplicada e uma lista de turmas disciplinas bem como um determinado status de matrícula na disciplina.

Esse serviço possibilita ao usuário do mesmo simular os valores a serem pagos pelo aluno antes de efetuarem a matrícula nas disciplinas de determinadas turmas, ou seja, não é necessário ter matrícula nas disciplinas bem como não é necessário se ter contrato para que o cálculo das parcelas seja feito.

O cálculo dos valores de parcelas segue a mesma regra da simulação de parcelas de contratos, ao selecionar uma determinada parcela na visão de parcela e clicar no botão para simular o cálculo.

### Simulação de valores de parcelas

O serviço de simulação de valores de parcelas será acessado via **REST** o qual funciona sobre o protocolo HTTP utilizando o verbo **POST**.

Os parâmetros de entrada bem como os valores calculados das parcelas são transmitidos no formato [JSON](http://json.org/json-pt.html).

O serviço em questão realiza a simulação dos valores de parcelas baseados no plano de pagamento informado, bem como suas turmas disciplinas e um status de matrícula a ser considerado.

### Configuração do HOST

Para que o serviço seja acessível, é necessário que sejam configuradas duas tags no arquivo RM.Host.exe.config (para HOST executado via executável) ou no arquivo RM.Host.Service.exe.config (para HOST executado via serviço do Windows). São elas:

* APIPORT: Porta que receberá as requisições do serviço.
* DEFAULTDB: Nome do alias do arquivo Alias.dat que apontará para o banco de dados a ser considerado.

Exemplo de configuração do arquivo RM.Host.exe.config:

### URL do serviço

Como o serviço é disponibilizado através de REST, se faz necessário uma URL pois o mesmo é executado utilizando o protocolo HTTP utilizando POST.

O formato da URL é o seguinte: http://{SERVIDOR}:{PORTA}/api/educational/v1/students/{STUDENTINTERNALID}//paymentplans/{PAYMENTPLANINTERNALID}/simulations.

Segue abaixo uma explicação dos campos da URL bem como um exemplo:

* SERVIDOR: Máquina ou servidor onde está hospedado o serviço
* PORTA: Número da porta HTTP onde está executando o serviço. É o mesmo número de porta setado na tag APIPORT do RM.Host.exe.config ou RM.Host.Service.exe.config
* STUDENTINTERNALID: É um ID com informações do aluno separadas por "|" para execução do serviço. O mesmo deverá ser informado no formato: Código da Coligada|Código da Filial|Código do nível de ensino|RA do aluno|ID. Habilitação Filial| Id.do período letivo
* PAYMENTPLANINTERNALID: É um ID com a informação da chave primária de plano de pagamento (SPLANOPGTO) que é: Código da coligada|Id. do período letivo|Código do plano de pagamento

**Exemplo:**

[http://localhost:8052/api/educational/v1/students/1|1|1|ES-00177|94|104/paymentplans/1|104|30/simulations](https://www.google.com/url?q=http://localhost:8098/api/educational/v1/students/1%7C1%7C1%7CES-00177%7C25%7C22/paymentplans/1%7C22%7C30/simulations&sa=D&source=hangouts&ust=1544704902967000&usg=AFQjCNFpVz8p59frebtqVinbEMJArjrzrw)

Caso não sejam informados todos os parâmetros necessários para a URL conforme descrito acima em URL do serviço, o sistema emitirá a mensagem de erro para o usuário:  
     "**Parâmetros insuficientes. Verifique se todos os parâmetros necessários para execução da API foram informados corretamente.**"

Caso o código da coligada e o id. do período letivo informados em "{StudentInternalID}" e "{PaymentPlanInternalID}" sejam diferentes, o sistema exibirá uma mensagem de erro para o usuário conforme abaixo:

* Código da coligada diferente: "**Código da coligada informada para o aluno na rota deve ser igual ao código da coligada informada para o plano de pagamento.**"
* Id. do período letivo diferente: "**Id. do período letivo informado para o aluno na rota deve ser igual ao id. do período letivo informado para o plano de pagamento.**"

### Parâmetros de entrada

Para que o serviço seja executado, além da edição dos arquivos do host e da informação da URL, é necessário que sejam informados alguns parâmetros de entrada via JSON conforme exemplo abaixo:

{

    "ListDisciplineClass" : [ 4762,4763,4764],  
    "UseAntecipationDiscount" : "S",  
    "UseScholarshipAntecipationDiscount" : "S",  
    "ScholarshipContractType" : "S",  
    "DisciplineRegistryStatusCode" : 123  
}

**Descrição dos parâmetros informados:**

* + ListDisciplineClass: Lista de ids. de turmas disciplinas (IdTurmaDisc) com as turmas disciplinas a serem consideradas na simulação dos valores.
  + UseAntecipationDiscount : Indica se será considerado desconto por antecipação ("S" - Sim ou "N" - Não). Caso não seja informado nenhum valor para o campo ou o campo seja omitido, o valor padrão para o mesmo será igual a "S".
  + UseScholarshipAntecipationDiscount : Indica se será considerado desconto por antecipação para cálculo de valores de bolsas ("S" - Sim ou "N" - Não). Caso não seja informado nenhum valor para o campo ou o campo seja omitido, o valor padrão para o mesmo será igual a "N".
  + ScholarshipContractType : Tipo da bolsa no contrato ("S" - Somar Bolsas, "M" - Aplicar Somente a Maior Bolsa, "C" - Aplicar Bolsas em Cascata). Caso não seja informado nenhum valor para o campo ou o campo seja omitido, o valor padrão para o mesmo será igual a "S".
  + DisciplineRegistryStatusCode : Código do status de matrícula.

    O status ou situação de matrícula na disciplina, no caso de simulação de parcelas calculadas por valor de crédito, deverão ter a opção de contar como créditos financeiros (cobrança por crédito) marcada. Vide imagem abaixo:

    Caso essa opção não esteja marcada, o serviço retornará os valores zerados para as parcelas.

### Exemplo de utilização do serviço utilizando o aplicativo POSTMAN

Caso queira fazer o download do POSTMAN, clique no [link](https://www.getpostman.com/apps) e escolha a versão correspondente do seu sistema operacional.

Exemplo de utilização do POSTMANPasso 01 - Criação de uma nova requisição

Clicar em New → Request

Informe o nome da requisição:

Na tela acima criar uma coleção ou pasta para a nova requisição.

Escolha o método POST

Autenticação básica

Para que o serviço faça a autenticação no HOST. É necessário informar o login e a senha do usuário do RM.

Na guia "Authorizaton", escolha o tipo "BasicAuth" autenticação básica e informe o login e a senha do RM

Parâmetros de entrada e execução do serviço

Na guia Body, marque a opção "raw" e escolha o formato JSON.

Depois informe os parâmetros conforme imagem abaixo:

xmlParâmetros de entrada

Após informar os parâmetros de entrada, clicar em Send para enviar a requisição para o servidor:

### Validações feitas pelo serviço

1. **Sistema não encontra as parcelas informadas**: Caso não sejam retornadas parcelas com valores simulados será exibida a seguinte mensagem "**Não foram encontrados registros a serem simulados**"
2. **Coligada não informada**: Caso a coligada não seja informada para o serviço, será exibida a mensagem "**Coligada deve ser informada.**"
3. **Filial não informada**: Caso a filial não seja informada para o serviço, será exibida a mensagem "**Filial deve ser informada.**
4. **Nível de ensino não informado**: Caso o nível de ensino não seja informado para o serviço, será exibida a mensagem "**Nível de ensino deve ser informado.**"
5. **Registro acadêmico não informado**: Caso não seja informado o RA do aluno, será exibida a mensagem "**RA deve ser informado."**
6. **Código do período letivo não informado**: Será exibida a mensagem "**Código do período letivo deve ser informado**".
7. **Código do plano de pagamento não informado**: Será exibida a mensagem "**Código do plano de pagamento deve ser informado**".
8. **Lista de Turmas Disciplinas não informada**: Será exibida a mensagem "**Lista de turmas disciplinas deve ser informada.**"
9. **Código da situação de matrícula nas disciplinas (status) não informado**: Será exibida a mensagem "**Status de matrícula na disciplina deve ser informado.**"
10. **Erros devido a inconsistências diversas**. Será exibida a mensagem informando o respectivo erro

### Retorno do Serviço

Conforme foi dito acima, o serviço retorna os valores simulados conforme regra de simulação de valores de parcelas de contratos da visão de parcelas  sem dependência de quaisquer matrículas em disciplinas nem de contratos existentes.

Após execução do serviço, serão retornados os parâmetros informados na entrada e o resultado estará na propriedade **listPaymentPlansSimulations** que é uma lista de simulação de valores de parcelas conforme abaixo:

xmlJSON de retorno

Abaixo segue uma explicação de cada tag do JSON de retorno do serviço.

* CompanyCode: Código da coligada.
* BranchCode: Código da filial.
* LevelEducacionCode: Código do nível de ensino.
* TermCodeDescription: Código do período letivo.
* StudentCode: Registro acadêmico.
* PaymentPlanCode: Código do plano de pagamento.
* SpecializationBranchCode : Id. habilitação filial.
* ListDisciplineClass : Lista de IdTurmaDisc.
* UseAntecipationDiscount : Indica se será considerado desconto por antecipação ("S" - Sim ou "N" - Não). Caso não seja informado nenhum valor para o campo ou o campo seja omitido, o valor padrão para o mesmo será igual a "S".
* UseScholarshipAntecipationDiscount : Indica se será considerado desconto por antecipação para cálculo de valores de bolsas ("S" - Sim ou "N" - Não). Caso não seja informado nenhum valor para o campo ou o campo seja omitido, o valor padrão para o mesmo será igual a "N".
* ScholarshipContractType : Tipo da bolsa no contrato ("S" - Somar Bolsas, "M" - Aplicar Somente a Maior Bolsa, "C" - Aplicar Bolsas em Cascata). Caso não seja informado nenhum valor para o campo ou o campo seja omitido, o valor padrão para o mesmo será igual a "S".
* DisciplineRegistryStatusCode : Código do status de matrícula.
* ```
  ListPaymentPlansSimulations: Lista de valores simulados de parcelas. Segue abaixo uma explicação para cada propriedade de simulação de parcela:
  ```

  + CompanyCode: Código da coligada da parcela.
  + InstalmentNumber: Número da parcela
  + Quota: Número da cota
  + OriginalValue: Valor original calculado
  + DiscountValue: Valor do desconto calculado para a parcela
  + NetValue: Valor líquido da parcela
  + ConditionalScholarshipValue: Valores de bolsas condicionais
  + UnconditionalScholarshipValue: Valores de bolsas incondicionais
  + TermCode: Id. do período letivo
  + TermCodeDescription: Código do período letivo
  + ServiceCode: Código do serviço
  + ServiceName: Nome do serviço
  + DueDate: Data de vencimento
  + CreditNumber: Indica se a parcela tem o valor calculado por crédito
  + CompetenceDate: Data de competência
  + RetroactiveCreditValue: Valor de crédito retroativo.
  + Scholarships: Lista de bolsas
    - ScholarshipCode: Código da bolsa
    - ScholarshipValue: Valor da bolsa
  + AntecipationDiscounts: Lista de itens de desconto por antecipação
    - CompanyCode: Código da coligada da parcela.
    - DiscountCode: Id. do item de desconto
    - PaymentValue: Valor de pagamento
    - AntecipationDiscountDate: Data limte calculada para o item de desconto
    - AntecipationDiscountValue: Valor do desconto calculado

Essa tag **VLRCREDRETROATIVO** só estará visível se a base do cliente estiver parametrizada para utilizar o modelo de bolsa retroativa sem alteração de parcelas baixadas utilizando devolução para os créditos retroativos.

A lista de **BOLSAS**exibirá os valores da bolsa referente ao primeiro vencimento do desconto por antecipação quando o desconto por calculado pelo sistema conforme as parametrizações realizadas. As bolsas consideradas serão as cadastradas na concessão de bolsa futura para o aluno.

Na alteração de plano de pagamento se a bolsa futura já existir no contrato será considerado as informações da bolsa já existente contrato e não será atualizado, somente serão incluídas novas bolsas.
