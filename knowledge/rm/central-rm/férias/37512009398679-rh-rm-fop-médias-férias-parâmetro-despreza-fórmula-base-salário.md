---
article_id: 37512009398679
category: Férias
content_hash: 6b2501d991c9eebe9d381797ef4c6a5c4546de77022a5d4633dbd021d65f87ee
fetched_at: '2026-06-28T22:46:56.135186+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: 'RH - RM - FOP - Médias - Férias: Parâmetro Despreza Fórmula Base Salário'
type: support-article
updated_at: '2026-01-07T19:57:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37512009398679-RH-RM-FOP-M%C3%A9dias-F%C3%A9rias-Par%C3%A2metro-Despreza-F%C3%B3rmula-Base-Sal%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37512009380759) Tempo aproximado para leitura: **00:01:43 min**  
  
**Dúvida**  
Como funciona o parâmetro “Despreza fórmula adicional para base de salário”? Ao habilitar esse parâmetro, as fórmulas adicionais deixam de compor o valor das férias ou apenas a base utilizada no cálculo da média?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37512009382167)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
O parâmetro “Despreza fórmula base salário” influencia exclusivamente o cálculo das médias, não interferindo diretamente no cálculo das férias.

Quando desmarcado, o sistema considera o salário base do funcionário somado às fórmulas adicionais cadastradas em: **Configurações | Parametrizador | Férias | Fórmulas Adicionais** para compor a base de cálculo das médias. Por exemplo, um salário base de 3.863,00 acrescido de uma fórmula adicional de 1.000,00 resulta em uma base de 4.863,00 para o cálculo da média.

Ao marcar o parâmetro, as fórmulas adicionais passam a ser desconsideradas na apuração das médias, sendo utilizado apenas o salário base do funcionário. Para que essa alteração seja aplicada corretamente, é necessário recalcular as médias após a marcação do parâmetro.

Ressalta-se que as fórmulas adicionais continuam sendo utilizadas normalmente no cálculo das férias. O impacto do parâmetro ocorre somente na base utilizada para o cálculo das médias.
