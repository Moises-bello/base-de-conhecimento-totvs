---
article_id: 27991402630679
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 875316ef65be4b8913a82b635e36c0b96a0678d977a6aa05a7e29c0b47a9fee2
fetched_at: '2026-06-28T22:38:39.782607+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Error.log citando o fonte
  ADDRULES no faturamento
type: support-article
updated_at: '2024-11-22T17:51:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27991402630679-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Error-log-citando-o-fonte-ADDRULES-no-faturamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27991366396823) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Error.log citando o fonte ADDRULES no faturamento, como resolver?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
  
**Solução**

Exemplo do erro:

```
erro no parâmetroFWFormModel:  
Desative a classe (DeActivate) para utilizar este método on FWFORMMODEL:ADDRULES(FWFORMMODEL.PRX)
```

1 - Procure no error.log pelo fonte presente no cabeçalho do erro (no topo) "FWFORMMODEL:ADDRULES(FWFORMMODEL.PRX)"

2 - Veja qual campo se destaca mais, exemplo abaixo são os Campos "(A1\_LAUDOEM)" e "(A1\_LAUEMAI)":

```
STACK FWFORMMODEL:ADDRULES(FWFORMMODEL.PRX) 17/05/2024 16:58:37  
  
Param 1: CIDSUBMODEL(C) : SA1MASTER  
Param 2: CIDFIELD(C) : A1_LAUEMAI  
Param 3: CIDTARGETSUBMODEL(C) : SA1MASTER  
Param 4: CIDFIELDTARGET(C) : A1_LAUDOEM  
Param 5: NTYPE(N) : 2  
Local 1: CIDSUBMODEL(C) :SA1MASTER  
Local 2: CIDFIELD(C) :A1_LAUEMAI  
Local 3: CIDTARGETSUBMODEL(C) :SA1MASTER  
Local 4: CIDFIELDTARGET(C) :A1_LAUDOEM  
Local 5: NTYPE(N) :2  
Local 6: SELF(O) :O  
Local 7: OSTART(U) :NIL  
Local 8: OTARGET(U) :NIL
```

3 - Vá no configurador, nos campos em questão, edite-os na aba "Dependências" e remova a dependência inserida:

![CHM_20636622.png](https://totvssuporte.zendesk.com/attachments/token/3nfQN5BDJl54d9LF2czfQ5lcN/?name=CHM_20636622.png&lotus_request=true)

Dúvidas em como realizar essa alteração, contate a Equipe Protheus Framework
