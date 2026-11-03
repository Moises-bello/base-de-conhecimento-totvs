---
content_hash: c0dc4bf0145425c4977819938e653b89322eeb363ca961a0826e66ac90e13bf7
fetched_at: '2026-06-29T00:09:28.006341+00:00'
page_id: '423938616'
product: rm
source: tdn-rm
title: Vincular Contrato com Solicitação de Manutenção
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938616
version: 3
---

Por este processo é possível vincular/desvincular uma Solicitação de Armazém originada do modulo SIGAMNT do Protheus a um Contrato.   
 Para habilitar o processo é necessário que esteja parametrizada e ativa a Integração Manutenção de Ativos x BackOffice RM, também é preciso que a permissão de acesso no perfil do usuário a este menu esteja permitida.

**Vínculo**

Ao selecionar um contrato e executar o processo Vincular Contrato com Solicitação de Manutenção, são exibidas para vinculação somente as Solicitações geradas pelo Modulo SIGAMNT do Protheus, que estão com status pendente ou parcialmente faturada.   
Se a Solicitação estiver participando de alguma de Cotação ou o tipo de movimento de estiver parametrizado para utilizar Faturamento por Valor, o item da solicitação não é apresentado para vinculação.  
Na janela Vínculo/Desvínculo Itens de Contrato x Itens de Solicitação de Solicitação de Manutenção na grid Itens de Contrato, são apresentados os itens de contrato que possuem solicitação de armazém com o mesmo produto, conforme os contratos selecionados na visão.   
Caso seja selecionado um contrato em que o item do contrato não possua solicitação de armazém com item equivalente disponível, o tela de vínculo não é aberta.  
Para realizar o vínculo deve ser selecionado o item na grid "Itens de Contrato" e selecionado o item correspondente na grid "Itens de Solicitação", ao clicar no botão "Vincular" a quantidade do item da solicitação é diminuída no saldo do item de contrato e o registro é incluído na grid inferior "Vinculo de Itens de Contrato x Itens de Solicitação", em seguida se deve clicar no botão "Executar" para que o vínculo seja efetivado.  
Caso ainda exista saldo do item de contrato após realizar o primeiro vínculo, pode-se continuar realizando vínculos com outras solicitações até que o saldo seja zerado.   
Se a quantidade do item da solicitação for maior que o saldo do item do contrato, o saldo do item do contrato será zerado e a quantidade restante do item da solicitação poderá ser vinculada a outro item de contrato com saldo disponível.  
Quando o item de contrato e item de solicitação possuem unidades de medida diferentes, ao realizar o vínculo, é realizada a conversão (desde que ambas unidades tenham a mesma unidade base) e o vínculo é realizado na unidade de medida do item da solicitação.  
**Movimento**: após realizado o vínculo do item de contrato com o item da solicitação, o movimento de solicitação tem o status alterado para "Em Contrato" no campo "Status de Mov. Relacionado ao Contrato" e não é permitido editar o item de movimento.

**Desvínculo**

Para desvincular um item de contrato de uma solicitação deve ser acesso o mesmo processo, os vínculos realizados são exibidos na parte inferior da tela, deve-se selecionar o vínculo que se deseja desfazer e clicar no botão "Desvincular\Reverter", após clicar no botão o saldo do item de contrato e a quantidade do item de solicitação serão atualizados com a quantidade do vínculo a desfazer (que será exibido com valor negativo).   
Após a execução do processo o vínculo será desfeito.  
O botão "Desvincular\Reverter" também pode ser utilizado para excluir da grid um vínculo que ainda não foi efetivado (caso seja realizado um vínculo indevido e ainda não se tenha executado o processo).  
Também é possível reverter um desvínculo (antes da execução do processo) ao utilizar o botão "Desvincular\Reverter".

**Item de Contrato - Aba Vinculações**

Na aba "Vinculações" do item do contrato são apresentadas as solicitações que estão vinculadas ao item, o campo "Quantidade Original" se refere a quantidade que foi originalmente vinculada ao item, o campo "Quantidade" se refere a quantidade do item que ainda não foi faturada, ou seja, a cada faturamento o campo "Quantidade" é diminuído com a quantidade faturada do item (até que seja zerado, quando realizado o faturamento total do item).  
 Não é possível editar dados dessa aba, para alterar vinculações deve-se executar o processo de Desvinculo.  
 ***Observações*:**

* Não é permitido excluir item de contrato que possui vinculação.
* É possível editar informações de um item de contrato com vinculação, exceto os campos Produto e Unidade.
* O processo de cancelamento/descancelamento do contrato não afeta as vinculações realizadas.

**Faturamento**

Depois de realizado o vínculo da Solicitação de Armazém com o Item de Contrato é possível realizar o faturamento dos itens, ao realizar o faturamento do item de contrato(Periódico/Não Periódico) ou da Medição do item de contrato, a quantidade faturada(que está vinculada) é subtraída da quantidade vinculada do item de contrato até que a mesma seja zerada.  
 A quantidade faturada vinculada também é subtraída da quantidade do Item da Solicitação que foi vinculado ao [Contrato](http://tdn.totvs.com/pages/viewpage.action?pageId=423938209), desta forma ao faturar um item de contrato vinculado, o status da Solicitação de origem será atualizado para "Parcialmente Faturado/Recebido" (em caso de faturada quantidade parcial do item de contrato) ou "Faturado/Recebido" (caso seja faturada a quantidade total do item de contrato).  
 Caso exista conversão de unidade no vínculo (unidade do Item da Solicitação diferente da unidade do item de Contrato), o faturamento é realizado com a unidade definida no Item do [Contrato](http://tdn.totvs.com/pages/viewpage.action?pageId=423938209).

**Cancelamento/Exclusão de Faturamento**

Ao excluir ou cancelar um movimento gerado a partir de um Contrato que possui vínculo, a Solicitação vinculada é reaberta e a quantidade do item é atualizada conforme a quantidade do item do movimento cancelado/excluído.  
O Status do Solicitação também é atualizado, assim como o "Status de Movimento Relacionado ao Contrato".  
***Observações***: Não é possível executar o processo "Estornar Item não Recebido" para itens de movimento que foram gerados a partir de Contrato com vinculação. Caso o movimento possua itens vinculados e não vinculados é exibido no processo de Estorno de Item não Recebido somente os itens sem vinculação.   
Se todos itens do movimento possuírem vínculo é exibida mensagem informando que "O Movimento selecionado não possui item para ser estornado".

**Status de Movimento Relacionado ao Contrato**

A coluna "Status de Mov. Relacionado ao Contrato" na visão de movimentos pode assumir os seguintes status de acordo com os vínculos e faturamentos de Contrato:

* **Em Contrato**: esse status é apresentado ao realizar o vínculo da Solicitação ao Item de [Contrato](http://tdn.totvs.com/pages/viewpage.action?pageId=423938209).
* **Faturado Parcialmente pelo Contrato**: esse status é apresentado ao faturar parcialmente um Item de Contrato que está vinculado a Solicitação.
* **Faturado pelo Contrato**: esse status é apresentado ao faturar a quantidade total de um Item de Contrato que está vinculado a Solicitação
* **Gerado pelo Contrato**: esse status é apresentado para os movimentos gerados a partir de Contratos que possuam uma Solicitação vinculada.

**Rastreamento**

Pelo botão "Rastreamento de Movimentos" na visão de movimentos é possível verificar a qual Contrato a Solicitação está vinculada ou a partir de qual Contrato foi gerado o movimento faturado a partir de Contrato.   
As informações do Contrato podem ser visualizadas na grid inferior da tela de Rastreamento na aba [Contratos](http://tdn.totvs.com/pages/viewpage.action?pageId=423938209).
