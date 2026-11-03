---
content_hash: c25c19471efc4c7d7c24c2b619a5ae07219532fcec2a1996d8337e9757335c8d
fetched_at: '2026-06-29T00:09:14.952984+00:00'
page_id: '421385315'
product: rm
source: tdn-rm
title: Definir Total
type: documentation
url: https://tdn.totvs.com/display/LRM/Definir+Total
version: 2
---

---

A funcionalidade Definir Total permite alterar o valor geral do projeto em aberto, aumentando ou diminuindo preços dos insumos, grupos de insumos ou serviços. Para acessar a funcionalidade, com o projeto aberto, selecione a aba "Orçamento". A mesma está disponível no menu principal, na parte de "Alterações".  
    
 A tela da funcionalidade é composta:

* **Cenário:** campo no qual deve ser informado o cenário principal do projeto, que será utilizado durante o processo.
* **Planilha:** deve ser selecionada a planilha na qual será aplicada a alteração do valor, se Atividades ou Serviços.
* *Seções:*
  + **Seleção:** onde devem ser informados os subprojetos inicial e final, para cálculo do valor atual do projeto.
  + **Valor da Seleção:** é apresentado o valor atual do projeto (calculado automaticamente após informar os dados na seção "Seleção"), e onde deve ser informado o valor desejado, ou seja, o novo valor do projeto.
  + **Sobre:** onde deve ser selecionado qual grupo de valores sofrerá a alteração. Quando selecionada a planilha de Atividades as opções são Insumos, Grupos de Custo ou Tarefas. Quando selecionada a planilha de Serviços a opção Tarefas será marcada automaticamente.
  + **Variação:** apresenta as variações que o projeto sofrerá. O tipo (se redução ou aumento), o total percentual da variação, e o percentual unitário que cada item sofrerá.
  + **Intervalo de Insumos:** disponível apenas quando o grupo de valores for a opção Grupos de Custo. Nesta seção é possível alterar o intervalo dos insumos do Grupo de Custo, aplicando assim a alteração dos valores apenas para o intervalo desejado.
  + **Opções para Insumo/Grupo de Custo:** permite definir se o preço existente sofrerá alteração ou se será criado um novo preço para os itens selecionados. Caso seja escolhido a criação de um novo preço é possível definir uma descrição ou deixar que seja utilizada a descrição padrão.
* **Grid:** onde são listados os itens com base no que foi informado no cenário, planilha, seleção e grupo de valores. Quando a planilha for a de atividades, grupo de valores Tarefas, serão listadas apenas as tarefas de valor cotado, e que não sejam de valor indireto.
* **Simular Variação:** simula a alteração que será realizada no projeto, informando na seção Variação o percentual unitário de alteração para cada item selecionado.

**Funcionamento**  
 Ao acessar a tela da funcionalidade deverão ser informados o cenário, a planilha e o subprojeto. Inseridas estas informações é realizado o cálculo do projeto e apresentado o valor atual do projeto.  
 Em seguida deve ser informado o grupo de valores. Com base nestas informações é apresentado no grid os itens que poderão sofrer alteração dos valores. Informe o valor desejado, e selecione no grid os itens que sofrerão alteração.

Se desejar:

* Simule a variação (botão "Simular Variação") para preencher o percentual unitário (seção "Variação") e saber o percentual da alteração em cada item selecionado.
* Crie um novo preço e informe a descrição do mesmo (seção "Opções para Insumo/Grupo de Custo").
* Altere o intervalo dos insumos do Grupo de Custo no qual será aplicada a variação.

Após executar o processo, será informado no final o percentual de variação aplicado, se foi ou não criado um novo preço, o valor antigo e o atual do projeto, e uma listagem com os insumos alterados, com código, descrição, valor anterior e valor atual.

**Importante!**  
 Não será possível executar o processo quando:

* O valor atual for menor que zero.
* O valor desejado for menor que zero.
* Não tiver sido definido grupo de valores (Insumos, Grupos de Custo, ou Tarefas).
* A soma dos percentuais dos itens selecionados não for maior que zero.
* A redução desejada corresponder À redução total dos itens selecionados.

Em todas as situações serão apresentadas mensagens informando o motivo da não execução do processo.
