---
content_hash: c855d028841c3084ef883c4edd88ca0c7968a949953b3492722f2ce857b63ba0
fetched_at: '2026-06-29T00:08:22.406119+00:00'
page_id: '269432340'
product: rm
source: tdn-rm
title: Integração com PDV PROTHEUS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269432340
version: 6
---

# INTEGRAÇÃO COM PDV PROTHEUS / INTEGRAÇÃO PDV

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM. | | |
| ****Segmento Executor:**** | Construção e Projetos | | |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Configuração da Integração*.* | ConConfiguraIntegracaoAction. | | Cancelar Movimento | MovCancelMovProcAction. | | | |
| **Chamado:** | Não se aplica. | | |
| **Requisito (ISSUE):** | CPMOV001-841*.* | | |
| **País:** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros:** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos>.* | | |

## Objetivo

 

Não permitir que o usuário cancele um movimento de Cupom Fiscal SAT gerado pelo PDV Protheus.

Emitir ao usuário um aviso sobre a disponibilidade do novo modelo de integração existente entre PDV Protheus x BackOffice RM.

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Configuração da Integração | Alteração | Integração \ Ferramentas \ Configurar | - |
| Movimento | Envolvido | Gestão de Estoque, Compras e Faturamento \ Outras Movimentações | - |
| Cancelar Movimento | Alteração | Gestão de Estoque, Compras e Faturamento \ Outras Movimentações \ Processos | - |

### Configurador de Integração

Quando o usuário executar o processo de Configurar Integração será emitido um aviso sobre a disponibilidade do novo modelo de integração existente entre TOTVS PDV Protheus x BackOffice RM. Os possíveis cenários são:

1. **Configurador de Integração sem nenhuma integração**  
   Neste caso será apresentada a integração atinga **BackOffice RM x SigaLoja Protheus.** Caso o usuário selecione esta opção será apresentada mensagem ao usuário e não será permitido a execução do configurador.
2. **Configurador de Integração com modelo antigo ativado**

   Neste caso será apresentada a integração atinga **BackOffice RM x SigaLoja Protheus.**Caso o usuário selecione esta opção será apresentada mensagem ao usuário e será permitido a execução do configurador.
3. **Configurador de Integração com modelo novo ativado**

   Neste caso não será apresentada a integração atinga **BackOffice RM x SigaLoja Protheus.** Será apresentado somente a opção do novo modelo de integração **BackOffice RM x PDV Protheus (Novo Modelo)** e será permidio a execução do configurador.

### Movimento

Na integração entre TOTVS PDV x BackOffice RM, quando for incluído um Movimento de Cupom Fiscal tipo SAT gerado pelo TOTVS PDV, este movimento não poderá ser cancelado no BackOffice. Caso o usuário execute o processo de cancelar este movimento, será apresentado uma mensagem de consistência não permitindo o cancelamento deste movimento.

O cancelamento deverá ser realizado no TOTVS PDV, que irá cancelar o movimento no RM através da mensagem única recebida.

A regra que será utilizada para identificar se o movimento é referente a Cupom SAT gerado pelo TOTVS PDV será:

* Movimento deve possuir Número do Cupom informado;
* Movimento deve possuir Ponto de Venda informado;
* Movimento deve possuir Contador de Reinicio de Operação informado (CRO);
* Tipo de Documento utilizado no movimento deve ser igual a SAT ou NFC-e;
* Deve existir um registro na Tabela De-Para de integrações para a Coligada | Identificador do Movimento que está sendo cancelado.

**Tabelas Utilizadas**

* HCPARAMETROS – Parâmetros do RM Conector.
* HCINTEGRACAOID – Tabela de-para dos identificadores de cada integração.
* TMOV– Movimentos.

## Procedimento para Utilização

**Configurador de Integração**

1. Acesse **RM \ Integração \ Ferramentas \ Configurar**  
   O sistema apresenta a janela de Assistente de Configuração da Integração.
2. Avance e no passo Configuração de banco de dados informe o Usuário e Senha do banco de dados e teste a conexão.  
   O sistema apresenta mensagem com status da conexão. Avance para o próximo passo.
3. No passo Projetos de Integração selecione a Integração BackOffice RM x SigaLoja Protheus e avance.  
   O sistema apresenta mensagem ao usuário informando sobre a existência do novo modelo de integração.
4. Confira os dados e confirme.
