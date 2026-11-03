---
article_id: 21713949195031
category: ADVPL - Classe e Função
content_hash: e0291dd6398930a00a055eab2de5619085c5e6668c33b4a1e7f6dcd318581ae6
fetched_at: '2026-06-28T22:40:21.510893+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL- Abertura de ambiente
  em rotinas customizadas via schedule
type: support-article
updated_at: '2024-06-07T15:18:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21713949195031-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Abertura-de-ambiente-em-rotinas-customizadas-via-schedule
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21713949166999) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Como deve ser feita abertura de ambiente em rotinas customizadas acionadas por schedule?  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**

Pode ser usado a função *scheddef*, ela irá abrir o ambiente automaticamente e irá usar as informações de empresa/filial cadastradas no schedule.   
Ou a abertura de ambiente no Schedule pode usar as funções como **(RpcSetEnv e Prepare Environment)**, neste caso, o ideal é sempre validar se já existe comunicação ativa com o banco de dados, antes da tentativa abertura do ambiente no schedule.

**Exemplo**

```
if Type("cFilAnt") == "C" .and. Type("cEmpAnt") == "C" .and. Type("dDataBase") == "D" .and. TCIsConnected()  
    //Ambiente já aberto com conexão no banco de dados  
else  
    //Ambiente encontra-se fechado ou nunca foi aberto  
endif
```

**Saiba Mais**

[Schedule](https://tdn.totvs.com/pages/releaseview.action?pageId=271167961)

[Scheddef](https://tdn.totvs.com/pages/releaseview.action?pageId=36800166)

[Funcionamento SchedDef no Schedule](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21895227246871/preview/eyJhbGciOiJIUzI1NiJ9.eyJpZCI6MjE4OTUyMjcyNDY4NzEsImV4cCI6MTcwOTkyNDQ1Nn0.JhaNB0Vgoy663U-fOipdtPKimu1FbYl8zZ1Ttk2vrE4)

[TCIsConnected](https://tdn.totvs.com/display/tec/TCIsConnected)
