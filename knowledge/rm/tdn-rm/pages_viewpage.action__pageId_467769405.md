---
content_hash: 8b3c59a342b18fafa5e0810e4bf74479e0127225c821d3b0d10d9dab58fab36b
fetched_at: '2026-06-29T00:10:16.018692+00:00'
page_id: '467769405'
product: rm
source: tdn-rm
title: Executar relatórios sempre via Job Server
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=467769405
version: 7
---

# Índice

---

* [Objetivo](http://tdn.totvs.com/pages/viewpage.action?pageId=467769405)
* [Introdução](http://tdn.totvs.com/pages/viewpage.action?pageId=467769405)
* [Demonstração](http://tdn.totvs.com/pages/viewpage.action?pageId=467769405)

# Objetivo

---

        Esta página tem a finalidade de relatar a forma de uso dos parâmetros globais de performance "Executar relatórios sempre via Job Server" e "NÃO executar relatórios em processos isolados (Job Runner)".

# Introdução

---

       Esses dois parâmetros foram criados para melhorar a performance e consumo de recurso de ambientes distribuídos (N camadas). Estes parâmetros permitem manipular a forma de executar qualquer relatório do sistema, inclusive os relatórios que são gerados em cadastros, telas e visões.  
      A execução dos relatórios via Job Server trazem uma série de benefícios para a aplicação, pois deixam de concorrer com a navegação e utilização do sistema no geral.  
      O parâmetro quando marcado envia os relatórios de tela, que por padrão são executados no servidor de aplicação, para o Job Server, porem não seguem o mesmo padrão de enfileiramento, para não causar uma sensação de perda de performance para os usuários.

# Demonstração

---

Os parâmetros podem ser acessados em Ambiente → Parâmetros → Parâmetros Globais → Guia Performance.

* Executar relatórios sempre via Job Server → Este parâmetro indica que qualquer relatório do sistema será executado no servidor de Job, logo terá registro de execução como qualquer outro processo do sistema.
* NÃO executar relatórios em processos isolados (Job Runner) → Este parâmetro indica que os relatórios que executam via Job Server não mais executarão via processo isolado, o Job Runner. Este parâmetro deve ser usado somente em caos extremos onde, por algum motivo, os relatórios estão mais lentos ao serem executados via Job Server, pois quando não isolados outros problemas como vazamento de memória e queda de Host podem acontecer.

OBS.: A alteração destes parâmetros só será refletida após 5 minutos.

Com essa opção marcada, não será mais possível visualizar o andamento real da execução do relatório (através do recurso de barra de progresso mostrado na tela).  Alguns relatórios dos produtos fazem uso desse recurso para mostrar para o usuário o andamento real da execução, porém, como nesses caso os relatórios serão executados em máquinas JobServer,  de forma assíncrona, não será mais possível capturar essa informação e mostrar na tela para o usuario. As propriedades de configuração desses recursos são: CallBackExecutionProgress e CallBackMessageExecution

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Parâmetros Globais

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**

**[Lorena Roberta de Paiva Braga](http://tdn.totvs.com/download/attachments/364922926/CONTATOS_V2.csv.txt?version=1&modificationDate=1527604640000&api=v2)**
