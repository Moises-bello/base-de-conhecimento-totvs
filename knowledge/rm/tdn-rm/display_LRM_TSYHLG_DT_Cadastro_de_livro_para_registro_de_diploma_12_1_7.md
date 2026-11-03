---
content_hash: 662cf9114938433783052d060293713e80d4a4f96063a65833231775bfc49c4e
fetched_at: '2026-06-29T00:06:02.537423+00:00'
page_id: '198946072'
product: rm
source: tdn-rm
title: TSYHLG_DT_Cadastro_de_livro_para_registro_de_diploma_12_1_7
type: documentation
url: https://tdn.totvs.com/display/LRM/TSYHLG_DT_Cadastro_de_livro_para_registro_de_diploma_12_1_7
version: 2
---

# DIPLOMAÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Educacional.* |
| **Módulo:** | *TOTVS Gestão Educacional.* |
| **Função:** | **Cadastro de livro para registro de diploma*.* |
| **Situação/Requisito:** | **Erro no cálculo do número da folha quando o livro cadastrado é do tipo "Contínuo"*.* |
| **Solução/Implementação:** | *For identificado que o sistema está gerando o número da folha incorretamente quando o tipo de livro for "Contínuo". Isto ocorre porque o sistema gera o*  *número do registro para tipo "Contínuo" considerando os demais contínuos cadastrados. Com isto, foi identificada uma inconsistência e foi definido que*  *quando livro for "Contínuo" não poderá haver mais de um aberto. Assim, foi incluída validação para tratar isto.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *12.1.7.* |
