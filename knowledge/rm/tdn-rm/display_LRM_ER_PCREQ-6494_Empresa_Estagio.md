---
content_hash: da07725e2fa709d5d446cea302e7517b4411aeca1fb4ffd2a431c5c08f7c10b2
fetched_at: '2026-06-29T00:06:04.965590+00:00'
page_id: '200913005'
product: rm
source: tdn-rm
title: ER_PCREQ-6494_Empresa_Estagio
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-6494_Empresa_Estagio
version: 5
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Educacional | **Módulo** | Educacional |
| **Segmento Executor** | Educacional | | |
| **Projeto1** | R\_EDU\_EDU011 | **IRM1** | PCREQ-6493 |
| **Requisito1** | PCREQ-6494 | **Subtarefa1** | PDR\_EDU\_EDU011-558 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.8 | **Réplica** |  |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Permitir que os cadastros básicos da rotina de estágio (cadastro de empresas, cadastro de funcionários da empresa, cadastro de vagas de estágio oferecidas pela empresa) possam ser utilizadas de dentro do Fluig, com as novas interfaces criadas com base no TOTVS HTML Framework.

## Definição da Regra de Negócio

A central de estágio possibilita explorar meios que proporcionam ao aluno formação profissional de qualidade, no âmbito dos estágios curriculares e na relação com o mercado de trabalho. Esta relação se desenvolve no contato direto com as empresas privadas, públicas, organizações sem fins lucrativos e órgão de classes.

Em âmbito institucional assume a função acadêmico-administrativa de orientar e articular as ações propostas pelas Coordenações de Curso e/ou de Estágios, tendo em vista assegurar a qualidade do estágio dos estudantes, respeitando as particularidades de cada curso.

O ponto de partida é a inclusão das empresas conveniadas a instituição para a disponibilização das oportunidades de estágio e emprego.

A tela de cadastro de empresas é uma tela de cadastro simples, onde deve-se observar apenas a seguinte regra:

* Se no banco de dados o país estiver definido como Brasil (tabela GPARAMS campo PAIS = "BRA") e no cadastro de empresas o campo país estiver com valor nulo ou igual à Brasil, ao salvar o registro o sistema deve validar o CNPJ e atribuir a máscara adequada à esse campo, caso contrário (país definido no banco de dados não for Brasil) o sistema **não** deve validar o CNPJ nem atribuir qualquer tipo de máscara.

Como anexo da tela de cadastro de empresas, temos as funcionalidades a seguir:

1. Cadastro de funcionários da empresa;
2. Cadastro de convênios entre empresa e instituição de ensino;
3. Cadastro das vagas de estágio oferecidas pela empresa;

A seguir cada uma das funcionalidades sera detalhada.

1. Cadastro de funcionários da empresa:  
     
   1. Nessa tela é possível que sejam cadastrados funcionários da empresa que serão responsáveis por acessar o portal educacional e realizar o cadastro de vagas de estágio e aprovações em relação ao estágio dos alunos. Nesse cadastro, temos dois tipos de funcionários que são:
      1. Supervisor: responsável pela supervisão do estagiário na empresa. O sistema permite que seja parametrizável quantos alunos cada supervisor poderá supervisionar.
      2. Contato: ponto de contato entre instituição de ensino e empresa.
   2. Com o objetivo de manter o mesmo padrão dos cadastros de aluno e professores, foram incluídos novos campos no cadastro de funcionários da empresa:
      1. Para funcionários de todos os países: número do passaporte, data de emissão do passaporte, data de validade do passaporte, país de origem;
      2. Para funcionários de empresas do México: RFC;
      3. Para funcionários de empresas de Portugal: cartão cidadão, data de emissão do cartão cidadão, data de validade do cartão cidadão, órgão de expedição;
   3. Nessa tela, também deverá ser mantido o mesmo padrão da tela de cadastro de empresa com relação à validação e aplicação de máscara para o campo CPF, ou seja, se no banco de dados o país estiver definido como Brasil (tabela GPARAMS campo PAIS = "BRA") e no cadastro de funcionários o campo país estiver com valor nulo ou igual à Brasil, ao salvar o registro o sistema deve validar o CPF e atribuir a máscara adequada à esse campo, caso contrário (país definido no banco de dados não for Brasil) o sistema **não** deve validar o CPF nem atribuir qualquer tipo de máscara.
   4. Para cada funcionário cadastrado é possível associar um único usuário. Para realizar a geração de usuários para todos os funcionários daquela empresa, basta acessar o processo geração de usuários (funcionários) do registro da visão selecionada. Ao acessar o portal o funcionário deverá alterar no assistente de configuração o contexto global. Em entrar como, informar empresa. Para usuários associados à várias empresas, é permitido selecionar qual será o contexto de trabalho no portal educacional. Esse contexto de trabalho tem as seguintes informações:
      1. Identificador da empresa;
      2. Nome da empresa;
      3. CNPJ da empresa;
      4. Identificador do funcionário;
2. Cadastro de convênios entre empresa e instituição de ensino:  
     
   1. No convênio definimos se o candidato poderá enviar o e-mail diretamente para a empresa no e-mail informado, a data de início e fim do convênio bem como o número de vagas. Em anexo ao convênio, informamos quem é o público alvo: Nível de ensino, Curso e Habilitação. É possível criar o alerta que será enviado via e-mail informando que as vagas do convênio ainda não foram preenchidas e estão próximas de ultrapassar a data limite de divulgação. Se o convênio exige algum documento a ser entregue, durante o cadastro deve ser informado quais são obrigatórios e a quantidade. Uma empresa pode possuir de um a "n" convênios com a instituição de ensino.
3. Cadastro das vagas de estágio oferecidas pela empresa:  
     
   1. No cadastro de vagas preenchemos as informações pertinentes a vaga, os requisitos, cargo, departamento, local de trabalho, a carga horária semanal, hora inicial e final do expediente, horário de intervalo, a quantidade de vagas, vagas para deficientes, valor da bolsa, data limite para divulgação, se a vaga é de estágio ou emprego e o status atual: Pendente de aprovação, em aberto ou preenchida.
      1. Pendente de aprovação: vagas com esse status foram cadastradas, porém ainda não estão disponíveis para visualização/consulta pelos alunos.
      2. Em aberto: vagas disponíveis para visualização/consulta pelos alunos;
      3. Preenchida: vagas já preenchidas.
   2. Alterações nos dados da vaga são permitidos até mesmo depois de inscrições efetuadas, no entanto, o usuário pode parametrizar o sistema para que nestas situações seja enviado um e-mail para todos os alunos inscritos notificando sobre a alteração. Para parametrizar essa situação, o usuário deve acessar a tela de parâmetros do TOTVS Educacional em Configurações | Parâmetros | Estágio e na pasta Estágio 1/6 marcar o parâmetro "Enviar e-mail para candidatos sempre que houver alteração na vaga". A seguir, acessar o menu Currículo e Oferta | Acadêmico | Auxiliares | Mensagens de notificação e cadastrar uma nova mensagem com o objetivo de "Informar ao candidato que houve alguma alteração na vaga de estágio para a qual ele está inscrito".
   3. As vagas também podem ser cadastradas através do portal educacional, no menu administração, exibindo somente convênios da empresa do contexto selecionado, que estejam vigentes;
   4. Em anexo a vaga associamos o público alvo e definimos qual é o período mínimo para concorrer a vaga. O período mínimo não é obrigatório. Ele poderá ser alterado desde que não tenha nenhum candidato associado a vaga. No processo de matrícula do aluno é informado em qual período ele está sendo matriculado, portanto é necessário verificar se o período mínimo da vaga corresponde ao do aluno. Além do público alvo, temos também um anexo de candidatos à vaga, onde é possível consultar, alterar e incluir novos candidatos à vaga bem como associar suas matrículas e documentos anexos. A seguir temos detalhes sobre como inscrever candidatos em vagas de estágio.
      1. Serão disponibilizadas para o aluno vagas em que o público alvo definido seja compatível com sua habilitação;
      2. O aluno deve estar matriculado em um período letivo na coligada determinada no convênio onde a vaga foi divulgada (nos casos em que a filial também estiver definida no convênio o aluno deve estar matriculado na coligada e filial);
      3. A vaga deve estar com o status “Em aberto”;
      4. A data limite de publicação da vaga deve ser válida (vagas sem a data limite definida estão disponíveis enquanto o status da mesma ainda for "Em aberto");
      5. Toda vaga possui um horário inicial e final de expediente definido que pode ocasionar choque de horário com as disciplinas cursadas pelo aluno. O aluno pode, via portal, solicitar sua inscrição em uma vaga. Para efetivação da inscrição o sistema avalia o parâmetro “permite efetivar inscrição à vaga mesmo com choque de horário”. Quando estiver desmarcado o processo só é completado se não houver choque de horário.  Ao se inscrever na vaga o aluno pode anexar o currículo, que dependendo da parametrização do convênio pode ser encaminhado diretamente para a empresa ou anexado ao registro de candidatura. Ao termino da inscrição o aluno pode solicitar a impressão do “Termo de Encaminhamento” e acompanhar o status da sua inscrição nesta mesma tela. O status da vaga pode assumir um dos seguintes valores:
         1. Preenchida  (vaga já foi preenchida por outro aluno);
         2. Inscrição realizada (o aluno já se inscreveu nesta vaga);
         3. Selecionado (a vaga é do aluno em questão);
         4. Desistência (o aluno desistiu de concorrer à vaga);
      6. Sempre que uma vaga for preenchida o sistema (dependendo das parametrizações do estágio) pode encaminhar um e-mail ou SMS para o aluno selecionado informando quais os próximos passos para conclusão do processo. Já nos casos em que não houver mais vagas disponíveis outro e-mail ou SMS pode ser enviado para os alunos que não foram selecionados.
   5. No portal educacional, há a possibilidade do funcionário da empresa parceira da instituição cadastrar uma nova vaga ou edita-la, essas vagas recebem o status “Pendente de aprovação”. Além de associar as mesmas ao público alvo.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
