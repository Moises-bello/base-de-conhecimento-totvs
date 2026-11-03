---
content_hash: 4ebd6ac6e63115244dc0bdc910865bc51489bcbe1e9b5a48a0983c9f4e1c95d8
fetched_at: '2026-06-29T00:06:14.471740+00:00'
page_id: '210046264'
product: rm
source: tdn-rm
title: TTMA03_DT_Exclusao_Prova_Dinamica_Erro
type: documentation
url: https://tdn.totvs.com/display/LRM/TTMA03_DT_Exclusao_Prova_Dinamica_Erro
version: 1
---

# Provas Dinâmicas

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Avaliação e Pesquisa* |
| **Função:** | *Provas* |
| **Situação/Requisito:** | *Ao tentar excluir uma prova dinâmica que não possui nenhum candidato ou questão associada o sistema retorna uma mensagem de erro não tratada e não conclui a exclusão.* |
| **Solução/Implementação:** | *Foi identificado que no momento da exclusão o sistema tentava verificar uma condição da prova, sendo que a prova já está com situação de exclusão assim não conseguindo acessar os dados e retornando o erro. Para corrigir o problema é feita uma verificação antes da exclusão, para que se a prova estiver com status de exclusão o sistema ignore métodos que são utilizados para criação e edição de provas.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *v* |
| **Versões/Release:** | *12.1.8* |
| **Versão Corrigida:** | *12.1.8* |
| **Versão Expedida:** | *12.1.8* |

divs
