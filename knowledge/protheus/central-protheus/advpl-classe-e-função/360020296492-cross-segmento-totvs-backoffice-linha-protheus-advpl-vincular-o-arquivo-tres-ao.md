---
article_id: 360020296492
category: ADVPL - Classe e Função
content_hash: d3d6b33130e6c35af2056f5eeb53bde5353a6710b297cc176941e433516eb58b
fetched_at: '2026-06-28T22:40:18.231591+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Vincular o arquivo
  .TRES ao .CH
type: support-article
updated_at: '2022-06-01T12:11:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020296492-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Vincular-o-arquivo-TRES-ao-CH
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:03:00 min   
  
Dúvida**Como vincular o arquivo .TRES (*Translate Resource*) a biblioteca .CH (*Clipper Header File*).  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 11.80  
  
**Solução**Atualmente o cliente não tem acesso aos arquivos de tradução .TRES dos fontes de relatórios do padrão, todavia a mesma biblioteca (arquivo .CH) pode trabalhar tanto da maneira legada quanto utilizando a função FwI18NLang().

No exemplo abaixo podemos ver como funciona a estrutura de um arquivo .TRES e .CH customizado para trabalhar tanto da nova forma, quanto no formato legado.  
  
FONTE: TRADSTR.PRW

```
// BIBLIOTECAS NECESSÁRIAS  
#Include "TOTVS.ch"  
#Include "TRADSTR.ch" // BIBLIOTECA CUSTOMIZADA  
  
// FUNÇÃO PARA TESTE DE DEFINIÇÕES DE LINGUAGEM  
User Function TRADSTR()  
    MsgInfo(STR0001, "Strings de T14STR.ch") // DEFINIÇÃO COM FWI18NLANG()  
    MsgInfo(STR0003, "Strings de T14STR.ch") // DEFINIÇÃO LEGADO  
Return (NIL)
```

BIBLIOTECA: TRADSTR.CH

```
#DEFINE STR0001 FWI18NLang("TRADSTR", "STR0001", 1)  
#DEFINE STR0002 FWI18NLang("TRADSTR", "STR0002", 2)  
#DEFINE STR0003 "ALTERADO"
```

ARQUIVO: TRADSTR\_pt-br.TRES

```
0001#STR0001#ALL#Variavel Teste I  
0002#STR0002#ALL#Variavel Teste II
```

**Saiba mais**  
[Nova estrutura de tradução do Protheus - arquivos .CH](http://tdn.totvs.com/pages/viewpage.action?pageId=181965465)
