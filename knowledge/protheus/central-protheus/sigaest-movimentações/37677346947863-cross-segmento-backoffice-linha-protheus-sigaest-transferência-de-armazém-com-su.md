---
article_id: 37677346947863
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 4e19e9ca2e5e58d8197c4eeff8113dcfd2d9c6b9aa84430c29d814dc6098616c
fetched_at: '2026-06-28T22:38:57.438345+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Transferência de Armazém
  com SubLote
type: support-article
updated_at: '2026-01-14T19:26:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37677346947863-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Transfer%C3%AAncia-de-Armaz%C3%A9m-com-SubLote
---

No sistema Protheus, não é possível realizar transferência de armazém com SubLote, pois não há campo de destino específico para sublotes na rotina MATA261. Para contornar, sugerem customização via pontos de entrada, desenvolvimento participativo com a TOTVS ou registrar sugestão na Central Colaborativa para futuras implementações.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37677350147351) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
É possível no sistema Protheus, realizar uma Transferência de Armazém com SubLote?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Realmente não existe o recurso de transferência entre SubLotes. Entendo perfeitamente que, como o sub-lote funciona como uma "ramificação" do lote dentro do padrão do sistema, a ausência de um campo de destino específico na rotina **MATA261** acaba limitando esse processo direto, gerando o impedimento (*Help MA260IGUAL*) que você mencionou.

Realizei uma busca detalhada e, de fato, confirmo que não existe um ponto de entrada "prativo" ou pronto para habilitar esse comportamento específico de forma nativa.

Para auxiliá-lo com as alternativas disponíveis, organizei as opções que podemos seguir:

* **Customização via Pontos de Entrada:** Encaminho o boletim com os pontos de entrada disponíveis para a rotina MATA261, que podem servir de base para sua equipe técnica: [Consulte aqui os Pontos de Entrada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004779102-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA261-Pontos-de-Entrada-da-rotina-Transfer%C3%AAncia-M%C3%BAltipla).
* **Desenvolvimento Participativo:** Caso prefira que o time de Desenvolvimento da TOTVS crie um ponto de entrada exclusivo para sua necessidade, você pode realizar uma cotação através do [Processo de Desenvolvimento Participativo](https://tdn.totvs.com/pages/releaseview.action?pageId=589518919).
* **Central Colaborativa:** Se você acredita que essa funcionalidade seria valiosa para o padrão do produto, encorajo fortemente que registre sua sugestão na nossa [Central Colaborativa](https://www.google.com/search?q=https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050853511-Central-Colaborativa-Funcionalidades-Dispon%25C3%25ADveis). Lá, sua ideia pode ser votada por outros usuários e avaliada diretamente pelo time de Produto.

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
