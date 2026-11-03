---
content_hash: a09f5b0466ebf89699b9292785e53632dd7e0f1d7b5889411e5449f4fcdf5a18
fetched_at: '2026-06-29T00:09:58.826209+00:00'
page_id: '452711949'
product: rm
source: tdn-rm
title: 3766454 MATESTCNTFTOF01-3426 DT Consistir Filtro por Usuário/Perfil ao Gerar
  OS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452711949
version: 2
---

# CONSISTIR FILTRO POR USUÁRIO/PERFIL

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | BackOffice RM. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Função:** | Gerar OS. |
| **Situação/Requisito:** | Ao gerar uma Ordem de Serviço pelo processo de atendimento a mensagem abaixo era apresentada:  **Valor inválido para o campo "CHAPA"** |
| **Solução/Implementação:** | Foi verificado que a mensagem estava sendo apresentada pois havia um filtro por perfil que bloqueava a seleção do funcionário associado ao usuário.  Realizado uma melhoria que verifica se há filtro por Usuário/Perfil que impossibilita a seleção do funcionário ao Gerar OS. Mais detalhes, verifique a seção **Descrição**. |
| **Conversores e Parâmetros:** | **Filtro por Usuário:** Módulo de Serviços Globais | Segurança | Usuários | Anexos | Filtro por Usuário.  **Filtro por Perfil:** Módulo de Serviços Globais | Segurança | Perfis | Anexos | Filtro por Perfil.  **Gerar OS pelo Atendimento:** No RM Officina acesse Operações | Atendimento | Atendimentos. |
| **Tickets relacionados:** | 3766454. |
| **Requisito:** | MATESTCNTFTOF01-3426. |

## Descrição

Ao Gerar OS, tanto pela tela de Atendimento, quanto pelas outras telas disponíveis, o sistema irá verificar se há filtro por Usuário/Perfil que impossibilita a seleção do funcionário associado ao usuário para a geração da OS.

Caso tenha alguma restrição, as mensagens abaixo serão apresentadas de acordo com o filtro que foi cadastrado.

**Filtro por Usuário**

**Filtro por Perfil**
