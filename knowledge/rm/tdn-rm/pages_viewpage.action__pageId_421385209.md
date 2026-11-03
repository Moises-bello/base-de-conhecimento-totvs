---
content_hash: aa95166d5b169bf75bb83f270e44800b9e6c4a564f330682c1e75788ddbe6a1c
fetched_at: '2026-06-29T00:09:14.346260+00:00'
page_id: '421385209'
product: rm
source: tdn-rm
title: Parametrizando  Gestão de Estoque Compra e  Faturamento  
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385209
version: 3
---

---

**Acessar o menu principal** do RM | BackOffice| Gestão Estoque, Compras e Faturamento| Ambiente| Parâmetros | Gestão Estoque, Compras e Faturamento| Outras Movimentações.

**Selecionar o tipo de movimento** de compras que será utilizado para requisição de compras na integração com o Totvs Obras e Projetos.

**Clicar em parametrizar** e iniciar a parametrização do tipo de movimento.

**Na aba Projeto** alterar o parâmetro 'Informa Projeto/Tarefa, para 'Obrigatório por Item Movimento ou Obrigatório por Movimento'. Caso este parâmetro esteja desativado não será solicitado o preenchimento do campo 'Projeto (Totvs Obras e Projetos) ' no movimento e nem o campo 'Tarefa (Totvs Obras e Projetos)' no item do movimento. Nesta mesma aba para que seja possível visualizar as apropriações de insumos no RM Solum, marque o parâmetro 'Gera Apropriação'. Se estiver gerando movimento de solicitação de compra para posteriormente gerar o movimento de compra, somente um dos movimentos deve estar parametrizado para gerar apropriação. No caso citado, recomendamos que seja o movimento de compra.

**Na aba Mov. – Data ½** altere o parâmetro 'Data de Entrega' para Mostra, para os tipos de movimentos que são gerados pelo RM Solum e que se deseja controlar a data de início no cronograma previsto, ou seja, ao habilitar esse parâmetro a data de início do período para o qual existe um percentual previsto para o serviço será colocada no campo Data de Entrega. Para que a data de Entrega do item do movimento também seja preenchida é necessário que, o campo Data de Entrega, deve ser selecionada a opção 'Edita' ou 'Consiste'. Se este parâmetro estiver com a opção 'Não Edita' a data de entrega não será enviada. A data de entrega de um item será igual à data de entrega do movimento, quando forem gerados movimentos por período. Se for gerado um único movimento, a data de entrega do item será a data de início do período previsto.

**Na aba Item –Preços** altere o parâmetro 'Preço' para Mostra, para os itens de movimentos para o qual serão preenchidos os valores na geração do movimento no Gestão de Estoque Compras e Faturamento.

**Na aba Rateio C. Custo Departamento** altere o parâmetro Tipo de Rateio = Percentual. Os campos Rateio do Movimento e Rateio do Item, tanto para Centro de Custo, quanto para Departamento, devem ser configurados como usa. 

**Na aba Item – Tab. – Global** altere o parâmetro Edita Centro de Custo e Editar Departamento para Edita.

**Na aba Item – Tab. –** Global altere o parâmetro Edita Centro de Custo e Editar Departamento para Edita. 

Quando algum parâmetro do Gestão de Estoque Compras e Faturamento (relacionado à integração) for alterado e o Totvs Obras e Projetos estiver sendo executado, será necessário reinicializá-lo.

---
