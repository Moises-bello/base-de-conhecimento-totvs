---
article_id: 4420930004119
category: PMS - Projetos
content_hash: ce0a12143966d281bf116b174838e37316b80219da791b69ea58f188aab5a581
fetched_at: '2026-06-28T22:37:15.973273+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Principais Parâmetros
type: support-article
updated_at: '2024-02-22T19:53:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420930004119-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Principais-Par%C3%A2metros
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21549459996951) Tempo aproximado para leitura: **00:02 min** **Dúvida**

Quais os principais parâmetros do Gestão de Projetos ?   
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAPMS - Todas as Versões.

**Solução**

O Ambiente de Gestão de Projetos (PMS - Project Management System) possui uma série de Parâmetros que determinam a forma de processamento de cada empresa, como por exemplo, o parâmetro (**MV\_****MOEDAn**), que indica quais moedas serão utilizadas para valorizar as movimentações.  
A MICROSIGA envia os Parâmetros padrões, que podem ser alterados de acordo com a sua necessidade. Os Parâmetros são customizados no Ambiente Configurador.  
Abaixo, estão listados os “Parâmetros” mais relevantes do Ambiente de Gestão de Projetos (PMS - Project   
Management System)

**MV\_PMSBXEM -** Este parâmetro indica se exibe ou não a tela de baixa de empenhos na amarração da NFE com o projeto.   
A tela de baixa de empenhos permite ao usuário selecionar o empenho que será baixado na entrada da NF (empenho que foi gerado a partir de uma solicitação de compras amarrada ao projeto ou um planejamento do projeto ) . Esse parâmetro poderá ser útil em empresas que não utilizam o controle de empenhos, facilitando a digitação da NF.  
Conteúdo : Lógico True = Exibe a tela  
False = Não exibe tela

**MV\_PMSCCT -** Indica se utiliza o Template de construção civil e terraplanagem com o PMS. 1=Sim; 2=Não.  
Este parâmetro só deve ser configurado com Sim para as Empresas que possuam o Template de Construção   
Incorporado ao SGAPMS. ( O template de Construção é comercializado separadamente do SIGAPMS ).

**MV\_PMSCUST -** Indica o método de cálculo das quantidades das tarefas dos orçamentos e projetos. 1=Unitário; 2=Total  
Método Unitário : indica que as quantidades informadas nos itens da tarefa ( produtos + recursos + despesas ) são unitárias e serão multiplicadas pela quantidade da tarefa para se chegar ao consumo total exigido pela tarefa. Esse método é, na maioria das vezes, utilizado em empresas de Engenharia e Construção, nas quais as tarefas são consideradas como Composições Unitárias.  
Método Total (default ): indica que as quantidades informadas nos itens são as quantidades previstas totais que serão consumidas pela tarefa.   
**MV\_PMSECOD -** Indica o método de codificação automática utilizado na inclusão de EDTs/Tarefas.

1= Estruturado: método que utiliza uma máscara (definida no cadastro de orçamento/projeto) para estruturação dos níveis do projeto .

Exemplo:  
Máscara: 234 Delimitador :   
Estrutura  
01 – Fundações   
01.01 – Fundação Prédio 1  
01.01.001 – Escavação  
01.01.002 – Limpeza  
01.02 – Fundação Prédio 2  
01.02.001 – Escavação  
01.02.002 – Limpeza  
2 = Sequencial: método que utiliza código sequencial único para codificação das EDTs e Tarefas.  
Estrutura  
0000001 – Fundações   
0000002– Fundação Prédio 1  
0000003– Escavação  
0000004– Limpeza  
0000005– Fundação Prédio 2  
0000006– Escavação  
0000007– Limpeza..

**MV\_PMSEVEN**  
Código de uso utilizado nos eventos para indicar o progresso físico previsto das tarefas do projeto.  
Este código será utilizado na avaliação do progresso físico previsto das tarefas pela técnica dos eventos– marco.  
**MV\_PMSEXP1, MV\_PMSEXP2, MV\_PMSIMP1, MV\_PMSIMP2, MV\_PMSPLN1**  
**MV\_PMSPLN2, MV\_PMSPLN3, MV\_PMSPLN4, MV\_PMSPLN5, MV\_PMSPLN6**  
**MV\_PMSPLN7, MV\_PMSPLN8, MV\_PMSPLNA, MV\_PMSPLNB**  
Estes parâmetros são utilizados internamente pelo SIGAPMS para configuração das colunas das planilhas do Orçamento/Projeto em suas diversas telas do sistema. Recomendamos que a configuração desses parâmetros sejam efetuadas sempre pela configuração das colunas ( Disponível em todas as telas que utilizam o Método planilha para exibição da Estrutura do Orçamento/Projeto)

**MV\_PMSTCOD -** Indica se a codificação será Manual (1) ou Automática (2) na montagem da estrutura do Orçamento/ Projeto.  
**MV\_PMSTEXC -** Indica se as tarefas que já possuem algum tipo de apontamento ( Custo ou Físico ) podem ser excluídas.  
Conteúdo S – Sim / N – Não  
**MV\_PMSVCOD -** Indica se no modo de Visualização do Orçamento / Projeto Árvore o código da Tarefa/EDT será exibido antes da Descrição.  
Conteúdo logico T –True - Exibe o Código F - Fase – Não Exibe

**MV\_PMSIPC -** Indica se utiliza associação automática da NFE com o Projeto amarrado na SC ou PC gerando uma RE5 automática para o Projeto.   
Conteúdo S – Sim - N – Não  
**MV\_INTPMS**  
Indica se a Integração entre o SIGAPMS e os outros módulos da aplicação está ativa, permitindo que  movimentos referentes a Estoques, Compras, Folha, Vendas, etc. alimentem o avanço físico e financeiro realizado dos Projetos.  
Conteúdo S – Sim - N - Não

**Saiba mais:** [Parâmetros Gestão de Projetos](https://tdn.totvs.com/x/FibsF)
