---
content_hash: fca575477f5546bad1e8b5ec5437153ca543f7c876b77573f40996e6f4dcc0d8
fetched_at: '2026-06-29T00:08:54.777236+00:00'
page_id: '346492228'
product: rm
source: tdn-rm
title: RMFIN-1629 DT - Parâmetro p/ conclusão manual no controle de glosa via importação
  XML.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=346492228
version: 1
---

# Parâmetro p/ conclusão manual no controle de glosa via importação XML.

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | Parâmetros Gerais |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | RMFIN-1629 |
| **Parâmetro(s):** | Encerramento manual de glosas via Importação de XML de retorno. |
| **Banco(s) de Dados:** | SQL SERVER® e ORACLE® |

## Descrição

Melhoria para que o sistema ao realizar a conciliação de uma conta a partir da importação do XML com do demonstrativo de pagamento, permita manter a conta com status JÁ INICIADA, para que o usuário acesse-a, valide os valores importados e finalize o processo de controle de glosas manualmente.

## Procedimento para Utilização

       1. Na **MDI antiga**, acessar o menu **Opções / Parâmetros / Parâmetros** **Gerais**:

       2. Na aba **Controle e Recurso de Glosas** marcar o parâmetro ***Encerramento manual de glosas via importação de XML de retorno***:

       3.  Na **nova MDI**, acessar **Faturamento / Faturamento para Convênios**, Processos → **Recebimento de Lote Guias/Recurso**:

       4.  Na **MDI Antiga**, acessar **Faturamento / Controle de Glosas**, buscar a fatura, a mesma deverá estar com status **Iniciada**:

       5.   As contas importadas no arquivo de retorno deverão estar com status **Revisar/**Pendente****:

       6.   E com os **registros de glosa** importados do arquivo:
