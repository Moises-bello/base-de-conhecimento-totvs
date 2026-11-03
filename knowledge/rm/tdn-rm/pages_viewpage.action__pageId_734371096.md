---
content_hash: 987fe13ea74be8df21c35a410035afe0b7eca5f663f187add3fb7a2b8d1a17bb
fetched_at: '2026-06-29T00:11:29.214065+00:00'
page_id: '734371096'
product: rm
source: tdn-rm
title: Análise de Antibiótico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=734371096
version: 12
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela Análise de Antibiótico**
   1. **Anexo - Cultura / Germe**
   2. **Anexo - Infecção**
   3. **Anexo - Antibiótico de Uso Prévio**
   4. **Anexo - Registro de Intervenção**
4. **Comportamentos do Painel**
   1. **Mais de um Sítio Secundário no Pedido de Antibiótico**
   2. **Protocolos Institucional**
5. **Tabelas utilizadas**

sumarioVisão Geral

## **01. VISÃO GERAL**

Essa funcionalidade tem a finalidade de servir como um painel para acompanhamento de Antibióticos utilizados pelo paciente (antibióticos dispensados) de acordo com o sítio de infecção, possibilitando analisar as culturas associadas e fatores relacionados às infecções, uso de antibióticos prévios, tempo de tratamento, se o antibiótico está de acordo com o protocolo institucional e sugerir intervenções além da possibilidade de definir data para revisão.

Essa funcionalidade **não** possui nenhuma ação cadastral na visão principal (Incluir, Excluir, Alterar) e não possui nenhuma execução de processo. Somente é possível registrar intervenções para cada antibiótico (conforme tópico "Anexo - Registro de Intervenção") ou informações no registro de infecção (conforme tópico "Anexo - Infecção").

Todas as colunas disponíveis na visão possuem possibilidade de construir filtros com base nas necessidades de análise dos dados. 

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

|  |  |
| --- | --- |
| **Menu / Caminho:** | Saúde/Controle de IRAS/Apoio Gerencial/Análise/Análise de Antibiótico |

## **03. TELA ANÁLISE DE ANTIBIÓTICO**

| Campo | Descrição |
| --- | --- |
| Leito | Leito na qual o paciente está acomodado no momento da análise (campo de Leito na rotina de movimentação de leito) |
| Atendimento | Identificador do atendimento do paciente preenchido na internação do paciente |
| Paciente | Nome do paciente |
| Data de Internação | Data de Internação do paciente referente ao atendimento que contém o antibiótico em análise |
| Data de Alta/Óbito | Data de Alta / Óbito do paciente referente ao atendimento que contém o antibiótico em análise |
| Tipo de Alta | Caso o paciente já tenha tido saída, informa qual o tipo de alta acordo com o preenchimento desse campo na internação:   * Alta * Transferência * Óbito |
| Tempo de Internação | Cálculo automático realizado pelo sistema, em número de dias, entre a data da internação e a data da alta/óbito |
| Grupo de Antibiótico | Grupo de Antibióticos à qual o antibiótico em análise pertence |
| Antibiótico | Antibiótico administrado no paciente na qual está sendo feita a análise |
| Cód. Sítio Secundário | Código do sítio secundário do pedido de antibiótico |
| Sítio Secundário | Sítio Secundário do pedido de antibiótico |
| Sítio Primário | Sítio Primário relacionado ao sítio secundário do pedido de antibiótico |
| Tipo de Infecção | Tipo de Infecção classificada no pedido de antibiótico:   * Hospitalar * Comunitária * Hospitalar de Outra Instituição |
| Especialidade Clínica | Especialidade do médico que realizou o pedido de antibiótico |
| Atende Protocolo | Indica se a utilização do antibiótico está seguindo algum protocolo institucional (1ª ou 2ª Linhas) ou se está fora dos protocolos.  \*Maiores informações na sessão "4b - Protocolos Institucional"   * 1ª Linha * 2ª Linha * Fora do Protocolo |
| Uso Prévio de Antibiótico | Indica se o paciente usou antibióticos nos atendimentos anteriores ao atendimento em questão observando o limite de 90 dias anteriores a contar da data da análise referente à data do pedido de antibiótico. |
| D1 de Antibiótico | Primeira data de uso de antibiótico no atendimento em questão (independente do pedido de antibiótico) |
| D Final de Antibiótico | Última data de uso de antibiótico no atendimento em questão (independente do pedido de antibiótico) |
| Total de Dias de Antibiótico | Cálculo automático realizado pelo sistema, em número de dias, entre o D1 de antibiótico e o D Final de antibiótico |
| Pedido / Requisição | Número do pedido/requisição de antibiótico |
| Data do Pedido / Requisição | Data do pedido/requisição de antibiótico |
| Indicação do Antibiótico | Indicação de uso do antibiótico classificado no pedido de antibiótico:   * Profilático * Terapêutico * Sem Indicação |
| Tipo de Ferida | Tipo de ferida classificada no pedido de antibiótico:   * Limpa * Potencialmente Contaminada * Contaminada * Infectada |
| Médico | Médico que realizou o pedido de antibiótico |
| Unidade Clínica | Unidade clínica de dispensação do antibiótico discriminada no pedido de antibiótico |
| Utilização | Dose (mg) dispensada |
| Data Fim | Data final de utilização do antibiótico, informada manualmente ou calculada na tela que contém as dispensações do antibiótico |
| Número da Internação | Código interno sequencial da internação do paciente |
| Antibiótico Validado | Indica se o pedido de antibiótico foi validado pelo usuário após a importação das dispensações (Status de importação) |
| Número do Paciente | Código interno sequencial do paciente |
| Prontuário | Número do prontuário do paciente |

* **Anexo - Cultura / Germe**
  1. Essa rotina tem como objetivo listar todas as culturas e germes importados para o prontuário do paciente no atendimento selecionado na visão principal.

* **Anexo - Infecção**

Essa rotina tem como objetivo listar todas as infecções registradas no prontuário do paciente no atendimento selecionado na visão principal.

* **Anexo - Antibiótico de Uso Prévio**

Essa rotina tem como objetivo listar todos os antibióticos utilizados pelo paciente em atendimentos / internações anteriores à que está sendo analisada.

{ex

* **Anexo - Registro de Intervenção**

Essa rotina tem como objetivo registrar as intervenções necessárias sugeridas pela equipe de Controle de IRAS após a análise do uso do Antibiótico pelo paciente. Cada Antibiótico dispensado (Antibiótico que está sendo analisado) poderá ter uma ou mais intervenções podendo ter uma evolução das ações de intervenção.

Cada registro de intervenção contém informações se há a Necessidade de Intervenção, Descrição da Intervenção, Observação da Análise, Data de Revisão e Status (se foi aceita ou não pelo corpo clínico).

Na tela de Anexo podem ser criados filtros baseados nessas informações para que a equipe possa gerenciar as intervenções em andamento.

| Campo | Descrição |
| --- | --- |
| Número | Código sequencial de registro da intervenção gerada de forma automática |
| Status | Status atual da Intervenção   * Não Analisada * Aceita * Não Aceita |
| Data de Revisão | Data da revisão da análise de intervenção por parte da equipe de Controle de IRAS. Preenchimento manual pelo usuário. |
| Necessário Intervenção | Informa se após a análise é necessária a intervenção da equipe de Controle de IRAS no uso do antibiótico pelo paciente |
| Descrição da Intervenção | Descrição / Ação que objetiva a Intervenção |
| Observações da Análise | Análise detalhada sobre a intervenção |

Comportamentos do Painel

## **04. COMPORTAMENTOS DO PAINEL**

* **Mais de um Sítio Secundário no Pedido de Antibiótico**

A base do painel de análise é a informação do antibiótico e seu sítio de infecção, portanto se, para o pedido de antibiótico dispensado, estiver associado mais de um Sítio Secundário a linha de análise do antibiótico se repetirá para cada sítio secundário e antibiótico.

Pedido de Antibiótico:

Painel de Análise desse Antibiótico:

Para uma melhor visualização, nesses casos recomendamos o agrupamento por Sítio de Infecção:

* **Protocolos Institucionais**

A coluna "Atende Protocolo" tem como objetivo indicar se a prescrição / dispensação do antibiótico segue um protocolo institucional ou não. Caso siga, essa indicará se a indicação de uso trata-se de um antibiótico de 1ª Linha ou 2ª Linha e caso não siga a indicação de um protocolo institucional será exibido o status de fora do protocolo conforme indicações visuais abaixo:

Os protocolos têm como gatilho a informação do sítio secundário para qual o antibiótico está sendo prescrito / dispensado.

O cadastro do protocolo pode ser feito no caminho: Saúde/Controle de IRAS/Cadastros/Cadastros/Antibiótico/Adequação de Antibiótico

Independente do tipo de adequação (Terapia empírica ou Terapia orientada por patógeno) deve-se informar o sítio de infecção a ser considerado para orientar o antibiótico a ser utilizado e qual sua linha de uso (1ª ou 2ª), caso o sistema não encontre essa associação (Sítio Secundário x Antibiótico) então será considerado como "Fora do Protocolo".

     

Tabelas utilizadas

## **05. TABELAS UTILIZADAS**

* SZJANALISEANTIBIOTICO     -     Análise de Antibióticos
* SZJANTIBIOTICO     -     Cadastro de Antibiótico
* SZJAREACRITICA     -     Internação na área crítica
* SZJESPECIALIDADE     -     Cadastro de especialidade
* SZJGERME     -     Cadastro de germes
* SZJGRUPOANTIBIOTICO     -     Cadastro do grupo de antibiótico
* SZJINFECCAOHOSPITALAR     -     Infecção hospitalar (clínica)
* SZJINTERNACAO     -     Tabela de internação do paciente
* SZJITEMPEDIDOANTIBIOTICO     -     Tabela lançamento antibiótico
* SZJMATERIAL     -     Grupo de material de cultura
* SZJMEDICO     -     Cadastro de médicos
* SZJPACIENTE     -     Cadastro paciente
* SZJPEDIDOANTIBIOTICO     -     Tabela inclusão de antibióticos
* SZJPEDIDOCULTURA     -     Pedido de cultura final
* SZJRESULTADOCULTURA     -     Resultado de cultura final
* SZJSITIOPRIMARIO     -     Cadastro de sítio primário
* SZJSITIOSECUNDARIO     -     Cadastro do sítio secundário
* SZJUNIDADECLINICA     -     Cadastro unidade clínica
* SZJXSITIOPEDANTIBIOTICO     -     Sítios secundários para o antibiótico
