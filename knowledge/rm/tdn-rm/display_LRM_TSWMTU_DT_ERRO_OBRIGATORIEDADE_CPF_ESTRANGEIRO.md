---
content_hash: f72c303bc2c74eb1320bcfea00d9d7cc91bc359affb88283c6793765d320c730
fetched_at: '2026-06-29T00:06:01.025645+00:00'
page_id: '198934899'
product: rm
source: tdn-rm
title: TSWMTU_DT_ERRO_OBRIGATORIEDADE_CPF_ESTRANGEIRO
type: documentation
url: https://tdn.totvs.com/display/LRM/TSWMTU_DT_ERRO_OBRIGATORIEDADE_CPF_ESTRANGEIRO
version: 1
---

# CADASTRO DE CANDIDATO - PROCESSO SELETIVO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional - Processo Seletivo* |
| **Módulo:** | *TOTVS Gestão Educacional - Processo Seletivo* |
| **Função:** | *Cadastro de Candidatos* |
| **Situação/Requisito:** | *Ao realizar um cadastro, ao selecionar um registro no UF natal de "estrangeiro" o campo CPF ainda estava sendo considerado obrigatório.*  *O uso do parametro "Utilizar parametrização dos campos da guia "Documentos" sem exigir obrigatoriedade" estava incoerente com a sua descrição, desta forma gerando validações inválidas no processo de inscrição.* |
| **Solução/Implementação:** | *Foi incluído um método para que ao selecionar um registro em UF natal, seja realizado uma validação da obrigatoriedade do campo CPF.*  *Acerto do uso do parametro "Utilizar parametrização dos campos da guia "Documentos" sem exigir obrigatoriedade".* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *12.1.7* |
