---
content_hash: 87479bc9fea10356a05b6aef2180ffa1b466fa82f325955211355fb868f61e36
fetched_at: '2026-06-29T00:11:38.110860+00:00'
page_id: '781213883'
product: rm
source: tdn-rm
title: API - Plano de Financiamento
type: documentation
url: https://tdn.totvs.com/display/LRM/API+-+Plano+de+Financiamento
version: 3
---

Plano de Financiamento

### Apis de Plano de Financiamento

API: GET: <http://localhost:8051/api/imb/v1/modalities/1/enterprises/20_28>

API que retorna os valores das condições de financiamento de todas as subunidades de um empreendimento, utilizando uma modalidade para simular

API: GET: <http://localhost:8051/api/imb/v1/modalities/1/enterprises/20_28_000001>

API que retorna os valores das condições de financiamento de todas as subunidades de uma unidade de um empreendimento, utilizando uma modalidade para simular

API: GET: <http://localhost:8051/api/imb/v1/modalities/1/enterprises/20_28_000001_000101>

API que retorna os valores das condições de financiamento de todas a subunidade de uma unidade de um empreendimento, utilizando uma modalidade para simular.

Modelo Json Solicitação Geração ComissãoRESPONSEtrueParâmetros

Parâmetros:

* codcoligada: coligada do empreendimento;
* codpessempr: código do emprrendimento;
* numunid: código de unidade;
* numsubunid: código da subunidade;
* area: área da subunidade;
* precoM2: preço do m2 da subunidade;
* precosubunid: preço da subunidade;
* componentesgeradores: componentes da modalidade;
  + codgrupo: código do grupo que pertence a modalidade;
  + codcompn: código do componente;
  + descompn: descrição do componente;
  + valorparcela: valor do componente;

API: GET: <http://localhost:8051/api/imb/v1/Sales/20_1914/rules>

API que retorna os principais campos e valores da condição de financiamento, por venda e utilizando uma modalidade para simular e enviar a proposta

API: GET: <http://localhost:8051/api/imb/v1/Sales/20_1912/rules/generate/1>

API que retorna os principais campos e valores da condição de financiamento, por venda e utilizando uma modalidade para simular e enviar a proposta

API: POST: <http://localhost:8051/api/imb/v1/Sales/20_1912/modality_rules>

API que gera e retorna o plano de financiamento da proposta de venda a partir de uma modalidade

API: DELETE: <http://localhost:8051/api/imb/v1/sales/1_46/rules/1/components/1>

 API para deletar apenas os componentes do gerador de parcela (entrada e principal), sendo que ao deletar esses componentes serão deletados os componentes dependentes como juros e cm se forem o caso.

API: GET: <http://localhost:8051/api/imb/v1/Sales/1_46/modality_rules>

API que retorna os componentes da modalidade que não estejam já inserido na regra da venda.

API: POST: <http://localhost:8051/api/imb/v1/sales/1_46/rules>

API para inserir um componente da modalidade na regra da venda

Modelo Json Solicitação Geração ComissãoPOST - Exemplo requisiçãotrue

API: PUT ou PATCH: <http://localhost:8051/api/imb/v1/sales/1_46/rules/1/components/1>

API para editar componente da regra da venda. somente permite a edição de um campo por vez, exceto a data de vencimento que pode editar com outros campos. Isso, porque um campo interfere em outro cálculo.

Modelo Json Solicitação Geração ComissãoPOST - Exemplo requisiçãotrueCampos Editáveis

* 1º Vencimento; permite editar sempre
* Nro de Parcelas; permite editar sempre
* Valor Parcela; somente pode editar se não for price, sac e sacre
* Valor Total. permite editar sempre

API: GET: <http://localhost:8051/api/imb/v1/sales/20_1/plans>

API que retornar o plano de financiamento com as parcelas geradas a partir das regras cadastradas na proposta

Modelo Json Solicitação Geração ComissãoRESPONSEtrueModelo Json Solicitação Geração ComissãoRESPONSEtrueParâmetros

Parâmetros:

* codcoligada: coligada do empreendimento;
* numvenda : Número da venda;
* codgrupo: código do grupo que pertence a modalidade;
* codcompn: código do componente;
* dsccompn: descrição do componente;
* qtdparc: quantidade de parcela do plano
* valorparcela: valor do componente;
* valortotal: Valor total do Componente financiado
* dataprimeirovencimento: data do primeiro vencimento
* codmodelocalculo: código do modelo de financiamento;
* dscmodelocalculo: descrição do modelo de financiamento;
* percentualcomponente: percentual do componente sobre o valor da proposta;
* valorcomissaocliente: Valor retido na comissão do pagamento pelo cliente;

API: GET: <http://localhost:8051/api/imb/v1/Sales/20_1914/VPL>

API que retornar o cálculo da análise da proposta do cliente comparando com a proposta padrão, entre os indicadores a VPL. Baixe a planilha excel com o cálculo

Modelo Json Solicitação Geração ComissãoRESPONSEtrueParâmetros

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

API: <http://localhost:8051/api/imb/v1/Sales/proposals/1>

API para retornar lista de propostas

Modelo Json Solicitação Geração ComissãoRESPONSEtrue

API: <http://localhost:8051/api/imb/v1/sales/proposals/1_10004>

API buscar uma proposta especifica.

Modelo Json Solicitação Geração ComissãoRESPONSEtrue
