---
article_id: 34045520733719
category: Folha Mensal
content_hash: 9ac6e795d37ad9d28530b049235666266914002ef4a33cc532e42c37d1494db1
fetched_at: '2026-06-28T22:46:58.021721+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Folha Mensal - Erro: O funcionário xxxx demitido não receberá
  o lançamento do grupo de eventos'
type: support-article
updated_at: '2026-05-26T18:24:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34045520733719-RH-RM-FOP-Folha-Mensal-Erro-O-funcion%C3%A1rio-xxxx-demitido-n%C3%A3o-receber%C3%A1-o-lan%C3%A7amento-do-grupo-de-eventos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34045546034839) Tempo aproximado para leitura: **00:02:24 min**  
  
**Ocorrência**  
Ao realizar o processo de Lançamentos - grupo de eventos,  o sistema emite a seguinte mensagem de erro: **"O funcionário XXXX demitido não receberá o lançamento do grupo de eventos, porque o período atual é maior que o período de rescisão. Novos eventos deverão ser lançados na Rescisão Complementar."** Por qual motivo este erro ocorre?   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**  
Esse incidente ocorre, pois o sistema identifica que o funcionário já foi desligado e que a tentativa de lançamento está sendo feita em um período posterior à data da rescisão.  
  
**Solução**

Como o funcionário já foi demitido, ele não recebe mais verbas diretamente pela folha mensal, pois os valores foram encerrados no envelope de rescisão.

Se for necessário adicionar novos eventos (como valores retroativos, diferenças salariais, ajustes,  ou eventos complementares), é preciso:  
  
1. Verificar o período em que a rescisão foi calculada (por exemplo, período 5);  
  
2. Caso os lançamentos estejam sendo feitos em um período posterior (ex: período 13), o sistema bloqueará, pois não há mais vínculo ativo;  
  
3. Para incluir novos valores, utilize o processo de **Rescisão Complementar**, selecionando o colaborador demitido e inserindo os eventos necessários

DICA 💡

Sempre que precisar lançar valores após o desligamento do colaborador, utilize a Rescisão Complementar. Essa funcionalidade é própria para ajustes e novos lançamentos pós-demissão, garantindo que os valores sejam corretamente calculados e informados ao eSocial.

Caso tenha dúvidas se o processo devido é uma Rescisão complementar ou uma Retificação de Rescisão, é necessário que verifique a documentação:  
  
 [RH - RM - FOP - Diferença entre Rescisão Complementar e Retificação de Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418631455767-RH-RM-FOP-Diferen%C3%A7a-entre-Rescis%C3%A3o-Complementar-e-Retifica%C3%A7%C3%A3o-de-Rescis%C3%A3o)

**SAIBA MAIS:**

[RH - RM - FOP - Calcular Rescisão Complementar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004150252-RH-RM-FOP-Calcular-Rescis%C3%A3o-Complementar)

[RH - RM - FOP - Retificação de rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413328440983-RH-RM-FOP-Retifica%C3%A7%C3%A3o-de-rescis%C3%A3o)
