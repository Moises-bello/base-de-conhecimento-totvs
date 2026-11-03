---
content_hash: ebb15c30477cd1c694405f85ebcdc0ba33a8a049d80924fb5f0f4a096c9cb1dd
fetched_at: '2026-06-29T00:11:36.069941+00:00'
page_id: '772018466'
product: rm
source: tdn-rm
title: 1- Assinatura de diário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=772018466
version: 69
---

Nessa funcionalidade o professor poderá assinar os documentos do diário de classe referentes a uma determinada turma/disciplina.

Para acessar o processo de integração é necessário que **RM** esteja devidamente parametrizado. **Para saber mais acesse** [Integração com TOTVS Assinatura Eletrônica](https://tdn.totvs.com/x/yCOOIQ).

Para conhecer o **TOTVS Assinatura Eletrônica** [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=605018639).

### 1.0 - Configuração Integração com o TAE e configuração do documento a ser exibido no Novo portal do professor

A instituição de ensino deve configurar os documentos para integração com o TOTVS Assinatura Eletrônica. **Saiba mais em**

### 2.0 - Configuração e processo de Assinatura de Diário através do Novo portal do professor

A assinatura do diário de classe é realizada individualmente **para cada professor da turma/disciplina**. Assim, se uma turma/disciplina tiver mais de um professor a opção **"Responsável por iniciar o processo de assinatura do diário"** no cadastro de **Turmas do professor**, o sistema considerará um documento de diário de classe separado para cada professor, **de forma independente**. Portanto, um professor não visualiza o documento de outro professor, a menos que a instituição de ensino o tenha incluído manualmente como destinatário daquele documento.

Permissão de acesso

Para as turmas ou disciplinas pelas quais o professor for responsável pela assinatura do diário, o portal exibirá um item correspondente a essa funcionalidade.

Responsável por iniciar o processo de assinatura do diário

Para acessar a funcionalidade, o professor deverá ter marcada a opção **"Responsável por iniciar o processo de assinatura do diário"** no cadastro de **Turmas do professor**, em: *Educacional | Turmas/Disciplinas | Anexos | Professores*.

Período do professor na turma

* **Verificação de aptidão**

  + O Portal do Professor utiliza as datas de **início** e **término** cadastradas para o professor na turma para verificar se ele pode iniciar o processo de assinatura do diário.
* **Critério de aptidão**

  + O professor será considerado apto somente se a **data atual** estiver dentro do período cadastrado.
* **Ausência de data de término**

  + Caso a data de término não esteja preenchida, será considerada apenas a data atual como referência.

Parametrização por curso

Para acessar a funcionalidade, é necessário que a opção "**Documento do diário de classe**" esteja **informada** no cadastro de **Parametrização do curso**.

Turma/Disciplina gerencial sem matriz aplicada

O portal permitirá a assinatura do diário de classe para turma/disciplina gerencial **sem matriz aplicada**, desde que possuam um **documento único de assinatura do diário de classe** configurado nas parametrizações dos cursos das turmas/disciplinas associadas. Caso haja mais de um documento configurado, o sistema emitirá um alerta e impedirá o processo.

Documentos disponíveis

O portal disponibilizará a lista de documentos para o professor conforme a regra definida no item **"Criação/alteração do documento para assinatura"**. Para mais detalhes, consulte a tela de documentação **Documento**.

Assinatura do documento

Para iniciar o processo de assinatura eletrônica de um documento **ainda não integrado** ao TOTVS Assinatura Eletrônica, clique na opção **"Gerar"** no documento desejado, na tela de listagem de documentos.

  

Ao clicar, será exibida uma barra de progresso indicando a geração do documento.

Documento disponível para assinatura, permitindo que o professor visualize as informações diretamente na tela ou faça o download para uma melhor visualização.

Para iniciar a assinatura de um documento, clique na opção "Assinar". O portal solicitará a confirmação do início do processo de assinatura, exibindo a mensagem abaixo:

Início do processo de assinatura

Após confirmar, o professor deve acessar seu e-mail e utilizar o token e o link enviados para realizar a assinatura, conforme as instruções contidas na mensagem.  
Para saber mais, acesse **TOTVS Assinatura Eletrônica** em: *Funcionalidades | Fluxo do usuário | Assinando um documento | Eletronicamente (com autenticação por envio de código por e-mail)*.

Visualizar o documento

Para visualizar um documento já integrado ao TOTVS Assinatura Eletrônica, clique na opção **"Visualizar"** no documento desejado, na tela de listagem de documentos.

Documento rejeitado

Caso o documento tenha sido rejeitado por todos os destinatários, não será possível visualizá-lo.

Ao clicar, será exibida uma barra de progresso indicando o carregamento do documento.

Documento disponível para visualização.

Download do documento

Para realizar o download do documento, tanto dos que ainda **não estão integrados** quanto dos **já integrados** ao TOTVS Assinatura Eletrônica, o professor pode utilizar o botão "Download".

Ao clicar, será exibida uma barra de progresso indicando o download do documento.

Excluir o documento

Para excluir um documento já integrado ao TOTVS Assinatura Eletrônica, o professor deve ter permissão configurada em: *Serviços Globais | Segurança | Acesso | Perfil | Sistema: Educacional | Educacional (Portal) | Professor | Diário de classe | Assinatura eletrônica | Excluir documento*.

Não será possível excluir o documento assinado

Caso o documento tenha sido assinado por todos os destinatários, **não será possível excluí-lo**, devido às regras de integridade do OTVS Assinatura Eletrônica. Para mais informações, acesse TOTVS Assinatura Eletrônica em: *Funcionalidades | Fluxo do usuário | Gerenciando uma publicação existente | Excluindo um documento*.

Documento excluído

Ao excluir um documento já integrado ao TOTVS Assinatura Eletrônica, o sistema remove apenas o vínculo entre o documento do diário de classe no Educacional e o TOTVS Assinatura Eletrônica.

* A **exclusão** do documento no TOTVS Assinatura Eletrônica **não é possível**, devido a regras de integridade contidas nele. Desta forma o documento continua existindo no TOTVS Assinatura Eletrônica, porém sem vinculo com o Educacional**.**
* A **exclusão** do documento no Educacional é **realizada com sucesso**.

Reverter o vínculo

Após este processo **não será possível reverter este vinculo**.

Após esse processo, o professor poderá iniciar um novo processo de assinatura.

O professor tem duas opções para excluir um documento:

**1.**Para excluir um documento, clique na opção **"Excluir"** no documento desejado, na tela de listagem de documentos.

**2.** Para excluir um documento, basta clicar na opção "Visualizar" no documento desejado na tela de listagem dos documentos. E após este procedimento, o portal irá exibir o documento integrado e o botão de "Excluir".

Protocolo de assinaturas do documento

O documento integrado ao TOTVS Assinatura Eletrônica contém, ao final do arquivo, as considerações sobre o Protocolo de Assinaturas, que inclui os destinatários do documento e seus respectivos status de assinatura. Para saber mais, acesse TOTVS Assinatura Eletrônica em:  
*Funcionalidades | Fluxo do usuário | Download de um documento*.

### 3.0 - Monitor de documento - Visualizar a relação de documentos que foram integrados ao TOTVS Assinatura Eletrônica

A instituição de ensino pode visualizar e realizar ações nos documentos integrados ao TOTVS Assinatura Eletrônica. **Saiba mais em**
