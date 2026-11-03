---
article_id: 5168088769175
category: Materiais - Compras (SIGACOM)
content_hash: 973c8ee93ee5a52a7eb2c311e16d77e4ae90041748090a4a56af384b27f442a7
fetched_at: '2026-06-28T22:41:17.643309+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Error log Nome de objeto
  'SXI' inválido - Em Rotinas do módulo Compras
type: support-article
updated_at: '2023-09-14T16:44:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5168088769175-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Error-log-Nome-de-objeto-SXI-inv%C3%A1lido-Em-Rotinas-do-m%C3%B3dulo-Compras
---

**Ocorrência**Ao realizar a inclusão de um cadastro de fornecedor apresenta o erro abaixo:

THREAD ERROR ([7988], ti, DKT-102) 30/03/2022 11:33:51  
: Error : 208 (S0002) (RC=-1) - [Microsoft][SQL Server Native Client 11.0][SQL Server]Nome de objeto 'SXI' inválido.  
( From tMSSQLConnection::GetQueryFile )  
Thread ID [3812] User [Administrador] IO [3277] Tables [73] MaxTables [73] Comment [MATA020 - TCPIP - ThreadID(7988)] SP [ ] Traced [No] SQLReplay [No] InTran [No] DBEnv [MSSQL/TOTVS12] DBThread [(SPID 59,60,62)] Started [30/03/2022 11:32:37] IP [127.0.0.1:1234] IDLE [ ] InTransact [ ] Memory [0] Running [ROP\_QUERY for 0 s.] RCV [122645] SND [571795] TCBuild [20210202-20210930] TCVersion [21.1.1.0] ARCH [64] OS [WINDOWS] BUILD [RELEASE]   
SELECT XI\_EVENTID FROM SXI SXI WHERE SXI.XI\_EVENTID = '036' AND SXI.D\_E\_L\_E\_T\_= ' ' on \_\_EXECSQL(APLIB300.PRW) 06/10/2021 13:57:35 line : 149

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - Todas as versões  
  
**Causa**O erro está  relacionado a não se estar encontrando como válida a tabela SIX do sistema no ambiente em questão. Esta tabela é do cadastro do programa CFGA040 (INscr. Event Viewer) do Configurador, e que também fica no menus dos módulos do Protheus.  
O acesso pelo módulo Configurador é **Ambientes / Cadastros / Inscr. Event Viewer**. Nos demais módulos, a rotina está disponível em **Miscelâneas / Inscr. Event Viewer**.

**Solução**

1.  Login com o usuário Administrador e acesso exclusivo ao módulo Compras;

2.  Acesse a rotina: Miscelanea -> Inscr. Event Viewer;

3. Verifique se a tabela SXI foi criada no banco de dados, via Top Connect, ou no diretório System do ambiente;

4. Se a tabela SXI não for criada, reinicie o serviço de banco de dados e o DBAccess e repita as etapas 1, 2 e 3.

Para correção é necessário verificar se a tabela é aberta/criada corretamente, e fazendo um teste de inclusão e exclusão de um registro conforme o vídeo abaixo, e verificando se o erro persiste.  
  
![20220401_104306.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5168018968343)

Caso ainda persista, realizar um teste reiniciando o DBAccess.

Verificar também se existe a tabela SXI do ambiente em questão, caso exista valide se possui um registro com o ID do evento 036 que é o que é mostrado no erro:  
  
![](https://totvssuporte.zendesk.com/attachments/token/2HE5Pm4yLVxqB7dhcKgL9m27D/?name=inline1978625017.png)

Se possuir o evento será necessário realizar processo de recriação desta tabela SXI, e realização de novos cadastros.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
