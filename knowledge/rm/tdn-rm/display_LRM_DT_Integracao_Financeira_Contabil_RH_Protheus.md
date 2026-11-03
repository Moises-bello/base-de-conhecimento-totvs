---
content_hash: b443155e4c7162e70f86857fddca7f5d69b6402a569b1fec386477a03e49b673
fetched_at: '2026-06-29T00:06:24.942488+00:00'
page_id: '224127138'
product: rm
source: tdn-rm
title: DT_Integracao_Financeira_Contabil_RH_Protheus
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Integracao_Financeira_Contabil_RH_Protheus
version: 5
---

# NTEGRAÇÃO FINANCEIRA E CONTÁBIL DO TOTVS FOLHA DE PAGAMENTO x BACKOFFICE DO PROTHEUS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Folha de Pagamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Segmento Integração* | *Integração* | |
| **Versão/Release:** | *12.1.4* |

## Descrição

Este documento contém informações da integração do TOTVS Folha de Pagamento RM com o BackOffice Protheus.

Na integração Financeira, pelo RM, não contempla o envio dos atributos "Item Contábil" e "Classe de Valor" para o Protheus.

## Procedimento para Utilização

**Instalar e Configurar EAI RM**

***Pré Requisitos:***O WebService de Integração da linha RM devem ser hospedados no Microsoft IIS. Além disto, a Biblioteca RM necessita da Microsoft .NET Framework. Assim, os pré-requisitos de instalação para o EAI RM são os seguintes:   
Microsoft .NET Framework 4.0;   
Internet Information Services (IIS)

***Instalar o WebService de Integração (TBC):***

Execute o instalador “TOTVS Business Connect – [versão].msi” e patchs disponíveis, se houver. Este pacote cria uma aplicação no IIS e copia os arquivos necessários para a utilização dos WS.  
Os WS serão instalados na porta 80 (como é a porta padrão pode ser omitida na url). E o alias de banco de dados padrão será CORPORERM. Mas o administrador do sistema deverá alterar esta e demais configurações, se desejado, editando o arquivo Web.config que se encontra no diretório de instalação RM na pasta WS\_TBC.

***Execução do Configurador da Integração***

Acesse RM / Segmento Integrações / Aba Ferramentas / Configurar. Será apresentado um wizard de configuração do TBC. Este projeto utiliza mensageira padrão TOTVS, então selecione a opção **“TOTVS Folha de pagamento RM x BackOffice Protheus”** e execute o processo.

***Configuração da Integração***

Acesse RM / Segmento Integrações / Aba Integração / Mensagem Única / Integrações. Esta interface permite incluir ou alterar um pacote de integração.

Selecione **TOTVS Folha de pagamento Rm x BackOffice Protheus** **(Identificador = 1010)** e clique em editar para alterar as configurações iniciais criadas pelo configurador *(tópico 3.4)*.

***Identificação***

NOME INTEGRAÇÃO: Este é o nome completo da integração. Trata-se de um campo meramente informativo.

NOME REDUZIDO: Este é o nome reduzido da integração. Trata-se de um campo apenas informativo.

SISTEMA INTEGRADO:  Este é um mnemônico que identifica a aplicação de origem e será enviado no atributo “name” da tag <Product> no XML trafegado. **Ex:** “PROTHEUS”.

SIGNIFICADO DE COLIGADA: Define qual o limite da identificação da coligada, se representa a companhia ou a unidade de negócio.

URL WEB SERVICE: Informe o endereço do WebService Protheus para envio de mensagens. Utilize o formato http://[servidor]:[porta]/EAIService.apw . Para verificar se o WS Protheus está disponível digite o endereço do mesmo no seu navegador (no formato http://[servidor]:[porta]), na página apresentada procure pelo texto EAISERVICE).

USUÁRIO AUTENTICAÇÃO: Informe o nome do usuário para autenticação pelo WebService.

SENHA AUTENTICAÇÃO: Informe a senha para autenticação pelo WebService.

 

***Mapeamento de Entidades (anexo)***

Aqui é possível fazer uma mapeamentos de cada entidade (cada mensagem única) que faz parte do pacote de integração. O Wizard de Configuração fará o mapeamento padrão automaticamente. Alterações só devem ser feitas com critério. Vale ressaltar que as alterações realizadas precisam ser muito bem documentadas, pois a atualização de versões e reconfiguração da integração pode substituí-las, para aplicar ajustes necessários ou até mesmo melhorias.

Caso seja necessário acrescentar uma entidade à integração que não esteja no pacote padrão, clique em Anexos e escolha “Mapeamento de Entidades”. Na tela que é apresentada informe o código ou nome da mensagem. Clique no botão reticências (...) para localizar a mensagem na lista de mensagens pré-cadastradas.

 

***EAI – Fila de Mensagens Únicas***

Acesse RM / Segmento Integrações / Aba Integração / Mensagem Única / Fila de mensagens únicas. Nesta tela serão registradas as informações de envio e recebimento de mensagens XML trafegadas pela integração. Para ver mais detalhes da mensagem trafegada de um duplo clique no registro, para detalhes de execução (erro ou sucesso) selecione o registro e clique em *Anexos / Informações de execução de mensagem*, neste anexo é possível visualizar a mensagem de resposta.

***Parametrização do Totvs folha de pagamento***

Acesse RM / segmento RH / aba Ambiente / Parâmetros / Folha de pagamento. Nesse parametrizador serão registradas informações dos parâmetros de integração da folha RM com qualquer BackOffice de terceiros.

Importante: O documento em questão detalha a integração da folha da RM com o  BackOffice do Protheus.

Porém, a folha da RM está preparada para integrar com qualquer BackOffice. Para isso, basta desenvolver e mapear as mensagens no EAI da RM.

 

**Usa integração com outros BackOffice:** Este parâmetro deve ser marcado caso queira integrar a folha da RM com outros BackOffice. Se o mesmo for desmarcado, a folha será integrada com o BackOffice da RM.  
**Qtde. partidas contábeis enviadas por pacote contábil:** Esse parâmetro armazena a quantidade de partidas contábeis que devem ser enviadas para os BackOffice. Esse parâmetro foi criado devido a uma limitação da arquitetura do Protheus em receber pacotes grandes de informações nas suas mensagens.

 

**Transações/Entidades**

***Mapeamento manual (cadastro de/para)***

Será necessário primeiro fazer o cadastro manualmente no Protheus e no RM e depois configurar o “de/para” de integração correspondente (RM e Protheus possuem interfaces específicas para este fim).

***Empresa e Filial***

O primeiro cadastro que deve ser realizado para operação dos sistemas é o de Empresa (Coligada) e suas Filiais. No RM estas entidades são cadastros comuns, mas no Protheus a Empresa e as Filias são definidas em arquivos de configuração de ambientes sendo parte da implantação do Protheus padrão.

A maioria das mensagens de integração fará referências ao cadastro de Empresa/Coligada.

Ex:

|  |  |
| --- | --- |
| **De-para RM (Empresa)** | |
| **Tabela RM** | GFILIAL |
| **Chave Primária RM** | CODCOLIGADA|CODFILIAL |
| **Valor Chave Primária RM** | 1|2 |
| **Sistema Integrado** | PROTHEUS |
| **Valor Chave Integração** | 10|113 |

Obs: Nas integrações com o Protheus, será necessário cadastrar manualmente na tabela de De/Para um mapeamento da coligada para ela mesma (conforme exemplo abaixo). Esse cadastro é necessário para o correto funcionamento dos códigos de *extensions* criados nas integrações.

|  |  |
| --- | --- |
| **De-para RM (Empresa)** | |
| **Tabela RM** | GCOLIGADA |
| **Chave Primária RM** | CODCOLIGADA |
| **Valor Chave Primária RM** | 1 |
| **Sistema Integrado** | PROTHEUS |
| **Valor Chave Integração** | 1 |

Nesse projeto não está sendo contemplado o sincronismo automático de empresas e filiais.  
Obs: Em integração específicas com o Protheus, no cadastro de “de/para” o campo “Tabela RM” deve ser preenchido com a tabela “GFilial” para buscar a coligada, conforme exemplo acima.

***Tipo de Documento***

Esse projeto não contempla o sincronismo automático de tipos de documentos. Portanto, o cadastro dessas informações deve ser feito manualmente no RM e no Protheus e o cadastro dos “de/para” devem ser feitos manualmente em ambos os lados.

A mensagem contendo dados de lançamentos financeiros fará referência aos tipos de documentos cadastrados.

|  |  |
| --- | --- |
| **De-para RM (Empresa)** | |
| **Tabela RM** | FTDO |
| **Chave Primária RM** | CODCOLIGADA|CODTDO |
| **Valor Chave Primária RM** | 1|0001 |
| **Sistema Integrado** | PROTHEUS |
| **Valor Chave Integração** | 10|1 |

***Mensagens de recebimento (Protheus -> RM)***

Já os cadastros a seguir devem ser feitos **somente no BackOffice Protheus** e sincronizados para o RM, via integração. No RM esses cadastros devem ser configurados para  “somente leitura” no módulo de segurança.

***Fornecedor***

As configurações iniciais desta integração criará um parâmetro chamado “RH\_CLIFORAUTOINC” que irá definir se utiliza Auto incremento ou não para o campo “FCFO.CODCFO”. Caso o parâmetro não seja “De auto incremento”, a máscara do código do Cliente/Fornecedor deve ser configurada de acordo com a máscara do cliente/fornecedor enviada pelo Protheus:

Ex: “QQQQQQQQ”. [permite qualquer caractere limitado a 8 posições].

Caso o parâmetro seja de “auto incremento”, a máscara deve ser definida como “” (vazio) e o parâmetro do financeiro “Usar código sequencial (se máscara for numérica)” deve ser marcado.

Além de fornecedor, é possível integrar o cadastro de clientes (que no Protheus é um processo separado). Para isso basta cadastrar o adapter para a rotina de Cliente da mesma forma que foi cadastrado o adapter de Fornecedor.

***Centro de Custo***

As configurações iniciais desta integração criará um parâmetro chamado “RH\_ CENTROCUSTOAUTOINC” que irá definir se utiliza Auto incremento ou não para o campo “GCCUSTO.CODCCUSTO”. Caso o parâmetro **não** seja “De auto incremento”, a máscara do código do Centro de custo deve ser configurada de acordo com a máscara do centro/custo enviada pelo Protheus:

Ex: “QQQQQQQQ”. [permite qualquer caractere limitado a 8 posições].

Caso o parâmetro seja “De auto incremento”, o Código do Centro de Custo no RM será gerado a partir da tabela GAUTOINC, sempre ignorando o código informado na mensagem única. Nesse caso, o parâmetro “Máscara do Centro de Custo” deve ser preenchido como “QQQQQQQ” [qualquer caractere].

***Banco***

O Banco, Agência, Conta Corrente e Conta Caixa devem ser cadastrados no BackOffice Protheus e sincronizados para o RM.  
O BackOffice Protheus possui apenas uma tabela que contém todas as informações Código do Banco, Nome, Agência, Conta, entre outros.  
Agência é um anexo da visão de Banco, assim como Conta Corrente é um anexo da visão de Agência. Na Linha RM são tabelas independentes: Banco (GBANCO), Agência (GAGENCIA), Conta Corrente (FCONTA) e Conta Caixa (FCXA). Com isso, a exclusão da entidade banco no Protheus, reflete na exclusão de uma Conta caixa, conta, agencias e banco no Lado RM.  
As configurações iniciais desta integração criará um parâmetro chamado “RH\_ CONTACAIXAAUTOINC” que irá definir:  
Se desmarcado: O Código da “Conta / Caixa” no RM será sempre o número da conta bancária  enviada na mensagem;  
Se marcado: O Código da conta caixa no RM será um valor a partir da tabela GAUTOINC, sempre ignorando o número da conta bancária enviada na mensagem única.

***Plano de Contas***

Está disponível no Rm um campo chamado “NATSPED” conforme print abaixo. Esse campo informa para o sped a natureza da conta (se é uma conta de ativo, passivo,  patrimônio líquido, contas de resultado, contas de compensação). Esse campo não será transferido na mensagem pois o mesmo deve estar somente no BackOffice.

Porém, esse campo é obrigatório para inclusão da conta contábil no RM. Sendo assim,iremos gravar o valor de valor “01 – Não informado” somente para permitir a gravação. O mesmo não será utilizado pelo RM Labore.

A máscara parametrizada da conta contábil no RM é validada no processo de inclusão da conta contábil. Portanto, o parâmetro de máscara contábil deve ser cadastrado de acordo com o formato do código da conta a ser enviado pelo Protheus. Caso o Protheus não envie máscara no seu código de conta (ex: 1011214), então o parâmetro “*Não utiliza máscara nas contas*” deve ser marcado. Caso contrário, ocorrerá um erro no processo de inclusão da conta.

***Histórico Padrão***

No primeiro momento não será implementada no lado do Protheus a sincronização via mensageria das informações de histórico padrão.  
No lado RM,  a rotina já está preparada para recebê-la quando a mesma for implementada pela equipe Protheus.

***Período Contábil***

No processo de integração, o lado RM atualizará as datas de período contábil sempre de acordo com a menor data inicial e a maior data final enviada pelo Protheus. No Protheus, essas informações são armazenadas em um cadastro, e no RM essas informações são armazenadas nos parâmetros, sendo assim, teremos espaço para armazenar somente uma dataIncial e uma dataFinal.

***Processo de envio de mensagens***

***Lançamentos financeiros***

***Cadastros financeiros***

*Tipo de documento:* as informações de “tipo de documento” devem ser cadastradas na tela abaixo e mapeadas manualmente no cadastro de “De/para” de acordo com os tipos de documentos correspondentes do Protheus.

*Parâmetros:* Parametrização dos lançamentos financeiros

*• Pasta [identificação]*

**Tipo Documento:** Informação recuperada da tabela de “FTDO - tipos de documentos”.  
**Cód.Fornecedor:** Informação recuperada da tabela de “FCFO – cliente/fornecedor”. Dados dessa tabela devem ser enviados pelo Protheus.

**Tipo contábil**: esse campo ficará desabilitado pois a geração contábil do lançamento financeiro ficará sob responsabilidade do backOffice Protheus.  
**Global**: esse campo ficará desabilitado pois os dados da conta caixa são enviados por coligada;  
**Conta caixa:** Informação recuperada da tabela de “FCXA – conta caixa”. Dados dessa tabela devem ser enviados pelo Protheus.  
**Tabelas opcionais**: ficarão desabilitadas nesse tipo de integração visto que o Protheus não as utiliza.  
**Rateio do fluxo de caixa**: esse campo ficará desabilitado. Será criado um parâmetro de integração para preenchimento de um default de natureza financeira.

Obs: Esse default será enviado para o Protheus. No RM a natureza financeira é gravada no rateio de centro de custo, e no Protheus essa informação fica no próprio lançamento.

***Geração dos lançamentos financeiros***

**Usar Conta/caixa do cliente/Fornecedor:** Essa opção ficará desabilitada, pois a conta caixa não é enviada para o cliente/fornecedor na mensageria padrão.  
**Conta caixa Global:** Essa opção ficará desabilitada, pois a conta caixa é enviada por coligada.  
**Gerar lanctos bloqueados para alteração**:  Essa opção deve ser desabilitada, pois os lançamentos gerados para o Protheus não estarão bloqueados para alteração.  
**Gerar lanctos rateados por departamento:** essa opção ficará desabilitada, pois não haverá rateio por departamento.  
**Gerar lanctos rateados por centro de custo:** em caso de integração com backoffice de terceiro, essa opção sempre ficará habilitada

***Integração dos lançamentos financeiros***

Acesse RM / segmento RH / aba Encargos / Grupo Financeiro / Lançamentos / Lançamentos(RM Labore).

Serão listados dados de financeiro gerados pela folha. Até esse momento as informações ainda não foram enviadas para o BackOffice de terceiro (diferentemente da integração da folha  com o BackOffice da RM cujo dados são enviados automaticamente). Ao executar o processo de “Integração financeira com outros BackOffice”, as informações de financeiro geradas pela folha serão enviadas automaticamente para o BackOffice conforme configuração da mensagem única.

O status do processamento da mensagem poderá ser consultado no anexo “Informações de processamento”.

Ao executar o processo "Excluir Lançamento Financeiro Labore/BackOffice", será enviado uma mensagem única de delete para o BackOffice, se o retorno for positivo o lançamento também será excluído no RM.

***Lançamentos Contábeis***

***Cadastro Contábeis***

*Alteração de Máscara:* ficará desabilitada pois a alteração na máscara de conta será feita somente no backOffice.

*Cadastros gerenciais:* Todas as opções do menu “Cadastros gerenciais” serão desabilitadas, visto que, não faremos a integração gerencial com o BackOffice do Protheus.

*Período para manutenção de lançamentos:* Essa opção ficará desabilitada as datas dos períodos contábeis serão enviadas pelo Protheus;

*Solicitação de tarefa e tarefas:* ficará desabilitado para o usuário pois a manutenção de lotes será feita pelo Protheus.

*Lançamentos (RM Saldus):* ficará desabilitado pois os lançamentos contábeis gerados pela folha não serão integrados com o RM Saldus.

*Lançamentos (RM Labore):* ficará habilitado para visualização dos lançamentos contábeis gerados pelo processo de contabilização. Será incluído nessa visão um menu para disparar o “processo para exportação dos dados contábeis para os backoffice de terceiro”.

*Integrar lote contábil com o Saldus:* ficará desabilitada pois os lançamentos contábeis não serão exportados para o RM saldus.

***I****ntegração dos lançamentos contábeis***

Acesse RM / segmento RH / aba Encargos / Grupo Contabilização / Lançamentos / Lançamentos(RM Labore).

Serão listados dados de lançamentos contábeis gerados pela folha. Até esse momento as informações ainda não foram enviadas para o BackOffice de terceiro (da mesma forma que acontece atualmente com a integração com o BackOffice da RM). Ao executar o processo de “Integração contábil com outros Backoffices”, as informações de contabilidade geradas pela folha serão enviadas automaticamente para o BackOffice conforme configuração da mensagem única.

O status do processamento da mensagem poderá ser consultado no anexo “Informações de processamento”.

Ao executar o processo "Excluir Lançamento Contábil Labore/BackOffice", será enviado uma mensagem única de delete para o BackOffice, se o retorno for positivo o lançamento também será excluído no RM.

A informação do “Código do Lote” [BatchNumber] será utilizada como identificador do lote contábil enviado para o Protheus.

No Protheus o campo referente ao BatchNumber tem a limitação de 6 caracteres, sendo que no RM o campo é do tipo int32 no qual suporta valores até 2.147.483.647. Então hoje para o correto funcionamento da integração o código do lote do RM enviado pode conter no máximo 6 caracteres.

Para garantir a integridade dos dados no Protheus já que o processo de contabilização no RM Labore poderá ser executado diversas vezes, será enviada uma mensagem do RM Labore para o Protheus excluir todos os registros contábeis do lote (somente em caso de já existir um mapeamento para o lote em questão no lado RM), e somente após isso, ocorrerá o envio das mensagens de inclusão de lançamentos. Caso ocorra algum erro no envio de algum pacote contábil, o Rm enviará uma mensagem de exclusão do lote em questão.

 

**IMPORTANTE**: as mensagens contendo os dados da contabilização serão enviadas de forma **síncrona**, ou seja, será enviada uma mensagem por vez. A mensagem seguinte somente será enviada se a mensagem anterior estiver com status de sucesso no seu processamento. Sendo assim, o receptor da mensagem deverá também trabalhar com o conceito de mensagem síncrona. Ou seja, antes dele enviar à resposta (ResponseMessage) a mesma deve ser processada pelo receptor. Isso para evitar que a mensagem de exclusão seja processada depois de alguma inserção já realizada.

**Obs**: As mensagens contábeis enviadas serão divididas em pacotes devido a uma limitação no recebimento das mesmas. Será criado um parâmetro no RM Labore para o usuário informar a quantidade de partidas que deverão ser enviadas em cada pacote.

O processo de envio de pacotes acontecerá no seguinte esquema:

1)Será enviada uma mensagem de “exclusão de lote” (**somente em caso de já existir uma sincronização do RM com o Protheus do lote em questão**, **ou seja, se existir um mapeamento para o lote na tabla de De/para**). Essa mensagem possuirá somente informações do lote (cabeçalho). Nenhuma partida será enviada nessa mensagem. No campo “TotvsMessage/BusinessMessage/BusinessEvent/Event” será enviada a informação de “**delete**”.

O Protheus deverá receber essa mensagem e excluir o lote e as partidas contábeis gravadas. 

2)Serão enviadas mensagens contendo os dados dos pacotes contábeis. Essas mensagens possuirão informações do lote (cabeçalho) e das partidas contábeis. No campo “TotvsMessage/BusinessMessage/BusinessEvent/Event” será enviada a informação de “**upsert**”. Caso ocorra algum erro no envio de algum pacote, os pacotes restantes não serão mais enviados, e uma mensagem de exclusão de lote será enviada logo a seguir.

***Permissão de usuário***

***Lançamentos Financeiros***

Acesse RM / segmento Globais / aba Segurança / Perfis.

Na edição de perfil, aba “Acesso a Menus” localize na árvore de tags o recurso em questão:

[Folha de Pagamento / Encargos / Financeiro / Lançamentos / Integração financeira com outros BackOffice]. Através dessa permissão, o usuário do perfil terá condições de executar o processo de envio de dados financeiros para o BackOffice de terceiros.

***Lançamentos Contábeis***

Acesse RM / segmento Globais / aba Segurança / Perfis.

Na edição de perfil, aba “Acesso a Menus” localize na árvore de tags o recurso em questão:

[Folha de Pagamento / Encargos / Contabilização / Lançamentos / Lançamentos (RM Labore) / Integração contábil com outros BackOffice]. Através dessa permissão, o usuário do perfil terá condições de executar o processo de envio de dados contábeis para o BackOffice de terceiros.

**Baixa de “Título a Pagar” no Protheus que teve Origem na Folha RM, quando indevido.**

No Protheus Financeiro, criar um novo motivo de baixa que não impacte na “Movimentação Financeira” conforme imagem abaixo.

Local para criação do motivo.

*Financeiro / Miscelânea / Arquivos / Tabela de Motivos de Baixa*

Criar com o código alfa numérico, exemplo “RM“-  Descrição “Título Origem RM”

O usuário do financeiro deverá fazer a baixa do título apontando para este motivo.

O título não impactará na movimentação financeira da empresa.

Posteriormente, quando a implementação do “Cancelamento do título” pelo RM estiver liberada ao mercado, o usuário poderá excluir estes títulos.  
Basta cancelar a baixa com a sigla criada pelo usuário e com o título “Em aberto” poderá excluí-los pelo processo que será disponibilizado no RM.

**Como proceder no RM para que o Lançamento Financeiro cancelado não fique visível na visão.**

1 - Acessar a visão de lançamentos financeiros

2 - Clicar em filtro e criar um novo filtro com a descrição sugerida pelo usuário ou “Lançamentos financeiros Ativos”

3 -  Selecionar o campo ‘Id.Financeiro’ e do lado direito selecionar o operador NOT IN (Valores)  
Selecionar os lançamentos financeiros cancelados e clicar no botão ‘adicionar’.  
Sempre que cancelar um lançamento deverá adicionar o id financeiro neste filtro.

4 -  Sugestão:  Marcar à opção “Sempre usar este filtro ao abrir a visão’.

Desta forma, sempre que entrar na visão,  o filtro criado será selecionado não exibindo os lançamentos cancelados.

5 - Outra sugestão é colocar o filtro como Global, para que todos os usuários tenham acesso ao filtro.

Basta clicar com o botão direito sobre o filtro e marcar a opção “Filtro global”.

Desta forma, o filtro será habilitado como global para qualquer usuário ter o acesso.
