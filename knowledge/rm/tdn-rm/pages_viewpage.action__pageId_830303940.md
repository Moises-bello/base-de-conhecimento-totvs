---
content_hash: 9a98402babb0817064c2f9a627d3f8c36600970a098099e44bc14652216971ad
fetched_at: '2026-06-29T00:11:48.949345+00:00'
page_id: '830303940'
product: rm
source: tdn-rm
title: Checagem.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=830303940
version: 27
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Itens para checagem**
4. **Dupla Checagem**
5. **Checagem de Hemocomponentes**
6. **Checagem de Sinais Vitais**
7. **Configurações RM**

ChecagemVisão Geral

## **01. VISÃO GERAL**

Recurso que permite ao usuário a realização da checagem dos itens prescritos e aprazados. Nesta tela estarão os itens da prescrição médica e prescrição de enfermagem. 

Exemplo de utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

Ao clicar no menu de "Processo de Enfermagem" e em "Checagem", será aberta a tela com os itens aprazados e pendentes de checagem da prescrição médica e de enfermagem.

* Selecione no combo de "Ciclo de prescrição" qual a vigência desejada para que os itens sejam exibidos na tabela.

* Após selecionar o ciclo, será exibido na tabela os itens prescritos numerados de acordo com a ordem de prescrição no momento da liberação da prescrição médica. Se após a liberação da prescrição o profissional acrescentar outro item, a lista seguirá a ordem numérica independente de qual a classificação ele estiver (Dieta, Medicamento, Soro e Componentes). Exemplo: A prescrição contém 10 itens, se após a liberação o médico acrescenta uma dieta, ele será contabilizado como o 11º item na lista.
* Para filtrar um item específico, insira o nome no campo de busca.
* Abaixo da lista será identificado o número total de itens prescritos e para exibir mais itens da prescrição, clique em "Carregar mais registros".
* Para exibir itens específicos utilize os filtros de status: **"Todos", "Próximo do horário", "Aprazados", "Executados"** ou **"Atrasados"** e clique no botão "Filtrar" para exibir o resultado.

| Filtros | Ação |
| --- | --- |
| **Todos** | Todos os status |
| **Próximo do horário** | Medicações a serem realizadas nas próximas 2h |
| **Aprazados** | Medicações aprazadas |
| **Executados** | Medicações já executadas |
| **Atrasados** | Medicações não realizadas até o horário de aprazamento |

* Quando ocorrer uma suspensão (na prescrição médica) de qualquer item pela equipe médica, o item ainda será apresentado na tabela com um ~~RISCO.~~

* Botão **"Opções Avançadas":**

* + Ao selecionar a opção **"Legendas"** é exibido uma modal contendo o significado de cada ícone dos status de um item na tabela de Planejamento Terapêutico, conforme imagem abaixo:

* + Ao selecionar a opção **"Visualizar prescrição"**, é exibido em uma nova guia um PDF contendo a descrição dos itens prescritos, dose, via, frequência e horários checados.

* + Ao selecionar a opção "**Reaprazar checagem",** será exibido na tela um modal para selecionar qual o item da prescrição o usuário deseja reaprazar, o intervalo e um campo obrigatório para descrever a justificativa do reaprazamento.
  + Ao clicar no botão **"Reaprazar"** será exibido um modal solicitando confirmação. Após a confirmação os itens serão exibidos na tabela de checagem com o status de **"Reaprazado"** .

 

Reaprazamento

O processo de reaprazamento **não reflete alteração no painel de dispensação da farmácia**, sendo necessário um alinhamento de processo interno do cliente.

Mantém-se a comunicação realizada no aprazamento inicial com os novos horários ao realizar a cópia da prescrição.

Entende-se que a funcionalidade de reaprazamento é utilizada em exceções e a construção será futura.

Itens para checagem

## **03.** **ITENS PARA CHECAGEM**

Ao abrir o menu de checagem, serão listados todos os itens da prescrição médica e de enfermagem pendentes de checagem. 

* Ao clicar no ícone de um item da tabela será exibido as opções de **"Checar"** e **"Reaprazar"**:

* Ao clicar em **"Checar"** será exibido um modal para checar o item selecionado. Neste modal encontramos as sessões para lançamento da data e hora da execução e um campo de observações/descrição da enfermagem. A validação da identificação do paciente poderá ser realizada através da leitura da pulseira, conforme parametrização no RM.
* Após o preenchimento, clique no botão **"Executar"** para finalizar a checagem.

* Ao clicar no botão **"Não executar"**, será exibido um modal solicitando uma justificativa (campo obrigatório) para a não execução. Após confirmar ação, ficará sinalizado na tabela o horário não executado com um ícone "X".
* Para visualizar o responsável por não executar ou pela suspensão, clique no ícone "X" e em seguida em "Checar", será exibido no modal o horário e o nome do profissional que realizou a ação.

* É possível **desfazer a checagem ou suspensão** clicando no ícone do item e em seguida em "Checar". Ao clicar no botão "Desfazer checagem" será exibido um modal solicitando uma justificativa (campo obrigatório) para a checagem desfeita.
* Após confirmar ação, no horário da checagem desfeita ficará sinalizado na tabela com o ícone "AP" (Aprazado - Pendente liberação) novamente.

* Ao selecionar a opção "**Reaprazar"** clicando no ícone do item,será exibido na tela um modal para selecionar o intervalo, os horários para alterar (clicando nas setas) e um campo obrigatório para descrever a justificativa do reaprazamento.
* Após confirmar ação, no horário reaprazado ficará sinalizado na tabela com o ícone "RP" e o novo horário com "AP".

Dupla checagem

## **04.** **DUPLA CHECAGEM**

A dupla checagem é um procedimento adotado pela equipe de enfermagem que envolve a verificação de informações por dois profissionais diferentes em alguns processos como na administração de medicamentos potencialmente perigosos, preparação e aplicação de terapias intravenosas, realização de procedimentos invasivos e no controle de transfusões sanguíneas.  Ao garantir que cada etapa crítica do processo seja verificada por mais de um profissional, a equipe de enfermagem minimiza a possibilidade de erros humanos que podem ter consequências graves para os pacientes. A dupla checagem é crucial para garantir a precisão e a segurança no atendimento ao paciente, promovendo uma assistência mais segura e eficaz.

Os Medicamentos Potencialmente Perigosos (MPP) ou de alta vigilância, conforme definidos pelo Instituto para Práticas Seguras no Uso de Medicamentos (ISMP Brasil), são aqueles com risco elevado de causar danos significativos se houver falhas no processo de utilização. Embora os erros com esses medicamentos possam não ser frequentes, suas consequências são geralmente mais graves, ocasionando danos permanentes ou mesmo a morte do paciente. O ISMP EUA e outras organizações de segurança recomendam que os profissionais de saúde conheçam esses riscos e implementem barreiras para prevenir erros.  Nos boletins publicados pelo ISMP Brasil, os MPPs são classificados por "classe terapêutica" (todos os medicamentos da classe são perigosos) ou "medicamentos específicos" (quando apenas alguns medicamentos da classe são perigosos). A identificação de pontos críticos em cada instituição auxilia na implantação de estratégias de prevenção adequadas à sua realidade. O cadastro das medicações utilizadas e consideradas como "Medicamentos Potencialmente Perigosos", dupla checagem e a utilização de alertas como barreiras de segurança do paciente serão cadastradas no RM.

Na tela de checagem, os medicamentos cadastrados como Medicamentos Potencialmente Perigosos no RM, serão exibidos com o alerta “**Alta vigilância”.**

Na tela de checagem, será exibido como título o nome da medicação e abaixo as tags conforme parametrizado no RM: **Diluir** e/ou **Via Endovenosa** e/ou **Dupla Checagem.**

Medicamentos classificados com a tag **“Via Endovenosa”** serão exibidos com o alerta: **“Este medicamento deve ser administrado somente Via Endovenosa. Fatal se administrado por outra via”.**

Quando o medicamento necessitar de dupla checagem, ao clicar em "Executar" uma modal será exibida com o campo de login e senha do segundo usuário a checar. A checagem será executada somente após a validação das informações do segundo usuário.

Após a checagem, ambos os profissionais serão exibidos como responsáveis pela checagem.

Checagem de Hemocomponentes

## **05.** **CHECAGEM DE HEMOCOMPONENTES**

A nova tela para checagem de hemocomponentes no PEP possibilita que a equipe de enfermagem possa registrar e monitorar a administração de hemocomponentes e garantir que seja feita de maneira segura e em conformidade com os protocolos hospitalares.

Na tela de checagem,  ao clicar em checar um hemocomponente, será exibido uma modal contendo como título o hemocomponente prescrito e abaixo as tags conforme parametrizado no RM. Abaixo estarão todos os campos necessários para a checagem de forma precisa e segura, composta por: 

1. Checkbox "Realizado a profilaxia conforme prescrição médica": A equipe de enfermagem poderá registrar se a profilaxia foi realizada conforme a prescrição médica, marcando este checkbox. Quando a profilaxia não for realizada, o checkbox não deverá ser marcado e um campo de texto livre ficará habilitado para descrever a justificativa da não realização. Quando o médico sinalizar que não foi prescrito profilaxia na modal de prescrição, este checkbox não será exibido em tela.
2. Data e Hora Inicial e Data e Hora Final: O usuário deverá inserir no campo a data e hora inicial e a data e hora final do procedimento de administração do hemocomponente. A hora inicial pode ser registrada de maneira retroativa mas não futura. A data e hora final deverá sempre ser menor que a inicial, podendo também ser registrado de maneira retroativa mas não futura.
3. Campos "Descrição do hemocomponente", "Tipo de hemocomponente", "Volume", "Tempo de infusão" e "Via de aplicação": Estes campos serão preenchidos automaticamente com as informações inseridas na prescrição médica correspondente.
4. Campos "Nº Bolsa de Sangue", "Tipo Sanguíneo" (com opção de preenchimento fixa: A, B, AB e O) e "Fator Sanguíneo" (com opção de preenchimento: Positivo ou Negativo): São campos para o preenchimento manual pela equipe de enfermagem.
5. Checkbox com opções relacionadas à segurança do paciente: A equipe de enfermagem poderá registrar marcando o checkbox correspondente se foram realizados os requisitos relacionados à segurança do paciente.
6. Campo "Observações / Descrição da Enfermagem": Campo de texto livre para anotações de observações e descrições da equipe de enfermagem sobre a administração do hemocomponente.

Para finalizar a checagem, clique no botão "Executar" para realizar a dupla checagem.

* Quando a utilização da dupla checagem estiver parametrizada para a unidade, a funcionalidade também estará habilitada para a checagem do hemocomponente.
* Ao abrir a modal de checagem de hemocomponentes, todos os campos devem ser preenchidos, exceto os campos "Data e Hora Final". Após a realização da dupla checagem, apenas os campos "Data e Hora Final" permanecem em branco neste momento. Quando a administração do hemocomponente for concluída, o profissional deverá retornar à tela e preencher o campo "Data e Hora Final".
* Após o preenchimento da data e hora final, a tela não permitirá a edição dos campos preenchidos anteriormente. Se o profissional optar por desfazer a checagem após a finalização da administração, todos os campos preenchidos serão excluídos e o profissional precisará preencher novamente todos os campos da tela e realizar uma nova dupla checagem com outro profissional.
Checagem de Sinais Vitais

## **06.** **CHECAGEM DE SINAIS VITAIS**

A nova funcionalidade para a checagem dos sinais vitais permite que a equipe de enfermagem registre as informações relacionadas à aferição de sinais vitais durante a administração de medicamentos e hemocomponentes de forma precisa e segura.

Na tela de checagem, será exibido na linha abaixo em que o medicamento ou hemocomponente estiver listado, a legenda dos sinais vitais conforme a cadência de horário padronizada no cadastro do RM, indicando os sinais vitais a serem aferidos e os horários correspondentes.

Ao clicar no ícone dos sinais vitais, uma modal relacionada aos controles de sinais vitais será exibida. Na modal, o usuário poderá realizar o preenchimento dos sinais vitais e salvar as informações inseridas.

Após o preenchimento dos sinais vitais, o usuário poderá visualizar ou editar as informações registradas clicando novamente no respectivo ícone "SSVV". Os sinais vitais registrados na tela de checagem também são registrados na tela de Controles de Enfermagem.

Após a finalização da administração do medicamento ou hemocomponente, os usuários poderão apenas visualizar ou excluir os sinais vitais registrados.

Se o usuário optar por excluir os sinais vitais, o sistema manterá um histórico da exclusão na tela de **Controles de Enfermagem** e dará a possibilidade de realizar um novo registro. Caso o usuário apenas exclua os sinais vitais sem registrar novas informações, os sinais vitais serão marcados como "não realizados", sem registro de checagem.

Configurações RM

## **07.** **CONFIGURAÇÕES RM**

1. **Cadastro de Medicamentos Potencialmente Perigosos (MPP) e parametrização de alertas de segurança:** RM > Cadastros > Cuidados com o Paciente > Processo de Enfermagem > Cadastro de Dupla Checagem.

* Para filtrar um item específico, descreva o nome do item no campo de busca e clique em "Filtros". Para alterar a exibição das colunas na tabela, clique em "Gerenciar tabela":

* Para iniciar o cadastro da medicação clique no botão **"+ Incluir"**. Será exibido uma tela com as opções para incluir a classe terapêutica e o princípio ativo. Ao selecionar cada classe é possível incluir os medicamentos vinculados a ela (princípio ativo).
* Dentro de cada produto vinculado existe a possibilidade de parametrizar os alertas: **"Diluir antes de administrar"**, **"Uso somente por via endovenosa"**, **"Alta Vigilância"** e **"Dupla checagem"**.  Para finalizar a inclusão, clique no botão **"Salvar"**.

* **A parametrização de dupla checagem será realizada em:** RM > Cadastros > Unidade atendimento > Prontuário Eletrônico > Aprazamento / Checagem > Checagem de medicamentos > "Habilita a dupla checagem por princípio ativo / hemocomponentes".
* Também é possível definir alguns parâmetros para comportamento do sistema nesta aba:

****2. Cadastro das cadências para a avaliação dos sinais vitais:****

RM > Cadastro > Prescrição médica > Padrão de prescrição > Selecionar princípio ativo >  aba Padrão de prescrição > Selecione a apresentação >  aba Padrão de prescrição > Selecione um padrão > Aferição de Sinais Vitais.

Ao clicar em buscar no campo "Aferição Sinais Vitais", o usuário poderá incluir ou editar um padrão de cadência. Na modal de inclusão será necessário preencher na aba "Identificação" os campos: "Descrição", "Tempo máximo em minutos" e "Frequência".

O cadastro inclui campos para o nome da cadência e seleção do período de tempo total da cadência. Por exemplo: Item A deverá ter a aferição de sinais vitais nas primeiras 2 horas de administração, então o tempo total da cadência será de 2 horas.

A "Frequência" cadastrada deve estar associada apenas a última ordem e não deve ser possível ter frequência em duas ou mais ordens.

É possível adicionar intervalos de avaliação à cadência, especificando o tempo inicial, tempo final e a frequência de avaliação dos sinais vitais durante cada intervalo. É possível também adicionar frequências sem seguir o mesmo intervalo, podendo cadastrar até 5 cadências. Os intervalos de avaliação são configuráveis e permitem uma variedade de frequências, como minutos, horas etc.

Na aba "Ordens", será necessário incluir cada "Tempo em minutos", referente ao horário de checagem do item. As ordens cadastradas sempre são referentes ao horário de administração, portanto devem estar em ordem crescente (A ordem cadastrada sempre deve ser maior que a anterior pois a referência é o horário da checagem).

## **Exemplo prático!**

**Item para checagem:** 1 bolsa de hemocomponentes.

**Protocolo do hospital:** aferir sinais vitais quando realizar a checagem, em 15 minutos e 40 minutos após início da infusão e depois de 1h/1h após início da infusão até a finalização, completando período máximo de 4 horas.

**O cadastro das ordens seria:**

1º ordem - 0 min (no momento do horário de checagem = Início)

2º ordem - 15 min (após horário inicial da checagem)

3º ordem - 40 min (após horário inicial da checagem)

4º ordem - 1h (após horário inicial da checagem)

Frequência após a última ordem - 1h/1h

Tempo Total - 4h

**Na tela de checagem no PEP,** os ícones indicando necessidade de aferição estariam inseridos nos seguintes horários:

Horário de checagem inicial do hemocomponente: 12h

**Horários de checagem dos sinais vitais:** 12h / 12h15 / 12h40 / 13h /14h /15h /16h
