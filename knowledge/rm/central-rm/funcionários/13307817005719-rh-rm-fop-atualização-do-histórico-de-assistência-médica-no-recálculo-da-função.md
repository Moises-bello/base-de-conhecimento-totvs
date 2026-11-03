---
article_id: 13307817005719
category: Funcionários
content_hash: 6ef162bfefe24260772e0ad929df87a2cf28f142ddaa178b35b73ebf1dfeb8d5
fetched_at: '2026-06-28T22:47:03.184643+00:00'
product: rm
section_id: 1500000861022
source: central-rm
title: RH - RM - FOP - Atualização do Histórico de Assistência Médica no recálculo
  da função de fórmula SALVAVALDEP
type: support-article
updated_at: '2025-01-21T19:28:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13307817005719-RH-RM-FOP-Atualiza%C3%A7%C3%A3o-do-Hist%C3%B3rico-de-Assist%C3%AAncia-M%C3%A9dica-no-rec%C3%A1lculo-da-fun%C3%A7%C3%A3o-de-f%C3%B3rmula-SALVAVALDEP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:  **00:02:40 min**

**Ocorrência**Ao realizar as parametrizações para o desconto do evento de assistência saúde com o Código de Cálculo 14 juntamente com uma fórmula com a função SALVAVALDEP o sistema alimenta corretamente o histórico de assistência saúde e envelope, mas se porventura ocorrer a retirada da marcação de incidência em **assistência médica** de algum **dependente**, após o lançamento dos eventos no envelope e for realizado o recálculo do envelope o sistema calcula o envelope corretamente com o novo valor do evento de Código de Cálculo 14 mas não altera o histórico sendo necessária intervenção manual para ajustes.  
 **Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Ocorreu alteração no comportamento da variável SALVAVALDEP.

**Solução**

O sistema no cálculo da distribuição da assistência médica irá excluir da tabela **PFHSTASSMED** os dependentes em que evento, competência, período e Tipo de Movimento 0 (assistência médica) não tiveram valor no cálculo da SALVAVALDEP.

Ao processar a distribuição o sistema obtém todos os registros da tabela PFHSTASSMED para a coligada, chapa, competência, período, Tipo de Movimento 0 e evento, trazendo assim todos os dependentes para os campos acima.

Após processar a inclusão ou atualização da distribuição da assistência médica. O sistema irá verificar quais dependentes estavam na PFHSTASSMED e que não estão na nova distribuição da assistência médica e excluí-los.

O mesmo procedimento será realizado para o Tipo de Movimento 1 - Férias, ao executar o cálculo do Recibo de Férias e caso já tenha lançado o valor de desconto para o dependente no histórico de assistência médica.

**Importante:**

Mesmo quando é lançado o valor da coparticipação, também terá que ter fórmula com a variável SALVAVALDEP para alimentar o histórico de assistência a saúde, caso contrario não será alimentado.  
  
**Saiba mais**  
[Atualização do Histórico de Assistência Médica no recálculo da função de fórmula SALVAVALDEP](https://tdn.totvs.com/pages/releaseview.action?pageId=742220869)
