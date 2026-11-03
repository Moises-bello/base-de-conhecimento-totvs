---
article_id: 360020388711
category: ADVPL - Classe e Função
content_hash: ca274a2fbba02de82915cb66c43f221a5d3a5527e74cadcdc6893faf1735e9ad
fetched_at: '2026-06-28T22:40:19.450208+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Função que retorna
  a Picture do Campo
type: support-article
updated_at: '2022-01-10T22:08:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020388711-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-que-retorna-a-Picture-do-Campo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Qual a função utilizada para retornar a Picture de um campo da SX3.  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – Advpl – A partir da versão 11.80  
  
**Solução**A função responsável pelo retorno da Picture do campo da Sx3 é a PesqPict().  
 *Parâmetros*PesqPict( "alias", "Campo")

**Exemplo**

```
#INCLUDE "TOTVS.CH"  
   
User Function PesqPict()  
Local cAlias := 'SD2'  
Local cCampo := 'D2_QUANT'  
   
MsgInfo( 'Valor: ' + cAlias+'/'+cCampo + CRLF + "Retorno: " + PesqPict( cAlias, cCampo ), 'TESTE' )  
Return( Nil )
```
