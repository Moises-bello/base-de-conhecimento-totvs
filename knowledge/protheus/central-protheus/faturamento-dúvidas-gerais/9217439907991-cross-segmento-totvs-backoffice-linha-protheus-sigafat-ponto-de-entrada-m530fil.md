---
article_id: 9217439907991
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 0c5f591e026413996b462e1f5b5c872861884dad1a32f8fcdfbfe3b7aec8e925
fetched_at: '2026-06-28T22:38:32.840778+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  M530FIL
type: support-article
updated_at: '2022-09-29T14:41:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9217439907991-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-M530FIL
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **M530FIL - Filtra vendedores.**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**

O ponto de entrada **M530FIL** existe na função **fa530Processa** e será disparado para **filtrar os vendedores** conforme os parâmetros dos clientes.  
  
**Exemplo**

```
User Function M530FIL()  
  
Local cFiltro := ""  
  
Alert("Entrou no Ponto de Entrada M530FIL")  
  
cFiltro:= "SE3->E3_VEND == '000001'"  
  
Return cFiltro
```

**Saiba Mais**

**[M530FIL - Filtra vendedores](https://tdn.totvs.com/x/BIZn)**
