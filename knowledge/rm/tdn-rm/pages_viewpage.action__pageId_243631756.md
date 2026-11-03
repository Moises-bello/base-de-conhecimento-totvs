---
content_hash: 2714501fe3850611fd8198d19b64b17840c73b7e75513e55c95a2c0d9295b321
fetched_at: '2026-06-29T00:08:11.958361+00:00'
page_id: '243631756'
product: rm
source: tdn-rm
title: RPT00014.1.1 - Propriedade Ângulo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243631756
version: 11
---

# Índice:

---

.\*ndice:

# Introdução:

---

       Utilizamos no **RM** um conjunto de componentes de uma empresa terceira chamada **"Devexpress"**, onde o **RM** Reports tem como base o **Xtrareports**, pertencente a esse conjunto de componentes.

]]>

A funcionalidade de **ângulo (propriedade)** do componente **Label (XRLabel)** não é suportado pelo **HTML (Relatório Web)** como reportado pelo próprio suporte da **Devexpress**.

]]>

Tanto a versão **10.1** dos componentes **Devexpress** utilizada na versão **11.8x** do **RM**, quanto a versão **14.1** dos componentes da **Devexpress** utilizada na versão **12.1.x** do **RM**, essa propriedade não é suportada pelo **HTML**.

Existem diversas respostas do suporte da **Devexpress**, em vários intervalos de tempo diferentes, porém colocamos a resposta mais recente que contempla a versão **14.1** da **Devexpress**, apresentada abaixo, traduzida.

**TÓPICO PRINCIPAL: [XtraReport viewer angle issue (Problema com ângulo no Visualizador do XtraReport)](https://www.devexpress.com/Support/Center/Question/Details/T145206)**

falseTradução

**[...]**

Por favor, observe que a especificação do HTML não suporta "orientação de texto", e é impossivel obter esse efeito via código HTML. Até o momento, a propriedade XRLabel.Angle não é efetiva ao visualizar/exportar um relatório no formato HTML.  
Referência a esse mesmo tópico em nossa Database: [<https://www.devexpress.com/Support/Center/Question/Details/DQ48000>] para uma solução de contorno da situação.

**[...]**

**TÓPICO SECUNDÁRIO:** **[Vertical text in html (Texto Vertical em HTML)](https://www.devexpress.com/Support/Center/Question/Details/DQ48000)**

falseTradução

**[...]**

O problema a que você se refere não é um problema de implementação do conjunto de componentes Xtrareport.  
O HTML Padrão não suporta "orientação de texto" e é impossível criar textos orientados verticalmente.  
Como uma solução de contorno você pode criar imagens com texto ao invés de cabeçalhos de página com textos orientados verticalmente.

**[...]**

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Propriedade ângulo

falsefalse

**Status:** Finalizado

false

**Data:** 10/10/2017

false

**Autores:**
