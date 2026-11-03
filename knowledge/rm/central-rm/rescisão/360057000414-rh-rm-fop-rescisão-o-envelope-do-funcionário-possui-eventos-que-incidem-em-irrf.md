---
article_id: 360057000414
category: Rescisão
content_hash: a0561bdac8454dc472b45d6086bdf821db1c35a08b1e5fcd457acf306ed378a0
fetched_at: '2026-06-28T22:46:55.276756+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - Rescisão: O envelope do funcionário possui eventos que incidem
  em IRRF com data de pagamento no caixa'
type: support-article
updated_at: '2025-01-20T14:40:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057000414-RH-RM-FOP-Rescis%C3%A3o-O-envelope-do-funcion%C3%A1rio-possui-eventos-que-incidem-em-IRRF-com-data-de-pagamento-no-caixa
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:00:02:36 min  
  
Dúvida**Ao recalcular uma rescisão, é apresentada a mensagem:

**Funcionário XXXX: O envelope do funcionário XXXX possui eventos que incidem em IRRF, com data de pagamento no caixa XX. Para que o recálculo seja processado, todos os eventos que compõem a Base de IRRF devem estar com data de pagamento no mês Caixa Local.**

Como corrigir?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Solução**Este erro ocorre porque, na rescisão, não é possível ter em um mesmo período de eventos com incidência em IRRF com data de pagamento em caixas diferentes. Para a solução do erro, existem as seguintes opções:  
  
**1. Primeira opção:** Criar um outro período para a rescisão, diferente da Folha, e manter os eventos que deseja com data de pagamento no mês desejado em período diferente.

**2. Segunda opção:** Caso deseje calcular tudo em um mesmo período, a data de pagamento deve ser no mesmo caixa. Neste caso, Parametrize a rescisão para igualar as datas de pagamento e poderá prosseguir com o recálculo. Sendo assim, após calcular a rescisão, irá apresentar a tela conforme o print abaixo e poderá marcar a flag indicada: **Altera Data Pagto. com Mês Caixa Posterior ao Pagto. Rescisão** e assim prosseguir com a rescisão.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6354445820439/mceclip0.png)
