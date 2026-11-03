---
article_id: 39345115352727
category: Folha Mensal
content_hash: 02070520003006127a1ce1d86c0277751cd9301e998dca278b1a15fcf952e372
fetched_at: '2026-06-28T22:46:57.956305+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Diferença salarial não recalcula eventos com fórmulas
type: support-article
updated_at: '2026-03-27T19:36:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39345115352727-RH-RM-FOP-Diferen%C3%A7a-salarial-n%C3%A3o-recalcula-eventos-com-f%C3%B3rmulas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39345115342743) Tempo aproximado para leitura: **00:01:49 min**  
  
**Dúvida**  
Ao realizar o processo de diferença salarial, por que os eventos que possuem fórmula de valor vinculada não são recalculados?

**Ambiente**  
 TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Solução**

Este comportamento ocorre porque o processo de diferença salarial não realiza o recálculo automático de fórmulas de valor de forma padrão. Para que o sistema processe esses valores corretamente, a estrutura das fórmulas deve estar preparada especificamente para a rotina de diferença salarial.

Geralmente, as fórmulas de eventos são configuradas para buscar valores mensais fixos ou variáveis do período atual. Durante o processo de diferença, essas fórmulas podem não identificar a variação salarial retroativa ou não possuir as funções de contexto necessárias para buscar o valor devido no mês de origem da diferença.

Ressaltamos que o suporte padrão da TOTVS não realiza a criação ou o ajuste de fórmulas personalizadas. Caso seja identificado que a fórmula não contempla o cenário de diferença salarial, o ajuste deve ser realizado internamente pelo responsável pelas fórmulas na instituição ou através de consultoria.

**Saiba Mais**

[RH - RM - FOP - Fórmulas e Funções](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061764374-RH-RM-FOP-F%C3%B3rmulas-e-Fun%C3%A7%C3%B5es)

[RH - RM - FOP - Diferença Salarial Cálculo e Lançamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4419368388887-RH-RM-FOP-Diferen%C3%A7a-Salarial-C%C3%A1lculo-e-Lan%C3%A7amento)
