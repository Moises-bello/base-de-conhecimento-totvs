---
article_id: 360025440391
category: ADVPL - Classe e Função
content_hash: 0d1d1a81589df6e9b7a445bef3dc1c11a0c842388f2b8c37092ea660649ebb7e
fetched_at: '2026-06-28T22:40:15.507497+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Como bloquear edição
  TGet
type: support-article
updated_at: '2022-01-04T20:10:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025440391-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-bloquear-edi%C3%A7%C3%A3o-TGet
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Preciso bloquear um campo de edição para o usuário em uma customização através do TGET.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Solução**Para bloquear a edição de um campo customizado criado pela **Classe TGet,** é necessário utilizar o parâmetro **lReadOnly** do construtor **New(),** onde recebe .T.(bloqueia edição) ou .F.(permite edição).

**Exemplo:**

```
User Function TDialog()  
  
// cria diálogo  
Local oDlg :=TDialog():New(180,180,550,700,'Exemplo TDialog',,,,,CLR_BLACK,CLR_WHITE,,,.T.)  
Local cTGet1 :="Teste TGet 01"  
  
//cria TGET  
Local oTGet1 :=TGet():New( 01,01,{||cTGet1},oDlg,096,009,"@!",,0,,,.F.,,.T.,,.F.,,.F.,.F.,,.F./*lReadOnly*/,.F.,,cTGet1,,,,)  
  
//Valida o usuario   
If __cUserId == "000003"  
  oTGet1 := TGet():New( 01,01,{||cTGet1},oDlg,096,009,"@!",,0,,,.F.,,.T.,,.F.,,.F.,.F.,,.T./*lReadOnly*/,.F.,,cTGet1,,,,)  
Endif  
  
// ativa diálogo centralizado  
oDlg:Activate()  
  
Return
```

**Saiba mais**[Classe TGet](http://tdn.totvs.com/display/tec/TGet)  
[Classe TDialog](http://tdn.totvs.com/display/tec/TDialog)
