---
content_hash: e4b29489d40d3334e280cd0fa9c0dfa15e1a2773e99c32026b0fdac3935c7550
fetched_at: '2026-07-02T19:24:21.365910+00:00'
page_id: '266979445'
product: protheus
source: tdn-tec
title: DBAccess - Seção [Environment], chave ConnectionString
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=266979445
version: 4
---

Permite especificar uma string de conexão com o SGBD, sem que seja necessário criar ou configurar um DSN de sistema na ODBC da máquina onde está o true.

Para todos os bancos (exceto Oracle) deve ser fornecida a string de conexão no formato ODBC, especificando:

* O nome do Driver utilizado entre chaves
* O nome do host onde está o MSSQL Server
* E o nome do Database a ser utilizado

Para Oracle, pode ser especificado o banco no formato: **//<ora\_host>:<ora\_port>/<oracle\_service\_name>**

---

## Exemplo ODBC

## Exemplo Oracle

---

## Observações

* Especificar a chave na seção de configuração de um banco de dados tem efeito sobre o valor default de todos os ambientes nele configurados.
* Para esta configuração ser considerada, e a string de conexão especificada ser usada na íntegra, também deve ser acrescentado no arquivo de configuração dbaccess.ini a chave **ConnectionMode=2**
* Caso seja especificada dentro de uma seção de conexão específica [Banco/ambiente], esta configuração será considerada para o ambiente em questão.
* Esta configuração está disponível e passa a ser considerada a partir do build **20161016** do true.

---

## Exemplos

text

---

## Veja Também
