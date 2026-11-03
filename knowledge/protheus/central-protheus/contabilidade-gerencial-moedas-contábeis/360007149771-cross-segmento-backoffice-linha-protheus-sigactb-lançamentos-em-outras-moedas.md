---
article_id: 360007149771
category: Contabilidade Gerencial - Moedas Contábeis
content_hash: a20ce5a8ff905bce23ba1e148a8ec4c0f482139c89a0ba09004c1ad2349c6318
fetched_at: '2026-06-28T22:40:51.314166+00:00'
product: protheus
section_id: 1500001537601
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Lançamentos em outras
  moedas
type: support-article
updated_at: '2024-03-01T18:01:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007149771-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Lan%C3%A7amentos-em-outras-moedas
---

**Dúvida**

Como efetuar um Lançamento Contábil em outras moedas?

**Ambiente**

Cross Segmento - Backoffice Linha Protheus – Contabilidade Gerencial – A partir da versão 12.1.17

**Solução**

O lançamento contábil leva em conta a conversão da moeda base do sistema(moeda 1) para as demais moedas cadastradas, ou seja, para que se torne possível fazer os lançamentos nas demais moedas, é obrigatório a utilização da moeda 1 no mesmo, não podendo contabilizar somente nas moedas 2 ou 3, por exemplo.

 A configuração da conversão é feita pelo campo CT2\_CONVER, para manipular este campo existe o parâmetro MV\_CRITPLN, neste parâmetro configuramos se o critério de conversão utilizado no lançamento contábil será o cadastrado no Plano de Contas (T), ou o existente no Inicializador Padrão do campo CT2\_CONVER.

* Através do cadastro de moeda (CTBA140) cadastre as moedas que deseja realizar lançamentos

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053407033)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417541190167)

* Através da rotina Moeda X calendário (CTBA200) amarre a moeda ao calendário

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053407053)

* Caso o usuário pretenda utilizar essa configuração diretamente pela Conta Contábil, deverá verificar em seu Plano de Contas(CTBA020) como se encontra o critério para a conta específica assim como no print:
* [Critérios\_de\_conversão\_da\_Contabilidade\_Gerencial](https://tdn.totvs.com/pages/releaseview.action?pageId=233753234)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16429833108887)

Na imagem podemos observar que na aba Conv. Moedas é possível configurar a forma de conversão, e se a moeda irá ser convertida tanto a débito quanto a crédito. Após configurá-la da forma desejada, basta efetuar um lançamento contábil com a conta em questão para que a conversão seja feita.

Ao realizar **contabilização** necessário os cadastros abaixo :

* Através do Cambio(CTBA150)   cadastre as taxas

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16429868952471)

* Através do cadastro do lançamento Padrão (CTBA080) campo CT5\_MOEDA informar para quais moedas deverão ser efetuados lançamentos contábeis.
* Para que  o sistema realize a conversão em outras moedas, se faz necessário preencher a moeda que serão convertidas (moeda 2 , por exemplo preencher o campo CT5\_VLR02)
* Poderá ser preenchido com:

1 - Efetua o lançamento na Moeda.  
2 - Não efetua o lançamento.  
Cada “1” ou “2” representa uma moeda em uso pelo sistema.

Ex: Se o campo for preenchido com  
“11211”, somente na moeda 3 não será  
efetuado o lançamento contábil

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16429868959767)

Exemplo :  [Criação de critério de conversão contábil para o LP 530](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040089154-MP-SIGAFIN-FINA080-Cria%C3%A7%C3%A3o-de-crit%C3%A9rio-de-convers%C3%A3o-cont%C3%A1bil-para-o-LP-530?source=search)

Saiba mais :

* [O intervalo de datas informadas não poderá ser processado.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020540691-MP-SIGACTB-CTBA102-O-intervalo-de-datas-informadas-n%C3%A3o-poder%C3%A1-ser-processado-?source=search)
* [CTBA150 Câmbio](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/ctba150.htm)
* [MP - SIGACTB - CTBA102 - O intervalo de datas informadas não poderá ser processado.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020540691-MP-SIGACTB-CTBA102-O-intervalo-de-datas-informadas-n%C3%A3o-poder%C3%A1-ser-processado-?source=search)
* [MP- SIGACTB- Help: ENTIDOBRIG](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360008112771-MP-SIGACTB-Help-ENTIDOBRIG?source=search)
* [**MV\_CRITPLN**](https://tdn.totvs.com/display/PROT/SIGACTB+-+Diversos+--+24238)
* [**Critérios\_de\_conversão\_da\_Contabilidade\_Gerencial**](https://tdn.totvs.com/pages/releaseview.action?pageId=233753234)
* **[Conversão e lançamento por conta](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020991371-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Convers%C3%A3o-e-lan%C3%A7amento-por-conta?source=search)**
