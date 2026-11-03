---
content_hash: df2b9d6324653f986011760ba530f3823a78a7f59d64037dc59e90d8284d6a6c
fetched_at: '2026-06-29T00:09:11.405978+00:00'
page_id: '403746948'
product: rm
source: tdn-rm
title: Fórmula Visual - RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=403746948
version: 10
---

# Índice

---

# Fórmula Visual - Linha RM

---

        A Fórmula Visual da linha RM é um recurso de funcionamento extenso e que busca o desenvolvimento visual de lógicas de negócio com o objetivo de estender as soluções TOTVS RM. Como finalidade inicial, possibilita pequenas customizações nos produtos, permitindo criar regras específicas em determinados cadastros/processos dentro da empresa, automatizando e/ou validando dados, permitindo assim a entrada de informações/resultados mais consistentes.  
Usa como base o Microsoft Framework .NET - Windows Workflow Foundation, um produto muito robusto e poderoso desde seu entendimento, onde é aplicado nos principais softwares da própria Microsoft.

**Este é o funcionamento normal RM:**  
  
**Este é o funcionamento RM com customização através de Fórmula Visual:**

# Permissão de Acesso Fórmula Visual

---

 Perfil de usuário que não possui permissão para **editar** a fórmula visual:

Ao dar dois cliques na fórmula visual será aberto o formulário ao invés da edição:

Perfil de usuário que não possui permissão para **executar** a fórmula visual:

Os botões "**Salvar e Executar**" e "**Salvar e Agendar Execução**" ficaram desabilitados:

# Montagem da Fórmula

---

         As fórmulas visuais podem ser acessadas de qualquer módulo pelo caminho: Módulo > Gestão > Fórmulas Visuais.

        Para a montagem de uma fórmula visual é necessário possuir bem definido o escopo das atividades que deverão compor a fórmula visual, assim como, os dados que deverão ser verificados/atualizados conforme necessidade. As fórmulas visuais são montadas graficamente com a ajuda de um designer (editor visual de programas), mostrando como ficará a seqüência de atividades a executar.

        O fluxo da fórmula visual pode ser disparado através do menu de processos, executando-o imediatamente, por meio de agendamento ou através de um evento (gatilho) que dispara a execução da Fórmula Visual.   
Segue abaixo a relação de alguns eventos que podem iniciar a execução da Fórmula Visual:

* antes de ler dados
* após ler dados
* antes de salvar dados
* após salvar dados

Para a criação de uma fórmula visual é necessário entender os cadastros de "Categoria", "Atividades" e "Gatilhos". Vejamos abaixo:

# Cadastro da Categoria

---

         Podemos denominar o cadastro de categoria como sendo um agrupador de perfis de segurança dos aplicativos RM, ou seja, para que uma determinada fórmula visual seja acionada ou exibida em processos de determinado cadastro, é necessário criar uma categoria e vincular os perfis de segurança que acionarão a fórmula visual em questão.

# Cadastro da Atividade

---

         A "Atividade" é conceituada como um dos passos da fórmula visual, sendo arranjadas logicamente como blocos sobrepostos. Dessa forma associamos duas ou mais atividades para formar uma Fórmula Visual com um propósito definido.

        As atividades possuem como finalidade apresentar de uma forma mais "amigável" as atividades desenvolvidas tanto pela TOTVS como pelo próprio cliente. Todas as atividades básicas necessárias para serem utilizadas na montagem de fórmulas visuais estão disponíveis na "Galeria de Atividades", entretanto, novas atividades podem ser criadas pelo próprio cliente através de programação em linguagem .NET e utilização da Framework RM.

# Cadastro dos Gatilhos

---

         A janela de gatilhos da Fórmula Visual permite definir em que ação do sistema e em qual cadastro/processo será disparada a fórmula visual em questão, podendo informar para uma mesma fórmula visual diversas ações e cadastros/processos diferentes. Além disso, é possível parametrizar se as exceções definidas na fórmula visual serão acionadas ou não, ou determinar algum gatilho como inativo.

        A escolha do gatilho correto é muito importante já que algumas atividades dependem direto dos dados que serão consultados no momento da execução. Pra incluir um gatilho, selecione um evento, clique no ícone de inclusão na barra superior da tela e na tela de procura apresentada, insira o nome da tela para localizar.

        Para tratar erros encontrados no Gatilho, clique na caixa de comando na coluna Tipo referente ao Gatilho inserido e escolha uma das opções:

* ***Desativado:*** O Gatilho não será considerado, logo não será executado a Fórmula Visual.
* ***Ativado com Exceções:*** Será executada a fórmula visual no gatilho selecionado, e se ocorrer erro será exibido para o usuário e a Fórmula Visual será interrompida.
* ***Ativado Ignorando Exceções:*** Será executada a fórmula visual no gatilho selecionado, e se ocorrer exceção, não será exibida para o usuário e a fórmula visual continuará a execução normalmente.*Ativado Ignorando Exceções:* Será executada a fórmula visual no gatilho selecionado, e se ocorrer exceção, não será exibida para o usuário e a fórmula visual continuará a execução normalmente.

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Fórmula Visual - Linha RM

falsefalse

**Status:** Finalizado

false

**Data:** 26/11/2018

false

**Autores:**
