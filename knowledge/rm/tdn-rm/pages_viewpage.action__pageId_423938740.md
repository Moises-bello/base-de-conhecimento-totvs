---
content_hash: 4ddda3cf2e29e072121622dcc0006fbb487f5a59110c60bc435598bd66982b77
fetched_at: '2026-06-29T00:09:28.656583+00:00'
page_id: '423938740'
product: rm
source: tdn-rm
title: Solicitações de Compra e de Cotação (Integração Gestão de Construção e Projetos
  x Gestão de Estoque, Compras e Faturamento)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938740
version: 14
---

Visualizando as Solicitações de Compra e Cotação enviadas do sistema de Gestão de Obras e Projetos para o Gestão de Estoque, Compras e Faturamento.

**Pré-Condições**

1. Acessar o menu de Geração de Pedidos
2. Editar o Perfil do Usuário - Marcar o parâmetro que permite [Editar o Item Integrado] nos tipos de movimento de Solicitação de Compra, Armazém e Compra de Materiais.
3. Editar o Perfil do Usuário e desmarcar o parâmetro que permite [Editar o Item Integrado] nos tipos de movimento de Solicitação de Compra, Armazém e Compra de Materiais.
4. Parametrizar o tipo de movimento de Pedido de Compras para Efetuar a apropriação de custos na tarefa
5. Parametrizar os tipos de Movimento de Solicitação de Compra, Solicitação de Cotação e Pedido de Compra
6. Validar a Permissão de Acesso para o sistema de Gestão de Obras e Projetos
7. Incluir um Projeto
8. Selecionar um Projeto
9. Configurar os Parâmetros do Projeto:
   1. Configurando a máscara
   2. Configurando o Cronograma
   3. Configurar as Integrações entre sistemas - Geral e Tipos de Movimento
   4. Planilha de Atividades
   5. Projeto
10. Incluir Produtos que serão utilizados como Insumos
11. Incluir um Insumo
12. Incluir uma Composição
13. Incluir a Cotação para as moedas utilizadas
14. Incluir a Planilha de Atividades com Obras, Etapas e Tarefas.
15. Gerar o Cronograma da Tarefa e informar o percentual previsto no cronograma
16. Calcular o Cronograma
17. Calcular o Projeto
18. Ter incluído a requisição de materiais e a enviado para o Faturamento.

**Passo 1** - Para visualizar os movimentos de solicitação de compra ou solicitação de cotação, acesse TOTVS Gestão de Estoque, Compras e Faturamento | menu Compras | Solicitação de Compras.

**Passo 2** - Será exibida uma tela de filtragem por tipo de movimento. Informe o código do tipo de Movimento de Solicitação de Compras ou de Solicitação de Cotação, preenchidos na parametrização da pré-condição 9.

**Passo 3**- O sistema exibirá todos os movimentos gerados para o tipo informado. Selecione o movimento desejado e clique no ícone [Editar].Acesse a aba Itens para visualizar os itens enviados pela requisição de materiais. Se o usuário tiver permissão para edição de itens de movimento integrado, o campo quantidade estará habilitado para alteração, a diferença desta alteração de quantidade será enviada para o TOTVS Obras e Projetos.

***Atenção!***

* É permitido aumentar a quantidade somente até o valor máximo solicitado no movimento. Exemplo: Existe uma previsão de 10 unidades e foi gerado um movimento com 5 unidades, neste caso é permitido aumentar até no máximo 5 unidades.
* O sistema permite o cancelamento de um movimento gerado dessa forma. Ao se executar esse cancelamento, o sistema irá estornar os itens para o TOTVS Obras e Projetos.
* O sistema não a Conclusão do Pedido, dos movimentos integrados através do sistema de Gestão de Estoque, Compras e Faturamento. Se for feita a tentativa de exclusão a mensagem a seguir será exibida: "Movimento gerado através do TOTVS Obras e Projetos só pode ser excluído por um processo específico!".
* Se for feita a tentativa de Conclusão do pedido, o sistema exibirá a seguinte mensagem: "O movimento selecionado não possui item originados deste módulo para serem concluídos."
