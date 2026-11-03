---
content_hash: 0ee5b1252e211b041b4134a725809204b0e8e51b08e96f528342f62be8f8f153
fetched_at: '2026-06-29T00:08:16.383110+00:00'
page_id: '244940460'
product: rm
source: tdn-rm
title: RPT00009.1.2 - Múltiplas Colunas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244940460
version: 34
---

# Índice:

---

.\*ndice:

# Passo a passo:

---

       Utilizamos no **RM** um conjunto de componentes de uma empresa terceira chamada **"Devexpress"**, onde o **RM** Reports tem como base o **Xtrareports**, pertencente a esse conjunto de componentes.

]]>

Na versão **14.1**, a qual utilizamos atualmente, a funcionalidade **Multi-Column (Múltiplas Colunas)** utilizada em conjunto com a funcionalidade **quebra de página** só funciona quando a propriedade **Layout** é **[Primeiro Cruzado, Então Descida],** quando o valor é **[Primeiro Descida, Então Cruzado]** a quebra não é realizada.

]]>OBSERVAÇÃO

A partir da versão **15.1** dos componentes **Devexpress****,** a funcionalidade **Multi-Column** juntamente com a funcionalidade **quebra de página** funcionam independente do valor escolhido para a propriedade **Layout.** Portanto, **a solução** para essa limitação **está disponível apenas** na versão **15.1 (ou superiores)** da **Devexpress,** como estamos na versão **14.1**, **a solução ainda não se encontra disponível.**

****TÓPICO SOLUÇÃO 15.1: [Page Builder - Múltiplas Colunas - Adicionar a funcionalidade de começar uma nova coluna (no caso de Direção igual a Primeiro Descida, Então Cruzado)](https://www.devexpress.com/Support/Center/Question/Details/Q322274)****

falseTradução

**[...]**

**Implementado:**

* **v2015 vol 1.3**

**Informações adicionais:**

Use a **Propriedade** do Detalhe **Quebra de Página** ou um **controle XRPageBreak** para iniciar uma nova coluna quando a propriedade **Layout** for **[Primeiro Descida, Então Cruzado]**.

**[...]**

Existem diversas respostas do suporte da **Devexpress**, em vários intervalos de tempo diferentes, porém colocamos as respostas mais recentes que contemplam a versão **14.1** da **Devexpress**, apresentadas abaixo, traduzidas.

**TÓPICO 1 : [Page breaks do not work in multi-column detail band (Quebra de Página não funciona em uma banda detalhe com múltiplas linhas)](https://www.devexpress.com/Support/Center/Question/Details/B141061)**

falseTradução

**[...]**

No momento, o XtraReports **não suporta** quebra de página quando criamos um relatório com múltiplas colunas com a direção de coluna **[Primeiro Descida, Então Cruzado]**. Estamos cientes dessa limitação.

**[...]**

**TÓPICO 2 : [XtraReports Page Breaking MultiColumns with Groups (Relatório com Múltiplas Colunas e Quebra de Página)](https://www.devexpress.com/Support/Center/Question/Details/Q489012)**

falseTradução

**[...]**

No momento, **Não existe funcionalidade** que force a quebra de página entre colunas no Modo [Primeiro Descida, Então Cruzado], veja ([Page Builder - Múltiplas Colunas - Adicionar a funcionalidade de começar uma nova coluna (no caso de Direção igual a Primeiro Descida, Então Cruzado)](https://www.devexpress.com/Support/Center/p/AS6131.aspx)). Como uma solução imediata, use o modo **[Primeiro Cruzado, Então Descida]**.

**[...]**

****TÓPICO 3 : [Column break in multi-column mode (Quebra de página em modo múltiplas colunas)](https://www.devexpress.com/Support/Center/Question/Details/Q322274)****

falseTradução

**[...]**

Você conseguirá o resultado esperado utilizando a propriedade [Layout](http://documentation.devexpress.com/#XtraReports/DevExpressXtraReportsUIMultiColumn_Layouttopic) com o valor [[Primeiro Cruzado, Então Descida]](http://documentation.devexpress.com/#CoreLibraries/DevExpressXtraPrintingColumnLayoutEnumtopic). Para informações adicionais acesse o artigo [Relatório Múltipla Coluna](http://documentation.devexpress.com/#XtraReports/CustomDocument2601).

**[...]**

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Múltiplas Colunas

falsefalse

**Status:** Finalizado

false

**Data:** 10/10/2017

false

**Autores:**
