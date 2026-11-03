---
content_hash: ef9d92c0fda093dc6c82a051ef57aed6e2082f7d0b5c17dad1365289958a2526
fetched_at: '2026-06-29T00:11:36.692826+00:00'
page_id: '773494654'
product: rm
source: tdn-rm
title: Monitor de documentos
type: documentation
url: https://tdn.totvs.com/display/LRM/Monitor+de+documentos
version: 45
---

As informações referente aos documentos integrados com TOTVS Assinatura Eletrônica.

Para acessar o processo de integração, é necessário que o **RM** esteja devidamente parametrizado. **Para saber mais acesse** [Integração com TOTVS Assinatura Eletrônica](https://tdn.totvs.com/x/yCOOIQ).

Para conhecer o **TOTVS Assinatura Eletrônica** [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=605018639).

Esta tela contempla apenas os documentos dos tipos **Aluno** ou **Diário de Classe** que foram integrados utilizando o cadastro de documento. **Para saber mais acesse**

Configurando o RM para a Integração com TOTVS Assinatura Eletrônica

É necessário realizar as parametrizações em: **Ambiente | Parâmetros Globais | Integração com o TOTVS Assinatura Eletrônica. Para saber mais acesse**

Usuário de acesso do Totvs Assinatura Eletrônica

O parâmetro de usuário de acesso do , responsável pela publicação e administração dos documentos no **TOTVS Assinatura Eletrônica**, deve ser configurado em: **Configurações | Parâmetros | Integração | TOTVS Assinatura Eletrônica**.

**Esta configuração é realizada por contexto, portanto, é necessário configurar cada contexto desejado.**

Perfil de acesso

Os usuários que poderão realizar a integração de documentos com o **TOTVS Assinatura Eletrônica** deverão ter seus perfis de acesso ajustados para permitir o acesso às telas responsáveis pela integração. Para isso, acesse o **cadastro de perfil** e conceda acesso às opções de **Assinatura Eletrônica** do sistema educacional.

Autenticação do usuário do TOTVS Assinatura Eletrônica no RM

Ao executar algum processo, será validado se o usuário já realizou a autenticação no portal do  por meio do **RM**. Caso ainda não tenha realizado, será exibida a tela para prosseguir com a autenticação e visualizar os documentos.

Usuário de acesso

Nesta tela, devem ser informados o **usuário** e a **senha de acesso** do .

Após a autenticação, o processo de integração com o será exibido.

* A autenticação será solicitada apenas uma vez durante a mesma sessão do **RM**. Ou seja, se o usuário fechar a aplicação e acessá-la novamente, a autenticação será solicitada outra vez.
* Para ambientes em **três camadas**, é possível agendar o **JOB** do processo de Integração  para execução posterior. Nesse cenário, é importante destacar que, quando o usuário realiza a autenticação, o **RM** armazena o **token** que será utilizado na execução do **JOB**. Esse token tem validade de **12 horas** a partir do momento da sua geração; portanto, o processo deve ser agendado para execução dentro desse período.

Caso o usuário do **RM** não possua acesso ao , deverá realizar o cadastro clicando em **“Cadastre-se aqui!”**.

Ao realizar o cadastro de um novo usuário, é importante selecionar uma empresa. Caso o cadastro do usuário no **TAE** seja efetuado sem a identificação da empresa, posteriormente, ao enviar um documento do **RM** para o **TAE**, poderá ser exibido o seguinte erro:

*Motivo: Erro ao consumir API. Código do erro: Forbidden*

Colunas

O sistema possui as seguintes colunas:

* **Descrição:** exibe a descrição do relatório no monitoramento.
* **Status:** exibe o status do documento ou relatório.
* **Job Relatório:** número do *job* de execução do relatório.
* **ID Arquivo Assinatura:** identificador do arquivo na API de assinatura.
* **Remetente:** usuário responsável pelo processo principal.
* **Mensagem:** mensagem de erro ou informação retornada pelo processo ou API.
* **Nome do Arquivo:** exibe o nome do arquivo gerado.
* **Campos-Chave:** campos que compõem a chave para a geração do relatório.
* **Valores-Chave:** valores que compõem o campo-chave.
* **Job Principal:** identificador do *job* responsável por disparar a geração dos relatórios, caso esteja relacionado a um processo principal.
* **Criado por:** usuário que criou o processo.
* **Criado em:** data de criação do processo.
* **Modificado por:** usuário que alterou o status do registro.
* **Modificado em:** data da modificação (alteração de status) do registro.

 Os registros de monitoramento poderão estar com um dos seguintes statusAtualização dos status ao abrir a tela

Caso o parâmetro **“Atualizar situação das assinaturas dos documentos ao carregar a visão”** esteja marcado, o sistema atualizará o status de todos os documentos que forem abertos na visão inicial. Para acessar, vá em **Ambiente | Parâmetros Globais | Integração com o TOTVS Assinatura Eletrônica**.

Visualizar ou editar um documento

Ao visualizar ou editar um registro, o usuário poderá ver as informações detalhadamente e acessar dados adicionais, como:

Destinatários

Serão exibidos os destinatários associados ao documento, a ação esperada do usuário e o status do usuário no documento.  
Será possível incluir ou excluir destinatários, desde que o usuário tenha permissão de acesso ao documento e este não esteja finalizado.  
Na tela de inclusão de destinatários, é possível realizar a seleção digitando o e-mail ou selecionando um cliente, fornecedor ou pessoa.

Assinatura do documento através do login com usuário e senha no TOTVS Assinatura Eletrônica

Todos os tipos de destinatários disponíveis nesta funcionalidade utilizam a assinatura do documento mediante login com usuário e senha no . Ou seja, para acessar o documento, o destinatário precisará se cadastrar no **TOTVS Assinatura Eletrônica** e, após realizar o login, poderá acessá-lo e assiná-lo. Para saber mais, acesse , na opção **Funcionalidades | Fluxo do Usuário | Publicando um Documento | Adicionando Destinatário**.

Prazo de assinatura 

Caso o documento possua um prazo de assinatura e não seja assinado até a data limite para validação, ao executar o processo **“Atualizar os status dos documentos integrados”**, o status do documento será alterado para **“Fora do prazo de assinatura”**.

**Data limite para validação/assinatura do documento**

Documento fora do prazo de assinatura

Os documentos com status **“Fora do prazo de assinatura”** não terão mais atualizações nos status das assinaturas dos destinatários.

Download do arquivo

Através desta opção, o usuário poderá acessar o arquivo PDF do documento já integrado ao  e realizar o download da sua última versão disponível no sistema de assinaturas. Caso o documento já possua alguma assinatura realizada, será exibido o **documento de manifesto**, contendo as informações das assinaturas.

Processos relacionados ao monitoramento

O sistema disponibiliza os seguintes **processos** relacionados aos documentos:

Atualizar os status dos documentos integrados

Ao ser executado, esse processo considerará apenas os documentos com status **"Pendente de assinatura"** ou **"Assinado parcialmente"** que tenham sofrido alguma alteração no TOTVS Assinatura Eletrônica, replicando essas informações no registro do **Monitoramento de Documentos** do RM.

Para os documentos com prazo de assinatura ou validação, o sistema verificará se o prazo foi expirado. Caso o prazo tenha expirado, o sistema cancelará o documento.

Assinar os documentos integrados

Esse processo permite que o usuário associado a um ou mais documentos realize a assinatura deles, sem a necessidade de acessar o portal **TOTVS Assinatura Eletrônica**. É importante que o usuário valide o documento antes de realizar a assinatura. O usuário deve se certificar de que o documento está correto e marcar a opção **“Ciente”** na tela.

Excluir os documentos integrados

Por meio desse processo, será possível excluir os documentos integrados que estejam pendentes ou finalizados com erro.

Não será possível excluir o documento assinado

Caso o documento já tenha sido assinado por todos os destinatários, **não será possível excluí-lo** devido às regras de integridade contidas no . Para saber mais, acesse **TOTVS Assinatura Eletrônica** na opção **Funcionalidades | Fluxo do usuário | Gerenciando uma publicação existente | Excluindo um documento**.

Exclusão do documento no TOTVS Assinatura Eletrônica não é possível

A exclusão do documento no **não é possível** devido às regras de integridade contidas no **TOTVS Assinatura Eletrônica**. Para saber mais, acesse **TOTVS Assinatura Eletrônica** na opção **Funcionalidades | Fluxo do usuário | Gerenciando uma publicação existente | Excluindo um documento**.

* A exclusão do documento no  não é possível devido às regras de integridade contidas nele. Dessa forma, o documento no **TOTVS Assinatura Eletrônica** terá seu status alterado para **“Cancelado”**.
* A exclusão do documento no **Educacional** é **realizada com sucesso**.
Reverter o vínculo

Após este processo **não será possível reverter este vinculo**.

Após esse processo, o professor pode iniciar um novo processo de assinatura.

Excluir os vínculos dos documentos integrados do diário de classe já assinados

Por meio desse processo, será possível excluir o vínculo entre o documento do **Diário de Classe** e o **TOTVS Assinatura Eletrônica** que já tenha sido assinado. Apenas os documentos do tipo **“Diário de Classe”** que estejam com o status **“Finalizado”** — ou seja, quando todos os destinatários já tiverem assinado — poderão ter o vínculo removido.

Exclusão do documento no TOTVS Assinatura Eletrônica não é possível

A exclusão do documento no não é possível devido às regras de integridade contidas no . Para saber mais, acesse **TOTVS Assinatura Eletrônica** na opção **Funcionalidades | Fluxo do usuário | Gerenciando uma publicação existente | Excluindo um documento**.

* A exclusão do documento no TOTVS Assinatura Eletrônica **não é possível**, devido a regras de integridade contidas nele. Desta forma o documento continua existindo no TOTVS Assinatura Eletrônica, porém sem vinculo com o Educacional**.**
* A exclusão do documento no **Educacional** é **realizada com sucesso**.
Reverter o vínculo.

Após este processo **não será possível reverter este vinculo**.

Após este processo, o professor pode iniciar novo processo de assinatura.

Enviar os documentos para assinatura

Esse processo permite o envio de documentos que não são integrados por meio do processo de integração de relatórios (**Processo de Integração**). O usuário pode selecionar um arquivo **PDF** do disco local ou de uma unidade de rede e enviá-lo para assinatura.  
As opções de aprovação e assinatura também estão disponíveis, assim como no processo de integração normal. Será possível incluir um destinatário associado ao cadastro de **Cliente/Fornecedor**, **Pessoa** ou, então, um **e-mail avulso**.

No grid de destinatários, é possível selecionar o tipo de participação do destinatário (**Assinar**, **Validar** ou **Testemunhar**) e, na coluna **“Prioridade de assinatura”**, utilizar o recurso de **workflow**, que funciona da seguinte maneira:

Ao utilizar o recurso de **workflow**, é possível definir uma ordem para as assinaturas, em que uma prioridade menor só poderá assinar após as prioridades maiores terem assinado.  
Exemplo:

[jose@integração.com](mailto:jose@integra%C3%A7%C3%A3o.com) - prioridade 0

[maria@integracao.com](mailto:maria@integracao.com) - prioridade 1

A Maria só conseguirá visualizar e assinar o documento depois que o José realizar sua assinatura. Caso o José rejeite o arquivo, ele não será exibido para a Maria.
