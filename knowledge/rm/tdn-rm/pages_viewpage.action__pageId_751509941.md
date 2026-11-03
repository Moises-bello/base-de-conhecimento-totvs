---
content_hash: 5a6cd9f941e962dd956f7ca4996fdf73ff46f35abf13c2fe6b207f1d1c7fcbd7
fetched_at: '2026-06-29T00:11:32.936974+00:00'
page_id: '751509941'
product: rm
source: tdn-rm
title: Relatórios - Gráfico - Desempenho dos Vendedores por Período - Smart View
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=751509941
version: 7
---

Este relatório apresenta um gráfico com o **Desempenho do Vendedores por Período**, promovendo aos gestores o controle sobre estes valores.

Ao acessar este relatório no Smart View é possível de se aplicar os seguintes *Parâmetros de Visualização*:

* **Código da Coligada:** Neste parâmetro é possível de se filtrar as Coligadas, onde o valor padrão *-1*, processa todas as coligadas e caso o usuário queira filtrar uma ou mais coligadas específicas, pode-se realizar esta ação alterando este valor e/ou acrescentando as demais coligadas, através do botão "+" localizado em frente à descrição do mesmo;
* **Código do Empreendimento:** Neste parâmetro é possível de se filtrar o Código do Empreendimento, onde o valor padrão -1, processa todos os empreendimentos e como ocorre com o parâmetro da entidade acima, caso o usuário tenha necessidade, pode-se filtrar um ou mais empreendimentos específicos através dos botões destinados a este fim;
* **Data Início:** Este parâmetro permite ao usuário especificar a data que será utilizada para o início do período da coleta dos dados; e
* **Data Fim:** Este parâmetro permite ao usuário especificar a data que será utilizada para o fim do período da coleta dos dados.

Importante!

Este relatório utiliza os dados das tabelas da [Nova Comissão](https://tdn.totvs.com/pages/viewpage.action?pageId=665033766), portanto as comissões no formato antigo não serão consideradas na composição do mesmo.

Para ter acesso a este relatório, é preciso que o Perfil do usuário tenha acesso à opção: [01.01.04.09] - Comissão: Visualizar.

Após definir estes parâmetros e gerar o relatório, o sistema apresentará as seguintes informações:

* Agrupador **Período**: neste agrupador é exibido o período definidos nos *parâmetros* de *Data Início* e *Data Fim*;
* **Gráfico**: No gráfico são apresentadas as seguintes informações:
  + No eixo vertical:
    - **Nome do Vendedor:**  O sistema apresenta o nome do vendedor que recebeu comissão neste período.

Para esta entidade, o sistema considera como vendedor o *Tipo Pessoa Quem Recebe*, definido nas *[Regras da Comissão](https://tdn.totvs.com/pages/viewpage.action?pageId=665033766)*, igual a *Corretor da Proposta*. 

* + No eixo horizontal:
    - **Valor Total Vendido:** O sistema apresenta a soma dos valores dos Contratos de Venda no qual este vendedor tem comissão, no período selecionado;
    - **% Vendido:** É percentual de vendas deste vendedor em relação ao total de vendas de todos os demais vendedores, no período listado.
