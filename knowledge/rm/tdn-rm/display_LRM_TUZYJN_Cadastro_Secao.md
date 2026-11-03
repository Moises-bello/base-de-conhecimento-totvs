---
content_hash: 8377a772f8e58af3754eaaad55539490c1dd41fc02dd2aff6a54c5e831d51107
fetched_at: '2026-06-29T00:08:09.370848+00:00'
page_id: '239034831'
product: rm
source: tdn-rm
title: TUZYJN_Cadastro_Secao
type: documentation
url: https://tdn.totvs.com/display/LRM/TUZYJN_Cadastro_Secao
version: 119
---

# CADASTRO DE SEÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Cadastro de Seção |
| **Situação/Requisito:** | Ao realizar o cadastro de uma nova seção, o sistema não está preenchendo o código pai da seção, sendo realizado o preenchimento apenas através do processo "Manutenção do cadastro de Seções". |
| **Solução/Implementação:** | Alteração na validação responsável pelo preenchimento do código pai. O nome da tabela não era verificado corretamente com letras maiúsculas. |
| **Chamados relacionados:** | TUZYJN |

divs
