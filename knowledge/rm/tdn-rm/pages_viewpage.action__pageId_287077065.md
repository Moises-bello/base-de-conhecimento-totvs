---
content_hash: 28e70ad6a16da93f28fc1253f146d2f88c2eaa4f1e0aa1a9cb36cbd9a2fba049
fetched_at: '2026-06-29T00:08:42.519449+00:00'
page_id: '287077065'
product: rm
source: tdn-rm
title: Utilizando a atividade "Transformar registro em XML"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=287077065
version: 4
---

# Objetivo

---

        A finalidade da atividade **Transformar registro em XML** da fórmula visual é converter registros em XML. Esses registros podem ser originados de uma Consulta SQL, de um DataServer ou de uma tabela. Da mesma forma, o destino do XML gerado dependerá do fluxo criado na fórmula visual, podendo ser um e-mail, uma exceção, um novo registro, entre outros.

**Dica:** Esta atividade é muito útil para ajudar a identificar problemas na lógica de execução da fórmula visual. Você pode utiliza-la para ver quais dados estão sendo utilizados como base na formula visual e poder diagnosticar se a os dados condizem com as condições e operações realizadas na fórmula. Utilize ela junto com a atividade de gerar exceção em pontos diferentes da fórmula para ver se as atividades executadas estão se comportando conforme deveriam.

        A seguir, veja um exemplo de como usar a atividade **Transformar registro em XML.**

# Exemplo - Atividade: Transformar registro em XML

---

        Fluxo criado para o exemplo:

* Foi usado uma atividade de Executar consulta SQL para filtrar os dados desejados. Essa atividade irá executar uma consulta SQL cadastrada no sistema.
* Com a atividade Transformar registro em XML o retorno da Consulta SQL foi convertido para XML.
* A atividade de Gerar exceção foi adicionada para visualização do XML.

falseExemploPasso 1Passo 1Passo 1

**Adicionando a atividade Executar consulta SQL**

1. Busque e adicione a atividade "Executar Consulta SQL" no fluxo;
2. Clique com o botão esquerdo do mouse e selecione a opção "Selecionar Consulta SQL";
3. Localize a consulta cadastrada no sistema;
4. As propriedades da atividade ficaram da seguinte forma:
Passo 2Passo 2Passo 2

**Adicionando a atividade Transformar Registro em XML**

1. Busque e adicione a atividade "Transformar Registro em XML" no fluxo;
2. Nas propriedades da atividade, clique duas vezes no ícone de banco da opção Tabela. Como utilizaremos o retorno da consulta SQL para transformar em XML, selecione-o para associar o membro;
3. As propriedades da atividade ficaram da seguinte forma:
Passo 3Passo 3Passo 3

**Adicionando a atividade Gerar Exceção**

1. Busque e adicione a atividade "Gerar Exceção" no fluxo;
2. Nas propriedades da atividade, clique duas vezes no ícone de banco da opção Mensagem de Erro. Nosso objetivo é executar a fórmula e visualizar o XML gerado na atividade anterior, como uma mensagem de exceção. Para isso, selecione a opção XML para associar o membro.
3. As propriedades da atividade ficaram da seguinte forma:
Passo 4Passo 4Passo 4

**Executar a Fórmula Visual**

1. Salve e execute a Fórmula Visual:
2. Visualize o Progresso da execução do processo:
3. XML gerado corretamente:

   00001
   3192.80

   00002
   1355.29

   00003
   5609.51

   00004
   580.00

   00005
   1734.66
   ]]>
falsefalse

**Produto:** Framework

false

**Versão:** 12.1.XX

false

**Processo:** Fórmula Visual

false

**Subprocesso:** Utilizando a atividade "Transformar registro em XML"

falsefalse

**Status:** Finalizado

false

**Data:** 22/09/2017

false

**Autores:**
