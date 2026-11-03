---
content_hash: e977c2600132f5cd41532626405f83b765675aa5d41ed3c972549b28605b023f
fetched_at: '2026-06-29T00:12:03.231012+00:00'
page_id: '904598142'
product: rm
source: tdn-rm
title: Protocolos assistenciais
type: documentation
url: https://tdn.totvs.com/display/LRM/Protocolos+assistenciais
version: 22
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Cadastros**
   1. **Identificação**
   2. **Formulário**
   3. **Gatilhos**
   4. **Validações**
3. **Prontuário Eletrônico**
4. **Alerta crítica**

Protocolos assistenciais1. Visão geral

## **01. VISÃO GERAL**

A funcionalidade de Protocolos Assistenciais permitirá que profissionais de saúde cadastrem, gerenciem e apliquem os protocolos clínicos preconizados pela instituição.

Os protocolos clínicos são ferramentas fundamentais na prática assistencial em ambientes hospitalares. Eles fornecem diretrizes baseadas em evidências científicas, padronizando condutas e garantindo uma abordagem uniforme no cuidado aos pacientes. Além disso, promovem a redução de variações indesejadas na prática médica, contribuindo para a melhoria da qualidade do atendimento.

A implantação e utilização de protocolos clínicos impactam diretamente na segurança do paciente, minimizando riscos e prevenindo eventos adversos. Isso é possível por meio da definição clara de fluxos de trabalho, identificação de etapas críticas no cuidado e a promoção de um ambiente mais seguro para o paciente e para os profissionais de saúde.

3. Cadastros

## **02. CADASTROS**

O cadastro de protocolos assistenciais é realizado no RM → Cadastros → Cuidados com o Paciente - Outros Cadastros → Gerenciamento de Risco → Cadastro de protocolos assistenciais.

Os protocolos assumem 3 status diferentes ao serem elaborados:

1. Emitido: Protocolo foi registrado, salvo e finalizado
2. Revisado: Protocolo emitido anteriormente porém a versão passou por alguma revisão. Este documento ele é utilizado como controle dos versionamentos e alterações realizadas porém, não encontra-se acessível ao usuário final para novos preenchimentos. O protocolo com status de revisado possui um novo documento criado com versionamento acima, portanto não apresenta a possibilidade de passar por alteração, suspensão ou cancelamento.
3. Suspenso: Protocolos suspensos não são apresentados ao usuário final e não apresenta a possibilidade de passar por alterações ou cancelamentos. São protocolos que deixaram de ser utilizados na instituições porém, em algum momento foi utilizado.
4. Pendente: Protocolos que não iniciados ou revisados porém não passaram pelos status de salvos e finalizados, ficam com o status de pendentes. Todos protocolos salvos porém não finalizados recebem este status.

## **2.1 IDENTIFICAÇÃO**

A tela de identificação do protocolo consiste no cadastro de campos que identificam este protocolo, detalham a unidade de atendimento em uso, o perfil de paciente a ser aplicado, tipos de alertas utilizados e restrições para abertura e fechamento do protocolo. 

Na primeira etapa de preenchimento temos os campos relacionados a identificação do documento, o seu versionamentos, datas de emissão, revisão e próxima revisão, e os seus responsáveis. Como regra não é possível ter dois protocolos com a mesma identificação de Código e Nome do protocolo com o mesmo número de versionamento, a versão deve sempre seguir uma ordem crescente conforme as revisões forem efetuadas. A data de revisão deve ser maior ou igual que a data de emissão e a data relacionada a próxima revisão será uma data futura. 

A segunda e terceira etapa temos a identificação do protocolo e  definição de sua aplicabilidade, deve-se determinar qual o tipo de protocolo estamos registrando, o nome e a sua descrição, a unidade de atendimento que ele será utilizado pela equipe assistencial. Define-se no produto determinação do tipo de protocolo de acordo com a sua aplicabilidade. Definições do produto:

1. Clínico → Protocolos utilizados a determinadas situações clínicas específicas
2. Cirúrgico → Protocolos utilizados somente na Jornada Cirúrgica do paciente (Ex. Protocolo de Cirurgia Segura)
3. Segurança do Paciente → Utilizado amplamente, independente do perfil ou da jornada de cuidado do paciente

Os últimos cadastrados são referencias de alerta que o protocolo vai apresentar ao ser utilizado e quais os perfis de profissionais vão ter permissão para abertura e fechamento de determinado protocolo. Trago como exemplo protocolo Sepse:

**Exemplo de Preenchimento**

**Protocolo Sepse**

* + - Unidade de atendimento: Todas as unidades → Vínculo em todas as unidades, uma vez que, a instituição use o protocolo por todo o serviço.
    - Perfil do paciente: Ambos → Não é um protocolo que apresenta alguma especificidade relacionada ao sexo do paciente
    - Alerta: Alerta crítico → Não é permitido o usuário final selecionar que não aceita receber este alerta, a determinação é da gestão do serviço.
    - Enviar e-mail → Adiciono os e-mails dos coordenadores, para que fiquem ciente que determinada unidade de atendimento e paciente teve um protocolo aberto
    - Classe profissional responsável pela abertura do protocolo → Vínculo de todas as classes assistenciais, portanto todos da assistência podem identificar e abrir um protocolo
    - Classe profissional responsável pelo fechamento do protocolo → CRM. Apenas a equipe médica pode finalizar um protocolo sepse depois de aberto.

## **2.2 FORMULÁRIO**

A tela de formulário é o local que será realizado o cadastro de todas as seções e perguntas do protocolo, é o espelho do que o usuário final preencherá na tela do PEP. 

Para iniciar a construção do formulário o usuário deve registrar uma seção que pode contemplar 0 ou "n" perguntas referente a determinado processo do protocolo. Ao construir o formulário estruture por processos realizados pelos usuários finais e os seus responsáveis. 

Para adicionar uma nova seção é necessário preencher os campos:

Título - Campo obrigatório

Descrição - Trazer as ações ou pontos relevantes daquele processo

Perfil do profissional (Obrigatório) - Trazer quais profissionais podem realizar o preenchimento daquela seção

O usuário pode realizar um cadastro sem perguntas associadas através da ação "Finalizar seção" após preencher os campos obrigatórios da seção.

Após a criação de uma seção será aberta a possibilidade de atrelar as perguntas seguindo uma ordenação pré determinada. Para o preenchimento das perguntas temos os campos:

Descrição - Campo obrigatório. Trazer o nome da pergunta a ser apresentada no PEP

Tipo de campo - Qual tipo de campo será utilizado para a resposta ( Múltipla seleção, Seleção única, Data/hora, Longo e Curto)

Após adicionar uma pergunta o usuário pode optar por finalizar a seção ou adicionar outra pergunta.

As seções e perguntas finalizadas vão compor uma tabela com todos os registros adicionados (seção, perguntas e opções de resposta) e com as possibilidade de exclusão da seção ou da pergunta e adição de novas perguntas dentro de uma seção.

## **2.3 CONDICIONAIS**

A construção das condicionais tem como objetivo apresentar para o usuário final uma jornada inteligente, com abertura das seções para preenchimento conforme determinação das condicionais.

A associação sempre será realizada entre um item (resposta) da pergunta e uma seção, sendo obrigatoriamente uma seção posterior aquela que a pergunta está contida. 

**Exemplo de Preenchimento**

**Protocolo Dor Torácica**

* + - Seção 01 - Tipo de dor torácica
    - Pergunta 01 - Tipo de Dor torácica
    - Itens de resposta - **Dor típica**

Dor atípica

Dor atípica - provavelmente não aginosa

* + - **Seção 02** - Sala de emergência
    - Descrição - Encaminhar o paciente para sala de emergência
    - Pergunta 01 - Característica da dor
    - Itens de resposta - Dor opressiva ou sensação de pressão no precórdio ou retroesternal

Síncope / Pré síncope: perda súbida da consciência / tônus total (incluir PCR) ou abortada

* + - Pergunta 02 - Data e hora do início da dor

No item de resposta **Dor típica**deve-se criar uma condicional relacionada a seção 02 assim, quando o usuário final realizar o preenchimento da pergunta 01, com a resposta relacionada a dor típica ele será encaminhado para a seção 02 e na tela terá como descrição a ação que deve ser realizada: **Encaminhar o paciente para sala de emergência**e o preenchimento da característica da dor, data e hora do inicio.

## **2.4 VALIDAÇÕES**

As validações foram construídas com objetivo de assegurar um registro correto pelo usuário final, trabalhando como barreira para erros que no momento no registro das datas e horas da ações podem ocorrer e consequentemente "poluir" indicadores com registros imprecisos. 

Na aba de validações o usuário que estiver cadastrando o protocolo deve definir qual pergunta deve contar uma informação de data/hora maior, menor ou igual a outra pergunta. Também é possível criar a validação referente a um período ou data específica.

**Exemplo de Preenchimento**

**Protocolo Dor Torácica**

* + - **Seção 02** - Sala de emergência
    - Descrição - Encaminhar o paciente para sala de emergência
    - Pergunta 01 - Data e hora do acionamento médico
    - Pergunta 02 - Característica da dor
    - Itens de resposta - Dor opressiva ou sensação de pressão no precórdio ou retroesternal

Síncope / Pré síncope: perda súbida da consciência / tônus total (incluir PCR) ou abortada

* + - Pergunta 03 - Data e hora do início da dor
    - Pergunta 04 - Data e hora da avaliação médica

Neste caso, o registro referente a pergunta 01 -  **Data e hora do acionamento médico**deve ser maior que a pergunta 03 - **Data e hora do início da dor.** Também podemos criar a validação que a **Pergunta 03 - Data e hora do início da dor**deve estar contida dentro de um período de **1 dia.**

## **2.5 GATILHOS**

A construção dos gatilhos têm por objetivo criar uma dinâmica de abertura de protocolos no PEP que garantam maior assertividade pelo usuário final. Ao cadastrar os gatilhos de abertura teremos como garantia que o usuário final terá a ciência que dentro do perfil ou situação do paciente a instituição possui um protocolo a ser aplicado. 

Inicialmente os gatilhos vão estar atrelados ao preenchimento das funcionalidades:

* **Score**

Para o score é apresentado a listagens de todos os scores cadastrados no sistema e qual a margem de valor que será o gatilho para a abertura de um protocolo. 

Exemplo de cadastro: Score de Morse (Risco de Queda) para valores entre 25 - 45 realizar a abertura do Protocolo Risco de Queda.

* **Sinais Vitais**

Para os sinais vitais também é apresentado a listagens de todos os scores cadastrados no sistema e qual a margem de valor que será o gatilho para a abertura de um protocolo. 

* **Dispositivos**

Para os dispositivos é carregado todos os cadastrados realizados em **"Cadastro de Dispositivos e Equipamentos"**

Exemplo de cadastro: Sonda Vesical de Demora, todos os pacientes que tiverem o registro em controles de enfermagem de utilização da Sonda Vesical de Demora será aberto um protocolo de Risco de Infecção do trato urinário.

* **Triagem**

Para o cadastro de triagem é necessário trazer qual protocolo o gatilho está inserido e qual o grau de criticidade.

Exemplo de cadastro: Na triagem temos um protocolo da triagem relacionado ao AVC, onde todo paciente que apresenta determinados sinais/sintomas que pode ter como diagnóstico final o AVC teremos a criticidade estipulada para um atendimento de Emergência. Com o cadastro de gatilho podemos amarrar neste que para este paciente obrigatoriamente será aberto o protocolo de AVC institucional. 

**Parâmetro para realização de triagem antes do registro de atendimento:**

Para os usuários que realizam a triagem antes do registro de atendimento, ao finalizar o formulário de triagem será exibido uma notificação sempre que as informações registradas atenderem aos gatilhos configurados no protocolo. Essa notificação é apenas informativa e não interrompe o fluxo da triagem no painel.

Após a finalização do registro de atendimento do paciente e o início do atendimento no painel, o protocolo aberto durante a triagem ficará disponível no PEP, no menu “Protocolos assistenciais”, para visualização e preenchimento. Dessa forma, garantimos que o profissional tenha ciência da abertura e possa dar continuidade à análise e preenchimento no momento mais adequado.

* **CID**

Para os CID´s trazemos alguns protocolos a partir do momento que o CID é preenchido pelo médico na Anamnese

Exemplo: CID - Dengue, abertura do protocolo de dengue divulgado pelo ministério da saúde.

* **Faixa etária**

Para a faixa etária deve-se trazer os protocolos relacionados a determinada idade.

Exemplo de cadastro: Pacientes com faixa etária > 60 anos obrigatoriamente realizar a abertura do protocolo de Risco de Queda.

Para o cadastro de gatilhos é importante trazer as associados corretas, pra isso temos como condicional "E" ou "OU" entre dois fatores de abertura do protocolo. 

**Exemplo de Preenchimento**

**Protocolo Risco e Queda**

Escala de Morse alterada **E** faixa etária > 60 anos

4. Prontuário Eletrônico (PEP)

## **03. PRONTUÁRIO ELETRÔNICO**

No prontuário eletrônico encontramos na aleta lateral a funcionalidade Protocolos Assistenciais, neste agrupamento teremos o acesso para a abertura, preenchimento, finalização e visualização de todos os protocolos. Nesta tela inicial utilizamos como status dos protocolos:

* **Em andamento:** Protocolo foi aberto e iniciado o preenchimento
* **Pendente:** Protocolo foi aberto através de um gatilho de abertura porém, preenchimento não foi iniciado
* **Concluído:** Protocolo aberto, preenchido e finalizado como concluído
* **Erro de abertura:** Protocolo aberto, preenchimento realizado ou não e finalizado como abertura incorreta
* **Não pertinente ao caso clínico:** Protocolo aberto, preenchimento realizado ou não porém, finalizado após decisão que o paciente embora tenha critérios para o protocolo não condiz com o caso clínico. Exemplo: Paciente em fim de vida podem apresentar sinais para abertura de diversos protocolos porém, por decisão não será realizado abordagens.

Um protocolo clínico pode ser iniciado a partir de dois fluxos:

* **Abertura manual pelo usuários:** Profissional da saúde identifica a necessidade de seguir determinado protocolo para o paciente e através da funcionalidade Protocolos assistenciais é possível abrir um protocolo através da escolha do Tipo de protocolo ( Clínico, Cirúrgico, Segurança do Paciente), seleção do formulário a ser aplicado e registro a data e hora de abertura.

* **Abertura automatizada:** O protocolo é aberto de maneira automatizada com base nos gatilhos cadastrados dentro do protocolo. Neste fluxo o protocolo automaticamente é aberto e recebe o status de pendente na tela inicial, aguardando o preenchimento pelo conselho responsável.

Muitas vezes vamos ter o gatilho de abertura iniciado através do registro de um profissional que não possui a permissão para realizar o primeiro preenchimento, neste caso o protocolo ficará com status Pendente até que o primeiro registro seja efetuado. Exemplo: Técnico de enfermagem realiza o preenchimento do registro dos sinais vitais, estes registros são coerentes com o gatilho de abertura do protocolo Sepse porém, a primeira etapa do preenchimento é de responsabilidade do enfermeiro. Com o registro do técnico de enfermagem o protocolo será aberto automaticamente e ficará com status de Pendente até um profissional com registro de enfermeiro realize o primeiro preenchimento e o status é alterado para em andamento. 

## **3.5 GATILHOS**

Quando protocolo é iniciado através do registro de informações compatíveis com os gatilhos cadastrados para abertura de protocolo, uma modal será apresentada ao usuário com as opções de "preencher o protocolo" ou "finalizar protocolos", as ações estarão disponíveis de acordo com a permissão do usuário. 

Todo protocolo aberto por gatilho, tem o seu horário de abertura o horário que o usuário realizou o registro da informação do sistema e não o horário de execução, exemplo: Sinais vitais aferido 10h porém, registrado no sistema 12h. Horário de abertura do protocolo por gatilho será 12h. 

A funcionalidade não permite dois ou mais protocolos iguais abertos para o mesmo paciente, será necessário encerrar o primeiro para na sequência abrir os demais. A regra também é aplicada aos gatilhos porém, quando um protocolo está em andamento ou pendente e temos um novo gatilho é apresentado ao usuário final uma modal com as informações: Nome do protocolo, data de criação do protocolo já aberto e critérios de ativação.

## **3.6 ENVIO POR E-MAIL**

Os usuários com e-mail cadastrado para recebimento do protocolo serão notificados quando ocorrer a abertura do protocolo, independente de ser por gatilho de abertura ou manualmente.

O e-mail apresenta uma estrutura padronizada contendo as informações: Nome do protocolo aberto, tipo de alerta, informações com os dados do paciente e informações do protocolo. 

## **3.7 IMPRESSÃO**

Alerta Crítico

## **05. ALERTA**

**O cadastro e utilização dos alertas relacionados a protocolo assistencial encontra-se na documentação: <https://tdn.totvs.com/x/eqGcM>**
