---
article_id: 360050181214
category: RH - Lançamentos
content_hash: 15b7757d566d9219ce6a353e328845190ac28aa90e26741efc3dae5d37d698f7
fetched_at: '2026-06-28T22:44:46.852832+00:00'
product: protheus
section_id: 32419271673111
source: central-protheus
title: RH - Linha Protheus - PON - Configuração para apuração de Horas Sobreaviso
type: support-article
updated_at: '2025-10-23T20:51:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050181214-RH-Linha-Protheus-PON-Configura%C3%A7%C3%A3o-para-apura%C3%A7%C3%A3o-de-Horas-Sobreaviso
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31775388391959) Tempo aproximado para leitura: 00:01:30 min****

**Dúvida**Configuração para pagamento de **horas Sobreaviso.**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**

A rotina **Horas de Sobreaviso (PONA425)**, acessada pelo caminho **Atualizações > Cadastro de Funcionários > Sobreaviso**, é responsável pelo **cadastro dos períodos em que o funcionário permanecerá em sobreaviso**.  
Com base nessas informações, o sistema realizará o **apontamento automático das marcações**, gerando o **evento de Horas de Sobreaviso** por meio do **ID de ponto 044A**.  
  
Além do evento de **Horas de Sobreaviso**, foram criados **três novos identificadores de cálculo** no **Ponto Eletrônico** com o objetivo de permitir a **separação das horas extras realizadas durante o período de sobreaviso**.  
Esses identificadores possibilitam distinguir de forma mais precisa os diferentes tipos de horas extras ocorridas dentro desse contexto. Os identificadores de HE Sobreaviso são:  
**049A – Hora Extra Sobreaviso****050A – Hora Extra Sobreaviso Noturna****051A – Adicional Noturno HE Sobreaviso**Esta funcionalidade descrita está liberada no pacote de **[expedição contínua do RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)** a partir de **26/03/2021** e, além de aplicar o patch, será necessário executar o **UPDDISTR** com o dicionário diferencial para a criação da tabela e grupos de perguntas.

Ao rodar a atualização do dicionário criará uma nova tabela para armazenar o cadastro de sobre aviso: **RRS - Sobreaviso.** Criará, também, o grupo de perguntas **PONA425 para a execução da inclusão em lote.** Para saber mais detalhes técnicos acesse o link a seguir na aba **'Informações Técnicas': [Documentação Técnica](https://tdn.totvs.com/pages/releaseview.action?pageId=604832353)**Caso seja necessário, segue os passos para incluir manualmente a rotina no [**menu do SIGAPON**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000575567-Framework-Linha-Protheus-Personaliza%C3%A7%C3%A3o-de-Menus?source=search) através do **Configurador(SIGACFG): Ambiente>Cadastros>Menu**, conforme exemplo abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32844175881367)  
  
Antes de prosseguir com o cadastro de Horas Sobreaviso, faça a validação dos cadastros de eventos, em Atualizações-Cadastro do Ponto-Eventos, deverá ter os cadastros relativos aos ID'S abaixo:  
**044A – Hora de Sobreaviso****049A – Hora Extra Sobreaviso****050A – Hora Extra Sobreaviso Noturna****051A – Adicional Noturno HE Sobreaviso  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35843136535831)**  
  
Ao acessar a rotina **Horas Sobreaviso, em Atualizações-Cadastro do Ponto-Horas de Sobreaviso,** é apresentado no *browse* a listagem dos funcionários. Para cadastro por funcionário basta selecionar o funcionário e clicar em "**Manutenção**" **![](https://centraldeatendimento.totvs.com/hc/article_attachments/35843094624919)**Ao clicar em manutenção é apresentada a tela para inclusão dos períodos de sobreaviso.

- Na parte superior, temos as **informações do funcionário**, com matrícula e nome.

- Na parte inferior, o **cadastro dos períodos de sobreaviso**, contendo os campos: **Data Inicio e Data Final**, para determinar o períodos em dias, **Hora Inicio e Hora Final**, para indicar qual período do dia o funcionário estará de sobreaviso e **Dias,** onde são selecionados os dias da semana nos quais os horários são válidos.  
  
Segue abaixo um exemplo de como a seleção por dias facilita o cadastro.  
No exemplo, o funcionário ficará de **sobreaviso** nos dias de **segunda à sexta dos dias** de **20/10 à 24/10,** em cada dia respeitando o horário das **07h as 23h;**

Dentro do período de **20/10 a 24/10**, os horários funcionarão conforme configurado para cada data/dia, da seguinte forma:  
**20/10** → das **07h00 às 23h00****21/10** → das **07h00 às 23h00**E assim por diante.  
  
No caso de **sobreaviso**, o sistema **não atua da mesma forma que na tabela de horários padrão (escalas)** — ou seja, não busca horas consecutivas, como ocorre em escalas noturnas, por exemplo.

Este tipo de cadastro **não tem a mesma funcionalidade da montagem de calendário de escalas ou jornadas de trabalho**.  
  
A finalidade desta configuração é definir o período de **Horas de Sobreaviso** do funcionário, aplicando-o dia a dia dentro do intervalo de datas e horários informados.  
Por esse motivo, **não recomendamos cadastrar horários que ultrapassem o limite do dia**, para evitar interpretações incorretas pelo sistema.

**Exemplo:**  
Se for informado o período de **20/10 a 24/10**, com **hora inicial às 22h** e **hora final às 05h do dia seguinte**, o sistema aplicará esse intervalo **em cada data** dentro do período selecionado.  
**20/10** → das **22h00 às 05h00****21/10** → das **22h00 às 05h00**E assim por diante.  
  
Segue um exemplo de Horas Sobreaviso cadastrado:  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/35843094627863)**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/35843094628375)**Além da rotina **Horas Sobreaviso** do cadastro por funcionário, foi disponibilizado também a opção de **inclusão em lote**, acessando em **Outras ações-Inclusão em Lote**,onde é apresentada uma tela com as perguntas para filtro dos funcionários (A), assim como as informações necessárias para o cadastro da rotina (B). Ao executar essa opção o sistema irá cadastrar o **sobreaviso** para todos os **funcionários** que atenderem aos filtros e gerará um log com as matriculas selecionadas.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35843094630167)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35843136543511)  
  
Ao término do processamento é apresentado um log demonstrando para quais funcionários foi feita a inclusão:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31775358797463)  
  
Para **utilização das horas de sobreaviso**, após o cadastro dos horários que serão considerados, é necessário cadastrar um evento com Identificador de Ponto **044A - Horas de sobreaviso**. Esse evento **deve estar associado a uma verba da folha em horas**, cadastrado com o percentual que deverá ser pago sobre o salário de cada hora realizada em**atualizações>cadastro do ponto>eventos**, clique em incluir e crie o evento amarrando ao **ID de ponto 044A**, exemplo:![](https://centraldeatendimento.totvs.com/hc/article_attachments/19433218834967)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19433218855319)  
Veja o exemplo de uma jornada das 08h00-12h00-13h00-18h00:  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/35843094632215)**No exemplo, o funcionário ficará de **sobreaviso** nos dias de **segunda à sexta dos dias** de **20/10 à 24/10,** em cada dia respeitando o horário das **07h as 23h;**Calculando o seguinte:  
**Das 07h as 08h->01h Sobreaviso  
Das 08h às 12h e das 13:30 as 18h->08:30 de falta  
Das 18h as 23h->05h Sobreaviso**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/35843094634007)**  
  
Caso ele não vá trabalhar, gerará falta e as horas de Sobreaviso, veja abaixo:  
**Obs.**Na eventual necessidade do funcionário ficar o dia inteiro de sobreaviso em um dia que ele deveria trabalhar, deve ser criada uma [exceção](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006080521-RH-Linha-Protheus-PON-Como-cadastrar-Exce%C3%A7%C3%A3o-por-Per%C3%ADodo-para-deixar-o-dia-N%C3%A3o-Trabalhado?source=search) para que o dia seja considerado não trabalhado.  
  
Com a exceção no dia não trabalhado, gerará só as horas totais de sobreaviso:  
**Das 07h as 23h=16h Sobreaviso**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35843136549015)  
  
Da mesma forma, considerando o mesmo horário e sobreaviso cadastrado anteriormente, se o funcionário realizar horas extras das das 18:00 às 19:00, veja exemplo abaixo:  
**Das 18h as 19h=01h HE Sobreaviso**  
**Das 07h as 08h=01h Sobreaviso**  
**Das 19h as 23h=04h Sobreaviso**  
**Total 05h Sobreaviso**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/35843094636311)**Caso realize os horas extras noturna, veja o resultado:  
**Das 07h as 08h=01h Sobreaviso  
Das 18h as 22h=04h HE Sobreaviso**  
**Das 22h as 23h=01h HE Sobreaviso Not****Das 22h as 23h=01h Adic Not HE Sobreaviso****![](https://centraldeatendimento.totvs.com/hc/article_attachments/35843094638487)****Observação:** Devido a peculiaridades do processo para gerar as horas que efetivamente foram de sobreaviso, em detrimento das que foram trabalhadas ou pagas como hora extra, **esta implementação não é utilizada no caso de horário móvel. Para este caso as horas de sobreaviso devem ser lançadas manualmente na folha.**Foi disponibilizado também o **[Relatório de horas Sobreaviso.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406219008535-RH-Linha-Protheus-PON-Como-gerar-o-relat%C3%B3rio-de-Horas-Sobreaviso?source=search)****Saiba mais:**[Como apontar as Horas Extras e Adicional noturno Sobreaviso](https://tdn.totvs.com/pages/releaseview.action?pageId=983813526)  
[Apuração de Horas Sobreaviso](https://tdn.totvs.com/pages/releaseview.action?pageId=604832353)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download?e=1080347)
