---
article_id: 13519418884759
category: Financeiro - Cadastros
content_hash: d5fd37ca2d078fa9998732d71668c4fe3736b61a133e36f7ad95e101468acaa4
fetched_at: '2026-06-28T22:37:53.194593+00:00'
product: protheus
section_id: 1500001550722
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Financeiro - Habilitar
  novas colunas na FINC010
type: support-article
updated_at: '2023-03-31T22:24:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13519418884759-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Financeiro-Habilitar-novas-colunas-na-FINC010
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:10:00min****Dúvida**Como habilitar novas colunas na Consulta de Cliente FINC010?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**Para habilitar novas colunas na rotina **Consulta de Cliente** (**FINC010)** deve utilizar o ponto de entrada FC010HEAD   
  
**Exemplo:**  
#INCLUDE "PROTHEUS.CH"  
User function FC010HEAD()  
Local aHeader := Paramixb  
  
AADD(aHeader,{"TESTE","E1\_NCONTRA","@!",13,0,"","","C","SE1","" } )  
  
// Conteúdo das colunas  
// AllTrim(X3Titulo())  
// X3\_CAMPO  
// X3\_PICTURE  
// X3\_TAMANHO  
// X3\_DECIMAL  
// X3\_VALID  
// X3\_USADO  
// X3\_TIPO  
// X3\_ARQUIVO  
// X3\_CONTEXT  
  
Return aHeader  
  
**Saiba mais**  
[FC010HEAD - Inclui colunas](https://tdn.totvs.com/display/public/PROT/FC010HEAD+-+Inclui+colunas)
