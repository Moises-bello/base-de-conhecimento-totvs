---
article_id: 360052266033
category: RH - Benefícios
content_hash: 3675cf5810b51e15f0e6ce2d0785398de77ffa48183599264c0c60eb62c346b2
fetched_at: '2026-06-28T22:44:03.459712+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: 'RH - Linha Protheus - GPE - Ao gerar o Relatório de Conferência do Plano de
  Saúde (GPER014), é gerado Error Log: Invalid column name ''RHS_CODFOR'''
type: support-article
updated_at: '2025-07-22T12:28:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052266033-RH-Linha-Protheus-GPE-Ao-gerar-o-Relat%C3%B3rio-de-Confer%C3%AAncia-do-Plano-de-Sa%C3%BAde-GPER014-%C3%A9-gerado-Error-Log-Invalid-column-name-RHS-CODFOR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20790388376343) Tempo aproximado para leitura: **00:01:00 min**

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
**Ocorrência**Ao gerar o **Relatório de Conferência do Plano de Saúde (GPER014)**, é gerado *Error Log:* ***Invalid column name* RHS\_CODFOR.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30918375575319)**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**O problema ocorre quando no Grupo de Perguntas **GP014R**, as perguntas **Fornecedor Médico** e **Fornecedor Odontológico** estão com o **Conteúdo (X1\_CNT01) incorretos.**  
  
**Solução**Para fazer o ajuste, acesse o **Configurador** (SIGACFG) em Base de Dados > Dicionário > Base de Dados > Perguntas > pesquisar o Grupo de Perguntas GP014R > Editar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33631962513047)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33631962514711)

Ao localizar as perguntas **Fornecedor Médico** e **Fornecedor Odontológico,** ajuste a coluna **Conteúdo** com **&cNomAlias** conforme exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33631955208471)  
  
**Obs:** Cabe ressaltar que o ajuste deve ser feito em **modo exclusivo.**

**Saiba Mais**[RH - Linha Protheus - GPE - Relatório de Cálculo Assistência Médica GPER008](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411051523735-RH-Linha-Protheus-GPE-Relat%C3%B3rio-de-c%C3%A1lculo-assist%C3%AAncia-medica-GPER008)
