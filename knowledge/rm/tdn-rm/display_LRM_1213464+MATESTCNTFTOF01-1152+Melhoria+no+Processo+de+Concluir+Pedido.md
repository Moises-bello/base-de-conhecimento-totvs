---
content_hash: d76252933bdab7ecf4049957bad2585d286606b5d4bfd4037463980b8e522e1b
fetched_at: '2026-06-29T00:08:47.182000+00:00'
page_id: '319784819'
product: rm
source: tdn-rm
title: 1213464 MATESTCNTFTOF01-1152 Melhoria no Processo de Concluir Pedido
type: documentation
url: https://tdn.totvs.com/display/LRM/1213464+MATESTCNTFTOF01-1152+Melhoria+no+Processo+de+Concluir+Pedido
version: 4
---

# MELHORIA NO PROCESSO DE CONCLUIR PEDIDO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção & Projetos. |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento. |
| **Função:** | Concluir Pedido. |
| **Situação/Requisito:** | Ao executar o processo de **Concluir Pedido** para um movimento de Solicitação de Compras que estava relacionado a uma cotação cancelada, a mensagem abaixo era apresentada:  **O processo não pode ser executado, possíveis causas:**  **- O movimento selecionado não possui item originados deste módulo para serem concluídos.** **- O movimento possui itens que estão participando do processo de cotação.**  Dada a apresentação dessa mensagem, o usuário alternava para a execução do processo de **Cópia de movimento a partir de itens não cotados**, onde o mesmo era utilizado em situações cuja solicitação participa do processo de cotação, mas nem todos seus itens não. Entretanto, ao salvar o movimento com o item que não estava sendo cotado, a mensagem abaixo era apresentada:  **Não é possível excluir itens do movimento quando a soma da quantidade dos itens restantes seja igual a 0.** **Para realizar a conclusão deste movimento deve-se utilizar o processo 'Concluir Pedido'.**  Todavia, o processo de **Cópia de movimento a partir de itens não cotados** era utilizado quando existia os processos em Delphi. Com a migração da Cotação e Movimento para a tecnologia .Net esse processo tornou-se obsoleto, conforme situação descrita e tratada no chamado **TFXFKT - Desativação do processo** **"Cópia de movimento a partir de itens não cotados"**. |
| **Solução/Implementação:** | Melhoria no processo de **Concluir Pedido** para permitir a conclusão de Solicitações de Compras que possuem status do Item da Cotação como estornado ou excluído.  Para Ordem de Compra gerada pela cotação cria-se a possibilidade de Concluir Pedido, uma vez que anteriormente essa ação não era permitida.  Por se tornar obsoleto, houve a remoção do processo **Cópia de movimento a partir de itens não cotados**, onde deverá ser utilizado único e exclusivamente o processo de **Concluir Pedido** para os cenários supracitados. |
| **Conversores e Parâmetros:** | Este processo só pode ser executado em movimentos com status **Pendente**, **Parcialmente Faturado**, **Parcialmente Recebido**;  A conclusão de movimento realiza todas as operações para que o sistema identifique o movimento como se o mesmo tivesse sido totalmente recebido/faturado. Estas operações são: Estorno do efeito do estoque, do orçamento, do financeiro;  Após o movimento ser concluído seu status muda para **Recebido** ou **Faturado**, conforme tipo de movimento utilizado;  O movimento concluído não estará disponível para continuar o faturamento e o **movimento/cotação** que o originou não voltará a ficar com status pendente. Para isso deve ser utilizado o processo de **Estornar Item não Recebido**;  Atualmente não tem como estornar a conclusão do movimento;  Os dados da conclusão de movimento como **motivo**, **usuário** e **data de conclusão** são gravados na tabela **TMOTIVOCONCLPED**, para efeito de consulta e posterior emissão de relatórios para controle gerencial. |
| **Tickets relacionados:** | 1213464. |
| **Requisito:** | MATESTCNTFTOF01-1152. |
| **Documentos de Referência:** | [Wikihelp - Conclusão de Pedidos](http://wikihelp.totvs.com.br/WikiHelp/EST/EST.ConclusaoPedidos.aspx).  [DT - Melhorias No Processo de Conclusão](http://tdn.totvs.com/pages/viewpage.action?pageId=212894614). |
