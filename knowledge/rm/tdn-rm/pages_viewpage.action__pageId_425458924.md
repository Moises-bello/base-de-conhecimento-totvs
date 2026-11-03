---
content_hash: 18c22043bc394abdfd64610b4f94ec6b228e1a61a5d8b9de0f6361f8ece7e706
fetched_at: '2026-06-29T00:09:32.809543+00:00'
page_id: '425458924'
product: rm
source: tdn-rm
title: Área de Interesse Ofertada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458924
version: 56
---

É por meio desse cadastro que é disponibilizada as opções ou áreas de interesse de um processo seletivo. Este cadastro é controlado por filial e por período de calendário (do processo seletivo), ou seja, se iniciar o período de seleção no calendário não será possível alterar dados deste cadastro. Esse cadastro se divide em 7 guias:

**1- Identificação**  
Compreende informações básicas que identificam uma área de interesse ofertada em um processo seletivo.  
Área de interesse: deve ser selecionada uma área de interesse a ser ofertada que exista na tabela auxiliar "Área de Interesse Disponível". Nº de vagas: é o número de vagas do processo seletivo, caso o processo seletivo utilize controle de vagas, este será o valor que o sistema irá utilizar para validar a quantidade de vagas da área de interesse ofertada para permitir ou não mais inscrições ou se irá considerar os candidatos como excedentes caso o número de vagas seja preenchido.

**Observação**: caso o processo seletivo utilize controle de vagas excedentes e o número de vagas for alterado para um valor menor que o número de candidatos inscritos já existente, o sistema irá emitir um alerta sobre a impossibilidade da redução do número de vagas. Á partir da versão 12.1.34 será permitido criar uma área ofertada com 0 vagas, neste caso, todas as inscrições serão excedentes e somente serão alteradas para inscritos quando o número de vagas for incrementado.

Informações

Caso o processo seletivo esteja fora do período de inscrição, exista candidatos excedentes e seja feito o aumento do número de vagas da área ofertada, o sistema irá emitir um alerta informando que o aumento do número de vagas nesta situação não irá fazer com que candidatos excedentes se tornem inscritos, neste caso deve ser executado o processo "Alterar candidatos excedentes para inscritos" (Informações no final da página).

* Mínimo de inscrições: esta informação está diretamente ligada ao processo "Cancelar Área Ofertada". O valor não impede que nenhum processo seja executado, funcionando mais como um indicador no qual a instituição irá se basear para decidir se seguirá com a seleção para a área ou se irá cancelá-la.
* Máximo de opcionais: limita o número de opções secundárias que o candidato poderá escolher no momento da inscrição se ele informar esta área de interesse como primeira opção.
  + Caso seja utilizado mais de uma área ofertada, é interessante utilizar o parâmetro "Utilizar o controle de chamada de uma única área ofertada por candidato, respeitando a ordem de prioridade", para mais informações acesse: .

Inscrições

A partir da versão 12.1.2205 foi disponibilizado no cadastro da área de interesse ofertada a possibilidade de definir um período de inscrição.

Caso o período não seja preenchido será mantida a regra que considera o período de inscrição do processo seletivo.

Para saber mais sobre inscrição clique em: [Regras para habilitar a inscrição](https://tdn.totvs.com/pages/viewpage.action?pageId=678587180)

**Itinerário formativo**

Os itinerários formativos são o conjunto de disciplinas, projetos, oficinas, núcleos de estudo, entre outras situações de trabalho, que os estudantes poderão escolher no ensino médio. 

Portanto, poderá ser parametrizado quais itinerários formativos serão ofertados na inscrição do candidato.

A funcionalidade ficara disponível apenas para o processo seletivo do ensino básico, que esteja com o parâmetro "utiliza novo portal de inscrições" habilitado.

Para processo seletivo do tipo "Venda Online" os dados referente a itinerário formativo não serão apresentados, pois esta configuração não se aplica para esse tipo de processo.

Os itinerários serão exibidos se estiverem cadastrados no curso/serie/ turno de acordo com a parametrização informada na área de interesse. Para mais informações sobre itinerário formativo, acesse: .

Os campos mínimo e máximo refere-se a quantidade de itinerários que o candidato pode selecionar para realizar a inscrição.

**2- Informações Complementares**

Compreende informações adicionais relevantes na definição de uma área de interesse ofertada.

Idiomas Oferecidos: Nº Máximo e Nº Mínimo: define a quantidade máxima e mínima de idiomas para relacionar à prova de língua estrangeira da área ofertada.

Ex: Se o número mínimo de idiomas for= 0 e o máximo = 5, então deverá ter pelo menos 5 opções de idiomas ofertados para 1 deles ser escolhido pelo candidato para a prova de língua estrangeira.  
Incide desconto: se estiver marcada, as configurações de desconto que forem parametrizadas na forma de inscrição escolhida serão aplicadas. Se não estiver marcada, a taxa de inscrição definida na guia identificação será cobrada integralmente independente da forma de inscrição escolhida.

Utiliza ENEM: se esta opção estiver marcada, a nota de ENEM do candidato poderá ser utilizada na classificação. A utilização de ENEM também impacta no serviço de inscrição do Portal, caso esteja marcada estará disponível para preenchimento.

Utiliza controle de faixa etária: este parâmetro permite que o usuário defina se uma determinada área irá "Utilizar controle de faixa etária". Quando essa opção for marcada, obrigatoriamente o usuário informará também a data de nascimento mínima e máxima dos candidatos que poderão se inscrever na área ofertada. A partir desta parametrização, sempre que um candidato se inscrever a sua idade será consistida dentro da faixa etária.

Fórmula de resultado: permite que seja selecionada uma fórmula personalizada a ser aplicado no processo "Classificar Candidatos".

**3- Informações Financeiras**  
A guia possui o campo utilizado para configuração da conta/caixa que será informada na geração do lançamento no momento da inscrição.

A conta/caixa, de maneira geral, consiste nas informações referentes à conta, agência e banco que receberão as movimentações financeiras geradas nas inscrições do processo seletivo.  Esse campo é opcional na área de interesse ofertada. Caso não seja preenchido, o sistema utilizará a informação cadastrada da conta/caixa do processo seletivo, localizada nas informações financeiras. Testar geração de lançamento: através deste recurso será possível simular a geração de lançamento de inscrições do processo seletivo para esta área ofertada utilizando a conta/caixa da mesma. Caso não seja configurada a conta/caixa na área ofertada, as configurações financeiras utilizadas serão as do processo seletivo.

**4- Termo Aceite**   Define o texto que contém o termo de aceite que os candidatos deverão visualizar quando finalizarem suas inscrições na área ofertada. O termo de aceite é um mecanismo legal para salvaguardar a instituição nos processos de inscrição em que acha desacordo entre as partes envolvidas (instituição e candidato). Esta informação não é obrigatória, pois a instituição pode não querer exibir um termo de aceite. Caso este seja definido ele será exibido na última etapa do processo de inscrição via web e poderá ser emitido no relatório de comprovante de inscrição do processo seletivo.

**5- Documento**  
Permite que o usuário defina um ou mais documentos que os candidatos concorrentes à área deverão apresentar. Os candidatos poderão ver, através do Portal, os documentos que ainda estiverem pendentes de entrega por eles. Para cada documento será necessário informar: Os tipos de documento a partir da lista existente na tabela auxiliar do Totvs Educacional "Documentos". Se a opção Obrigatório for marcada esta informação afetará o processo "Alocar Candidatos em Locais de Provas".  O processo não irá alocar os candidatos que não apresentaram todos os documentos obrigatórios, a menos que, na configuração do "processo" o campo "Aloca sem documentação exigida" tenha sido marcado.

**6- Idioma Ofertado**   
Nessa guia deverá ser criada a lista de idiomas a serem disponibilizados para escolha dos candidatos que optarem por essa área ofertada. A quantidade de idiomas a serem incluídos na lista dependerá do valor informado para o campo "Idiomas oferecidos - Nº mínimo" da guia "Informações Complementares".

**7- Etapas**  
É por meio dessa guia que será possível parametrizar a fase de seleção para cada uma das áreas de um processo seletivo. As etapas ocorrem durante o período de seleção de um processo seletivo. Cada etapa poderá acontecer em diversos horários ao longo de um ou mais dias. Em cada horário de uma etapa será aplicado um conjunto de provas. Para cada etapa será necessário definir um nome, provas e horários em que ela ocorrerá. Para cada um dos horários de uma etapa, além da sua data, hora de início e término, deverá ser incluída uma lista das provas que serão aplicadas. Cada prova deverá receber configurações únicas. Estas informações estarão em cadastros anexados a Etapa.

Para garantir a consistência entre as etapas de uma área ofertada são aplicadas as regras abaixo durante o salvamento: Em uma mesma área ofertada/Etapa os horários não podem se sobrepuser. O 1º horário deverá ser definido e após o 1º acontecerá o 2º, o 3º após o 2º e assim por diante: Ex: 1ª horário de 12 h às 13 h do dia 01. O 2º horário terá que começar obrigatoriamente após às 13 h do dia 01, podendo ser em qualquer horário do dia 02, 03, etc.

Em uma mesma área com mais de uma etapa, deverá existir coerência cronológica entre elas. Ex: O primeiro horário da 2ª etapa deverá ser posterior ao término do último horário da 1ª etapa e assim por diante.

O primeiro horário de uma etapa determina a sua ordem dentro do conjunto de etapas de uma área ofertada. Assim a 1ª Etapa de uma área ofertada é aquela que inicia antes de todas as outras e assim por diante. Sempre que uma área ofertada é salva o sistema redefine a seqüência de etapas com base nessa regra. Para que uma etapa seja considerada a 1ª Etapa de um processo seletivo não basta que seu campo "Nome da Etapa" esteja escrito "1ª Etapa". É preciso que ela realmente tenha seu horário inicial anterior a todos os outros horários de prova. A ordem da etapa será mostrada na visão e na edição da etapa.

Importante

As datas e horários das etapas são meramente informativos para controle interno das instituições, não tendo ação nenhuma sobre as etapas do processo seletivo.

***Impactos*:**

 A alocação de candidatos ocorrerá por etapa. Na lista de cada forma de alocação estarão presentes as etapas de acordo com o que foi configurado para as áreas ofertadas do processo seletivo. Se o processo seletivo contiver mais de uma etapa, a alocação para a 2ª etapa e consecutivas ocorrerão apenas para candidatos já classificados que estejam com status "Classificado para próxima etapa". Caso contrário, se contiver somente uma etapa, a alocação ocorrerá normalmente verificando se o candidato está com status "Inscrito para seleção".

No local de prova do candidato ao salvar uma alocação manual, será verificado se o local comporta somente naquela etapa que o usuário deseja alocá-lo e só será possível alocar um candidato para a 2ª etapa se ele estiver com o Status "Classificado para a próxima etapa" na 1ª seleção e assim por diante.

Para Classificar o candidato sempre será verificado em qual etapa ele se encontra (casos para mais de uma etapa na área ofertada e classificação por Nota).

Se ele estiver na última etapa prevista para sua área ofertada então seu status será alterado para "Classificado para chamada". Senão, se houver outras etapas seu status será alterado para "Classificado para a próxima etapa".

Se a área ofertada já tiver sido classificada anteriormente e ocorrer nova classificação, a ordem de classificação dos candidatos já classificados será mantida. Os novos candidatos classificados terão ordem de classificação a partir da ordem do último candidato classificado nos processamentos anteriores.

No cancelamento da Alocação, Cancelamento da distribuição de provas e Cancelamento de Classificação será feito por etapa.

Em Inscrições-Resultados na área privada do Portal aparecerá o campo "Etapa Realizada" preenchida somente após a classificação de alguma Etapa ter ocorrido.

Em Resultados Gerais divulgado na área publica do Portal, se o processo seletivo possuir área ofertada com mais de uma etapa, será mostrada então a lista de seleção por etapas. O usuário pode optar para que a montagem da lista seja por ordem de classificação ou alfabética.

Importação de Gabaritos: Apenas será capaz de identificar as provas de um candidato se o campo IDETAPA for informado corretamente no arquivo de importação. Este código é visível somente por Select no banco de dados.

Registro de presença de candidatos: Se a área ofertada em que um candidato se escreveu possuir mais de uma etapa, ao clicar no sinal de mais  que fica ao lado do candidato, aparecerão todos os dias destas etapas, sendo possível registrar a presença ou falta por etapa.

**8- Local de prova**

Informações 

Esta funcionalidade está disponível à partir das versões ***12.1.2306.***

Ao realizar o cadastro da Área Ofertada estará disponível a opção: **"Usa local de prova online"**. Esta opção informa se essa área utilizará local de prova online e caso seja selecionada o sistema vai adicionar o local disponível automaticamente, desde que exista cadastrado nas tabelas auxiliares, um local que seja local de prova online. Dessa forma, o candidato no portal não precisará selecionar um local de prova e essa parte será transparente para ele.

Somente será cadastrado um local disponível de prova online para o processo seletivo e todos os candidatos dessas áreas ofertadas, serão alocados, nesse local.

Assim que for finalizar a inscrição, seja pelo portal ou pelo desktop, esses candidatos que escolheram áreas ofertadas que usam prova online e tenha etapa cadastrada, serão alocados automaticamente no local disponível de prova online.

Para mais informações acesse: 

Informações 

A partir da versão **12.1.2410.299,** caso existam candidatos inscritos no processo seletivo para a área de interesse, não será possível alterar a opção **"Usa local de prova online".**

**9- Distribuir prova**

Informações 

Esta funcionalidade está disponível à partir das versões ***12.1.27.288***, ***12.1.28.200*** e ***12.1.29.125***, mediante a execução dos scripts disponibilizados no "***RM.Atualizador.exe***".

Este recurso permitirá a alocação em um local de prova e distribuição do caderno de provas juntamente com o processo de envio de e-mail de forma automática após efetuar a inscrição de um candidato no processo seletivo. Após a inscrição ser concluída com sucesso, o caderno de provas estará distribuído, o candidato estará alocado e um local de prova e um e-mail contendo os dados da prova para execução através do TOTVS Educacional | Módulo: Avaliação e Pesquisa estará no e-mail do candidato. Este recurso está disponível para os processos seletivos que utilizem o novo portal de inscrições.

Esta funcionalidade é um facilitador para que o candidato receba o código gerado para executar a prova logo após sua inscrição, ou seja, esta funcionalidade agrupa os processos de "Alocar candidatos em locais de prova", "Distribuir caderno de prova" e "Enviar e-mails".

*Leia mais sobre a[Confirmação de Inscrição](https://tdn.totvs.com/pages/viewpage.action?pageId=425458310).*

Para a correta execução destes processos que integram esta funcionalidade, algumas definições são necessárias:

* O processo seletivo deve utilizar o novo portal, não ser do tipo venda online de cursos  e o campo e-mail do candidato deve estar visível e obrigatório (parâmetros do processo seletivo).
* O preenchimento dos campos de "Assunto do e-mail" e "Texto do e-mail" são obrigatórios.
* Devem existir locais de prova aptos a receber candidatos com e sem deficiência.
* Estes locais de prova devem ter  vagas suficiente para o volume de candidatos esperado no processo seletivo.
* As áreas ofertadas do processo seletivo devem ter pelo menos uma etapa com pelo menos uma avaliação do TOTVS Educacional | Módulo: Avaliação e Pesquisa vinculada.
* Os parâmetros globais de envio de e-mail devem estar configurados e funcionais.

Importante

Caso ocorra alguma falha em um dos processo, a inscrição não será efetuada.

Ao se utilizar o recurso "***Distribuir prova***"**,**será **obrigatória** a criação de uma etapa, na área ofertada, com uma prova do ***TOTVS Educacional | Módulo: Avaliação e Pesquisa***.

Serão disponibilizados, junto a aba "***Identificação***" na tela "***Provas da etapa***" dois campos para definição de algumas configurações possíveis para a execução da prova:

* Limite para a realização da prova (dias)
  + Define que o candidato tem um prazo de até X dias para iniciar a avaliação, à partir do momento de sua inscrição, ou seja, se ele de inscreve no dia 20/07/2020 às 13:15 e foi definido 3 dias no limite para iniciar a prova, ele tem até 23/07/2020 às 13:15 para iniciar a prova, após esse dia e horário a prova não poderá mais ser executada.
* Tempo limite para a finalização da prova (minutos)
  + Define a duração para finalização da prova, após seu início.

Essas parametrizações serão utilizadas na configuração do ambiente do Executor para a execução da prova online. O candidato terá um prazo para a finalização da prova e essas informações poderão ser enviadas por e-mail ( [Processo de envio de](https://tdn.totvs.com/x/f-1bGQ)[e-mails](https://tdn.totvs.com/x/f-1bGQ) ).

O parâmetro relacionado ao limite de dias para a execução da prova não é obrigatório quando a prova informada já possui um período cadastrado. Para esses casos, será sempre considerado o último período, caso a prova tenha mais de um cadastrado. Quando o período cadastrado não tiver uma data válida ou a prova não tiver um período cadastrado, o campo com limite para iniciar a execução da prova, no Processo Seletivo, será obrigatório.

Dessa forma, ao se notificar o candidato com as informações da prova será considerada a data final do último período cadastrado para a prova ou a data limite com os dias parametrizados na etapa do processo seletivo, que seria a data de sua confirmação de inscrição somado os dias de limite para a sua finalização.

*Leia mais sobre o* [período da prova](https://tdn.totvs.com/x/EPxbGQ).

Na utilização da matrícula através do portal é necessário que exista um usuário de código “***RMProcessoSeletivo***” cadastrado.

Esse cadastro pode ser realizado através do menu “***Serviços Globais | Segurança | Usuários***”.

Esse usuário precisa de acesso ao processo de envio de e-mails e, se for utilizada a contabilização na geração de lançamentos é necessário que ele tenha acesso ao período contábil para a geração de lançamentos contábeis.

Permissão:  
*Processo Seletivo | 04 Processos | 04.01 Utilitários e administrativos | 04.01.06 Processos administrativos | 04.01.06.02 Enviar e-mails*

 Anexos

---

 Processos

---
