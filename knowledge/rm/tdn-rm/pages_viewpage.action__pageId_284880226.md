---
content_hash: afe57dbde17eb8411cc3ddff09b371874121cd48216b69a5668cc5800a2844b0
fetched_at: '2026-06-29T00:08:37.613245+00:00'
page_id: '284880226'
product: rm
source: tdn-rm
title: Requerimentos disponíveis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284880226
version: 38
---

Nessa página, o aluno ou responsável visualiza as solicitações disponíveis e pode **requerer novos serviços** de acordo com o grupo ou tipo de atendimento desejado.

Para acessar o processo de integração entre o TOTVS Educacional e o TOTVS Aprovações e Atendimento. **Para saber mais acesse** [Integração TOTVS Educacional x TOTVS Aprovações e Atendimento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037558413-RM-EDU-Como-realizar-a-integra%C3%A7%C3%A3o-Totvs-Educacional-x-Totvs-Gest%C3%A3o-de-Relacionamento-com-o-Cliente).

Permissão de acesso

Para acessar a funcionalidade, o perfil do usuário deverá ter a permissão em: **Serviços Globais | Segurança | Acesso | Perfil | Sistema: Educacional | Educacional (Portal) | Acadêmico | Solicitações**

Vínculo do usuário ao perfil de TOTVS Aprovação e Atendimento 

Para acessar a funcionalidade, o usuário deve estar vinculado a pelo menos um perfil do **TOTVS Aprovações e Atendimento**.

Grupos/tipos de atendimento disponíveis

O portal **lista** todos os tipos de atendimento parametrizados para o período letivo de matrícula do aluno.

Período do tipo de atendimento

Embora os campos de prazo (inicial e final) não sejam obrigatórios, os requerimentos só serão exibidos no portal se houver um **período válido** configurado.

Abrir uma nova solicitação

O aluno dispõe de duas formas para iniciar a solicitação: acessando o link **'Ver detalhes'** ou clicando diretamente no botão **'Solicitar'**.

Clicar no Link do Tipo de Atendimento

Após o clique, o usuário é direcionado à tela de detalhes. Nela, deve-se conferir as informações do atendimento e preencher os campos obrigatórios para concluir a solicitação.

Anexo da solicitação

O sistema permite o anexo de **apenas um arquivo** por solicitação.

Parametrização de armazenamento

Para o correto funcionamento, é necessário configurar o armazenamento de arquivos em: **TOTVS Aprovações e Atendimento |** **Configurações | Parâmetros | Arquivos anexos ao atendimento. Saiba mais em**

Upload de arquivos grandes

Caso a instituição permita uploads no portal com tamanho superior ao tamanho padrão **30mb** do **IIS(Internet Information Services)**será necessário realizar algumas configurações adicionais. Saiba mais em

Incluir anexo

Para anexar arquivos, o usuário deve possuir a permissão necessária e selecionar a opção **'Adicionar arquivos'**.

Permissão

A opção 'Adicionar arquivos' só estará disponível mediante a permissão no **TOTVS Aprovações e Atendimento**, localizada em: **TOTVS Aprovações e Atendimento | Meus Atendimentos | Atendimentos | Atendimentos | Arquivos anexos do atendimento**

Parâmetros da solicitação por tipo de atendimento

O portal lista todos os parâmetros vinculados ao tipo de atendimento da solicitação selecionada, conforme configurado no **TOTVS Aprovações e Atendimento. Para saber mais acesse**

Ordem de exibição dos parâmetros

O portal irá listar os parâmetros do tipo de atendimento da solicitação **ordenado crescentemente** pelo "**Código do parâmetro**" no cadastro do parâmetro no **TOTVS Aprovações e Atendimento.**

Parâmetro obrigatório

O portal exigirá o preenchimento do parâmetro caso a opção **'Parâmetro exigido'** esteja marcada no vínculo do parâmetro do tipo de atendimento no **TOTVS Aprovações e Atendimento.**

Parâmetro(s) invisíve(is)

A visibilidade dos parâmetros no portal é configurada diretamente no cadastro da etapa do tipo de atendimento, dentro do **TOTVS Aprovações e Atendimento**. **Saiba mais em [Etapas](https://tdn.totvs.com/display/public/LRM/Etapas)**

Tipo do parâmetro igual a tabela

O parâmetro do tipo **'Tabela'** **não é suportado no portal**, sendo uma funcionalidade exclusiva do sistema **RM (ambiente MDI/Desktop)**.

Parâmetro com sentença SQL

Para utilizar este recurso, é necessário informar o campo **'Cód. da sentença'** vinculado à consulta SQL que será executada para exibir os campos.

Parâmetro com a opção “Cód. da sentença” preenchido

Caso o **'Cód. da sentença'** esteja preenchido, o sistema ignora o **'Tipo do parâmetro'** e define o campo automaticamente como **String**, exibindo uma lista de valores baseada no retorno da consulta SQL.

A descrição e valor das opções do parâmetro

O portal exibirá a **primeira coluna** do retorno da consulta SQL como a **descrição** do parâmetro, enquanto a **segunda coluna** será utilizada como o **código** (valor).

Parâmetro com dependência de outro parâmetro

O portal permite a **dependência entre parâmetros**. Ao selecionar um item no **parâmetro pai**, o **parâmetro filho** utiliza automaticamente esse valor para filtrar os dados via consulta SQL.

Para habilitar essa relação, a consulta SQL do parâmetro filho deve conter a variável `:PARAMETRO_XX`, onde **XX** corresponde ao código do parâmetro pai.

Exemplo

**Parâmetro Pai**

**Parâmetro Filho, que é dependente do parâmetro pai, onde o "código do parâmetro" igual a 13**

Parâmetros duplicados ou repetidos no portal

Caso ocorra uma situação em que o portal exiba parâmetros duplicados ou repetidos, isso indica que há uma configuração incorreta no cadastro da "**Etapa**" do tipo de atendimento no **TOTVS Aprovações e Atendimento**

Para o correto funcionamento do portal é necessário possuir **apenas** uma "Etapa" do tipo de atendimento no **TOTVS Aprovações e Atendimento** com a opção **"Primeira etapa de um possível fluxo" marcada**

Salvar a solicitação

Para incluir uma nova solicitação no **TOTVS Aprovações e Atendimento**, o sistema irá considerar algumas informações na criação:

Atendente responsável pela abertura

O atendente responsável pela abertura é parametrizado em **Educacional |** **Configurações | Parâmetros | Integração | Atendimento | Atendimento - Geral 2/3**

Gerar lançamento da solicitação

Para a geração do lançamento da solicitação, é necessário realizar as seguintes configurações:

* O aluno deve possuir um **responsável financeiro** cadastrado;
* O aluno deve possuir um **contrato ativo** no período letivo correspondente à solicitação.

* O tipo de requerimento configurado no **TOTVS Educacional** deve ter o campo **'Serviço'** preenchido e a opção **'Inserir serviço extra e gerar lançamento ao abrir o atendimento'** marcada.

 

* A parcela vinculada à solicitação deve pertencer ao **período letivo** vigente e possuir uma **data de vencimento** superior à data atual. O número informado no campo **'Parcela'** determinará qual parcela será gerada no contrato identificado. Essas definições são realizadas em: **Educacional | Configurações | Parâmetros | Integração | Atendimento | Atendimento - Geral 3/3**.

Caso a solicitação preveja a cobrança de um valor extra, ao clicar em **'Solicitar'**, o portal processará a informação e exibirá uma mensagem confirmando a geração do boleto. Em seguida, o usuário poderá ser redirecionado ao menu **Extrato Financeiro** do Portal do Aluno. Saiba mais acessando
