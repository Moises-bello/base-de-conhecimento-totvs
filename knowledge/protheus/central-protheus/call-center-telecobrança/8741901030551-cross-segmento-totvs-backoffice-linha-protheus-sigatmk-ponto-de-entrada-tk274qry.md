---
article_id: 8741901030551
category: Call Center - Telecobrança
content_hash: 64f4873576ff321e6089cc883b1e151f758b45d0fcdfdcfcdfc7c0a9d657f9e1
fetched_at: '2026-06-28T22:41:28.707913+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGATMK - Ponto de Entrada
  TK274QRY
type: support-article
updated_at: '2022-09-08T20:05:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8741901030551-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Ponto-de-Entrada-TK274QRY
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **TK274QRY - Inclusão de novos filtros para busca de títulos vencidos.**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAPMS - A partir da release 12.  
  
**Solução**

Ele deve ser utilizado quando houver a necessidade de **inserir novos filtros** para a **busca de títulos** vencidos do cliente, através de uma expressão SQL, quando utilizada a seleção manual na telecobrança.  
  
**Exemplo**

```
User Function TK274QRY()  
  
    Local cQueryRet := ""  
  
    Alert('Acessado ponto de entrada TK274QRY!')      
  
    //Novo filtro para busca de títulos com tipo Boleto  
    cQueryRet := "K1_TIPO = 'BOL'"  
  
ReturncQueryRet
```

 **Saiba Mais**

**[TK274QRY - Inclusão de novos filtros para busca de títulos vencidos](https://tdn.totvs.com/x/OwBeBw)**

**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGATMK - Ponto de Entrada TMKA271ACG](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8741919551639-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Ponto-de-Entrada-TMKA271ACG)**
