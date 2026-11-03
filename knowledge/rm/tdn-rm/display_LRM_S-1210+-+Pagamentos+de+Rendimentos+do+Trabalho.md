---
content_hash: 830821533b2d8dc775919a3fb81b23d32fe60a9aad762a11b92fb45e1261b906
fetched_at: '2026-06-29T00:08:59.670535+00:00'
page_id: '364909290'
product: rm
source: tdn-rm
title: S-1210 - Pagamentos de Rendimentos do Trabalho
type: documentation
url: https://tdn.totvs.com/display/LRM/S-1210+-+Pagamentos+de+Rendimentos+do+Trabalho
version: 5
---

|  |  |
| --- | --- |
| **Obrigatoriedade** | Empregador/contribuinte/órgão público que pagou para trabalhadores remuneração, rendimento ou PLR e benefícios do RPPS |
| **Pré-requisitos** | Envio dos eventos "S-1000 - Informações do Empregador/Contribuinte/Órgão Público/Órgão Público", "S-1010 – Tabela de rubricas" (exceto para os casos de pagamentos relativos a período anterior à obrigatoriedade do eSocial), "S-1200 – Remuneração de trabalhador vinculado ao Regime Geral de Previdência Social", "S-1202 – Remuneração do servidor vinculado a Regime de Previdência Social", "S-1207 – Benefícios previdenciários – RPPS", "S-2299 – Desligamento", "S-2399 - Trabalhador sem vínculo de Emprego/Estatutário – Término", conforme o caso, e S-2200-Cadastramento Inicial do Vínculo e Admissão/Ingresso do Trabalhador", no caso de pagamento de férias (não é necessário o S-1200, mas o empregado deve constar no RET).  **Observação**: Mas detalhes consulte os manuais do eSocial. |
| **Prazo de Envio** | Deve ser enviado até o dia 07 do mês seguinte ou antes do envio do fechamento dos eventos periódicos (evento "S-1299 – Fechamento dos Eventos Periódicos"), o que ocorrer primeiro. Antecipa-se o envio deste evento para o dia útil imediatamente anterior quando não houver expediente bancário. |
| **Descrição** | Evento utilizado para prestar informações relativas aos pagamentos dos rendimentos do trabalho com ou sem vínculo e ao pagamento da Participação nos Lucros ou Resultados (PLR). Aplica-se também aos benefícios pagos por RPPS.  **Atenção:** Caso não exista nenhum evento lançado para o funcionário no período de apuração, o registro S-1210 não será gerado, porém se existir algum evento, ainda que zerado, com data de pagamento dentro do período de apuração, o evento será gerado.  **Integração Folha de Pagamento x Gestão Financeira (Autônomos)**  Para que as informações de pagamentos feitas aos autônomos do TOTVS Gestão Financeira sejam consideradas na geração do XLM do evento S-1210, foi criado o flag "Gera Autônomos do Fluxus/Externos" que deverá ser marcado, ao gerar o XML do evento S-1210.  É importante observar os critérios abaixo para a correta geração do XML.   1. Os lançamentos dos valores no TOTVS Gestão Financeira precisam estar no intervalo de datas do [Período de Apuração](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.PeriodoApuracao.aspx). 2. O lançamento precisa estar baixado. |
| **Mapeamento** | [Regras de definição entre o TOTVS Folha de pagamento e as tags de composição do xml para eSocial.](http://tdn.totvs.com/display/public/LRM/Evento+S-1210) |
