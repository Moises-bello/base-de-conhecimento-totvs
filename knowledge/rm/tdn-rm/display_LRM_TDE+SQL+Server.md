---
content_hash: bb772e7ba26134c69f04589d2850f313f46753a34ad72886771495af1cae65a3
fetched_at: '2026-06-29T00:10:38.154604+00:00'
page_id: '544178819'
product: rm
source: tdn-rm
title: TDE SQL Server
type: documentation
url: https://tdn.totvs.com/display/LRM/TDE+SQL+Server
version: 9
---

O **TDE** (Transparent Data Encryption) para **SQL Server** é uma ferramenta oficial da **Microsoft**, de criptografia para o banco de dados **SQL Server**, disponível a partir do **SQL Server 2008**. De acordo com a [documentação disponibilizada pela Microsoft](https://docs.microsoft.com/pt-br/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver1), o **TDE** performa a criptografia e "descriptografia" de I/O em tempo real dos dados e arquivos de *log*. Ele utiliza uma chave para criptografia da *database* **DEK** (Database Encryption Key), armazenada no registro de *boot* da *database* para disponibilidade durante a recuperação. 

Esta ferramenta foi estudada e testada para verificar a viabilidade de seu uso no produto **RM**, para que este esteja apto, caso o cliente queria atender algum item de gerenciamento/segurança, de dados em garantias à **Lei Geral de Proteção de Dados** (LGPD).

# Ambiente Operacional

Para os testes de performance, utilizamos as 4 versões do SQL Server atualmente homologadas para o RM, sendo essas: SQL 2012, 2014, 2016 e 2017, todas estas na release DEVELOPER.

Para maior fidelidade ao teste, utilizamos o mesmo modo de compatibilidade em todas as versões: SQL 2012 (110)

* Sistema Operacional Windows Server 2016 Standard
* Processador Intel Xeon Silver 4116 @ 2.10GHz
* Memória RAM 16GB
* HD virtualizado VMWare

Para consultar mais informações, clique abaixo
