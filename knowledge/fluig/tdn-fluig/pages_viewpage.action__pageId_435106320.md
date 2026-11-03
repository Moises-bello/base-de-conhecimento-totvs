---
content_hash: 33b63c7e3b65f964eebd6702a63e1d137c3b2967572c68c4a4374cb70ebffd07
fetched_at: '2026-06-28T21:35:26.851143+00:00'
page_id: '435106320'
product: fluig
source: tdn-fluig
title: ARQ - Problema nas pesquisas de registros que contenham "[" (abre colchete)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435106320
version: 4
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

**Banco de Dados:** SQL Server

# Ocorrência

Os registros que são gravados com o caractere "**[**" (abre colchete) não são localizados na plataforma, ao acionar a opção Filtrar.

A animação abaixo demonstra o problema:

# Solução

Caso você precise pesquisar algum registro que contenha '[' (abre colchete) conforme a situação relatada, deve-se aplicar um "escape" utilizando a sequência de caracteres '[[]' (dois abre colchetes e um fecha colchete). 

**Exemplo:**  
Descrição do registro: [e1] Grupo A  
Para realizar a busca deve usar assim: [[]e1] Grupo A

# Observação

Esse procedimento só é necessário nas buscas realizadas com o banco de dados SQL Server.
