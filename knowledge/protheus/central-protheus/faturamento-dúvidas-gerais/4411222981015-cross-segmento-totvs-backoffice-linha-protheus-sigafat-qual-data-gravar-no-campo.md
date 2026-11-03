---
article_id: 4411222981015
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 2b36e1fcf545b965bc9686565e73171414dc5b2a41b236428b57325296e72c83
fetched_at: '2026-06-28T22:38:28.659911+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - Qual data gravar
  no campo F2_DTLANC
type: support-article
updated_at: '2022-05-11T17:53:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411222981015-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Sigafat-Qual-data-gravar-no-campo-F2-DTLANC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Na Contabilização do Modulo Faturamento, qual data o sistema gravará no campo F2\_DTLANC ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Faturamento - Todas as versões  
  
**Solução**  
**Contabilização Off Line**

Para que a contabilização Off-Line (**CTBANFS**) respeite a data de emissão do campo **F2\_EMISSÃO** na gravação dos campos **CT2\_DATA** e **F2\_DTLANC**verifique a configuração abaixo:  
  
**Pergunta (Gera Lanc. Por?)**  
     Deve-se configura-la com o conteúdo "Dia" ou "Documento"  
![](https://totvssuporte.zendesk.com/attachments/token/HBqzNqjMP8EWDhceo55yGv3rM/?name=inline-445814069.png)​  
**Parâmetro SX6 - MV\_CTBFLAG**  
​     Deve-se configurar com o conteúdo igual a .F.  
  
Caso deixe configurado diferente, a contabilização Off Line grava o dia que houve a Contabilização (não é o dia que emitiu a NF), isto é, grava um lote de Nfs com a mesma data (database do sistema).  
  
**Contabilização On Line**On Line grava a data da geração da NF, pois a gravação é feita no momento da sua geração. 

Para mais informações sobre a contabilização no Faturamento, acesse: **[Integração Faturamento X SigaCtb (SIGAFAT)](https://tdn.totvs.com/x/W2nXIQ)**
