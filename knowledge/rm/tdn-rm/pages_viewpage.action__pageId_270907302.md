---
content_hash: 4bee83f05c179134f7f35e40b126ea7ba6cee67d78cd33b87fe9bbbc5ad725b6
fetched_at: '2026-06-29T00:08:24.843617+00:00'
page_id: '270907302'
product: rm
source: tdn-rm
title: RPT00009.3.1 - Sobreposição dos Componentes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270907302
version: 8
---

# Índice:

---

.\*ndice:

# Introdução:

---

       Utilizamos no **RM** um conjunto de componentes de uma empresa terceira chamada **"Devexpress"**, onde o **RM** Reports tem como base o **Xtrareports**, pertencente a esse conjunto de componentes.

A sobreposição de campos pode ocasionar falhas na apresentação do design do relatório. Essas falhas podem ocorrer **quando**?

* Exportação do Relatório para **HTML, RTF, XLS, XLSX**.
* Preview do Relatório .NET **Web**.

Observe na imagem abaixo, que os campos sobrepostos, são postos em vermelho. Uma mensagem é apresentada indicando quais os controles estão sobrepostos, e a possibilidade de falha ao exportar o relatório ou visualiza-lo web.

Existem diversas respostas do suporte da **Devexpress**, em vários intervalos de tempo diferentes, quem corroboram o explicado acima; Colocamos as respostas mais recentes que contemplam a versão **14.1** da **Devexpress**, apresentadas abaixo, traduzidas.

**TÓPICO GERAL : [Overlapped controls cause Export problems (Controles sobrepostos causam problemas na exportação)](https://www.devexpress.com/Support/Center/Question/Details/DB29502)**

falseTradução

**[...]**

Nos estamos cientes desse problema, e é assim que o processo de exportação para **HTML, RTF e XLS**, do componente **XtraReport**, funciona. A razão disso é que a funcionalidade exportação para  **HTML, RTF e XLS** é construida a partir do conceito de **"Leiaute Tabela (Table Layout)"** onde o posicionamento dos componentes **são relativos** uns aos outros. Entretanto, já recebemos uma grande quantidade de pedidos para que seja possível exportar para **HTML, RTF e XLS** onde os componentes tenham **posições absolutas**, ou seja, **possa ficar sobrepostas**. Caso queria acompanhar o pedido, esse é o link: [www.devexpress.com/issue=A2128](http://www.devexpress.com/issue=A2128).

**[...]**

No caso de uma imagem que serve como plano de fundo + componentes de texto sobrepostos a essa imagem, temos outras repostas do suporte da Devexpress:

**TÓPICO 1 : [Place other controls over xrPictureBox on XtraReport (Colocar outros controles sobre um componente Imagem no Relatório)](https://www.devexpress.com/Support/Center/Question/Details/Q323059)**

falseTradução

**[...]**

... limitações :

1) Não existe um funcionalidade que consiga esticar a imagem de acordo com o tamanho da página.

2) Um layout com controles sobrepostos podem não ser preservados quando exportados para alguns formatos **(ex: HTML)** - veja [Preview Html não é o mesmo do que os outros Preview (MDI) quando uma imagem é colocada.](https://www.devexpress.com/Support/Center/Question/Details/B142037)

Eu recomendo que você use uma [Marca d'agua](http://documentation.devexpress.com/#CoreLibraries/clsDevExpressXtraPrintingDrawingWatermarktopic) ao invés da Imagem **[Funcionalidade disponível somente em versões superiores a versão 14.1 da devexpress (14.2.3 ou superiores) ainda não utilizada na biblioteca RM]**.

**[...]**

OBSERVACAO

Caso queria saber melhor sobre Marca d'agua e as limitações de seu uso, veja .

**TÓPICO 2 : [Html Preview is not the same as other Preview when a Picture element is placed (Preview Html não é o mesmo do que os outros Preview (MDI) quando uma imagem é colocada.)](https://www.devexpress.com/Support/Center/Question/Details/B142037)**

falseTradução

**[...]**

Esse comportamento é causado pela interseção dos controles. Você irá entender se você perceber que existem alertas vermelhos quando os controles estão sobrepostos.

**[...]**

**[...]**

Se você for capaz de criar seu relatório com um leiaute onde os controles não se sobreponham, o relatório não sofrerá alterações quando exportado para Excel, HTML e MHT ou vistos via preview HTML Peço que veja o topico [Overlapped controls cause Export problems](https://www.devexpress.com/Support/Center/p/DB29502.aspx) para melhores explicações sobre o assunto.

**[...]**

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Sobreposição dos Componentes

falsefalse

**Status:** Finalizado

false

**Data:** 10/10/2017

false

**Autores:**
