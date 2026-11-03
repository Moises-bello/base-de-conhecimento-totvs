---
content_hash: af1d62b2a06a2bdd73d160155f55087e06d4294fb6f5ce921bd536b3497fcb5a
fetched_at: '2026-06-29T00:10:31.269183+00:00'
page_id: '521136479'
product: rm
source: tdn-rm
title: Fonte - Provedor de Dados
type: documentation
url: https://tdn.totvs.com/display/LRM/Fonte+-+Provedor+de+Dados
version: 18
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       O objetivo deste documento tem por finalidade explicar a como utilizar um Provedor de Dados como Fonte de Dados em um relatório .Net (Totvs Reports).

# Introdução:

---

        Para confeccionar relatórios .Net (Totvs Reports) temos três opções de fonte de dados para uso: Tabelas, Consultas SQL e Provedor de Dados. Nesta página exemplificaremos o tipo Provedor de Dados.

falseFonte - Provedor de DadosFonte-ProvedorDados1Associando Provedor de Dados ao Relatório

        Existem duas formas de associar um provedor de dados como fonte de dados de um relatório.

        A primeira opção pode ser feita no momento da criação de um relatório. Depois de especificar o código e descrição do relatório (campos obrigatórios) é possível escolher o Provedor de Dados clicando nas reticências da opção “Fonte de Dados”.

        Uma tela seguinte será carregada para que possa ser pesquisado a fonte de dados. No exemplo iremos pesquisar pela fonte de dados “[Analise Curricular](https://tdn.totvs.com/x/lmpKE)”. Depois de selecionado a fonte de dados, clique em “Parâmetros”, para verificar se esta fonte exige definições de parâmetros para sua execução.

        A segunda forma é feita pelo design do relatório. Depois de atribuído o código e descrição ao relatório (campos obrigatórios) selecione o registro e clique no menu “Processos | Editar Estrutura”. Dentro do design vá ao menu “inicio” e selecione “Adicionar Fonte de Dados”.

        Na visão seguinte será apresentado as possíveis fontes de dados para se associar ao relatório, clique na guia “Provedor de Dados”.

        No exemplo vamos pesquisar pela fonte de dados “[Analise Curricular](https://tdn.totvs.com/x/lmpKE)”, selecione o registro e em seguida no botão “Adicionar / Atualizar”.

false

        Na segunda forma, para atribuir valores aos parâmetros da fonte de dados. Se deve primeiramente associar a fonte de dados a uma banda (detalhe ou sub-detalhe) do relatório. Em seguida acesse a propriedade da banda e em “Dados | Parâmetros da Fonte de Dados” poderá ser feita a atribuição de valores aos parâmetros.

2Atualizando Provedor de Dados

        Constantemente as informações dos provedores de dados são atualizadas por seus respectivos produtos. Para que os provedores já inseridos nos relatórios possam ser atualizados com as novas informações acesse o design do relatório, selecione o menu “Inicio” e clique no botão “Adicionar Fonte de Dados”. Pesquise pela fonte de dados utilizadas no relatório, selecione o registro e clique no botão “Adicionar/Atualizar” para que seu provedor seja atualizado.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.XX

false

**Processo:** Provedor de Dados

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
