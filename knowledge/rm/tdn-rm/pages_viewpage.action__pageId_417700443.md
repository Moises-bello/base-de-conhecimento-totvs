---
content_hash: 213f76d774fa233b90ddecf73b7e612a845519fbdf7407aff7f275e1005815aa
fetched_at: '2026-06-29T00:09:12.409024+00:00'
page_id: '417700443'
product: rm
source: tdn-rm
title: Taxa de Componente Cirúrgico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=417700443
version: 1
---

**Taxa de Componente Cirúrgico**   
O cubo taxa de componente cirúrgico faz parte das estatísticas do menu Relatórios. Expressa as taxas de cirurgias que permite você analisar os dados pelas dimensões (linha, coluna e filtros) disponíveis.   
   
Filtro: Sítio Primário e Sítio Secundário.  
Quando selecionar filtro sítio primário "todos os sítios" o relatório apresentará um resultado trazendo todas as infecções por todos os sítios.  
Quando selecionar um filtro por um determinado sítio primário você poderá também selecionar todos os sítios secundários ou algum especifico.  
Dimensões: IRIC, procedimentos, anestesista, anestesia, tipo de cirurgia, potencial de contaminação, cirurgião/função, ano/trimestre/mês/semana/dia, especialidade.  
Fato de análise: infecções, cirurgias, taxas.  
Comparativo de Cirurgião está presente no relatório de Componente Cirúrgico.  
Ao abrir o relatório "Taxa de Componente Cirúrgico", será mostrado um botão "Comparativo", para que, após a abertura e estruturação dos campos do relatório, seja clicado para estender o relatório e mostrar os dados de comparativo de cirurgiões.  
Após chamar o comparativo, a disposição dos campos e colunas, ordenação ou filtro não poderão ser alterados, até que o botão seja acionado novamente, removendo os dados do comparativo.  
Foi feito assim para simplicidade dos cálculos, então, devera preparar o layout do relatório antes de clicar no botão comparativo. Caso necessita realizar outro filtro nas dimensões, faz-se necessário clicar no botão comparativo novamente.  
Quando o comparativo é chamado, duas novas colunas são adicionadas ao fato:  
Taxa IRIC:  
É a taxa IRIC informada para o procedimento cirúrgico de acordo com as condições em que a cirurgia foi realizada.  
Uma vez que não tenha informação da taxa de IRIC no cadastro de procedimento cirúrgico não será informado o calculo para o procedimento que não consta a informação da taxa.  
Infecções esperadas:  
São as infecções que seriam esperadas, se baseando na taxa IRIC e a quantidade de cirurgias realizadas.  
Fórmula de cálculo: Cirurgias \* Taxa IRIC  
E um painel de informações também é adicionado ao cubo.  
Tal painel contém as seguintes informações:  
Taxa padronizada:  
Fórmula de cálculo: Infecções observadas (reais) / Infecções esperadas  
Taxa ajustada:  
numerador = (Taxa padronizada / 100) - 0.01  
denominador = raiz((Taxa padronizada / 100) \* (1 - (Taxa padronizada / 100)) / Cirurgias realizadas)  
resultado = numerador / denominador  
Dedução da taxa ajustada:  
se a taxa ajustada for menor que 1.96, o número de infecções é MENOR OU IGUAL ao esperado.  
se não o número de infecções é MAIOR que o esperado.  
   
   
Observações  
A partir das dimensões disponíveis você obterá vários relatórios permitindo relacionar mais de uma dimensão.  
Ao gerar um período permite você retirar diversos relatórios deste mesmo período arrastando as dimensões para coluna ou linha conforme desejar dispor o relatório. Retira-se substituindo por outras e obtem-se vários relatórios sucessivos.   
Os filtros das dimensões são realizados clicando no filtro existente no cubo que ao clicar sob o mesmo abre-se uma relação disposta no cubo permitindo desmarcar todos e marca os que serão analisados.
