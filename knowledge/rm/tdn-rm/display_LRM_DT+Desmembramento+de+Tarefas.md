---
content_hash: e7421c4900d2ae27cb8ce9c6fe00b1d949ad0f3db348b69b558850ce5f116ab6
fetched_at: '2026-06-29T00:09:39.864044+00:00'
page_id: '431673179'
product: rm
source: tdn-rm
title: DT Desmembramento de Tarefas
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Desmembramento+de+Tarefas
version: 16
---

# DESMEMBRAMENTO DE TAREFAS PARA FOLHA DE PRODUTIVIDADE

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **Gestão de Obras e Projetos** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Desmembramento de Tarefas | Desmembramento de Tarefas | |
| **Cadastros Iniciais:** | Tarefas, Unidade de Serviço, Local de Serviço e Equipe de Mobilidade |
| **Parâmetro(s):** | Não se aplica |
| **Ponto de Entrada:** | Não se aplica |
| **Tickets relacionados** | Não se aplica |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | <http://jiraproducao.totvs.com.br/browse/TOPORCAPLAN001-4806> |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas Utilizadas:** | Não se aplica |
| **Sistema(s) Operacional(is):** | Windows |
| **Pacote:** | Não se aplica |

## Descrição

Esta melhoria visa a criação de um processo onde é permitido o desmembramento de uma tarefa a partir de vários locais de serviço.

**Importante: Tarefas que possuem divisão não podem ser desmembradas.**

## Procedimento para Utilização

Através do processo "Desmembrar Tarefas", da Planilha de Atividades é possível desmembrar uma atividade a partir de vários locais de serviço e uma Equipe do Projeto.

Após a execução do processo a tarefa selecionada irá se transformar em uma etapa e será criada uma nova atividade para a tarefa original e novas atividades para cada Local de Serviço com os campos de Unidade de Serviço, Local de Serviço e Equipe preenchidos (opcional).

Ex:

Processo Executado

A quantidade desmembrada será dividida igualmente entre as novas tarefas criadas para cada local de serviço selecionado. Ficando o restante para a tarefa original.

O valor de Mão Obra da Tarefa se refere aos valores dos insumos de Natureza "Mão de Obra", onde esses valores não tem a incidência de Leis Sociais.

Através da opção "Adicionar descrição da Unidade de Serviço e Local de Serviço na descrição da(s) tarefas(s) criada(s)" a descrição das tarefas que serão resultado do desmembramento receberá a concatenação das descrições de Unidade e Local de Serviço. Essa opção somente estará disponível se o parâmetro de projeto "Igualar Descrição/Nome da tarefa a Descrição do recurso que está sendo associado" não estiver marcado.

Através dos parâmetros de cores (Parâmetros de Projeto/Exibição/Cores) é possível definir uma cor diferenciada para a tarefa que foi utilizada para o desmembramento.

Caso o processo seja executado novamente para a tarefa original, não será criada uma nova etapa. Neste caso apenas será criado uma nova atividade para cada local de serviços.

Através do desmembramento é possível definir informações para o PERT e cronograma para as tarefas que serão criadas, basta definir a Nova Data Início e a Nova Duração, sendo que essas informações são Data Inicio Programada e Duração da tarefa selecionada, os Dias de Folga e a opção de Sequenciar Datas de Início das Tarefas caso deseje. Ao executar o processo, as tarefas criadas terão suas datas de início programada alteradas, assim como a duração, e no caso de sequenciar as datas das mesmas, serão incluídas as predecessoras em relação à cada tarefa criada, considerando a folga (defasagem).

Se a opção "Criar uma Folha Tarefa de Produtividade para cada Tarefa desmembrada" estiver marcada, serão criadas novas Folhas Tarefas com as respectivas novas tarefas associadas com o valor alocado de acordo com o desmembramento. Para definir o Valor Alocado do item da folha tarefa, existem duas possibilidades, a primeira sem a opção "Recalcular projeto antes de criar as Folhas Tarefas" que calcula a partir do valor unitário da tarefa origem vezes a quantidade da nova tarefa criada, a segunda possibilidade, esta com a opção de recalcular o projeto marcada, busca o valor de mão de obra da tarefa criada, porém é realizado o cálculo do projeto após a criação das tarefas para que o valor possa ser resgatado.
