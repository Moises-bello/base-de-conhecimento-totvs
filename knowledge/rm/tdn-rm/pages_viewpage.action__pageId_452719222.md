---
content_hash: ff98e7e98573012a952c4aafda5fcf3ed4e3d253e6c6943c5389b1ff1c8c0e12
fetched_at: '2026-06-29T00:10:04.583520+00:00'
page_id: '452719222'
product: rm
source: tdn-rm
title: Dados Contábeis do Encargo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719222
version: 80
---

**Dados Contábeis do Encargo**
Os dados contábeis são informações que serão considerados pelo \*RM Saldus\* para contabilização dos encargos. Haverá a possibilidade de montar o plano de contas selecionando os grupos e integração cadastrados previamente nas Tabelas Dinâmicas.
 
A Conta Contábil - Grupo conta débito é um agrupador de encargos utilizado para contabilização. Este grupo tem como objetivo facilitar a montagem do plano de contas no RM Labore, evitando que o usuário tenha que criar um item no plano de contas para cada encargo. Os grupos devem ser criados (veja abaixo onde cadastrá-los) de acordo com o nível de detalhamento que a contabilidade exige, ou seja, encargos que tenham o mesmo destino na contabilidade provavelmente usarão o mesmo grupo de conta.
Referência:
Tabela: PENCARGO
Campo: CONTADEBITO
Onde cadastrar: Cadastros de Tabelas Dinâmicas - Código GRPCONT
 
Como normalmente se contabiliza os valores creditando em uma conta e debitando em outra, é necessário indicar um grupo de conta para débito e outro para crédito, bem como indicar se existe integração contábil e integração contábil por funcionário para cada caso.
A Conta Contábil - Grupo conta crédito, portanto, é idêntica ao grupo de conta débito exceto o fato de ser destinada ao crédito.
Referência:
Tabela: PENCARGO
Campo: CONTACREDITO
Onde cadastrar: Cadastros de Tabelas Dinâmicas - Código GRPCONT
 
Quando o encargo tem o campo "Tem integração contábil" marcado significa que será utilizado o grupo de conta débito mais o código de integração atribuído à seção ou ao centro de custo do funcionário para determinar a conta contábil correta no plano de contas.
\*Observação:\*
Este parâmetro tem a mesma funcionalidade para todas as contas.
 
Quando o encargo tem o campo "Tem integração por funcionário" marcado, significa que o sistema agregará ao grupo de conta débito o código de integração por funcionário do cadastro do funcionário para determinar a conta no plano de contas. Os campos "integração contábil" e "integração por funcionário" são independentes entre si, portanto, se o campo "tem integração contábil" também estiver marcado então a procura no plano de contas será por: grupo de conta débito + código integração + código integração por funcionário.
\*Observação:\*
Este parâmetro tem a mesma funcionalidade para todas as contas.
 
A Contabilização parcial indica que será utilizado somente a contabilização do crédito ou do débito, a parte ausente será contabilizada posteriormente de uma outra forma. Quando este campo não está marcado, obrigatoriamente deve-se informar os grupos de crédito e débito.
 
A Conta Gerencial - Grupo conta débito também é um agrupador de encargos utilizado para contabilização. Este grupo tem como  objetivo facilitar a montagem do plano de contas no RM Labore, evitando que o usuário tenha que criar um item no plano de contas para cada encargo. Os grupos devem ser criados (veja abaixo onde cadastrá-los) de acordo com o nível de detalhamento que a contabilidade exige, ou seja, encargos que tenham o mesmo destino na contabilidade provavelmente usarão o mesmo grupo de conta.
Referência:
Tabela: PENCARGO
Campo: CGDEBITO
Onde cadastrar: Cadastros de Tabelas Dinâmicas - Código GRPGER
 
Como normalmente se contabiliza os valores creditando em uma conta e debitando em outra, é necessário indicar um grupo de conta para débito e outro para crédito, bem como indicar se existe integração contábil e integração contábil por funcionário para cada caso.
A Conta Gerencial - Grupo conta crédito, portanto, é idêntica ao grupo de conta débito exceto o fato de ser destinada ao crédito.
Referência:
Tabela: PENCARGO
Campo: CGCREDITO
Onde cadastrar: Cadastros de Tabelas Dinâmicas - Código GRPGER
 
O histórico padrão será obrigatório de acordo com a parametrização do RM Saldus e a informação será a referência do histórico-padrão cadastrado no sistema de contabilidade.
 
A Fórmula para Complemento de Histórico será \*ADICIONADA\* ao Complemento do Histórico Padrão.
\*Observação:\*
O uso da fórmula para complemento de histórico não elimina o conteúdo existente no complemento de histórico e, sim, acrescenta informação.
 
\*Exemplo:\*
\*Complemento de Histórico:\* Contabilização ref ao mês:
\*Fórmula para Complemento de Histórico{\*}: MES (fórmula retorna o Mês competência atual) . Ao contabilizar este evento ou encargo o Complemento de histórico gerado será: \*Contabilização ref ao mês: 02\* (sendo o mês usado no exemplo o Mês de Fevereiro).
 
\*Observação:\*
\*01 -\* Entre os campos Complemento do Histórico e a Fórmula do Complemento do Histórico será acrescentado, no lançamento contábil, um espaço em branco para separar as informações entre estes dois campos.
\*02 -\* Informando uma fórmula com a variável PAR serão levados para o complemento do histórico do lançamento contábil o mês, o ano e o(s) período(s) da competência que está sendo gerado o lote.
O retorno da variável PAR assume dois formatos:
\*Formato 1\* - Quando for(em) selecionado(s) período(s) específico(s) na competência:
\*MM-AAAA-P{\*}, onde:
MM = Mês da competência
AAAA = Ano da competência
P = Período(s) \[quando houver mais de um período, aparecem separados por vírgula\]
Exemplo: 01-2011-1,2 onde
01 = Janeiro
2011 = Ano de 2011
1,2 = Períodos 1 e 2
\*Formato 2\* - Quando NÃO for(em) selecionado(s) período(s) específico(s) na competência:
\*MM-AAAA{\*}, onde:
MM = Mês da competência
AAAA = Ano da competência
Exemplo: 12-2011 onde:
12 = Dezembro
2011 = Ano de 2011
\*Atenção:\*
O retorno da variável PAR na contabilização é sempre STRING, e os valores de Mês, Ano e Período(s) da competência são separados por hífen (-).
 
\\]]>

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Encargos
