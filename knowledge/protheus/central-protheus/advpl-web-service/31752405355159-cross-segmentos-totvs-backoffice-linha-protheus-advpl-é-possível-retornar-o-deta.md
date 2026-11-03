---
article_id: 31752405355159
category: ADVPL - Web Service
content_hash: b9c343cf0f40926d9a9f86133c5a32ae28f506e52d8083d2c1d0c61792e45adb
fetched_at: '2026-06-28T22:40:10.585620+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - É possível retornar
  o detalhe da mensagem de erro utilizando a função SetRestFault em APIs TLPP?
type: support-article
updated_at: '2025-05-14T11:36:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31752405355159-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-%C3%89-poss%C3%ADvel-retornar-o-detalhe-da-mensagem-de-erro-utilizando-a-fun%C3%A7%C3%A3o-SetRestFault-em-APIs-TLPP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31752405341847) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**É possível retornar o detalhe da mensagem de erro utilizando a função SetRestFault em APIs TLPP?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões   
  
**Solução**Em TLPP, não temos o TTALK como no AdvPL, dessa forma, não é possível utilizar o parâmetro cDetailMsg para retornar os detalhes da mensagem de erro utilizando a função SetRestFault. Logo, em APIs TLPP, pode ser utilizado o SetFault para atender a necessidade.  
\*Importante possuir a configuração do REST TLPP para o funcionamento. 

\*\*O TTALK mencionado acima é responsável por padronizar as mensagens trocadas entre os diversos produtos de diferentes marcas da Totvs. No TLPP, o TTALK não existe, ficando a critério do desenvolvedor responsável padronizar as mensagens. Para maiores detalhes, veja na seção Saiba mais.  
  
Exemplos:

```
#include "tlpp-core.th"
#include "tlpp-rest.th"

@Get("/documentation/setFault")
Function u_fSetFault()
    Local cResponse := ""
    Local lRet      := ""

    cResponse := '{"setFault": "método setFault executado com sucesso, mensagem de retorno padrao alterada"}'
    lRet := oRest:setFault(cResponse)
return .T.
```

**Saiba mais  
[SetRestFault](https://tdn.totvs.com/display/public/framework/SetRestFault)  
[SetFault](https://tdn.totvs.com/display/tec/oRest%3AsetFault)  
[REST Tlpp](https://tdn.totvs.com/display/tec/Via+INI)  
[TTALK](https://tdn.totvs.com/pages/releaseview.action?pageId=453308173)**
