---
content_hash: 94d5294cfe716f514c5da069dde0364160a288a1b7cfd05743d12319519a1863
fetched_at: '2026-06-29T00:08:46.215913+00:00'
page_id: '315905536'
product: rm
source: tdn-rm
title: 1146369 MATESTCNTFTOF01-517 DT Código do Bem no Item de Movimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=315905536
version: 105
---

# CÓDIGO DO BEM NO ITEM DE MOVIMENTO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM*.* |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Solicitação de Armazém / Solicitação de Compras | MovMovimentoTBCAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Movimento | MovMovimentoTBCAction | | Parâmetros Tipos de Movimento | RMSParamsWizardAction | | Configurador de Integrações | ConConfiguraIntegracaoAction | | Transformação | ConTransformacaoAction | |
| **Cadastros Iniciais:** | Não se aplica. |
| **Parâmetro(s):** | Configurar o Tipo de Movimento associar o código do bem ao item de movimento. Acesse os Parâmetros Tipos de Movimento, Etapa Manutenção e marque os campos: **Integrado com SigaMNT** e **Integra código do bem SigaMNT ao item de movimento**. |
| **Ponto de Entrada:** | Não se aplica. |
| **Tickets relacionados** | 1146369. |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MATESTCNTFTOF01-517/MATESTCNTFTOF01-1069 |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | SQL Server e Oracle. |
| **Tabelas Utilizadas:** | TTMVEXT - Tipos de movimento  TITMMOV - Itens de Movimento  HCTRANSFORMACAO – Transformação Mensagem Única TOTVS.  HCMAPAINTEGRACAO – Tabela de mapeamento das entidades para cada Integração. |
| **Sistema(s) Operacional(is):** | Windows 7 Service Pack 1 ou superior. |

## Descrição

Considera-se como escopo deste requisito a implementação do adapter de recebimento de Mensagens Únicas TOTVS para integração de Solicitação de Armazém / Solicitação de Compra com informação do Código do Bem, estando o adapter de envio desta mesma mensagem fora do escopo do requisito.

A análise e o desenvolvimento do adapter será efetuado considerando a integração com o Manutenção de Ativos Protheus, mas também viabilizará a integração com outras fontes de dados desde que respeitado o layout da mensagem.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Parâmetros | Alteração | RM \ BackOffice \ Gestão de Estoque, Compras e Faturamento \ Ambiente \ Parâmetros \ Gestão de Estoque, Compras e Faturamento \ Outras Movimentações \ Tipo de Movimento. | - |
| Movimento | Alteração | RM \ BackOffice \ Gestão de Estoque, Compras e Faturamento \ Outras Movimentações | - |
| Configurador de Integração | Alteração | RM \ Integração \ Ferramentas \ Configurar | - |

**Regras de Integridade:**

O Código do Bem será gravado no item de movimento para os movimentos de Ordem de Serviço (OS), Solicitação (SA ou SC) e Baixa de Estoque. Para que a integração considere esta informação serão realizadas as seguintes ações:

* Criar a mensagem única Request versão 1.010 (xsd) e adicionar os campos “EquipmentInternalId” e “EquipmentCode”. Estes campos devem ser  do tipo string e adicionados para item de solicitação.
* Criar a mensagem única MaintenanceOrder versão 1.002 (xsd) e adicionar os campos “EquipmentInternalId” e “EquipmentCode”. Estes campos devem ser  do tipo string e adicionados para item de OS.
* Criar a mensagem única StockTurnOver versão 1.006 (xsd) e adicionar os campos “EquipmentInternalId” e “EquipmentCode”. Estes campos devem ser  do tipo string e adicionados para item de baixa.
* Esta informação deverá ser gravada no campo "CODBEMSIGAMNT" da tabela de Itens de Movimento do RM, somente quando o tipo de movimento estiver configurado para gravar esta informação.
* Atualizar o Configurador de Integração do RM para contemplar esta nova versão da mensagem Request para a Integração Manutenção de Ativos x BackOffice RM.
* Atualizar o cadastro de Transformação do RM para contemplar esta nova versão da mensagem Request.
* Atualizar a Fórmula Visual de Integração da mensagem Request para considerar a versão 1.010.

**Configurador de Integrações**

Será necessário realizar a seguinte atualização no Configurador de Integrações:

1. Projeto de Integração Manutenção de Ativos x BackOffice RM  
   1. Apagar a mensagem REQUEST versão 1.000 caso exista;
   2. Inserir a versão 1.010 da mensagem REQUEST.
   3. Apagar a mensagem MAINTENANCEORDER versão 1.000 caso exista;
   4. Inserir a versão 1.002 da mensagem MAINTENANCEORDER.

**Ponto de atenção:**

* O recebimento da mensagem Request\_ 1.010 do Protheus para o RM contemplará todos os campos enviados na mensagem Request\_1.009 mais a informação da tag EquipmentCode. Os demais campos não serão considerados neste momento.
* O recebimento da mensagem MaintenanceOrder 1.002 do Protheus para o RM contemplará todos os campos enviados na mensagem MaintenanceOrder \_1.000 mais a informação da tag EquipmentCode. Os demais campos não serão considerados neste momento.
* O recebimento da mensagem StockTurnOver 1.006 do Protheus para o RM contemplará todos os campos enviados na mensagem StockTurnOver \_1.002 mais a informação da tag EquipmentCode. Os demais campos não serão considerados neste momento.

**Entidades de Integração**

**Solicitação (SA/SC):**

* Transformação  
  + Identificador da Mensagem: Request
  + Versão: 1\_010
  + Tipo do Server: DataServer
  + DataServer: MovMovimentoTBCData
* Source Code(GUID):
* Fluxo da mensagem: Entrada
* Tipo de Envio: Síncrono.
* Mandatário: Manutenção de Ativos.

**Ordem de Serviço (OS):**

* Transformação  
  + Identificador da Mensagem: MaintenanceOrder
  + Versão: 1\_002
  + Tipo do Server: DataServer
  + DataServer: MovMovimentoTBCData
* Source Code(GUID):
* Fluxo da mensagem: Entrada
* Tipo de Envio: Síncrono.
* Mandatário: Manutenção de Ativos.

**Baixa de Estoque:**

* Transformação  
  + Identificador da Mensagem: StockTurnOver
  + Versão: 1\_006
  + Tipo do Server: DataServer
  + DataServer: MovMovimentoTBCData
* Source Code(GUID):
* Fluxo da mensagem: Entrada / Saída.
* Tipo de Envio: Síncrono.
* Mandatário: Manutenção de Ativos.

## Procedimento para Configuração

**CONFIGURAÇÃO DE INTEGRAÇÃO**

1. No **RM**, acesse **Integração/Mensagem Única/Integrações**. Abra o anexo **Mapeamento de Entidades** e realize as seguintes ações para cada mensagem:
   1. MAINTENANCEORDER: edite o registro, no campo **Eventos**clique sobre o link e ao abrir a janela de **Cadastro de códigos fontes** clique em excluir. Exclua o mapeamento MAINTENANCEORDER 1.000.
   2. REQUEST: edite o registro, no campo **Eventos**clique sobre o link e ao abrir a janela de **Cadastro de códigos fontes** clique em excluir. Exclua o mapeamento REQUEST 1.000.
   3. STOCKTURNOVER: edite o registro, no campo **Eventos**clique sobre o link e ao abrir a janela de **Cadastro de códigos fontes** clique em excluir. Exclua o mapeamento STOCKTURNOVER 1.002.
2. No **RM**, acesse **Integração/Ferramentas/Configurar**.
   1. Na janela **Assistente de Configuração de Integração** avance para a etapa **Configuração do banco de dados** e informe Usuário e Senha para conectar ao banco. Teste a conexão e avance.
   2. Na etapa **Projetos de Integração** selecione o item **Manutenção de Ativos x BackOffice RM**, avance e execute o assistente.
3. No **PROTHEUS**acesse **Configurador (SIGACFG)**, acesse **Ambiente/Schedule/Adapter E.A.I**.   
     
   Crie/Altere o adapter REQUEST conforme dados a seguir:

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| ****Mensagem Única:**** | Sim |
| ****Rotina:**** | NGMUREQUES |
| ****Mensagem:**** | REQUEST |
| ****Envia:**** | Sim |
| **Recebe:** | Sim |
| **Método:** | Síncrono |
| **Operação:** | Todas |
| **Canal Envio:** | EAI |
| **Versão Envio:** | 1.010 |

Crie/Altere o adapter MAINTENANCEORDER conforme dados a seguir:

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| ****Mensagem Única:**** | Sim |
| ****Rotina:**** | NGMUMNTORD |
| ****Mensagem:**** | MAINTENANCEORDER |
| ****Envia:**** | Sim |
| **Recebe:** | Sim |
| **Método:** | Síncrono |
| **Operação:** | Todas |
| **Canal Envio:** | EAI |
| **Versão Envio:** | 1.002 |

Crie/Altere o adapter STOCKTURNOVER conforme dados a seguir:

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| ****Mensagem Única:**** | Sim |
| ****Rotina:**** | NGMUSTOTUO |
| ****Mensagem:**** | STOCKTURNOVER |
| ****Envia:**** | Sim |
| **Recebe:** | Sim |
| **Método:** | Síncrono |
| **Operação:** | Todas |
| **Canal Envio:** | EAI |
| **Versão Envio:** | 1.006 |

divs
