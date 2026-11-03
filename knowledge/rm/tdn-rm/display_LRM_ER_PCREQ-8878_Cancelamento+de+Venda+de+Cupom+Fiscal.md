---
content_hash: 62af6f3fdeafd2aecf8310548724ba9ef3eb45613b061741a9ccf76a71467f1d
fetched_at: '2026-06-29T00:06:23.110747+00:00'
page_id: '223932917'
product: rm
source: tdn-rm
title: ER_PCREQ-8878_Cancelamento de Venda de Cupom Fiscal
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-8878_Cancelamento+de+Venda+de+Cupom+Fiscal
version: 130
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Estoque, Compras e Faturamento | **Módulo** | Faturamento |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | Integração BackOffice RM x PDV Protheus | **IRM1** | PCREQ-7769 |
| **Requisito1** | PCREQ-8878 | **Subtarefa1** | PDR\_CP\_MOV009-103 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.10 | **Réplica** | Não |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 

Implementação do adapter de integração via Mensagem Única TOTVS do Cancelamento de Cupom Fiscal. Este adapter irá viabilizar o recebimento da mensagem de Cancelamento do Cupom Fiscal (Venda e SAT) gerado pelo PDV PROTHEUS.

## Definição da Regra de Negócio

Considera-se como escopo deste requisito a implementação do adapter de recebimento de Mensagens Únicas TOTVS para integração do cancelamento de Cupom Fiscal (Venda e SAT), estando o adapter de envio desta mesma mensagem fora do escopo do requisito.

 

 A análise e o desenvolvimento do adapter será efetuado considerando a integração com o PDV Protheus, mas também viabilizará a integração com outras fontes de dados desde que respeitado o layout da mensagem.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Cupom Fiscal | Alteração | RM \ BackOffice \ Gestão de Estoque, Compras e Faturamento \ Cadastros \ Fiscais\ Mais...\ Cupom Fiscal | - |
| Movimento | Alteração | RM \ BackOffice \ Gestão de Estoque, Compras e Faturamento \ Vendas \ Faturamento \ Movimentação | - |

**Regras de Integridade**

**Inclusão de Cupom Fiscal Cancelado**

Este cenário ocorre quando o cliente desiste da venda ainda no caixa. Para este cenário o PDV deverá enviar ao RM a mensagem RETAILSALES com a tag "IsCanceled" com valor igual a "true". O cupom cancelado será incluído sem a informação de pagamento, ou seja, serão preenchidos somente os dados de Cupom Fiscal e Item de Cupom Fiscal.

**Observação****:** na inclusão do Cupom Fiscal Cancelado não é gerado Movimento para o cupom.

**Item de Cupom Cancelado**

Este cenário ocorre quando o cliente desiste de comprar algum item no momento da venda. Para este cenário o PDV deverá enviar ao RM a mensagem RETAILSALES com a tag "IsCanceled" com valor igual a "true" para o Item de Cupom.

**Observação****:**O movimento gerado para o Cupom irá considerar somente os itens não cancelados.

**Cupom Fiscal Cancelado**

O Cupom Fiscal não pode sofrer alterações além do cancelamento. Sendo assim o PDV irá enviar a mensagem RETAILSALES com a tag "IsCanceled" com valor igual a "true". Após o recebimento da mensagem pelo EAI RM será consumido o DataServer de Cupom Fiscal onde serão preenchidos os dados da classe de parâmetro de Cancelamento de Cupom e realizado a seguinte consistência:

* + O Cupom Fiscal a ser cancelado deve estar cadastrado.

Ao consumir o serviço de Cancelamento do Cupom Fiscal são executados no RM:

* + Cancelamento do Movimento a Partir do Cupom Fiscal
    - Consiste se existe movimento associado ao cupom fiscal.
    - Consiste se o movimento associado ao cupom fiscal está cancelado.
    - Preenche a classe de Cancelamento de Movimento (MovMovCancelamentoPar) com Motivo de Cancelamento igual a "Cancelamento de Cupom Fiscal" e Data Cancelamento igual a data atual do servidor.
    - Executa o serviço de Cancelamento de Movimento.
  + Cancelamento do Cupom Fiscal  
    - Atualiza a coluna CANCELADO da tabela  TCUPOMFISCAL com o valor: 1 - Cupom Cancelado.

**Cupom Fiscal SAT Cancelado**

O Cupom Fiscal do tipo SAT não pode sofrer alterações além do cancelamento. Sendo assim o PDV irá enviar a mensagem RETAILSALES com a tag "IsCanceled" com valor igual a "true".

Após o recebimento da mensagem pelo EAI RM será consumido o DataServer de Cupom Fiscal e quando o Tipo do Cupom for igual a SAT será recuperado o Identificador do Movimento referente ao Cupom SAT. O filtro a ser realizado para buscar o Identificador do Movimento referente ao Cupom SAT na tabela de Movimentos é: Código da Coligada e Chave de Acesso.

Serão preenchidos os dados da classe de parâmetro de Cancelamento de Cupom e consumido o serviço de Cancelamento do Cupom Fiscal.

Ao consumir o serviço de Cancelamento do Cupom Fiscal são executados no RM:

* + Cancelamento do Movimento
    - Consiste se existe movimento associado ao Cupom Fiscal SAT.
    - Consiste se o movimento associado ao cupom fiscal SAT está cancelado.
    - Preenche a classe de Cancelamento de Movimento (MovMovCancelamentoPar) com Motivo de Cancelamento igual a "Cancelamento de Cupom Fiscal", Data Cancelamento igual a data atual do servidor e Id do Movimento com o Identificador do Movimento SAT.
    - Executa o serviço de Cancelamento de Movimento.

**Observação:** Cupom Fiscal SAT está disponível a partir do release 12.1.14.

**Entidades de Integração**

* DataServer envolvido
  + MovCupomFiscalData
* Transformação:
  + Id: RetailSales
  + Versão: 2.009
* SourceCode (Evento)
  + GUID: 1efe6424-027b-44af-8dd3-ef18a527d6b6

**Tabelas Utilizadas**

* TCUPOMFISCAL – Cupom Fiscal
* TCUPOMFISCALITM - Itens de Cupom Fiscal
* TCUPOMFISCALFIN - Pagamentos do Cupom Fiscal
* TMOV - Movimentos
* TITMMOV - Itens de Movimento

## Fluxo do Processo

## Mapeamento de Campos

**Mensagem:**RetailSales 2.009 - mapeamento encontra-se disponível na especificação de .

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
