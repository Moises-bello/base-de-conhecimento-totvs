---
article_id: 360044829274
category: RH - Dissídio
content_hash: a7235205b1c87900514125a60b365119346c17cb92cb7628630baade2f0cb3b7
fetched_at: '2026-06-28T22:43:43.466426+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus -GPE - Como realizar importação de valores para cálculo
  de dissidio retroativo
type: support-article
updated_at: '2025-08-20T12:31:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044829274-RH-Linha-Protheus-GPE-Como-realizar-importa%C3%A7%C3%A3o-de-valores-para-c%C3%A1lculo-de-dissidio-retroativo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34313966321303) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Como realizar importação de valores para cálculo de dissidio retroativo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.25  
  
**Solução**Foi disponibilizado, a partir da versão 12.1.25, a possibilidade de informar verbas para o cálculo do dissídio retroativo. Após a atualização para a versão em questão, será criado um novo campo **Valor Informado** (RHH\_VALINF) para possibilitar o uso da melhoria.

Após efetuar o cálculo do dissídio geral, o recálculo poderá ser feito para cada funcionário individualmente, acessando o cálculo através do botão "Manutenção" que foi disponibilizado.

Na rotina de manutenção será possível informar o valor que será utilizado no cálculo no campo **Valor Informado**, para todas as verbas, exceto a **000**. Também será possível a inclusão de linhas com verbas que não tenham sido calculadas.

A rotina deve ser utilizada da seguinte forma:

Imaginemos que o valor original de uma verba qualquer seja de R$500,00 e o novo valor calculado seja de R$550,00, gerando uma diferença de R$50,00. Supondo que a diferença correta a ser paga fosse de R$100,00 e não foi calculada corretamente devido a, por exemplo, mudanças nas incidências das verbas, para que o cálculo seja feito será necessário os seguintes procedimentos:

* Incluir o valor R$600,00 no campo "Valor Informado" da verba, desta forma, a diferença entre o calculado e o original será de R$100,00 após o recálculo.
* Em "Ações Relacionadas" clicar em "Recálculo".
* A rotina irá carregar os parâmetros de cálculo de acordo com o funcionário e período abertos e irá exibir os dados para conferência, podendo, neste momento, efetuar qualquer alteração.
* Após confirmar, o cálculo é refeito, utilizando todas as verbas informadas no recálculo, alterando não só a verba efetivamente alterada, mas todas as demais que ela incidir (Impostos por exemplo).
* Após o recálculo a tela é recarregada já com os valores de diferenças corretos.

Para casos em que por ventura uma verba não deva ser paga, basta colocar no valor informado o mesmo valor calculado originalmente na folha, desta forma a diferença gerada será zero.

Outra possibilidade de informar valores é através de um arquivo do **tipo CSV**, delimitado por ponto e vírgula ";". O arquivo deverá conter a seguinte estrutura:

* Filial
* Matrícula
* Roteiro
* Período do cálculo original
* Semana do cálculo original
* Verba Original
* Valor Informado

 Exemplo

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10217284848919)

Cálculo do dissídio antes da importação do arquivo é exemplificado que os valores das verbas 001 e 179 na coluna de valor origem (box azul) e valor calculado (box verde) são os mesmos, pois como não há diferença a ser processada o valor a pagar (box laranja) fica zerado:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10217366106007)

Ao recalcular o dissídio importando o arquivo CSV, pode ser observado que as verbas 001 e 179 na coluna de valor calculado (box verde) assumem os valores importados pelo arquivo e a coluna de valor a pagar (box laranja) é preenchida de acordo com a diferença processada no cálculo entre valor origem e valor calculado:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10217544477079)

Foi criado uma nova pergunta (SX1) no grupo de perguntas referentes ao cálculo para que o arquivo .CSV possa ser selecionado.

Caso seja informado um arquivo, no momento do cálculo ele será lido, e todas as verbas ali informadas serão utilizadas, ignorando os valores originais calculados pelo sistema. Caso o período e semana da linha não estiver dentro do range selecionado para cálculo a linha será ignorada, da mesma forma as verbas que não existirem na SRV também serão.

**Importante:**

1. Caso uma verba já tenha sido editada individualmente, através da rotina de manutenção, e um novo cálculo geral for efetuado posteriormente, as verbas informadas serão mantidas. Para que as verbas informadas sejam apagadas e o cálculo seja feito com base nos valores calculados pelo sistema será necessário efetuar a exclusão prévia do cálculo.
2. Para quando existir duplicidade de verbas no arquivo de importação será assumido o valor do último lançamento encontrado no arquivo.

**Saiba mais:**

<https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio>
