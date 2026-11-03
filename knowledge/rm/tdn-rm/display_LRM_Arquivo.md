---
content_hash: e38a31a9eba6b901a379655fb939145048f555e438d1754097b7954f138100cb
fetched_at: '2026-06-29T00:11:21.351391+00:00'
page_id: '692927342'
product: rm
source: tdn-rm
title: Arquivo
type: documentation
url: https://tdn.totvs.com/display/LRM/Arquivo
version: 4
---

Nesta guia será possível parametrizar o tipo de armazenamento dos arquivos. Os arquivos podem ser armazenados de duas maneiras:

**Arquivo na base de dados**

Os arquivos serão salvos direto na base de dados.

**Arquivo de algum diretório**

Os arquivos serão salvos no diretório informado no parâmetro "Diretório de armazenamento".

A partir da versão 12.1.2209

Caso a instituição esteja utilizando o RM com a tag TenantPathEnabled habilitada, então haverá uma mudança na forma onde será salvos os arquivos, quando utilizado a opção "Arquivo de algum diretório".

Agora a deve ser informado somente o nome da pasta onde os arquivos serão salvos. Sendo assim os arquivos serão salvos no seguinte caminho:

"{Servidor do RM.Host.exe}\Arquivos\{Alias}\{Pasta definida nas parametrizações do processo seletivo}".
