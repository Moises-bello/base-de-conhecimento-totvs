---
content_hash: 1212f938b3731abf6b8d0cb1b8c825f6827ec4a07ff547c67307574e29a8e206
fetched_at: '2026-06-29T00:10:35.343281+00:00'
page_id: '528481517'
product: rm
source: tdn-rm
title: CheckBox
type: documentation
url: https://tdn.totvs.com/display/LRM/CheckBox
version: 14
---

# Índice:

---

[^Páginas Filhas://Índice:].\*

# Objetivo:

---

       O objetivo desta página tem por finalidade demonstrar como utilizar um CheckBox no designer de um relatório TReports.

# Introdução:

---

       O controle CheckBox é uma caixa de seleção onde o usuário pode definir seu status como Marcado, Desmarcado ou Indeterminado.  Com esse controle é possível visualizar seleções no relatório, como exemplo, em qual valor percentual de comissão um vendedor se enquadra.

# CheckBox:

---

       Para adicionar um CheckBox em seu designer, acesse a Barra de Controles, clique no ícone do CheckBox e arraste para o seu layout.

       Nas propriedade do seu CheckBox, você poderá escolher uma das 3 opções de status: Unchecked - Checked - Indeterminate.

       Segue um exemplo da visualização da caixa de seleção para cada status definido.

1true2Seleção Automática

      É possível fazer com que o CheckBox seja marcado de forma programada.

Vamos exemplificar com um relatório de vendas de um determinado mês. Neste relatório, vamos fazer com que a comissão do vendedor seja selecionada automaticamente ao imprimir o relatório. Nesse cenário, vamos definir que a comissão desse vendedor será de 5% caso ele atinja um valor total de vendas inferior à R$1500,00. Acima desse valor, sua comissão será de 10%.

       Para isso, devemos definir na propriedade "Estado de Marcação" o status do CheckBox como "Indeterminate".   
       Logo a seguir, temos uma propriedade também chamada como "Estado de Marcação", porém essa possui o menu (...) que permite fazer uma expressão para definir quando o status do CheckBox será "Checked" e quando será "Unchecked".

       Clicando em (...) , será apresentada a janela para definição da expressão.

       Nessa expressão foi definido que, quando o somatório das vendas for menor do que R$1500,00, o status do CheckBox será "Checked". Caso seja maior ou igual à R$1500,00 o status do CheckBox será "Unchecked".

Iif  
(   
Sum( [VALORORIGINAL] ) < 1500,   
[ReportItems.checkBox1.Checked]=true,   
[ReportItems.checkBox1.Checked]=false  
)  
  
       Com isso, o CheckBox para a comissão de 5% será marcado automaticamente quando o somatório das vendas for menor do que R$1500,00.

       É necessário fazer a mesma configuração para o CheckBox da comissão de 10%, porém redefinindo a expressão para que seja definido o status como "Checked" quando o somatório das vendas for maior ou igual à R$1500,00:

Iif  
(   
Sum([VALORORIGINAL]) >= 1500,   
[ReportItems.checkBox2.Checked]=true,   
[ReportItems.checkBox2.Checked]=false  
)  
  
  
  
       Temos então as gerações do mesmo relatório para quantidade de vendas diferentes:

3Múltiplos CheckBox

      É possível fazer com que um CheckBox seja definido como Checked após um grupo determinado de outros CheckBox estiverem com o status Checked.

      Vamos exemplificar com um relatório que é uma Lista de Documentos à serem entregues para determinado setor.

     No CheckBox "Candidato com todos os documento?", acesse a propriedade "Estado de Marcação" e defina como "Indeterminate".

Em seguida, na propriedade logo abaixo, também com o nome "Estado de Marcação", clique no menu (...) que permitira a inserção de uma expressão para definição do status do CheckBox.

A Expressão irá verificar os outros CheckBox definidos e somente definira o seu próprio status como Checked caso todos os outros CheckBox estejam com o status Checked.

Iif

( 

([ReportItems.checkBox4.Checked]==true) And 

([ReportItems.checkBox5.Checked]==true) And

([ReportItems.checkBox6.Checked]==true) And

([ReportItems.checkBox7.Checked]==true),

[ReportItems.checkBox3.Checked]=true,

[ReportItems.checkBox3.Checked]=false

) 

Tendo assim a geração do mesmo relatório preenchendo o CheckBox "Candidato com todos os Documentos?" de forma automática.

falsefalse

**Produto:** TReports

false

**Versão:** 12.1.23 ou superiores

false

**Controle:** Check Box

falsefalse

**Status:** Em Construção

false

**Data:**

false

**Autores:**
