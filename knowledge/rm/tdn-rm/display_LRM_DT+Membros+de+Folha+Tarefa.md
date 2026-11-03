---
content_hash: c96e6892ee4f63b31ed64ac877205446a10c0d21185ae0a4f81dbc5c2fa58182
fetched_at: '2026-06-29T00:10:16.561987+00:00'
page_id: '471948797'
product: rm
source: tdn-rm
title: DT Membros de Folha Tarefa
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Membros+de+Folha+Tarefa
version: 3
---

# MEMBROS DE FOLHA TAREFA

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos.* |
| **Módulo:** | **Gestão de Obras e Projetos*.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Membros de Folha Tarefa | Membros de Folha Tarefa |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Folha Tarefa | Folha Tarefa | |
| **Cadastros Iniciais:** | Projeto, Insumos, Funções, Equipe de Mobilidade, Pessoas, Funcionários |
| **Parâmetro(s):** | *Não se aplica.* |
| **Ponto de Entrada:** | *Não se aplica.* |
| **Tickets relacionados** | *Não se aplica.* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [TOPORCAPLAN001-6816](http://jiraproducao.totvs.com.br/browse/TOPORCAPLAN001-6816) |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | **SQL Server e Oracle** |
| **Tabelas Utilizadas:** | *Não se aplica.* |
| **Sistema(s) Operacional(is):** | **Windows** |
| **Pacote:** | *Não se aplica.* |

## Descrição

Anexo de Folha Tarefa que permite associar/alocar funcionários à uma determinada folha tarefa do tipo Produtividade.

## Procedimento para Utilização

Para que o pagamento dos funcionários de uma Folha de Produtividade possa ser processado, é necessário que os membros estejam associados à Folha Tarefa do tipo Produtividade. Para isso, existe o anexo de "Membros de Folha Tarefa", onde é possível alocar os funcionários à uma determinada folha. A inclusão do membro pode ser realizada através de três formas diferentes:

* Através da inclusão da tela de edição: Necessário informar o Funcionário e a Data de Inclusão sendo que o Peso e Valor são opcionais. O membros sempre será incluído com a situação de Ativado.
* Através do processo de Incluir Membros na Folha Tarefa: Através da seleção da equipe os membros da mesma são exibidos, onde é possível editar o Valor e o Peso, este, vindo do cadastro de membros de equipe. Também é possível informar a data de inclusão e selecionar somente o membros ativos na equipe. Ao executar o processo os membros serão associados à folha tarefa e será registrado no histórico.
* Através da tela de edição da própria folha tarefa, sendo que essa opção somente estará disponível no momento de criar uma nova folha e não na edição da mesma. É possível realizar a inclusão de um funcionário avulso ou de membros de uma determinada equipe.

O anexo de membros da folha tarefa exibe o valor alocado de cada membro para toda a folha tarefa. Os membros com valor terão seu valor fixo e os que possuem peso terão seu valor calculado com o valor total alocado das tarefas da folha, subtraídos da soma dos membros com valor.

No anexo de membros de folha tarefa existe o processo de Ativar/Desativar Membros da Folha Tarefa, onde é possível alterar o situação de Ativo do membro. Além da ação, é possível definir a data no qual essa ação será considerada, pois essas informações serão registradas como histórico do membro da folha para que possa ser utilizada no momento de gerar o pagamento para a folha de produtividade. As opções de Ativar e Desativar estarão habilitadas de acordo com as linhas selecionadas na visão de membros da folha tarefa, isto é, se somente ativos estiverem selecionados, apenas a opção de desativar estará disponível, e vice e versa.
