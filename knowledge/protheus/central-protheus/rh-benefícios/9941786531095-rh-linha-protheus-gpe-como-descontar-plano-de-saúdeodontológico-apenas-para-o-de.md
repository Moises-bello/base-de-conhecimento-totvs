---
article_id: 9941786531095
category: RH - Benefícios
content_hash: 9b0432438ea9a3c561d44a90073fd10a9614388616ab315a3a948556321fffa6
fetched_at: '2026-06-28T22:44:03.755722+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Como descontar plano de saúde/odontológico apenas
  para o dependente
type: support-article
updated_at: '2025-09-04T19:44:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9941786531095-RH-Linha-Protheus-GPE-Como-descontar-plano-de-sa%C3%BAde-odontol%C3%B3gico-apenas-para-o-dependente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29616416414743) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como descontar plano de saúde/odontológico apenas para o dependente?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para ser descontado o plano apenas para o dependente realize os seguintes passos:

1. Acessar em **Atualizações> Definições de Cálculo> Manutenção de tabela (GPEA320)** e cadastre os dados de Assistência Médica (S008, S009, S028 ou S029) ou Odontológica (S013, S014, S030 ou S031) deixando o campo referente ao **Desconto do Titular** com **0,00**

No exemplo abaixo foi usado a tabela S028:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9941123170199)

2. Vincule o plano para o Titular e Dependente em **Atualizações> Benefícios> Plano de Saúde> Planos Ativos (GPEA001)**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9941495754647)

3. Calcule o Roteiro PLA em **Atualizações**> **Benefícios**> **Plano de saúde**> **Cálculo Plano de Saúde (GPEM016)**4. Consultando o cálculo em **Atualizações> Benefícios> Plano de Saúde> Planos Ativos> Outras Ações> Consultar Calculo**, é possível verificar que foi descontado somente para o dependente.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9941667831063)

**Importante:** Essa conferência do calculo pode ser realizada também pela rotina de Relatório de Cálculo em **Atualizações > Benefícios > Planos de Saúde > Relatório de Cálculo** (**GPER008**):  
[RH - Linha Protheus - GPE - Relatório de cálculo assistência medica GPER008](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411051523735-RH-Linha-Protheus-GPE-Relat%C3%B3rio-de-c%C3%A1lculo-assist%C3%AAncia-medica-GPER008)

**Saiba Mais**[RH - Linha Protheus - GPE - Documentações relacionadas a rotina de plano de saúde](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11223604924695-RH-Linha-Protheus-GPE-Documenta%C3%A7%C3%B5es-relacionadas-a-rotina-de-plano-de-sa%C3%BAde)  
[RH - Linha Protheus - GPE - Documentações relacionadas a rotina de plano odontológico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11245418684951-RH-Linha-Protheus-GPE-Documenta%C3%A7%C3%B5es-relacionadas-a-rotina-de-plano-odontol%C3%B3gico)  
[RH - Linha Protheus - GPE - Documentações relacionadas a rotina de coparticipação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11301756760855-RH-Linha-Protheus-GPE-Documenta%C3%A7%C3%B5es-relacionadas-a-rotina-de-coparticipa%C3%A7%C3%A3o)
