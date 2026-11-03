---
article_id: 17143292484759
category: ACOMPANHA CUSTOS - JORNADA DE FECHAMENTO (NOVO)
content_hash: 460878a25b374bcefee185a7497f8c0afdba55bee397f8e0f83fdae063cad442
fetched_at: '2026-06-28T22:38:48.209177+00:00'
product: protheus
section_id: 5367899706647
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA038 - Como realizar
  o novo fechamento de estoque na rotina Acompanha Custos?
type: support-article
updated_at: '2026-06-26T13:59:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17143292484759-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA038-Como-realizar-o-novo-fechamento-de-estoque-na-rotina-Acompanha-Custos
---

O artigo explica o processo de fechamento de estoque na rotina Acompanha Custos do TOTVS Protheus, detalhando tipos de custos, rotinas envolvidas, parametrizações, validação de saldos, dados gravados e possibilidade de reabertura de períodos. Destaca a importância dos parâmetros MV\_ULMES, que deve ser exclusivo por filial para evitar erros, e MV\_DBLQMOV, usado para bloquear movimentações durante o fechamento. O fechamento pode ser feito com saldos desbalanceados e não funciona via SCHEDULE.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17143308670231) Tempo aproximado para leitura: **00:09:10 min**  
  
**Dúvida**

Qual o roteiro e maneira para efetuar o Fechamento de estoque com a nova jornada da rotina Acompanha custos? Quais as finalidades dos parâmetros MV\_ULMES e MV\_DBLQMOV neste Processo?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Apartir da Release 12.1.33.

**Solução**

**How To SIGAEST - Como realizar o novo fechamento de estoque custos**  
**Parte 1:** [**https://youtu.be/TYe75k-bacc**](https://youtu.be/TYe75k-bacc)  
**Parte 2:** [**https://youtu.be/6RVEbGOJraA**](https://youtu.be/6RVEbGOJraA)

**Duvida frequente:**

***A rotina MATA330 foi descontinuada?***

**R: Não**, voce pode usar ela normalmente, ou a propria MATA038, basta efetuar a etapa inicial de calculo, e ao finalizar, caso não queira seguir com o fechamento, basta "cancelar o fechamento", dessa forma ela processara apenas a etapa de "calculo de custo".

### **Antes de iniciarmos com as etapas de processo, precisamos saber primeiro, oque seria o fechamento de um periodo no estoque?**

* O fechamento de periodo, se trata de um processo no qual se realizada a finalização dos saldos e movimentações de uma determinada data, mantendo assim um estoque saudavel com os fechamentos condizentes a suas necessidades e entregas.

  É possivel que ocorra fechamentos de diferentes tipos, por exemplo:

  **Semanal, Quinzenal, Mensal, Semestral e Anual**, ou de acordo a necessidade da empresa.

**Tópicos**

* 1. Qual o tipo de custos na etapa de fechamento?
* 2. Quais rotinas devem ser processadas e sua ordem?
* 3. Qual a parametrização para realizar a Jornada de fechamento?
* 4. Como validar os saldos antes e após o fechamento?
* 5. Quais dados e parametros a etapa da jornada tem efeito?
* 6. É possivel reabrir um periodo após ele ser encerrado?
* 7. Eu posso efetuar o fechamento com saldos desbalanceados?
* 8. Eu posso apenas efetuar a etapa de calculo de custo e contabilização?
* 9. Quais são os dados gravados na virada de saldos?
* 10. A rotina funciona via SCHEDULE?
* 11. Oque não fazer?

**1. Qual o tipo de custos na etapa de fechamento?**

Para a execução da etapa da "[**Jornada de Fechamento**](https://tdn.totvs.com/display/PROT/Novo+Fechamento+-+Jornada+de+Fechamento)", existem dois tipos de apropriação para custos, onde é definido de acordo o seu parametro [**MV\_CUSMED**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007482371-MP-SIGAEST-MATA330-Recalculo-do-custo-M%C3%A9dio-On-Line-MATA330-e-Saldo-Atual-para-Final-MATA350-), os saldos serão efetuados conforme o seu metodo.

**Valide isso no ambiente, é EXTREMAMENTE IMPORTNTE saber qual seu tipo, Mais detalhes**

[MP - SIGAEST - MATA330 - Recalculo do custo Médio On-Line (MATA330) e Saldo Atual para Final (MATA350)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007482371-MP-SIGAEST-MATA330-Recalculo-do-custo-M%C3%A9dio-On-Line-MATA330-e-Saldo-Atual-para-Final-MATA350-)

Primeiro **PARAMETRO** ao clicar em **NOVO FECHAMENTO** > "**Data Para Fechamento do Custo**", deve-se colocar a **data de FECHAMENTO** do seu periodo.

* **Porque a data ja não é gravada com a ultima do periodo?**

**R:** Existem clientes com diferente tipos de apropriação para fechamento, sendo: semanal, quinzenal, mensal, semetral, anual etc, por isso a data não é preenchida com a do ultimo dia do mês vigente, assim como na rotina antiga também não era preenchido, fica a critério do cliente de qual periodo deseja realizar a virada de saldos.

Dessa forma, a **DATA PARA O FECHAMENTO DE CUSTO** é aberta.

**Caso queira deixar a data fixa, somente via ponto de entrada na rotina MATA330.**

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003970802-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Pontos-de-Entrada-da-rotina-Rec%C3%A1lculo-do-Custo-M%C3%A9dio>

**Eu preciso estar logado na database do mês que vou realizar o fechamento?**

Se o seu fechamento é **OFFLINE (MV\_CUSMED = M)**, não há nenhuma necessidade de estar na mesma database do fechamento, por exemplo:

Se estamos em **12/2024** mas preciso fechar o mês **11/2024** com data de **30/11/2024**, você não precisa logar com o sistema nessa data, você pode processar em qualquer data em aberto, basta atentar-se no pergunte da jornada "**DATA PARA FECHAMENTO DE CUSTO**" o primeiro pergunte de inicio da jornada, ele quem define a data de calculo das movimentações e virada de saldos.

**2. Quais rotinas devem ser processadas e sua ordem?**

**Etapas antes da jornada que** **não** **fazem parte da ROTINA ACOMPANHA CUSTOS**, conforme o antigo roteiro de fechamento de estoque, e sua ordem fica a critério do cliente, **não existe uma obrigatoriedade de processamento.**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Roteiro para Fechamento de Estoque (virada de saldos)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048372754-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Roteiro-para-Fechamento-de-Estoque-virada-de-saldos-)

* **MATA190** - Refaz custo de entrada. (Saiba mais > [Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051999634-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Refaz-Custo-de-Entrada-MATA190-Conceito-e-Exemplos))
* **MATA270/MATA340** - Digitação e Inventario. (Saiba mais > [Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020799592-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Processo-de-Invent%C3%A1rio-Conceito-Exemplo-e-D%C3%BAvidas))
* **MATA300** - Refaz Saldos. (Saiba mais > [Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420659401751-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA300-Refaz-Saldos-Conceito-e-Informa%C3%A7%C3%B5es))
* **MATA216** - Refaz Poder de terceiros. (Saiba mais > [Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005090232-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-efetuar-o-Controle-de-Poder-De-Em-Terceiros-))

**Etapas da jornada de fechamento ACOMPANHA CUSTOS**: Para a rotina Acompanha Custos, ja é contemplada das seguintes rotinas de processamento para calculo de custo e virada de saldos.

* **MATA330** - Recalculo de custo médio (MV\_CUSMED = M).
* **MATA350** - Saldo Atual para final (MV\_CUSMED = O).
* **MATA331** - Contabilização de custo médio.
* **MATA280** - Virada de Saldos.

**Caso você tenha problemas com saldos, custos alterados por notas fiscais, problema com saldo de terceiros, inventarios não processados, as rotinas "avulsas" servem para correção desses saldos em sua maioria das vezes dependendo do cenario.**

**(MATA190,MATA270/MATA340,MATA300,MATA216)**

### **Fica a critério do cliente para execução ANTES ou naõ do fechamento, isso é uma particularidade de cada empresa.**

**3. Qual a parametrização para realizar a Jornada de fechamento?**

Existe varias parametrizações que podem ser realizadas, **e cada uma varia de acordo a necessidade de fechamento da sua regra de negocios.**

Para exemplificar abaixo segue um boletim que lhe encaminha para a sessão em questão, e la você podera validar as parametrizações disponiveis para uso.

<https://tdn.totvs.com/display/PROT/Novo+Fechamento+-+Jornada+de+Fechamento#:~:text=Etapas%20Jornada%20de%20Fechamento>

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17143865043991)

**4. Como validar os saldos antes e após o fechamento?**

Antes de ser efetuado a ultima etapa da Jornada de Fechamento, é importante que seja efetuado um DE/PARA, afim de verificar se os saldos dos produtos, estão condizentes as necessidades de movimentações que ocorreram para ele no periodo em questão.

Hoje na rotina Acompanha Custos, existe uma etapa chamada "Analise e Revisão" e essa pode ser utilizada, para a validação de custos dos produtos, que se da com o valor de custo médio gravado no ultimo periodo, e comparado com um ultimo custo calculo do periodo vigente, Assim fica a critério se basear por esse, para geração de relatorios de saldos.

Caso não apresente dados é porque não foi carregado divegencias para apresentação, podera seguir normalmente com o fechamento.

**Menu > Analise e Revisão**

<https://tdn.totvs.com/display/PROT/Novo+Fechamento+-+Jornada+de+Fechamento#:~:text=Etapas%20Jornada%20de%20Fechamento>

E quais relatorios posso utilizar para comparar os saldos?

* **MATR900** - Kardex por periodo (Saiba mais > [Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011930291-MP-SIGAEST-An%C3%A1lise-de-Custos-MATR900-Kardex-por-Per%C3%ADodo))
* **MATR260** - Estoque Analitico (Saiba mais > [Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018559171-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR260-Import%C3%A2ncia-da-pergunta-Saldo-do-produto-a-considerar-para-correta-emiss%C3%A3o-do-relat%C3%B3rio))
* **MATR460** - P7 (Saiba mais > [Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001540542-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Perguntas-do-relat%C3%B3rio-MATR460-Invent%C3%A1rio-Modelo-7-))
* **MATR282** - Divergencia de saldos (Saiba mais > [Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018463012-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR282-Parametriza%C3%A7%C3%A3o-para-identificar-diverg%C3%AAncia-de-saldos-entre-tabelas-SB2-X-SB8-X-SBF))

**5. Quais dados e parametros a etapa da jornada tem efeito?**

A virada de saldos, tem por objetivo repassar os saldos calculados no periodo em questão, gravados nos **saldos atuais "SB2"** sob os campo **"B2\_QFIM, B2\_VFIM, B2\_CMFIM1"** de acordo com o tipo de calculo se ONLINE ou OFFLINE, mediante parametro MV\_CUSMED, para que esses sejam repassados para o periodo final vigente e corrente para o periodo inicial, sob os **Saldos Inicias "SB9"** em prol dos campo **"B9\_QINI, B9\_VINI1 e B9\_CM1",** e fora ressalvamos se utilizar produtos com controle de lote e endereço, saldos serão levados para **"SBJ e SBK"**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Conceito e tabelas de controle de Lote e Endereço no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018454332-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-tabelas-de-controle-de-Lote-e-Endere%C3%A7o-no-Protheus)

**Detalhes:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17144296825495)

Também por si, grava a data de fechamento do periodo efetuado "SB9\_DATA" e essa data e repassada para o parametro MV\_ULMES.

**Efetivamente, deve-se considerar o parametro MV\_ULMES de forma a ser exclusiva para CADA FILIAL.** Assim evita que o proceso de reabertura de forma a considerar N filiais, ocorra erro, ou até mesmo impossibilitar a abertura somente de uma filial caso esteja compartilhado.

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Funcionalidade do parâmetro MV\_ULMES](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009616322-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Funcionalidade-do-par%C3%A2metro-MV-ULMES)

Também existe a possibilidade de travar movimentos com o parametro **MV\_DBLQMOV**, ele é extremamente importante, para evitar disparidade de saldos, durante o processo de fechamento.

[MP - SIGAEST - Como realizar o bloqueio de Movimentações no Estoque durante o Fechamento de Estoque?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018844351-MP-SIGAEST-Como-realizar-o-bloqueio-de-Movimenta%C3%A7%C3%B5es-no-Estoque-durante-o-Fechamento-de-Estoque-)

**6. É possivel reabrir um periodo após ele ser encerrado?**

Hoje com a nova jornada, sim é possivel! para mais detalhes basta acessar o boletim a seguir, com as etapas e processo para a reabertura de estoque.

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA038 - Processo de Reabertura de Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6420543172247-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA038-Processo-de-Reabertura-de-Estoque)

**7. Eu posso efetuar o fechamento com saldos desbalanceados?**

Sim voce pode realizar a virada de saldos com itens pendentes de correção para SALDOS A DISTRIBUIR, caso exista algum item pendente de endereçamento que possa comprometer o fechamento o sistema apresentará no fechamento uma tela de Saldos à Distribuir, onde serão listados todos os itens com pendencias para que seja possível finaliza-las e realizar o fechamento. Caso necessário, também é possível cancelar o fechamento nessa etapa.

Aviso

Atenção, essa etapa será apresentada durante a jornada de fechamento, apenas se o ambiente estiver com a configuração de exibir relatório de Saldo a Distribuir **(****MV\_A280SDA) habilitada.**

![](https://tdn.totvs.com/download/attachments/572501579/sados_distribuir.gif?version=1&modificationDate=1645017724637&api=v2)

**8. Eu posso apenas efetuar a etapa de calculo de custo e contabilização?**

Sim, você pode fazer isso, a proposito o processamento na rotina PO-UI é mais rapido! quando finalizar a etapa de calculo de custo, e contabilização, voce pode apenas clicar em Cancelar Fechamento, sem avançar para ultima etapa, assim voce vai ter processado somente o custo e contabilização.

**9. Quais são os dados gravados na virada de saldos?**

**Saldo fisico SB2:** (B2\_QFIM repassa para B9\_QINI) | (B2\_VFIM1 repassa para B9\_VINI)

**Saldo por lote SBJ:** (B2\_QFIM repassa para BJ\_QINI de acordo lotes)

**Saldo por endereço SBK:** (B2\_QFIM repassa para BK\_QINI de acordo endereços)

**10. A rotina funciona via SCHEDULE?**

**Não,** não é possivel configurar a rotina MATA038 via SCHEDULE, devido ao formato ser em PO-UI.  
Porém a jornada usa as seguintes rotinas de acordo sua configuração para realizar o fechamento, e cada rotina individual pode ter o schedule configurado para validação "durante o processamento da jornada"  
MATA330 - Recalculo de custo médio  
MATA350 - Saldo atual pra final  
MATA280 - Virada de saldos.  
<https://tdn.totvs.com/pages/releaseview.action?pageId=862110729>

**11. Oque não fazer?**

Suponha que a sua empresa, efetua a etapa de calculo de custo para o periodo 31/05/2026, mas a apuração dos saldos para seguir para a etapa da "virada de saldos", vai ocorrer daqui a 15 dias. (ou seja estariamos no dia 15/06/2026).

Não processe o CUSTO MEDIO com data maior de 31/05/2026, pois se for efetuado a etapa da virada de saldos, e alguem tiver rodado o custo médio com data até JUNHO, os saldos calculados serão de JUNHO, e ai vai ficar errado em consideração a MAIO.

**Saiba mais**:

[*Clique aqui e veja mais artigos sobre a Nova Jornada de Fechamento no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/5367899706647-ACOMPANHA-CUSTOS-JORNADA-DE-FECHAMENTO-NOVO-)
