---
article_id: 30037644977687
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 815ba02d16147c950c372a47b6e3f30100ac5486cbecf32f7be8ebce0a5172b9
fetched_at: '2026-06-28T22:38:42.539533+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Como alterar a aparência
  do Pedido de Venda
type: support-article
updated_at: '2025-02-17T14:48:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30037644977687-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-alterar-a-apar%C3%AAncia-do-Pedido-de-Venda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30037635155863) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como alterar a aparência do Pedido de Venda (**MATA410**)?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da versão 11.8  
  
**Solução**O parâmetro responsável por alterar a aparência do *layout*/visualização do sistema é o **MV\_ENCHOLD**. Para localizar o parâmetro acesse pelo menu do **Configurador (SIGACFG): Ambiente > Cadastros > Parâmetros**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30037644945687)

Clique em**seta para baixo** para **expandir** as opções da empresa selecionada e clique em**parâmetros**. No ícone da **lupa,** buque pelo parâmetro **MV\_ENCHOLD.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30037644946583)

**MV\_ENCHOLD = 1 -**Define visualização da Enchoice no padrão das versões anteriores à P11 = Sim![](https://centraldeatendimento.totvs.com/hc/article_attachments/30037635158807)

Visualização da rotina "Pedidos de Venda (**MATA410**)" quando  **MV\_ENCHOLD = 1:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/30037635164183)**

**MV\_ENCHOLD = 2 -**Define visualização da Enchoice no padrão das versões anteriores à P11 = Não **![](https://centraldeatendimento.totvs.com/hc/article_attachments/30037644951831)**

Visualização da rotina "Pedidos de Venda (**MATA410**)" quando **MV\_ENCHOLD = 2:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30037635165335)

**Observação**Devido à evolução tecnológica do sistema Protheus, algumas rotinas da release 12 passaram a operar no modelo MVC (Model-View-Controller).

É importante ressaltar que o parâmetro **MV\_ENCHOLD** não é aplicável nesse formato, o que impossibilita a alteração da aparência do layout ou da visualização em rotinas que utilizam essa arquitetura.

**Saiba mais**

* [Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Parâmetro MV\_ENCHOLD na rotina CRMA980 cadastro do cliente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10725950454039-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Par%C3%A2metro-MV-ENCHOLD-na-rotina-CRMA980-cadastro-do-cliente)
* [Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Tratar o espaçamento entre colunas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040812414-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Tratar-o-espa%C3%A7amento-entre-colunas)
* [Cross Segmento - Backoffice Linha Protheus - ADVPL - Como validar se uma rotina está em MVC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016345572-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Como-validar-se-uma-rotina-est%C3%A1-em-MVC)
