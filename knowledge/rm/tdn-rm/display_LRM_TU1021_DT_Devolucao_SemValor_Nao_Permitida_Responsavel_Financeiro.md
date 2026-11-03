---
content_hash: 9405e8d6286d95bec9a66a9cba1c2fb3e62f6fdaefdeb378f3a10cdfda9f77fa
fetched_at: '2026-06-29T00:06:22.991671+00:00'
page_id: '223927525'
product: rm
source: tdn-rm
title: TU1021_DT_Devolucao_SemValor_Nao_Permitida_Responsavel_Financeiro
type: documentation
url: https://tdn.totvs.com/display/LRM/TU1021_DT_Devolucao_SemValor_Nao_Permitida_Responsavel_Financeiro
version: 124
---

# DEVOLUÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Bibliotecária* |
| **Função:** | *Devolução* |
| **Situação/Requisito:** | *Ao realizar uma devolução para um usuário que não tem responsável financeiro o sistema emite uma mensagem de erro falando que não é possível realizar a devolução sem responsável financeiro mesmo para movimentações que não geram nenhum valor.* |
| **Solução/Implementação:** | *O sistema não efetuava validação de valor antes de verificar o responsável financeiro, sendo assim foi inserido uma verificação para que se a movimentação não gera nenhum valor o sistema não verifique se o usuário possui responsável e conclua a movimentação com sucesso.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *TU8357* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11.82.43*  *12.1.9* |
| **Versão Corrigida:** | *11.82.43*  *12.1.9* |
| **Versão Expedida:** | *11.82.43*  *12.1.9* |

divs
