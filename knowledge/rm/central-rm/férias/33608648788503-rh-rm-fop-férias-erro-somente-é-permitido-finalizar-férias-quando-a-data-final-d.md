---
article_id: 33608648788503
category: Férias
content_hash: f9e8a7498f6cf3ba3b038f39234121385c2109f791e908f20734616e15b81749
fetched_at: '2026-06-28T22:46:56.144369+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: 'RH - RM - FOP - Férias - Erro: Somente é permitido finalizar férias quando
  a data final das férias está na competência atual'
type: support-article
updated_at: '2026-05-26T18:28:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33608648788503-RH-RM-FOP-F%C3%A9rias-Erro-Somente-%C3%A9-permitido-finalizar-f%C3%A9rias-quando-a-data-final-das-f%C3%A9rias-est%C3%A1-na-compet%C3%AAncia-atual
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33608627367063) Tempo aproximado para leitura: **00:01:18min**  
  
**Ocorrência**  
Ao tentar finalizar as férias partidas, o sistema dispara a seguinte mensagem de erro: **"Somente é permitido finalizar férias quando a data final das férias está na competência atual."**

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**  
Essa mensagem ocorre pois, em caso de férias partidas, a finalização ocorre no último mês de gozo de férias.  
  
**Solução**  
Suponha que o colaborador possui férias que se iniciam em julho/2025 e finalizam em agosto/2025, neste cenário, caso você esteja na competência julho/2025, as férias devem ser finalizadas na competência agosto/2025.   
  
Importante: O procedimento deve ser feito nessa ordem, pois as férias do funcionário são quebradas em duas competências, logo, só podem ser finalizadas na competência seguinte.   
  
Caso opte por finalizar dentro da competência atual, existe o parâmetro "**Lança o movimento próximo mês**", localizado em: **Férias | Finalizar**. Marcando este parâmetro, o sistema finaliza as férias que vencem no próximo mês.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33610527508631)

**Saiba mais:**

[RH - RM - FOP - Férias: Finalizar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012328752-RH-RM-FOP-F%C3%A9rias-Finalizar)

[RH - RM - FOP - Dúvidas frequentes: Processo de Férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23673187786007-RH-RM-FOP-D%C3%BAvidas-frequentes-Processo-de-F%C3%A9rias)
