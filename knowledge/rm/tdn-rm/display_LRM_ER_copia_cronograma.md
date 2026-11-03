---
content_hash: 7fd18f564100b18fd53458a8e3698a39a25401edc55c2363cf63e621b7f65afb
fetched_at: '2026-06-29T00:06:00.385445+00:00'
page_id: '196805613'
product: rm
source: tdn-rm
title: ER_copia_cronograma
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_copia_cronograma
version: 33
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOP (Totvs Obras e Projetos) |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | R\_C&P\_TOP007 | **IRM1** | PCREQ-5993 |
| **Requisito1** | PCREQ-5995 | **Subtarefa1** | PDR\_CP\_TOP007-1214 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.7 | **Réplica** | não |
| **País** | (x) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | |  |  |  | | --- | --- | --- | | 1 | Cronograma | <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Cronograma.aspx> | | 2 | Tarefas | <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Planilhas.aspx> | | 3 | Cenários | <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Cenarios.aspx> | | 4 | Cópia de Cronograma | $/RM.Net/Docs\_Proj/Roadmap\_2013\_2014/Construcao\_e\_Projetos/Projetos/R\_TOP003/Analise/R\_TOP003\_CopiaDeCronograma.docx | | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## 

## Objetivo

Copiar as informações do cronograma de uma tarefa para outra, dentro de uma mesma planilha.

## Definição da Regra de Negócio

## 

## **1.****Cópia de Cronograma**

Copiar Cronograma é um processo que possui como finalidade copiar os cronogramas de uma tarefa para outra(s). Estes cronogramas são categorizados como “Previsto”, “Medido” e “Realizado”. O usuário poderá selecionar a quantidade e qualquer categoria que desejar. 

De forma técnica a implementação deste processo estará disponível em todas as visões das planilhas, Atividades e Serviços, e também inclui todos os Cenários, com o nome “Copiar cronograma”, conforme o . O desenvolvimento deste processo permite maior rapidez e operabilidade no sistema, de modo que o usuário poderá copiar o cronograma de uma **única tarefa de origem para várias tarefas de destino**.

Com relação ao modo de execução do processo de cópias de cronogramas o usuário poderá selecionar várias tarefas de destino. Diante disso, a execução deste processo segue com as seguintes restrições de modo a efetivar a sua operabilidade:

* A tela do processo somente abrirá se houver alguma tarefa selecionada;
* Somente uma tarefa deverá ser utilizada como origem;
* Tarefas receita, marco, valor cotado, inativas, rateadas ou que sejam obra ou etapa não podem ser utilizadas como tarefa(s) destino, o  ilustra estra restrição.

Obras e etapas não possuem cronogramas diretamente vinculados a eles, as informações que esses tipos de registros exibem são oriundas das subtarefas relacionadas.

Durante a cópia de cronogramas, será copiado o percentual, de modo que a quantidades e o valor serão calculados em virtude do percentual.

De acordo com os processos “Aplicar curva de distribuição” e “Lançamentos Múltiplos”, o processo “Copia de cronograma” não deverá copiar valores para os períodos travados.

Os registros selecionados no campo de destino correspondem aos registros oriundos da mesma planilha, assim como o registro da tarefa de origem responsável pela cópia dos dados. Deste modo, não será possível copiar informações contidas em um determinado cronograma com planilhas diferentes.

Conforme padronizado no sistema, o processo de cópia de cronograma **não efetuará** o cálculo do módulo de cronograma, para que este seja atualizado, com as informações advindas do processo, será necessário, **manualmente**, que o usuário calcule o cronograma. Este mesmo comportamento é realizado no cálculo do projeto.

**2. Execução do Processo**

Na visão das Planilhas de Tarefas (Atividades e Serviços para todos os Cenários), o usuário selecionará a tarefas que deseja realizar a cópia do cronograma. O usuário poderá selecionar uma tarefa agrupadora como destino (como obras e/ou etapas), por conseguinte, todas as subtarefas relacionadas, serão copiadas enviadas como **tarefa(s) destino** automaticamente. Outros tipos de tarefas poderão ser selecionadas, desde que estejam conforme as restrições descritas acima.

Ao abrir o processo será exibido um formulário bem simples, contendo dois campos: um com o escopo das tarefas de destino selecionadas, e outro com um campo para selecionar a tarefa de origem. A escolha da tarefa origem será realizada através da seleção de um tipo de informação, seja ela a descrição, ou o código ou nome do formulário conforme , em seguida, o processo pode ser executado ao clicar no botão “Executar” conforme . O sistema exibirá a mensagem informando que o processo foi executado com êxito, conforme ilustra o .

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [Cópia de Cronograma] | [Downgrade] | [Orçãmento-> Planilha] | - |
|  |  |  |  |

***Tabelas Utilizadas***

* MTAREFA – Tarefas (Atividades e Serviços)
* MTRFPLAN – Cronograma Planejado
* MTRFMEDIDO – Cronograma Medido
* MTRFREAL – Cronograma Realizado

## Protótipo de Tela

**Protótipo 01 - Localização do processo “Copiar cronograma” nas visões das planilhas.**

## **Protótipo 02 - Seleção da(s) tarefa(s) destino.**

## **Protótipo 03 - Pesquisa e seleção da tarefa origem**

## **Protótipo 04 - Tela antes de executar o processo.**

## **Protótipo 05 - Finalização da execução do processo **“Copiar cronograma”.****

## **Protótipo 06 - Mensagem de restrição**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
