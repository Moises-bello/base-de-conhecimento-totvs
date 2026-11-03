---
content_hash: e6a685ac7202d86218a1814b36f81b2fd24d016cfeee8a5ec025f4b704407aa2
fetched_at: '2026-06-29T00:09:04.102141+00:00'
page_id: '382549508'
product: rm
source: tdn-rm
title: 2978208 DEDUINTEGRACOES-2529 DT Permissão de edição do default contábil da
  bolsa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=382549508
version: 3
---

# PERMISSÃO DE EDIÇÃO DO DEFAULT CONTÁBIL DA BOLSA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Gestão Educacional. |
| **Função:** | Cadastro de default contábil da bolsa. |
| **Situação/Requisito:** | Está sendo possível editar o cadastro de default contábil da bolsa mesmo sem permissão de alteração dos campos da tela no perfil do usuário. |
| **Solução/Implementação:** | Por padrão as permissões (inclusão, edição, exclusão) dos default's contábeis no sistema estão relacionadas à permissão de edição do cadastrado principal vinculado ao default contábil. Desta forma, a permissão do default contábil da bolsa está relacionada à permissão de edição do cadastro de bolsa. Se o perfil do usuário não tiver permissão de editar a bolsa. O usuário não terá permissão para incluir, editar ou excluir  o default contábil da bolsa.  O default contábil do serviço também tem esse mesmo comportamento.  Já na matriz aplicada as permissões  (inclusão, edição, exclusão) dos default's contábeis estão relacionadas às respectivas permissões de (inclusão, edição e exclusão) do cadastro de matriz aplicada. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | N/A. |
| **Documento de Referência:** | N/A. |
| **Pacote:** | Informe o [linkdopacote] |
