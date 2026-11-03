---
article_id: 4402695530007
category: Escrita Fiscal - Error.log
content_hash: 1671cee8c0cd2eaaed9deda4c8b5f9c3ca554b915b92b549bdcf4ff378d200f8
fetched_at: '2026-06-28T22:39:32.950619+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: RH - Linha Protheus - GPE - Erro ao efetuar o fechamento da Folha - type mismatch
  on compare  on FORDAVALSR8(GPEM120.PRX)
type: support-article
updated_at: '2021-07-12T20:43:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402695530007-RH-Linha-Protheus-GPE-Erro-ao-efetuar-o-fechamento-da-Folha-type-mismatch-on-compare-on-FORDAVALSR8-GPEM120-PRX
---

**Ocorrência**Ao tentar efetuar o fechamento da folha, através da rotina **GPEM120** é gerado *error log*: "***type mismatch on compare on*** **FORDAVALSR8(GPEM120.PRX)**"  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**O erro ocorre por ter sido liberado uma versão da rotina de fechamento de folha (**GPEM120**), data de 18/05/2021 em diante, onde validava a ordenação fixa de campos da tabela **SR8.**  
  
**Solução**Para correção do erro será necessário aplicar a atualização do pacote abaixo. A data do **GPEM120** deve ficar a partir de **08/07/2021**, versão que passou a não validar a ordenação fixa dos campos da tabela **SR8**:  
12.1.17:<https://r.totvs.io/p/1031406> ;  
12.1.23:<https://r.totvs.io/p/1031407> ;  
12.1.25:<https://r.totvs.io/p/1031408> ;  
12.1.27:<https://r.totvs.io/p/1031409> ;  
  
**Informações complementares:**Pacote Expedição Contínua RH: [MP - GPE - Como fazer o download (baixar) do pacote de expedição continua (acumulado) do modulo Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854)  
Pacote Acumulado e-Social: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051585234>
