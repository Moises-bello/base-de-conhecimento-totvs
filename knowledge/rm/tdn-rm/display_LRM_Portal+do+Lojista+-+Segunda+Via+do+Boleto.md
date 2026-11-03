---
content_hash: 7c1479fb75dc0bdbb21e7e0954ef3957c1dbdac0259460f781c29c8bd195418c
fetched_at: '2026-06-29T00:05:51.692087+00:00'
page_id: '1053168885'
product: rm
source: tdn-rm
title: Portal do Lojista - Segunda Via do Boleto
type: documentation
url: https://tdn.totvs.com/display/LRM/Portal+do+Lojista+-+Segunda+Via+do+Boleto
version: 7
---

---

### 📋 1. Introdução

O módulo de **Segunda Via de Boleto** tem como principal objetivo facilitar o processo de geração de 2ª via de boletos para os lojistas.

Esse módulo permitirá que os lojistas, através do portal, possam gerar uma segunda via dos boletos de maneira prática, garantindo assim a redução de possíveis atrasos no pagamento de aluguéis ao shopping.

### 🚀 2. Utilização

#### 🔑 Acesso e Permissão para o Usuário

No primeiro momento, será necessário conceder a permissão ao usuário através do cadastro de perfis no Acesso a Menus:

* `Gestão de Imóveis (Portal) \ Cliente \ Boleto 2ª Via`

Atenção!

* Para que os boletos sejam exibidos no Portal do Lojista é preciso [habilitar o uso do contrato de locação para portal e aplicativo](https://tdn.totvs.com/pages/viewpage.action?pageId=435105240#TotvsIncorpora%C3%A7%C3%A3oPar%C3%A2metrosAluguel-Geral2/2).
* Serão exibidos os boletos das entidades abaixo, caso estejam no status Registrado ou Registrado Online

  + Condomínio;
  + Fundo de promoção;
  + Evento Financeiro (avulso);
  + Aluguel complementar.

  Para saber mais sobre a geração e manutenção de boletos acesse a documentação do TOTVS Gestão Financeira:

  + **[Boleto](https://tdn.totvs.com/display/LRM/FIN+-+Boleto)**
  + **[Boleto Híbrido](https://tdn.totvs.com/pages/viewpage.action?pageId=908344227)**
  + **[Pagamento Instantâneo (PIX)](https://tdn.totvs.com/pages/viewpage.action?pageId=603107670)**
* Caso o usuário possua um **boleto agrupado**, cujos lançamentos pertençam a um contrato de aluguel e um contrato de venda, o mesmo boleto irá aparecer tanto na visão de boletos de aluguel, quanto na visão de boletos de venda e seu valor sempre será o valor total de todos os lançamentos que compõem o boleto, independente do contexto selecionado.

### 🖥️ 3. Interface e Funcionalidades do Portal

Ao acessar o Portal do Lojista e selecionar o menu **"Segunda via de boleto"**, o usuário poderá consultar informações detalhadas sobre a situação dos lançamentos do contrato selecionado. Nesta visão, estarão disponíveis as seguintes funcionalidades e blocos de dados:

#### 📊 Painel de Indicadores Financeiros

* **Boletos em Atraso:** Exibe os boletos que estão vencidos e ainda não foram pagos.
* **Próximo Vencimento:** Informa a data de vencimento do próximo boleto a ser pago.
* **Parcelas Pagas:** Lista as parcelas que já foram quitadas.
* **Parcelas a Pagar:** Mostra as parcelas que ainda estão pendentes.

#### 📋 Detalhes dos Boletos (Listagem)

Logo abaixo dos indicadores, serão exibidos os detalhes adicionais sobre cada boleto cadastrado:

* **Situação dos Boletos:** Indica se o boleto está vencido ou a vencer.
* **Código de Barras:** Fornece o código de barras do boleto para pagamento.
* **QR Code:** Disponibiliza o QR Code do boleto para pagamento via dispositivos móveis.
* **Número do Contrato:** Identifica o número do contrato relacionado ao boleto.
* **Vencimento:** Apresenta a data de vencimento do boleto.
* **Valor das Parcelas:** Mostra o valor de cada parcela.

*Essas funcionalidades permitem uma visão completa e clara da situação dos boletos, facilitando o gerenciamento financeiro do lojista.*
