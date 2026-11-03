---
content_hash: 7bbcdf535444e0a99d780415025b1a9682f88e99db3ddf7825bff2e033b7babf
fetched_at: '2026-06-29T00:08:57.762942+00:00'
page_id: '354474788'
product: rm
source: tdn-rm
title: Análise de Performance Visual Studio (Alternativo ao Yourkit)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=354474788
version: 5
---

# Análise de Performance Visual Studio (Alternativo ao Yourkit)

# Objetivo

Este documento tem por objetivo mostrar a utilização do Performance Profiler do Visual Studio para analisar performance da aplicação. Tal procedimento é um alternativo ao Yourkit.

# Passos

Primeiramente é necessário abrir a *solution*do produto.

Após abrir a *solution* acessar o menu **Analyse | Performance Profiler...**

Será aberta uma nova aba, a partir dela acessar **Change Target | Executable.**Feito isso clique em **Start.**

 

Selecione a opção **Instrumentation** e clique em **Next**. Após isso será exibido os projetos da aplicação, deixe selecionado **One or more avaliable projects** e clique em **Next**.

 

Agora informe o caminho do que quer analisar RM.exe ou RM.Host.exe no campo **Executable path** e clique em **Next.**Deixe marcado o item****Lanch profiling after the wizard finishes**** e clique em **Finish**.

Feito isso, a solution será compilada e após isso o profiler irá iniciar o **exe**que selecionou para executar, no nosso caso foi o **RM.Host.exe.**

Após ele iniciar será necessário executar o **RM.exe**e executar o processo que deseja avaliar a performance.

 

Após executar o processo que deseja avaliar, clique em **Stop profiling.** Após parar o profiler será aberta a tela do diagnóstico conforme abaixo.

Para verificar as chamadas que foram feitas clique na caixa de seleção **Current View | Call Tree**.

É apresentada algumas colunas por padrão, sendo as mais relevantes as mencionadas abaixo:

* **Number of Calls**
  + Número de chamadas da função.
* **Elapsed Inclusive Time (%)**
  + Tempo total gasto na execução de uma função e suas funções filhas.
* **Elapsd Exclusive Time (%)**
  + Tempo total gasto na execução de uma função e excluindo as funções filhas.

Entretanto é possível incluir as colunas **Elapsed Inclusive Time (%)** e **Elapsd Exclusive Time (%)** em milissegundos para uma melhor análise. Para isso bastar clicar com botão direito em cima das colunas e ir em **Add/Remove Columns** e selecione conforme abaixo as colunas **Elapsed Inclusive Time**e **Elapsed Exclusive Time** e clique em **OK.**

 

Feito isso a visão ficará da seguinte forma:

A partir daí é abrir a árvore e efetuar a análise.

# Exemplo

Segue a seguinte árvore que salva o log em uma tabela, onde é gerado o autoinc pelo método GetIdLogNota().

Fazendo análise é verificado que foi executado 9 vezes e gastou o tempo total de 610,04 milissegundos.
