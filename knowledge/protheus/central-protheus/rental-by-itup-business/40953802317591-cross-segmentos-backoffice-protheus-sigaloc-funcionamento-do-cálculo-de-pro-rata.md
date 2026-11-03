---
article_id: 40953802317591
category: Rental by ItUp Business
content_hash: d635c69b24c46070e415634de56ba806dc9cfe82b30edb8f81c4c48d7ee72e96
fetched_at: '2026-06-28T22:36:20.641264+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC - Funcionamento do cálculo
  de Pro Rata
type: support-article
updated_at: '2026-06-08T12:09:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40953802317591-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Funcionamento-do-c%C3%A1lculo-de-Pro-Rata
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40953802294551) Tempo aproximado para leitura: **00:03:30 min**  
  
**Dúvida**  
O que é e como funciona o cálculo de Pro Rata no módulo de Gestão de Locação (SIGALOC), incluindo o comportamento de retornos no mesmo dia e os processos relacionados?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - Todas as versões  
  
**Solução**  
O cálculo de Pro Rata é o responsável por apurar a quantidade de dias efetivamente utilizados dentro do período contratual.

O motor de cálculo contratual (LOCA001) funciona com as seguintes premissas:

* Considera a data de remessa e a data de retorno.
* Calcula a diferença em dias dentro do período aberto.
* Não realiza controle por horas.

Sobre a consideração de remessa e retorno no mesmo dia: Quando a data de saída e a data de retorno forem iguais, o sistema considera 1 (um) dia de utilização, pois o cálculo é baseado exclusivamente nas datas informadas.

Relação com outros processos do sistema: O resultado do Pro Rata é consumido diretamente pelo Faturamento Automático e pelo Relatório de Pré-Fatura. É importante ressaltar que esses processos não recalculam os valores, eles apenas utilizam o resultado já apurado pelo cálculo proporcional.

**Passos** O comportamento do cálculo de Pro Rata para retornos (tanto retornos de locação normais quanto retornos de estruturas via NF) varia conforme o status do mês:

1. Retorno em Mês Aberto: O sistema calcula apenas o Pro rata final.
2. Retorno em Mês Fechado: O sistema calcula o Pro rata início e o Pro rata final.
