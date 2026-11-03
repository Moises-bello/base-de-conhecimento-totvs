---
content_hash: a7b71495962e36edf9f3c23c87e87e49fe8ffdf7ff9b0107bdbca9b4c0d1f0af
fetched_at: '2026-07-02T19:24:21.449661+00:00'
page_id: '267794675'
product: protheus
source: tdn-tec
title: DBAccess - Seção [Environment], chave ClientLibrary
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267794675
version: 6
---

ClientLibrary

Define uma **biblioteca** específica para conexão com **banco de dados**.

---

## Valores válidos

| Sistema Operacional | Valor | Descrição |
| --- | --- | --- |
| Linux | /opt/unixODBC/lib/libodbc.so | Utiliza unixODBC para conexões com o banco de dados |
| Windows | C:\app\client\user\product\12.1.0\client\_1\oci.dll | Utiliza OCI para conexões com o Banco Oracle 12 |

---

## Observações

* Quando esse valor é definido para um banco, ele será global para todas as configurações do mesmo.
* O path/caminho de disco da unixODBC pode variar de acordo com a versão e/ou distribuição do sistema operacional.
* Para a plataforma Linux, é pré-requisito o uso da unixODBC com versão igual ou superior a 2.3.7

---

Exemplo

Conexões Microsoft SQL Server utilizarão a biblioteca unixODBC

textdbaccess.ini
