---
article_id: 34047905816215
category: Folha Mensal
content_hash: cf83fb08b08b3852166b190255270955ded4fd5f16cdfbf789ee28285727373a
fetched_at: '2026-06-28T22:46:58.018253+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Diferença Salarial lançando dois eventos com Código de cálculo
  37
type: support-article
updated_at: '2025-08-08T18:00:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34047905816215-RH-RM-FOP-Diferen%C3%A7a-Salarial-lan%C3%A7ando-dois-eventos-com-C%C3%B3digo-de-c%C3%A1lculo-37
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34047874615063) Tempo aproximado para leitura: **00:02:41 min**  
  
**Dúvida**  
Ao realizar o processo de Diferença salarial por dissídio, o sistema está lançando dois eventos com Código de cálculo 37, sendo um deles com incidência em INSS e o outro sem, sendo que deveria estar sendo lançado apenas o evento de Diferença salarial sem incidência. Por qual motivo isso ocorre e como ajustar?

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
Esse comportamento ocorre devido ao período informado na parametrização da diferença salarial.

O sistema entende que o dissídio se refere a meses anteriores à competência atual (regime de competência). Quando a data final da diferença inclui o mês atual, o RM lança:

➡️ Eventos sem incidência de INSS para os meses retroativos (anteriores à competência atual), e

➡️ Evento com incidência de INSS para o mês vigente, pois o INSS segue o regime de competência.

Exemplo prático: 

Suponha que a competência atual no RM seja 08/2025.

Na parametrização da diferença salarial, o usuário informa:

**Data início: 01/06/2025**

**Data fim: 31/08/2025**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34047905802519)

Neste caso, o sistema entenderá:

Junho e Julho como retroativos → Lança evento **SEM** incidência de INSS;

Agosto como mês atual → Lança evento **COM** incidência de INSS.

Para evitar que o sistema gere o evento com incidência de INSS, informe apenas os meses retroativos no período da diferença salarial.

Exemplo: 01/06/2025 a 31/07/2025. Não inclua o mês atual (08/2025) na parametrização, caso a diferença salarial não se aplique a ele. Assim, o sistema irá gerar apenas eventos sem incidência de INSS, como esperado para valores retroativos.

O comportamento é padrão do sistema, baseado na legislação previdenciária, onde o INSS é apurado por competência. Ao envolver o mês atual, mesmo dentro de um processo de dissídio, a incidência será aplicada conforme a regra do regime.

**SAIBA MAIS:**

[RH - RM - FOP - Diferença salarial por dissídio retroativa à competência atual](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414433322519-RH-RM-FOP-Diferen%C3%A7a-salarial-por-diss%C3%ADdio-retroativa-%C3%A0-compet%C3%AAncia-atual#:~:text=Como%20realizar%20diferen%C3%A7a%20salarial%20retroativa%20%C3%A0%20compet%C3%AAncia%20atual%3F&text=A%20diferen%C3%A7a%20salarial%20por%20dissidio,principalmente%20o%20calculo%20do%20INSS.)
