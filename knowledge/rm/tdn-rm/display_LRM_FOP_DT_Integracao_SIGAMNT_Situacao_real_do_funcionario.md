---
content_hash: 4193b5e58444dedbf67954acac74914e88de9264bd47cdfc35fcdda116294650
fetched_at: '2026-06-29T00:06:29.691324+00:00'
page_id: '234615779'
product: rm
source: tdn-rm
title: FOP_DT_Integracao_SIGAMNT_Situacao_real_do_funcionario
type: documentation
url: https://tdn.totvs.com/display/LRM/FOP_DT_Integracao_SIGAMNT_Situacao_real_do_funcionario
version: 1
---

# SIGAMNT - Ler situação real do funcionario no RM

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Folha de Pagamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Funcionários |  | |
| **Versões/Release:** | 12.1.10 |

## Descrição

Nesta versão, permitimos que o módulo SigaMNT do Protheus recupere a situação atual dos funcionários no módulo TOTVS Folha de Pagamento da linha RM. Com isso foi adicionado um mapeamento de uma mensagem de requisição, para que o Protheus solicite a situação dos funcionários e o RM retorne.

## Procedimento para Utilização

Para que o sincronismo dessa mensagem funcione corretamente, é necessário que os seguintes pré-requisitos sejam atendidos:

• WebService RM configurado no Protheus.  
• Cadastro do de-para da empresa/filial realizado.  
• Integração de funcionários realizada.

Para atender a arquitetura proposta, deverá ser utilizado/implementado os seguintes itens:

**Mensagem única:** Será utilizada a mensagem de requisição *GetEmployeeSituations\_1\_000*, que atende à demanda desse requisito. Segue a estrutura da mensagem

**• Transformação:** Criamos um cadastro de transformação para realizar a montagem da mensagem acima no RM. O cadastro será realizado através do configurador de integrações e terá as seguintes informações:

 ****•**Id (Nome da entidade):** GETEMPLOYEESITUATIONS  
**•****Versão (Versão da mensagem única):** 1.000  
**•****Tipo do server:** Custom Adapter – adapter customizado.  
**•****Descrição:** Retorna a situação do funcionário conforme matrícula do funcionário e período informado.  
**•****DataServer:** Adapter para manipular os campos de entrada e o retorno enviado para o Protheus.

 Será implementado uma chamada ao serviço de retorno das situações conforme imagens abaixo:

**Cadastro de código de fonte**

**Implementação das funções DoExecute() e CreateReturnContent()**

****•**XsltEntrada:** Transformação da parte de requisição da mensagem única para o contexto RM.  
****•**XsltRetorno:** Transformação do retorno RM para a mensagem única.

Para acessar o cadastro, siga os passos abaixo:

***Passo 1: Acessar o módulo de Integração***

***Passo 2: Acessar o menu Transformação***

******•****De-para:** O de-para é um requisito da própria integração. Precisa ser garantido que o de-para de empresa/filial esteja cadastrado, e que os funcionários já estejam integrados.  
****•******Mapeamento de entidades:**  Adicionamos um novo cadastro de mapeamento à integração. O cadastro será realizado através do configurador de integrações e terá as seguintes informações:  
******•****Entidade:** Transformação que será utilizada

 

Para acessar o cadastro, seguir os passos abaixo:

***Passo 1: Acessar o módulo de Integração***

***Passo 2 : Acessar o menu Integrações***

******Passo 3: Selecionar a integração e acessar o anexo Mapeamento de Entidade******

******•****Configurador de integrações:** O configurador será utilizado para realizar o cadastro dos itens acima. Deverá ser realizado novamente para integração conforme imagens abaixo

****Passo 4: Acessar o módulo de Integração****

******Passo 5: Acessar o menu Configurar******

******Passo 6: Informar usuário/senha do banco de dados e avançar******

***Passo 7: Selecionar a opção da integração destacada e avançar***

***Passo 8: Executar o processo para atualizar a integração***

**Parâmetros Necessários**

Para o correto funcionamento da integração, o Protheus deverá enviar as seguintes informações obrigatórias para o RM:

 ******•******CompanyId: Código da empresa do funcionário  
******•******StartDate: Data início da situação  
******•******FinishDate: Data fim da situação  
******•******StartEmployeeCode: InternalId do funcionário

No caso de ser apenas um dia, o FnishDate deverá ter o mesmo calor que o StartDate.

**Matrícula do Funcionário** 

Como a chapa pode ser valor alfanumérico, não será utilizado a faixa de matrículas. Nesse caso será utilizado somente a tag ***StartEmployeeCode***, enquanto a tag ***FinishEmployeeCode*** ficará obsoleta.

 

**Mapeamento das situações no RM**

O mapeamento das situações no RM será realizado da seguinte maneira:

1) Segue o de-para das situações da mensagem única com as situações do RM:

Significado da situação:

|  |  |  |
| --- | --- | --- |
|  | PCODSITUACAO.CODINTERNO | DESCRIÇÃO |
| 1 - Trabalhando | A/V/X/Z | Ativo |
| 2 - Afastado | U/P/T/E/M/R/W | Afastado |
| 3 - Entrada Transferência | - | - |
| 4 - Saída Transferência | - | - |
| 5 - Férias | F/G | Férias |
| 6 - Rescisão Contrato | D | Demitido |
| 7 - Falta Injustificada | - | - |
| 8 - Jornada Incompleta | - | - |
| 9 - Ausência Justificada | - | - |
| 10 - Contrato Desativado | C | Contrato de Trabalho Suspenso |

Tipo do afastamento:

|  |  |  |
| --- | --- | --- |
|  | PCODSITUACAO.CODINTERNO | DESCRIÇÃO |
| 1 - Ausência | U | Outros |
| 2 - Doença | P/I/O | Previdência Social/ Apos. Invalidez/ Doença Ocupacional |
| 3 - Acidente | T | Acidente do Trabalho |
| 4 - Maternidade | E/W | Licença Mater./ Licença Mater. Compl. 180 dias |
| 5 - Paternidade | - | - |
| 6 - Serviço Militar | M | Serv. Militar |
| 7 - Licença Remunerada | R/S | Licença Remun./ Mandato Sindical |
| 8 - Licença não Remunerada | L | Licença s/venc |

1) Será verificado se a data informada é anterior a data de admissão do funcionário. Caso positivo será enviado um retorno informando que o funcionário não estava admitido.

2) Se a data informada for igual ou posterior a data de admissão:

   2.1) Será verificado se existe data de desligamento e a data informada é maior ou igual a data desligamento. Caso positivo a situação mapeada será “D”. (Demitido).

   2.2) Caso negativo, será verificado se existe data de desligamento e a data informada é menor que a data desligamento, ou se não existe a data de desligamento. Caso positivo:  
        2.2.1) O sistema irá verificar no histórico de férias se possui período de gozo na data informada. Caso positivo a situação mapeada será “F”. (Férias).  
        2.2.2) Caso negativo, o sistema irá verificar no histórico de afastamento se o funcionário esteve afastado na data informada. Caso positivo a situação mapeada será o tipo do afastamento encontrado.  
        2.2.3) Caso negativo, o sistema irá verificar no histórico de situação se o funcionário possui histórico para a data informada. Caso positivo a situação mapeada será a situação encontrada no histórico.  
        2.2.4) Caso negativo, a situação mapeada será “A”. (Ativo)

3) A data início e fim da situação será conforme o histórico. Caso a situação seja a situação atual, a data fim enviada será a data atual.

Exemplos:

Situação 1 :

Funcionário demitido em 15/03/2015

Hoje é 15/03/2015 e foi pedido a situação do funcionário em 16/03/2015.  
Deverá retornar a situação ‘D’ (15/03/2015 a data atual)

Hoje é 15/03/2015 e foi pedido a situação do funcionário em 14/03/2015.  
Deverá verificar se o funcionário está de férias ou afastado, caso não esteja em nenhumas destas situações deverá verificar se a data está dentro de algum dos períodos do histórico de situação e retornar a situação equivalente. Caso não seja encontrado em nenhuma dessas alternativas, deverá ser retornado ‘A’ (Ativo) como padrão (Data admissão a data atual).

Situação 2 :

Funcionário Ativo em 15/03/2015  
Férias em 01/04/2015 a 20/04/2015  
Afastado por Acidente do Trabalho em 01/02/2015 a 28/02/2015

Hoje é 15/03/2015 e foi pedido a situação do funcionário em 16/03/2015, deverá retornar ‘A’ (Ativo) (15/03/2015 a 31/03/2015)  
Hoje é 15/03/2015 e foi pedido a situação do funcionário em 01/04/2015, deverá retornar ‘F’ (Férias) (01/04/2015 a 20/04/2015)  
Hoje é 15/03/2015 e foi pedido a situação do funcionário em 10/02/2015, deverá retornar ‘T’ (Afastado por acidente de trabalho)  
(01/02/2015 a 28/02/2015)
