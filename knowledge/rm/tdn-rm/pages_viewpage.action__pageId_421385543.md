---
content_hash: e913f767459eee8f5c10eb7995ede0d5355a68bf4ef4a1c206c31bef0ad8a6db
fetched_at: '2026-06-29T00:09:16.746004+00:00'
page_id: '421385543'
product: rm
source: tdn-rm
title: Relatório de Tarefas por Grupo de Custo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385543
version: 1
---

**Relatório de Tarefas por Grupo de Custo**   
O Relatório de Tarefas por Grupo de Custo exibe as tarefas da planilha de atividades, da planilha de serviços ou dos cenários  de um projeto.   
Para gerar o relatório acesse: Menu "Relatórios"|"Tarefas"|"Planilha de Tarefas". E no momento da execução pode-se optar entre os relatórios denominados "Tarefas por Grupo de Custo (por Valor)" ou "Tarefa por Grupo de Custos (por Custo)".  
O valor dos grupos de custo e o total da tarefa são compostos pela soma do valor produtivo com o valor improdutivo. Sendo que no relatório que apresenta o custo, será considerado o valor de custo e custo improdutivo.  
As informações contidas no relatório são:

* Código da Tarefa;
* Nome;
* Unidade;
* Disciplina;
* Quantidade;
* Valor da mão de obra;
* Valor de materiais;
* Valor de equipamentos;
* Valor de transporte;
* Valor total da tarefa;
* Valor total da etapa;
* Valor total da obra;
* Valor total do projeto.
* Custo

É opcional a execução do recalculo da curva ABC que poderá ocorrer antes da execução. Para isto, o deve-se marcar a respectiva opção.  
   
**Restrições**  
Este relatório será padrão no sistema e por questão de segurança o usuário não poderá editar ou excluir o mesmo, podendo duplicá-lo para criar seu próprio relatório customizado.  
O padrão atende à estrutura das planilhas de atividades/serviços que possuem a hierarquia definida em obra, etapa e tarefa. Contempla assim todos os níveis. Permite customizar, adicionando quantos níveis forem necessários.  
Ao customizar o relatório, será necessário adicionar filtros específicos para determinar o conteúdo apresentado para obra, etapa e tarefa conforme abaixo:  
Obra -> Serviço = 0 e Quantidade > 0;  
Etapa -> Serviço = 0 e Quantidade IS NULL;  
Tarefa -> Serviço = 1.  
   
**Filtros**  
-Por Cenário e Tipo de Planilha: Selecionar qual a planilha a ser utilizada para gerar o relatório;  
-Tarefa Inicial e Final: Filtro para selecionar inicio e fim do intervalo de tarefas a serem exibidas no relatório;  
-Por Disciplina: Ao selecionar uma ou mais disciplinas para o filtro do relatório, serão exibidas no relatório gerado apenas as tarefas associadas as disciplinas constantes do filtro.  
**Observação:** O usuário que tem acesso para gerar relatórios, só conseguira gerar relatórios para Tarefas sem disciplina associada ou para as disciplinas que o usuário tiver acesso.  
   
**Localização do Relatório**  
Pasta "Objetos Gerenciais" localizada no diretório de instalação do Produto.  
   
 

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Disciplinas  
Curva ABC de Grupo de Custo  
Grupo de Custo Planilhas
