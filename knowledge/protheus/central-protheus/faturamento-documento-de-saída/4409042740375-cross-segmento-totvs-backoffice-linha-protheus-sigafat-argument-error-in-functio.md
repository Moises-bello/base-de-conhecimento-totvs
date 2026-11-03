---
article_id: 4409042740375
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 7783b7fd0870f30f9813de867b52da537a8cd8331b0cced3e98791e6a65af75b
fetched_at: '2026-06-28T22:38:43.944158+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT- Argument error
  in function Len() on FAAVALSE1(FINXAPI.PRX) na exclusão da nota
type: support-article
updated_at: '2021-09-21T11:14:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409042740375-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Argument-error-in-function-Len-on-FAAVALSE1-FINXAPI-PRX-na-exclus%C3%A3o-da-nota
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao tentar excluir uma nota de Serviço, gera o error.log: **argument error in function Len() on FAAVALSE1(FINXAPI.PRX)**  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT- Todas as versões.  
  
**Causa**

O erro**argument error in function Len() on FAAVALSE1(FINXAPI.PRX)** ocorre na exclusão da nota de saída (**mata521**), é sempre relacionado a nota de Serviços e muitas vezes é precedido do Help:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409049647767/mceclip0.png)

A rotina pai da função **FA040PENC** é o **FINA040**, um dos motivos de ocorrer a mensagem seria a falta da função **FA040PENC** para poder concluir o processo. Como esta função já está declarada no **FINA040**, a outra possibilidade é que a função **FAAVALSE1** que pertence ao **FINXAPI** esteja mais atualizada em relação ao **FINA040.**  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Efetue o download do pacote de expedição contínua do módulo financeiro, relacionado a release utilizada: **[Pacotes de Atualização - Financeiro - P12](https://tdn.totvs.com/x/HrCmHw)**  
2. Via Vs-Code, aplique a atualização, primeiramente em base de homologação para validar e posteriormente, em base de produção.   
3.Após a atualização, reinicie o smartclient e refaça o processo.

**Obs**: O tratamento indicado  requer conhecimento técnico de Vs-Code, caso necessite de apoio mais técnico, contate a equipe de Advpl.

**Clientes Cloud**, solicite a equipe de Atendimento Cloud para efetuar a atualização no ambiente.
