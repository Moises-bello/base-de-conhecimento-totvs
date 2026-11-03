---
content_hash: fda5539d6f4bbb34548dad51869e37e1e09e514afeb31233219bd329b9ea833e
fetched_at: '2026-06-29T00:08:43.050303+00:00'
page_id: '301187563'
product: rm
source: tdn-rm
title: 1423069 FINANCEIRO01-2880 Layout Remessa de Pagamento
type: documentation
url: https://tdn.totvs.com/display/LRM/1423069+FINANCEIRO01-2880+Layout+Remessa+de+Pagamento
version: 96
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção & Projeto |
| **Módulo:** | TOTVS Gestão Financeira. |
| **Função:** | Gerador de Saídas - Layout de Remessa de Pagamento. |
| **Situação/Requisito:** | Ao realizar a edição do layout de Remessa de Pagamento do banco Itaú, está apresentando a seguinte mensagem de erro: “ Uma ou mais colunas abaixo não foram encontradas! Verifique se a coluna existe e se o relacionamento da GLINKSREL está correto. Caso o relacionamento tenha sido alterado, a seleção da coluna deverá ser refeita para que o sistema a interprete corretamente.  FORMAPAGAMENTO (FDADOSPGTO: CODCOLIGADA;CODCOLCFO;CODCFO;IDPGTO)  NUMEROBANCO (FDADOSPGTO: CODCOLIGADA;CODCOLCFO;CODCFO;IDPGTO)  CODIGOAGENCIA (FDADOSPGTO: CODCOLIGADA;CODCOLCFO;CODCFO;IDPGTO) “ |
| **Solução/Implementação:** | Foi realizado o ajuste do layout "FINLAY0021- Pag. Itaú" direto na base do cliente informando novamente os campos que apresentavam problemas na mensagem. Foi feito o ajuste do layout do book também. Após ajuste no layout foi feita uma remessa de pagamento e a mesma foi gerada com sucesso.  O erro ocorria porque os campos apresentados na mensagem perderam o relacionamento, então foi necessário informando novamente os campos no contexto01 do layout com os mesmos nomes apresentados na mensagem de erro.  OBS: Não foi feito nenhum ajuste no código fonte do sistema, apenas ajuste no layout do gerador de saídas. O layout ajustado foi disponibilizado para o cliente e será publicado nas próximas versões e canais de comunicação do cliente. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | Informe o(s) chamado(s) relacionado(s). |
| **Requisito:** | N/A |
|  |  |

divs
