---
content_hash: 57281ede1c0462b60dbc64e5e624efa40194eb0378a6d638555b64db7989b657
fetched_at: '2026-06-29T00:09:02.267437+00:00'
page_id: '379300170'
product: rm
source: tdn-rm
title: Inconsistências para serem Analisadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=379300170
version: 7
---

| Versão | Problema | Issue | Situação |
| --- | --- | --- | --- |
| 12.1.19 a 12.1.21 | Faturamento direto está com efeito colateral em períodos de reajuste. Ao gerar período de reajuste, e informar faturamento direto, está ocorrendo erro e também ocorre erro de FK ao tentar cancelar o reajuste. | TOPEXECONTROL01-3537 | Ok |
| 12.1.19 | Ao cadastrar um de-para de contrato com 21 caracteres no RM o Protheus trunca em 20 na tabela mas grava de-para com 21, ao abrir anexo de faturamento direto o retorno do Protheus de de-para trava o sistema. |  |  |
| 12.1.19 a 12.1.21 | Faturamento direto não informando no anexo a unidade do produto. |  |  |
| 12.1.19 | Ao incluir o produto de faturamento direto pelo processo de Liberar período a coluna percentual não e calculada, somente se sair da tela e voltar e carregado o percentual corretamente. |  |  |
|  |  |  |  |
|  | REVIEW |  |  |
|  | Avaliar outra coluna de saldo na tela de associação de faturamento. Saldo após a digitação.  Valor Total do Saldo em Negrito. No processo de faturamento Direto.  Avaliar colocar somatório de coluna fixo. Nas telas, resultado dos itens que foram desenvolvidos.  Salvar a configuração de Layout do Processo de Faturamento Direto.  Avaliar inclusão de Nota Fiscal e Cliente Fornecedor nas informações de Produto.  Mudar ordem Coluna de Unidade e Moeda no Grid de Produto Faturado.  Periodo de Reajuste  Criar outro icone Faturamento Direto.  Liberar contrato Insumo para Faturamento Direto.  Mudar o tipo da categoria do Tipo de detalhamento de faturamento direto. Não permitir.  Armando  Criar Historia de EAI 2 teste  Criar Historia equalizar com Nucleus. |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
