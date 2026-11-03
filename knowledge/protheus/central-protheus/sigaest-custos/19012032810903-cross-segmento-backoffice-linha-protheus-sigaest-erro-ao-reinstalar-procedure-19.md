---
article_id: 19012032810903
category: SIGAEST - CUSTOS
content_hash: 68634fab15bb8f8b15bee2724eaa02ecc44e8565585620ca82dc27e1ec939289
fetched_at: '2026-06-28T22:39:00.905935+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Erro ao reinstalar
  procedure 19 - TR201SP: TOP Error -19 - Field not found for table'
type: support-article
updated_at: '2025-03-12T12:27:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19012032810903-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Erro-ao-reinstalar-procedure-19-TR201SP-TOP-Error-19-Field-not-found-for-table
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19012034934423) Tempo aproximado para leitura: **00:04:20 min****Dúvida**O que fazer quando ocorrer o erro na reinstalação da procedure 19:

*THREAD ERROR ([XXXXX],*  
***TR201SP: TOP Error -19 - Field [B2\_VATU1] not found for table [TR201SP].***

*( From tISAMFile::**CreateIndex** )*  
*Thread ID [XXXX] User [Administrador] IO [XXXXX] Tables [XX] MaxTables [XX] Comment [CFGX051 - TCPIP - ThreadID(XXXXX)] SP [ ] Traced [No] SQLReplay [No] InTran [No] DBEnv [MSSQL/NOME\_DO\_AMBIENTE] DBThread [(SPID 101,110,294)] Started [10/11/2023 00:01:00] IP [192.168.0001] IDLE [ ] InTransact [ ] Memory [0] Running [**ROP\_CREATEINDEX** for 0 s.] RCV [XXXXX] SND [XXXXXXX] TCBuild [20230303-20230929] TCVersion [23.1.1.0] ARCH [64] OS [WINDOWS] BUILD [RELEASE]*   
***on A330CRTABS(MATA330.PRX) 20/09/2023 09:52:14 line : 13309***  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

O erro apresentado indica que há um problema na criação de um índice na tabela [**TR201SP**], pois o campo [**B2\_VATU1**] não foi encontrado.

Para validar e corrigir esse erro, é recomendável verificar a estrutura da tabela [**TR201SP**] no banco de dados, garantindo que o campo [**B2\_VATU1**] esteja definido corretamente.

Também é possível checar **se há um índice personalizado (não padrão)** relacionado a essa tabela, pois pode ser que o índice em questão não esteja devidamente configurado ou tenha sido removido.

Esse processo deve ser avaliado pelo seu adminstrador de banco de dados.

**Exemplo consultando o indice (em SQL Server):**

```
SELECT * FROM SB2990
```

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19012299073943)

Selecione somente o nome da tabela, e pressione a tecla (**ALT + F1), e sera retornado a seguinte informação:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/19012299075223)**

Esse é o indice padrão atualmente tabela SB2 **(datado em 2023/11/12)**

|  |  |  |
| --- | --- | --- |
| SB29901 | nonclustered located on PRIMARY | B2\_FILIAL, B2\_COD, B2\_LOCAL, R\_E\_C\_N\_O\_, D\_E\_L\_E\_T\_ |
| SB29902 | nonclustered located on PRIMARY | B2\_FILIAL, B2\_LOCAL, B2\_COD, R\_E\_C\_N\_O\_, D\_E\_L\_E\_T\_ |
| SB29903 | nonclustered located on PRIMARY | B2\_FILIAL, B2\_LOCAL, B2\_QACLASS, R\_E\_C\_N\_O\_, D\_E\_L\_E\_T\_ |
| SB2990\_PK | clustered, unique, primary key located on PRIMARY | R\_E\_C\_N\_O\_ |
| SB2990\_UNQ | nonclustered, unique located on PRIMARY | B2\_FILIAL, B2\_LOCAL, B2\_COD, R\_E\_C\_D\_E\_L\_ |

Se em sua base de dados for diferente disso, a sugestão é que o seu DBA efetue o ajuste devido e deixe conforme padrão.

**Como saberemos se o indice é ou não personalizado?**

Essa questão é bem simples, pois o DBA sabera informar se ele é ou não personalizado ao validar os indices de sua base de dados, pois toda alteração em banco, tem registros e logs que podem ser consultados pelo mesmo.

**Se mesmo após a avaliação, o erro persistir?**

Basta encaminhar ao time de suporte, um print do select do indice da tabela SB2 em questão, bem como o error.log em anexo gerado, para que seja avaliado.

**Essa mesma avaliação, pode ser feita para outros campos?**

Sim, você pode utilizar da mesma analogia sob o erro apresentado, caso ele seja outros campos e tabelas, ao invés do B2\_VATU1 e tabela TR2.

Pois o erro em SQL referente a "**TOP Error -19 - Field**" indica um problema relacionado à cláusula "**TOP**" em uma consulta. A cláusula "TOP" é comumente usada para limitar o número de linhas retornadas em um conjunto de resultados. O código de **erro -19** sugere que há uma discrepância ou uma inadequação no campo especificado na cláusula "**TOP**". Isso pode ocorrer devido a um campo inexistente, malformado ou incompatível com a operação de classificação ou para o indice nesse caso.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
