---
content_hash: 45980542725659f4bca4d05ad773c3a178783c78f8494a493e0a41b6d092799c
fetched_at: '2026-06-29T00:10:08.819132+00:00'
page_id: '452719586'
product: rm
source: tdn-rm
title: Configuração de Competência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719586
version: 4
---

Etapa utilizada para configurar de modo global o caixa de cálculo da Folha de Pagamento e definir a descrição dos períodos e a data de fechamento da folha. Também é possível consultar a competência atual da base.  
   
   
**Competência**  
Exibir a competência atual da base. Não é possível editar esse campo, sendo o mesmo alterado através do processo de liberação de competência.   
   
   
**Caixa**  
Permite definir o mês e ano caixa para pagamento do eventos.  
O sistema permite informar o mês de pagamento igual ou o posterior ao mês da competência. Para a competência de Dezembro, o sistema permite o usuário informar mês 1 para mês-caixa se ano-caixa for posterior ao ano da competência. Para o campo ano é permitido cadastrar um ano-caixa posterior ao ano competência somente se o mês da competência for 12 e o mês-caixa 1.  
   
   
**Período**  
Permite definir o número do período e o dia para pagamento do eventos.  
O sistema valida o dia de pagamento de acordo com o mês-caixa informado, não permitindo para o dia um valor maior que o último dia do mês. Para o período é validado se o mesmo é diferente de 0 (zero).  
  
  
**Descrição de Períodos**  
Exibe a descrição de Períodos. O usuário poderá nomear seus períodos para facilitar a identificação de seus lançamentos. A descrição dos períodos pode ser cadastrada em Cadastro | Tabelas Dinâmicas | PDESCPER e quando o usuário informa um período cadastrado na tabela PDESCPER o campo mensal é preenchido automaticamente com nome do período cadastrado de acordo com o código do período atual e afeta todas as coligadas. Os demais campos deverão ser preenchidos manualmente.

**Exemplo**

Período 1 : Adiantamento

Período 2 : Folha de Pagamento

**Observação**

Caso haja a necessidade de utilização de períodos pré-definidos, advertimos que há a necessidade de que a criação desses períodos respeitem a ordem cronológica de pagamento.

**Atenção**

Essa opção foi criada apenas para ajudar o usuário na identificação de seus lançamentos, portanto o sistema não fará nenhum tipo de controle com relação a movimentação a ser lançada. Por exemplo, o usuário poderá estar no período com a descrição "Folha de Pagamento" e lançar o Adiantamento Salarial que o sistema não fará nenhuma consistência.  
  
  
**Exibir descrição de períodos**  
Com parâmetro marcado criará/atualizará na tabela dinâmica PDESCPER o período e sua descrição, buscando sempre do campo **'Mensal'** e exibirá no nome do período no rodapé da tela principal do sistema, nos processos de entrada de movimento.

**Observação**   
No processo de liberação de competência no campo de 'Descrição do Período' caso informe um nome para um novo período ou um que já exista na tabela dinâmica PDESCPER o mesmo não será atualizado e nem criado.   
Caso informe um novo período não existente na tabela dinâmica o sistema no processo de liberação de competência retornará uma mensagem "Não existe uma descrição para o período selecionado", informe a descrição para o campo 'Mensal', lembrando que não criará este novo período na tabela dinâmica.  
   
   
**Data de Fechamento da Folha**   
Esse parâmetro é utilizado apenas em integrações com SAP, para validar a data de importação de registros. Ele deve ser atualizado manualmente no parametrizador sempre que necessário.  
   
[<<Retornar para **Parametrizador**](http://tdn.totvs.com.br/display/LRM/Parametrizador)
