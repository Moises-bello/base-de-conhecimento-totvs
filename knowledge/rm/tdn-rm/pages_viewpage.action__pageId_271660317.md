---
content_hash: 201c6ea7209cec476f2d7e2a280d9428d56779f7bba84b1b7dbab01f8eded160
fetched_at: '2026-06-29T00:08:28.123753+00:00'
page_id: '271660317'
product: rm
source: tdn-rm
title: Parâmetros de execução de Fórmula Visual via processo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271660317
version: 12
---

# Índice:

---

.\*ndice:

# Objetivo:

---

      Exemplificar a criação de uma Fórmula Visual que utilize parâmetros passados pelo usuário para execução através de Processo.

# Criando a Fórmula Visual:

---

No exemplo a seguir, criaremos uma Fórmula Visual que irá alterar as permissões de Acesso a Campos de diversos perfis ao mesmo tempo.

falseCriando a Fórmula Visual1º Passo

      Criaremos uma nova Fórmula Visual. No exemplo, daremos o nome Teste\_Perfil.

.

2º Passo

      Em seguida, na edição da Fórmula, informamos os Parâmetros de Execução

      Depois, adicionamos uma nova Tabela, conforme exemplo abaixo:

Informamos as Colunas e Título dos Campos que serão utilizados, por exemplo: Os campos da tabela GAUTZTAB.

Observação

Os nomes das colunas não precisam necessariamente serem os mesmos da tabela. Para simplificar a execução da Fórmula Visual, utilizaremos os nomes semelhantes aos da Tabela em questão.

3º Passo

      Em seguida adicionaremos a atividade “Para cada interação” e “Sequência” que percorrerá todas as linhas da tabela, conforme exemplo abaixo:

4º Passo

      Em seguida adicionamos a atividade “Ler Registro” e informamos o nome do DataSet junto com a Chave Primaria da Leitura:

Selecione o DataServer que será utilizado. Neste exemplo utilizamos o cadastro de Perfis.

Em seguida, informar as Chaves primárias da leitura conforme exemplo abaixo:

5º Passo

      Adicione a atividade “Adicionar registro na Tabela” Informando primeiro a Tabela a ser selecionada, em seguida os parâmetros que serão utilizados, conforme o exemplo abaixo:

Após informar a tabela, os campos da mesma serão carregados nas propriedades:

Em seguida informamos as Chaves e os parâmetros a serem solicitados na Fórmula conforme abaixo:

Após as chaves primárias, informamos em seguida os parâmetros criados no passo 2 do tutorial conforme abaixo:

6º Passo

      Por fim, adicionaremos a atividade “Salvar Registro” para salvar a as alterações nos campos.

# Executando a Fórmula Visual:

---

      Com a edição da Fórmula Visual finalizada, vamos adicioná-la a visão de Perfis para ser executada, conforme exemplo a seguir:

falseExecutando a Fórmula Visual1º Passo

      Para executar a Fórmula Visual, acesse o menu de Perfis (localizado em “Serviços Globais | Segurança | Perfis”). Depois de carregada a visão é necessário selecionar a opção “Processos | Fórmula Visual | Gerenciar”. Selecionaremos a aba “Processos de Fórmula Visual” e anexamos a Fórmula Visual:

2º Passo

      Feito isso, basta selecionar os perfis que deseja alterar e executar a Fórmula Visual conforme exemplo abaixo:

      Neste exemplo os campos Pode Alterar e Pode Consultar receberão apenas os caracteres F = False ou T = True

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.15 ou Superiores

false

**Processo:** Execução de Fórmula Visual com Passagem de Parâmetro via Processo

falsefalse

**Status:** Finalizado

false

**Data:** 14/02/2017

false

**Autores:**
