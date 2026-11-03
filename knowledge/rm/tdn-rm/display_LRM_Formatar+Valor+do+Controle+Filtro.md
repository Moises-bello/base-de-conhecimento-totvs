---
content_hash: b9260881b5bb3b4b73752710ff6165a305e7b2038d6533c0fb709329407eca5f
fetched_at: '2026-06-29T00:10:24.972641+00:00'
page_id: '500295423'
product: rm
source: tdn-rm
title: Formatar Valor do Controle Filtro
type: documentation
url: https://tdn.totvs.com/display/LRM/Formatar+Valor+do+Controle+Filtro
version: 16
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       Esta página tem por objetivo demonstrar como formatar valores do controle ***Filtro*** inseridos nos relatórios.

# Introdução:

---

       Esta configuração atende aos usuários quanto a necessidade de se formatar o valor apresentados pelo controle Filtro.

false.Formatando o filtro

       Para exemplo, utilizaremos um relatório que fará uso da tabela de funcionários (PFUNC). Criado um filtro no relatório para data de admissão do funcionário.

       Para que o valor desse filtro seja visualizado no relatório inserimos o controle do tipo “Filtro”. Selecionado o controle e acessado as propriedades do controle teclando F4 (ou acessando o menu Exibição | Janelas | Grade de Propriedades)

       Nas propriedades do controle “Filtro” altere a propriedade “Filtro” para “Filtro do Relatório”. Em seguida altere a propriedade “Clausula” para o filtro que será impresso no relatório. Por último selecione na propriedade “Valor” a condição do filtro que será formatada.

       Feitos os ajustes na propriedade do controle a opção para formatação estará habilita nas propriedades do Controle e no menu de propriedades do controle.

       A formatação também será possível acessando o menu de propriedades do controle acessado através da smart tag do controle. Em seguida acesse a propriedades “Formato do texto” e atribua a formatação desejada.

Restriçãofalse

  A formatação do valor do filtro **estará disponível somente** quando a propriedade “**Valor**” for diferente de “**Ambos**”. Quando selecionado a opção “**Ambos**” na propriedade “**Valor**” o sistema irá bloquear essa formatação.

*Propriedade do Controle*

*Menu de Propriedades do Controle*

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.24 ou superiores

false

**Processo:** Formatar filtros

falsefalse

**Status:** Finalizado

false

**Data:** 10/07/2019

false

**Autores:**
