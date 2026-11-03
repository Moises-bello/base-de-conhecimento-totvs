---
article_id: 360026121694
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 31a6e7076e44842cc3dd7843937e4a430f9658adf2240f964057104c216ead37
fetched_at: '2026-06-28T22:42:42.175836+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Definição das legendas das OPs
type: support-article
updated_at: '2021-11-05T10:54:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026121694-Manufatura-Linha-Protheus-SIGAPCP-Defini%C3%A7%C3%A3o-das-legendas-das-OPs
---

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min****Dúvida**No **MATA650**, como são definidas as legendas das **OPs**?  
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**O **MATA650** faz a leitura de dados em alguns campos e tabelas para definir a legenda ou situação das **OPs**, conforme regra abaixo:  
  
**Ordem de produção prevista:** campo **C2\_TPOP** com o conteúdo **P**.**Ordem de produção em aberto:** campo **C2\_TPOP** com o conteúdo **F**, o campo **C2\_DATRF** vazio, não existem movimentos nas tabelas **SD3** e **SH6** para a Ordem de Produção em questão, além **Database** menos **C2\_DATPRI** ser menor que o tempo definido no campo **C2\_DIASOCI** para indicar que a **OP** está ociosa.  
  
**Ordem de produção iniciada:** campo **C2\_TPOP** com o conteúdo **F**, o campo **C2\_DATRF** vazio, existem movimentos nas tabelas **SD3** ou **SH6**, e a **Database** subtraída da data do último movimento for menor do que o tempo indicado no campo **C2\_DIASOCI** para indicar que a Ordem de Produção está ociosa.  
  
**Ordem de produção ociosa:** campo **C2\_TPOP** com o conteúdo **F**, o campo **C2\_DATRF** vazio e a **Database** subtraída da data do último movimento ou do conteúdo do campo **C2\_DATPRI** for maior ou igual ao tempo definido no campo **C2\_DIASOCI**.  
  
**Ordem de produção encerrada parcialmente:** campo **C2\_TPOP** com o conteúdo **F**, o campo **C2\_DATRF** preenchido, porém a quantidade do campo **C2\_QUJE** é menor do que **C2\_QUANT.****Ordem de produção encerrada totalmente:** campo **C2\_TPOP** com o conteúdo **F**, o campo **C2\_DATRF** preenchido e o campo **C2\_QUJE** maior ou igual a **C2\_QUANT**.  
  
**Glossário**  
**C2\_QUJE** - Qtd.Produzid  
**C2\_TPOP** - Tipo Op    
**C2\_DATRF** - DT Real Fim   
**C2\_DATPRI** - Previsao Ini  
**C2\_QUANT** - Quantidade    
**C2\_DIASOCI** - Dias Ocios.   
**MATA650** - Ordem de produção  
**SD3** - Movimentações Internas  
**SH6** - Movimentação da Produção  
**OPs** - Ordens de Produção
