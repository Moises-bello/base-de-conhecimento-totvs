---
content_hash: fea03333a501eb687db6daa0320bd425a91ff4df55f0c951ec770ca3867a847b
fetched_at: '2026-06-29T00:06:26.540955+00:00'
page_id: '225951106'
product: rm
source: tdn-rm
title: Ferramenta Conversor
type: documentation
url: https://tdn.totvs.com/display/LRM/Ferramenta+Conversor
version: 6
---

Antes da execução é obrigatória a leitura e aplicação de todos os passos presentes na página:

Antes da execução deste passo é importante que tenham sido criadas cópias de segurança da base de dados.

Observações: 

- Verifique se os parâmetros MAXEXTENTS estão configurados de forma a permitir que o Banco de Dados cresça durante a conversão.   
- Durante a conversão devem existir segmentos de ROLLBACK suficientes e que possam ser expandidos.   
- Certifique-se que existe espaço disponível no disco, para armazenamento do log.  
- Clientes que possuírem estratégias de espaço de backup baseadas em cópias do log de transações e que não utilizem a opção "Truncate Log On Checkpoint", deverão após a conversão realizar o backup completo da base de dados novamente.

**Antes da entrada em produção, mesmo que o log não apresente nenhuma falha, o suporte da TOTVS deve ser acionado para validar todo o processo.**

**Conteúdo**

- Definição do contexto de migração

- Telas de Parametrização

**Definição do contexto de migração**

O TOTVS Educacional agrupa os cursos oferecidos em Níveis de Ensino, um conceito inexistente no RM CLASSIS. O usuário deve especificar para cada Coligada que vai ser convertida quais Níveis de Ensino devem ser criados para agrupar a oferta.

O Conversor de tabelas do RM CLASSIS deve ser executado para cada COLIGADA existente na base original.

A tela inicial do aplicativo alerta o usuário para as providências que se fazem necessárias antes de se executar a migração.

O primeiro passo é o Login na base de dados que deve estar definida por um alias do BDE.

Somente serão apresentados os Alias que estiver com a descrição inicial definida "CorporeRM\_", conforme o exemplo acima.

O passo seguinte é a especificação do Sistema de Origem, Básico ou Superior, e do nome do arquivo de log, em formato texto, que será gerado durante o processo.

Caso o Sistema de Origem seja o **Ensino Superior**, podem ser definidas duas opções

[ 1 ] - Migrar as Equivalências de acordo com o padrão do novo sistema “por disciplina” ou fazer a migração mantendo o conceito do sistema de origem que leva em conta a Grade.

[ 2 ] – Criar grupos de Disciplinas Optativas/Eletivas por Período Letivo tal como é feito no sistema de origem ou trabalhar com estas disciplinas de acordo com o conceito do TOTVS onde estão agrupadas num “período zero”.

Caso o Sistema de Origem seja o **Ensino Básico**, não existem outras opções

O botão <Iniciar Conversão> só vai ser habilitado após estas informações serem registradas

O passo seguinte é selecionar a COLIGADA e cadastrar os níveis de ensino.

O registro dos níveis de ensino é feito diretamente na planilha. Deve ser informado um código único e uma descrição.

Siga a sequência abaixo:

Se o botão <Avançar> for clicado antes de se salvar um registro vai ocorrer um erro e o Conversor vai ser encerrado.Os níveis de ensino ficam salvos na base e quando ocorre um reprocessamento eles são automaticamente recuperados pela ferramenta quando a Coligada é selecionada.

Após a criação dos níveis de ensino o sistema ficará com a tela, conforme o print abaixo:

**Etapas de Conversão**

O Conversor é dividido em uma série de passos que serão executados de acordo com o sistema que vai ser migrado Ensino Básico ou Ensino Superior. Em alguns destes passos vão ser apresentadas telas permitindo a especificação de parâmetros para o processo.

O usuário pode marcar quais passos deseja executar.

O Conversor é dotado de um mecanismo que determina pré-requisitos para a execução de cada passo, e caso um passo que foi selecionado pelo usuário não tenha tido todos os passos obrigatórios para sua execução já executados ele vai ser “desmarcado” **automaticamente** quando o Conversor tentar inicia-lo.

A lista de todos os passos para o Ensino Básico e para o Ensino Superior pode ser encontrada no final deste documento.

**Telas de Parametrização**

As telas de parametrização são utilizadas para que o usuário possa associar aos dados migrados informações que não podem ser inferidas pela ferramenta, a maioria delas solicita a vinculação de dados a um nível de ensino.

**Filiais**

Esta tela permite informar os Níveis de Ensino oferecidos em cada Filial.

**Graus do Ensino Fundamental**

Exibida apenas na migração do Ensino Superior. Solicita ao usuário a correlação entre os registros da tabela de cursos de segundo grau mantida no RM CLASSIS com a lista fixa de cursos de segundo grau do TOTVS Educacional. Como este é um dado opcional no RM CLASSIS esta tela pode ser exibida “em branco”.

**Cursos**

Permite vincular o Curso com o Nível de Ensino correspondente.

A tela permite que a lista seja ordenada com um clique no título da planilha, e que um grupo de cursos seja arrastado para o Nível de Ensino desejado.

**Disciplinas**

Na aba **Mapeamento** as disciplinas que não estão associadas a nenhuma grade são exibidas nesta tela. Como a disciplina no TOTVS deve ter um código único, disciplinas com códigos iguais de cursos diferentes receberam um novo código que podem ser modificados nesta aba.

Na aba **Principal** o usuário pode associar cada disciplina a Níveis de Ensino específicos.

A modificação de códigos não pode ser feita após ter sido feita qualquer associação.

**Períodos Letivos**

Nesta tela podem ser associados os períodos letivos em que cada Filial ofereceu um determinado nível de ensino.

Ao final da Conversão o sistema exibirá o resultado da Conversão, indicando se houveram erros críticos, que impedem a entrada em produção.

Mesmo não apresentando nenhum no log, ou na mensagem, conforme o print acima, é altamente recomendado que o procedimento seja validado pela equipe de Suporte Técnico do Educacional.
