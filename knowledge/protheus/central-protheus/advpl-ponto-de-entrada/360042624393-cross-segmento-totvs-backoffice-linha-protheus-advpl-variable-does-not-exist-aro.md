---
article_id: 360042624393
category: ADVPL - Ponto de Entrada
content_hash: 9575767183264645453d1cef44947b72462f2e1fe155bebb1eba4fb029d0b655
fetched_at: '2026-06-28T22:40:12.916877+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - variable does not
  exist AROTINA on U_MA080MNU
type: support-article
updated_at: '2021-12-30T18:10:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042624393-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-variable-does-not-exist-AROTINA-on-U-MA080MNU
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Ao utilizar o PE **MA080MNU** o sistema retorna o erro abaixo

```
variable does not exist AROTINA on U_MA080MNU
```

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.25  
  
**Causa**Correção na chamada do ponto **MA080MNU** para receber o **aRotina** por parâmetro e dessa forma possibilitar o cliente incluir novos menus.  
  
**Solução**Utilize o exemplo abaixo:

```
#INCLUDE "rwmake.ch"  
#INCLUDE "Topconn.ch"  
#INCLUDE "protheus.ch"  
#INCLUDE "FWMVCDEF.CH"  
   
   
User Function MA080MNU()  
   
Local aRotina := ParamIxb[1]  
   
 ADD OPTION aRotina TITLE "opção adicionada 01" ACTION 'A080Manut' OPERATION 2 ACCESS 0 //"Visualizar"  
 ADD OPTION aRotina TITLE "opção adicionada 02" ACTION 'A080Manut' OPERATION 2 ACCESS 0 //"Visualizar"  
 ADD OPTION aRotina TITLE "opção adicionada 03" ACTION 'A080Manut' OPERATION 2 ACCESS 0 //"Visualizar"  
 ADD OPTION aRotina TITLE "opção adicionada 04" ACTION 'A080Manut' OPERATION 2 ACCESS 0 //"Visualizar"  
 ADD OPTION aRotina TITLE "opção adicionada 05" ACTION 'Alert("PE MA080MNU")' OPERATION 4 ACCESS 0 //"Executa Função"  
   
Return aRotina
```

**Saiba mais**  
[MA080MNU](https://tdn.totvs.com/pages/releaseview.action?pageId=525029733)
