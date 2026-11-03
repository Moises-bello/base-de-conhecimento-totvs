---
content_hash: d333d62ac1966c4a100e090333512214791bf5fc753b06e25918861a6159f2dd
fetched_at: '2026-06-29T00:12:06.137389+00:00'
page_id: '913815628'
product: rm
source: tdn-rm
title: RPT00003.3.1 - Campos de formato Hora incapazes de serem somados após exportação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=913815628
version: 2
---

# Índice:

---

.\*ndice:

# Objetivo:

---

      Foi detectada uma limitação na exportação de relatórios que possuem campos de Hora para XLS/XLSX. Neste documento, será explicada a situação e como fazer para solucioná-la

# Contexto:

---

     Atualmente, ao exportar um relatório que possui campos de hora em formato XLS ou XLSX, estes ficam impossibilitados de serem calculados, como por exemplo em uma soma:

Este problema ocorre por conta de uma inconsistência na integração entre o Excel e o mecanismo de exportação e pode ser constatado nos fóruns do próprio Microsoft Excel: [Refresh cells for format change - Microsoft Community](https://answers.microsoft.com/en-us/msoffice/forum/all/refresh-cells-for-format-change/96ce8bc1-9d85-4a1c-a7d1-6b68a30f2262)

# Como Solucionar:

---

false

**1.** Primeiramente, se deve selecionar a coluna ou células que deseja corrigir:

**2.** Selecione a aba **Dados** e logo após, o botão **Texto para Colunas** :

3. Clique em **concluir**

**4.** Os campos selecionados agora estarão corrigidos, sem a necessidade de acessar um por um e recarregar (Apertando **Enter**)

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.20 ou Superiores

false

**Processo:** Exportação de Relatórios para Xls e Xlsx

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
