---
content_hash: 9e2844b6c23d2c17c12ed4152917c8e729359aed28998f9734f7381a560254c9
fetched_at: '2026-06-29T00:09:47.755357+00:00'
page_id: '435105062'
product: rm
source: tdn-rm
title: Plano - Componentes
type: documentation
url: https://tdn.totvs.com/display/LRM/Plano+-+Componentes
version: 10
---

Nesta opção serão cadastrados os componentes que posteriormente estarão associados a uma [Modalidade de Venda](https://tdn.totvs.com/display/LRM/Plano+-+Modalidades) ou diretamente nas [Condições de Financiamento](https://tdn.totvs.com/pages/viewpage.action?pageId=435105209) da Venda.  
Exemplo: Sinal, Mensais, Semestrais, Anuais, Correção Monetária, Taxa de Juros, Taxa de Seguro, etc.

Através deste cadastro é possível controlar:

**Identificação**  
Ao cadastrar ou editar um componente, abrirá a janela de edição, na pasta Identificação, onde iremos cadastrar os seguintes campos:

* **Código**: Referência numérica para o código do tipo de componente;
* **Descrição**: Descrição do componente;
* **Tipo de Componente**: Informe o Tipo de Componente que irá agir sobre este componente cadastrado;
* **Tipo de Parcela**: Informe o Tipo de Parcela. Se este componente irá ter uma parcela exclusiva no plano de financiamento; Poderá ser associado somente um tipo de parcela por componente e após a utilização do tipo em um plano de financiamento não poderá mais ser modificado do componente.
* **Surgimento do Componente**: Informe se o componente surgirá na geração ou na valorização do plano. Na geração significa que no momento da venda e na geração do plano de financiamento, o componente já será criado. Na valorização, o componente só será criado se ocorrer algum evento na parcela. Por exemplo, o componente de desconto surgirá na valorização, pois é uma negociação da parcela no momento do pagamento, ou seja, se o cliente pagar uma parcela com desconto, este componente será criado apenas para esta parcela;
* **Ação do Componente**: Informe se a ação deste componente irá ocorrer antes da entrega do empreendimento, após a entrega do empreendimento ou em ambos os casos;

Para Escolher a ação do componente, ele tem que ser do tipo Juros ou Correção Monetária. Somente nestes dois tipos de componente, poderá ter uma diferenciação na ação do componente com relação à data da entrega do empreendimento.

* **Componente compõe valor base para o cálculo de**: Informe se este componente cadastrado, irá compor o valor base para efetuar os cálculos de Juros de Contrato e/ou por Correção Monetária.

Para escolher o tipo de reajuste do componente, terá que ser de um tipo diferente de Juros ou Correção Monetária, pois estes componentes já são de um tipo de reajuste.

* **Desconsiderar valor na exportação para SPED / DIMOB:** Ao marcar esta opção o sistema deixará de considerar o valor do componente na exportação para o SPED e DIMOB.

Informações - DIMOB

Para o DIMOB, caso o componente gerador da parcela estiver definido para desconsiderar o valor, então todos os demais componentes que compõem o valor desta parcela também serão desconsiderados independente da sua configuração.

Exemplo: Parcela é composta pelo componente Mensal, CM e Juros. O componente Mensal foi configurado para ser desconsiderado no valor final. Portanto o valor do componente Mensal, do CM e do Juros serão desconsiderados.

No mesmo exemplo a cima, caso o usuário tenha definido que somente o componente CM seja desconsiderado, então o DIMOB irá gerar o valor composto pelo componente Mensal e Juros.

* **Sobre componentes de Juros e CM:** Se algum componente de Juros ou CM estiver sendo utilizado em alguma venda, este não poderá ser alterado nem excluído. A regra do plano de financiamento só deve ser alterada através da venda.

Informações Complementares

---

Componentes que geralmente são utilizados são:

* [Entrada](https://tdn.totvs.com/display/LRM/Componentes+-+Componente+de+Entrada)
* [Principal](https://tdn.totvs.com/display/LRM/Tipos+de+Componentes+-+Principal) (Mensal, Bimestral, Semestral, Anual)
* [Juros](https://tdn.totvs.com/display/LRM/Componentes+-+Componente+de+Juros)
* [Correção Monetária](https://tdn.totvs.com/pages/viewpage.action?pageId=435105184)
* [Resíduo](https://tdn.totvs.com/pages/viewpage.action?pageId=435105140)
* [Encargos](https://tdn.totvs.com/display/LRM/Componentes+-+Componente+de+Encargos)

* [Seguro por Empreendimento](https://tdn.totvs.com/display/LRM/Incluir+Componente+de+Seguro+por+Empreendimento)

**Processos**- Gerar Todos os Valores de Integração

Recomendamos que este processo seja utilizado para que os valores de integração sejam gerados corretamente com as ações necessárias ao Financeiro.

  O processo de gerar todos os valores de integração, fará a geração e até mesmo a correção das ações dos valores de integração que já exista na base do cliente, para isso o processo se baseia no tipo de componente do TCGI selecionado para o componente.
