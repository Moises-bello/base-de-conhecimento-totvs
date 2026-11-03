---
content_hash: 168a7a47dde555f36166731c1cdb27917ab95f25429c409dd5f2d590408edf4b
fetched_at: '2026-06-29T00:11:49.547825+00:00'
page_id: '834806131'
product: rm
source: tdn-rm
title: API de Lançamento Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=834806131
version: 37
---

# Sumário

---

Sumário

# Objetivo

---

      Esse documento tem o objetivo de exemplificar o uso da API de Lançamento Contábil utilizando todos os métodos implementados.

Importante

Recurso disponível a partir da release 12.1.2406.

# 1 - Campos e Parâmetros

---

      Descrição detalhada dos campos da API de lançamento contábil.

false

As tabelas abaixo são divididas da seguinte maneira:

* **Campo:** Identificação do campo no Json.
* **Identificador:** Identificação do campo no banco de dados RM correspondente ao campo Json.
* **Tipo:** Tipo de valor aceito no campo, podendo ser numérico (Int, Decimal), condicionais (Boolean), texto (String, Datetime), além do tipo List, para esse último, é esperado uma nova sequência de dados (Bloco interno).
* **Descrição:** Fornece uma descrição do campo.
* **Obrigatório:** Especifica se a informação é obrigatória durante operações de envio (POST, PUT, PATCH). Caso a informação seja obrigatória condicionalmente essa informação será descrita no campo Observação.
* **Observação:** Informações condicionais ou importantes para o funcionamento da API serão apresentadas nesse campo.

falseLançamento

| LANÇAMENTO | | | | | |
| --- | --- | --- | --- | --- | --- |
| Campo | Identificador | Tipo | Descrição | Obrigatório | Observação |
| operationId | IDOPERACAO | Int | Identificador de Operação | - | Uso interno do Sistema |
| reversal | ESTORNO | Boolean | Lançamento de Estorno | - | Uso interno do Sistema |
| companyId | CODCOLIGADA | Int | Coligada | POST, PUT, PATCH |  |
| entryId | IDLANCAMENTO | Int | Id do Lançamento | POST, PUT, PATCH | No caso de Inserção de lançamento, o valor informado deve ser zero (0). |
| batchCode | CODLOTE | Int | Código do Lote | POST, PUT, PATCH |  |
| description | DESCRICAO | String | Descrição do Lançamento | POST, PUT |  |
| approvalUserId | CODUSUARIOAPROVACAO | String(20) | Código do usuário que aprovou o lançamento (para o lote 0[zero]) | - | Apenas informativo (seu valor é gerado por um processo dentro do TOTVS Gestão contábil). Caso tal campo seja informado para os métodos POST, PUT, PATCH o sistema o desconsiderará. |
| approvalDate | DATAAPROVACAO | DateTime | Data em que o lançamento foi aprovado (para o lote 0[zero]) | - | Apenas informativo (seu valor é gerado por um processo dentro do TOTVS Gestão contábil). Caso tal campo seja informado para os métodos POST, PUT, PATCH o sistema o desconsiderará. |
| accountEntry | PARTIDA | List | Partidas | POST, PUT | Não é possível inserir lançamento sem partidas. |

falsePartida

partida

No método PUT (Alteração de lançamento), é possível realizar inclusões, alterações e exclusões de partidas. Para isso, é necessário seguir os seguintes procedimentos:

* **Alteração:** Deve-se informar a chave da partida (entryNumberId) que deseja modificar.
* **Inclusão:** Ao passar a chave (entryNumberId) com o valor zero (0), o sistema interpretará como uma inserção de nova partida.
* **Exclusão:** As partidas não incluídas na requisição do método PUT serão removidas do lançamento.

| PARTIDA (accountEntry) | | | | | |
| --- | --- | --- | --- | --- | --- |
| Campo | Identificador | Tipo | Descrição | Obrigatório | Observação |
| entryNumberId | IDPARTIDA | Int | Identificador da Partida | POST, PUT, PATCH | No caso de Inserção de lançamento (POST), ou inserção de nova partida em lançamento já existente (PUT) o valor do campo deve ser zero (0). |
| branchId | CODFILIAL | Int | Filial | POST, PUT |  |
| branchName | NOMEFILIAL | String | Descrição Filial | - | Campo somente para leitura |
| costCenterCode | CODCCUSTO | String | Código do Centro de Custo | - |  |
| document | DOCUMENTO | String | Documento | Condicional | Obrigatório quando parametrizado. |
| date | DATA | DateTime | Data | POST, PUT | A data deve estar dentro do período contábil atual. |
| dateInclusion | DATAINCLUSAO | DateTime | Data da inclusão do lançamento | - | Uso interno do sistema, a data será preenchida com a data da inclusão do lançamento. |
| companyIdDebitAccount | CodColDebito | Int | Coligada da Conta a Débito | Condicional | Obrigatório se tiver conta Débito |
| debitAccount | CodContaDebito | String | Cód. conta débito | Condicional | Obrigatório pelo menos uma conta de débito ou crédito |
| debitDescription | DescricaoDebito | String | Descrição da Conta Débito | - | Campo somente para leitura |
| companyIdCreditAccount | CodColCredito | Int | Coligada da Conta a Crédito | Condicional | Obrigatório pelo menos uma conta de débito ou crédito |
| creditAccount | CodContaCredito | String | Cód. conta crédito | Condicional | Obrigatório se tiver conta Crédito |
| creditDescription | DescricaoCredito | String | Descrição da Conta Crédito | - | Campo somente para leitura |
| companyIdAgainstEntry | CodColContraPartida | Int | Coligada da Conta Contra Partida | - |  |
| value | VALOR | Decimal | Valor | POST, PUT | O valor informado deve ser maior que zero. |
| value2 | VALOR2 | Decimal | Segundo Valor | - |  |
| date2 | DATA2 | Data | Data da Cotação do Segundo Valor | - |  |
| integrateApplication | IntegraAplicacao | String | Aplicação que Gerou o Lançamento. | - | Campo de controle interno. |
| generationType | TipoGeracao | String | Tipo de Geração | - | Campo de controle interno. |
| historicCode | CODHISTP | String | Histórico | - |  |
| user | Usuario | String | Usuário que incluiu lançamento | - | Será gravado o usuário que enviou a requisição. |
| complementaryFields | CamposComplementares | List | Complemento | - |  |
| apportionmentDebit | RateioDebito | List | Rateio Debito | Condicional | Obrigatório para conta débito que exige rateio |
| apportionmentCredit | RateioCredito | List | Rateio Credito | Condicional | Obrigatório para conta crédito que exige rateio |
| valuesCurrencies | MoedaValores | List | MultiMoedas | - |  |
| apportionmentValuesCurrencies | RateioMoedasValores | List | Rateio MultiMoedas | - |  |

falseCampos Complementares

CamposComplementares

Os campos complementares são adaptados para atender às necessidades específicas de cada sistema.   
Abaixo, listamos somente os campos obrigatórios que devem ser preenchidos quando há informações adicionais.

| CamposComplementares (complementaryFields) | | | | | |
| --- | --- | --- | --- | --- | --- |
| Campo | Identificador | Tipo | Descrição | Obrigatório | Observação |
| codlote | CODLOTE | Int | Código do lote atual | PUT, PATCH | Deve ser suprimido nas inserções, o sistema irá gerar automaticamente. Veja exemplo no método POST. |
| lctref | LCTREF | Int | Referência do Lançamento | PUT, PATCH | Deve ser suprimido nas inserções, o sistema irá gerar automaticamente. Veja exemplo no método POST. |
| idpartida | IDPARTIDA | Int | Identificador da Partida | PUT, PATCH | Deve ser suprimido nas inserções, o sistema irá gerar automaticamente. Veja exemplo no método POST. |
| ? | ? | ? | Campo Complementar | PUT, POST, PATCH | O campo complementar deve ser informado no arquivo JSON tal como está cadastrado no RM, o seu valor deve respeitar o tipo definido. |

falseRateios Credito/Debito

RateioDebito

Contas que exigem rateio devem ter a lista de rateio fornecida. Na inclusão (método POST), se uma conta possui um rateio padrão, o sistema utilizará esses dados automaticamente, caso a lista de rateio não seja enviada. No entanto, este comportamento não é aplicado durante alterações (método PUT). Portanto, o rateio deve ser explicitamente enviado na requisição para este caso.

No método PUT (Alteração de lançamento), é possível realizar inclusões, alterações e exclusões de rateios. Para isso, é necessário seguir os seguintes procedimentos:

* **Alteração:** Deve-se informar a chave do rateio (apportionmentId) que deseja modificar.
* **Inclusão:** Ao passar a chave (apportionmentId) com o valor zero (0), o sistema interpretará como uma inserção de novo rateio.
* **Exclusão:** Os rateios não incluídos na requisição do método PUT serão removidos do lançamento.

| RateioDebito (apportionmentDebit) / RateioCredito(apportionmentCredit) | | | | | |
| --- | --- | --- | --- | --- | --- |
| Campo | Identificador | Tipo | Descrição | Obrigatório | Observação |
| companyId | CODCOLIGADA | Int | Coligada do Rateio | POST, PUT |  |
| date | DATA | DateTime | Data do Lançamento do Rateio | POST, PUT |  |
| companyIdAccountManagement | CODCOLCONTA | Int | Código da Coligada da Conta Contábil | POST, PUT |  |
| accountManagementInactive | ATIVO | Int | Status | - |  |
| accountManagementCode | CODCONTA | String | Código da Conta | POST, PUT |  |
| apportionmentId | IDRATEIO | Int | Identificador do Rateio | POST, PUT, PATCH | Na inserção, pode ser enviado como zero (0) ou suprimir. |
| entryNumberId | IDPARTIDA | Int | Identificador da Partida | PUT | Na inserção, pode ser enviado como zero (0) ou suprimir. |
| value | VALOR | Decimal | Valor | POST, PUT |  |
| percentual | PERCENTUAL | String | Porcentagem do Rateio | - | Campo calculado pelo sistema. |

falseMultimoeda

Multimoeda

Para contas que possuem configurações de conversão de multimoeda, como Taxa Histórica, Taxa Média Histórica e Taxa de Fechamento, os valores de multimoeda são automaticamente gerados com base na cotação correspondente. No caso de conversão multimoeda do tipo Fixa, o valor deve ser informado manualmente.

| MoedaValores(valuesCurrencies) | | | | | |
| --- | --- | --- | --- | --- | --- |
| Campo | Identificador | Tipo | Descrição | Obrigatório | Observação |
| companyId | CODCOLIGADA | Int | Coligada Moeda | POST, PUT, PATCH |  |
| entryNumberId | IDPARTIDA | Int | Identificador da Partida | POST, PUT, PATCH |  |
| currency | MOEDA | String | Símbolo da Moeda | POST, PUT, PATCH |  |
| value | VALOR | Decimal | Valor Moeda | POST, PUT, PATCH |  |

falseRateio Multimoeda

RateioMultimoeda

Os campos abaixo não podem ser manipulados pelo requisitante, eles são calculados de acordo com o rateio gerencial da conta.

| RateioMoedasValores(apportionmentValuesCurrencies) | | | | | |
| --- | --- | --- | --- | --- | --- |
| Campo | Identificador | Tipo | Descrição | Obrigatório | Observação |
| companyId | CODCOLIGADA | Int | Coligada | - | Gerado pelo sistema |
| apportionmentId | IDMULTIMOEDA | Int | Identificador de MultiMoeda | - | Gerado pelo sistema |
| currency | MOEDA | String | Moeda utlizada no rateio multi moeda. | - | Gerado pelo sistema |
| value | VALOR | Decimal | Valor do rateio convertido para moeda cadastrada. | - | Calculado pelo sistema |

# 2 - Métodos

---

      Métodos disponíveis na API de Lançamento Contábil:

falsefalseGET (Recuperar lançamentos contábeis do sistema)

**GET:** Exemplos de requisições que buscam e recuperam lançamentos no sistema.

falseGet All (Recuperar todas os Lançamento da coligada escolhida)falseGetAll

**Máscara de Url:** http://{domínio}:{porta}/api/ctb/v1/AccountingEntries/{companyId}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Url Utilizada:** <http://localhost:8051/api/ctb/v1/AccountingEntries/6>

falseExemplo de ResultadoVer resultado JSON...jsRDark1Resultado (JSON)truefalseOrder (Retorna os dados ordenados)Parâmetros

**Order:** parâmetro responsável pela ordenação do resultado, podendo ser ascendente ou descendente. O resultado com a ordem descendente deve ser precedida do caractere "-" (menos).

**Exemplo 1:** ?order=campo1 (Ascendente)

**Exemplo 2:** ?order=-campo1 (Descendente)

**Múltiplos campos de ordenação:** ?order=[-]campo1, [-]campo2, [-]campo3 ...

falseOrder (Asc)

**Máscara de Url:** http://{domínio}:{porta}/api/ctb/v1/AccountingEntries/{companyId}?order={campo}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** description

**Tipo de Ordenação:** Ascendente

**Url Utilizada:** <http://localhost:8051/api/ctb/v1/AccountingEntries/6?order=description>

falseExemplo de ResultadoVer resultado JSON...jsRDark1Resultado (JSON)truefalseOrder Desc (Ordena o resultado de forma decrescente)falseOrder (Desc)

**Máscara de Url:** http://{domínio}:{porta}/api/ctb/v1/AccountingEntries/{companyId}?order=[-]{campo}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** description

**Tipo de Ordenação:** Descendente

**Url Utilizada:** <http://localhost:8051/api/ctb/v1/AccountingEntries/6?order=-description>

falseExemplo de ResultadoVer resultado JSON...jsRDark1Resultado (JSON)truefalseFilter (Resultado filtrado)falseFilter

**Máscara de Url:** http://{domínio}:{porta}/api/ctb/v1/AccountingEntries/{companyId}?{campo}={valor}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** entryId

**Valor:** 9

**Url Utilizada:** <http://localhost:8051/api/ctb/v1/AccountingEntries/6?entryId=9>

falseExemplo de ResultadoVer resultado JSON...jsRDark1Resultado (JSON)trueFiltros Complexos - OData

Para realizar filtros complexos na API de Lançamento e Partida é possível adotar o padrão OData. Para entender melhor sobre a utilização desse padrão, acesse o link da documentação [Utilizando filtros complexos - Exemplos do guia de API - ODATA](https://tdn.totvs.com/display/LRM/Utilizando+Filtros+Complexos+-+Exemplos+do+guia+de+API+-+ODATA).

falsePaginação (Retorno de quantidades específicas por página)Parâmetros

**Page:** Página que será apresentada.

**PageSize**: Quantidade máxima de registros por página que serão apresentados.

**Exemplo:** ?page=1&pageSize=1

**Valores padrão:** Caso não sejam preenchidos os parâmetros evidenciados acima serão preenchidos com valores padrão.

**Page:** 1

**PageSize:** 20

falsePaginação

**Máscara de Url:** http://{domínio}:{porta}/api/ctb/v1/AccountingEntries/{companyId}?page={valor1}&pageSize={valor2}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Valor1:** 1

**Valor2:** 3

**Url Utilizada:** <http://localhost:8051/api/ctb/v1/AccountingEntries/6?page=1&pageSize=3>

falseExemplo de ResultadoVer resultado JSON...jsRDark1Resultado (JSON)truefalseFields (Retorno de campos específicos no resultado)Parâmetros

**Fields:** parâmetro responsável pela especialização de campos em um resultado, ou seja, o usuário define quais campos serão apresentados no resultado.

**Exemplo:** ?fields=campo1

**Múltiplos campos de ordenação:** ?fields=campo1, campo2, campo3 ...

falseFields

**Máscara de Url:** http://{domínio}:{porta}/api/ctb/v1/AccountingEntries/{companyId}?fields={campos}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo 1:** entryId

**Campo 2:** batchCode

**Campo 3:** description

**Url Utilizada:** <http://localhost:8051/api/ctb/v1/AccountingEntries/6?fields=entryId,batchCode,description>

falseExemplo de ResultadoVer resultado JSON...jsRDark1Resultado (JSON)truefalseGetOne (Recuperar Lançamento e Partida pela chave composta)Parâmetros

Nos parâmetros do GetOne é necessário passar uma chave composta ("id"), por isso informamos "companyId" (código da coligada), além do Lançamento que queremos selecionar, o "entryId"

(Id de Lançamento), o "batchCode" (código Lote), sendo eles separados pelo caractere "|" pipe.

falseGetOne

**Máscara de Url:** http://{domínio}:{porta}/api/ctb/v1/AccountingEntries/{companyId}/{entryId}|{batchCode}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**companyId:** 6

**entryId:** 9

**batchCode:** 0

**Url Utilizada:** <http://localhost:8051/api/ctb/v1/AccountingEntries/6/9|0>

falseExemplo de ResultadoVer resultado JSON...jsRDark1Resultado (JSON)truefalsePost (Inserir um Lançamento e Partida)

**POST:** Cria um novo lançamento no sistema.

falsePost

**Máscara de Url:** http://{domínio}:{porta}/api/ctb/v1/AccountingEntries/{companyId}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**CompanyId:** 1

**Url Utilizada:** [http://localhost:8051/api/ctb/v1/AccountingEntries/1](http://localhost:8051/api/ctb/v1/AccountingEntries/6)

falseExemplo de EntradaVer resultado JSON...

O JSON abaixo contém os dados para incluir uma nova partida na coligada 1 (um). Além dos dados comuns, estamos enviando informações de rateio gerencial, valores de multimoeda e campo complementar.  
  
No caso de campo complementar observe que na requisição de envio os campos chave são suprimidos.

jsEmacs1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...

Na resposta do resultado, são retornadas algumas informações adicionais. Destacamos especialmente o cálculo do rateio de multimoeda, realizado pelo sistema, bem como o valor percentual do rateio gerencial.

jsRDark1Resultado (JSON)truefalseExemplo de Resultado NegativoVer resultado JSON...jsFadeToGrey1Resultado (JSON)truefalsePatch (Atualização parcial de um Lançamento ou Partida

**PATCH:** Altera um lançamento no sistema, nesse caso apenas as chaves primárias e dados de alteração precisam ser enviados.

falsePatch

**Máscara de Url:** http://{domínio}:{porta}/api/ctb/v1/AccountingEntries/{companyId}/{entryId}|{batchCode}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**CompanyId:** 1

**entryId:** 3001

**batchCode:** 0

**Url Utilizada:** [http://localhost:8051/api/ctb/v1/AccountingEntries/1/3001|0](http://localhost:8051/api/ctb/v1/AccountingEntries/6/12|0)

falseExemplo de EntradaVer resultado JSON...

Nessa requisição, para exemplificar o uso do método PATCH, faremos as seguintes alterações:

1. Descrição do lançamento de "Inclusão de Lançamento VIA API com rateio - POST" para "Inclusão de Lançamento VIA API com rateio - ALTERAÇÃO PATCH" .
2. Alteração do valor da partida de R$ 1.000,00 para R$ 2.000,00
3. Alteração do rateio a débito, alteraremos o valor do primeiro item.
4. Alteração do rateio a crédito para se adaptar ao novo valor da partida.
5. Alteração dos valores de multimoeda para equalizar o novo valor da partida.

jsEmacs1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...

Observa-se que os valores calculados foram ajustados de acordo com o novo valor da partida.

jsRDark1Resultado (JSON)truefalseExemplo de Resultado NegativoVer resultado JSON...jsFadeToGrey1Resultado (JSON)truefalsePut (Atualização completa de um Lançamento e Partida)

**PUT:** Altera um lançamento no sistema.

falsePut

**Máscara de Url:** http://{domínio}:{porta}/api/ctb/v1/AccountingEntries/{companyId}/{entryId}|{batchCode}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**CompanyId:** 1

**entryId:** 3001

**batchCode:** 0

**Url Utilizada:** [http://localhost:8051/api/ctb/v1/AccountingEntries/1/3001|0](http://localhost:8051/api/ctb/v1/AccountingEntries/6/12|0)

falseExemplo de EntradaVer resultado JSON...

As alterações que serão passadas no PUT, seguem as regras da tela de Lançamento do sistema.  
  
Nesse exemplo, retornamos o valor da partida para R$ 1.000,00, adaptamos os rateios, mas notem que apenas um dos itens do rateio a débito foi passado, isso informa ao sistema que os itens não passados serão excluídos.

jsEmacs1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...jsRDark1Resultado (JSON)truefalseExemplo de Resultados NegativoVer resultado JSON...jsFadeToGrey1Resultado (JSON)truejsFadeToGrey1Resultado (JSON)truejsFadeToGrey1Resultado (JSON)truejsFadeToGrey1Resultado (JSON)truefalseDelete (Exclui um Lançamento e Partida)

**DELETE:** Deleta um lançamento do sistema.

falseDelete

**Máscara de Url:** http://{domínio}:{porta}/api/ctb/v1/AccountingEntries/{companyId}/{entryId}|{batchCode}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**CompanyId:** 1

**entryId:** 3001

**batchCode:** 0

**Url Utilizada:** [http://localhost:8051/api/ctb/v1/AccountingEntries/1/3001|0](http://localhost:8051/api/ctb/v1/AccountingEntries/6/12|0)

falseExemplo de Resultado Positivo Postman

Por fim deletamos o lançamento anteriormente criado e modificado. Em caso de sucesso, será retornado o **respondeCode = 204** sem JSON de retorno.

falseExemplo de Resultado NegativoVer resultado JSON...jsFadeToGrey1Resultado (JSON)true
