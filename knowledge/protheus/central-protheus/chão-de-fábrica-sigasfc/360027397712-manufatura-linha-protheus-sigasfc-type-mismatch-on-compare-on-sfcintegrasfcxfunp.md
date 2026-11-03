---
article_id: 360027397712
category: Chão de Fábrica (SIGASFC)
content_hash: c951c941662bc489dcc8d9454c1f367558f7106c05137d1e6371e2644aeac63d
fetched_at: '2026-06-28T22:42:49.892639+00:00'
product: protheus
section_id: 360005696234
source: central-protheus
title: Manufatura - Linha Protheus - SIGASFC - Type mismatch on compare  on SFCINTEGRA(SFCXFUN.PRW)
type: support-article
updated_at: '2023-07-05T16:49:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027397712-Manufatura-Linha-Protheus-SIGASFC-Type-mismatch-on-compare-on-SFCINTEGRA-SFCXFUN-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:51 min****Ocorrência**Ao executar o **UPDDISTR** ocorre o erro **Type mismatch on compare on SFCINTEGRA(SFCXFUN.PRW).**  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Chão de Fábrica (SIGASFC) - Versão 12   
  
**Causa**Esta mensagem ocorre quando o parâmetro **MV\_INTSFC - Define se existe integração entre o Módulo SIGASFC e outros módulos** **0=Nao integra; 1=Protheus; 2=Datasul** está com o campo **Tipo** definido como **1 - Lógico**.  
  
**Solução**Para que esta mensagem não seja exibida é necessário alterar o **Tipo** do parâmetro **MV\_INTSFC** para **2 - Numérico**.  
Para isso abra a tabela **SX6 - Parâmetros** através do **APSDU** e altere o campo **X6\_TIPO** para **N**.  
  
**Importante**  
Para informar que não existe integração com outros módulos, o parâmetro deve ter conteúdo igual à **0=Não integra**.
