---
article_id: 360060285114
category: LEGAIS - BLOCO H/MATR460
content_hash: d48d226d8fbdc410cfecbdce41c7bb52266adaa853da760b30aa2451f2ae4419
fetched_at: '2026-06-28T22:42:15.021037+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Bloco H - THREAD
  ERROR - Invalid data type on (ALQ_PICM) on BLOCOH460(MATXSPED.PRW) '
type: support-article
updated_at: '2021-06-14T14:21:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060285114-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Bloco-H-THREAD-ERROR-Invalid-data-type-on-ALQ-PICM-on-BLOCOH460-MATXSPED-PRW
---

**Dúvida**Ao gerar o SPED Fiscal com Bloco H é gerado o error.log THREAD ERROR - Invalid data type on (ALQ\_PICM) on BLOCOH460(MATXSPED.PRW). O que fazer para resolver?  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da versão 12.1.17  
**Solução**Para solucionar este problema, siga os passos abaixo:

**1. Revise os passos feitos na geração do Bloco H.**

Gere o Relatório MATR460 - Registro de Inventário Modelo 7 (P7) preenchendo as perguntas conforme abaixo:  
**- Gerar Exp. SPED FISCAL** = Sim;  
**- Data de fechamento de estoque** = 31/12/2020 (Data de quando o inventário foi fechado);  
**- Nome Arq. Gerado no Reg. In. MOD 7** =  20201231 (Data de fechamento do inventário).

**Observação**: A data é meramente ilustrativa.

O sistema irá gravar no Banco de Dados as informações referentes ao relatório MATR460 na tabela H\_20201231 + grupo + filial. Após abrir e conferir, **f****eche a tabela em H\_ em sua base de dados.**

Gere o arquivo do Sped Fiscal verificando as perguntas abaixo:  
**- Gera Inventário** = Sim;  
**- Data de fechamento do estoque** = Data em que foi feito o fechamento do estoque, 31/12/2020;  
**- Motivo do Inventário** = 01-Final do Período.

Com isso, provavelmente este error.log não será mais apresentado e o arquivo Sped será gerado normalmente.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Bloco H e MATR460 (P7) no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033001-SIGAEST-LEGAIS)*
