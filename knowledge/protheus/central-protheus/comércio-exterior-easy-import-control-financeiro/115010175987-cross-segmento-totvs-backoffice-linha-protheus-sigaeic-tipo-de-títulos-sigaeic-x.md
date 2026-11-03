---
article_id: 115010175987
category: Comércio Exterior - Easy Import Control - Financeiro
content_hash: ac75a03cc11a2bb54fc214c5e04042d0f17676c693a93eaffd9fdd6bc595a691
fetched_at: '2026-06-28T22:39:44.427097+00:00'
product: protheus
section_id: 1500001549642
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Tipo de Títulos  SIGAEIC
  x SIGAFIN
type: support-article
updated_at: '2024-09-13T11:38:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115010175987-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Tipo-de-T%C3%ADtulos-SIGAEIC-x-SIGAFIN
---

**Dúvida**Quais são os tipos de títulos gerados pelo SIGAEIC ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**Este documento tem como objetivo explicar os procedimentos realizados no Easy Import Control (SIGAEIC) para a geração de títulos no Financeiro.  
Serão apresentados os tipos de títulos que são utilizados pelo módulo, as parametrizações necessárias para que haja a geração dos mesmos e possíveis cenários que podem ocorrer no sistema.  
Os parâmetros definem como o sistema irá tratar as movimentações dos processos de Importação.  
Serão apresentados os parâmetros necessários para gerar títulos no Financeiro dos processos do Easy Import Control.

* **MV\_EASY** - Define se haverá ou não integração do módulo de Importação.
* **MV\_EASYFIN** - Define se haverá integração do módulo de Importação com o Financeiro.
* **MV\_EASYFCA** - Define se será gerado título provisório (PR) do câmbio quando há pagamento antecipado.
* **MV\_EASYFPO** - Define se serão gerados títulos provisórios (PR) do valor do processo, das despesas e impostos na fase do PO.
* **MV\_EASYFDI** - Define se serão gerados títulos provisórios (PRE) de Despesas e impostos na fase do Embarque.
* **MV\_PG\_ANT** - Define se o sistema gerará câmbio antecipados e títulos “PA” no Financeiro -**Descontinuado.**
* **MV\_EIC0003** - Define se o título provisório do valor antecipado do processo será ou não excluído em casos de liquidação de pagamento antecipado. (Este parâmetro não é padrão na versão P10, para criá-lo é necessário executar o update UI082956)
* **MV\_COMPAUT** - Define se será realizada a compensação automática no Financeiro do título INV contra o PA (Este parâmetro não é padrão na versão P10, para criá-lo é necessário executar o update UICOMPAUT).

**Atenção:**O parâmetro **MV\_EASYFPO** não pode ser habilitado (S) se o **MV\_EASYFDI** estiver desligado (F).

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028897991)**

**Tipo de títulos**São utilizados no SIGAEIC dois tipos de títulos, os provisórios e os reais. Para melhor compreensão serão apresentados todos os títulos que podem ser utilizados num processo de Importação e em que situação cada um é gerado.

* **PR** – Título provisório, este título é gerado na fase do PO e para pagamentos antecipados.
* **PRE** – Título provisório gerado na fase do embarque/desembaraço.
* **PA** – Título real para pagamentos antecipados do despachante ou do valor do processo.
* **INV** – Título real para pagamento da Invoice.
* **NF** – Título real para pagamento de despesas e impostos.

Cenários  
Para facilitar a compreensão de como o sistema trabalha com relação à geração de títulos no Financeiro, foram criados alguns possíveis cenários explicando os procedimentos realizados pelo sistema em cada situação.  
Com exceção do cenário 1 os demais deverão estar com os parâmetros de acordo com o informado abaixo:

* **MV\_EASY** = “S”
* **MV\_EASYFIN** = “S”
* **MV\_PG\_ANT** = .T.

**Cenário 1**Cliente que não utiliza as outras soluções da TOTVS, parametrização:

* **MV\_EASY** = “N”
* **MV\_EASYFIN** = “N”
* **MV\_EASYFCA** = “N”
* **MV\_EASYFPO** = “N”
* **MV\_EASYFDI** = “N”
* **MV\_EIC0003** = “1”

**Cenário 2**Geração somente de títulos “PA”, “INV” e “NF”, parametrização:

* **MV\_EASYFCA** = “N”
* **MV\_EASYFPO** = “N”
* **MV\_EASYFDI** = “N”
* **MV\_EIC0003** = “1”

**Exemplo:**Ao lançar o Purchase Order (PO) o sistema irá criar o Pedido de Compras no módulo de Compras, mas não irá gerar títulos provisórios no Financeiro.  
Ao lançar o câmbio antecipado o sistema também não gerará títulos provisórios, só gerará movimentação no SIGAFIN quando a parcela for liquidada.  
No embarque/desembaraço os únicos títulos que serão lançados são os da Invoice “INV” quando a mesma for incluída no processo e o despesas quando geradas na rotina de despesas.  
  
**Cenário 3**Geração dos títulos “PA”, “INV” e “NF” e “PR” do cambio antecipado, parametrização:

* **MV\_EASYFCA** = “S”
* **MV\_EASYFPO** = “N”
* **MV\_EASYFDI** = “N”
* **MV\_EIC0003** = “1”

**Exemplo:**Ao lançar o Purchase Order (PO) o sistema irá criar o Pedido de Compras no módulo de Compras e não gerará títulos provisórios no Financeiro.  
Ao lançar o câmbio antecipado o sistema irá gerar títulos provisórios “PR” no SigaFin, o mesmo será substituído pelo título real “PA” quando a parcela for liquidada.  
Caso seja necessário o estorno da liquidação desta parcela, no Financeiro o título “PA” será estornado automaticamente e o “PR” será regerado.  
No embarque/desembaraço os únicos títulos que serão lançados são o da Invoice “INV” quando a mesma for incluída no processo e o das despesas quando geradas na rotina de despesas.  
Os títulos de despesas são gerados na fase na Purchase Order (PO) como título provisórios "PR", na fase de Embarque/Desembaraço como título provisórios "PRE" e ao incluir no Desembaraço , as despesas efetivas do processo será gerado o título "NF".  
  
**Cenário 4**Geração de todos os títulos reais e provisórios, parametrização:

* **MV\_EASYFCA** = “S”
* **MV\_EASYFPO** = “S”
* **MV\_EASYFDI** = “S”
* **MV\_EIC0003** = “1”

**Exemplo:**Ao gerar o PO o sistema efetuará movimentações no Financeiro criando os títulos provisórios referentes às despesas cadastradas na tabela de pré-calculo inserida no PO e do valor total do processo.  
Ao gerar o câmbio antecipado, o sistema deverá criar títulos provisórios “PR” no SIGAFIN referente a cada parcela gerada.  
Ao liquidar a parcela o sistema irá excluir título “PR” e gerar o “PA”.  
Caso seja necessário estornar a liquidação do câmbio antecipado o sistema irá excluir o “PA” e regerar título “PR” no Financeiro.  
Ao gerar o processo de embarque\desembaraço serão gerados os títulos provisórios “PRE” das despesas e impostos referentes às despesas da tabela pré-calculo inserida no processo. Quando a Invoice for inclusa no processo o sistema irá gerar no Financeiro o(s) título(s) “INV” e excluirá os títulos ‘”PR” do valor do processo.  
Neste exemplo será gerado pelo menos um “INV” que será utilizado para compensar o pagamento antecipado “PA”. Caso seja necessário estornar o embarque, o sistema irá excluir o título “INV” e regerá os títulos “PR” do valor do processo.  
Após lançar o embarque com a Invoice o sistema gerará automaticamente o câmbio principal com as parcelas relacionadas aos títulos “INV”.  
No câmbio principal ao vincular o valor pago antecipado á parcela da Invoice o sistema realizará a compensação automática do título “INV” contra o “PA” e ao liquidar as parcelas da Invoice o sistema baixará os títulos “INV” no Financeiro.  
  
**Cenário 5**   
Geração de todos os títulos reais e provisórios, parametrização:

* **MV\_EASYFCA** = “S”
* **MV\_EASYFPO** = “S”
* **MV\_EASYFDI** = “S”
* **MV\_EIC0003** = “2”

**Exemplo:**Ao gerar o PO o sistema efetuará movimentações no Financeiro criando os títulos provisórios do valor do processo e referentes às despesas cadastradas na tabela de pré-calculo inserida no PO.  
Ao gerar o câmbio antecipado, o sistema irá excluir o título “PR” do processo proporcional ao valor antecipado e criará um novo título provisório “PR” da parcela antecipada.  
Ao liquidar a parcela de câmbio provisório o sistema irá excluir os títulos “PR” do principal da *Purchase Order PO* e do adiantamento e irá gerar os títulos do tipo “PA” dos pagamentos antecipados.   
Caso seja necessário estornar a liquidação do câmbio antecipado o sistema irá excluir o “PA” e gerará título “PR” no Financeiro.  
Ao gerar o processo de Embarque/ Desembaraço, serão gerados os títulos provisórios “PRE” das despesas e impostos referente às despesas da tabela pré-calculo inserida no processo.  
Ao incluir a Invoice no processo o sistema irá gerar no Financeiro os títulos “INV” que excluirão os títulos ‘”PR” do valor do processo.  
Neste exemplo será gerado pelo menos um “INV” que será utilizado para compensar o pagamento antecipado “PA”.   
Caso seja necessário estornar o embarque, o sistema irá excluir o título “INV” e regerá os títulos “PR” do valor do processo.  
Após lançar o embarque com a Invoice o sistema gerará automaticamente o câmbio principal com as parcelas relacionadas aos títulos “INV”.  
No câmbio principal ao vincular o valor antecipado á parcela da Invoice relacionada à mesma o sistema realiza a compensação automática do título “INV” contra o “PA” e ao liquidar as parcelas da Invoice o sistema baixa o “INV” no Financeiro.  
  
**Cenário 6**   
Neste cenário o sistema irá gerar todos os títulos reais serão gerados e apenas os provisórios do Embarque/Desembaraço, parametrização:

* **MV\_EASY** = “S”
* **MV\_EASYFIN** = “S”
* **MV\_EASYFPO** = “N”
* **MV\_EASYFDI** = “S”
* **MV\_EASYFCA** = “N”

**Exemplo:**Ao gerar o PO o sistema não efetuará movimentações no Financeiro.  
Ao lançar o câmbio antecipado o sistema também não irá gerar títulos provisórios, só realizará movimentações quando a parcela de câmbio antecipada for liquidada.  
Ao gerar o processo de Embarque/ Desembaraço serão gerados os títulos provisórios “PRE” das despesas e impostos referente às despesas da tabela pré-calculo.  
Ao incluir a Invoice no processo o sistema irá gerar no Financeiro os títulos “INV”.  
Após lançar o embarque com a Invoice o sistema gerará automaticamente o câmbio principal com as parcelas relacionadas aos títulos “INV”.  
No câmbio principal ao liquidar as parcelas da Invoice o sistema baixará o “INV” no Financeiro.   
  
**Importante:** Os títulos provisórios só serão excluídos nos seguintes casos:

* Quando o PO for lançado total no embarque os títulos “PR” serão excluídos, caso seja lançado parcialmente o sistema irá deixar o saldo proporcional à quantidade do(s) item(s) que ficarão no pedido.
* Quando o título real da despesa/imposto for gerado, os “PRE”s só serão excluídos se o valor da despesa gerada possuir o valor total previsto, caso contrário ficará um saldo.
* Ao preencher a data de encerramento no Desembaraço, assim o sistema entende que não há mais nenhuma pendência no processo.
