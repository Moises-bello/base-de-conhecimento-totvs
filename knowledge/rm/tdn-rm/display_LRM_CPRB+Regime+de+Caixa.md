---
content_hash: 811b0f38e33a7acf3016c567318265daa0f5354402d0907aa7bafe7966c226cd
fetched_at: '2026-06-29T00:10:52.220491+00:00'
page_id: '571010139'
product: rm
source: tdn-rm
title: CPRB Regime de Caixa
type: documentation
url: https://tdn.totvs.com/display/LRM/CPRB+Regime+de+Caixa
version: 6
---

**Regime de caixa**: As receitas e despesas da empresa só são contabilizadas quando ocorrer recebimento ou pagamento e não quando são negociadas, compradas ou vendidas. Dessa forma a empresa só é tributada pelos valores recebidos e não os valores registrados no momento de emissão da Nota Fiscal.

false1true1Apuração da CPRB por Regime de Caixa

As informações para a geração da base de cálculo e valor do Tributo neste regime serão carregadas exclusivamente dos Lançamentos Financeiros.

Os Lançamentos serão selecionados de acordo com as informações de Tipo de Documento gravadas no [Cadastro de Parâmetros de Processos](http://tdn.totvs.com.br/pages/viewpage.action?pageId=490650588).

A Apuração da CPRB será feita exclusivamente pela Filial Matriz que pode ser definida nos parâmetros do TOTVS Gestão Fiscal, processo 03.02.10 (IRRF Pessoa Jurídica), etapa 11 (Filial Matriz).

No cadastro da Filial Matriz (Anexo Dados Fiscais | Tributos) deverá ser informado o tipo de apuração da CPRB que ela irá executar.

Imagem

Mesmo sendo um Tributo Federal que deve ser apurado centralizado todas as Filiais deverão possuir o Período de Apuração para o Tributo do tipo **Contribuição Previdenciária.**Os lançamentos financeiros deverão ser gravados na devida filial.

Quando se tratar de Filial SCP a apuração será individualizada para cada uma delas.

2Origem das informações

Serão selecionados no processo todas as baixas de Lançamentos Financeiros a Receber efetuadas no período da apuração e que possuam os documentos informados no  [Cadastro de Parâmetros de Processo](http://tdn.totvs.com.br/pages/viewpage.action?pageId=490650588).

false2lefttrue1Lançamentos Financeiros Manuais ou integrados

**Lançamentos Financeiros Manuais ou integrados:**Uma vez que estes não possuem informação de Item deverão ter gravados em seu anexo Dados Fiscais o código de Atividade da Atividade Econômica. Neste caso somente um código é permitido.

Imagem2Lançamentos Financeiros originados no TOTVS Gestão de Compras ou Gestão Fiscal

**Lançamentos Financeiros originados no TOTVS Gestão de Compras ou TOTVS Gestão Fiscal:** Neste caso para o correto cálculo do valor da receita os produtos utilizados nos Itens do Movimento, somente os que comporão a receita, devem possuir o Código de Atividade Econômica preenchido no anexo Dados Fiscais do Produto.

Imagem3Lógica

* Movimento/Lançamento Fiscal com somente um item e baixa total: O valor da receita será o valor da baixa.
* Movimento/Lançamento Fiscal com mais de um item e baixa total: O valor da receita será o valor da baixa rateado em relação ao valor de cada item. Os de mesmo Código de Atividade serão agrupados. Se houver item sem Código de Atividade Econômica ele não participará da apuração.
* Movimento/Lançamento Fiscal com mais de um item e baixa parcial: O valor da receita será o valor da baixa parcial rateado em relação ao valor de cada item. Os de mesmo Código de Atividade serão agrupados. Caso este Lançamento Financeiro sofra várias baixas no mesmo mês para o cálculo da receita serão consideradas todas elas. Os valores restantes serão considerados nos respectivos meses de suas baixas. Se houver item sem Código de Atividade Econômica ele não participará da apuração.
* Quando houver Devolução e a mesma deverá estar vinculada ao Lançamento Financeiro: O valor da receita será o valor baixado no Lançamento Financeiro rateado em relação aos itens do Lançamento Fiscal/Movimento que possuírem Código de Atividade Econômica.
* Devoluções (a pagar) que não estão associadas a Lançamentos Financeiros: Serão totalizadas por Código de Atividade e demonstradas na coluna Exclusões do respectivo Código de Atividade/Alíquota/Código de Receita.
* A alíquota a ser aplicada à base da CPRB para o cálculo do valor a pagar será carregada do [Cadastro de Códigos de Atividade Econômica.](http://tdn.totvs.com.br/pages/viewpage.action?pageId=493625982)

ImagemInformações

* O cálculo da proporcionalização será feito sempre entre o valor da baixa do Lançamento Financeiro e o valor bruto do Item do Movimento ou Lançamento Fiscal.
* O Código de Receita  para o recolhimento será carregado:
  + Do cadastro do Tributo CPRB para Lançamentos Financeiros originados do RM Fluxus
  + Do Tributo contante no Item do Movimento/Lançamento Fiscal para Lançamentos Financeiros que possuírem esta origem. Quando o Tributo CPRB não existir nos itens destas origens o Código de Receita será carregado do Cadastro do Tributo.
  + Se o Código de Receita não existir em nenhum destes lugares ficará vazio na Apuração.
* Os campos de Valor Total do Faturamento e Valor Exclusões Faturamento devem estar preenchido no Período de Apuração da Filial Matriz para que a apuração seja executada.
* Quando no valor do imposto da receita houver uma diferença de 0,05 centavos em relação ao imposto total dos itens, o valor de imposto considerado será a soma dos itens. Caso contrário será mantido o imposto do valor total da receita.
