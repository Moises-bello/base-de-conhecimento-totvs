---
article_id: 360028453391
category: ADVPL - Classe e Função
content_hash: d826c54c864fe4ead1a429763ed7d358118e42c1e9022bb89621d7e28e6ce8cf
fetched_at: '2026-06-28T22:40:17.040176+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - MostraErro em branco
  na rotina automática mata103
type: support-article
updated_at: '2022-03-21T11:57:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028453391-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-MostraErro-em-branco-na-rotina-autom%C3%A1tica-mata103
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:04:00 min  
  
Ocorrência**Quando ocorrido algum erro durante a execução da rotina automática MATA103, a caixa de diálogo da função MostraErro() é exibida em branco.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Causa**O uso da variável lAutoErrNoFile == .T. no fonte MATA103.prw desviava o fluxo da mensagem de erro que seria enviada para a função MostraErro() para a variável \_\_aErrAuto.  
  
**Solução**Removida a declaração da variável no fonte padrão MATA103.prw em datas inferiores à 15/03/2019.  
Para realizar o download do pacote de correção, [clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=742099).  
 **Observação**É necessário o uso da função MsExecAuto() para realizar a chamada da rotina automática MATA103, caso a rotina seja executada diretamente, a caixa de diálogo da função continuará em branco.  
  
Certo

```
MSExecAuto({|x, y, z| MATA103(x, y, z)}, aCabec, aItens, 3)
```

Errado

```
MATA103(aCabec, aItens, 3)
```

**Saiba mais**  
[5211923 DMANMAT02-16356 DT Help apresentado sem texto](http://tdn.totvs.com/display/PROT/5211923+DMANMAT02-16356+DT+Help+apresentado+sem+texto)  
[GetAutoGRLog - retorno de array durante a execução da rotina automática](http://tdn.totvs.com/pages/releaseview.action?pageId=6815090)
