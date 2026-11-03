---
article_id: 38437263034007
category: Gestão de Contratos (SIGAGCT)
content_hash: bc25bd1c1ca7e01aac429e8245a2e4abbdaa15ee75d165e6cf4a968834d2c131
fetched_at: '2026-06-28T22:36:25.937770+00:00'
product: protheus
section_id: 1500001545522
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Ao tentar visualizar
  ou estornar a medição ocorre Error log "variable does not exist C7_FORNECE"
type: support-article
updated_at: '2026-02-16T20:13:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38437263034007-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Ao-tentar-visualizar-ou-estornar-a-medi%C3%A7%C3%A3o-ocorre-Error-log-variable-does-not-exist-C7-FORNECE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38437316529303) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
  
Ao tentar visualizar ou estornar a medição ocorre Error log variable does not exist C7\_FORNECE on {|a,b,c| FWInitCpo(a,b,c),xRet:=(POSICIONE("SA5",1,XFILIAL("SA5")+SC7->(C7\_FORNECE+C7\_LOJA+C7\_PRODUTO),"A5\_CODPRF")),FWCloseCpo(a,b,c,.T.),FwSetVarMem(a,b,xRet),xRet }  
  
**Ambiente**  
  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de contratos - Todas as versões  
  
**Causa**  
  
Esse incidente ocorre, pois a validação que foi informada no campo está incorreta.  
  
**Solução**  
  
1. Pesquise no erro pela validação apresentada na linha de estouro do erro conforme exemplo abaixo:

**FWInitCpo(a,b,c),xRet:=(POSICIONE("SA5",1,XFILIAL("SA5")+SC7->(C7\_FORNECE+C7\_LOJA+C7\_PRODUTO),"A5\_CODPRF")),FWCloseCpo(a,b,c,.T.),FwSetVarMem(a,b,xRet),xRet }**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38437263023767)

2. Na stack do erro será apresentado o nome do campo que está com erro na validação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38437263024023)

3. Realize o ajuste da validação do campo , para realização de um novo teste.Nesse exemplo o campo apresentado é customizado ,se no seu cenário o caso o campo seja customizado **X3\_PROPRI = U** realize um teste sem o campo customizado.

Caso erro persista após validações acima , abra um ticket em um de nossos canais de atendmento com o arquivo de erro atualizado para análise de equipe de suporte.

**Saiba Mais:**

[Guia de Referencia - Gestão de Contratos - Protheus 12](https://tdn.totvs.com/pages/viewpage.action?pageId=224127467)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
