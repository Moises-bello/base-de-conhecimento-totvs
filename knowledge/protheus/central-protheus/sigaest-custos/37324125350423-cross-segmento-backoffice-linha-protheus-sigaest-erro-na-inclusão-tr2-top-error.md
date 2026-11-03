---
article_id: 37324125350423
category: SIGAEST - CUSTOS
content_hash: 5aeea55287ff9af5ff0227af768a2d92321e7ce9bb2a34ba0fd2ce6ac7667452
fetched_at: '2026-06-28T22:39:00.341148+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Erro na inclusão
  TR2: TOP Error -19 - The size (10) of the integer part of the number (1406287275)
  informed is greater than the size (9) supported by the field (B2_CM4). (Row 403
  Col 13)'
type: support-article
updated_at: '2025-12-29T19:44:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37324125350423-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Erro-na-inclus%C3%A3o-TR2-TOP-Error-19-The-size-10-of-the-integer-part-of-the-number-1406287275-informed-is-greater-than-the-size-9-supported-by-the-field-B2-CM4-Row-403-Col-13
---

O erro no processamento do Custo Médio (MATA330) ocorre porque o valor inteiro informado (ex: 1406287275) excede o tamanho máximo suportado pelo campo B2\_CM4, que é 9 dígitos. A solução é ajustar o tamanho do campo no Configurador para suportar o valor, recomendando 15 dígitos com 4 decimais, e atualizar as stored procedures após a alteração.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37324125346327) Tempo aproximado para leitura: **00:04:00 min**  
  
**Ocorrência**

Ao efetuar o processamento do Custo Médio (MATA330) apresenta o error.log abaixo. O que devemos analisar no ambiente para ajustar:

THREAD ERROR ([4545], 354368583, TOTVSTI10)   29/12/2025 15:41:00  
**Erro na inclusão TR2: TOP Error -19 - The size (10) of the integer part of the number (1406287275) informed is greater than the size (9) supported by the field (B2\_CM4). (Row 403 Col 13)**  
( From tDBServer::ROP\_DBINSERT )  
Thread ID [22358]    User [admin]    IO [3640]    Tables [74]    MaxTables [74]    Comment [MATA330 - TCPIP - ThreadID(2572)]    SP [ ]    Traced [No]    SQLReplay [No]    InTran [Yes]    DBEnv [MSSQL/DADOSADV]    DBThread [(SPID 132,148,326)]    Started [29/12/2025 15:41:07]    IP [0.0.0.0:000]    IDLE [ ]    InTransact [0 s.]    Memory [0]    Running [ROP\_DBINSERT for 0 s.]    RCV [1346720]    SND [3225636]    TCBuild [20240224-20250929]    TCVersion [24.1.1.0]    ARCH [64]    OS [WINDOWS]    BUILD [RELEASE]      
on INSERTTR2(MATA330.PRX) 03/09/2025 16:21:32 line : 15830

[TOTVS build: 7.00.240223P-20251030]  
Called from A330TR2INI(MATA330.PRX) 03/09/2025 16:21:32 line : 15709  
Called from MA330PROCESS(MATA330.PRX) 03/09/2025 16:21:32 line : 835  
  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Causa**

Esse incidente ocorre, pois esta processando um valor que não cabe no campo na parte inteira do Número, por exemplo o valor a ser ajustado no processamento seria **1406287275 observe que esse número contém 10 posições inteiras,** porém, **a parte inteira no campo B2\_CM4** é suportado no máximo 9 posições inteiras. Observe no print abaixo que a parte inteira é composta de 9 posições mais o ponto.

|  |
| --- |
| **Erro na inclusão TR2: TOP Error -19 -** **The size (10) of the integer part of the number (1406287275)** **informed is greater than** **the size (9) supported by the field (B2\_CM4)****. (Row 403 Col 13)** |

![b2_cm4.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/37324798954519)

**Solução**

Para solucionar essa ocorrência, identifique o campo indicado e revise o tamanho inteiro do mesmo e ajuste pelo módulo Configurador para um tamanho superior ou igual ao inteiro apresentado no error.log.

Nesse exemplo que apresentamos, o tamanho adequado para o campo **B2\_CM4 é 15 com 4 decimais**. Após esse ajuste não apresentara mais o error.log.

**Informações importantes:**

**- 1 -** Nesse cenário também avaliar o Grupo de Campos Numéricos ([link](https://tdn.totvs.com/x/JVo9L)) e ajustar pelo mesmo.

**- 2 -** Após alteração do Grupo de Campos Numéricos ou mesmo um campo específico deve efetuar a **atualização das STORED PROCEDURES** como indicado [***nesse link***](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15131065568791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Procedure-Desatualizada-ou-Incompat%C3%ADvel).

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre CUSTOS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)

[SIGAEST - Como avaliar o erro Data width error em rotinas de processamento?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17995686483095-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-avaliar-o-erro-Data-width-error-em-rotinas-de-processamento)

[Grupo de Campos Numéricos](https://tdn.totvs.com/x/JVo9L)

[SIGAEST - Procedure Desatualizada ou Incompatível](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15131065568791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Procedure-Desatualizada-ou-Incompat%C3%ADvel)
