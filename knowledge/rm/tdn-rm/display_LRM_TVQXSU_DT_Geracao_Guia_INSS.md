---
content_hash: 8cb1d75dda4f3140481ceb7d8bd0f1e0fff02a88d719577519813188213d1fde
fetched_at: '2026-06-29T00:08:17.013130+00:00'
page_id: '249956120'
product: rm
source: tdn-rm
title: TVQXSU_DT_Geracao_Guia_INSS
type: documentation
url: https://tdn.totvs.com/display/LRM/TVQXSU_DT_Geracao_Guia_INSS
version: 112
---

# GUIA DE INSS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Guia de INSS* |
| **Situação/Requisito:** | Quando é gerado a guia de INSS importando autônomos (fluxus ou externo), e é informado a quebra da Seção diferente da quebra de CGC, está retornando o erro abaixo:  ### Processo finalizado com Erros e/ou Avisos. System.Data.ConstraintException: Column 'CODCOLIGADA, IDLAN' is constrained to be unique. Value 'X, XX' is already present. |
| **Solução/Implementação:** | Foi realizada uma validação que informa ao usuário que se o parâmetro de importar autônomos estiver marcado, o código de quebra para a geração da guia INSS deve ser o código de quebra por CGC. |
| **Chamados relacionados:** | TVQXSU |

divs
