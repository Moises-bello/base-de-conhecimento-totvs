---
content_hash: 6e3336a1181fc58b489d1432eeae5d790028dee7fbc22653b97d909db2bd2c0c
fetched_at: '2026-06-29T00:10:38.953245+00:00'
page_id: '545631319'
product: rm
source: tdn-rm
title: TOTVS Gestão Hospitalar > Integrações > Anestech
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=545631319
version: 69
---

## **ÍNDICE**

1. **Visão Geral**
2. **Configuração**
3. **Fila da Integração**
4. **Itens que são****integrados**
5. **Integração Relacionamento**
6. **Recebimento Cirurgia de Emergência**

Visão GeralVisão Geral

## **01. VISÃO GERAL**

Esse documento explica como configurar e como funciona a integração do RM com o sistema AxReg da Anestech.

Configuração

## **02.** **CONFIGURAÇÃO**

Para o funcionamento correto da integração é necessário realizar as seguinte configurações:

1 - Parâmetros Gerais (Ambiente > Parâmetros > Gestão Hospitalar > Integrações > Anestech)

Na tela devemos indicar qual a URL e chave de segurança, para a integração com a API da Anestech, para isso devemos acessar a tab Integração e na parte inferior da aba devemos selecionar Anestech, vide imagem abaixo:

Devemos preencher as informações correspondentes a cada uma dos campos.

Além disso, também temos o parâmetro Utilizar múltiplos ambientes

2 - Unidade de atendimento (Cadastros > Uso Geral > Unidade de Atendimento)

Na tela de cadastro a unidade de atendimento foi adicionado uma caixa de seleção, onde o usuário deve configurar se a unidade está utilizando integração com a Anestech, vide imagem abaixo:

Fila da Integração

## **03.** **FILA DA INTEGRAÇÃO**

Foi criada uma fila da integração com a Anestech onde pode ser verificado tudo o que foi enviado para a Anestech e o retorno da integração, que pode ser sucesso ou a mensagem de erro. Você pode acessar essa fila em (Utilitários> Integrações > Integração Anestech).

Para que os itens que estão com o Status *Aguardando a integração* seja integrados você executar o processo *Enviar dados para Anestech* para que a integração seja efetuada imediatamente.

Para que o envio seja feita automaticamente é necessário agendar a execução desse processo para que seja executado na periodicidade desejada. Você pode ver detalhes de como fazer o agendamento na seguinte documentação: 

O processo *Receber dados da Anestech* também deve ser agendado para ser executado automaticamente dessa forma serão importados os dados do sistema da Anestech. Será criada inicialmente uma linha na tabela Integração Anestech com a mensagem recebida com os procedimentos e depois para cada importação será criada um outra linha informando se foi efetuado com sucesso ou se teve algum problema.

Para o recebimento das informações referentes aos procedimentos é necessário que: No caso de atendimento sus seja cadastrado o código do procedimento sus. Caso convênio necessário ter cadastrado o item de débito. Para realizar as configurações citadas devemos acessar: Menu > Cadastro > Cirurgias > Procedimento para Agenda de Cirurgia, após abrir a tela, acessar a aba Itens de Débito e/ou Procedimentos SUS.IMPORTANTE!

O processo Reintegrar dados da Anestech deve ser utilizado para tentar reimportar os dados que não foram possível devido algum erro, por exemplo, quando for tentar importar um medicamento mas não está cadastrado o seu identificador na tabela Integração Relacionamento.

Existe o processo *Inserir dados na integração com a Anestech* que pode ser utilizado para inserir itens na fila de integração dessa forma não é necessário editar e salvar cada cadastro que deseje que seja integrado, esse processo deve ser utilizado para carga inicial da integração com Anestech.

Através desse processo você pode inserir os  Convênios, Materiais, Procedimento cirúrgico e Sala do bloco cirúrgico  que devem ser integrados.

No caso de a instituição utilizar o conceito de grupo, ao adicionar um material na fila, será validado se o mesmo possui saldo no local de estoque vinculado a unidade de atendimento, caso tenhamos mais de um grupo configurado no RM, iremos adicionar o material na fila N vezes, de acordo com a quantidade de grupos. Caso tenhamos o grupo A e grupo B, no momento que adicionamos o material na fila será criado duas linhas, para que o produto seja enviado para ambos os grupos.

Os Materiais não serão integrados quando é inserido ou editado. Você precisa adicionar eles através desse processo na fila de integração.IMPORTANTE!

Itens que são integrados

## **04.** **ITENS QUE SÃO INTEGRADOS**

Abaixo segue uma tabela com todos os itens do RM que são integrados com a Anestech.

| Dado do RM | Dado da Anestech | Envio/Recebimento | Observações |
| --- | --- | --- | --- |
| Unidade de Atendimento | Setor/Centro Cirúrgico | Envio | Integra se a Unidade de atendimento está com o parâmetro *Possui integração com Anestech* marcado. |
| Sala do Bloco Cirúrgico | Sala Cirúrgica | Envio | Integra se tiver associada a uma unidade de atendimento integrada. |
| Materiais | Materiais | Envio | Precisa ter alguma unidade de atendimento integrada. Os materiais não são integrados no momento que é salvo o cadastro, para que seja realizada a integração é necessário usar o processo *Inserir dados na integração com a Anestech*. |
| Convênio | Convênio | Envio | Precisa ter a tabela de procedimentos básico definida nos parâmetros gerais. No momento de envio do convênio, caso não exista a tabela enviada incluiremos na fila nesse momento. |
| Prestador / Agenda Cirúrgica / Registro de Informações Cirúrgica | Cirurgião | Envio | Precisa ter alguma unidade de atendimento integrada. |
| Prestador/ Agenda Cirúrgica / Registro de Informações Cirúrgica | Equipe médica | Envio | Precisa ter alguma unidade de atendimento integrada. |
| Paciente | Paciente | Envio | É integrado através da adição de agendamento de cirurgia e também de atendimento. |
| Agenda Cirúrgica | Procedimentos | Envio | É integrado através da adição ou alteração de agendamentos cirúrgicos, desde possuam procedimentos cadastrados.  O recebimento dos dados dos procedimentos cirúrgicos que forem cadastrado no ambiente Anestech somente serão retornado ao RM, caso a agenda cirúrgica tenha sido vinculada a um Registro de Informação Cirúrgica.  Caso nesse momento o paciente não tenha sido integrado ele será inserido na fila de integração. |
| Folha de Sala | Procedimentos/Drogas | Recebimento | Quando for finalizado o procedimento na Anestech será criada uma Movimentação de Estoque do tipo Folha de Sala que é associada ao Registro de Informações de Cirurgia com os medicamentos inseridos. |
| Agenda Pré Anestésica | Agenda de atendimentos | Envio | Precisa ter alguma unidade de atendimento integrada e a agenda deve ser do tipo pré anestésica. |
| Procedimento cirurgião | Procedimento cirurgião | Envio | Necessário que exista algum convênio integrado com a Anestech. |
| Registro de Informações de Cirurgia | Procedimentos | Envio | É integrado através da adição ou alteração de registro de informação cirúrgicas. Entretanto, devem possuir procedimentos cadastrados. |
| Registro de Informações de Cirurgia / Tempo de Cirurgia | Procedimentos | Recebimento | Quando for finalizado o procedimento na Anestech será importado a data e hora do início e do final do procedimento. Também será calculado o tempo da cirurgia. Caso o tempo de cirurgia for maior que o tempo de sala, o usuário deve atualizar essa informação manualmente no RM, a Anestech não nos envia o tempo de sala. |

Para as instituições que utilizam o conceito de grupo, antes de enviar as informações é necessário configurar o grupo como descrito nas instruções abaixo. As entidades afetadas pelo uso de grupo são: Agendamento, materiais, paciente, sala cirúrgica e unidade de atendimentoIMPORTANTE!

Integração Relacionamento

## **05.** **INTEGRAÇÃO RELACIONAMENTO**

Para fazer integração com medicamentos antes é necessário que esteja cadastrado no sistema os identificadores de medicamentos dos produto RM e Anestech. Para fazer isto acesse Utilitários e depois Integração relacionamento. Como é mostrado abaixo

Para cadastrar um novo clique em incluir e preencha da seguinte forma:

* **Identificador RM**: Identificador do medicamento que consta no sistema RM
* **Identificador Sistema:** Identificador do medicamento que consta no sistema Anestech
* **Descrição**: Pode-se entrar qualquer coisa
* **Tipo de Integração:** Para anestech usamos ou Produto ou Unidade
* **Sistema Integrador:** No caso, sempre será escolhido Anestech

Após clicar em salvar, o registro será salvo. Dessa forma, ao fazer uma integração que envolva medicamentos estas informações serão consultadas para fazer a integração corretamente.

Foi criado um processo para importar todos os medicamentos da Anestech visando simplificar o cadastro do de/para dos medicamentos.

**Para as instituições que utiliza grupo**. Foi criado um processo para a importação de todos os grupo da Anestech com o intuito de permitir o vínculo entre o grupo da Anestech com a unidade de atendimento no RM. Com esse cadastro no momento do envio das informações para Anestech elas devem ser agrupadas pelo seu determinado grupo.

Recebimento - Cirurgia de Emergência

## **06.** **RECEBIMENTO - CIRURGIA DE EMERGÊNCIA**

Quando um procedimento cirúrgico é criado pela Anestech, existe a possibilidade deste ser importado para o RM. Essa importação consiste na criação do Paciente\*, Registro de Atendimento, Agenda Cirúrgica e do Registro de Informação Cirúrgica.

O Paciente só será criado caso o mesmo não exista no RM. Ao recuperar as informações para criar a cirurgia de emergência, caso o paciente utilizado possui CPF será verificado se ele já está cadastrado no RM, caso esteja não será criado um novo paciente no RM, caso não, será criado um novo paciente no RM com os dados informados pela integração com a anestech.

Para que o recebimento seja finalizado, todas a informações utilizadas no cadastro do procedimento (Anestech) já devem ter sido enviadas pelo RM.

A regra para seleção do Plano e Convênio que serão utilizados no Registro de Atendimento será o último utilizado pela paciente, caso não exista nenhum Registro de Atendimento, será utilizado o primeiro Plano vinculado ao Convênio seleciondo na Anestech. Esta regra é necessária pois não há a possibilidade de selecionar o Plano na cadastro do procedimento pela Anestech.

Além disso, existem alguns pré requisitos que devem ser parametrizados no RM:

No Registro de Atendimento os campos “Cod. Usuário Convênio”, “Validade Carteira”, “Dep.”, “Procedencia”, “UF” e “Cidade Origem” não poder ser obrigatórios para o convênio utilizado.

Para alterar a obrigatoriedade dos campos “Dep” e “Validade Carteira”, acessar Cadastros > Condições Contratuais, selecionar o convênio, na guia “Parâmetros 1” e desmarcar as opções abaixo:

Para alterar a obrigatoriedade dos campos “Procedência”, “UF” e “Cidade Origem”, acessar Ambiente > Parâmetros > Gestão Hospitalar > Registro e Controle > Solicitar no Registro de Atendimento e desmarcar as opções abaixo:

O processo responsável pelo recebimento da cirurgia de emergêcia pode ser executado atraves do processo **Receber dados da Anestech,**em Utilitários> Rotinas > Integração Anestech.

## **07.** **Padrão de envio de informação de data/hora com time zone**

Conforme solicitado pela Anestech foi revisado o padrão de envio de informação data/hora e o padrão será 2020-02-11T09:00:00-03:00 ( AAAA-MM-DDTHH:MM:SSZZZ )
