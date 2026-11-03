---
content_hash: ddfdfb77236f284586e97f6ab9ea41f8b126a3fa63a2eca6aa35105f8588460e
fetched_at: '2026-06-29T00:08:17.939804+00:00'
page_id: '259561095'
product: rm
source: tdn-rm
title: DT_Melhorias_Planejamento_Captacao
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Melhorias_Planejamento_Captacao
version: 7
---

# DT\_Melhorias\_Planejamento\_Captacao

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM | | |
| ****Segmento Executor:**** | Construção e Projetos. | | |
| **Módulo:** | *Gestão de Pessoas* | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Informe a rotina.* | *Informe o nome técnico da rotina.* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Informe a(s) rotina(s) envolvidas*.* | *Informe o nome técnico da(s) rotina(s) envolvidas.* | |  |  | | | |
| **Chamado:** | *Informe o(s) chamado(s) relacionado(s)* | | |
| **Requisito (ISSUE):** | *Informe o requisito relacionado (Issue).* | | |
| **País:** | (  ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros:** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos>.* | | |

## Objetivo

 O objetivo deste projeto é a implementação de melhorias para o módulo de Planejamento e Capacitação.

## Inovações Feitas

## 1    Triagem

### 1.1  Filtros Pesquisa Triagem

Foi alterado para que a pesquisa de Triagem tenha as mesmas opções de filtros do Cadastro de Candidatos.

As mudanças feitas no Cadastro de Candidatos são refletidas automaticamente na Pesquisa de Triagem.

### 1.2   Triagem Por Palavras Chave

Foram criadas parametrizações da triagem para palavras chave.

Primeiramente você deve ter Palavras Chave cadastradas. Para isso vá em TOTVS Gestão de Pessoa | Planejamento e Capacitação | Triagem | Clique em novo ou altere algum já existente

No cadastro, pode-se inserir quantos Sinônimos forem necessários, sendo eles separados por ; (ponto e virgula)

Após cadastrar as palavras chaves, você poderá escolher o modo que o sistema irá filtrar, sendo eles;

* **Selecionar somente candidatos que possuam todas as palavras chave da triagem.**

* **Selecionar somente candidatos que possuam pelo menos uma das palavras chave da triagem.**

* **Não utilizar palavras chave da triagem.**

Todas as informações inseridas refletirão na Pesquisa da Triagem.

### 1.3    Triagem por Andamento do Curso

Passa a ser possível selecionar mais de uma opção para o "Andamento do Curso" dentro de uma triagem.

A "Pesquisa da Triagem" respeita essa nova opção.

### 1.4    Triagem por Nível de Grau de Formação e de Formação Acadêmica

Para ter mais flexibilidade na busca, é possível triar por Nível de Grau de Formação e de Formação Acadêmica.

Para isso vá em TOTVS Gestão de Pessoa | Planejamento e Capacitação | Triagem | Clique em novo ou altere algum já existente

* **Em Triagem de Dados Pessoais**

* **Em Cursos Acadêmicos**

### 1.5   Submeter Candidato a uma Triagem

É possível aplicar um processo de Triagem a um ou mais candidatos do cadastro, escolhendo uma triagem é exibido um log com os critérios aplicados na triagem e se o candidato possui ou não os requisitos impostos.

Para isso, acesse : ...Vagas | Anexos | Candidatos Pelo Portal | Processos..

Também pode-se aplicar o processo a partir da visão de candidatos inscritos numa vaga pelo portal. Nesse caso a triagem da vaga deve ser escolhida como padrão no assistente.

## 2    Banco de Talentos

### 2.1   Para o Analista de RH

* Foi disponibilizado um anexo às Vagas de Seleção onde é possível visualizar as pessoas que se candidataram pelo Banco de Talentos.
* Passa a ser possível enviar e-mail aos candidatos.
* Pode-se também realizar a Triagem dos candidatos.
* Ao executar a Triagem, é atualizado o status dos candidatos aprovados e não aprovados na Triagem.

### 2.2   Para as Pessoas que se Candidataram Pelo Banco de Talentos

Na tela das pessoas que se candidataram pelo Banco de Talentos passa a exibir um status, de como anda o seu processo. São eles:

* **"Aguardando triagem"** - Que refere-se ao status inicial.
* **"Aprovado na triagem"** - quando iniciar o processo e o candidato for triado
* **"Reprovado na triagem"** - quando iniciar o processo e o candidato não for triado
* **"Não computado"** - para candidaturas anteriores a nova funcionalidade

### 2.3   Quando Candidato Interno

Quando um interno se cadastrar a uma vaga pelo Banco de Talentos, pode ser aberta uma requisição de Liberação ou não pelo seu líder. A continuidade do processo dependerá da aprovação da requisição.

O funcionário poderá acompanhar o andamento pela própria tela da vaga do Banco de Talentos.

### 2.4   Detalhamento da Experiência Profissional

Para deixar o cadastro mais completo, é possível descrever as atividades desempenhadas pelo candidato em experiências profissionais. Em Banco de Talentos | Perfil | Exp. Profissional | Adicionar Detalhes.

Foi adicionado o campo texto para inserir a "Descrição das Atividades"

É possivel triar por esse novo campo utilizando os recursos de Palavras Chave (Módulo 1.2 Desse Documento)

## 3    E-mail

### 3.1    Novo Campo E-mail

Para o usuário do Banco de Talentos possa ter acesso mesmo que ele saia da empresa, foi criado um novo campo para cadastrar E-mail Pessoal no Cadastro de Candidato dentro da aba Perfil Profissional;

O sistema consegue distinguir a situação do candidato para saber em qual e-mail deve ser enviado, em caso de demissões, é enviado para o E-mail Pessoal, caso ele esteja preenchido.

Ele também permite que recupera a senha, em caso de perda da mesma.

### 3.2    E-mail de Boas Vindas

Passa a ter um novo tipo para customizar o E-mail de Boas Vindas.

## 4    Perfil Profissional

### 4.1  Pontuação

Para poder fazer uma melhor classificação de candidatos por vaga, passa a ser possível configurar pontos para cada item dentro do cadastro de Perfil de Vagas | Perfil Profissional

Na visão de Candidatos da Etapa, o usuário poderá verificar qual candidato obteve maior pontuação através do Perfil Profissional, determinando assim, qual candidato melhor se adapta a vaga.

## 5    Exibição para o Candidato no Portal

### 5.1  Status

Passa a ser possível definir se um candidato que se inscreveu pelo portal poderá ver detalhe do andamento da vaga. Deverá ser marcado a opção dentro do cadastro da Vaga de Seleção.

* Só é possível exibir detalhe do andamento para vagas que são publicadas no portal.
* Para vagas com etapas sequencias é exibido um indicativo de qual etapa o candidato está, alem de exibir qual etapa de um total o candidato se encontra ex: 3/5.
* No caso de etapas paralelas é exibido: Você já cumpriu x etapas de um total de y etapas.
* Enquanto a vaga ainda não tiver sido iniciada, mantém a informação "Você está concorrendo para esta vaga" ao candidato
* Caso a vaga tenha sido iniciada e o candidato não tenha passado pela triagem, exibe a mensagem de agradecimento;

Foi criado um novo campo de texto no cadastro para mensagem de agradecimento de participação. Essa mensagem será exibida caso o candidato tenha sido reprovado ou eliminado.

**Atenção**, pois uma pessoa pode se candidatar a uma vaga que já esteja em andamento. Neste caso, deve exibir a mensagem "Você está concorrendo para esta vaga" até que ele seja triado ou que a vaga seja encerrada. Nestes casos, segue o fluxo já previsto nesta história.

## 6    Tipo de Pessoas

### 6.1   Cadastro

Foi criado um cadastro de Tipo de Pessoas (papéis) baseado em uma consulta ao banco de dados cadastrado no sistema. Ele permite o controle de permissões de acesso a campos e painéis do Banco de Talentos, configurados por Tipos de Pessoas.

Os Tipos de Pessoas cadastrados por padrão do sistema não poderão ser excluídos.

### 6.2   Painel de Opções

Alterado o Painel de Opções para incluir configuração de restrição baseados no Tipo de Pessoas para configurar as restrições.

Na tela do Painel de Opções é carregado checkbox de restrições de acesso para cada tipo de pessoa cadastrado

Na tela do Painel de Opções é carregado lookup multirecords que será utilizado para informar quais tipos de pessoas pode editar determinado campo;
