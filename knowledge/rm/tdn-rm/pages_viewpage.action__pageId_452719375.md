---
content_hash: 83300a9c244888a3ebe40fc6fbaa968eb24926729cd39e213a37a329cdd1cec8
fetched_at: '2026-06-29T00:10:07.207955+00:00'
page_id: '452719375'
product: rm
source: tdn-rm
title: Agrupamento de Contas Contábeis (RM Labore)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719375
version: 2
---

Através desta informação se faz o vínculo entre as contas identificadoras da unidade da empresa e as contas contábeis cadastradas no RM Saldus, sistema de contabilidade gerencial da TOTVS.  
    
 As informações de *Grupo Conta, Código de Integração* e C*ódigo de Integração por Funcionário* tem o objetivo único de identificar o número da conta contábil e opcionalmente a filial e o centro de custo a ser contabilizado.  
    
 Quando analisando cada evento ou encargo, o sistema concatena os Códigos de integração de acordo com a parametrização feita nos cadastros de eventos e encargos (*veja Cadastro de Evento e Cadastro de Encargos).* Após montar os códigos, o sistema procura por uma chave idêntica no plano de contas e quando encontrada tem-se a conta contábil. Se não encontrar a chave, o sistema emite uma mensagem de erro.  
    
 O *grupo conta* especificamente é o mesmo agrupador de eventos e encargos utilizado nestes cadastros. Portanto, para cada grupo utilizado em eventos ou encargos, provavelmente existirá um ou mais registros no plano de contas com este grupo.   
 **Referência:**

|  |  |
| --- | --- |
| Tabela | PCONTAS |
| Campo | GRPCONTA |
| Onde cadastrar | CADASTROS DE TABELAS DINÂMICAS - Código GRPCONT |

O Código de Integração é o mesmo agrupador de seções ou centros de custo usado nestes cadastros. Aqui no plano de contas deve ser cadastrado em conjunto com os demais Códigos de Integração quando a combinação deles é possível e tem uma conta contábil a qual deve ser direcionado o valor a ser contabilizado.  
 **Referência:**

|  |  |
| --- | --- |
| Tabela | PCONTAS |
| Campo | CODINTEGR |
| Onde cadastrar | CADASTROS DE TABELAS DINÂMICAS - Código CODINTCONT |

Da mesma forma que os demais Códigos de Integração, o Código de Integração por Funcionário somente difere em relação a ser o agrupador de funcionários.  
 **Referência:**

|  |  |
| --- | --- |
| Tabela | PCONTAS |
| Campo | INTEGRCFUNC |
| Onde cadastrar | CADASTROS DE TABELAS DINÂMICAS - Código INTCONTFUNC |

A Conta Saldus é o objetivo principal do agrupamento de contas contábil (RM Labore), ou seja, determina a conta contábil. Este agrupamento de contas é o link entre os dados de folha de pagamento e os dados necessários para a contabilidade. Basicamente a contabilidade precisa das contas de débito e crédito, o valor a ser contabilizado e opcionalmente centro de custo e filial. O campo *Conta Saldus* determina ora uma conta débito ora uma conta crédito.  
 **Observação:**  
 Quando houver dois códigos de Contas Saldus iguais (coligada corrente e coligada global), ao informar o código o sistema acatará o código da coligada corrente. Se o usuário desejar informar o código da Conta Saldus da coligada global, o mesmo deverá ser selecionado pelo nome ou pela conta reduzida.  
    
 As contas permitidas neste campo são cadastradas no RM Saldus.  
 **Referência:**

|  |  |
| --- | --- |
| Tabela | PCONTAS |
| Campo | CONTASALDUS |
| Onde cadastrar | RM Saldus: CADASTROS DE PLANO DE CONTAS CONTÁBIL |

A informação da Filial é opcional e quando informado tem prioridade sobre a filial que a seção ou centro de custo indicam para contabilização (número da filial contábil). É uma forma de contabilizar direcionando os valores de um evento ou encargo para uma filial específica. Se não for informada a filial no agrupamento de contas considerará a filial cadastrada na seção.  
 **Referência:**

|  |  |
| --- | --- |
| Tabela | PCONTAS |
| Campo | CODFILIAL |
| Onde cadastrar | CADASTROS DE FILIAIS |

A informação do Departamento é opcional e permite contabilizar direcionando os valores de um evento ou encargo para um departamento específico. Se não for informado no agrupamento de contas, o lançamento contábil considerará o departamento da seção.   
 **Referência:**

|  |  |
| --- | --- |
| Tabela: | PCONTAS |
| Campo: | CODDEPARTAMENTO |
| Onde cadastrar: | CADASTROS DE DEPARTAMENTOS |

**Observação:**  
 Caso exista informação neste campo e no campo "Departamento Contábil" em Cadastros | Seções | Dados Contábeis, o sistema dará prioridade a informação do campo "Departamento" do Agrupamento de Contas ignorando a informação do campo "Departamento Contábil" informado nas Seções. Caso o campo "Departamento" no Agrupamento de Contas não tenha informação, o sistema irá buscar a informação do campo "Departamento Contábil" das Seções.  
    
 A informação do Centro de Custo é opcional e quando informado tem prioridade sobre o centro de custo que a seção indica para contabilização. É uma forma de contabilizar direcionando os valores de um evento ou encargo para um centro de custo específico. Se não for informado o centro de custo no agrupamento de contas nem na seção, o lançamento contábil não terá centro de custo.  
 Na contabilização por centro de custo quando não utiliza o centro de custo no agrupamento de contas, o sistema utiliza o centro de custo indicado no rateio do cadastro de funcionários.  
 **Referência:**

|  |  |
| --- | --- |
| Tabela | PCONTAS |
| Campo | CODCCUSTO |
| Onde cadastrar | CADASTROS DE CENTROS DE CUSTO (LABORE) |

**Exemplo:**  
 No Agrupamento de contas abaixo, supondo contabilização de eventos por seção, temos:

* Todos os eventos do grupo 111 que não tem integração contábil nem integração por funcionários, dos funcionários cuja seção não tem integração contábil e a integração por funcionários também é nula è Contabilizar na conta 111.1.1, na filial contábil e centro de custo da seção do funcionário.
* Todos os eventos do grupo 111 que tem integração contábil e não tem integração por funcionários, dos funcionários cuja seção tem integração contábil 1 e a integração por funcionários é nula è Contabilizar na conta 111.1.2, na filial contábil 1 e centro de custo da seção do funcionário.
* Todos os eventos do grupo 111 que não tem integração contábil e tem integração por funcionários, dos funcionários cuja seção não tem integração contábil e a integração por funcionários é 10 è Contabilizar na conta 111.1.3, na filial contábil da seção do funcionário e centro de custo 103.
* Todos os eventos do grupo 111 que tem integração contábil e tem integração por funcionários, dos funcionários cuja seção tem integração contábil 4 e a integração por funcionários é 50 è Contabilizar na conta 111.1.4, na filial contábil e centro de custo da seção do funcionário.

  |  |  |  |  |  |  |  |
  | --- | --- | --- | --- | --- | --- | --- |
  |  | GRUPO DE CONTAS | INTEGR CONTÁBIL | INTEGR   FUNCION | CONTA   CONTÁBIL | FILIAL | CENTRO CUSTO |
  | 1 | 111 |  |  | 111.1.1 |  |  |
  | 2 | 111 | 1 |  | 111.1.2 | 1 |  |
  | 3 | 111 |  | 10 | 111.1.3 |  | 103 |
  | 4 | 111 | 4 | 50 | 111.1.4 |  |  |
