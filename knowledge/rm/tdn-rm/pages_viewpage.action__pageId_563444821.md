---
content_hash: 51d8280f9f3bc5c1f51bacb950d88a401c16894cea2724fef64d6e2731c98cf0
fetched_at: '2026-06-29T00:10:50.841369+00:00'
page_id: '563444821'
product: rm
source: tdn-rm
title: DT Consulta situação Solicitação de Armazém/Compras
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=563444821
version: 5
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice    TOTVS Manutenção de Ativos |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão de Estoque, Compras e Faturamento |
| Função: | Consulta Situação do Movimento |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | MATESTCNTFTOF01-8665 |

## **02. SITUAÇÃO/REQUISITO**

Implementação do adapter de integração via Mensagem Única TOTVS para retornar o status do movimento para o Manutenção de Ativos (SigaMNT).Descreva a situação/requisito. 

## **03. SOLUÇÃO**

Considera-se como escopo deste requisito a implementação do adapter de recebimento de Mensagens Únicas TOTVS para integração de consulta status do movimento de Solicitação de Armazém ou Solicitação de Compras vinculados à Ordem de Manutenção que foi integrada ao BackOffice RM, estando o adapter de envio desta mesma mensagem fora do escopo do requisito. 

A análise e o desenvolvimento do adapter será efetuado considerando a integração com o Manutenção de Ativos Protheus, mas também viabilizará a integração com outras fontes de dados desde que respeitado o layout da mensagem.

 

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Configurador de Integração EAI 2.0 | Alteração | RM \ Integração \ EAI 2.0 \ Ferramentas \Configurador | - |
| Diagnóstico de Integração | Alteração | RM \ Integração \ EAI 2.0 \ Ferramentas \ Diagnóstico \ Diagnóstico de Integrações |  |
| Conversor EAI 2.0 | Alteração | RM \ Integração \ Mensagem Única \ Conversor EAI 2 |  |
| Ordem de Serviço | Envolvida | PROTHEUS \ SIGAMNT \ Atualizações \ Controle de Oficina \ Ordem de Serviço \ Corretiva | - |
| Solicitação de Armazém/Solicitação de Compra | Envolvida | PROTHEUS \ SIGAMNT \ Atualizações \ Controle de Oficina \ Ordem de Serviço \ Corretiva \ Incluir OS com insumo tipo Produto | - |

**Tabelas Utilizadas**

* TMOV - Movimentos
* GEAIDEPARA - Tabela de DePara EAI2

**Entidades de Integração**

* Adapter: TraceabilityRequest
* Versão: 2.000
* Fluxo da mensagem: Entrada
* Tipo de Recebimento: Síncrono.

### **Regras de Integridade:**

Ao receber mensagem de Consulta Status do Movimento serão realizadas as seguintes ações:

* Recupera na tabela de De-Para qual é o Identificador do Item de Movimento com base no valor da tag RequestItemInternalId enviado.
* Busca o status do movimento e a quantidade do item para verificar se será permitido prosseguir com a alteração e montar o retorno que será enviado ao Protheus.

O movimento poderá ser alterado pelo Manutenção de Ativos quando o status do movimento for igual a:

* Pendente (A) ou Bloqueado (B) ou Normal (N) ou Não Processado (R). Para estas situações de movimento o no retorno da mensagem o campo Status recebe valor *1* e a Descrição recebe o valor: *Permitido alteração da movimentação.*
* Parcialmente Recebido (G):
  + Nova quantidade do item é maior que a quantidade total já solicitada: altera a quantidade do item acrescentando a diferença entre nova quantidade e quantidade total;
  + Nova quantidade do item é menor que a quantidade total já solicitada:
    - Se a diferença entre quantidade Protheus e Quantidade total é menor que a quantidade: altera a quantidade do item, reduzindo a diferença entre quantidade Protheus e Quantidade Total,

      Exemplo:

      SC gerada com quantidade = 10

      Realizada a compra de 6, Quantidade pendente no RM 4

      OS alterada para quantidade = 7

      Quantidade RM (1) = Quantidade pendente no RM (4) - Diferença entre QTDADE PROTHEUS e QUANTIDADETOTAL (3)
    - Se a diferença entre quantidade Protheus e quantidade total é maior que quantidade já faturada: Não permite a alteração da OS

      Exemplo:

      SC gerada com quantidade = 10

      Realizada a compra de 6, Quantidade pendente no RM 4

      OS alterada para quantidade = 4

      Quantidade RM (-2) = Quantidade pendente no RM (4) - Diferença entre QTDADE PROTHEUS e QUANTIDADETOTAL (6)

      Quantidade não pode ser negativa
    - Se a diferença entre quantidade Protheus e quantidade total é igual à quantidade já faturada: não permite alteração da OS.

      Exemplo:

      SC gerada com quantidade = 10

      Realizada a compra de 6, Quantidade pendente no RM 4

      OS alterada para quantidade = 6

      Quantidade RM (0) = Quantidade pendente no RM (4) - Diferença entre QTDADE PROTHEUS e QUANTIDADETOTAL (4)

Para os demais status de movimento o Status será 0 (zero) e descrição referente ao status respeitará a tabela abaixo:

| Status | Descrição referente ao status |
| --- | --- |
| F | Movimentação não permitida pois o movimento está faturado. |
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
| Type | Tipo da Solicitação |  |  | 000 - Solicitação de Armazém  001 - Solicitação de Compra  002 - Ordem de Manutenção |
| RequestItemInternalId | InterlId do Item de Solicitação | TITMMOV | CODCOLIGADA|IDMOV|NSEQITMMOV |  |
| Quantity | Quantidade a ser alterada | TITMMOV | QUANTIDADE |  |
| **ReturnContentType** | | | | |
| InternalId | InternalId da Solicitação |  |  |  |
| CompanyInternalId | InternalId Empresa |  |  |  |
| CompanyId | Empresa |  |  |  |
| BranchId | Filial |  |  |  |
| Type | Tipo da Solicitação |  |  | 000 - Solicitação de Armazem  001 - Solicitação de Compra  002 - Ordem de Manutenção |
| RequestItemInternalId | Identificador do Item de Solicitação |  |  |  |
| Status | Status de alteração |  |  | 0 - Não é permite alterar movimentação  1- Permite alterar movimentação. |
| Description | Descrição referente ao status |  |  | Será preenchido conforme status do movimento. Consulte a tabela no tópico Regras de Integridade |

## **04. DEMAIS INFORMAÇÕES**

Outras ações/ações relacionadas 

**Este adapter está disponível para utilização apenas no pacote de integração Manutenção de Ativos x BackOffice RM com EAI 2.0IMPORTANTE!**

## **05. ASSUNTOS RELACIONADOS**

* Documento de integração:

div.theme-default .ia-splitter #main {
margin-left: 0px;
}
.ia-fixed-sidebar, .ia-splitter-left {
display: none;
}
#main {
padding-left: 10px;
padding-right: 10px;
overflow-x: hidden;
}
.aui-header-primary .aui-nav, .aui-page-panel {
margin-left: 0px !important;
}
.aui-header-primary .aui-nav {
margin-left: 0px !important;
}
.aui-tabs.horizontal-tabs>.tabs-menu>.menu-item.active-tab a::after {
background: #FF9900; !important
}
.menu-item.active-tab {
border-bottom: none !important;
}
]]>
