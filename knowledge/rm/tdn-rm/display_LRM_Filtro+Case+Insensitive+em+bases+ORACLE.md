---
content_hash: c9f5fd24d2ec13d97be4e47b6ef6ccdb6d602142cfa06cd07b5b55c40bb9f7ca
fetched_at: '2026-06-29T00:08:48.521532+00:00'
page_id: '325851556'
product: rm
source: tdn-rm
title: Filtro Case Insensitive em bases ORACLE
type: documentation
url: https://tdn.totvs.com/display/LRM/Filtro+Case+Insensitive+em+bases+ORACLE
version: 3
---

|  |  |
| --- | --- |
| **Produto:** | Configurações para filtro Case Insensitive em bases ORACLE |
| **Versões:** | Todas |
| **Ocorrência:** | Utilizar o operador IN SQL nos filtros de tela do sistema RM, para que os resultados sejam retornados como CASE\_INSENSITIVE: |
| **Ambiente:** | RM |
| **Passo a passo:** | 1-      Crie um novo filtro selecionando a coluna NOME da tabela de Funcionário:      2-      Crie uma nova sentença SQL no sistema:      3-      Crie uma consulta SQL com a seguinte sintaxe (**SELECT**NOME **FROM**PFUNC **WHERE****UPPER**(NOME) **LIKE**'%' || **UPPER**(:NOME) || '%'):      4-      Adicione a sentença SQL ao filtro:      5-      Execute o filtro utilizando letras maiúsculas ou minúsculas ou ambas:      6-      Em todas as pesquisas os registros serão retornados: |
| **Observações:** | Para mais informações:    **COMUNIDADE** [R@Tecnologia](http://fluig.totvs.com/portal/p/10097/post/rtecnologia-community/1639774)   **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 8 – (Tecnologia), 2 – (Banco de Dados) |
