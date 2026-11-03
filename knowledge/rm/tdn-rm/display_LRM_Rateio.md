---
content_hash: 3e71f900fc7d0e3c026b656a260130e4ddce7273323163099f9a077e7b88ea91
fetched_at: '2026-06-29T00:09:29.286983+00:00'
page_id: '423938863'
product: rm
source: tdn-rm
title: Rateio
type: documentation
url: https://tdn.totvs.com/display/LRM/Rateio
version: 2
---

Tem por objetivo proporcionar ao Gestor uma melhor análise dos custos uma vez que informar o centro de custo/departamento do movimento e/ou do item pode não apresentar o real cenário da empresa.   
Através dos rateios é possível avaliar o custo para produzir ou fabricar um produto ou serviço e auxiliar na tomada de decisão em relação ao preço do produto ou serviço vendido. Não restringindo apenas a venda, também é possível controlar os gastos que não é explicitamente ligada a produção, auxiliando ao Gestor direcionar melhor os recursos disponíveis.   
O rateio é a proporção do valor atribuído a um ou mais centro de custo/departamento de acordo com os valores totais do movimento ou item, na visão do produto TOTVS Gestão de Estoques, Compras e Faturamento também é um detalhamento em forma de grid dos custos da empresa apresentando informações que podem ser utilizadas para processos fiscais ou contábeis: Código do Centro de Custo/Departamento, Descrição, Histórico, valores e/ou percentuais etc.

**Rateio por Centro de Custo e Departamento**: Só será apresentado no movimento o recurso de rateio por centro de custo/departamento se nos parâmetros do tipo de movimento, etapa Rateio de Centro de Custo e Departamento, for parametrizada para usar rateio. Nos parâmetros do tipo de movimento, etapa Rateio de Centro de Custo e Departamento, temos a opção:

* Tipo do rateio: Percentual ou Valor.
* Rateio do Movimento: Usa Rateio por Centro de Custo e/ou Usa Rateio por Departamento.
* Rateio do Item: Usa Rateio por Centro de Custo e/ou Usa Rateio por Departamento. Considerações quanto ao rateio por valor:
* Nos parâmetros, etapa Rateio de Centro de Custo e Departamento, ao parametrizar o "Rateio por Valor" é habilitado o campo "Fórmula para o Rateio". A fórmula associada a este campo será o valor total do Rateio. Caso não seja informada nenhuma fórmula, o sistema considera o "Valor Líquido" para o Rateio do movimento e o "Valor do Item" para o Rateio do item.
* Será possível informar o rateio, tanto por valor quanto percentual. Considerações quanto ao Rateio do item.
* É necessário habilitar o rateio do movimento, uma vez que as informações presentes no rateio do item serão carregadas para o rateio do movimento.
* Considerações quanto ao Rateio do movimento:
* Não é possível informar o rateio pelo movimento caso o rateio do item esteja habilitado, o rateio deve ser informado pelo item e ao incluir o movimento, o rateio dos itens será carregado para o rateio movimento.

**Atenção às mensagens ao incluir rateios**: "Deseja incluir um novo rateio por Centro de Custo?" / "Deseja incluir um novo rateio por Centro de Custo?":

* Atente-se ao clicar em "SIM", pois se o "Valor Total Rateado" ultrapassar o valor estipulado para o rateio, o campo "Diferença" não estará zerado e o sistema permitirá a conclusão do rateio, porém não permitirá a inclusão do movimento.
* Se o usuário clicar em "NÃO", não quer dizer que o rateio não possa ser alterado, apenas que o usuário terá que clicar em "Incluir", novamente, caso precise incluir novos centro de custos/departamentos, "Editar" para alterações em registros existentes ou "Excluir" para exclusão do registro propriamente dito.

***Observações***: Ao faturar agrupando dois ou mais movimentos e caso o tipo de movimento de destino esteja também parametrizado com rateio, o sistema copia o rateio dos movimentos de origem para o movimento de destino agrupando os Centro de Custos/Departamento que forem iguais. Você pode exportar a visão de seu rateio utilizando o recurso "Exportar". O arquivo gerado poderá ter as seguintes extensões: .cvs, .xls, .pdf, xlsx, txt e rtf. Após selecionar a extensão desejada o sistema abre o "Assistente de Exportação de Documentos". Caso trabalhe apenas com rateio do movimento existe o recurso "Aplicar default rateios por Cliente/Fornecedor". Este recurso tem por finalidade incluir o rateio presente na Aba "Dados Adicionais" do Cliente/Fornecedor para o rateio do movimento, basta clicar no ícone "Aplicar default rateios por Cliente/Fornecedor " presente na janela de rateios do movimento. Ao faturar um movimento gerando o lançando financeiro, é possível exibir o rateio do centro de custo e/ou departamento no lançamento gerado. O valor do rateio será proporcional ao valor do lançamento, ou seja, se o movimento gerar mais de um lançamento financeiro, cada lançamento terá o seu rateio.

**Código do Grupo Orçamentário no rateio do item**: O Grupo Orçamentário é uma tabela intermediária entre Centro de Custo e a Natureza Orçamentária/Financeira que define um agrupamento dos valores orçados. Considerando a tabela de Classificação dos Períodos.   
Ao criar Períodos de Orçamento com periodicidades coincidentes podemos classificar estes períodos de forma diferenciada.   
A cada centro de custo informado para o rateio do item, é possível habilitar o Cód. Grupo Orçamentário.   
Só é apresentado o campo se na etapa Orçamento dos parâmetros do tipo de movimento, estiver parametrizado para "Editar/Mostrar Tabela de Grupo Orçamentário no item" e o tipo de movimento estiver parametrizado para usar Rateio de Tarefa..

**Rateio de Tarefa**: O Rateio por tarefa é um processo de integração com RM Solum, onde é possível associar um projeto e uma respectiva tarefa a cada centro de custo presente no rateio.   
Só será apresentado no movimento o recurso de Rateio por Tarefa se nos parâmetros do tipo de movimento, etapa Projeto, for parametrizada para usar Rateio de Tarefa. Uma vez parametrizado para usar Rateio de Tarefa será apresentado na janela do rateio do centro de custo dois novos campos: "Projeto" e "Tarefa". Esta parametrização tem a finalidade de melhorar a integração RM Solum x RM Nucleus, já que pelo sistema RM Solum não será mais necessário gerar um movimento para cada tarefa de um projeto.   
Será apenas um movimento e as respectivas tarefas serão tratadas pelo rateio deste movimento.

***Atenção!***

* Para o preenchimento dos campos "Projeto" e "Tarefa" são necessários tê-los previamente cadastrados no RM Solum.
* É possível trabalhar com Rateio de Tarefa mesmo que o Tipo de Movimento não esteja integrado ao RM Solum.
