---
article_id: 360005090492
category: SIGAEST - PODER DE TERCEIROS
content_hash: 366bfea15ad9a1c599f54e99adf3c88208b70ba468605a4c426a033a4d38d5a8
fetched_at: '2026-06-28T22:39:03.129950+00:00'
product: protheus
section_id: 1500001538881
source: central-protheus
title: MP - SIGAEST - Conceito da Operação Triangular no Protheus
type: support-article
updated_at: '2021-04-28T15:10:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005090492-MP-SIGAEST-Conceito-da-Opera%C3%A7%C3%A3o-Triangular-no-Protheus
---

**Dúvida**Qual o conceito da Operação Triangular no Protheus?  
  
**Ambiente**Protheus – Estoque – A partir da versão 11.80  
  
**Solução**

Operação Triangular consiste em uma transação que envolve mais de 2 empresas para um processo de beneficiamento.

Podemos exemplificar como:

Uma empresa **A**envia um material à empresa **B**para beneficiamento, e esta envia à empresa **C**, que deve efetuar o trabalho e devolver o material diretamente à empresa **A**.

Desta forma, a Nota Fiscal de Remessa para Beneficiamento é enviada da empresa **A** para a empresa **B**, enquanto a Nota Fiscal de Devolução desta mercadoria é enviada pela empresa **C** para a empresa **A**.

É possível fazer este controle no Siga através do parâmetro “**Operação Triangular (S/N)?** “ nas rotinas de Pedido de Venda e Nota Fiscal de Entrada.

Os parâmetro são acessados através da tecla [F12] (na versão DOS, pela tecla [F10]).

Nestes casos, a Nota Fiscal Origem pode ser acessada, pressionando a tecla [F4] sobre o campo “Quantidade”, onde serão apresentadas todas as Notas Fiscais do Produto que envolvem Poder de Terceiros.

Desta forma pode-se dar entrada de uma NF do fornecedor **C** e selecionar a NF de origem do fornecedor **B**.

### EXEMPLO:

**OBS**: Se atentar ao [F12] da rotina MATA410 (Pedido de Venda) no pergunte **Operação Triangular (S/N)?**

Temos três empresas A, B e C.

Inclua o produto TESTE com saldo inicial.

1) Acesse a empresa A e inclua uma NF de SAIDA (NORMAL) para a empresa B (a empresa B deve ser cadastrada como cliente) para o produto TESTE com quantidade = 15 com TES que atualiza estoque e remessa para terceiros **(F4\_ESTOQUE = Sim e F4\_PODER3 = Remessa)**.

2) Acesse a empresa B e inclua uma NF de Entrada NORMAL para o fornecedor A (a empresa B deve ser cadastrada como fornecedor) para o produto TESTE com quantidade = 15 e TES que atualiza ESTOQUE  porém, não controla poder de terceiros **(F4\_ESTOQUE = Sim e F4\_PODER3 = Não Controla)**.

3) Na empresa B, lance a NF de SAIDA – tipo BENEFICIAMENTO do produto TESTE para a fornecedor C, com quantidade = 15, utilizando TES que atualiza estoque e de remessa para terceiro **(F4\_ESTOQUE = Sim e F4\_PODER3 = Remessa).**

4) Acesse a empresa C e inclua uma NF de Entrada NORMAL do fornecedor B (a empresa B deve ser cadastrada como fornecedor) para o produto TESTE com quantidade = 15 e TES que atualiza ESTOQUE com remessa para terceiros **(F4\_ESTOQUE = Sim e F4\_PODER3 = Remessa)**.

5) Acessar a empresa C e lançar uma NF de SAIDA – NORMAL para o cliente A do produto TESTE com quantidade = 15 e TES que atualiza estoque sendo uma devolução para terceiros **(F4\_ESTOQUE = Sim e F4\_PODER3 = Devolução).**

6) Acessar a empresa B e lançar uma NF de ENTRADA - TIPO NORMAL, puxando a NF original da empresa C do produto TESTE com quantidade = 15 e TES que atualiza estoque, sendo devolução para o terceiro **(F4\_ESTOQUE = Sim e F4\_PODER3 = Devolução).**

7) Acessar a empresa B, lance uma NF de SAIDA - NORMAL para a empresa A, com o produto TESTE com quantidade = 15 e atualizando estoque

8) Acessar a empresa A, e lance uma NF de ENTRADA - TIPO BENEFICIAMENTO, puxando a NF original da empresa B do produto TESTE com quantidade = 15 e TES que atualiza estoque sendo devolução para terceiro **(F4\_ESTOQUE = Sim e F4\_PODER3 = Devolução)**.

**RESUMO**

|  |  |  |
| --- | --- | --- |
| **EMPRESA A** | **EMPRESA B** | **EMPRESA C** |
| 1) NF de Saída - Normal para B como REMESSA para 3o. | 2) NF de Entrada – Normal da empresa A. |  |
|  | 3) NF de Saída – tipo BENEFIC. para fornecedor C como REMESSA para 3o. | 4) NF Entrada – Normal do B como REMESSA de 3o. |
|  |  | 5) NF Saída – Normal para A com DEVOLUCAO para 3o. |
|  | 6) NF de Entrada – tipo NORMAL puxando NF original de C com TES de DEVOLUCAO de 3o. |  |
| 8) NF de Entrada – tipo BENEFICIAMENTO puxando NF original de B como DEVOLUCAO de 3o. | 7) NF de Saída – Normal para a A |  |

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Poder de Terceiros no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012199513-SIGAEST-PODER-DE-TERCEIROS)*
