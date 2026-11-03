---
article_id: 20196179471383
category: 'Financeiro - Borderô contas a Pagar '
content_hash: 41e93137868cbecbd2c94773e0a238e983f207769312f671eea7ed6a15c025fd
fetched_at: '2026-06-28T22:37:34.967723+00:00'
product: protheus
section_id: 35057529029143
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA241 - Quando utilizar
  a rotina de geração de borderô com Impostos FINA241
type: support-article
updated_at: '2026-03-25T19:50:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20196179471383-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA241-Quando-utilizar-a-rotina-de-gera%C3%A7%C3%A3o-de-border%C3%B4-com-Impostos-FINA241
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20196179445015) Tempo aproximado para leitura: **05:00** min  
  
**Dúvida**  
Quando devemos utilizar a rotina de geração de borderô com Impostos FINA241 e qual a diferença da rotina FINA340  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA241**-** Todas as versões.  
  
**Solução**

A rotina **FINA241** foi desenvolvida para ser utilizada quando um título será enviado para pagamento via CNAB, em que o título possui retenções e o fato gerador é a baixa.

A rotina **FINA241** fará a retenção dos impostos no momento da geração do borderô, podendo ser enviado via **CNAB** apenas o saldo a pagar do título.   
   
Vale lembrar que, para impostos com fato gerador sendo na **baixa**, quando utilizamos o borderô de Impostos - **FINA241** a retenção acontece **incondicionalmente**na geração do borderô, em que o seu vencimento fica impactado, pois é gerado para o 20.º dia do mês subsequente à geração.

Caso em seu ambiente ative o parâmetro **MV\_CNBIMPG,** não é possível utilizar a geração do borderô via FINA241.

Para que a retenção seja criada com base efetivamente na baixa ao ativar este parâmetro, terá que gerar o borderô via rotina FINA240.

Saiba mais  
[CNAB\_MV\_CNBIMPG\_FINA430](https://tdn.totvs.com/display/public/PROT/FIN0042_CNAB_MV_CNBIMPG_FINA430)
