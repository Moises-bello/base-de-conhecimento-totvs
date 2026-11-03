---
content_hash: ecae7f087a28625a6acdb4bf37552be4ad5e011ce92037d059e4306b70ec93c4
fetched_at: '2026-06-29T00:10:06.550507+00:00'
page_id: '452719314'
product: rm
source: tdn-rm
title: Agrupamento de Contas Gerenciais ( RM Labore)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719314
version: 2
---

Através desta informação se faz o vínculo entre as contas do plano de contas contábeis e o plano de contas gerenciais do **RM Saldus** (sistema de contabilidade gerencial DA LINHA RM) e as contas identificadoras das unidades (matriz/filiais/coligadas) da empresa (aqui denominadas **Contas Labore**).  
    
 O sistema considera as informações desse cadastro para estabelecer o relacionamento entre as **contas Labore** e as contas contábeis informadas na janela de edição **Seção**, pasta **Dados Contábeis** (considerando as variáveis informadas).  
    
 Assim, é através desse cadastro que o sistema fará a substituição da variável constante na pasta citada, para cada seção e/ou filial, e as integrantes do plano de contas.   
    
 O plano de contas gerencial é idêntico ao plano de contas contábil, porém voltado para uma visão gerencial.   
    
 O *grupo conta* junto com *código de integração* e *código de integração por funcionário* tem o objetivo único de identificar o número da conta gerencial e opcionalmente a filial e o centro de custo a ser contabilizado.  
    
 Quando analisando cada evento ou encargo, o sistema concatena os Códigos de integração de acordo com a parametrização feita nos cadastros de eventos e encargos (*veja Cadastro de Eventos, Cadastro de Encargos).* Após montar os Códigos, o sistema procura por uma chave idêntica no plano de contas e quando encontrada tem-se a conta gerencial. Se não encontrar a chave, o sistema emite uma mensagem de erro.  
    
 O *grupo conta* especificamente é o mesmo agrupador de eventos e encargos utilizado nestes cadastros. Portanto, para cada grupo utilizado em eventos ou encargos, provavelmente existirá um ou mais registros no plano de contas com este grupo.   
 **Referência:**

|  |  |
| --- | --- |
| Tabela | PCONTASGER |
| Campo | GRPCONTA |
| Onde cadastrar | CADASTROS DE TABELAS DINÂMICAS - Código GRPGER |

O código de integração é o mesmo agrupador de seções ou centros de custo usado nestes cadastros. Aqui no plano de contas deve ser cadastrado em conjunto com os demais Códigos de integração quando a combinação deles é possível e tem uma conta contábil a qual deve ser direcionado o valor a ser contabilizado.  
 **Referência:**

|  |  |
| --- | --- |
| Tabela | PCONTASGER |
| Campo | CODINTEGR |
| Onde cadastrar | CADASTROS DE TABELAS DINÂMICAS - Código CODINTGER |

Da mesma forma que os demais Códigos de integração, só que o código de integração por funcionários é o agrupador de funcionários.  
 **Referência:**

|  |  |
| --- | --- |
| Tabela | PCONTASGER |
| Campo | INTEGRCFUNC |
| Onde cadastrar | CADASTROS DE TABELAS DINÂMICAS - Código INTGERFUNC |

O objetivo principal do plano de contas gerencial é determinar a conta gerencial. Este plano de contas é o link entre os dados de folha de pagamento e os dados necessários para a contabilidade. Basicamente a contabilidade precisa das contas de débito e crédito, o valor a ser contabilizado e opcionalmente centro de custo e filial. O campo *Conta Saldus* determina ora uma conta débito ora uma conta crédito.  
 **Observação:**  
 Quando houver dois códigos de Contas Saldus iguais (coligada corrente e coligada global), ao informar o código o sistema acatará o código da coligada corrente. Se o o usuário desejar informar o código da Conta Saldus da coligada global, o mesmo deverá ser selecionado pelo nome ou pela conta reduzida.  
 As contas permitidas neste campo são cadastradas no RM Saldus.  
 **Referência:**

|  |  |
| --- | --- |
| Tabela | PCONTASGER |
| Campo | CONTASALDUS |
| Onde cadastrar | RM Saldus: CADASTROS DE PLANO DE CONTAS GERENCIAL |

A Filial é opcional e quando informado tem prioridade sobre a filial que a seção ou centro de custo indicam para contabilização (número da filial contábil). É uma forma de contabilizar direcionando os valores de um evento ou encargo para uma filial específica. Se não for informada a filial no plano de contas nem na seção ou centro de custo, o lançamento contábil não terá a filial.  
 **Referência:**

|  |  |
| --- | --- |
| Tabela | PCONTASGER |
| Campo | CODFILIAL |
| Onde cadastrar | CADASTROS DE FILIAIS |

O departamento é opcional e permite contabilizar direcionando os valores de um evento ou encargo para um departamento específico. Se não for informado no plano de contas, o lançamento contábil não terá o departamento. O departamento tem que ser coerente com a filial, ou seja, deve-se informar um departamento que exista na filial acima.  
 **Referência:**

|  |  |
| --- | --- |
| Tabela | PCONTAS |
| Campo | CODDEPARTAMENTO |
| Onde cadastrar | CADASTROS DE DEPARTAMENTOS |

O Centro de Custo (Labore) também é opcional e quando informado tem prioridade sobre o centro de custo que a seção indica para contabilização. É uma forma de contabilizar direcionando os valores de um evento ou encargo para um centro de custo específico. Se não for informado o centro de custo no plano de contas nem na seção, o lançamento contábil não terá centro de custo.  
 Na contabilização por centro de custo quando não utiliza o centro de custo no plano de contas, o sistema utiliza o centro de custo indicado no rateio do cadastro de funcionários.  
 **Referência:**

|  |  |
| --- | --- |
| Tabela | PCONTASGER |
| Campo | CODCCUSTO |
| Onde cadastrar | CADASTROS/CENTROS DE CUSTO (LABORE) |

**Exemplo:**  
 No plano de contas abaixo, supondo contabilização gerencial de eventos por seção, temos:

* Todos os eventos do grupo 111 que não tem integração contábil nem integração por funcionários, dos funcionários cuja seção não tem integração contábil e a integração por funcionários também é nula
* Contabilizar na conta 111.1.1, na filial contábil e centro de custo da seção do funcionário.
* Todos os eventos do grupo 111 que tem integração contábil e não tem integração por funcionários, dos funcionários cuja seção tem integração contábil 1 e a integração por funcionários é nula
* Contabilizar na conta 111.1.2, na filial contábil 1 e centro de custo da seção do funcionário.
* Todos os eventos do grupo 111 que não tem integração contábil e tem integração por funcionários, dos funcionários cuja seção não tem integração contábil e a integração por funcionários é 10
* Contabilizar na conta 111.1.3, na filial contábil da seção do funcionário e centro de custo 103.
* Todos os eventos do grupo 111 que tem integração contábil e tem integração por funcionários, dos funcionários cuja seção tem integração contábil 4 e a integração por funcionários são 50
* Contabilizar na conta 111.1.4, na filial contábil e centro de custo da seção do funcionário.

  |  |  |  |  |  |  |  |
  | --- | --- | --- | --- | --- | --- | --- |
  |  | GRUPO DE CONTAS | INTEGR CONTÁBIL | INTEGR   FUNCION | CONTA   GERENCIAL | FILIAL | CENTRO CUSTO |
  | 1 | 111 |  |  | 111.1.1 |  |  |
  | 2 | 111 | 1 |  | 111.1.2 | 1 |  |
  | 3 | 111 |  | 10 | 111.1.3 |  | 103 |
  | 4 | 111 | 4 | 50 | 111.1.4 |  |  |
