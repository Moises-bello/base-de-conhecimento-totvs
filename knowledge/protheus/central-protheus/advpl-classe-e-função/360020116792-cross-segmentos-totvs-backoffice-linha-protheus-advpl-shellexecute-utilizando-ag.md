---
article_id: 360020116792
category: ADVPL - Classe e Função
content_hash: ed589f2a4c725b2df47c7624ddc9d9b45f68a77f561c434e81761d758f420208
fetched_at: '2026-06-28T22:40:20.558878+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - ShellExecute utilizando
  agendador do Windows
type: support-article
updated_at: '2022-06-01T18:15:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020116792-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-ShellExecute-utilizando-agendador-do-Windows
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Criei uma rotina para executar uma linha de comando que dispara uma mensagem, utilizando a função ShellExecute não está funcionando?  
Exemplo:

```
ShellExecute( "Open", "C:\Windows\System32\cmd.exe", 'SCHTASKS /RUN /TN "\SPARK"',"C:\", 1 )
```

**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Causa**Caminho não foi encontrado.  
  
**Solução**Neste caso é necessário colocar o caminho do executável e verificar diretrizes do usuário, para utilização da função [**ShellExecute:**](http://tdn.totvs.com/display/tec/ShellExecute)

```
#Include 'Protheus.ch'  
  
User Function TshellExec()  
  
local cLinha:= "/RUN /TN SPARK"  
  
ShellExecute( "Open", "C:\Windows\System32\Schtasks.exe", cLinha,"C:\", 1 )  
  
Return
```
