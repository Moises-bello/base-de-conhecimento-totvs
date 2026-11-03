---
article_id: 23664227112215
category: RH - Provisão
content_hash: 02d74baf2e33c5ca8652d4276c55e51825dadd2d3fb3f7e9da036c1ab1d0a646
fetched_at: '2026-06-28T22:43:56.731092+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Provisão de Férias e 13º Salário não Calcula FGTS
type: support-article
updated_at: '2025-06-13T20:12:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23664227112215-RH-Linha-Protheus-GPE-Provis%C3%A3o-de-F%C3%A9rias-e-13%C2%BA-Sal%C3%A1rio-n%C3%A3o-Calcula-FGTS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23664227082519) Tempo aproximado para leitura: **00:03:00 min****Dúvida**O que analisar quando ao Processar as Provisões de Férias e 13º Salário a verba de FGTS não é calculada?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Acesse: Atualizações / Definições de Cálculo / Verbas (GPEA040), e verifique se as verbas com Identificador de Cálculo 0132 e 0138 já estão cadastradas, conforme o exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23664227086231)  
  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23664227087639)  
  
Importante: As verbas devem ser incluídas como Base Provento, e sem nenhuma incidência.

2. Acesse: Atualizações / Definições de Cálculo / Manutenção de Tabelas (GPEA320), Localize a tabela S037 e clique em Visualizar.  
Confirme se na tabela S037 estão cadastrados os percentuais de INSS Patronal e FGTS para os Tipos de Contrato 1 e 2, como no exemplo abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23664255004055)

3. Verifique se a base está atualizada com o último pacote RH Expedição Contínua:  
  
12.1.33: <https://suporte.totvs.com/portal/p/10098/download#detail/1039093>

**Somente para clientes com Garantia Estendida.**

12.1.2210: <https://suporte.totvs.com/portal/p/10098/download#detail/1080347>

**Somente para clientes com Garantia Estendida.**

12.1.2310: <https://suporte.totvs.com/portal/p/10098/download#detail/1123885>

12.1.2410: <https://suporte.totvs.com/portal/p/10098/download?e=1123885>   
  
4. Exclua os Cálculos já processados de provisão e calcule novamente.  
Para mais informações sobre como excluir os cálculos de provisão [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036636774-RH-Linha-Protheus-GPE-Como-Excluir-o-C%C3%A1lculo-Individual-das-Provis%C3%B5es-de-F%C3%A9rias-e-13%C2%BA-Sal%C3%A1rio).

**Saiba Mais:**

[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
