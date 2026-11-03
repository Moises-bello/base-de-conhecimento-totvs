---
content_hash: 01d2494f587ac3209120331c004d13558ee0a392d8e72c8a9baf26c06360c00e
fetched_at: '2026-06-29T00:08:22.352767+00:00'
page_id: '269427729'
product: rm
source: tdn-rm
title: MRH-2767_DT_INCLUSAO_FUNCIONARIO_WEBSERVICE
type: documentation
url: https://tdn.totvs.com/display/LRM/MRH-2767_DT_INCLUSAO_FUNCIONARIO_WEBSERVICE
version: 116
---

# INCLUSÃO DE FUNCIONÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Inclusão de Funcionário* |
| **Situação/Requisito:** | *Ao tentar incluir um funcionário via webservices, com o parâmetro de geração automática de chapa ativado, o sistema exibia mensagem de erro dizendo não ser possível o campo CHAPA ser nulo* |
| **Solução/Implementação:** | *A validação e geração automática da chapa conforme parametrização foi adicionada ao dataserver. Quando parametrizado para gerar a chapa automaticamente, a tag CHAPA deve ser enviada vazia no XML.* |
| **Chamados relacionados:** | MRH-2767 |

divs
