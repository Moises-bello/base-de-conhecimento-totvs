---
content_hash: aa8a920fc52ca236143874542091742b8329195ccb8111140afc1d4134946a61
fetched_at: '2026-06-29T00:09:29.344791+00:00'
page_id: '423944030'
product: rm
source: tdn-rm
title: RPT00003.3 - Exportação XLS/XLSX
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423944030
version: 9
---

# Índice:

---

.\*ndice:

# Objetivo:

---

      O objetivo deste documento é exemplificar as possibilidades existentes na exportação de relatórios para Excel.

# Descrição:

---

      Atualmente, é possível exportar um relatório para os formatos XLS/XLSX de duas formas: por meio de "Processos | Gerar Relatório | Exportação Para Arquivo" ou, após a geração do relatório, através da aba "Visualização da Impressão" e "Exportar Para".

# Formato Numérico:

---

      Em relatórios onde há campos customizados com formato numérico, para que tais campos sejam exibidos corretamente após a exportação, é necessário que sejam exportados como texto.

falseIExportar Para Arquivo

Para essa exportação é necessário que seja alterada a propriedade  "Exportar texto para Xlsx e Xls" nas propriedades do relatório, alterando para Verdadeiro.

Visualização de Impressão | Exportar

Ao selecionar uma opção de exportação nessa tela, basta alterar o campo "Modo de exportação de texto" para Texto

Ao optar por exportar após a geração, é necessário que seja selecionado o modo de exportação de texto mesmo que a opção esteja marcada no Designer.

Atenção

Relatórios que possuam Sub-Relatórios no detalhe.

Caso o Sub-Relatório possua **Cabeçalho/Rodapé de** **PÁGINA**, ao exportar a ferramenta **entende** que deve pegar as informações **sempre** do primeiro item da página no caso do **Cabeçalho** e o último Item da página no caso do **Rodapé.**

Neste caso é necessário utilizar o**Cabeçalho/Rodapé de Detalhe**.

# Exportação com Reconhecimento de Dados:

---

      Quando precisamos exportar um relatório para o MS Excel nas extensões XLS ou XLSX e desejamos priorizar os dados ao invés do layout/design, como por exemplo evitar que as células sejam mescladas, devemos seguir os passos abaixo após a geração do relatório:

* Visualização de Impressão | Exportar Para | Arquivo XLSX

* Marque a opção "Modo de dados brutos"

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.20 ou Superiores

false

**Processo:** Exportação de Relatórios para Xls e Xlsx

falsefalse

**Status:** Finalizado

false

**Data:** 19/10/2018

false

**Autores:**
