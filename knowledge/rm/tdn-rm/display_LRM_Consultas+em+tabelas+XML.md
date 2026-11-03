---
content_hash: b03e8caf2bdf1ddaaba36ddae20ff3aadeeb767340ef1c8dccee7335fdac2301
fetched_at: '2026-06-29T00:05:59.453256+00:00'
page_id: '190519728'
product: rm
source: tdn-rm
title: Consultas em tabelas XML
type: documentation
url: https://tdn.totvs.com/display/LRM/Consultas+em+tabelas+XML
version: 9
---

# **Introdução**

---

Tabelas ou registros XML é um recurso presente nos SGBD´s (Sistemas gerenciadores de banco de dados) SQL Server e Oracle. Para uso, devemos utilizar instruções T-SQL para o carregar informações de um documento XML.

**Como Fazer**

---

Por limitação técnica, o RM não suporta carregar uma consulta T-SQL que utilize um documento XML. Entretanto é possível a criação de uma view diretamente no banco de dados e no cadastro de consulta SQL do sistema referencie a view criada.

Observações

***A view pode ser definida como uma tabela virtual composta por linhas e colunas de dados vindos de tabelas relacionadas em uma query (um agrupamento de SELECT’s, por exemplo). As linhas e colunas da view são geradas dinamicamente no momento em que é feita uma referência a ela.***

***A query que determina uma view pode vir de uma ou mais tabelas, ou até mesmo de outras views e podemos alterar dados por meio delas, o que é feito com algumas restrições.***

Mediante as informações citadas, podemos manusear através de views informações de arquivos ou registros do formato XML.

Para maiores informações:

****[@FRAMEWORK](http://fluig.totvs.com/portal/p/10097/subject/rframework)****

**Canais de Atendimento**

**Chamado:** Através do Portal TOTVS - [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2-2-3-9-5 (Framework) ou 2-2-3-9-4 (BI)

|  |  |
| --- | --- |
| **Produto** | Framework |
| **Versão** | Qualquer versão |
| **Processo** | Cadastro de Consulta SQL |
| **Subprocesso** | Utilizando Consulta SQL |

|  |  |
| --- | --- |
| Status do Documento: | Produção |
| Data: | 01/07/2015 |
| Versão: | Qualquer Versão |
| Versão Anterior: | Qualquer Versão |
| Autores: | Gustavo Henrique Silva Seabra |
