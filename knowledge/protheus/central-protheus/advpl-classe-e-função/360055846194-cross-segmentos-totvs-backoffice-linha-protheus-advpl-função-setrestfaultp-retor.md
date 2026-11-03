---
article_id: 360055846194
category: ADVPL - Classe e Função
content_hash: e5f2ae39b0dd25673a1121ec01a79acc4bb95b9ba1e992e6a06b726e4b37198d
fetched_at: '2026-06-28T22:40:19.463489+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Função SetRestFaultP():
  Retorno no formato Json'
type: support-article
updated_at: '2022-01-10T22:16:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055846194-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-SetRestFaultP-Retorno-no-formato-Json
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**O conteúdo da função **SetRestFaultP()** não está saindo em **Json**, como fazer pra sair?   
Exemplo esperado:

```
{  
errorCode: 400,  
errorMessage: Erro ao incluir solicitação de armazém,  
detailedMessage: Filial 4444 não encontrada  
}
```

**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17

**Solução**O parâmetro **lJson** da função **SetRestFault** diz respeito ao retorno no formato **JSON** no método **REST**, não sobre o conteúdo do parâmetro **cMessage**. Exemplo;

```
//--------------------------------------  
// Verifica se a saída é JSON  
//--------------------------------------  
  
If ::cFormat <> "json"  
    lRetorno := .F.  
    SetRestFault(002,STR0002) //"Somente o formato json é permitido"  
EndIf  
If lRetorno  
    ...  
    ::cResponse := cJson      
EndIf  
Return(lRetorno)
```

**Saiba mais**[SetRestFault](https://tdn.totvs.com/pages/editpage.action?pageId=75269463)
