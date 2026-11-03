---
content_hash: 97a2084e403e2d3748a2722c064c1d5bc7d1ad239a2c6e99b62f0620ac19ef88
fetched_at: '2026-06-29T00:08:35.545884+00:00'
page_id: '281261214'
product: rm
source: tdn-rm
title: Consulta situação Solicitação de Armazém/Solicitação de Compras
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=281261214
version: 12
---

# INTEGRAÇÃO SIGAMNT - CRIAÇÃO DE SERVIÇO E MENSAGEM ÚNICA PARA RETORNAR STATUS DO MOVIMENTO

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM. | | |
| **Segmento Executor:** | Construção e Projetos. | | |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Consulta Situação do Movimento | TraceAbilityRequestAdapter\_1.001*.* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Ordem de Manutenção (OS) | MaintenanceOrder. | | Solicitação de Armazém (SA) | Request. | | Solicitação de Compras (SC) | Request*.* | | Configurador de Integração | ConConfiguraIntegracaoAction. | | | |
| **Chamado/Ticket:** | 438515. | | |
| **Requisito/Story/Issue:** | MATESTCNTFTOF01-246/MATESTCNTFTOF01-327. | | |
| **País:** | ( X ) Brasil  (  ) Argentina  (  ) México  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colômbia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros:** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos>.* | | |

### Objetivo

 

Implementação do adapter de integração via Mensagem Única TOTVS para retornar o status do movimento para o Manutenção de Ativos (SigaMNT).

### Definição da Regra de Negócio

Considera-se como escopo deste requisito a implementação do adapter de recebimento de Mensagens Únicas TOTVS para integração de consulta status do movimento de Solicitação de Armazém ou Solicitação de Compras vinculados à Ordem de Manutenção que foi integrada ao BackOffice RM, estando o adapter de envio desta mesma mensagem fora do escopo do requisito. 

 

 A análise e o desenvolvimento do adapter será efetuado considerando a integração com o Manutenção de Ativos Protheus, mas também viabilizará a integração com outras fontes de dados desde que respeitado o layout da mensagem.

 

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Configurador de Integração | Alteração | RM \ Integração \ Ferramentas \ Configurar | - |
| Ordem de Serviço | Envolvida | PROTHEUS \ SIGAMNT \ Atualizações \ Controle de Oficina \ Ordem de Serviço \ Corretiva | - |
| Solicitação de Armazém/Solicitação de Compra | Envolvida | PROTHEUS \ SIGAMNT \ Atualizações \ Controle de Oficina \ Ordem de Serviço \ Corretiva \ Incluir OS com insumo tipo Produto | - |

**Tabelas Utilizadas**

* TMOV - Movimentos
* HCINTEGRACAOID - Tabela de-para dos identificadores de cada integração

**Entidades de Integração**

* Transformação  
  + Id: TraceAbilityRequest
  + Versão: 1\_001
* Custom Adapter (GUID): 4291dd00-72a8-4781-abd3-579e814fb1ec
* Fluxo da mensagem: Entrada
* Tipo de Recebimento: Síncrono.

### **Regras de Integridade:**

Ao receber mensagem de Consulta Status do Movimento serão realizadas as seguintes ações:

* Aplica-se a transformação do XSLT de Entrada.
* Recupera na tabela de De-Para qual é o Identificador do Movimento com base no InternalId enviado.
* Busca o status do movimento para montar o retorno que será enviado ao Protheus.

O movimento poderá ser alterado pelo Manutenção de Ativos quando o status do movimento for igual a: Pendente (A) ou Bloqueado (B) ou Normal (N) ou Não Processado (R). Para estas situações de movimento o no retorno da mensagem o campo Status recebe valor *1* e a Descrição recebe o valor: *Permitido alteração da movimentação.*

Para os demais status de movimento o Status será 0 (zero) e descrição referente ao status respeitará a tabela abaixo:

| Status | Descrição referente ao status |
| --- | --- |
| F | Movimentação não permitida pois o movimento está faturado. |
| G | Movimentação não permitida pois o movimento está parcialmente faturado. |
| P | Movimentação não permitida pois o movimento está parcialmente quitado. |
| Q | Movimentação não permitida pois o movimento está faturado. |
| C | Movimentação não permitida pois o movimento está cancelado. |
| D | Movimentação não permitida pois o movimento está com status de perda. |
| I | Movimentação não permitida pois o movimento está inativo. |
| U | Movimentação não permitida pois o movimento está em faturamento. |
| O | Movimentação não permitida pois o movimento está em orçamento. |
| Z | Movimentação não permitida pois o movimento está terminado. |

#### Tabela De-Para da mensagem TraceAbilityRequest

| Mensagem Única | | RM | | Observação |
| --- | --- | --- | --- | --- |
| **Elemento** | **Descrição** | **Tabela** | **Campo** |
| **BusinessContentType** | | | | |
| InternalId | InternalId da Solicitação | TMOV | CODCOLIGADA|IDMOV | O adapter RM irá usar a informação desta tag para buscar o Identificador do Movimento na tabela de De-Para. |
| CompanyInternalId | InternalId Empresa |  |  |  |
| CompanyId | Empresa |  |  |  |
| BranchId | Filial |  |  |  |
| Type | Tipo da Solicitação |  |  | 000 - Solicitação de Armazem  001 - Solicitação de Compra  002 - Ordem de Manutenção |
| **ReturnContentType** | | | | |
| InternalId | InternalId da Solicitação |  |  |  |
| CompanyInternalId | InternalId Empresa |  |  |  |
| CompanyId | Empresa |  |  |  |
| BranchId | Filial |  |  |  |
| Status | Status de alteração |  |  | 0 - Não é permite alterar movimentação  1- Permite alterar movimentação. |
| Description | Descrição referente ao status |  |  | Será preenchido conforme status do movimento.Consulte a tabela no tópico Regras de Integridade |
| Type | Tipo da Solicitação |  |  | 000 - Solicitação de Armazem  001 - Solicitação de Compra  002 - Ordem de Manutenção |

## Procedimento para Configuração

**CONFIGURAÇÃO DE INTEGRAÇÃO**

1. No **RM**, acesse **Integração/Ferramentas/Configurar**.
   1. Na janela **Assistente de Configuração de Integração** avance para a etapa **Configuração do banco de dados** e informe Usuário e Senha para conectar ao banco. Teste a conexão e avance.
   2. Na etapa **Projetos de Integração** selecione o item **Manutenção de Ativos x BackOffice RM**, avance e execute o assistente.
2. No **PROTHEUS** acesse **Configurador (SIGACFG)**, acesse **Ambiente/Schedule/Adapter E.A.I** . Crie o adapter TRACEABILITYREQUEST conforme dados a seguir:

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| **Mensagem Única:** | Sim |
| **Rotina:** | NGMUTRAREQ |
| **Mensagem:** | TRACEABILITYREQUEST |
| **Envia:** | Sim |
| **Recebe:** | Não |
| **Método:** | Síncrono |
| **Operação:** | 1 - Todas |
| **Canal Envio:** | EAI |
| **Versão Envio:** | 1.001 |

## **Procedimento para Utilização**

1. No  **Manutenção de Ativos** cadastrar uma O.S. com status liberado possuindo um insumo do tipo produto como previsto.
2. No **BackOffice RM** baixar (faturar a S.A.) que foi gerada para a O.S.
3. No  **Manutenção de Ativos** editar a O.S. criada e deletar o insumo do tipo produto.
