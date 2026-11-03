---
article_id: 360011285312
category: Férias
content_hash: 95bb158592a7d1e6fd89da20dcf363cb293464a2781dad94ef48b3a742d249b9
fetched_at: '2026-06-28T22:46:56.492290+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: 'RH - RM - FOP - Diferença de Férias: The given key was not present in the
  dictionary'
type: support-article
updated_at: '2026-05-08T14:22:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011285312-RH-RM-FOP-Diferen%C3%A7a-de-F%C3%A9rias-The-given-key-was-not-present-in-the-dictionary
---

**Ocorrência**  
Ao lançar uma diferença de férias é apresentado a seguinte mensagem de erro: **The given key was not present in the dictionary.**   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento -Todas as versões  
  
**Causa**  
Esse incidente ocorre, pois a parametrização do sistema está incorreta para o Cálculo da Diferença das Férias.  
  
**Solução**  
Para solucionar essa ocorrência, realize os passos abaixo:  
  
**01.** Acesse o menu **Administração de Pessoal | Sindicatos | Férias | Eventos para Pagamento de Médias de Férias** e inclua os eventos, conforme imagem abaixo:  
  
  
![KCS.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360008476472)  
  
  
Abaixo, estão mais informações sobre os eventos para pagamento de férias e diferença de férias:  
  
Pagamento de férias, Código de cálculo 38  
[Código de Cálculo 38 - Férias](https://tdn.totvs.com/pages/releaseview.action?pageId=452718560)  
  
Eventos de Diferença de Férias, Código de cálculo 45  
[Código de Cálculo 45 - Dif. Férias Pagas no Mês](https://tdn.totvs.com/pages/releaseview.action?pageId=452718398)  
  
**02.** Caso o erro persista, verifique se nos eventos que incidem em média se existe algum que esteja **Inativo.** Localizando o evento inativo, desmarque a Flag **Inativo**. Se não encontrar nenhum evento inativo para esse funcionário, verifique todos os outros que compõem média para cálculo.  
  
  
![KCS.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360008514991)

**Saiba mais**

[RH - RM - FOP - Diferença de Férias: Lançamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018744251-RH-RM-FOP-Diferen%C3%A7a-de-F%C3%A9rias-Lan%C3%A7amento)

[RH - RM - FOP - Eventos que compõe a diferença de férias por dissidio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5125957667351-RH-RM-FOP-Eventos-que-comp%C3%B5e-a-diferen%C3%A7a-de-f%C3%A9rias-por-dissidio)
