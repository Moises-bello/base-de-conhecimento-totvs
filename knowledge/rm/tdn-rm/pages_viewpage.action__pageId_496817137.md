---
content_hash: ca68644a1684c95ef4c6b8505db26ea86cd1747273d94fc5969edb09952f4909
fetched_at: '2026-06-29T00:10:22.518410+00:00'
page_id: '496817137'
product: rm
source: tdn-rm
title: Utilizando a Atividade "Copia de Filtros"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=496817137
version: 3
---

## **ÍNDICE**

1. **Visão Geral**
2. **Exemplo de utilização**

**01. VISÃO GERAL**

      A atividade "Copia de Filtros" tem por função, copiar os filtros de uma coligada para outra de acordo com o dataset da visão.

**02. EXEMPLO DE UTILIZAÇÃO**

      Descrição dos campos da atividade "Cópia de Filtros":

**Atividade:**

* **Nome:**Nome da atividade
* **Descrição:** Descrição da atividade
* **Habilitado:** Define se a atividade estará em uso ou não.

**Parâmetros da Atividade:**

* **Código da Aplicação:**Código da aplicação que deseja copiar os filtros
* **Código da Coligada Origem:**Código da Coligada que deseja copiar os filtros
* **Somente Filtros Globais:**Opção de copiar ou não os filtros globais

    Como exemplo, vamos realizar a copia dos filtros da coligada "1 (TOTVS SA)" para uma coligada "6 (Instituto TOTVS de Ensino SA)".

    Após a criação da fórmula, adicione a atividade "Copia de Filtros" no Fluxo de Trabalho Sequencial, como mostra imagem abaixo:

Em seguida é necessário configurar os parâmetros da atividade. No exemplo utilizado foi utilizado a aplicação "G (Serviços Globais)" e a coligada 1 (TOTVS SA), para replicar os filtros para a coligada "6 (Instituto TOTVS de ensino SA)". O parâmetro de Filtros globais foi deixado como falso, ou seja, os filtros globais não serão copiados (Caso deseje copiar também os filtros globais, é só deixar o parâmetro como "True"). Imagem abaixo:

Realizado a configuração da atividade, é necessário adicionar um gatilho no processo da formula visual. Para tal configuração, selecione a formula criada e clique em "Editar", na tela de edição selecione a aba "Processos de Fórmula Visual", e adicione a action "GlbColigadaAction" como mostra a imagem abaixo:

Após adicionado o gatilho, foi acessado a visão de coligada "Serviços Globais | Administração | Coligada". Ao ser carregada a visão foi selecionado a coligada "6 (Instituto TOTVS de ensino SA)" , clicado em "Processos | Fórmula Visual | Atividade Cópia de Filtros" e executado o processo. Imagem abaixo:

Após execução da fórmula, foi acessada a coliga "6 (Instituto TOTVS de ensino SA)" e acessado a visão de "Usuários" por exemplo, Verifique que os filtro foram copiados corretamente, em exceto os filtros globais, pois a opção de copiar os filtro globais estava como "False". Imagens abaixo:
