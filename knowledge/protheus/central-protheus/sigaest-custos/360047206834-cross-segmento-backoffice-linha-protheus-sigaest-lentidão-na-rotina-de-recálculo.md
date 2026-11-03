---
article_id: 360047206834
category: SIGAEST - CUSTOS
content_hash: 837a2c26802a99a1d70f4f7c24ca30c6205aea424d3818087a67b5325e9e881f
fetched_at: '2026-06-28T22:39:00.352115+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Lentidão na rotina
  de Recálculo do Custo Médio (MATA330)
type: support-article
updated_at: '2026-04-28T20:23:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047206834-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Lentid%C3%A3o-na-rotina-de-Rec%C3%A1lculo-do-Custo-M%C3%A9dio-MATA330
---

A lentidão na rotina de Recálculo do Custo Médio (MATA330) no TOTVS Protheus pode ser causada por fontes desatualizadas, artefatos desatualizados, configurações incorretas de DBAPI.DLL, compartilhamento inadequado de tabelas contábeis, parâmetros de multi-thread mal configurados, processamento de produtos obsoletos, entre outros. É recomendado atualizar fontes, procedures, bibliotecas, revisar parâmetros e, se necessário, coletar logs para análise detalhada.

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32900714156183)** **Tempo aproximado para leitura:****00:05:30 min**

**Ocorrência**

O processamento da rotina de **Recálculo do Custo Médio (MATA330)** apresenta lentidão. O que avaliar para resolver este problema?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

A lentidão na rotina de Recálculo de Custo Médio (MATA330) pode ocorrer por diversos motivos. Desta forma, listaremos abaixo os motivos mais comuns que geram a lentidão e como resolvê-los.

**Observações:** Verifique primeiramente se o ambiente esta com o pacote Acumulado Backoffice mais atualizado. [***Clique aqui***](https://tdn.totvs.com/x/2hgdHw) para acesso ao link para a página direcionadora aos pacotes.

**- 1 -  Identificar se as rotinas e as procedures estão atualizadas**. Ao pressionar as teclas **SHIFT + F6** na rotina **Custo Médio (MATA330)** é possível avaliar a data do fonte. E, em seguida, comparar com a data do fonte disponível no portal de suporte. Para facilitar a localização, segue abaixo o link dos artefatos do Custo Médio, dentre eles o link da Stored Procedure e Fonte:

[***https://tdn.totvs.com/x/NYJJF***](https://tdn.totvs.com/x/NYJJF)

Já para visualizar se a Procedure está ou não atualizada, basta acessar ao **Configurador (SIGACFG) -> Base de Dados -> Dicionário -> Stored Procedure**. Ao abrir, selecione a operação "Consulta" e clique em OK.

Na coluna "Status" será possível visualizar se a Stored Procedure está OK, Desinstalada ou Desatualizada. [***Nesse link***](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15131065568791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Procedure-Desatualizada-ou-Incompat%C3%ADvel) apresenta um passo a passo sobre **como atualizar as STORED PROCEDURES**.

![CONSULTA PROCEDURE.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/32900706703767)

**OBS**: Em caso de atualização da rotina e Stored Procedure, é necessário que a rotina MATA320 e a Procedure 20 também sejam atualizadas.

**- 2 - É necessário que os artefatos de LIB, Binários e DBAcess estejam com as últimas atualizações do portal do Cliente,** [***nesse link***](https://tdn.totvs.com/x/tGjNI) **você tem acesso direto:**

**- 3 - É necessário verificar o arquivo DBAPI.DLL se estão com a mesma data de modificação nos diretórios AppServer e DBAcess.**

Para analisar, é preciso ter acesso às pasta do AppServer e DBAcess. Localize o arquivo "dbapi.dll" e analise as datas de modificação. Elas precisam estar iguais.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069842173)

Caso tenha alguma dúvida referente ao compartilhamento do arquivo, [**clique aqui.**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028710652-MP-FRAME-Arquivo-dbapi-dll-do-DBAccess-no-AppServer)

**- 4 -** **Verificar o compartilhamento das tabelas do módulo Contábil**.

Outro fator que pode impactar é o compartilhamento das tabelas do módulo Contábil. Se elas não estiverem com o mesma configuração, pode apresentar lentidão. [Clique aqui](https://tdn.totvs.com/display/public/PROT/CTB0012_Compartilhamento_de_tabelas_SIGACTB) e veja como fazer o compartilhamento.

**- 5 - Verificar os parâmetros de Multi Thread, onde auxiliam no processamento e ganho de performance:**

**MV\_M330THR:** Quantidade Threads para execução da rotina.

Define o numero de threads que serão utilizadas na rotina de recalculo do custo médio (informar os números de 1 a 99 threads).  
IMPORTANTE: Ao aumentar o numero de threads o administrador de infraestrutura deverá verificar durante a execução da rotina se a quantidade de threads está de acordo com a capacidade de seu ambiente.

**MV\_M330JCM:**

Define se utiliza threads no processamento dos movimentos de ordem 100/300/500 na rotina de custo médio (MATA330).

**MV\_THRSEQ = .F.**  
Informa se na geração do arquivo TRB da rotina de recalculo do custo médio será utilizado o controle de Jobs por .T. = Sequencial ou .F. = Paralelo.  
**IMPORTANTE: Para melhor performance o parâmetro deve estar configurado com .F. = Paralelo.**

**- 6 - Avaliar o parâmetro** [**MV\_A330GRV**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062164934-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Valida%C3%A7%C3%A3o-dos-par%C3%A2metros-MV-A330GRV-e-MV-A280GRV-para-produtos-obsoletos) **para processar ou não o Recálculo de produtos obsoletos**

* [**MV\_A330GRV**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062164934-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Valida%C3%A7%C3%A3o-dos-par%C3%A2metros-MV-A330GRV-e-MV-A280GRV-para-produtos-obsoletos) **= .T (True/Verdadeiro):** com este conteúdo (padrão) todos os produtos e armazéns terão seus saldos iniciais recálculos independentes de serem ou não obsoletos. Este é o processo utilizado.
* [**MV\_A330GRV**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062164934-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Valida%C3%A7%C3%A3o-dos-par%C3%A2metros-MV-A330GRV-e-MV-A280GRV-para-produtos-obsoletos) **= .F.(False/ Falso):** com este novo conceito somente os produtos e armazéns que possuem movimentação de estoque dentro do período de processamento e que possuem quantidades e custos **diferentes** **de zero**, terão seus saldos iniciais recalculados. Os produtos que não se enquadram nesta regra (obsoletos) não são recalculados pela rotina.

**- 7 -** Verifique se a lentidão ocorre quando esta contabilizando**,** revise os **parâmetros MV\_PROCCV3** e **MV\_A330190.**

**- 8 - Utilizar (opcional) a ferramenta MALLOC-IO (onde aloca a memoria para ganho de performance):**

Para obter mais informações sobre o programa e como utilizar, [clique aqui.](https://tdn.totvs.com/display/public/PROT/MallocIO) Também veja [**nesse link**](https://www.youtube.com/watch?v=UeO3VbLw2R8) o vídeo com instruções sobre a **ferramenta MALLOC-IO**

**- 9 - Ativar a chave DBPulse no DbAcess (****Caso tenha ambiente Cloud****).** [**Veja detalhes de como ativar clicando aqui**](https://tdn.totvs.com/pages/viewpage.action?pageId=394209930)

**- 10 -** ***Caso o problema de lentidão*** ***persista, mesmo com os passos*** ***acima já revisado*****, segue as ações para avaliação (****Serve tanto para cliente Cloud quanto cliente com ambiente Standard****), ou mesmo** [***nesse link dessa FAQ***](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20441141102743-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Configura%C3%A7%C3%A3o-e-coleta-de-logs-para-avalia%C3%A7%C3%A3o-da-performance-no-recalculo-de-custo-m%C3%A9dio) **consta as instruções sobre configuração e coleta de logs para avaliação da performance no recalculo de custo médio:**

**- 10.1 -** Solicitar o apoio de um DBA para acompanhar a execução da rotina e verificar os possíveis pontos de manutenção no data-base para otimizar o processamento.

**- 10.2 -**Habilitar o mecanismo de LogProfiler para gerar uma auditoria dos tempos de processamento. Deve ser criada a chave ConsoleMaxsize com conteudo 104857600 no appserver.ini, vide [ConsoleMaxSize -- 29343](https://tdn.totvs.com/display/tec/ConsoleMaxSize+--+29343), reduzindo o risco do logprofiler ficar incompleto.

Para saber como habilitar e gerar o LogProfiler veja a documentação disponibilizada no link [http://tdn.totvs.com/pages/viewpage.action?pageId=243638663](https://tdn.totvs.com/pages/viewpage.action?pageId=243638663)

**IMPORTANTE:** Não acionar por **<SHIFT>+<F6>**, pois sua apresentação envolve somente a thread corrente. A rotina faz uso de varias threads que serão apresentadas somente no console.log/console.bak, sendo acionado através da chave LogProfiler=1 inserido no appserver.ini

**- 10.3 -**Após a geração do LogProfiler realizar a abertura de um novo ticket para equipe de Suporte Técnico atraves do portal do cliente ( [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/) ), anexando os seguintes itens:

* Uma evidencia em vídeo com todas as configurações utilizadas em seu ambiente
* Arquivo de console.log
* Arquivo de console.bak
* Arquivo de error.log
* Arquivo de dbaccess.log
* Arquivo de dbconsole.log
* Uma cópia completa da tabela CV8, de preferencia no formato CTREE(.DTC)
* Envie em .**dtc ou .sdb** a tabela **CV8** filtrada para o campo **CV8\_PROC=MATA330** se processado pela rotina MATA330;
* Envie em **.dtc ou .sdb** as tabelas **D3X, D3Y e D3W completas** se processado pela rotina Acompanha Custos MATA038;

**Saiba mais:**

[(Linha Protheus) - SIGAEST - Configuração e coleta de logs para avaliação da performance no recalculo de custo médio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20441141102743-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Configura%C3%A7%C3%A3o-e-coleta-de-logs-para-avalia%C3%A7%C3%A3o-da-performance-no-recalculo-de-custo-m%C3%A9dio)

[*Dicas para melhor performance no Recálculo do Custo Médio*](https://tdn.totvs.com/pages/releaseview.action?pageId=6087429)

[*MP - SIGAEST - Rotina MATA330 - Perguntas do Recálculo do Custo Médio*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024805291)

[*MP - SIGAEST - Performance na Contabilização do CM*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016500251-MP-SIGAEST-Performance-na-Contabiliza%C3%A7%C3%A3o-do-CM)

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000049222-SIGAEST-CUSTOS)
