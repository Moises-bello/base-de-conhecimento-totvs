---
article_id: 360044775973
category: ADVPL - Rotina Automática
content_hash: 829fda060d92e33aa2f05f2fbde42b7617343084fb810cfd29439b79370fad9e
fetched_at: '2026-06-28T22:40:23.964890+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Data de validade do Lote
  incorreta ExecAuto MATA242
type: support-article
updated_at: '2021-12-29T13:58:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044775973-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Data-de-validade-do-Lote-incorreta-ExecAuto-MATA242
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:02:00 min  
Dúvida** **ExecAuto** do **MATA242** está apresentando data de validade do Lote incorreta, como corrigir?  
  
**Ambiente**  
Protheus – ADVPL – A partir da versão 12  
  
**Solução**Este é o comportamento esperado da função **Execauto**, uma vez que é seguido a ordem do array que é passado na alimentação dos dados, no array montado para os itens que o cliente passou, o campo **D3\_DTVALID** esta depois do campo **D3\_LOTECTL** que é o campo que altera o valor do campo **D3\_DTVALID**, com isso o valor do campo **D3\_DTVALID** será alterado pois irá pegar o conteúdo informado no array abaixo:

```
aAutoItens := {{ {"D3_COD" , _cProdDest , Nil}, ;  
{"D3_LOCAL" , _cLocal , Nil}, ;  
{"D3_QUANT" , SB1->B1_CONV , Nil}, ;  
{"D3_LOTECTL", _cLote , Nil}, ;  
{"D3_DTVALID", _dDtValid , Nil}, ;  
{"D3_MOTMOV" , "01" , Nil}, ;  
{"D3_RATEIO" , 100 , Nil}, ;  
{"D3_LOCALIZ", Substr(cEnder,1,6) , Nil} };  
}
```

Para que o cliente tenha o comportamento esperado, o mesmo deve informar o campo **D3\_DTVALID** antes do **D3\_LOTECTL**, ficando assim o array:

```
aAutoItens := {{ {"D3_COD" , _cProdDest , Nil}, ;  
{"D3_LOCAL" , _cLocal , Nil}, ;  
{"D3_QUANT" , SB1->B1_CONV , Nil}, ;  
{"D3_DTVALID", _dDtValid , Nil}, ;  
{"D3_LOTECTL", _cLote , Nil}, ;  
{"D3_MOTMOV" , "01" , Nil}, ;  
{"D3_RATEIO" , 100 , Nil}, ;  
{"D3_LOCALIZ", Substr(cEnder,1,6) , Nil} };  
}
```

**Saiba Mais:**   
**[MATA242 - Rotina Automática de Desmontagem de Produtos](https://tdn.totvs.com/pages/releaseview.action?pageId=6087466)**
