---
content_hash: 518cb0f907b19cccfc017997c361953f2982507919f4cfd45cc417976cba62d2
fetched_at: '2026-06-29T00:05:59.694785+00:00'
page_id: '191468713'
product: rm
source: tdn-rm
title: ER_Reformulação_Banco_Talentos_Web
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=191468713
version: 68
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Pessoas | **Módulo** | RHU |
| **Segmento Executor** |  | | |
| **Projeto1** | PDR\_RH\_RHU004 / RHU – DESENVOLVIMENTO RHU – 12.1.2 | **IRM1** | PCREQ-1739 |
| **Requisito1** | PDR\_RH\_RHU004-140 / Requisito - Banco de Talentos | **Subtarefa1** | PDR\_RH\_RHU004-141 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.8 | **Réplica** |  |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** |  | | |

Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Reformulação do módulo “Banco de Talentos” disponível no produto TOTVS Gestão de Pessoas, visando a melhoria no design de interface, usabilidade e de suas funcionalidades disponíveis no portal, visando melhorar a experiência de uso  e seus recursos.

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| Rotina | Tipo de Operação | Opção de Menu | Regras de Negócio |
| Banco de Talentos | Alteração | Portal > Currículo | - |
| Candidatos da Etapa de Seleção | Alteração | TOTVS Gestão de Pessoas > Planejamento e Captação > Banco de Talentos > Painel de Etapas > Candidatos da Etapa | - |
| Painel de Opções | Alteração | TOTVS Gestão de Pessoas > Planejamento e Captação > Banco de Talentos > Painel de Opções | - |
| Vagas da Seleção | Alteração | TOTVS Gestão de Pessoas > Planejamento e Captação > Painel de Seleção > Vagas da Seleção | - |

### 1 Melhorias na interface

Será feito o redesenho da interface web do Banco de talentos visando facilitar a operação e interação com as funcionalidades disponíveis. Para isso, serão feitas as seguintes melhorias:          

- Criação de uma nova página inicial para usuários não autenticados, destacando as vagas disponíveis no momento. Nesta página também conterá um banner com fotos e textos dinâmicos com informações básicas (fixas) sobre o banco de talentos;

- Formulário de login passará a pertencer à página inicial, descrita no item anterior, e ficará localizado no cabeçalho da página;

- Substituição do menu principal de navegação (vertical) que contém todas as áreas para cadastro do currículo, acesso à vagas e seleções, por uma barra de navegação horizontal com um número reduzido e simplificado de menus;

- Reformulação da Home do sistema, para usuários autenticados, onde será disponibilizado um painel de vagas recentes, uma caixa com registros de notificações e outra com informações sobre o preenchimento dos dados do perfil do currículo;

- No cabeçalho de todas as páginas do sistema, para usuários autenticados, será exibido seu nome e foto enquanto  o mesmo estiver conectado ao sistema. Juntamente a esses dados, será disponibilizado um ícone contador de notificações que registrará a quantidade de notificações não lidas e proverá um link de acesso rápido a uma caixa flutuante que conterá o registro das últimas notificações;

- Criação de pop-up de “boas vindas”, ao se autenticar no sistema, que conterá links de acesso rápido a algumas funcionalidades disponíveis no sistema;

- Remodelagem da interface das telas de listagem e detalhamento de vagas, como também a mudança da tela de visualizar oportunidades (visualização de vagas para usuários não autenticados) por uma área de vagas em destaque na página inicial do sistema;

- A principal mudança será a visualização, edição e impressão do perfil de currículo que passará a ser representada em uma única página.

Todas as mudanças na interface podem ser visualizadas na seção "Protótipos" deste documento.

### 2 Novos Recursos

**2.1 Barra de menu do Usuário**

No cabeçalho da página será incluído o nome do usuário e foto, enquanto o mesmo estiver conectado e autenticado no sistema, conforme pode ser visto no protótipo 4.

#### **2.2 Inclusão de links de perfis da empresa proprietária do banco de talentos nas redes sociais (Rodapé)**

No rodapé da página serão incluídos ícones com links de acesso aos perfis da empresa mantenedora do banco de talentos, todos previamente cadastrados no sistema e carregados dinamicamente. Este cadastro, por sua vez, será criado no TOTVS Gestão de Pessoas (desktop), contendo os campos:

Nome da Rede Social: Campo do tipo texto que irá identificar o nome da rede social do perfil cadastrado;

URL do Perfil: Campo do tipo texto para informar a URL do perfil da empresa na rede social;

Ícone: Campo de entrada de arquivo para um arquivo de imagem (somente serão aceitos arquivos com extensão .png), que serão utilizados para exibição no rodapé no portal;

Ativo?: Campo do tipo "check" que indica se o ícone e link estão ativos e visíveis no portal.

*Por padrão, o sistema já exibirá um cadastro prévio de seguintes redes sociais: Facebook, Twitter, Google+ e LinkedIn, com informações básicas e genéricas.*

#### **2.3 Menu Principal (horizontal)**

O menu atual de navegação será substituído por uma barra de navegação horizontal simplificada, com a seguinte estrutura de itens:

- Home

- \*Perfil

- Painel de Vagas, com os sub-itens “Todas as Vagas”, \*“Vagas Salvas”, \*“Vagas que estou concorrendo”

- \*\*Cadastre seu perfil

- Documento anexos

- Questionários

*\* Este Item somente será exibido para usuários autenticados*

*\*\* Este Item somente será exibido para usuários não autenticado*

#### **2.4 Caixa de controle de preenchimento do Perfil de currículo**

Na página de Home, será criado uma caixa que disponibilizará informações sobre o preenchimento do perfil de currículo do usuário conectado. Nesta estrutura será informado o percentual de completude de preenchimento dos campos do perfil de currículo como também as seções do currículo que possuem dados obrigatórios ainda não preenchidos (protótipo 4).

Para calcular o percentual de completude de preenchimento, o sistema deverá realizar o cálculo baseado na quantidade de campos obrigatórios definidos no “\*Painel de Opções” do banco de talentos. Desta forma, efetuará o cálculo da seguinte forma:

                Variáveis:

                                PC = Percentual de completude

                                QTD\_CO = Quantidade de campos obrigatórios

                                QTD\_CP = Quantidade de campos obrigatórios preenchidos no banco de talentos

                Fórmula de cálculo:

**PC = QTD\_CP \* 100 / QTD\_CO**

*O resultado do cálculo sempre será apresentado arredondado e sem casas decimais.*

\*O Painel de Opções é um recurso existente no TOTVS Gestão de Pessoas, que permite configurar os campos e seções disponíveis no Banco de Talentos configurando a visibilidade e obrigatoriedade desses itens.

#### **2.5 Notificações**

Será criado um recurso para notificar os usuários sobre possíveis pendências em suas operações ou mensagens informativas. Desta forma busca-se centralizar as informações de mudanças ocorridas no banco de talentos.

As notificações serão de dois tipos:

- Alertas: destinado às notificações informativas ou de operações pendentes e opcionais no sistema.

Serão utilizadas para informar a abertura de novas vagas, pendências no preenchimento de questionários opcionais e/ou envio de documentos opcionais relacionados às vagas a que o usuário esteja concorrendo.

\*Este tipo será representado por um ícone circular na cor amarela.

- Pendências: destinado às notificações de operações obrigatórias e que estão pendentes no sistema.

Serão exibidas para informar pendências no preenchimento de questionários obrigatórios e/ou no envio de documentos obrigatórios relacionados às vagas a que o usuário esteja concorrendo.

\*Este tipo será representado por um ícone circular na cor vermelha.

As informações de notificações poderão ser visualizadas através de 3 estruturas: caixa de notificações, página de listagem de notificações ou caixa flutuante de notificações. Todas essas estruturas são novas e serão criadas no sistema.

A caixa de notificações será criada na página Home do sistema e terá a função de listar as 3 últimas notificações não lidas, conforme pode ser visualizado no protótipo 4.

A listagem completa de notificações, será criada uma nova página que deverá listar todas notificações não lidas (protótipo 11) e que poderá ser acessada através do link "ver notificações" localizado na caixa de notificações.

Por último, será criado um ícone no cabeçalho da página que exibirá contador de notificações não lidas e que ao clicar neste ícone, o sistema exibirá a caixa de notificações flutuante próximo ao item clicado, conforme pode ser visualizado no protótipo 10.

Todas as estruturas de exibição de notificações possuirão a mesma estrutura de item de informação. Cada item será representado por ícone para descrever o tipo de notificação (alerta ou pendência), seguido de um título e uma linha abaixo com descrição das informações.

#### **2.6 Aviso automático de vagas por e-mail**

Para avisar por e-mail os candidatos cadastrados no Banco de Talentos sobre a abertura de uma nova vaga, será realizada uma alteração na tela de cadastro de Vagas da Seleção, na versão desktop do TOTVS Gestão de Pessoas. No momento em que o usuário salvar uma nova vaga, o sistema exibirá uma caixa de diálogo questionando se deseja notificar os candidatos cadastrados no banco de talentos, caso a escolha seja afirmativa, o sistema enviará um e-mail customizado (processo em background) com as informações da nova vaga (exceto para vagas confidenciais). Somente receberão as notificações os usuários que indicaram em suas configurações para receber o aviso automático de vaga (por padrão é configurado como desativado). Para realizar essa configuração, será criada uma nova tela no portal e esta será acessada através do Portal > Menu Usuário > Configurar Aviso de Vagas (protótipo 12), onde será possível ativar ou desativar o recurso.

Para configurar o e-mail de comunicação, será criado um campo lookup com o nome "Aviso de Nova Vaga" no parametrizador do sistema (protótipo 18), para vincular um registro de \*E-mail Customizado (por padrão esse campo já será configurado com um e-mail padrão). Esse novo campo ficará disponível através do caminho: TOTVS Gestão de Pessoas > Configurações > Parametrizador > RM Portal > Mensagens Automáticas > \*Formatação de Mensagens.

*Será removido o campo  "usuário para agendamento de mensagens" e os campos Formatação de Mensagens estarão liberados para vinculação de e-mails customizados.*

#### **2.7 Painel de Vagas**

Conforme descrito no item Melhorias de Interface deste documento, as telas de listagem e detalhamento de vagas como também a exibição das vagas na página Home do sistema, sofrerão  alterações com o objetivo de melhoria em sua usabilidade.

Além das mudanças no design, será adicionado o recurso de salvar vagas como favoritas em todas as telas que exibição de vagas. Para salvar estas vagas, será adicionado um ícone de estrela nas telas com que exibem informações de vaga.

Juntamente a essa nova alteração, a tela de listagem de vagas receberá mais 3 tipos de filtros: Painel de Vagas (TODAS), Vagas Salvas e Vagas que estou concorrendo. Estes filtros também poderão ser acionados através de acesso ao menu principal do sistema (subitens do menu Painel de Vagas), que quando acionados já abrirão a tela de listagem com o filtro realizado.

As mudanças significativas nas estruturas e telas de  informações de vagas poderão ser visualizadas através dos protótipo 02, protótipo 06  e protótipo 07.

#### **2.8 Vínculo de tipos anexos ao perfil de vaga**

Com o objetivo de associar um perfil de vaga ao envio de documentos anexos (obrigatório ou opcionais), será criado um cadastro de tipo de anexos,  uma rotina para vincular o perfil da vaga com os tipos de documentos anexos e possibilitar enviar o arquivo tipo de anexo através do portal na vaga em que o usuário efetuou candidatura.

##### **2.8.1 Criação cadastro de tipos de documento anexo**

Criação do cadastro "Tipos documento de anexo" conforme o protótipo 19  e que será acessado através do caminho TOTVS Gestão de Pessoas > Planejamento e Captação > Seleção > Tabelas Auxiliares > Tipos de Documento Anexo. Este cadastro possuirá os seguintes campos:

- código: campo do tipo texto para informar o código do Tipo do documento;

- descrição: campo do tipo texto para informar a descrição do tipo de documento (ex: Atestado, portifólio e etc.);

- obrigatório: campo do tipo checkbox para informar se o envio do tipo de anexo é obrigatório, quando o mesmo estiver vinculado à candidatura de uma vaga.

Por padrão, no sistema já terão cadastros os tipos: Antecedentes Criminais, Geral, Portfólio, Atestado de Saúde Ocupacional e Documento de Identificação.

##### ****2.8**.2 Associar tipos de documento ao perfil de vaga**

Será alterado o cadastro de perfil de vaga, na versão desktop TOTVS Gestão de Pessoas, para inclusão de um campo lookup multirecords de "Tipos de Documento Anexo", com o objetivo de vincular os tipos de anexos ao perfil de vaga que será disponibilizado para candidatura no portal.

****2.8**.3 Envio de documento anexo vinculado à vaga**

No portal, ao usuário candidatar-se a uma vaga (tela de detalhe da vaga), será exibido um link "Enviar Anexo" onde ao acessar será exibido um pop-up com listagem dos tipos de anexos obrigatórios e opcionais associados à vaga em questão (ver protótipo 17).

Desta forma, o usuário poderá escolher o tipo de anexo que deseja associar, através do link "Anexar outro documento" (para escolher um arquivo em seu computador para envio) ou caso já tenha enviado o documento do mesmo tipo anteriormente em outro momento poderá clicar no link "Usar documento". Após realizar qualquer uma das operações, ao confirmar a operação através do botão "Enviar anexo "o sistema irá associar o documento ao perfil da vaga e salvará o anexo na mesma estrutura de anexo já existente.

Somente poderão ser enviados, um documento anexo para cada tipo cadastrado.

#### 2.9 Compartilhamento de dados da vaga em redes sociais e por e-mail

Nas telas de listagem e detalhes de vagas (protótipos 06 e 07) serão criados links que possibilitarão compartilhar as informações das vagas em redes sociais ou através de e-mails. Nos detalhes de cada vaga, haverão links que quando acionados carregarão os detalhes de cada vaga e sua URL para serem compartilhados nas redes Facebook, Google+, LinkedIn e Twitter ou através de e-mail informado pelo usuário no momento do compartilhamento.

Escolhida a rede social para compartilhamento, o sistema irá redirecionar para a página desta rede com todas as informações da vaga ficando a critério do provedor do serviço a confirmação de postagem do conteúdo.

Contudo, para compartilhar por e-mail, o sistema carregará um pop-up solicitando o(s) endereço(s) de e-mail de destino e um campo de mensagem para que o usuário possa complementar a mensagem a ser compartilhada (protótipo 16). Ao concluir a operação, o sistema criará uma mensagem padrão com os dados e URL da vaga e concatenará com a mensagem digitada pelo usuário e enviará o e-mail (usará como remetente o endereço de e-mail global do TOTVS Gestão de Pessoas) para os destinatários informados.

#### **2.10 Melhorias de acesso**

##### ****2.10**.1 Pop-up: Boas-vindas**

Ao se autenticar no sistema será disponibilizado um pop-up de boas-vindas que conterá 4 links de acesso rápido às seguintes funcionalidades do sistema: “Preenchimento do Currículo”, “Painel de Vagas”,”Central de Notificações” e “Configurador de aviso de vaga”, visando facilitar o acesso às principais funções do Banco de talentos.

##### ****2.10**.2 Importação LinkedIn no momento do cadastro**

Na página de cadastro de novos usuários, será criado um botão com descrição "Importação LinkedIn" (conforme protótipo 15), que permitirá aos usuários no momento de seu cadastro importar suas informações de "Formação Acadêmica", "Experiência Professional" e "Formação Adicional" e já salvá-las automaticamente em seu perfil de currículo ao término do cadastro. Ao realizar esse procedimento o sistema informará quais informações foram importadas do LinkedIn.

##### ****2.10**.3 Pop-up: Candidatura na vaga antes do cadastro ou acesso**

Na tela de detalhe das vagas será incluso a opção para usuários se candidatarem à vaga mesmo não estando autenticados no sistema. Ao selecionar o botão “candidatar”, o sistema exibirá um pop-up solicitando o logon (formulário de login) ou um novo cadastro (botão Cadastre-se), conforme protótipo 15.

Caso o usuário opte por efetuar o logon, o mesmo deverá informar os dados acesso e ao confirmar a operação o sistema executará sua candidatura na vaga e o redirecionará para a página com detalhes da vaga e com a confirmação da operação. Caso o contrário, ao acionar o botão “Cadastre-se” o mesmo será redirecionado para a página de cadastro de novos usuários, onde deverá informar todos os dados necessários e confirmar a operação. Ao realizar o procedimento sistema irá redirecioná-lo também para a página de detalhes da vaga confirmando a operação de candidatura na vaga.

#### ****2.11** Campo Possui Pendência? na visão de candidatos**

Na visão de Candidatos da Etapa da Seleção, na versão desktop do TOTVS Gestão de Pessoas, será adicionado uma novo campo para filtro chamado "Possui Pendência?", que indicará se o candidato possui pendência de preenchimento de questionários e/ou envio de anexos obrigatórios para o perfil da vaga de seleção em que  o mesmo é candidato.

#### ****2.12** Processo de envio de e-mail candidatos (e-mail customizado)**

Com o objetivo de aumentar a flexibilidade de comunicação entre a área de recrutamento e os candidatos de uma etapa de uma seleção, será alterado o processo "Envio de e-mail para Candidatos" permitindo informar um e-mail customizado como opção para envio de e-mail. Para isso, na segunda etapa do processo no momento de selecionar o campo "Opção de envio" será adicionado a opção "E-mail Customizado"(protótipo 20).

Caso seja selecionado a opção de envio de E-mail Customizado ao avançar a etapa do processo o sistema irá abrir uma nova etapa solicitando que o usuário informe em um campo lookup um registro de e-mail customizado. Este e-mail, por sua vez, possuirá disponível os seguintes parâmetros:

NOMECANDIDATO - Nome do candidato

PENDENCIAS - Lista de pendência na candidatura da vaga

NOMEVAGA - Nome da vaga

FUNCAO - Função vinculada à vaga

Uma vez selecionado o e-mail customizado ao avançar a etapa do processo, o sistema fará o envio de acordo com o funcionamento já existente da rotina de e-mail customizado, substituindo os valores dos parâmetros utilizados pelos dados o candidato e da vaga e seleção em questão.

## Protótipo de Tela

**Protótipo 01 - Página Inicial de usuários não autenticados**

****Protótipo 02**- Página Inicial de usuários não autenticados (com identificação das estruturas da página)******

******Protótipo 03**- Página Inicial de usuários autenticados********

******Protótipo 04**- Página Inicial de usuários autenticados (com identificação das estruturas da página)********

**********Protótipo 05**- Pop-up: Boas Vindas************

**************Protótipo 06**- Listagem de Vagas****************

******************Protótipo 07**- Detalhamento de vaga********************

**********************Protótipo 08**- Perfil de currículo************************

**************************Protótipo 09**- Edição de currículo****************************

******************************Protótipo 10**- Box de Notificações********************************

**********************************Protótipo 11**- **Listagem de Notificações**************************************

**************************************Protótipo 12**- Configuração de aviso de vaga****************************************

******************************************Protótipo 13**- **Enviar anexo**********************************************

**********************************************Protótipo 14**- Pop-up de acesso************************************************

************************************************Protótipo 15 - Tela de cadastro************************************************

************************************************************************************************Protótipo 16 - Compartilhamento de Vaga por E-mail************************************************************************************************

************************************************************************************************************************************************Protótipo 17 - Envio de documento anexo************************************************************************************************************************************************

************************************************************************************************************************************************Protótipo 18 - Campo Aviso de Nova Vaga (Parametrizador)************************************************************************************************************************************************

************************************************************************************************************************************************Protótipo 19 - Cadastro de Tipo de Documento Anexo************************************************************************************************************************************************

************************************************************************************************************************************************Protótipo 20 - Vínculo de perfil de vaga com tipo de documento anexo************************************************************************************************************************************************

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
