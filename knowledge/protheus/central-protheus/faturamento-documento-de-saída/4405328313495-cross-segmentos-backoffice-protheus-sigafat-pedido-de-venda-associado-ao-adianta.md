---
article_id: 4405328313495
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: a8916ad8168a0d63f06bbec297a2b8b02199c843d4a8aa79857777fa15d0d0fd
fetched_at: '2026-06-28T22:38:44.109817+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Pedido de venda associado
  ao Adiantamento
type: support-article
updated_at: '2024-11-28T20:03:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405328313495-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Pedido-de-venda-associado-ao-Adiantamento
---

**Dúvida**Ao preparar o documento de saída do pedido de venda associado ao adiantamento apresenta a mensagem: "Foram encontrado(s) pedido(s) usando condição de pagamento associado com 'Adiantamento', porém sem nenhum Adiantamento associado. Deseja selecionar agora o(s) Adiantamento(s)?", como resolver?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da versão 12.

**Causa 1**

O problema é devido ao tamanho dos campos "Fil. Origem (FIE\_FILROG)" e "Fil.Orig (FR3\_FILGORI)"

**Solução da causa 1**

* Aplique [pacote acumulado Financeiro e](https://tdn.totvs.com/x/HrCmHw)[pacote acumulado Faturamento](https://tdn.totvs.com/x/Iw4dHw), depois rode o UPDDISTR com arquivo sdf de dicionário contido no acumulados;

OBSERVAÇÃO: No modo UPDDISTR, atualize dicionário um por vez não faça atualização dos módulos junto vai ocorrer de sobrepor a atualização.

**Causa 2**

O pedido de venda com adiantamento foi gerado a partir do módulo de Exportação (SIGAEEC ou SIGAEIC)

**Solução da causa 2**

Quando o pedido de venda precisar ter adiantamento e ele foi gerado pelo módulo de exportação, a condição de pagamento do exportação que deve possuir o adiantamento "Adiant. (E4\_CTRADT) = SIM".

A condição de pagamento colocada no pedido de venda "Cond. Pagto (C5\_CONDPAG)" gerado, nesse caso não deve possuir o CAMPO "Adiant. (E4\_CTRADT) = NÃO", após ter sido gerado do módulo de exportação.

**Causa 3**

Numeração "Numero (C5\_NUM)" do pedido de venda errada.

**Solução da causa 3**

Ajuste no configurador, pelo License Server () a numeraçõa da tabela SC5. Pois se ela estiver desconfigurada, a numeração que ele está sugerido pode ser de um pedido de venda anterior no qual tinha condiçõa de pagamento que exigia adiantamento.

Assim, ele pode pedir o adiantamento mesmo sem estar definido na condição de pagamento, por conta da numeração "Numero (C5\_NUM)" errada.

**Causa 4**

Simplesmente falta vincular um adiantamento que deseja usar.

**Solução da causa 4**

* Altere o pedido de venda
* Vá em outras ações > "Adiantam."
* Vincule o adiantamento

**Saiba mais:**

[FAT0149 - Recebimento Antecipado (RA/Adiantamento) no Pedido de Venda (MATA410)](https://tdn.totvs.com/x/GkD2Dw)
