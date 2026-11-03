---
article_id: 360018425712
category: ADVPL - Classe e Função
content_hash: 3fa0c8530e637c064e25991e36fc4104d655f402ef94b698af0887e83679d356
fetched_at: '2026-06-28T22:40:15.622107+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Comportamento de
  Case-sensitive na função CpyT2S
type: support-article
updated_at: '2024-04-26T11:05:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018425712-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Comportamento-de-Case-sensitive-na-fun%C3%A7%C3%A3o-CpyT2S
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23062616058391)Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Estou tentando utilizar a função **CpyT2S** para copiar alguns arquivos **.xml** do meu servidor de uma pasta outra. O sistema consegue copiar corretamente, porém não respeita o nome do arquivo que possui letras maiúsculas.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80

**Solução**A função **CpyT2S** possui o 4° parâmetro ***lChangeCase***que, se informado verdadeiro (.T.), nomes de arquivos e pastas serão convertidos para letras minúsculas, caso contrário, falso (.F.), não será feito nenhum ajuste no nome do arquivo informado. O parâmetro não é obrigatório e possui valor *default*(.T.) ou seja, quando não informado, o nome da cópia do arquivo será criado em letras minúsculas.   
Segue exemplo de utilização onde não é feita nenhuma modificação no nome do arquivo copiado:

```
User Function TSTCOPY()  
local lRet := .F.  
  
lRet := CpyT2S( "C:\TEMP\MANUAL.DOC", "\BKP", .F., .F. )  
  
If lRet  
 Alert("Arquivo copiado com sucesso")  
Else  
 Alert("Arquivo não copiado")  
EndIf  
  
Return
```

**Saiba Mais**

**[CpyS2T](https://tdn.totvs.com/display/tec/CpyS2T)  
[CpyT2S](https://tdn.totvs.com/display/tec/CpyT2S)  
[CpyS2TEx](https://tdn.totvs.com/display/tec/CpyS2TEx)  
[CpyS2TW](https://tdn.totvs.com/display/tec/CpyS2TW)  
[Demais funções de manipulação de arquivos](https://tdn.totvs.com/pages/viewpage.action?pageId=6063692)**
