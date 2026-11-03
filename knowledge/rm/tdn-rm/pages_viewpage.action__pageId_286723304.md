---
content_hash: 45d8c7890922264a1cdc6e1500f18d474cb2c13800152f252be132370875a986
fetched_at: '2026-06-29T00:08:41.359882+00:00'
page_id: '286723304'
product: rm
source: tdn-rm
title: 1267005 MSAU-13692 DT Ajuste no Formulário de Faturamento de Convênio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286723304
version: 103
---

# Ajuste no Formulário de Faturamento de Convênio

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão de Saúde |
| **Função:** | Faturamento para Convênio |
| **Situação:** | Ao processar um faturamento para convênio, e caso um Honorário fosse uma instituição que não possui número de CBO no cadastro de prestadores, o sistema informava no arquivo XML um número de CBO que não possui relação com os prestadores lançados. |
| **Solução:** | Foram realizados ajustes no formulário para que ao processar a confecção do arquivo XML, seja subustituido o campo que não possui CBO cadastrado,  pelo número 999999, que na nomenclatura da codificação TISS3 significa: - CBO DESCONHECIDO OU NÃO INFORMADO PELO SOLICITANTE |

divs
