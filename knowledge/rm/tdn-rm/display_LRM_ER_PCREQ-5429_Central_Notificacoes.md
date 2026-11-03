---
content_hash: 90a94eac4291be8715e5d83006eb42db7cf472e762234a2df45f52b6c54e71fa
fetched_at: '2026-06-29T00:06:03.664613+00:00'
page_id: '200901835'
product: rm
source: tdn-rm
title: ER_PCREQ-5429_Central_Notificacoes
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-5429_Central_Notificacoes
version: 2
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Educacional, TOTVS Gestão Bibliotecária e TOTVS Avaliação e Pesquisa | **Módulo** | Educacional, Gestão Bibliotecária e Avaliação e Pesquisa |
| **Segmento Executor** | Educacional | | |
| **Projeto1** | [R\_EDU\_EDU011](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B11311%5D+%3D+R_EDU_EDU011 "R_EDU_EDU011") | **IRM1** | [PCREQ-5428](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-5428 "PCREQ-5428") |
| **Requisito1** | [PCREQ-5429](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-5429 "PCREQ-5429") | **Subtarefa1** | [PDR\_EDU\_EDU011-507](http://jira.totvs.com.br/browse/PDR_EDU_EDU011-507) |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.7 | **Réplica** |  |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 

O objetivo dessa melhoria é retirar das telas de parâmetros dos produtos TOTVS Educacional, TOTVS Gestão Bibliotecária e TOTVS Avaliação e Pesquisa, TODOS os campos onde são definidos textos para envio de e-mail, seja pelo sistema ou pelo portal, iniciando assim, um processo de centralização das mensagens de comunicação com os usuários do sistema e do portal, além de proporcionar uma melhoria na performance das aplicações, uma vez que os templates de e-mail, que normalmente são grandes, não serão mais carregados juntamente com a classe de parâmetros, muitas vezes desnecessariamente.

## Definição da Regra de Negócio

Todos os parâmetros do TOTVS Educacional, TOTVS Gestão Bibliotecária e TOTVS Avaliação e Pesquisa que atualmente são campos texto onde o usuário pode escrever um e-mail padrão para ser enviado por algum processo, parte do sistema ou portal educacional, deverá ser retirado da tela de parâmetros e incluído em uma nova estrutura que será detalhada a seguir. Todas as TAGs utilizadas para configuração desses modelos de textos também devem ser movidas para a nova tela de cadastro de mensagens de notificação.

 Para que essa mudança seja possível, deverá haver uma tela de cadastro de mensagens de notificação dentro de cada um dos produtos listados a seguir:

* TOTVS Educacional
* TOTVS Gestão Bibliotecária
* TOTVS Avaliação e Pesquisa

 No TOTVS Educacional deverá ser criado um novo item de menu com uma nova TAG de segurança. Esse item de menu deverá se chamar “Mensagens de notificação” e estar incluído dentro do menu “Auxiliares” do grupo de “Curriculo e Oferta”, subgrupo Acadêmico.

 No TOTVS Gestão Bibliotecária deverá ser criado um novo item de menu com uma nova TAG de segurança. Esse item de menu deverá se chamar “Mensagens de notificação” e estar incluído dentro do grupo de Cadastros, no novo subgrupo a ser criado chamado Auxiliares.

 No TOTVS Avaliação e Pesquisa deverá ser criado um novo item de menu com uma nova TAG de segurança. Esse item de menu deverá se chamar “Mensagens de notificação” e estar incluído dentro do grupo de Cadastros, subgrupo já existente Auxiliares.

 Os pontos do sistema onde atualmente são chamados os parâmetros com as mensagens de e-mail, deverão ser alterados para que em vez de buscar valores do parâmetro, busquem da nova estrutura detalhada nesse documento.

 Deverá ser criado na classe apropriada (EduEnumConsts, BibEnum ou TstEnum), um tipo eumerado onde o nome será composto pela sigla que identifica o sistema (“Edu”, “Bib” e “Tst”) mais a palavra “EduMensagemNotificacao".

 Por exemplo, para o TOTVS Gestão Educacional, deveremos criar na classe EduEnumConsts um tipo enumerado chamado “EduMensagemNotificacao”.

 Dentro de cada tipo enumerado criado, deverão ser incluídos todos os parâmetros retirados da tela de parâmetros de cada módulo do sistema, com o seguinte formato:

 SIGLASISTEMA + "\_" + GRUPOPARAMETRO + “\_” + ObjetivoParametro

Para alguns parâmetros, atualmente o cliente tem a opção de utilizar TAG’s para formatação do texto, como forma de elaborar um texto que contenha alguns valores padrão, como por exemplo “Nome do Aluno”, “Período Letivo”, etc. Deverá existir um método no lado servidor que receba como parâmetro o tipo enumerado e retorne para a aplicação a lista de TAG’s disponíveis para utilização. Caos não haja nenhuma TAG disponível, o botão para inclusão de TAG’s no texto não deverá ser exibido.

O texto informado como modelo do e-mail para ser enviado deverá SEMPRE ser gravado no banco de dados na tabela descrita a seguir, no formato HTML ou formato TEXTO, conforme definição do usuário no momento do cadastro.

A nova tela deverá ser construída como base na tela de “Envio de mala direta”, onde o usuário tem a possibilidade de enviar uma mensagem formatada, com imagens e outros elementos no corpo do texto.

**Inclusão de mensagens do TOTVS Gestão Educacional**

Para mensagens incluídas para o TOTVS Gestão Educacional, os valores de coligada, filial e nível de ensino serão considerados com base no contexto do usuário logado no sistema, desde que não haja ainda um cadastro para aquela mensagem.

**Inclusão de mensagens do TOTVS Gestão Bibliotecária**

Para mensagens incluídas para o TOTVS Gestão Bibliotecária, os valores de coligada, filial e unidade bibliotecária serão considerados com base no contexto do usuário logado no sistema, desde que não haja ainda um cadastro para aquela mensagem.

**Inclusão de mensagens do TOTVS Avaliaçao e Pesquisa**

Para mensagens incluías para o TOTVS Avaliação e Pesquisa, os valores de coligada serão considerados com base no contexto do usuário logado no sistema, desde que não haja ainda um cadastro para aquela mensagem.

 A inclusão de uma nova mensagem será permitida para os casos em que o conjunto de valores que compõem o contexto do produto em conjunto com o tipo enumerado que define a utilização da mensagem ainda não estejam gravados no banco de dados.

Por exemplo:

Para o TOTVS Gestão Educacional iremos gravar uma mensagem correspondente ao tipo enumerado “Estágio: mensagem de e-mail para candidatos sempre que houver alteração na vaga” para a coligada 1, filial 1 e nível de ensino “Ensino Superior”. Essa mensagem somente poderá ser gravada, caso ainda NÃO haja na base de dados, na tabela SMENSAGENSNOTIFICACAO um registro cujos campos CODCOLIGADA, CODFILIAL, CODTIPOCURSO e IDENUMERADO sejam correspondentes aos valores citados anteriormente.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Parâmetros Secretaria Lista de Espera Reserva Recurso / Instalação | [Alteração] | Educacional | Parâmetros | Secretaria | Geral 3/5 | - |
| Parâmetros Estágio Envio E-mail Candidatos Alteração Vagas | [Alteração] | Educacional | Parâmetros | Estágio | Estágio 1/6 | - |
| Parâmetros Estágio Envio E-mail Aluno Selecionado Vaga | [Alteração] | Educacional | Parâmetros | Estágio | Estágio 3/6 | - |
| Parâmetros Estágio Envio E-mail Aluno Não Selecinado Vaga | [Alteração] | Educacional | Parâmetros | Estágio | Estágio 3/6 |  |
| Parâmetros Estágio Envio E-mail Aprovação Reprovação Plano Atividades | [Alteração] | Educacional | Parâmetros | Estágio | Estágio 4/6 |  |
| Parâmetros Envio de E-mails Processos Biblioteca | [Alteração] | Gestão Bibliotecária | Parâmetros / Configurações | Parâmetros do Sistema | Envio de E-mails | Pasta Reservas Confirmadas |  |
| Parâmetros Envio de E-mails Processos Biblioteca | [Alteração] | Gestão Bibliotecária | Parâmetros / Configurações | Parâmetros do Sistema | Envio de E-mails | Pasta Usuários Empréstimo Atraso |  |
| Parâmetros Envio de E-mails Processos Biblioteca | [Alteração] | Gestão Bibliotecária | Parâmetros / Configurações | Parâmetros do Sistema | Envio de E-mails | Pasta Usuários Devolução Prevista |  |
| Parâmetros Envio de E-mails Processos Biblioteca | [Alteração] | Gestão Bibliotecária | Parâmetros / Configurações | Parâmetros do Sistema | Envio de E-mails | Pasta Texto Livre |  |
| Parâmetros Envio de E-mails Processos Biblioteca | [Alteração] | Gestão Bibliotecária | Parâmetros / Configurações | Parâmetros do Sistema | Envio de E-mails | Pasta Usuários Reserva Vencida |  |
| Parâmetros Envio de E-mails Processos Biblioteca | [Alteração] | Gestão Bibliotecária | Parâmetros / Configurações | Parâmetros do Sistema | Envio de E-mails | Pasta Usuários Sugestão Compra Adquirida |  |
| Parâmetros Envio de E-mails Processos Biblioteca | [Alteração] | Gestão Bibliotecária | Parâmetros / Configurações | Parâmetros do Sistema | Envio de E-mails | Pasta Usuários Área Interesse |  |
| Parâmetros E-mail de Inscrição | [Alteração] | Avaliação e Pesquisa | Parâmetros | Parâmetros do Sistema | Envio de Emails | E-mails Inscrição |  |
| Parâmetros E-mail de Resultado | [Alteração] | Avaliação e Pesquisa | Parâmetros | Parâmetros do Sistema | Envio de Emails | E-mails Resultado |  |

***Tabelas Utilizadas***

* *SMENSAGENSNOTIFICACAO - Cadastro de mensagens para envio por e-mail*

### Dicionário de Dados

**Arquivo ou Código do Script:** */\*MARIO ALEXANDRE DE CASTRO - CN.2015.07\_10 - OC.:PVR\_R\_V12-116 - 31/07/2015 VERSAO.: 12.1.7 - EQUIPE:INOV \*/*

 

|  |  |
| --- | --- |
| **Campo** | CODCOLIGADA |
| **Tipo** | DCODCOLIGADA – NOT NULL |
| **Tamanho** | 2 |
| **Descrição** | Código da coligada para a qual a mensagem cadastrada estará disponível |
| **Título** | Código da Coligada |
| **Help de Campo** | Código da coligada para a qual a mensagem cadastrada estará disponível |
| **Campo** | CODSISTEMA |
| **Tipo** | VARCHAR – NOT NULL |
| **Tamanho** | 1 |
| **Descrição** | Código do sistema para o qual a mensagem estará disponível |
| **Título** | Código do sistema |
| **Help de Campo** | Código do sistema para o qual a mensagem estará disponível |
| **Campo** | IDMENSAGEMNOTIFICACAO |
| **Tipo** | AUTOINC – NOT NULL |
| **Tamanho** | 4 |
| **Descrição** | Identificador da mensagem de notificação cadastrada |
| **Título** | Id. mensagem |
| **Help de Campo** | Identificador da mensagem de notificação cadastrada |
| **Campo** | CODFILIAL |
| **Tipo** | SMALLINT - NULL |
| **Tamanho** | 2 |
| **Descrição** | Código da filial para a qual a mensagem cadastrada estará disponível |
| **Título** | Código da Filial |
| **Help de Campo** | Código da filial para a qual a mensagem cadastrada estará disponível |
| **Campo** | CODTIPOCURSO |
| **Tipo** | SMALLINT - NULL |
| **Tamanho** | 2 |
| **Descrição** | Código do nível de ensino para a qual a mensagem cadastrada estará disponível |
| **Título** | Nível de Ensino |
| **Help de Campo** | Código do nível de ensino para a qual a mensagem cadastrada estará disponível |
| **Campo** | CODUNIDADE |
| **Tipo** | INT - NULL |
| **Tamanho** | 4 |
| **Descrição** | Código da unidade bibliotecária para a qual a mensagem cadastrada estará disponível |
| **Título** | Unidade Bibliotecária |
| **Help de Campo** | Código da unidade bibliotecária para a qual a mensagem cadastrada estará disponível |
| **Campo** | TEXTOMENSAGEM |
| **Tipo** | MEMO – NOT NULL |
| **Tamanho** |  |
| **Descrição** | Texto da mensagem que será exibida para o usuário, eviado por –email, etc. |
| **Título** | Texto da Mensagem |
| **Help de Campo** | Texto da mensagem que será exibida para o usuário, eviado por –email, etc. |
| **Campo** | IDENUMERADO |
| **Tipo** | VARCHAR - NOT NULL |
| **Tamanho** | 10 |
| **Descrição** | Identificador do tipo enumerado que define qual a utilidade da mensagem cadastrada |
| **Título** | Identificador do Tipo Enumerado |
| **Help de Campo** | Identificador do tipo enumerado que define qual a utilidade da mensagem cadastrada |
| **Campo** | TIPOMENSAGEM |
| **Tipo** | VARCHAR – NOT NULL |
| **Tamanho** | 20 |
| **Descrição** | Tipo da mensagem que está sendo gravida no banco. H para mensagens gravadas em formato HTML ou T para mensagens gravadas no formato Texto. |
| **Título** | Tipo da Mensagem (Html ou Texto) |
| **Help de Campo** | Tipo da mensagem que está sendo gravida no banco. H para mensagens gravadas em formato HTML ou T para mensagens gravadas no formato Texto. |
| **Campo** | ASSUNTOEMAIL |
| **Tipo** | VARCHAR - NULL |
| **Tamanho** | 150 |
| **Descrição** | Assunto do e-mail que está sendo cadastrado. |
| **Título** | Assunto |
| **Help de Campo** | Assunto do e-mail que está sendo cadastrado. |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
