---
content_hash: 008779cac3e16416123451d063d6e7bb23da53daaaf9ce7f45fdf61efef03da4
fetched_at: '2026-06-29T00:10:47.402812+00:00'
page_id: '556886967'
product: rm
source: tdn-rm
title: Integração Automação de Testes Jira x Testflow
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=556886967
version: 14
---

# **1) Introdução**

---

Este documento é um passo a passo para a atuação do TOTVER nas tarefas relacionadas a automação de testes na ferramenta Jira.

# **2) Subtasks do Jira**

---

As subtasks serão usadas no desenvolvimento de automações em issues de manutenção e no desenvolvimento de automações em issues de inovação.

* Para automações que envolvem a ferramenta Testflow, devemos utilizar obrigatoriamente a subtask do tipo "**Teste Automatizado**";
* Para automações que envolvem teste unitário, a subtask obrigatória que deverá ser utilizada é a do tipo "**Teste Unitário Automatizado**"

# **3) Criação de evidências**

---

Dentro de cada subtask, antes de sua conclusão é obrigatório anexar uma evidência de teste automatizado que pode ser;

* Print do cenário automatizado. Exemplo: Log com sucesso do Testflow, detalhe do projeto de teste, etc;
* Vídeo do Cenário automatizado. Exemplo: O vídeo grava a execução da automação e o resultado do projeto executando com sucesso no Testflow;
* Documento (.doc, .pdf, etc) do cenário automatizado. Exemplo: Word detalhando os cenários automatizados.

# **4) Links e rastreabilidade (Jira x Testflow x Jira)**

---

Visando atender auditorias, além das evidências de teste, devemos obrigatoriamente associar a subtask em questão à um link do projeto no Testflow e no Testflow, associá-las à issue pai no Jira.  
Essa rastreabilidade permitirá também a rápida identificação dos motivos que levaram a criação daquela automação. Isso pode nos ajudar a entender melhor os nossos projetos de testes de automação.

### Jira x Testflow

---

Para realizar este link, basta ir em More / Links como mostra a figura:

Após isso, basta linkar a issue com o projeto de teste criado no Testflow selecionando a opção "Weblink" e apontar para a url do projeto. Além disso, o campo "Link Text" deve ser preenchido com o nome do projeto criado no Testflow e o comentário a critério do analista.

### Testflow x Jira

---

Para realizar este link, temos duas opções:

Link na descrição do projeto de teste ou link dentro do caso de teste.

O campo descrição do projeto de teste pode ser editado para receber o link da issue do jira, como mostra a figura:

Temos também a opção de inserir o link da issue do Jira no campo "Caso de Teste" do projeto de testes:

Dentro do caso de teste do projeto, inserir o link da issue do Jira:

# **5) Links e rastreabilidade (Jira x Visual Studio x Jira)**

---

Quando a atividade de automação é do tipo Teste Unitário, devemos realizar o link através do checkin da atividade de teste unitário dentro do Visual Studio. Este changeset será sincronizado no Jira e possibilitará um rastreio desta automação.

O link será realizado através do checkin do teste unitário feito via Visual Studio, apontando diretamente para a subtask do teste sistêmico. O Jira irá atualizar a subtask com o changeset realizado no Visual Studio. O campo **ID-Subtarefa\ID-Requisito** deverá apontar para a subtask de teste unitário e a issue pai dentro do Jira como mostra a imagem:

Após o checkin feito, o Jira automaticamente irá sincronizar este changeset na atividade de Teste Unitário no campo related checkins:

É importante no TFS que o checkin do teste unitário seja feito e aponte sempre para a subtask correta do teste unitário na issue.

Estando estes critérios atendidos, pode-se concluir a tarefa de automação de testes.
