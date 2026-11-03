---
article_id: 360028078052
category: ADVPL - Classe e Função
content_hash: 914726231ad20791331060e6916d127b9674ace65441c4adef541bf4f5897fed
fetched_at: '2026-06-28T22:40:15.617656+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Comportamento da
  função FUNNAME()
type: support-article
updated_at: '2022-01-05T14:18:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028078052-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Comportamento-da-fun%C3%A7%C3%A3o-FUNNAME
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**A função **FUNNAME**(), não está trazendo o conteúdo correto, impedindo de realizar validações através da função.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Solução**Quando executamos uma rotina direto no protheus, onde não é necessário preparar o ambiente, a **FUNNAME**() ira trazer o nome da função que da inicio ao processo

**Exemplo:**

```
User function CustomExc()  
  
MSExecAuto({|k,v,w,x,y,z| MATA120(k,v,w,x,y,z)},1,aCabec,aItens,3,,/*aRatCC*/)  
  
return
```

Nesse caso a **FUNNAME**() ira retornar "**CustomExc**".  
Quando temos uma customização onde precisamos prepara o ambiente, o comportamento é diferente, pois se não informar os parâmetros  que referenciam o nome da função, o sistema irá trazer por padrão o nome "**RPC**"  
Exemplo:

```
User function CustomExc()  
  
PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01" MODULO "FAT"   
  
  MSExecAuto({|k,v,w,x,y,z| MATA120(k,v,w,x,y,z)},1,aCabec,aItens,3,,/*aRatCC*/)  
  
RESET ENVIRONMENT  
  
return
```

ou

```
User function CustomExc()  
  
RPCSetEnv("99" , "01",,,"FAT",,,,,,)  
  
  MSExecAuto({|k,v,w,x,y,z| MATA120(k,v,w,x,y,z)},1,aCabec,aItens,3,,/*aRatCC*/)  
  
return
```

Nesse caso a **FUNNAME**() irá retornar "RPC".  
Para informar o nome que será enviado para a variável **cFunname,**você pode preparar o ambiente da seguinte forma

**Exemplo:**

```
RPCSetEnv("99" , "01",,,"FAT","MATA120",,,,,)
```

ou

```
PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01" MODULO 'FAT' FUNNAME 'MATA120'
```

**Saiba mais**[FunName](http://tdn.totvs.com/pages/releaseview.action?pageId=6814875)  
[Prepare Environment](http://tdn.totvs.com/pages/releaseview.action?pageId=6814708)  
[RpcSetEnv - Abertura do ambiente em rotinas automáticas](http://tdn.totvs.com/pages/releaseview.action?pageId=6814927)
