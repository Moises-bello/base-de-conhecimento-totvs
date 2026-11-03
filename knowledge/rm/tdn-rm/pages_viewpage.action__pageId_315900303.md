---
content_hash: 7e74734877375ed4f0fe6e0f7e03c02d45eeae14cd7c0dcaac7ede1442eb7e17
fetched_at: '2026-06-29T00:08:45.831381+00:00'
page_id: '315900303'
product: rm
source: tdn-rm
title: FOPROTINAS01-2265 Adequações na GRRF Referentes à Reforma Trabalhista
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=315900303
version: 95
---

# INCLUSÃO DO TIPO DE MOVIMENTAÇÃO 'I5' E CÓDIGO DE SAQUE DE FGTS '07'

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | GRRF |
| **Situação/Requisito:** | No dia  , a Caixa Econômica Federal emitiu a circular 789/2017, referente às alterações no SEFIP e GRRF decorrentes da Reforma Trabalhista (lei 13.467/2017). As alterações estão descritas na versão 5 do Manual de Orientações Recolhimentos Mensais e Rescisórios ao FGTS e das Contribuições Sociais. Dentre as mudanças geradas na GRRF, é necessária a adequação do relatório para contemplar o novo tipo de movimentação 'I5' e código de saque do FGTS '07', ambos com descrição 'Rescisão do contrato de trabalho por acordo entre trabalhador e empregador'. |
| **Solução/Implementação:** | Para que as modificações sejam efetivas, é necessária a execução de um script. Há três casos distintos:  1. Clientes que estão em versões anteriores a 12.1.17 vão executar os scripts da Reforma Trabalhista durante a conversão para 12.1.17 ou 12.1.18    2. Clientes que estão na 12.1.17 ou 12.1.18 e ainda não executaram o script da Reforma Trabalhista, vão somente executar o script da reforma já disponibilizado   3. Clientes que estão na 12.1.17 e 12.1.18 e que já executaram o script da reforma trabalhista terão que executar somente script com a marcação LB.2017.11\_06 separadamente (que já está disponibilizada junto ao patch das versões, basta acessar o RM.Script.Executor)    Após execução do script, o novo código de saque do FGTS '07' estará disponível para seleção no cadastro de rescisão, aba 'Rescisão', no lookup 'Código de Saque':      Além disso, ao cadastrar uma rescisão com o tipo 'V - Comum acordo' para um funcionário e gerar a GRRF para ele, o código da movimentação informado será 'I5 - Rescisão do contrato de trabalho por acordo entre trabalhador e empregador':      Log de execução da GRRF:      Arquivo GRRF.RE: |
| **Tickets relacionados:** | - |

divs
