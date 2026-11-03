---
article_id: 16539544944535
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 355d213c8bf8bd1d5b6b206e159e393c5cc2ab943b3b49e2ab32a8f661209f97
fetched_at: '2026-06-28T22:38:45.437316+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  M461LSF2
type: support-article
updated_at: '2023-08-22T20:10:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16539544944535-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-M461LSF2
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16539539770391) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **M461LSF2 - Alteração de dados da tabela SF2**.  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**

Este ponto de entrada pertence à rotina de geração de notas fiscais, **MATA461()**.  
Está localizado na rotina de **gravação da nota fiscal**, é executado **após a gravação** dos dados da nota possibilitando alterar dados da **tabela SF2**.  
O ponto de entrada **não recebe parâmetros** e as tabelas estão devidamente preparadas para manipulação.  
  
**Exemplo**

```
#INCLUDE "PROTHEUS.CH"  
  
User Function M461LSF2()  
      
MsgInfo("TESTE Campo XX_XXXXXX", "Ponto de Entrada M461LSF2")  
  
Return
```

**Saiba Mais**

**[M461LSF2 - Alteração de dados da tabela SF2](https://tdn.totvs.com/x/zoRn)**
