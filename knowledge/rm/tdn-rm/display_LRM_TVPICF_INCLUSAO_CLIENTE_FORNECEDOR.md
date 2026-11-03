---
content_hash: 551d20b24bec4c34b91fcb07dfcf4881f0db17b973c4d88c8ce65094f3083cdb
fetched_at: '2026-06-29T00:08:16.858622+00:00'
page_id: '248581090'
product: rm
source: tdn-rm
title: TVPICF_INCLUSAO_CLIENTE_FORNECEDOR
type: documentation
url: https://tdn.totvs.com/display/LRM/TVPICF_INCLUSAO_CLIENTE_FORNECEDOR
version: 103
---

# INCLUSÃO DE CLIENTE FORNECEDOR ATRAVÉS DO CADASTRO DE FUNCIONÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Inclusão de Cli/For Através de funcionário* |
| **Situação/Requisito:** | Ao editar o cadastro de um funcionário e acessar o menu Processos -> Inclusão de Cliente/Fornecedor para realizar a inclusão do cliente fornecedor na aba Banco Pgto/Financeiro do cadastro do funcionário é apresentado o seguinte erro:    Não foi possível executar o processo corretamente:  String or binary data would be truncated. |
| **Solução/Implementação:** | *O sistema estava utilizando a descrição do Município como o código do município e como a descrição possuía mais de 20 caracteres o erro era apresentado, foi ajustado o campo código de município para que o sistema utilizasse o código ao invés da descrição para a correta inserção.* |
| **Chamados relacionados:** | TVPICF |

divs
