---
content_hash: 02666c28ff1dc19e7ea29b618bc327335f06ad91e8142113ef460af730599368
fetched_at: '2026-06-29T00:06:26.378819+00:00'
page_id: '225262153'
product: rm
source: tdn-rm
title: TUEUBL_DT_Campos_Responsavel_Obrigando_Igual_Candidato
type: documentation
url: https://tdn.totvs.com/display/LRM/TUEUBL_DT_Campos_Responsavel_Obrigando_Igual_Candidato
version: 120
---

# CADASTRO RESPONSÁVEL - PORTAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Processo Seletivo* |
| **Função:** | *Cadastro de responsável - Portal* |
| **Situação/Requisito:** | *Ao efetuar o cadastro de um responsável que já existe após cadastrar o candidato, o sistema obriga o preenchimento de alguns campos que nos parâmetros dos responsáveis não estão como obrigatório porém são obrigatórios para o candidato.* |
| **Solução/Implementação:** | *Foi identificado que a validação dos dados no momento de salvar o responsável estava utilizando a mesma função utilizada para validação dos dados do candidato assim retornando a obrigatoriedade de campos incorretamente, foi feito o ajuste ao salvar um responsável para que utilize a validação de campos obrigatório definidas para o responsável.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *TUUEB4* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.10* |
| **Versão Corrigida:** | **12.1.9**  *12.1.10* |
| **Versão Expedida:** | *12.1.10* |

divs
