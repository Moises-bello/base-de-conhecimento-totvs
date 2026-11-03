---
content_hash: 6150b4350831ccec0a82cd45c1d8416fbb56c1410fd7b6e8db0036746c198d8e
fetched_at: '2026-06-29T00:06:24.644594+00:00'
page_id: '224118829'
product: rm
source: tdn-rm
title: TUBUCM_DT_BibUsuarioData_DataServer_WebService_Erro
type: documentation
url: https://tdn.totvs.com/display/LRM/TUBUCM_DT_BibUsuarioData_DataServer_WebService_Erro
version: 119
---

# CADASTRO DE USUÁRIOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Bibliotecária* |
| **Função:** | *Cadastro de usuários via web service.* |
| **Situação/Requisito:** | *Ao utilizar o dataserver "BibUsuarioData" via webservice para salvar um registro o sistema retorna o erro "String was not recognized as a valid Boolean".* |
| **Solução/Implementação:** | *Foi identificado que a falha foi causada por uma inconsistência na geração do esquema do dataset, não estava sendo carregado corretamente todos os campos relacionados aos dados da pessoa, sendo que no momento de salvar o dataset era criado com alguns formatos incorretos por não conterem no esquema, assim gerando erro em validações de consistência do cadastro de pessoa. Foi feito o ajuste para que seja carregado o correto esquema do dataset para que no momento que o webservice enviar o xml com os dados, estes sejam armazenados corretamente.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *TUDHAT* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11.82.43*  *12.1.10* |
| **Versão Corrigida:** | *11.82.43*  *12.1.10* |
| **Versão Expedida:** | *11.82.43*  *12.1.10* |

divs
