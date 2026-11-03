---
article_id: 360021743431
category: Financeiro - Contas a Pagar
content_hash: 7cda8e72f0220da6502f9a4295c84f818404b0878c73d8fef7775ae642758f82
fetched_at: '2026-06-28T22:38:07.071966+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Como validar adiantamentos
  existentes na baixa de títulos a pagar
type: support-article
updated_at: '2026-02-20T16:39:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021743431-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Como-validar-adiantamentos-existentes-na-baixa-de-t%C3%ADtulos-a-pagar
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38528907084567)**Tempo aproximado para leitura:**00:03:00 min**  
  
**Dúvida**  
Caso haja adiantamento com saldo para o fornecedor, é possível verificar antes da realização da baixa?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**  
  
Caso necessite de alguma validação além desta como trava por exemplo, somente customizando por ponto de entrada, seja na rotina de baixas ou compensações.

Por meio da configuração do parâmetro **MV\_VLTITAD** é possível habilitar e verificar a existência de adiantamentos com saldo para compensação no momento da baixa a pagar / compensação a pagar. Quando habilitado o parâmetro, será exibido um alerta na tela sobre a existência da adiantamentos.

O sistema emite a mensagem em anexo com o parâmetro configurado como .T.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38528938875031)

Os possíveis conteúdos do parâmetro são:

.T. - Ativa verificação no momento da baixa;

.F. - Verificação desabilitada.

Saiba mais: [MV\_VLTITAD - Verifica no momento da baixa a pagar, se o fornecedor possui títulos de adiantamento para compensação](https://tdn.totvs.com/pages/releaseview.action?pageId=403741037)
