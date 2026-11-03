---
article_id: 38266894706071
category: Financeiro - Comissão
content_hash: 426bc60e76da0b2e646e351500ded3c19a86a72e9d2f7d774c36bbeebf7161db
fetched_at: '2026-06-28T22:37:50.822380+00:00'
product: protheus
section_id: 26655771327895
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Manter alteração da
  comissão
type: support-article
updated_at: '2026-02-09T13:23:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38266894706071-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Manter-altera%C3%A7%C3%A3o-da-comiss%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38266894696727) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Como alterar a comissão de um título sem que o valor seja sobrescrito pela rotina de recálculo (FINA440)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Versão 12.1.2210.  
  
**Solução**  
Para garantir que as alterações manuais do valor da comissão não sejam alteradas pelo processamento da rotina de Recálculo de Comissão (FINA440), existem dois caminhos possíveis:

**Opção 1: Alteração via Baixa Manual (Baixa de Títulos)** indicada para ajustes pontuais diretamente na rotina de baixa:

1. Acesse a rotina de **Baixa Manual** (FINA070);
2. Selecione o título desejado;
3. Antes de confirmar a baixa, pressione a tecla **F12** no teclado para abrir os parâmetros da rotina;
4. Localize a opção "**Mostra Comissão?"** E altere o conteúdo para **sim.**

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38266894697623)
5. Ao confirmar a baixa, o sistema abrirá a tela de comissões. O valor digitado manualmente nesta tela será preservado pelo sistema, impedindo que o recálculo o altere posteriormente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38266894697751)

**Opção 2: Ajuste via Ponto de Entrada:**

1. Utilize o Ponto de Entrada [**F440FLAGE3**](https://tdn.totvs.com/pages/releaseview.action?pageId=877162116);
2. Este PE permite manipular o flag que indica ao sistema que aquela comissão não deve ser recalculada pela rotina de recálculo (FINA440), mantendo a integridade da informação customizada ou ajustada previamente.

**Saiba mais**

[Financeiro - Comissão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/26655771327895-Financeiro-Comiss%C3%A3o)
