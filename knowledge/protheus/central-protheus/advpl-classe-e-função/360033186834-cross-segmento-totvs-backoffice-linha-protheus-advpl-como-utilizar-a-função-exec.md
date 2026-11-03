---
article_id: 360033186834
category: ADVPL - Classe e Função
content_hash: 068f9095bfca33383524dbb32d092314d28f9725963c500fde66376a1b06226f
fetched_at: '2026-06-28T22:40:15.574680+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Como utilizar a
  função ExecBlock() durante a integração com planilha Excel
type: support-article
updated_at: '2022-03-23T11:14:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033186834-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-utilizar-a-fun%C3%A7%C3%A3o-ExecBlock-durante-a-integra%C3%A7%C3%A3o-com-planilha-Excel
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como utilizar a função ExecBlock() durante a integração com planilha Excel para execução de funções customizadas?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Solução**É necessário macro executar o conteúdo do parâmetro enviado via PARAMIXB:

```
#Include "TOTVS.ch"  
  
User Function MOVFAT()  
 Local aContent := &(PARAMIXB)  
 Local cMessage := "NOME: " + aContent[1] + " | IDADE: " + CValToChar(aContent[2])  
Return (cMessage)
```

Na célula a sintaxe ficará desta forma:

```
ExecBlock("MOVFAT"; "{'Gil', 45}")
```

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042521894/mceclip0.png)  
  
**Saiba mais**[Funções utilizadas na Integração Siga Protheus - Excel](http://tdn.totvs.com/pages/viewpage.action?pageId=185751753)
