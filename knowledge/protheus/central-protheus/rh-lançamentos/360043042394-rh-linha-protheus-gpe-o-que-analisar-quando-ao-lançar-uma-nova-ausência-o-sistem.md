---
article_id: 360043042394
category: RH - Lançamentos
content_hash: 95c057af50da04960b32809188bf9a52b96a2d2421904f3f08eca64e7470f670
fetched_at: '2026-06-28T22:43:31.337732+00:00'
product: protheus
section_id: 360010781734
source: central-protheus
title: RH - Linha Protheus - GPE - O que Analisar quando ao Lançar uma Nova Ausência,
  o sistema exibe a mensagem "Limite de Lançamentos do Mesmo Tipo Para o Mesmo Período
  Alcançado"
type: support-article
updated_at: '2025-06-09T16:37:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043042394-RH-Linha-Protheus-GPE-O-que-Analisar-quando-ao-Lan%C3%A7ar-uma-Nova-Aus%C3%AAncia-o-sistema-exibe-a-mensagem-Limite-de-Lan%C3%A7amentos-do-Mesmo-Tipo-Para-o-Mesmo-Per%C3%ADodo-Alcan%C3%A7ado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26468918619159) Tempo aproximado para leitura: **00:01:30 min****Dúvida**O que Analisar quando ao Lançar uma Nova Ausência, o sistema exibe a mensagem "Limite de Lançamentos do Mesmo Tipo Para o Mesmo Período Alcançado"?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

Para solucionar essa dúvida, realize os seguintes passos:  
  
**1.** Acesse **Atualizações > Definições de Cálculo > Tipos de Ausência (GPEA430)**, localize a Ausência que está sendo lançada para o funcionário, e verifique qual é o código da verba atribuída à Ausência;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26468945468823)  
  
**2.** Acesse **Atualizações > Definições de Cálculo > Verbas (GPEA040)**, localize o código da verba e verifique os campos "**Qtde.Lancto**" (RV\_QTDLANC) e "**Lcto.Diário**" (RV\_LCTODIA) estão preenchidos conforme o exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26468918627479)

O campo "**Qtde.Lancto**" deve estar preenchido com **9**, e o campo "**Lcto.Diário"**deve estar preenchido com **Sim**. Altere o conteúdo destes campos, e clique em **Confirmar**, para salvar as alterações no cadastro da verba.  
  
**Saiba mais:**

[RH - Funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011909593-RH-Funcion%C3%A1rios)
