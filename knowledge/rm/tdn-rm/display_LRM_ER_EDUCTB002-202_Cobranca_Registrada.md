---
content_hash: 6caf0be5e9cce213c9de4431902d92b1d7148d2eb9179e4fb865feecf1d5c37f
fetched_at: '2026-06-29T00:08:21.537977+00:00'
page_id: '269059257'
product: rm
source: tdn-rm
title: ER_EDUCTB002-202_Cobranca_Registrada
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_EDUCTB002-202_Cobranca_Registrada
version: 132
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOTVS Gestão Financeira |
| **Segmento Executor** | Educacional | | |
| **Projeto** | EDUCTB002 | **IRM** |  |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

## 

## Objetivo

Segundo comunicado da Febraban, a partir de janeiro/2017, os boletos devem ser emitidos por cobrança registrada para que sejam aceitos pelos bancos. Desde 01/06/2015, a rede bancária deixou de ofertar o produto cobrança sem registro. Os novos contratos de cobrança oferecidos pelos bancos são apenas de cobrança registrada.

O TOTVS Gestão Financeira foi evoluído para permitir num mesmo lançamento mais de um boleto. Com isso o comportamento do boleto mudará nos processos de geração, baixa e remessa.

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Cadastro de Convênio | Alteração | Movimentações Bancárias -> Controle Bancário-> Convênio | Parâmetros para controle da remessa e cobrança registrada |
| Registro de Boleto | Alteração | Contas a Pagar/Receber -> Operações Financeiras -> Boleto | Defaults de boleto, status, impressão e geração de código de barras |
| Lançamentos Financeiros | Alteração | Contas a Pagar/Receber -> Operações Financeiras -> Lançamentos | Não gravar campos do boleto no lançamento |
| Boletos do Lançamento | Alteração | Contas a Pagar/Receber -> Operações Financeiras -> Lançamentos -> Boleto | Mais de um boleto por lançamento, desvincular boleto do lançamento |
| Baixa de Lançamento | Alteração | Contas a Pagar/Receber -> Operações Financeiras -> Lançamentos -> Baixa | Status dos boletos vinculados |
| Conta Caixa | Alteração | Movimentações Bancárias -> Controle Bancário-> Contas/Caixa | Novos defaults na conta caixa |
| Fórmulas do Financeiro | Alteração | Fórmula | Leitura de dados do boleto |
| Registro Online de boletos | Criação | Portal Educacional -> Financeiro | Registro de boletos online |
| Impactos Boleto Registrado | Criação | Utilitários -> Impacto de Conversão -> Verifica Impactos Novo Boleto Registrado. | Verifica os impactos o boleto registrado dentro do sistema. |

**Evolução do convênio**

Objetivo: automatizar a geração de remessa de cobrança, débito automático e pagamento; facilitar o processo do cliente, permitindo que não seja necessário o preenchimento dos campos a cada inclusão de boleto.

* Campos para cada tipo de remessa (cobrança, pagamento e débito automático)  para informar a composição do nome do arquivo de remessa no convênio. Essa configuração aceitará uma parte fixa e tags para substituir por outras informações
* Campos para cada tipo de remessa (cobrança, pagamento e débito automático) para informar a extensão do arquivo de remessa.
* Campos para cada tipo de remessa (cobrança, pagamento e débito automático) para informar o diretório destino default para salvar as remessas.
* Nos processos de remessa os diretórios e nomes de arquivos serão carregados automaticamente se as informações estiverem preenchidas no convênio da remessa.
* Campos para informar os defaults para os seguintes campos do boleto: Espécie CNAB, Comando, Instrução Cod. 1, Instrução Cod. 2 e Aceite. Esses defaults estão disponíveis nos processos de inclusão e alteração do cadastro de Convênio e usados no processo de inclusão de boleto.
* Campo para definir se o boleto permite o registro online dos boletos gerados. Caso afirmativo irá disponibilizar campos para informar URL do serviço de registro de boleto e URL do serviço de retorno de registro.
* Campo para indicar o relatório default para impressão (filtrar por relatórios com Aplicação "Financeiro", coligada corrente ou global, e tipo igual a 81).

**Evolução do boleto**

Objetivo: facilitar o processo do cliente, permitindo que não seja necessário o preenchimento dos campos a cada inclusão de boleto; adequar o boleto à exigências de cobrança registrada.

* Tratamento no processo de impressão de boletos do Financeiro para que o relatório definido no convênio do boleto seja selecionado automaticamente. Caso seja selecionado mais de um boleto de diferentes convênios que estejam parametrizados com diferentes relatórios não será selecionado default.
* Criada a opção "Inativo" para o campo *Status do boleto*, que será usada para indicar a inativação quando os lançamentos desse boleto foram totalmente baixados por outros boletos. O boleto com esse status terá comportamento similar ao "Cancelado" e assim foi tratado em todos os pontos onde há filtro ou condições de execução que teste esse valor.
* Para o campo Status CNAB criada a opção "Registrado online" que indica que o boleto foi registrado através do processo de registro online disponibilizados pelos bancos.
* No processo de inclusão de boleto adicionados os campo Conta caixa, Convênio e a opção "Utilizar conta e convênio do lançamento". Se ela estiver marcada o boleto deverá buscar a conta caixa e o convênio do lançamento, caso contrário, estas opções deverão ser informadas manualmente. Neste caso apenas o convênio deve ser obrigatório.
* As informações de conta caixa e convênio no lançamento passam a ser apenas default para a geração de boletos, ou seja, não é necessário que o boleto possua o mesmo convênio do lançamento. Ao alterar essas informações no lançamento, os boletos não serão alterados.
* O processo de geração de código de barras realizará a validação do tipo do boleto e, se for de débito automático, deverá ser enviada uma mensagem informando que o código de barras não pode ser gerado. A tela de inclusão/edição de boleto também deverá ser alterada para que o campo e o botão, responsável por gerar o código de barras, e o campo IPTE sejam desabilitados para os boletos de débito automático.
* Criado processo associado ao boleto onde o usuário escolhe o lançamento que será desvinculado apenas desse boleto.
* Trava no processo Relatórios / Impressão de boletos na visão de boletos, só executar caso o boleto de um convênio com tipo de cobrança "Registrada" esteja com o Status CNAB valorado como "Registrado".

**Evolução do lançamento**

Objetivo: o lançamento financeiro será evoluído para permitir o vínculo a mais de um boleto de cobrança.

* O registro de lançamento financeiro a receber (tabela FLAN) não mais grava as informações do boleto (IDBOLETO, CNABNOSSONUMERO, CNABBANCO, CNABACEITE, CNABINSTRUCAO1, CNABINSTRUCAO2) na inclusão ou alteração do boleto. Sempre que precisar dessas informações do boleto o sistema irá buscar na tabela de boleto (FBOLETO) e não mais no lançamento (FLAN).
* Tratar o campo CNABSTATUS do lançamento: serão avaliados todos os boletos associados a ele para que o CNABSTATUS mais relevante seja atualizado utilizado. Seguem, em ordem decrescente, os status mais relevantes:   
  \* Baixado  
   \* Registrado ou Registrado Online  
   \* Remetido  
   \* Recusado  
   \* Não remetido   
   Por exemplo: O lançamento "x" está associado aos boletos 1 e 2 . O primeiro possui CNABSTATUS igual a remetido e o segundo registrado. Neste caso o CNABSTATUS do lançamento será alterado para registrado .
* Permitir mais de um boleto para um mesmo lançamento. Esse comportamento será possível se o lançamento não possuir um boleto de débito automático vinculado e possuir status "Em Aberto" ou "Parcialmente Baixado". O boleto poderá ser parcial, com o controle feito através de um parâmetro geral do Financeiro "Contas a Receber | Manutenção de Lançamento / Permitir inclusão de boleto parcial Permitir inclusão de boleto parcial", que deve ficar desabilitado se Parâmetro “Não gerar outro boleto para lançamento após baixa parcial” habilitado.
* No processo geração de boleto, ao incluir boleto de cobrança, o usuário poderá optar por gerar um boleto parcial, informando o valor desejado (somente se o parâmetro estiver habilitado). Essa opção só estará disponível para boleto de cobrança e não poderá ser utilizada se o boleto for de débito automático. Nesse caso, o valor do boleto será o valor informado pelo usuário. O sistema validará para que não seja permitido informar um valor maior do que o valor do lançamento (de acordo com a parametrização do convênio – líquido, líquido parcial ou original). Se o parâmetro “Não gerar outro boleto para lançamento após baixa parcial” estiver marcado, não será permitido a inclusão de mais de um boleto para o mesmo lançamento.
* Não permitir vincular um novo lançamento a um boleto parcial.
* O processo de desvincular lançamento do boleto irá desvincular o lançamento de todos os boletos aos quais ele esteja associado.

**Evolução da baixa**

Objetivo: tratar a inativação de boletos associados ao lançamento, quando ocorrer a baixa de um dos boletos daquele lançamento.

* A baixa do boleto continuará a baixar os lançamentos associados a ele. Se o lançamento for baixado totalmente, o status dos boletos associados a ele será alterado para “Inativo”, caso não existam outros lançamentos também associados ao mesmo boleto. Se há algum boleto com outro lançamento associando o boleto o status só altera para inativo caso todos os lançamentos daquele boleto estejam totalmente baixados.
* Ao baixar um lançamento, o usuário deverá escolher qual boleto será baixado, caso exista mais de um associado.
* Ao baixar um boleto parcial, se a baixa do lançamento for parcial, não será gerado um novo boleto para os lançamentos associados ao boleto.
* No cancelamento da baixa de um boleto que foi baixado parcialmente se existir mais de um boleto com status "Em aberto" o boleto que foi gerado na baixa não será cancelado. Caso contrário, o comportamento continua o mesmo já existente, ou seja, o boleto em aberto será cancelado.
* No cancelamento da baixa de um boleto, se existir algum boleto inativo, o status desse será alterado para em aberto ou parcialmente baixado, dependendo da situação.

**Evolução da remessa e retorno bancários**

Objetivo: evoluir a geração de remessa de cobrança e débito automático para a cobrança registrada.

* A geração do código de barras será chamada durante a remessa de cobrança. No caso de ocorrer um erro na geração, aquele lançamento não será enviado para a remessa e a informação será registrada no log para que o usuário tenha conhecimento.
* No processo de cancelamento da remessa o sistema irá limpar automaticamente o código de barras do boleto. Dessa forma, quando o lançamento for remetido novamente ao banco, o boleto poderá ser gerado.
* Os processos de Remessa e Retorno de cobrança, pagamento e débito automático permitirão agendamento.

**Tratamento das fórmulas e relatórios**

Objetivo: evoluir fórmulas e relatórios para tratar mais de um boleto para o lançamento.

* As funções de fórmulas que contém informações relacionadas ao boleto (ACEITE, CARTEIRA, NOSSONUMERO, CONTACAUCAO, DADOSPAGAMENTOBRADESCO, CODBARRABOLETO e IPTEBOLETO) foram evoluídas para permitir lançamentos com mais de um boleto. Vale ressaltar que o contexto de lançamento deixará de ser utilizado, dando lugar para o contexto de boleto.
* Os relatórios e layouts padrões do book que contém informações relacionadas ao boleto (nosso número, código de barras, CNAB, referência do boleto) foram revisados para funcionar de acordo com a evolução que permite lançamentos com mais de um boleto.

**Portal Educacional**

Objetivo: filtro de boletos registrados no Portal.

* Portal Educacional / Processo Seletivo / Gestão Bibliotecária: só apresentará no portal os boletos cujo convênio tem tipo de registro de cobrança como "Registrada" para os boletos com Status CNAB como "Registrado". Para o Educacional há dois pontos, na matrícula e na visualização do extrato financeiro.

**Registro online de boleto**

Cada banco definiu um formato para chamada do serviço de registro online de boletos. Entretanto, existem vários pontos em comum. Será disponibilizada uma página que poderá ser utilizada pelos portais para o registro online. Essa página será responsável por redirecionar o usuário ao banco com o qual esteja trabalhando. Por default, o convênio utilizado para o registro online será o parametrizado no Financeiro.

* Registro Online de boleto no Portal Educacional

Registro de boleto online no Portal Educacional realizando a chamada da página disponibilizada pelo Financeiro:

A tela de parâmetros do módulo educacional (Educacional->RM Portal->Portal - Geral 8/8) deverá fornecer as seguintes opções:

1 - Apresentar boleto de cobrança registrada ainda não registrado no Portal.

2 - Serviços que permitem registro online. Esta opção só ficará habilitada se a opção citada acima estiver desmarcada. Vale ressaltar que os serviços não poderão ser selecionados se o convênio default não for informado na tela de parâmetros do módulo financeiro (Financeiro->Contas a receber->Integração bancária->Cobrança eletrônica).

O extrato financeiro, existente no portal educacional, exibe os boletos do usuário logado. Eles deverão levar em consideração as seguintes regras:

1 - Deverá ser exibida a segunda via se o tipo de cobrança do convênio do boleto for "Registrada" ou, "Não Registrada" e o boleto registrado ou o parâmetro "Apresentar boleto de cobrança registrada ainda não registrado no Portal" estiver marcado.

2 - Se houverem serviços habilitados e marcados, o tipo de cobrança do convênio do boleto for "Registrada" e o boleto possuir CNABSTATUS diferente de registrado será exibida uma tela que irá encaminhar o usuário para a página do banco responsável por registrar boleto.

3 - Se as opções 1 e 2 não forem atendidas será exibida uma mensagem de aviso informado que o boleto precisa ser registrado.

**Validador**

O validador é a ferramenta responsável por procurar nos cadastros de  Consultas SQL, Fórmulas, Relatórios, Eventos Contábeis, Filtros na Visão de Lançamento, Planilhas Net, Gerador de Saídas, Relatórios e até mesmo em Views no Banco de Dados, pelos campos referentes à integração bancária que deixarão de ser preenchidos nos lançamentos, para serem preenchidos no Boleto. Os campos a serem verificados são (tabela FLAN): IDBOLETO, CODIGOBARRA, IPTE, CNABNOSSONUMERO, CNABBANCO, CNABCARTEIRA, CNABCOMANDO, CNABACEITE, CNABINSTRUCAOCOD1 e CNABINSTRUCAOCOD2.

* Sobre o FILTRO: no validador existe uma parametrização de filtro para otimizar o validador. Nele será possível filtrar pelos Sistemas Financeiro (F), Educacional (E,S,U), Incorporação (X) e Estoque Compras e Faturamento (T). Lembrando que o Financeiro não poderá ser desmarcado pois é o sistema que apresentará maior número de impactos. Caso o filtro seja desabilitado será executado para todos os sistemas da linha RM, o que pode causar um aumento considerável no tempo de processamento.
* Sobre o LOG: após a execução será gerado um Log apresentando todos os cadastros onde foram encontrados os campos que sofrerão modificação.

**Tabelas Utilizadas**

* FLAN – Lançamentos financeiros
* FBOLETO - Boletos
* FLANBOLETO - Boletos vinculados ao lançamento
* FCONVENIO - Cadastro de Convênio
* FCXA - Cadastro de Conta Caixa

## Dicionário de Dados

**Arquivo ou Código do Script:** /\*$Versao=FS.2016.09\_02\*/, /\*$Versao=FS.2016.09\_03\*/.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Tabela** | **Campo** | **Tipo** | **Tamanho** | **Valor Inicial** | **Mandatório** | **Descrição** |
| FCONVENIO | CNABINSTRUCAO1 | Short |  |  | Sim ( ) Não (X) | Instrução Cod 1 |
| FCONVENIO | CNABINSTRUCAO2 | Short |  |  | Sim ( ) Não (X) | Instrução Cod 2 |
| FCONVENIO | ESPECIECNAB | Varchar | 1 |  | Sim ( ) Não (X) | Espécie Cnab |
| FCONVENIO | CNABCOMANDO | Short |  |  | Sim ( ) Não (X) | Comando (Cobrança Eletrônica) |
| FCONVENIO | CNABACEITE | Short |  |  | Sim ( ) Não (X) | Aceite (Cobrança Eletrônica) |
| FCONVENIO | URLRETORNOREGBOLETO | Varchar | 255 |  | Sim ( ) Não (X) | URL para retorno do serviço de registro de boleto |
| FCONVENIO | URLSERVICOREGBOLETO | Varchar | 255 |  | Sim ( ) Não (X) | URL do serviço de registro de boleto |
| FCONVENIO | DESTINOREMESSACOB | Varchar | 150 |  | Sim ( ) Não (X) | Caminho do diretório de destino remessa de cobrança eletrônica |
| FCONVENIO | NOMEARQUIVOCOB | Varchar | 100 |  | Sim ( ) Não (X) | Nome do arquivo de cobrança eletrônica |
| FCONVENIO | EXTARQUIVOCOB | Varchar | 5 |  | Sim ( ) Não (X) | Extensão do arquivo de cobrança |
| FCONVENIO | DESTINOREMESSADEBAUTO | Varchar | 150 |  | Sim ( ) Não (X) | Caminho do diretório de destino remessa débito automático |
| FCONVENIO | NOMEARQUIVODEBAUTO | Varchar | 100 |  | Sim ( ) Não (X) | Nome do arquivo de débito automático |
| FCONVENIO | EXTARQUIVODEBAUTO | Varchar | 5 |  | Sim ( ) Não (X) | Extensão do arquivo de débito automático |
| FCONVENIO | DESTINOREMESSAPAG | Varchar | 150 |  | Sim ( ) Não (X) | Caminho do diretório de destino remessa de pagamento |
| FCONVENIO | NOMEARQUIVOPAG | Varchar | 100 |  | Sim ( ) Não (X) | Nome do arquivo de pagamento |
| FCONVENIO | EXTARQUIVOPAG | Varchar | 5 |  | Sim ( ) Não (X) | Extensão do arquivo de pagamento |
| FCONVENIO | DESTINORETORNOPAGAMENTO | Varchar | 150 |  | Sim ( ) Não (X) | Caminho do diretório de destino retorno de remessa de pagamento |
| FCONVENIO | DESTINORETORNOCOB | Varchar | 150 |  | Sim ( ) Não (X) | Caminho do diretório de destino retorno de cobrança eletrônica |
| FCONVENIO | DESTINORETORNODEBAUTO | Varchar | 150 |  | Sim ( ) Não (X) | Caminho do diretório de destino retorno de remessa débito automático |
| FCONVENIO | PERMITEREGONLINEBOLETO | Short |  |  | Sim ( ) Não (X) | Permite registro de boleto online |
| FCONVENIO | IDRELATORIOBOLETO | Int |  |  | Sim ( ) Não (X) | Identificador do relatório impressão boleto |
| FCONVENIO | CODCOLRELATBOLETO | DCODCOLIGADANULL |  |  | Sim ( ) Não (X) | Coligada relatório impressão boleto |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
