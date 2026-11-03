---
article_id: 24245364581527
category: ADVPL - Classe e Função
content_hash: 972ca1763417c2bf130df65ad976214fa04e2e436e5dda86ee96c5f7a9996e54
fetched_at: '2026-06-28T22:40:21.517587+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL- Ao executar o menudef
  é convertido para letras maiúsculas sua leitura?
type: support-article
updated_at: '2024-06-18T19:22:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24245364581527-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ao-executar-o-menudef-%C3%A9-convertido-para-letras-mai%C3%BAsculas-sua-leitura
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24245364559639) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao executar o menudef é convertido para letras maiúsculas sua leitura?  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**

Por padrão o menudef é convertido para letras maiúsculas durante sua leitura, validação e execução.

Para situações como essa, recomendamos que a função seja encapsulada, mantendo assim o case das strings envolvidas.

**Exemplo**

```
Static Function MenuDef()  
Local aRotina := {}  
  
ADD OPTION aRotina TITLE 'Teste' ACTION 'U_xteste' OPERATION 7 ACCESS 0  
  
Return aRotina  
  
user function xteste()  
  
FWMsgRun(, {|oSay| ExecTest(oSay) }, "Processando", "Processando a rotina...")  
  
return
```

**Saiba Mais**

[Menudef](https://tdn.totvs.com/display/public/framework/MenuDef)
