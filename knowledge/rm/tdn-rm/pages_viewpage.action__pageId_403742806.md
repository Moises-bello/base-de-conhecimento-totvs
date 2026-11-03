---
content_hash: 8e06419fc1f3d3e316391ddce8dd07f34e0cc4a164f01e6ad0435d8a5bd69e90
fetched_at: '2026-06-29T00:09:11.277682+00:00'
page_id: '403742806'
product: rm
source: tdn-rm
title: Como gerar S-1200 para Autônomos do Fluxus que utilizam categoria 712?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=403742806
version: 9
---

Para gerar autônomos com categoria diferente do De / Para, deverá criar um campo complementar em Administração de Pessoal/Cliente Fornecedor.

O campo complementar deverá ter o código igual **CODCATEGORIAESOCIAL e Tipo Inteiro.**

  Após criar o campo complementar, acessar Cliente/Fornecedor e editar informando nos campos complementares a categoria desejada

**OBS**: Deixando este campo em branco o sistema irá considerar o de / para conforme help das categorias.

  Gerando o XML S-1200  a tag  *codCateg* será preenchida com a categoria informada nos campos complementares.
