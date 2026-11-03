---
content_hash: 2c728a1418b1d8f607d61fc8431a49a36cda48407c23b41bc78eb489e87a06c0
fetched_at: '2026-06-29T00:11:36.715122+00:00'
page_id: '773500944'
product: rm
source: tdn-rm
title: Documento
type: documentation
url: https://tdn.totvs.com/display/LRM/Documento
version: 95
---

A integração entre o sistema Educacional e o TOTVS Assinatura Eletrônica possibilita o gerenciamento completo da assinatura digital de documentos que precisam ser validados por um ou mais destinatários. Por meio dessa integração, os documentos podem ser enviados automaticamente para assinatura, de acordo com critérios previamente configurados no sistema, tornando o processo mais ágil, seguro e rastreável.

Para acessar o processo de integração é necessário que **RM** esteja devidamente parametrizado. **Para saber mais acesse** [Integração com TOTVS Assinatura Eletrônica](https://tdn.totvs.com/x/yCOOIQ).

Para conhecer o **TOTVS Assinatura Eletrônica** [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=605018639).

Esta tela contempa **apenas os documentos** do tipo de documento **aluno ou** **diário de classe.**

Configurando o RM para a Integração com TOTVS Assinatura Eletrônica

É necessário realizar as parametrizações em: **Ambiente | Parâmetros Globais | Integração com o Totvs Assinatura Eletrônica.**

Usuário de acesso do Totvs Assinatura Eletrônica

O parâmetro de **usuário de acesso ao TOTVS Assinatura Eletrônica**, responsável pela publicação e administração dos documentos nessa plataforma, deve ser configurado em: **Configurações | Parâmetros | Integração | TOTVS Assinatura Eletrônica**.

Essa configuração é realizada **por contexto**, portanto, é necessário definir o usuário para **cada contexto** em que a integração será utilizada.

Perfil de acesso

Os usuários que irão integrar documentos com o TOTVS Assinatura Eletrônica devem ter seus perfis ajustados para permitir o acesso às telas responsáveis por essa integração.  
Para isso, acesse o cadastro de perfil e habilite as permissões relacionadas às opções de **Assinatura Eletrônica** no sistema Educacional.

Gerenciamento do documento

Por meio desta tela, o usuário deverá cadastrar os **tipos de relatórios** que serão integrados com o TOTVS Assinatura Eletrônica. O correto preenchimento dessas informações permitirá a geração do relatório, a definição dos destinatários e o posterior envio do documento para assinatura.

Configurações dos relatórios

O sistema suporta apenas relatórios gerados pelo RM Reports. **Para saber mais acesse** .

Tipo de documento

O sistema possui dois tipos de documentos, sendo:

Aluno

A seguir, algumas particularidades deste tipo de documento:

Tipo de relatório

Para que seja possível gerar o relatório pelo portal, é necessário configurar o tipo de relatório como: **“Relatórios de Alunos”**, **“Relatórios de Tesouraria”** e **“Relatórios de Secretaria”**.

Filtros enviados para o relatório

Cada relatório deve conter os **campos obrigatórios** para que a emissão seja realizada corretamente. Os filtros são preenchidos automaticamente pelo sistema.

**Parâmetros obrigatórios:**

* **Documento gerado pelo processo da tela “Aluno”**: `CODCOLIGADA`, `RA`
* **Documento gerado pelo processo da tela “Matrícula no Período Letivo”**: `CODCOLIGADA`, `RA`, `IDPERLET`, `IDHABILITACAOFILIAL`
Regras para geração do nome do arquivo

**Regras para geração do nome do arquivo PDF:**

As opções disponíveis para definição do nome do arquivo são:

1. **Nome do relatório + data da geração**
2. **Descrição do documento + data da geração**
3. **Descrição do documento + RA + data da geração**
Configurações de prazos

Caso o documento possua **prazo de assinatura** e não seja assinado até a **data limite de validação/assinatura**, ao executar o processo **“Atualizar os status dos documentos integrados”**, o status do documento será alterado para **“Fora do prazo de assinatura”**.

**Data limite para validação/assinatura do documento:** corresponde à data definida para que o documento seja assinado, após a qual ele não poderá mais ser validado ou assinado.

Documento fora do prazo de assinatura

Os documentos com status **“Fora do prazo de assinatura”** **não terão mais atualizações** relacionadas ao status das assinaturas dos destinatários.

Diário de classe

A seguir, algumas particularidades deste tipo de documento:

Tipo de relatório

Para que seja possível gerar o relatório pelo portal, é necessário configurar o tipo de relatório como **“Relatórios de Turmas”**.

Filtros enviados para o relatório

Cada relatório deve conter os **campos obrigatórios** para garantir a emissão correta. Os filtros são preenchidos automaticamente pelo portal.

**Quando o relatório utiliza a tabela master `STURMADISC` (Turma/Disciplina):**

* **Parâmetros obrigatórios:** `CODCOLIGADA`, `IDTURMADISC` (os filtros são preenchidos automaticamente pelo portal)
* **Parâmetros opcionais:** `CODETAPA` (preenchido automaticamente quando o tipo de relatório é **por cada etapa**)

Filtros do relatório

Caso deseje filtrar os dados por professor, é necessário incluir o parâmetro **`$CODUSUARIO`** na consulta SQL, que corresponde ao código do usuário logado. **Para saber mais acesse [Variáveis dinâmicas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003987132-Framework-Linha-RM-Frame-Vari%C3%A1veis-din%C3%A2micas-)**

Regras para geração do nome do arquivo

As opções disponíveis para definir o nome do arquivo são:

1. **Nome do relatório + data da assinatura do professor**
2. **Descrição do documento + data da assinatura do professor**
Data início para assinatura no portal do professor

Por meio desta informação, identificamos a **data de início** em que o documento ficará disponível no **Portal do Professor**.  
As opções disponíveis são:

Etapa consideradas

São consideradas para exibição:

* **Tipo das etapas:** “Faltas”
* **Opção marcada:** “Exibe no portal e na Central do Aluno”

Documento com o processo de assinatura já iniciado ou finalizado

O portal exibirá todos os documentos que já iniciaram o processo de **“Assinatura Eletrônica”**. Dessa forma, **não serão considerados o período de “Data de Início” nem a “Data Limite”** para assinatura do Diário de Classe no Portal do Professor.

Data final de cada etapa

Para cada etapa da turma/disciplina, o portal considerará a **“Data de Término”** cadastrada na tela de **“Etapa”** como a **data de início** para exibição e assinatura pelo professor no Portal do Professor.

Data final da última etapa (última etapa da turma/disciplina do período letivo)

Para a **última etapa**, o sistema considera a **maior “Data de Término”** cadastrada da turma/disciplina. Dessa forma, o portal utilizará essa data como a **data de início** para exibição e assinatura pelo professor no Portal do Professor.

Data limite de digitação de conteúdo efetivo de cada etapa

Para cada etapa da turma/disciplina, o portal considerará a **“Dt. Limite Conteúdo Efetivo”** cadastrada na tela de **“Etapa”** como a **data de início** para exibição e assinatura pelo professor no Portal do Professor.

Data limite de digitação da última etapa (última etapa da turma/disciplina do período letivo)

Para a última etapa (leva em consideração a última Etapa Cadastrada), o sistema considera a maior "**Data de término**" cadastrada da turma/disciplina. Desta forma, o portal irá considerar a "**Data de término**" cadastrada na tela de **"Etapa"**, como a **data início para ser exibido e poder ser assinado pelo professor no portal do professor.**

Observação

Caso existam várias etapas com a mesma data de término, o portal considerará a última etapa criada (pela data de criação).

Data personalizada a escolha da instituição

Para cada turma/disciplina, o portal exibirá um relatório quando a data informada no campo 'Data personalizada', na tela de 'Documento de assinatura eletrônica', for posterior à data atual.

Data limite para assinatura no portal do professor

Com base nessa informação, identificamos a data limite para que o documento fique disponível no portal do professor. As opções disponíveis são:

Data final do período letivo

O portal considerará a "**Data de término**", se preenchida; caso contrário, utilizará a "**Previsão de término**", cadastrada na tela de "**Período letivo**", como a data final para exibição e assinatura pelo professor no portal.

Sem limite. Até que todos os documentos sejam assinados

O portal **não definirá** uma data limite para o diário ser assinado pelo professor.

Data personalizada a escolha da instituição

O portal considerará a "Data personalizada", cadastrada na tela de "Documento de assinatura eletrônica", como a data final para exibição e assinatura pelo professor no portal.

Destinatário(s) do documento

Através dessa opção, é possível definir os destinatários do documento.

Campos obrigatórios dos destinatários

O preenchimento do nome e do e-mail dos destinatários é obrigatório.

Assinatura do documento através do código via e-mail

Todos os tipos de destinatários disponíveis nesta funcionalidade utilizam a assinatura do documento por meio do envio de um **código via e-mail**. Ou seja, para acessar e assinar o documento, o destinatário precisará clicar no link recebido por e-mail e, em seguida, receberá um código de validação em outro e-mail. Ao digitar o código na página, ele terá acesso ao documento e poderá assiná-lo. **P****ara saber mais acesse** [TOTVS Assinatura Eletrônica](https://tdn.totvs.com/x/fvccJ) na opção de **Funcionalidades | Fluxo do usuário | Publicando um documento | Adicionando destinatário**

Ordem de assinatura

Para definir a ordem das assinaturas, basta informar o número correspondente à posição do destinatário no fluxo de assinaturas. Dessa forma, o fluxo (envio de e-mails) só prossegue quando o destinatário atual realiza a assinatura. **Para saber mais acesse** [TOTVS Assinatura Eletrônica](https://tdn.totvs.com/x/fvccJ) na opção de **Funcionalidades | Fluxo do usuário | Publicando um documento |  Definindo ordenação das assinaturas (workflow)**

Não utilizar a ordenação para as assinaturas

Caso não queira utilizar a ordenação das assinaturas, basta definir todos os destinatários com a ordem igual a 0.

 Tipo de documento - Diário de classe

O professor responsável pela assinatura do diário será sempre o primeiro destinatário do fluxo, com ordem de assinatura igual a 0.

Tipo de destinatário

O tipo de destinatário define a finalidade de cada usuário no fluxo de assinatura.  **Para saber mais acesse** [TOTVS Assinatura Eletrônica](https://tdn.totvs.com/x/fvccJ) na opção de **Funcionalidades | Fluxo do usuário | Publicando um documento |  Adicionando destinatários**

* **Assinador:** usuários que assinarão digitalmente via certificado A1/A3 ou eletronicamente, utilizando seus dados de usuário (nome, CPF, geolocalização e IP da máquina).
* **Validador:** usuários que apenas validarão o documento; não participam da assinatura e servem apenas para confirmar se o documento está “OK”.
* **Testemunha:** usuários que assinarão eletronicamente como testemunha, utilizando seus dados de usuário (nome, CPF, geolocalização e IP da máquina).
* **Assinar com Certificado digital A1/A3:** usuários que assinarão obrigatoriamente via certificado digital A1/A3.
* **Observador:** usuário observador participa do documento de forma indireta, podendo apenas acompanhar seu fluxo, mas sem influenciá-lo. São listados na aba **Informações** do documento, logo abaixo dos participantes ativos.

O tipo de destinatário **Observador** atualmente exige usuário e senha para acessar o documento.

Tipo de documento - Aluno

As opções disponíveis de destinatários para este tipo de documento são:

Pessoa

Os registros a serem considerados são as pessoas vinculadas ao documento.

Aluno

O registro a ser considerado é o próprio aluno.

Pai

Os registros a serem considerados são as pessoas relacionadas na filiação com o tipo de relacionamento **"Pai" ou "P"**.

Mãe

Os registros a serem considerados são as pessoas relacionadas na filiação com o tipo de relacionamento **"Mãe" ou "M"**.

Responsável acadêmico

O registro a ser considerado é a pessoa relacionada como **"Responsável acadêmico".**

Responsável financeiro

O registro a ser considerado é o cliente/fornecedor relacionado como **"Responsável financeiro"**.

Tipo de documento - Diário de classe

As opções disponíveis de destinatários para este tipo de documento são:

Pessoa

Os registros a serem considerados são as pessoas vinculadas ao documento.

Coordenador da turma/disciplina

Os registros a serem considerados são as pessoas classificadas com a opção **"Coordenador"** no campo **"Tipo professor"**, cuja vinculação esteja dentro do período definido pelos campos **"Data de início"** e **"Data de término"** no cadastro de **"Turmas do professor"**.

Data de término não preenchido

Caso o campo **"Data de término"** **não esteja preenchido**, o sistema **não irá considerar** uma data final. Nessa situação, será considerado apenas o campo **"Data de início do mandato"** para os registros.

Coordenador da matriz aplicada

Os registros a serem considerados são as pessoas classificadas com a opção **"Coordenador"** no campo **"Função"**, e cuja data esteja dentro do período definido pelos campos **"Data de início do mandato"** e **"Data de término do mandato"** no cadastro de **"Comissão coordenadora"** da matriz aplicada.

Data de término do mandato não preenchido

Caso o campo **"Data de término do mandato"** **não esteja preenchido**, o sistema **não irá considerar** uma data final. Nessa situação, será considerado apenas o campo **"Data de início do mandato"** para os registros.

Secretário 1

Os registros a serem considerados são as pessoas classificadas no campo **"Secretário 1"**, cuja data, informada na aba do **"Diretor"**, esteja dentro do período definido pelos campos **"Data de início"** e **"Data Fim"** no cadastro de **"Diretor de filial"**. Esta tela está disponível em **Filial | Dados Educacionais | Instituição do MEC | 'Anexo' Diretores por instituição**.

Secretário 2

Os registros a serem considerados são as pessoas classificadas no campo **"Secretário 2"**, cuja data, informada na aba do **"Diretor"**, esteja dentro do período definido pelos campos **"Data de início"** e **"Data Fim"** no cadastro de **"Diretor de filial"**. Esta tela está disponível em **Filial | Dados Educacionais | Instituição do MEC | 'Anexo' Diretores por instituição**.

Professor responsável por iniciar o processo de assinatura do diário

Os professores responsáveis pela assinatura do diário de classe, ao iniciarem o processo de assinatura, serão automaticamente adicionados como destinatários do tipo **"Assinar"**, não sendo possível removê-los.

Destinatário a serem considerados 

As validações dos destinatários a serem considerados ocorrem no momento da iniciação do processo de assinatura do diário de classe pelo professor.
