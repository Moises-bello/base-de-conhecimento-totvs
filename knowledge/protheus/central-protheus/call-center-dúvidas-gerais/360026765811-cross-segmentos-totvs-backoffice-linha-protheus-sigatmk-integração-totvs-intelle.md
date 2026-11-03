---
article_id: 360026765811
category: Call Center - Dúvidas Gerais
content_hash: ebcfc42e4801c466966e00ff9f702c35e0a2939439c28864f8c8bc23e1cc1482
fetched_at: '2026-06-28T22:41:26.837734+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK- Integração Totvs
  Intellector x Call Center
type: support-article
updated_at: '2022-06-17T16:37:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026765811-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Integra%C3%A7%C3%A3o-Totvs-Intellector-x-Call-Center
---

**Dúvida**

O que é a integração Totvs Intellector no Call Center?

Ambiente

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK- a partir da versão 11.80.

**Solução**

A integração do Microsiga Protheus® com o Intellector é feita por um WebService e tem como objetivo avaliar o risco do cliente no momento da venda e calcular o limite de crédito no seu cadastro e alteração.

Os processos envolvidos são **[Front-Loja (Atendimento)](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/frta271.htm), [Emissão de Pedido de Venda](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/mata410.htm), [Televendas](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/tmka271.htm) e [Cadastro e Alteração do Cliente](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/mata030.htm).**

Alguns parâmetros são utilizados para realizar a integração:

[MV\_TIPACRD](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/sigatmk_t.htm):Define a maneira como é feita a análise de crédito. Apresenta as opções 1=SIGACRD (default) e 2=INTELLECTOR.

[MV\_TOLUSUA](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/sigatmk_t.htm): Define o usuário de execução do Intellector.

[MV\_TOLSENH](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/sigatmk_t.htm): Define a senha de execução do Intellector.

[MV\_TOLURL](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/sigatmk_t.htm): WSDL Intellector. Define o caminho de conexão do servidor em que o Intellector está instalado.

[MV\_TOLPOVE](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/sigatmk_t.htm): Define o nome da política de venda criada no Intellector.

[MV\_TOLPOCL](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/sigatmk_t.htm): Define o nome da política de cliente que criada no Intellector.

[MV\_TOLTIVE](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/sigatmk_t.htm): Define o nome do tipo de política de venda liberada no Intellector. O tipo de política é fornecido junto com a licença do produto.

[MV\_TOLTICL](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/sigatmk_t.htm): Define o nome do tipo de política de cliente liberada no Intellector. O tipo de política é fornecido junto com a licença do produto.

[MV\_TOLLAYO](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/sigatmk_t.htm): Define o nome do layout criado no Intellector.

Obs. Esta documentação também pode ser obtida no Help Online da rotina:**<http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/sigatmk.htm>**
