---
content_hash: 3a14c0c8994292cb0845dde29db041a04a74155cb2539239763873dac008734b
fetched_at: '2026-06-29T00:10:09.453445+00:00'
page_id: '452719673'
product: rm
source: tdn-rm
title: E-social - S-1210 - Pagamentos de Rendimentos do Trabalho
type: documentation
url: https://tdn.totvs.com/display/LRM/E-social+-+S-1210+-+Pagamentos+de+Rendimentos+do+Trabalho
version: 2
---

Evento utilizado para prestar informações relativas aos pagamentos dos rendimentos do trabalho com ou sem vínculo e ao pagamento da Participação nos Lucros ou Resultados (PLR). Aplica-se também aos benefícios pagos por RPPS.

**Atenção:** Caso não exista nenhum evento lançado para o funcionário no período de apuração, o registro S-1210 não será gerado, porém se existir algum evento, ainda que zerado, com data de pagamento dentro do período de apuração, o evento será gerado.  
    
 **Integração Folha de Pagamento x Gestão Financeira (Autônomos)**  
 Para que as informações de pagamentos feitas aos autônomos do TOTVS Gestão Financeira sejam consideradas na geração do XLM do evento S-1210, foi criado o flag "Gera Autônomos do Fluxus/Externos" que deverá ser marcado, ao gerar o XML do evento S-1210.  
 É importante observar os critérios abaixo para a correta geração do XML.

1. Os lançamentos dos valores no TOTVS Gestão Financeira precisam estar no intervalo de datas do Período de Apuração.
2. O lançamento precisa estar baixado.

[**Mapeamento das informações do evento**](http://tdn.totvs.com/display/LRM/Evento+S-1210)

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Eventos Periódicos

Gerar XML
