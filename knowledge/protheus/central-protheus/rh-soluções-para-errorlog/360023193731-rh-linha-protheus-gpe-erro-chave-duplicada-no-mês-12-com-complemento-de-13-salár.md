---
article_id: 360023193731
category: RH - Soluções para error.log
content_hash: b6a73f5dfd9c1f80f33b03195760edd45a60d9d6218130d28cf659521db0cd22
fetched_at: '2026-06-28T22:44:08.859167+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: RH - Linha Protheus - GPE - Erro chave duplicada no mês 12 com complemento
  de 13° salário
type: support-article
updated_at: '2025-08-20T18:02:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023193731-RH-Linha-Protheus-GPE-Erro-chave-duplicada-no-m%C3%AAs-12-com-complemento-de-13-sal%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34323921654295)** Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**  
Ao tentar realizar o **cálculo da folha** do mês 12 com o **mnemônico P\_CCOMP13** ativo para pagamento do complemento de **13° Salário**, com um roteiro customizado que utilize a **função fGeraverba**, é apresentado o error log: **DB *error* (*Insert*): -37 *File*: SRC080 - *Error* : 2601 (23000) (RC=-1) - [*Microsoft][SQL Native Client][SQL Server]Cannot insert duplicate key row in object* 'dbo.SRC080' *with unique index* 'SRC080\_UNQ'.*****INSERT INTO* dbo.SRC080(RC\_FILIAL,RC\_MAT,RC\_PD,RC\_TIPO1,RC\_VALOR,RC\_DATA,RC\_DTREF,RC\_SEMANA,RC\_CC,RC\_TIPO2,RC\_SEQ,RC\_VALORBA,RC\_PROCES,RC\_PERIODO,RC\_NUMID,RC\_ROTEIR,RC\_CODB1T,RC\_IDCMPL,R\_E\_C\_N\_O\_) VALUES ( ?,?,?,?,?,?,?,?****,?,?,?,?,?,?,?,?,?,?,?)****Ambiente**  
TOTVS RH - TOTVS RH (Linha protheus) – Gestão de Pessoal – A partir da versão 12.  
  
**Causa**   
Incidente ocorre, por **falta tratamento em posição na variável cSeq**.  
  
**Solução**  
Para solucionar essa ocorrência, analise a customização e ajuste conforme exemplos do documento técnico a seguir: [http://tdn.totvs.com/x/HCkcGw](http://tdn.totvs.com/x/HCkcGw "Follow link")  
  
**Saiba mais**[RH Expedição Contínua](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-MP-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-continua-acumulado-do-modulo-Gest%C3%A3o-de-Pessoal?source=search)
