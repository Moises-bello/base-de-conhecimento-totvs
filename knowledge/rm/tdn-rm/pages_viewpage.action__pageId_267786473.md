---
content_hash: 8ee37479c638017b808ec214c3122b85fddac5fe03a5baf3ceeced0e8d55b047
fetched_at: '2026-06-29T00:08:19.447595+00:00'
page_id: '267786473'
product: rm
source: tdn-rm
title: RPT00038.1.1 - Alteração de valor de propriedade utilizando a tecla TAB
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267786473
version: 13
---

# Índice:

---

.\*ndice:

# Introdução:

---

      O objetivo deste documento é mostrar como fazer a alteração dos valores de propriedades dos componentes do Reports utilizando a tecla TAB para mover o cursor a próxima propriedade.

# Passo a passo:

---

   Utilizamos no **RM** um conjunto de componentes de uma empresa terceira chamada **"Devexpress"**, onde o **RM** Reports tem como base o **Xtrareports**, pertencente a esse conjunto de componentes.

Na versão **14.1**, a qual utilizamos atualmente, existe uma **não-conformidade** na grade de propriedades, que ocorre quando **alteramos o valor** de uma determinada propriedade e **pressionamos a tecla TAB** para mover o cursor para a próxima propriedade, disparando uma exceção dentro dos componentes da **Devexpress**, levantando a exceção exibida na imagem abaixo.

1Alteração Propriedade Usando TAB

****TÓPICO PRINCIPAL: [Null Reference Exception Tab after value changed in XtraReport (Exceção de Referência Nula após trocar valor no componente XtraReports)](https://www.devexpress.com/Support/Center/Question/Details/T228477)****

falseTradução

**[...]**

**Usuário1**: Eu tenho um erro quando eu pressiono TAB ao trocar de valor no XtraReport (Relatório .Net).

**[...]**

**[...]**

Nos fomos alertados desse problema e já foi solucionado. Peço que atualize seus controles. A versão onde o problema foi solucionado está descrito em: [NullReferenceException in PropertyGrid FormattingRules after the Tab key is pressed](https://www.devexpress.com/Support/Center/p/T211642.aspx)

**[...]**

OBSERVAÇÃO

A inconsistência está documentada no fórum de suporte da **Devexpress** e já foi solucionada na versão **15**. A migração do **RM** para a versão **15** da **Devexpress** está em **RoadMap** e assim que for realizada, os clientes serão notificados através dos release notes. Estamos na versão **14.(1.11)**, portanto ****a solução ainda não se encontra disponível.****

****TÓPICO SOLUÇÃO 15.1: [NullReferenceException in PropertyGrid FormattingRules after the Tab key is pressed (Exceção de Referência Nula na grade de Propriedades 'Regras de Formatação' após a tecla TAB ser pressionada)](https://www.devexpress.com/Support/Center/Question/Details/T211642)****

falseTradução

**[...]**

**Implementado:**

* + **v2015 vol 1.3**
  + **v2014 vol 2.6**

**[...]**

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Valor de propriedade usando TAB

falsefalse

**Status:** Finalizado

false

**Data:** 10/10/2017

false

**Autores:**
