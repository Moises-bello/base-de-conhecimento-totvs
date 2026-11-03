---
content_hash: d71c3dd6178fc88800e90bc7134d22a642aa36926c48cc171758ae53c35d1aea
fetched_at: '2026-06-29T00:09:36.216896+00:00'
page_id: '425459484'
product: rm
source: tdn-rm
title: Backoffice RM x Protheus SigaMNT
type: documentation
url: https://tdn.totvs.com/display/LRM/Backoffice+RM+x+Protheus+SigaMNT
version: 5
---

**Backoffice RM x Protheus SigaMNT**

---

**Backoffice RM**

A Backoffice RM tem o objetivo de gerenciar os cadastros que serão utilizados em processos dentro da Gestão contábil , Financeira , Fiscal, Patrimonial , e de Estoque, Compras e Faturamento. Por ser uma ferramenta de grande eficiência no controle das transações fornecidas por todo o seu módulo, e ser um produto que está adequado a leis e a melhores práticas de processos é muito indicado para auxiliar também em manutenções.  
   
**Protheus SigaMNT**

O módulo  SIGAMNT permite gerenciar  a manutenção feita em bens da empresa, que por ser uma ferramenta muito eficaz que amplia a capacidade de gerenciamento em diversos ambientes industriais, comerciais e de serviços suportando perfeitamente as necessidades frente às manutenções preventivas.  
   
**Integração Backoffice  RM x Protheus SigaMNT**

A integração Backoffice RM x Protheus SigaMNT permite aos clientes gerenciar todo o processo de manutenção de equipamentos, como abertura de ordem de serviço, agendamentos e planos de manutenção, tudo isso aliado aos processos de BackOffice, como baixa de estoque, ordem de compra, solicitação de compra, faturamento de OS entre outros.   
Através da integração os clientes podem usufruir da potencialidade do ERP RM e suas avançadas funcionalidades, comunicando com o módulo de gerenciamento de manutenção de ativos (Backoffice RM x Protheus SigaMNT), de maneira que o módulo de manutenção é dedicado ao propósito CMMS (Sistema Computadorizado de gerenciamento de manutenção), gerando informações necessárias para que as manutenções sejam programadas e planejadas corretamente a fim de gerir a empresa como um todo.  
   
**Comunicação**

A comunicação entre os sistemas ocorre através da utilização de WebServices, que tem o objetivo de enviar e receber as mensagens  em arquivos XML  que contém os dados de cadastros e processos executados na integração entre os sistemas.  
Os cadastros feitos no Backoffice RM  disparam uma mensagem única contendo um XML ao EAI do Protheus SigaMNT, que então fica encarregado de passá-lo às rotinas dos Adapters Protheus. O Adapter Protheus por sua vez, depois de consistir os dados, envia uma mensagem de resposta ao RM confirmando que os dados da mensagem são válidos e só depois disso é feita a persistência dos dados em ambos os Sistemas. O Mesmo ocorre durante a execução dos processos de Gerenciamento de Manutenções do Protheus SigaMNT, porém de forma inversa.  
Para saber mais sobre Mensagem Única, **clique aqui**.

   
**Módulos e Funcionalidades Integrados**

Os módulos e funcionalidades que compõem a integração são:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **RM** |  |  |  |  |
| **RH** | **Projetos** | **BackOffice RM** |  |  |
| **Folha de Pagamento** | **Construção e Projetos** | **Gestão de Estoques, Compras e Faturamento** | **Gestão Patrimonial** |  |
| * Funcionário | * Projeto * Obra * Etapa * Tarefa | * Centro de custo * Cliente/Fornecedor * Condição de Pagamento * Local de Estoque * Moedas * Produto * Unidade de Medida | * Patrimônio |  |

|  |  |
| --- | --- |
| **Protheus SigaMNT** |  |
| **Manutenção de Ativos** | **Gestão de Frotas** |
| * Abertura de Atendimento * Agendamento de O.S por plano de Manutenção * Ampliação Patrimonial * Apropriação de Custos * Baixa de Estoque * Consulta de Saldos e Custos * Contrato de Manutenção * Ordem de Serviço * Ordem de Serviço de Terceiros * Solicitação de Armazém * Solicitação de Compra | * Abastecimento Manual * Análise Técnica de Pneus * Conciliação de Abastecimentos * Geração de Documentos * Gerar Documentos * Honorários de Despachante * Ordem de Serviço de Pneus * Sinistros e Multas * Transferência de Pneus * Sinistros e Multas * Transferência de Pneus |

   
**Clique nos links abaixo para mais informações desta integração.**

* **Pré-requisitos**
* **Configuração e Parâmetros Backoffice RM**
* **Configuração e Parâmetros  Protheus SigaMNT**
* **Cadastros**
* **Processos**
