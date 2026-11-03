---
content_hash: 083e08fcbf37ad9b1e1455114e205b5983e6e87636fdcfbc22419fb2dcf405dd
fetched_at: '2026-06-29T00:06:20.224475+00:00'
page_id: '221549703'
product: rm
source: tdn-rm
title: ER_Melhorias_Gerar_Contrato_a_partir_de_um_Pedido_de_Compras
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_Melhorias_Gerar_Contrato_a_partir_de_um_Pedido_de_Compras
version: 138
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

# **Melhorias no processo Gerar Contrato a partir de um Pedido de Compras**

**Informações Gerais**

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Estoque, Compras e Faturamento | **Módulo** | Contrato |
| **Segmento Executor** | TOTVS Construção e Projetos | | |
| **Projeto1** | MOV - Projeto de Desenvolvimento 12.1.9 | **IRM1** | PCREQ-6357 |
| **Requisito1** | PCREQ-8870 | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.9 | **Réplica** |  |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos).

### (Obrigatório)

## Objetivo

Implementar as melhorias identificadas no processo Gerar Contrato a partir de um Pedido de compras.

### (Obrigatório)

## Definição da Regra de Negócio

**Agrupamento por Fornecedores**

O processo Gerar Contrato agrupando os itens por Fornecedor passa a considerar os dados de cada movimento não apenas os dados no primeiro movimento computado, assim a informação de cada movimento será copiada para cada item de contrato como por exemplo a condição de pagamento do movimento será copiada para cada item de contrato referente ao seu movimento de origem.

Os campos que serão tratados nesse caso são:

* Local de Estoque (CODLOC)
* Condição de pagamento (CODCPG)
* Representante (CODRPR)
* Comissão do Representante (COMISSAOREPRES)
* Município (CODMUNICIPIOSERV)
* Estado (CODETDMUNSERV)
* Natureza do Movimento(IDNATMOV)
* Tipo de Frete (TIPOFRETE)
* Comprador (CODVEN1)
* Percentual de comissão do Comprador (PERCENTCOMISSAO)

Durante a geração do contrato o sistema verifica se o campo está preenchido no item de movimento e caso positivo o mesmo é copiado para o item de contrato, caso contrario (a informação não esta no item de movimento mas está no movimento) a informação é copiada do movimento de origem para o item de contrato correspondente.

**Unidade de Medida**

O item de contrato passa a ter a informação de unidade de medida. Isso se faz necessário, pois o movimento de origem pode ter itens iguais com unidades distintas ou mesmo agrupar itens de movimentos distintos com unidades diferentes em um mesmo item de contrato.

Nesse caso será criado o campo CODUND na tabela TITMCNT e será realizada a alteração na rotina de faturamento para que o mesmo passe a considerar a unidade de medida do item de contrato na geração de movimentos.

*Consistências:*

* Este campo não será preenchido com nenhum default vindo do cadastro do produto,
* Será filtrado de acordo com a unidade base da unidade de controle do produto selecionado.
* Não será possível alterar o campo CODUND caso o item de contrato seja do tipo medição e tenha alguma medição já faturada.
* Durante o faturamento de um item de contrato serão feitas as mesmas consistências que já são realizadas pelo serviço do movimento.

**Exclusão de Contrato Gerado a partir de um pedido**

Será possível excluir um contato criado a partir de um pedido de compras que ainda não sofreu nenhum faturamento.

* O serviço de exclusão do contrato irá realizar todas a(s) movimentações(s) de estoque e orçamento necessárias e o retorno do status do movimento para pendente.
* No caso de exclusão de itens de contrato será realizado o tratamento para não permitir que os itens vinculados a pedidos de compra sejam excluídos.

**Orçamento**

Será removida a restrição de parametrização para o movimento que será utilizado para gerar contrato. Com isto também serão realizados os tratamentos necessários para que o a rotina de geração de contratos copie os dados do item de orçamento para os itens de contrato.

 - Ao gerar o contrato a partir de um pedido o orçamento do movimento em questão será desfeito, e só afetará no contrato se o usuário informar um tipo de contrato que afete o orçamento e faça os devidos ajustes no contrato para que isto ocorra.

**Rastreabilidade de Contratos Gerados a partir de um pedido**

Será adicionado na tela de rastreabilidade do movimento uma aba para que sejam apresentados os dados dos contratos gerados a partir do movimento. Semelhante ao que já existe para a Cotação.

***Tabelas Utilizadas***

* *TITMCNT – Cadastro de Itens de Contrato*
* *TITMCNTMOVRELAC - Relacionamento de itens de movimento e itens de contrato*  

  |  |  |  |  |
  | --- | --- | --- | --- |
  | **Rotinas** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
  | Gerar Contrato a partir do Pedido de Compra | Agrupar itens por Fornecedor | [Movimentos -> Processo -> Gerar Contrato] | - |
  | Manutenção de Contratos | Criação do campo Unidade na edição dos itens de contrato | [Contratos -> Manutenção de Contratos] | - |
  | Rastreamento do Contrato | Rastrear os contratos gerados a partir do pedido de compras | [Movimentos -> Processo -> Rastreamento de Movimentos] | - |

### Opcional

## Protótipo de Tela

**Protótipo 01 - Alteração de Unidade**

**Protótipo 02 - Tela de Rastreamento de movimentos**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
