---
content_hash: 9377a9053545a25f60b300a1b05151d4fec45dd857c013fe404fae6007f6fa41
fetched_at: '2026-06-29T00:11:36.868944+00:00'
page_id: '773518821'
product: rm
source: tdn-rm
title: TCGI - Comissão - Parcela Atrelada a Baixa ou Fórmula Valor Parcela
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=773518821
version: 8
---

### Processo de gerar ou cancelar parcela de comissão atrelada a baixa de lançamento ou do tipo ou Fórmula Valor Parcela

Estes processos encontram-se  na visão de Comissão, menu processos e é Global, ou seja, é executado para as baixas de **todas** as Comissões na competência especificada na execução deste processo.

Processo de Gerar/cancelar Parcela de Comissão Atrelado a Baixa ou Fórmula Valor Parcela, que irá :

* Buscar **todas** as baixas em uma determinada competência para as comissões que tenham o tipo de cálculo atrelado a baixa.
  + Ao realizar a baixa de uma parcela que esteja associada a comissão através do contrato de venda, o sistema irá buscar o percentual da máximo vinculado a parcela para gerar a parcela de comissão na competência da baixa, da mesma forma. o sistema irá cancelar a parcela de uma competência específica.
* Buscar **todas** as comissões que tem o tipo cálculo Valor Parcela Fórmula e tenha saldo devedor do comissionado para gerar a parcela com base na fórmula. **\*12.1.2310**
  + O sistema irá executar a fórmula para definir o valor da parcela e esse valor não poderá ser maior que o saldo devedor do comissionado.

Tipos de Geração de Parcelas Atrelado a Baixa

Define quais tipos de parcelas não podem ser geradas comissão em parâmetros gerais

  

Contrato de Venda encontra-se com Parcela Paga!

Modelo de Cálculo , cadastrado com o Tipo de Comissão Paga pela Empresa : **Percentual máximo vinculado ao recebimento das parcelas.**

Modalidade de Comissão cadastrada com o Modelo de Cálculo e vinculada ao contrato de venda na qual encontra-se uma parcela PAGA.

Comissão encontra-se gerada para o contrato de Venda 9899 e SEM PARCELA de comissão.

Selecionando a Comissão e em seguida : Processos | Gerar Parcela da Comissão Atrelado a Baixa.

Podendo selecionar o Mês corrente ou Data Específica.

Parcela de Comissão criada.

Mostrando o Lançamento da Baixa juntamente com a Parcela de Comissão Gerada.

Valor Parcela Fórmula

Somente a partir da versão **\*12.1.2310**

No cadastro de Modelo de Cálculo seleciono o tipo Valor Parcela Fórmula

Fórmula de Cálculo da Parcela - Será gerado a parcela somente se o valor for maior do que zero -

Comissionado com a configuração e sem parcela gerada

Processo de Gerar Parcela

Selecione a competência para gerar a parcela, o vencimento da parcela será no último dia do mês

Parcela gerada com 40% do saldo devedor por ser a primeira parcela

Log da geração da parcela.

Excluir Parcela Comissão

Selecionar a Comissão na qual foi gerada parcela e em seguida : Processos | Excluir Parcela da Comissão Atrelado a Baixa ou Fórmula Valor Parcela.

Seleciona a Competência e em seguida - Executar.

Parcela Excluída.
