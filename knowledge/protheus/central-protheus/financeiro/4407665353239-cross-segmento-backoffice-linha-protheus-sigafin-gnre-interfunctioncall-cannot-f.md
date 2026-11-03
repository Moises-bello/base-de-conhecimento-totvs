---
article_id: 4407665353239
category: Financeiro
content_hash: d38d9c8938fe941cdc611819b53e68af64ae8451e972711400f8cc0d5b259318
fetched_at: '2026-06-28T22:38:01.130945+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus -SIGAFIN - GNRE - InterFunctionCall:
  cannot find function FINCBLD in AppMap on GETLISTBOX(FISA095.PRW)'
type: support-article
updated_at: '2021-09-02T17:55:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407665353239-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-GNRE-InterFunctionCall-cannot-find-function-FINCBLD-in-AppMap-on-GETLISTBOX-FISA095-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **05 min****Ocorrência**Ao acessar o monitor da GNRE WS ( **FISA095**) ocorren erro.log  
InterFunctionCall: cannot find function FINCBLD in AppMap on GETLISTBOX(FISA095.PRW)Ambiente

**Ambiente**Cross Segmento - Backoffice Linha Protheus – Financeiro – A partir da versão 12.1.25

**Causa**O erro ocorre por que falta a função **FINCBL  - cannot find function FINCBLD**  
  
**Solução**Para solucionar, os pacotes abaixo devem ser aplicados, conforme abaixo:

**Pacote release 12.1.25**

1° Aplicar os dois pacotes primeiramente:

12.1.25:<https://r.totvs.io/p/1005199>

12.1.25:<https://r.totvs.io/p/1006371>

2° Aplicar o pacote

12.1.25:<https://r.totvs.io/p/1001508>

**Pacote release 12.1.27**1° Aplicar os dois pacotes primeiramente:

12.1.27:<https://r.totvs.io/p/1030446>

12.1.27:<https://r.totvs.io/p/1006372>   
  
2° Aplicar o pacote

12.1.27:<https://r.totvs.io/p/1001509>

**Saiba mais**  
Mantenha o Modulo Financeiro atualizado  
[MP - SIGAFIN - Atualização do Ambiente Modulo Financeiro - Modulo 06 - Acumulado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056740354-MP-SIGAFIN-Atualiza%C3%A7%C3%A3o-do-Ambiente-Modulo-Financeiro-Modulo-06-Acumulado?source=search)
