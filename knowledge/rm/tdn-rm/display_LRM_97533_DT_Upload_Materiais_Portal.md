---
content_hash: 889be6b6fb0ceda32c4c718ea667a28996c4f43dc152d25802b92ae3c197760f
fetched_at: '2026-06-29T00:08:23.266610+00:00'
page_id: '269553886'
product: rm
source: tdn-rm
title: 97533_DT_Upload_Materiais_Portal
type: documentation
url: https://tdn.totvs.com/display/LRM/97533_DT_Upload_Materiais_Portal
version: 112
---

# UPLOAD DE MATERIAIS - PORTAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Upload de Materiais - Portal* |
| **Situação/Requisito:** | *A ferramenta de upload de materiais não funciona corretamente quando o nome do arquivo contém certos caracteres especiais na codificação UTF-8 gerado pelo MacOS, por exemplo.* |
| **Solução/Implementação:** | *Script para alterar o campo PATHARQUIVO da tabela SWEBMATERIALSEC de varchar para nvarchar (SQL Server) e varchar2 para nvarchar2 (Oracle), para que possa ser gravado a nome do arquivo contendo caracteres na codificação UTF-8.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *TVTYXI* |
| **Requisito (ISSUE):** | *N/A* |

divs
