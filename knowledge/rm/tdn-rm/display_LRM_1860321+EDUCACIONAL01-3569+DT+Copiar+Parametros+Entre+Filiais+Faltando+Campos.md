---
content_hash: 73cfeef0dc4e2cb189ca2e870439a708b50e6a860ca4816e612ce34e16b8e67c
fetched_at: '2026-06-29T00:08:50.090731+00:00'
page_id: '331862551'
product: rm
source: tdn-rm
title: 1860321 EDUCACIONAL01-3569 DT Copiar Parametros Entre Filiais Faltando Campos
type: documentation
url: https://tdn.totvs.com/display/LRM/1860321+EDUCACIONAL01-3569+DT+Copiar+Parametros+Entre+Filiais+Faltando+Campos
version: 95
---

# PARÂMETROS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Educacional. |
| **Função:** | Parâmetros |
| **Situação/Requisito:** | Foi identificado que alguns parâmetros não eram copiados corretamente entre filiais quando utilizado o itens de "salvar processo como" e "carregar processo":    - 15.04 - RM Portal | 15.04.01 - RM Portal - Gerais | 5/11 - Calendário do aluno - 15.04 - RM Portal | 15.04.01 - RM Portal - Gerais | Relatórios | 1/2  -15.09 - Geração de Usuários | Aluno | 2/5 - Localidades  -15.09 - Geração de Usuários | Professores | 2/3 - Localidades  -15.09 - Geração de Usuários | Funcionários | 2/3 - Localidades |
| **Solução/Implementação:** | Foi identificado que a cópia não era feita pois os itens que não eram copiados não possuem vínculo direto com nenhum componente na tela, ou seja, são exibidos através de métodos que manipulam os dados e exibem na tela e o processo de salvar utiliza os campos com vínculos (bind) direto na tela. Foram criados campos ocultos com vínculos destes campos para que o processo de salvar e carregar os dados consiga ter acesso aos dados da tela. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A. |

divs
