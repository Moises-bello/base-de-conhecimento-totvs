---
article_id: 10926890427799
category: RH - 13º salário
content_hash: a6be1f8dec54f1bc77797a92fed5453243c247e2f180a385a65ca95de7a02ae7
fetched_at: '2026-06-28T22:44:01.648710+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Valor INSS 13º salário é deduzido duas vezes da
  base de IRRF no calculo do 13° Salario
type: support-article
updated_at: '2026-04-28T16:58:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10926890427799-RH-Linha-Protheus-GPE-Valor-INSS-13%C2%BA-sal%C3%A1rio-%C3%A9-deduzido-duas-vezes-da-base-de-IRRF-no-calculo-do-13-Salario
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18726784615575) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Valor INSS 13º salário é deduzido duas vezes da base de IRRF no calculo do 13° Salario.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - Todas as versões.  
  
**Causa**  
O incidente ocorre devido os dois Identificadores de calculo 0070 - INSS 13° e 0169 Dedução INSS 13° estarem com SIM no campo IR no cadastro da verba.   
  
**Solução**

Acesse: Atualizações / Definições de Cálculo / Verbas (GPEA040), Localize a verba com Id 0070, e verifique se o campo IR (RV\_IR) está configurado com Sim, e altere o conteúdo deste campo para Não.  
   
Apenas o Identificador de calculo 0169 deve estar com SIM no campo IR no cadastro da verba.  
  
**Importante:** Orientamos a deixar o Id 0169 com Sim para IR pois no calculo da rescisão o Protheus olha esse Id para deduzir, conforme artigo [RH - Linha Protheus - GPE - Valor INSS 13º salário não é deduzido para a base de IR 13º salário em rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051550714-RH-Linha-Protheus-GPE-Valor-INSS-13%C2%BA-sal%C3%A1rio-n%C3%A3o-%C3%A9-deduzido-para-a-base-de-IR-13%C2%BA-sal%C3%A1rio-em-rescis%C3%A3o?source=search), sendo assim, o ID 0070 deve ficar com Não no campo IR para que não ocorra a dedução na base duas vezes.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40075006585495)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10926370805015)

**Saiba Mais:**

[RH - 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)   
**Essas documentações também podem ser acessadas através da Carolina, veja como acessar a assistente virtual, via Protheus ou central de atendimento:**[**https://www.youtube.com/watch?v=T7b4zMlphTI**](https://www.youtube.com/watch?v=T7b4zMlphTI)
