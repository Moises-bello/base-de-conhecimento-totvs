---
content_hash: 04c09d6d6d24d7fe5cd72fb79cf6cf9e2cf9992d7d7b88e021e36f095113ab44
fetched_at: '2026-06-29T00:06:02.483172+00:00'
page_id: '198945341'
product: rm
source: tdn-rm
title: TSM148_DT_Cadastro_de_livro_para_registro_de_diploma_11_82_41
type: documentation
url: https://tdn.totvs.com/display/LRM/TSM148_DT_Cadastro_de_livro_para_registro_de_diploma_11_82_41
version: 2
---

# DIPLOMAÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Educacional.* |
| **Módulo:** | *TOTVS Gestão Educacional.* |
| **Função:** | *Cadastro de livro para registro de diploma.* |
| **Situação/Requisito:** | *Erro no cálculo do número da folha quando o livro cadastrado é do tipo "Contínuo".* |
| **Solução/Implementação:** | *For identificado que o sistema está gerando o número da folha incorretamente quando o tipo de livro for "Contínuo". Isto ocorre porque o sistema gera o*  *número do registro para tipo "Contínuo" considerando os demais contínuos cadastrados. Com isto, foi identificada uma inconsistência e foi definido que*  *quando livro for "Contínuo" não poderá haver mais de um aberto. Assim, foi incluída validação para tratar isto.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *11.82.38 / 11.82.41.* |
