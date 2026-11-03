---
content_hash: bb035ccc64e9bcd917c4f5ca0ab7a756725da29aa69d335b76b1fe5bca34d699
fetched_at: '2026-06-29T00:09:28.500515+00:00'
page_id: '423938694'
product: rm
source: tdn-rm
title: Processo de Execução do Rateio Gerencial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938694
version: 3
---

*Atenção!*  
   
Esta funcionalidade só está disponível para as bases já migradas para o Novo Modelo do BackOffice.  
   
O processo de Rateio Gerencial tem como finalidade dar suporte em algumas operações onde não é possível determinar o critério de distribuição no momento do registro da operação, isso ocorre geralmente quando o critério para a distribuição só é obtido no final de um determinado período. Dessa forma a operação é registrada em uma conta gerencial transitória ou de apoio e no final do período é realizada a distribuição para as devidas contas gerenciais sem perder o histórico da operação anterior. Para isto, deverão ser cadastrados Mapas de Rateio.  
Através da execução deste processo, a nova distribuição gerencial será realizada gerando novos lançamentos na contabilidade. A indicação do período e o mapa de redistribuição deverão ser informados para a execução do processo.

**Parâmetros**  
Mês para seleção do(s) lançamento(s) contábil(eis);  
Ano para seleção do(s) lançamento(s) contábil(eis);  
Lote: Lote onde serão gerados os lançamentos do rateio. Informe o número para um novo lote. Este lote será incluído automaticamente pelo processo e receberá os novos lançamentos gerados pelo rateio. Para conferir a existência ou não do lote, após informá-lo, utilize o botão de Verificação.  
Descrição: Permite descrever informações referentes ao processo. Esta descrição fará parte do nome do lote que receberá os lançamentos gerados pelo processo.

**Observações**

* Os lançamentos que fazem parte da movimentação das contas selecionadas para o processo segundo o Mapa de Rateio indicado, não poderão estar bloqueados. Lançamentos bloqueados são aqueles que têm diferenças entre os valores de débitos e créditos e também aqueles que estão sendo editados por outros usuários.
* Os lançamentos gerados pelo processo de distribuição gerencial receberão sempre a data do último dia do mês selecionado. Eles serão gerados dentro de um lote que, depois de conferidos, deverão ser integrados ao lote zero para que façam parte dos lançamentos oficiais da contabilidade compondo os saldos e relatórios.
* O processo de rateio gerencial deverá sempre ser executado antes que a Transferência de Grupos Contábeis tenha sido executada, pois após a Transferência, o saldo das contas de receitas e despesas ficará zerado.
* O processo de rateio gerencial irá sempre respeitar a data de fechamento do RM Saldus, ou seja, se a data de fechamento informada nos parâmetros for, por exemplo, 31/03/2009, esse processo só poderá ser executado a partir do mês de abril de 2009.

**I****tens de Rateio**  
Mapa de rateio: Selecione o mapa de rateio a ser executado.  
Os itens de rateio exibidos estão relacionados ao mapa de rateio escolhido. Pode-se selecionar um ou mais itens que serão executados em ordem crescente conforme valor seqüencial.
