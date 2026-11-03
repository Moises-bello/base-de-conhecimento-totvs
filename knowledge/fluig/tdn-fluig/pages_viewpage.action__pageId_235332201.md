---
content_hash: 980851b32ad93712f35842082b8e7eafb0e6007e00c78432175cdf0ebc41d57e
fetched_at: '2026-06-28T21:35:22.254671+00:00'
page_id: '235332201'
product: fluig
source: tdn-fluig
title: DES - Erro wdk/MetaList na criação de novos formulários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235332201
version: 8
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

**Versão:** 1.5.7

# Ocorrência

Ao exportar um novo formulário do TDS (TOTVS Developer Studio) para a plataforma, é exibido o seguinte erro em tela: JBAS014581: EJB 3.1 FR 13.3.3: *BMT bean wdk/MetaList should complete transaction before returning*.

**Figura 1 - Erro ao exportar o novo formulário**

# Causa

O problema está na utilização de palavras reservadas em campos do formulário, por exemplo: version, documentid, companyid, etc. Ao utilizar esses nomes, a plataforma tentará criar duas colunas com o mesmo código, onde gera o erro da **Figura 1**.

xmlExemplo de uso incorreto - Campo documentId
