---
article_id: 17828188765719
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: d028ecb261d87753af9421de77a34206ad7a96cb139e7b433965f25415351039
fetched_at: '2026-06-28T22:38:42.787030+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  MTA455P
type: support-article
updated_at: '2023-09-26T17:14:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17828188765719-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-MTA455P
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17828173832983) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **MTA455P - Validar liberação de estoque**.  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**

Valida a Liberação de Estoque  
Executado após liberação do estoque, e impede a liberação dependendo do retorno.  
  
**Exemplo**

```
User Function MTA455P()  
  
    Local lRet := .F.   //Conteudo de retorno  
  
    If MsgYesNo("Confirma a liberacao de estoque?", "PE MTA455P")  
        lRet := .T.  
        Alert("Passou pelo Ponto de Entrada MTA455P, liberacao confirmada") //Clicou no Sim  
    Else  
        lRet := .F.  
        Alert("Passou pelo Ponto de Entrada MTA455P, liberacao nao confirmada") //Clicou no Não  
    EndIf  
  
Return(lRet)
```

**Saiba Mais**

**[MTA455P - Validar liberação de estoque](https://tdn.totvs.com/x/m4Vn)**
