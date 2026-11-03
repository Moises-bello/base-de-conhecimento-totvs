---
article_id: 20789199642903
category: RH – DIRF
content_hash: 099c43828c9df42780efc2252fb735640b14b3d69aa35cbf29368ac3dec82590
fetched_at: '2026-06-28T22:44:06.966654+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - DIRF Dedução Simplificada sem IDs de Cálculo
type: support-article
updated_at: '2025-06-16T20:07:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20789199642903-RH-Linha-Protheus-GPE-DIRF-Dedu%C3%A7%C3%A3o-Simplificada-sem-IDs-de-C%C3%A1lculo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20789199636375) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como gerar a DIRF com Dedução simplificada sem Identificadores de cálculo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - À partir do release 12.1.33  
  
**Solução**Conforme Leiaute da DIRF 2024, será utilizada uma nova coluna para a Dedução Simplificada e para isso, os valores deverão estar vinculados à novos Tipos de Rendimento na tabela genérica 36, conforme publicado em [Novos Tipos de Rendimentos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20772420455703).  
Porém, para quem não usa os IDs de cálculo abaixo nos cálculos da folha foi implementado ajuste para que sejam gravados os valores referente à Dedução Simplificada através da Geração da DIRF.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20789199637271)

O sistema validará qual o tipo de tributação usado nos cálculos do IR, validando a coluna Trib.IR (RD\_TRIBIR) das verbas de Base de IR, se a coluna estiver com 2-Simplificado, será gerado o valor da dedução simplificada informada na tabela S002 na DIRF.  
  
  
1. **Ded. Simplificada**:  
Contempla o valor da Dedução Simplificada gravada na tabela S002 - Imposto de Renda, que será utilizada nos cálculos da Folha de Pagamento, Férias e Adiantamento conforme o artigo abaixo:  
[Cálculo do IRRF - MP 1.171/2023](https://tdn.totvs.com/pages/releaseview.action?pageId=756458638)

2. **Ded. Simplificada 13o**:  
Contempla o valor da Dedução Simplificada gravada na tabela S002 - Imposto de Renda, que será utilizada nos cálculos de 13º Salário, conforme o artigo abaixo:  
[Cálculo do IRRF - MP 1.171/2023](https://tdn.totvs.com/pages/releaseview.action?pageId=756458638) 

**Saiba Mais:**  
[DIRF com Dedução Simplificada sem IDs de Cálculo](https://tdn.totvs.com/pages/releaseview.action?pageId=819527400)   
[DIRF com Dedução Simplificada com IDs de Cálculo](https://tdn.totvs.com/pages/releaseview.action?pageId=819498302)   
[RH - DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)
