---
content_hash: e48f4aa279ac5bcae2f1823703aa48f5ce0f1c7632184d32f51d8b0ca4b696be
fetched_at: '2026-06-29T00:08:58.009939+00:00'
page_id: '358455115'
product: rm
source: tdn-rm
title: DT Parâmetro "Salvar arquivo de remessa gerado no servidor de aplicação" na
  tela do processo de remessa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=358455115
version: 5
---

# Integração Bancária - Remessa

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Remessa de Cobrança | Integração Bancária - Remessa de Cobrança | | Remessa de Custódia de Cheques | Integração Bancária - Remessa de Custódia de Cheques | | Remessa de Débito Automático | Integração Bancária - Remessa de Débito Automático | | Remessa de Pagamento | Integração Bancária - Remessa de Pagamento | |
| **Cadastros Iniciais:** | Lançamento; Borderô; |
| **Parâmetro(s):** | "Salvar arquivo de remessa gerado no servidor de aplicação" |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-5913> |
| **País(es):** | BRA |
| **Banco(s) de Dados:** | SQLServer;Oracle |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Na tela de processos de remessas bancárias será apresentada o parâmetro "**Salvar arquivo de remessa gerado no servidor de aplicação**". essa opção permite que o usuário altere o caminho onde será salvo o arquivo gerado. Essa flag será carregada por default de acordo com o parâmetro "Permite agendamento da remessa bancária". Caso opte pelo server, será emitido um alerta de que é necessário informar um diretório compartilhado.

## Procedimento para Utilização

       1.            Ao executar qualquer um dos processo de remessa bancária a opção "Salvar arquivo de remessa gerado no servidor de aplicação" será apresentada.

       2.            Marque o parâmetro e execute o processo. Observação: Caso opte salvar o arquivo da remessa no destino server, será necessário informar um diretório compartilhado.
