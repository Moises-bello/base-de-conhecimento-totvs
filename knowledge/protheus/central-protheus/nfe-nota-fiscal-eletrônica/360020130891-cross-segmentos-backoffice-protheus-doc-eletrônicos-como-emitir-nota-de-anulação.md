---
article_id: 360020130891
category: NFe - Nota Fiscal Eletrônica
content_hash: b5d8e31d7c644e363cedb51a92ba9bf576094a888b558ea055aa876c0f4b2cf7
fetched_at: '2026-06-28T22:40:01.653968+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como emitir nota
  de anulação de frete'
type: support-article
updated_at: '2023-12-14T19:49:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020130891--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-emitir-nota-de-anula%C3%A7%C3%A3o-de-frete
---

**Dúvida**Como emitir nota de anulação de frete?   
Como corrigir a rejeição 321 para nota de anulação de frete?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

* O CTE deve ter sido lançado na rotina MATA103 (Tipo Normal) e com formulário próprio igual NÃO com espécie igual CTE
* Se tiver lançado pela MATA116 (de forma a atribuir o valor ao custo médio do produto) é necessário Excluir por essa mesma rotina (estornando assim o custo), e lançar o CTE pela MATA103 - Documento de Entrada

* Criar um produto novo chamado "FRETE" para lançar a entrada

* Gerar um Pedido de venda (MATA410) do tipo Devolução (obs: incluir o Pedido manualmente, e não na opção de retorno) nesse pedido deve ser com espécie SPED e deve referenciar o CTe que deseja anular pelos campos **NF Ori, Serie Ori e Item NF. Ori.**

* Informar no campo Fornecedor a Entidade registrada com os dados do emitente do CTE

* No grid, informar o produto "FRETE" registrado no CTE de entrada (e não o produto da nota de origem de entrada)

* Registrar Quantidade 1 e TES que não movimenta estoque

* Utilizar o CFOP 5206 – Anulação de valor relativo a aquisição de serviço de transporte

* **Registrar este CFOP no parâmetro MV\_DEVCFOP para esta operação. Caso seja operação Interestadual informar o CFOP 6206**.

* Faturar o pedido e efetuar a transmissão
