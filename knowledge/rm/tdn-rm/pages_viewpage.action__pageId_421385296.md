---
content_hash: 5b64013206b4a2f6d3db4c16449be9739f61338219290f526ae50883b14ee743
fetched_at: '2026-06-29T00:09:14.890627+00:00'
page_id: '421385296'
product: rm
source: tdn-rm
title: Utilizando a Equalização de Insumos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385296
version: 2
---

---

Na tela de Cadastro de Insumo, existe o anexo de Equalização de Insumos.  
 Para Visualizar basta clicar em Anexos e em seguida Equalização de Insumos.  
 Em seguida será possível visualizar na aba de Anexos, a Equalização referente ao Insumo selecionado.

Os campos informados são:

* **Total Teórico:** É o total de horas no Período. Calculado com base no cronograma físico da Planilha de Atividades e o uso do Insumo nas Tarefas do Projeto, proveniente dos índices das composições e suas respectivas quantidades. Partindo da premissa de que nem o índice da composição, nem a quantidade e nem o período de execução de determinado serviço foram alterados, temos que a quantidade de horas para aquele insumo, naquele período é fixa, o que irá variar é se essas horas serão Normais ou Extras.
* **Efetivo Calculado:** É o total do recurso alocado necessário para o período. Este cálculo deve buscar manter estável o número de recursos alocados, ou seja, que o Efetivo Calculado seja o mais próximo entre os períodos, quando os limites de horas extras máximas e mínimas forem definidos. Quando os limites não forem definidos, o calculo do Efetivo Calculado será direto, ou seja, quantidade de horas do período dividido pela jornada do período. Para isto o cálculo irá identificar o período com maior demanda e calculá-lo alocando maior quantidade de horas extras possíveis, ou seja, o menor efetivo.  Os demais períodos devem ser alocados buscando o Efetivo Calculado com valo próximo ao primeiro período calculado.
* **H. E. Calculada %:** É o percentual total de hora extra no período. É calculado da seguinte maneira: = (Total Teórico – (Jornada **(Efetivo Calculado)))/(Jornada**(Efetivo Calculado)
* **Custo Calculado $:** É o custo levando em consideração o Total Teórico, Custo do Insumo e Hora Extra. É calculado da seguinte maneira: = Total Teórico \* Custo do Insumo + Número de HE \* (Custo de Hora Extra - Custo de Hora Normal)
* **Efetivo Adotado:** É o campo onde pode o usuário poderá editar o Efetivo Calculado. Este campo, inicialmente será preenchido com valor do Efetivo Calculado.
* **Hora Extra Adotada %:** É um campo calculado em função do número de horas restantes, dado o Efetivo Adotado. É calculado da seguinte maneira: =(Total Teórico – (Efetivo Adotado \* Jornada))/(Efetivo Adotado \* Jornada)
* **Custo Adotado $:** É o custo levando em consideração o Efetivo Adotado, Jornada, Custo do Insumo e Hora Extra Adotada. É calculado da seguinte maneira: =Efetivo Adotado \* Jornada \* Custo do Insumo + Numero de Hora Extra Adotado \* Custo de Hora Normal + Número de Hora Extra Adotado \* (Custo de Hora Extra - Custo de Hora Normal)

**Obervação:**

Caso a Hora Extra seja negativa, não considerar para o calculo do Custo adotado.  
 Na Equalização há a possibilidade de exportar os dados visíveis na tela para Excel, PDF ou a Impressão direta. Basta selecionar o Insumo desejado, em seguida, na tela de anexo, clicar no botão "Exportar visão para arquivo no formato CSV.", e selecionar uma das opções disponíveis.
