---
content_hash: 00a3764fcaf5991bf27991f5b29e57670e8f2ab86c8dde76845003dab752a406
fetched_at: '2026-06-29T00:11:38.129950+00:00'
page_id: '781214661'
product: rm
source: tdn-rm
title: Proposta - Validação de VPL
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=781214661
version: 2
---

API de Validação de VPL

| Título | **API de Validação de VPL** |
| --- | --- |
| Endpoint | [http://localhost:8051/api/imb/v1/Sales/](http://localhost:8051/api/imb/v1/Sales/20_1914/VPL)[{Cod Coligada}\_{Número da Venda}](http://localhost:8051/api/imb/v1/sales/proposals/20_1914/approval?note=Solicitar)[/VPL](http://localhost:8051/api/imb/v1/Sales/20_1914/VPL) |
| Verbo | Get |
| Parameters | no parameters |
| Descrição | API que retornar o cálculo da análise da proposta do cliente comparando com a proposta padrão, entre os indicadores a VPL.  Baixe **[aqui](https://tdn.totvs.com/download/attachments/665033766/PLANILHA%20ANALISE%20VPL%20.xlsx?version=2&modificationDate=1657125942857&api=v2)**a planilha excel com o cálculo  Para o  cálculo da VPL os campos da modalidade da proposta do TCGI → Portal do Imóveis  Ao validar a VPL  os campos da tabela  de venda e regras serão espelhados nas tabelas antigas do PI (XPIPROPOSTA, XPIPESSOA\_PROPOSTA, XPIPROPOSTACOMPOSICAOHIST)  para manter o funcionamento dos relatórios e telas antigas |
| Modalidade  da Venda TCGI | . |

Modelo Json Solicitação Geração ComissãoBodytrueModelo Json Solicitação Geração ComissãoRESPONSEtrueParâmetros do Response

Parâmetros:

* codcoligada: coligada do empreendimento;
* numvenda : Número da venda;
* valortabelaprecopadrao:  Valor da Tabela de Preço Padrão da modalidade padrão
* valortabelaprecoproposta: Valor da Tabela de Preço Padrão da modalidade padrão
* valorfinanciadoatulizadopadrao: Valor sumarizado dos componentes de Entrada e Principal da modalidade padrão
* valorfinanciadoatulizadoproposta: Valor sumarizado dos componentes de Entrada e Principal da modalidade proposta
* valorpadraovpl: Valor sumarizado das parcelas da modalidade padrão - Inclui todos os valores de todos os componentes
* valorpropostavpl: Valor sumarizado das parcelas da modalidade proposta- Inclui todos os valores de todos os componentes
* percentualtma: Percentual da TMA - Taxa mínima de atratividade. A TMA é basicamente uma taxa de desconto que representa o retorno mínimo que o investidor deseja obter.
* aprovada:  O VPL foi aprovado, true ou false
* mensagem: Proposta AProvada ou Reprovada
* log: Detalhe da mensagem quando for reprovada
* itensvpl:
  + nomeparametro: Prazo de Financiamento;
  + valortabela: Nro de Meses do componente principal;
  + valorproposta:  Nro de Meses do componente principal;
  + parametrodeaprovacao: Não valida para esse tipo de parâmetro;

* + nomeparametro: % Captação a Vista;
  + valortabela: Percentual do componente de entrada;
  + valorproposta:  Percentual do componente de entrada;
  + parametrodeaprovacao: Pode validar entre %mínimo  e %máximo, se configurado com valor na modalidade;

* + nomeparametro: % Captação até Entrega;
  + valortabela: Percentual do valor previsto para receber até a entrega;
  + valorproposta:  Percentual do valor previsto para receber até a entrega;
  + parametrodeaprovacao: Não valida para esse tipo de parâmetro;

* + nomeparametro: % Captação até 1 mês Antes Entrega;
  + valortabela: Percentual do valor previsto para receber até um mês antes da entrega;
  + valorproposta:  Percentual do valor previsto para receber até um mês antes da entrega;
  + parametrodeaprovacao: Não valida para esse tipo de parâmetro;

* + nomeparametro: % Captação até Metade da proposta em relação a Entrega da Subunidade;
  + valortabela: Percentual do valor previsto para receber até a metade do tempo que falta para entrega;
  + valorproposta:  Percentual do valor previsto para receber até a metade do tempo que falta para entrega;
  + parametrodeaprovacao: Não valida para esse tipo de parâmetro;

* + nomeparametro: Valor m2;
  + valortabela: Valor do m2 ;
  + valorproposta:  Valor do m2 ;
  + parametrodeaprovacao: Não valida para esse tipo de parâmetro;

* + nomeparametro: Valor m2 VPL;
  + valortabela: Valor do m2 com a VPL;
  + valorproposta:  Valor do m2 com a VPL;
  + parametrodeaprovacao: Não valida para esse tipo de parâmetro;

* + nomeparametro: % Arrecadação;
  + valortabela: (Valor do total financiado / Valor Tabela Preço) - 1;
  + valorproposta:  (Valor do total financiado proposta / Valor Tabela Preço Proposta) - 1;
  + parametrodeaprovacao: Pode validar entre %mínimo  e %máximo, se configurado com valor na modalidade;

* + nomeparametro: % Desconto;
  + valortabela: 1- (Valor do total original / Valor Tabela Preço) ;
  + valorproposta:  1- (Valor do total original proposta / Valor Tabela Preço Proposta) ;
  + parametrodeaprovacao: Pode validar entre %mínimo  e %máximo, se configurado com valor na modalidade;

* + nomeparametro: % Diferença do VPL;
  + valortabela: Percentual de diferença da VPL em reação ao padrão, nesse caso sempre será 0, pois é a coluna do padrão;
  + valorproposta:  Percentual de diferença da VPL em reação ao padrão,  se for maior que 0, está abaixo da tabela padrão e se for maior que 0, está acima da padrão;
  + parametrodeaprovacao: Pode validar entre %mínimo  e %máximo, se configurado com valor na modalidade;
