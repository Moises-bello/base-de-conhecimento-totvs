---
article_id: 360018399291
category: RH - Folha de Pagamento
content_hash: 9e3318ebf811ed8bb098901d69372ba23f9871db219f9ecd9923c62b23c4a50c
fetched_at: '2026-06-28T22:44:16.162767+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Por que o sistema calcula diferença de IR de férias
  na folha de pagamento de forma indevida? ID 0101 (Dif. I.Renda Férias)
type: support-article
updated_at: '2025-05-16T17:53:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018399291-RH-Linha-Protheus-GPE-Por-que-o-sistema-calcula-diferen%C3%A7a-de-IR-de-f%C3%A9rias-na-folha-de-pagamento-de-forma-indevida-ID-0101-Dif-I-Renda-F%C3%A9rias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25972040855447) Tempo aproximado para leitura: 00:02:00 min**

**Ocorrência**Por que o sistema calcula diferença de IR de férias na folha de pagamento de forma indevida? ID 0101 (Dif. I.Renda Férias)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoas - Todas as versões  
  
**Causa**  
Incidência errada de verbas.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos de conferência na rotina de **Verbas** pelo caminho **Atualizações >Definições cálculos >Verbas (GPEA040)**:  
  
**1.** Verifique na aba **Incidência** se a incidência de IR de **todas** as verbas que constam no cálculo das férias estão corretas seguindo a legislação atual, pois no cálculo das férias, todas as verbas com SIM para IR serão somadas na base de IR férias, e ao integrar para a folha, caso sejam verbas com o campo Ref a Fer com Não, o sistema irá desconsiderar o valor da verba da base de IR Férias;  
2. A verba com ID 0101 "Cod Dif. I.Renda Férias" deve ser parametrizada como **Desconto** e na pasta **Incidências** da verba o campo **Ref. a férias** deve estar com **Sim**;  
3. As demais verbas que são de folha devem estar com **Não** para **Ref. a férias.** **Exemplo**: salário, hora extra na aba Incidências;   
4. As verbas que se referem as férias devem estar com **Sim** no campo **Ref. a férias**, como por exemplo o **id 0168** (Dedução INSS Base IR Férias) e demais verbas na aba Incidências  
5. Verifique se existe alguma verba configurada com **Sim** para **Incorpora salário** que não fez parte do cálculo de férias.   
  
 **Saiba mais**

[RH - Linha Protheus - GPE - Como fazer filtro das verbas com SIM para IR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060961393)   
[RH - Linha Protheus - GPE - Como o sistema efetua o recalculo de IR de folha quando existe férias e reajuste salarial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058339693-RH-Linha-Protheus-GPE-Como-o-sistema-efetua-o-recalculo-de-IR-de-folha-quando-existe-f%C3%A9rias-e-reajuste-salarial?source=search)

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
