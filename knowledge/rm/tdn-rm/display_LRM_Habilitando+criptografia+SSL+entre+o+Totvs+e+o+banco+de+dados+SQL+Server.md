---
content_hash: b0941d6499e4ad25dceb23cdb59591122e746a107f9f52f4941122ecb33dee13
fetched_at: '2026-06-29T00:10:58.804348+00:00'
page_id: '607036538'
product: rm
source: tdn-rm
title: Habilitando criptografia SSL entre o Totvs e o banco de dados SQL Server
type: documentation
url: https://tdn.totvs.com/display/LRM/Habilitando+criptografia+SSL+entre+o+Totvs+e+o+banco+de+dados+SQL+Server
version: 3
---

1- Abra na pasta do RM o arquivo RM.Host.exe.config com um editor de texto.

2- Adicione as TAGS:

<add key="EnableWSSecurity" value="true" />  
<add key="DBSCONNSTREXTENSIONS" value="encrypt=true;trustServerCertificate=true" />

3- Reinicie o serviço do host.
