---
content_hash: ee4dc4c7e35c6a0463a877313ec5c4f56f53789edab98bdc9d4d880423590a20
fetched_at: '2026-06-29T00:10:09.960155+00:00'
page_id: '452719755'
product: rm
source: tdn-rm
title: Carga Inicial Funcionários Demitidos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719755
version: 4
---

Neste processo, serão gerados os gatilhos dos eventos não periódicos [S-2200 – Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719244) e S-2300 – Trabalhador Sem Vínculo de Emprego/Estatutário - Início  para a Fila de Eventos dos funcionários demitidos anterior a data de obrigatoriedade do eSocial.   
**Atenção:**

1. 1. Será possível filtrar por "Período da Rescisão" e/ou "Período do último movimento ".
   2. O processo também disponibiliza sua execução para Multi-Coligadas.

**Observação:**

01 - Na seleção de Funcionários por default, somente será consistida a situação "D - Demitidos", os demais dados de seleção (Tipo de Funcionário, Código de Recebimento, Fórmulas e Filtros) poderão ser realizados da maneira desejada.

02 - Quando há rescisão complementar e a data de último movimento for alterada, o processo poderá ser filtrado para considerar o limite entre "Período da Rescisão" e "Período do último movimento ". Para que ocorra desta forma deve-se selecionar os dois períodos.

**Exemplo:**

**Funcionário A** demitido em 31/03 e com rescisão complementar alterando a data de último movimento para 30/06.

**Funcionário B** demitido em 31/03 e com rescisão complementar alterando a data de último movimento para 30/09.

Selecionando  "Período da Rescisão" = 01/03 a 31/03 e "Período do último movimento ". 01/03 a 31/07 será selecionado o **funcionário A** somente.
