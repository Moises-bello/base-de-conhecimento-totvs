---
content_hash: 1fe92d4701d79b34c8f304e75c68e659a1d9891e41c03fbf2152e3c3b3730d04
fetched_at: '2026-06-29T00:06:16.063844+00:00'
page_id: '211062337'
product: rm
source: tdn-rm
title: DT_Central_Notificacao
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Central_Notificacao
version: 129
---

# Central de Notificação

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | *TOTVS Educacional* |
| **Módulo:** | *Educacional* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Mensagens de notificação | Cadastro de templates das mensagens de notificaçõe*s* | | Mala Direta | Processo de envio de mala direta | | Envio de posts para comunidades e notificações para usuários do Fluig | Processo de envio de posts para comunidades e notificações para usuários do Fluig | | Envio de mensagens de notificações temporais | Processo que envia mensagens de notificações temporais |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Parâmetros Globais | Cadastros dos parâmetros globais | | Parâmetros do TOTVS Educacional | Cadastros dos parâmetros do TOTS Educacional | |
| **Cadastros Iniciais:** | *Parametrização da integração com o Fluig e servidor de E-mail* |
| **Parâmetro(s):** | Parâmetros do sistema relacionados a central de notificação e conta de comunicação, parâmetros globais para integração com o Fluig |
| **Requisito (ISSUE):** | [PCREQ-5421](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-5421 "PCREQ-5421") |
| **País(es):** | *Brasil* |
| **Tabelas Utilizadas:** | SMENSAGEMPADRAO, STURMA, STURMADISC, SSUBTURMA, SCURSO, SHABILITACAO, SALUNO, SPROFESSOR, PPESSOA, GUSUARIO, SCOMUNIDADESOCIAL, SPARAM, SATIVIDADE |
| **Versões/Release:** | *12.1.9* |

## Descrição

 A central de notificação será composta da junção de duas funcionalidades já implementadas no TOTVS Educacional e a adição de outras duas, são elas: 

* Cadastro de Mensagens de Notificação
* Processo de Mala Direta
* Processo de Envio de Notificação e/ou Post nas Comunidades (nova funcionalidade)
* Processo de Envio de Mensagens de Notificações Temporais (nova funcionalidade)

# Configuração do ambiente

## Fluig:

1. Utilizar o usuário administrador do Fluig e acessar o**Painel de controle -> WCM**
2. Configurar o**Oauth Provider**
3. Configurar o **Oauth App**(pode-se utilizar qualquer conjunto de caracteres para definição do *Consumer Key* e *Consumer Secret*)  
   Para mais detalhes sobre o passo 2 e 3 consulte o documento "Cadastrar aplicativo no Fluig" pelo link: <http://tdn.totvs.com/display/public/fluig/Fluig+API#FluigAPI-CadastraraplicativonoFluig>

## Parâmetros Globais e Contas de Comunicação

1. Acessar a guia **Ambiente -> Parâmetros -> Globais**
   1. Aba: **Integração Fluig** definir:
      1. Endereço do servidor do Fluig
      2. Id da empresa do Fluig
      3. Usuário administrador do Fluig
      4. Senha do usuário administrador do Fluig
   2. Aba: **Integração oAuth** definir:
      1. Chave de consumo: é a chave *consumer key* definida na etapa da configuração do fluig.
      2. Chave secreta: é a chave*consumer secret* definida na etapa da configuração do fluig.
   3. Salvar os parâmetros
2. Acessar a guia **Gestão -> Fontes** e verificar se a fonte de comunicação com o Fluig está cadastrada. Caso não encontre entre em contato com o suporte da TOTVS.
3. Acessar a guia **Gestão -> Contas -> Contas individuais** e criar um novo registro
   1. Código da fonte de comunicação: vincular a fonte relacionada ao Fluig
   2. Utilizar "Usar esta conta como remetente"
   3. Identificação na rede social: informar o usuário mestre do Fluig
   4. Obter credenciais: ao clicar neste botão será exibida a tela de login do Fluig onde deve ser informado o usuário administrador e sua senha
   5. As credenciais serão obtidas e o campo Descrição será preenchido com o nome do usuário administrador.
   6. Salvar o registro

## Cadastro de Mensagens de Notificação (Acessar TOTVS Educacional | Atividades Acadêmicas | Central de notificações | Mensagens de Notificação)

Na versão 12.1.7 todos os parâmetros do sistema relacionados a definição das mensagens de e-mail foram deslocados para este cadastro, unificando o ponto de definição das mensagens de notificação. A partir da versão 12.1.9 este cadastro sofre mais uma evolução passando a permitir que as mensagens de notificação possam ser também enviadas como notificações para usuários no Fluig. Importante frisar que esta evolução foi implementada apenas para o módulo TOTVS Educacional.

Outro ponto, é que a partir desta versão todos os parâmetros que determinam o envio ou não da mensagem foram transferidos dos parâmetros do Educacional para esse cadastro, desta forma na definição da mensagem o usuário passa a parametrizar se utilizará o envio por e-mail e/ou por notificação.

O tipos de mensagens de notificação disponíveis no TOTVS Educacional:

1. **Categoria: Secretária**
   1. Confirmar reservas de recursos
   2. Confirmar reservas de instalações
2. **Categoria: Estágio**
   1. Informar ao aluno que houve alguma alteração na vaga de estágio para a qual ele está inscrito
   2. Informar ao aluno que ele foi selecionado para a vaga de estágio na qual está inscrito
   3. Informar ao aluno que ele não foi selecionado para a vaga de estágio na qual está inscrito
   4. Informar ao aluno sobre aprovação do plano de atividades do estágio
   5. Informar ao aluno sobre reprovação do plano de atividades do estágio
   6. Informar para o participante que ele foi convidado para a banca
3. **Categoria: Pesquisa e Extensão**
   1. Informar os pesquisadores sobre a divulgação do edital (Pesquisa)
   2. Informar os pesquisadores sobre a divulgação do edital (Extensão)
4. **Categoria: Matrícula e Avaliação**
   1. Pendências financeiras do aluno
   2. Cadastro de ocorrência para o aluno
   3. Frequência do aluno próximas do limite ou excedida
   4. Pendências de matrícula
   5. Liberação ou digitação de etapa de nota
   6. Liberação ou digitação de etapa de falta

Os tipos de mensagens passam a ter uma classificação interna que determina de que modo estas são disparadas:

1. **Classificação: Fixa** -> mensagens com este tipo de classificação são disparadas por funcionalidades já existentes no sistema.
2. **Classificação: Temporal** -> mensagens com este tipo de classificação são disparadas pela funcionalidade "**Envio de mensagens de notificações temporais**".   
   As mensagens temporais disponíveis neste primeiro momento são:
   1. Pendências financeiras do aluno
   2. Frequência do aluno próximas do limite ou excedida
   3. Pendências de matrícula.

Escolhida a mensagem que se quer definir pode-se preencher os seguintes campos:

1. Ativar envio por e-mail
   1. Assunto do e-mail
   2. Texto do e-mail (para envio no formato HTML é permitido formatar o texto e incluir imagens)
   3. Enviar e-mail como HTML ou texto
2. Ativar envio por notificação via Fluig
   1. Texto da notificação (não poderá conter formatação e nem imagens)

Lembrado que cada mensagem de notificação possui algumas tag's que podem ser incluídas na definição do template da mensagem a ser encaminhada.

## Processo de Mala Direta (Acessar TOTVS Educacional | Atividades Acadêmicas| Central de Notificações| Mala direta**)**

1. Informar a consulta SQL responsável por listar os usuários, depois de informado os parâmetros (caso sejam necessários) e executada a consulta os registros são listados para visualização do usuário. Caso seja necessário remover algum registro basta selecionar o mesmo e clicar em remover.
2. Informar o conteúdo da mensagem a ser encaminhada via mala direta. Neste passo o usuário tem as seguintes opções:
   1. Importar um arquivo template para a mala direta
   2. Criar um novo arquivo
   3. Editar um arquivo existente.Após criar a mensagem o usuário poderá salvá-la em um arquivo para que possa ser utilizado futuramente no envio de outra mala direta (através dos recursos disponíveis na barra de formatação). No conteúdo da mensagem é possível utilizar tags bastando clicar no botão “Tags Disponíveis” e selecionar a que se quer utilizar. As tags disponíveis são as colunas retornadas pela consulta SQL selecionado pelo usuário.
3. Definir a forma de execução  
   1. **Enviar por e-mail**  
      * Informar assunto do e-mail;
      * Tipo de remetente:
        + Usuário logado no sistema;
        + Coligada atual; Coligada global;
        + Parâmetros globais (parametrização padrão de envio de mensagens que está definido na tela de parâmetros Globais na aba Envio E-mails);
        + Personalizado: o usuário poderá informar um e-mail e nome do remetente a ser identificado. Esta lista de e-mail(s) personalizado precisa ser informado em **TOTVS Educacional | Configurações | Configuração |Parâmetros | Secretaria | Geral 4/4]**
        + Identificador dos registros de log.**Atenção:** Para que seja possível enviar e-mails a consulta SQL utilizada precisa conter a coluna EMAIL.
   2. **Gerar arquivos**
      * Informar diretório físico onde serão gravados os arquivos criados;
      * Informar o prefixo para nome dos arquivos. Caso o usuário tenha carregado um arquivo de template no editor de texto, o nome do arquivo será carregado neste campo “prefixo para nome dos arquivos”, podendo o usuário alterar o seu conteúdo.
      * Informar em  “Salvar como” qual extensão para os arquivos. O usuário terá como opção às seguintes extensões: pdf, rtf, doc, docx e html.
      * Identificador dos registros de log.
4. Após clicar no botão “Executar” será exibida a tela padrão de andamento do processo e nesta teremos dois botões com funcionalidades diferentes:  
   1. Botão “Cancelar”: Aborta o andamento do processo, mostrando o log até o momento do cancelamento.
   2. Botão “Fechar”: Ao clicar neste botão, o usuário será informado que a tela do processo será fechada e que sua execução continuará em segundo plano. Para que a tela seja fechada é solicitado ao usuário uma confirmação escolhendo a opção “Sim” a tela é fechada e a execução é realizada em segundo plano, ou a opção “Não” que continua o processamento normalmente com a tela aberta.  
      **Importante:** Quando o processo estiver sendo executado em segundo plano, o usuário  receberá uma caixa de mensagem quando sua execução for finalizada.

## Processo de Envio de Posts para Comunidades e Notificações para Usuários do Fluig (Acessar TOTVS Educacional | Atividades Acadêmicas| Central de Notificações| Envio de posts para comunidades e notificações para usuários do Fluig)

Este processo só estará disponível se houver integração com o Fluig. A integração será entendida como ativa quando o parâmetro código de comunicação estiver preenchido nos parâmetros do TOTVS Educacional. Este processo disponibilizará as seguintes etapas:

1. Definições relacionadas ao mecanismo de geração das informações.

1. 1. Campo: "Tipo de saída"
      * Post nas comunidades do Fluig (esta opção só estará disponível se o sistema estiver integrado com a parte Social do Fluig, ou seja, o TOTVS Educacional deve estar configurado para utilizar a funcionalidade "Acadêmia Social")
      * Notificação para usuários do Fluig
   2. Campo: "Tipo de consulta"
      * Consulta padrão do sistema
      * Consulta SQL
   3. Entidades:
      * Para "Post nas comunidades do Fluig" podemos ter (depende de quais entidades estão parametrizadas para integrar com o Fluig):
        + Turma
        + Turma/Disciplina
        + Subturma
        + Atividade Ofertada
        + Curso
        + Habilitação ou Serie
      * Para "Notificação para usuário do Fluig" podermos ter:
        + Aluno
        + Professor
        + Pessoa
2. Seleção dos registros
   1. Se o campo tipo saída for: "Post nas comunidades do Fluig"
      * Definição de SQL:
        + A sentença deverá conter obrigatoriamente o campo "ALIASCOMUNIDADE".
        + Se a sentença retornar comunidades inativas na execução do processo essas deverão ser ignoradas
      * Definição via consulta as comunidades:
        + Selecionar as comunidades que devem receber o post (apenas comunidades ativas são listadas)
   2. Se o campo tipo saída for: "Notificação no Fluig"
      * Definição do SQL responsável por buscar a lista dos destinatários das notificações.
      * A sentença SQL deverá conter obrigatoriamente os campos "CODUSUARIO" e "EMAIL".
3. Definição da mensagem a ser encaminhada
   1. As tags disponíveis para definição da mensagem contém todos os campos retornados no SQL criado pelo cliente ou na consulta exibida na seleção das comunidades.
   2. A mensagem não permitirá formatação do texto e/ou inclusão de imagens
4. Ao executar o processo o mesmo terá como resultado final a criação do post nas comunidades ou o envio das notificações para os usuários do Fluig.

## Processo de Envio de Mensagens de Notificações Temporais (Acessar TOTVS Educacional | Atividades Acadêmicas| Central de Notificações| Envio de mensagens de notificações temporais)

 Este processo será responsável por disparar as mensagens de notificações classificadas como temporais, para tanto o usuário deverá:

1. Definir o período letivo
2. Definir as notificações temporais que devem ser executadas
3. Definir o tipo de consulta:
   1. Consulta padrão do sistema
      1. Pode-se definir a curso, habilitação, matriz curricular ou matriz aplicada
      2. Pode-se definir a turma
   2. Consulta SQL
      1. Definir a consulta SQL. Deve possuir obrigatoriamente os campos CODCOLIGADA, RA, CODUSUARIO e EMAIL para todas as notificações temporais e para a notificação de pendência de matrícula ainda deverá conter os campos "IDHABILITACAOFILIAL", "CODCURSO", "NOMECURSO", "CODHABILITACAO" e "NOMEHABILITACAO".
      2. Preencher os parâmetros
4. Se a mensagem de notificação temporal estiver parametrizada para envio por e-mail todos destinatários que não possuírem um e-mail definido serão ignorados.
5. Se a mensagem de notificação temporal estiver parametrizada para notificação no Fluig:
   1. Parâmetros Educacional: deve possuir a definição da conta de comunicação
   2. Todos destinatários que não estiverem cadastrados no Fluig serão ignorados.
6. O log final do processo contendo o detalhamento das mensagens enviadas com sucesso e as que por algum motivo não puderam ser enviadas.

## Documentação Adicional:

1. Para utilizar o envio de posts para comunidades deve-se parametrizar a acadêmia social, para mais informações sobre este item acesso o Documento Técnico:

divs
