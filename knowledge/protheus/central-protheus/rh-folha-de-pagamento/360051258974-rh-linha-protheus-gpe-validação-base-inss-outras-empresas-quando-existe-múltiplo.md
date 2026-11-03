---
article_id: 360051258974
category: RH - Folha de Pagamento
content_hash: 357b9cba733c2cf929babdbd5c80f198cb9c2bb0149edaaf57a93c4585ec30ef
fetched_at: '2026-06-28T22:44:16.398502+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Validação Base INSS outras Empresas quando existe
  Múltiplo Vínculo
type: support-article
updated_at: '2025-08-22T19:56:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051258974-RH-Linha-Protheus-GPE-Valida%C3%A7%C3%A3o-Base-INSS-outras-Empresas-quando-existe-M%C3%BAltiplo-V%C3%ADnculo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22249664214167)**Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Sistema valida Base de INSS Outras Empresas informada para composição do INSS quando existe múltiplo vínculo com outras empresas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**Sim. O sistema valida a verba de Base INSS Outras Empresas, pois como existe múltiplo vínculo, o cálculo é proporcional, para que nenhuma empresa recolha o encargo indevidamente.   
  
**Exemplo**:   
Primeiro vínculo calculou o INSS incorretamente, deveria ser descontado R$556,93, mas descontaram R$556,16, ficando uma diferença de R$0,77. Lançamos o valor descontado na outra empresa, mas o Protheus calculou um INSS de R$ R$114,18, ou seja com a mesma diferença dos R$0,77, pois o outro vinculo ficou incorreto, logo, a outra empresa deve fazer os ajustes para que o INSS de seu funcionário fique correto.  
  
O cálculo de INSS efetuado no Protheus fica correto, pois o sistema valida o valor exato que o funcionário deveria ter tido de desconto em seu cálculo.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081429673)  
  
Caso queira que o sistema efetue o calculo sem considerar o erro efetuado pela outra empresa, não lance a verba de Base de INSS Outras Empresas, dessa forma o sistema não validará o múltiplo vínculo e calculará o valor do INSS sem validar a inconsistência do primeiro vinculo da folha de pagamento.  
  
**Saiba Mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Calculo Autonomo/Prolabore](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983113-RH-Calculo-Autonomo-Prolabore)
