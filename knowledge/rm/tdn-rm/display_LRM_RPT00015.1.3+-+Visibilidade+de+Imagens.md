---
content_hash: c2f213420f2e7bfe00655a78bd9c1a7c6f7b7fae1b3a6c7a1038444d10dc357a
fetched_at: '2026-06-29T00:08:41.525286+00:00'
page_id: '286733217'
product: rm
source: tdn-rm
title: RPT00015.1.3 - Visibilidade de Imagens
type: documentation
url: https://tdn.totvs.com/display/LRM/RPT00015.1.3+-+Visibilidade+de+Imagens
version: 3
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       Este documento objetiva mostrar como ocultar uma imagem ao gerar um relatório no RM Reports.

# Introdução:

---

      Ao criar um relatório no RM Reports que contenha imagens, é possível alterar as configurações fazendo com que somente uma das imagens apareça quando o relatório for gerado.

       Exemplo: Um relatório que contenha Imagem1 e Imagem2 e deseja que na situação "A" somente a Imagem1 seja exibida.

       Para isso, é só configurar para que na condição "A" a Imagem2 seja ocultada, desta forma somente a Imagem1 aparecerá ao gerar o relatório.

# Processo de Configuração:

---

             No passo a passo abaixo será mostrado como ocultar uma imagem ao gerar um relatório no RM Reports. Para isso é necessário que o relatório tenha como fonte de dados uma consulta SQL que retorne o valor desejado para ser utilizado na condição da formatação.

**Passo a passo para configuração:**

falseInstalação em N camadas (App Server)1º Passo:

Selecione a imagem que será escondida e clique em Regras de Formatação.

2º Passo:

 Em seguida clique em "Editar Regra Folha..."

3º Passo:

 Clique em "Condição".

4º Passo:

 Agora vamos informar qual a condição para que a imagem seja escondida.

No caso abaixo, é quando a consulta SQL retorna um valor de CODIGO igual a 1.

5º Passo:

 Em seguida, altere o campo "Visível" para FALSO. Desta forma, a imagem escolhida não ficará visível.

6º Passo:

 Não se esqueça de aplicar a regra de formatação, conforme evidenciado na imagem abaixo.

Clique em OK e pronto! A imagem agora será escondida quando a condição estabelecida for respeitada.

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.XX e 12.01.XX

false

**Processo:** Visibilidade de Imagens

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
