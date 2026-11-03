---
content_hash: e6ea9bb31b9c84a90c29ac3c6af1a30d169556d7166455c951286a34569fb31f
fetched_at: '2026-06-29T00:08:26.198929+00:00'
page_id: '271165491'
product: rm
source: tdn-rm
title: RPT00024.2.1 - Limitação de Design
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271165491
version: 59
---

# Índice:

---

.\*ndice:

# 1 - Introdução

---

Utilizamos no **RM** um conjunto de componentes de uma empresa terceira chamada **"Devexpress"**, onde o **RM** Reports tem como base o **Xtrareports**, pertencente a esse conjunto de componentes.

Alguns problemas relacionados ao design do texto rico **(XtraRichText)**, já são conhecidos e já foram reportados ao suporte da **Devexpress**.

Tanto a versão **10.1** dos componentes **Devexpress** utilizada na versão **11.8x** do **RM**, quanto a versão **14.1** dos componentes da **Devexpress** utilizada na versão **12.1.x** do **RM**, essas inconsistências existem.

Existem diversas respostas do suporte da **Devexpress**, que indicam a existência dessas inconsistências, o conhecimento por parte deles, das mesmas, e a busca pela solução, que ainda não foi realizada.

# 2 - Limitações de Design

---

Serão apresentadas nesse documento algumas inconsistências que podem ocorrer, ao se utilizar o componente de **Texto Rico (XtraRichText)**.

OBSERVACAO

Todas as inconsistências informadas aqui, podem (ou não) ser solucionadas através de mudanças no relatório.

Na maioria das vezes, ao realizar algumas mudanças, como:

* **Diminuir (ou aumentar) o comprimento do componente;**
* **Diminuir (ou aumentar) a largura do componente;**
* **Remover e reinserir o componente;**
* **Remover e reinserir o conteúdo do componente;**
* **Refazer a ligação de dados do componente;**
* **Dividir o componente de Texto Rico em dois ou mais Textos Ricos.**

O componente passa a ser gerado corretamente.

# 2.1 - Texto Cortado

---

O primeiro caso que vamos tratar é quando o conteúdo do texto rico é cortado.

OBSERVACAO

A inconsistência acontece na exportação para **RTF** e **HTML**.

As imagens acima mostram que os componentes de texto rico foram cortados na geração do Relatório.

Existem diversas respostas do suporte da **Devexpress,** que indicam a **existência** dessa **inconsistência** e a **impossibilidade de solução** a **curto prazo**, em vários intervalos de tempo diferentes, porém colocamos as respostas mais recentes que contemplam a versão **14.1** da **Devexpress**, apresentada abaixo, traduzidas.

**TÓPICO 1: [Text is truncated when it is exported to RTF (Texto é cortado quando exportado para RTF)](https://www.devexpress.com/Support/Center/Question/Details/Q355556)**

falseTradução

**[...]**

[GDI e GDI+](#). Por favor, acompanhe o tópico **[Grid Export HTML Error - Group Columns not visible](https://www.devexpress.com/Support/Center/Question/Details/B50289)** para mais informações. Nesse cenário, eu posso apenas sugerir que você acompanhe também, as seguintes sugestões:

**Mais Informações sobre GDI e GDI+**  
  
•  [Graphics Device Interface](https://en.wikipedia.org/wiki/Graphics_Device_Interface)  
•  [Rendering Methods Comparison Or GDI Vs GDI+](https://theartofdev.com/2014/04/21/text-rendering-methods-comparison-or-gdi-vs-gdi-revised/)  
•  [Interoperability Between GDI and GDI+](https://support.microsoft.com/en-us/help/311221/info-interoperability-between-gdi-and-gdi)  
•  [GDI Vs GDI+ Text Rendering Performance](https://blogs.msdn.microsoft.com/cjacks/2006/05/19/gdi-vs-gdi-text-rendering-performance/)

]]>

[**Drawing - Rewrite the printing engine with GDI methods instead of GDI plus methods**](https://www.devexpress.com/Support/Center/p/AS3119.aspx)**[Measurement - Improve the accuracy of storing values that are measured in report units (e.g. sizes and locations) to achieve more exact positioning of report controls when printing or exporting](https://www.devexpress.com/Support/Center/p/S31584.aspx)**

Nos desculpe pela possível inconveniência.

**[...]**

**TÓPICO 2:** **[XRRichText HTML Export - text gets truncated at the end (Exportação Texto Rico para HTML - Texto Rico é cortado ao final)](https://www.devexpress.com/Support/Center/Question/Details/T100721)**

falseTradução

**[...]**

Esse comportamento é causado por limitações do mecanismo de exportação do Texto Rico. O tamanho do conteúdo do Texto Rico pode se diferenciar da representação HTML. Nós já discutimos sobre essa limitação antes. por exemplo, reveja o seguinte tópico:

**[Export to Html truncates text at end](https://www.devexpress.com/Support/Center/p/Q425951.aspx)**

Espero que essa informação lhe seja útil.

**[...]**

# 2.2 - Texto em Pequenos Blocos

---

O segundo caso que vamos tratar é quando o conteúdo do texto rico é representado como pequenos blocos, em vez de um bloco único, onde se pode editar todo o paragrafo.

Observe na imagem acima que, o texto rico foi exportado como um bloco único, onde todo o conteúdo pode ser editado normalmente.

Observe na imagem acima que, em vez de um bloco único, onde todo o conteúdo pode ser editado, o texto foi exportado como pequenos blocos editáveis.

Existem diversas respostas do suporte da **Devexpress,** que indicam a **existência** dessa **inconsistência** e a **impossibilidade de solução** a **curto prazo**, em vários intervalos de tempo diferentes, porém colocamos as respostas mais recentes que contemplam a versão **14.1** da **Devexpress**, apresentada abaixo, traduzidas.

**TÓPICO 1:** **[XRRichText - Multiple frames are created when exporting to RTF (Texto Rico - Múltiplos blocos são criados quando se exporta para RTF)](https://www.devexpress.com/Support/Center/Question/Details/B205817)**

falseTradução

**[...]**

```
Nós agradecemos por sua paciência. Nós examinamos esse problema e chegamos a conclusão que o comportamento atual é devido ao design.  
 
```

RTF entre páginas no modo **[WYSIWYG](#)**. Por isso, a primeira página é desenhada como **um bloco único** e as próximas páginas com o conteúdo **RTF** é desenhado como múltiplos blocos na página **(um bloco por palavra)**.

**Mais Informações WYSIWYG**  
  
•  [O que é WYSIWYG?](https://www.tecmundo.com.br/institucional/2057-o-que-e-wysiwyg-.htm)  
•  [WYSIWYG (Wiki)](https://pt.wikipedia.org/wiki/WYSIWYG)

]]>

Sinto dizer que nós não podemos consertar esse problema sem refazer por inteiro a estrutura interna atual do nosso componente. Peço que aceite nossas desculpas pela inconveniência.

**[...]**

**TÓPICO 2:** **[Export a report to RTF (Page by Page) productes weird result (Exportar um Relatório para RTF (Página por Página) produz um resultado estranho)](https://www.devexpress.com/Support/Center/Question/Details/T164647)**

falseTradução

**[...]**  
Esse comportamento é do design. Quando o **XRRichText (Texto Rico)** é impresso/exportado ele gera blocos separados para cada palavra para que o conteúdo **RTF** seja apresentado corretamente em todos os formatos. Desde que blocos separados são usados, nosso motor de **exportação para RTF** cria um painel que envolve cada bloco.  
  
Sinto dizer que não há maneira de mudar esse comportamento na versão atual dos nossos controles.  
**[...]**

# 2.3 - Texto dentro de uma tabela

---

O terceiro caso é quando se usa uma tabela dentro do Texto Rico, ou algum outro tipo de objeto que agrupa um texto, inserido dentro do Texto Rico.

Veja o exemplo na imagem abaixo:

Neste caso o objeto selecionado com linhas vermelhas é o Texto Rico e dentro dele existe outro objeto selecionado com linhas cinzas.

Como relatado acima nos casos anteriores, este objeto pode ser ignorado pela **Devexpress** nas versões mais novas, devido a limitação de design e pode gerar um comportamento inconsistente.

O texto dentro deste objeto pode ficar cortado e não realizar a quebra de página, ou seja, a limitação de design da **Devexpress** pode fazer com que o layout não fique de acordo com o esperado.

### Solução para este caso específico:

Para este caso pode ser possível contornar o problema de quebra de página fazendo a seguinte alteração no layout.

1. Copie todo o conteúdo de texto deste objeto.  
   1. Isso pode ser feito clicando duas vezes sobre ele e depois pressionando as teclas Ctrl + A
   2. Clique novamente sobre ele com o botão direito e selecione Copiar.
2. Selecione este objeto e exclua.
   1. Tente clicar na borda e depois pressione a tecla Del.
   2. Ou remova todo o texto e depois apague o objeto.
3. No Word (versão 2013 ou superior) ou usando o Google Docs
   1. Insira uma tabela e cole o texto(copiado anteriormente) dentro desta tabela.
   2. Selecione toda a tabela e depois selecione copiar.
4. Volte para o layout do relatório e copie a tabela dentro do Texto Rico.

Este procedimento pode resolver o problema de cortar o texto e fazer a quebra da página.

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Limitação de Design

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
