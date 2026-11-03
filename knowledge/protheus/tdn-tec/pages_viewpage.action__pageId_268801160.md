---
content_hash: 3c1e39ec12eddcef44b3e43479647747b9680f2097c8ade628ade8b740326754
fetched_at: '2026-07-02T19:24:21.605392+00:00'
page_id: '268801160'
product: protheus
source: tdn-tec
title: "\uFEFFMelhoria - Possibilidade de definir a largura final de um código de\
  \ barras gerado pelo agente TOTVS Printer"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268801160
version: 1
---

Melhoria - Possibilidade de definir a largura final de um código de barras gerado pelo agente TOTVS Printer

|  |  |
| --- | --- |
| Situação | Necessidade de fixar a largura total de um código de barras verticais impresso pelo agente TOTVS Printer. |
| Ocorrência | Utilizando o comando de criação de código de barras verticais na TOTVS Printer é possível definir apenas a largura padrão de cada barra, assim não é possível prever a largura final do código de barras, pois ele irá variar de acordo com a quantidade de informações contidas no código. Isto acarreta problemas para os clientes que precisam inserir um código de barras dentro de um espaço fixo do documento de impressão. |
| Melhoria | Foi implementado uma melhoria no comando 0011 do agente de impressão TOTVS Printer onde é possível definir a largura total do código de barras verticais. |
| Informações adicionais | * Para maiores informações sobre a melhoria, consulte a documentação do comando [Código de barras vertical](http://tdn.totvs.com.br/pages/viewpage.action?pageId=102924576) da [TOTVS Printer Extension](http://tdn.totvs.com.br/display/tec/TOTVS+Printer+Extension+-+INTERNA). * Referente ao chamado: SSIM-1252 * Referente à ocorrência: TVUSPX * Disponível a partir da versão 1.6.5 da TOTVS Printer. |
