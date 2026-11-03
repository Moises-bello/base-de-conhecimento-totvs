---
article_id: 25992291725463
category: SIGAEST - PODER DE TERCEIROS
content_hash: 53d5e6f04588fff0d42b7f7b93de875b2637ea5449d71354c094ca97583a4462
fetched_at: '2026-06-28T22:39:03.265086+00:00'
product: protheus
section_id: 1500001538881
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Relatório de controle
  de poder de terceiros com controle de lote
type: support-article
updated_at: '2026-03-17T19:57:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25992291725463-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Relat%C3%B3rio-de-controle-de-poder-de-terceiros-com-controle-de-lote
---

O controle de poder de terceiros no Protheus é feito pela tabela SB6, que não possui campos para lote/sub-lote, portanto não há relatório padrão que mostre esse controle por lote. Os relatórios MATR480 e MATR485 são usados, mas podem ser customizados para incluir essa função. MATR480 foi substituído pelo SmartView, e MATR485 tem consulta correspondente no SmartView - NFs De/Em Terceiros. Fontes e documentações estão disponíveis para customização e consulta.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25992306198807) Tempo aproximado para leitura: **00:01:03min**  
  
**Dúvida**  
Precisamos emitir um relatório que exiba as informações de controle de poder de terceiros com controle de lote, qual relatório contempla essas informações ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

O controle de Poder de Terceiros é realizado por meio da tabela SB6, e conforme pode ser visto ao consultar essa tabela, não existem campos relacionados ao Lote/SubLote.

Dessa maneira não tem um relatório que demonstre o poder de terceiros com o controle de lote para conseguir identificar que o lote XPTO está em posse de algum terceiro.

Os relatórios que possuímos para analise do controle de poder de terceiros atualmente são o MATR480 e MATR485, e uma sugestão para obter esse comportamento é realizar o Download do fonte, realizando customizações para que ele tenha esse comportamento.

Para obter os fontes de relatório do estoque [Clique aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058126794-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Fontes-de-relat%C3%B3rios-Estoque-para-altera%C3%A7%C3%A3o-ou-customiza%C3%A7%C3%A3o-fora-do-padr%C3%A3o?source=search)

Outra possibilidade é sugerir essa nova funcionalidade na central colaborativa através do link abaixo:

[Central Colaborativa](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics)

Para conhecer mais sobre as suas **funcionalidades** clique [**AQUI**](https://www.youtube.com/watch?v=LTqWbDsBb6s&list=PLYQXMbUS13r-xtKThVYHMFsLK3ezvpo3q&index=13) e assista o nosso vídeo ou acesse nosso artigo [**Central Colaborativa - Funcionalidades Disponíveis**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039466814-Funcionalidades-Dispon%C3%ADveis-na-Central-Colaborativa-TOTVS).

**Observação:**  
Com relação à descontinuação dos relatórios MATR480 e MATR485, foi identificado que:

* Para o MATR480, já existe documentação no TDN indicando sua substituição via SmartView.
* Para o MATR485, a consulta correspondente é: [**Smart View - NFs De/Em Terceiros**.](https://tdn.totvs.com/pages/releaseview.action?pageId=754621744)

Além disso, é possível consultar todas as queries SmartView do módulo de Estoque e suas documentações no repositório oficial:

<https://tdn.totvs.com/pages/releaseview.action?pageId=753648179>

**Saiba mais:**

[Clique aqui e veja mais artigos sobre Poder de Terceiros no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538881-SIGAEST-PODER-DE-TERCEIROS)
