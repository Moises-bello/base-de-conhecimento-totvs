---
content_hash: 2da1134ff2086a85b578b2143e5866f2a17758293ecd744d4435837454c77325
fetched_at: '2026-06-29T00:09:37.223266+00:00'
page_id: '425459577'
product: rm
source: tdn-rm
title: Backoffice RM x Protheus SigaMNT - Configuração e Parâmetros Linha RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459577
version: 4
---

**Configuração e Parâmetros Linha RM**

---

**Configurador**  
    
 O configurador é uma funcionalidade que gera a integração, cria o mapeamento das entidades, a transformação das mensagens únicas e está incluído no instalador do ERP RM.   
    
 O Assistente de  Configuração tem o objetivo de  criar a conexão que integrará os módulos Backofice RM e Protheus SigaMNT.   
    
 Durante o processo, são inseridas as credenciais para conexão ao banco de dados em que as informações do Linha RM estão gravadas, e  selecionada a integração responsável por conectar os dois sistemas.

  Para executar o configurador acesse: RM / Integração / Ferramenta / Configurar

**1**. Clique em avançar, insira um Usuário e Senha com permissão de acesso ao banco de dados utilizado ao conectar ao sistema RM.

**2**. Após o preenchimento dos dados de conexão, clicar em Testar para validar a conexão com o banco. Em seguida clique no botão Avançar.

**3**. Selecionar a integração TOTVS Manutenção de Ativos x BackOffice RM. Após clique em Avançar, e em Executar.

**Configurando o Web Service da Mensagem Única**  
    
 Para que a integração conecte os sistemas é necessário que seja informado o endereço de Webservice do Protheus SigaMNT e as suas credenciais de autenticação.

**1**.   Para isso acesse: RM / Integração / Integração / Mensagem Padrão / Integrações.  
 **2**.   Selecione a integração TOTVS Manutenção de Ativos x BackOffice RM e edite o registro.  
 **3**.   Preencha os campos:

* + Url Web Service: Endereço que identifica o local onde o Webservice está instalado.
  + Usuário Autenticação: usuário com permissão de acesso ao Webservice.
  + Senha Autenticação: Senha de acesso ao Webservice.

**4**.   Selecionar o check Box Ativo  
 **5**.   Salve as modificações realizadas.  
    
 **Importar Fórmulas Visuais**  
    
 O configurador cria o mapeamento das entidades que serão utilizadas na integração BackOffice RM x Protheus SigaMNT automaticamente , sendo necessário apenas importar as fórmulas visuais , com seus respectivos gatilhos, para que quando ocorra algum evento de inserção , alteração ou exclusão de cadastros ou processos os dados sejam importados entre o BackOffice RM e Protheus SigaMNT.

**1**. Para importar as fórmulas visuais acesse : Integração / Mensagem Única / Integrações.  
 **2**. Selecione a integração Manutenção de Ativos x BackOffice RM e acesse : Anexos / Mapeamento de Entidades.  
 **3**. Para verificar as entidades mapeadas, acesse: Anexos / Mapeamento de Entidades .  
    
 As entidades mapeadas são :  
     
 **Cadastros:**

|  |  |
| --- | --- |
| **Entidade** | **Versão** |
| CustomerVendor | 2.002 |
| Currency | 2.000 |
| UnitOfMeasure | 2.000 |
| Item | 2.000 |
| CostCenter | 2.000 |
| Assets | 1.001 |
| Employee | 2.001 |
| Project | 2.000 |
| SubProject | 2.000 |
| TaskProject | 2.000 |
| StepProject | 2.000 |
| PaymentCondition | 2.000 |
| Company | 1.000 |
| Branch | 2.000 |
| Warehouse | 1.000 |

**Processos**

|  |  |
| --- | --- |
| **Entidade** | **Versão** |
| Request | 1.000 |
| CancelRequest | 1.000 |
| CancelMaintenanceOrder | 1.000 |
| StockTurnover | 1.000 |
| StockTurnover | 1.000 |
| StockLevel | 1.000 |
| AppointmentCost | 1.000 |
| MaintenanceOrder | 1.000 |
| MaintenanceOrder | 1.000 |
| AssetsValuation | 1.000 |
| Order (Pedido de Compra) | 3.002 |
| Order (Pedido de Pagamento) | 3.002 |
| InfoOfParcelvalues | 1.000 |

**Outros**

|  |  |
| --- | --- |
| **Fórmula Visual** | **Versão** |
| InternalId | 1.000 |
| Request | 1.000 |

**4**.  Selecione a integração Manutenção de Ativos x BackOffice RM e acesse : Processos / Configurações Gerais.  
 **5**.  Clique em Avançar.  
 **6**.  A tela permite que novas entidades sejam adicionadas a configuração geral da integração selecionada. Clique em Avançar.  
 **7**.  Clique em Importar Fórmula Visual.  
 **8**.  Clique em Adicionar Objetos e selecione as mensagens únicas das entidades mapeadas.  
 **9**.  Após adicionar as fórmulas visuais acessar a aba Parâmetros e marcar o checkbox Iportar Gatilhos para cada uma das fórmulas inseridas. Clique em executar.  
 **10**. Clique em Fechar.  
 **11**. Clique em Avançar.  
 **12**. Clique em executar.  
    
 **Cadastro do De-Para Manual  no Sistema RM para as Coligadas**  
    
 O cadastro de Coligada devera ser feito manualmente no RM e no PROTHEUS, atraves da funcionalidade "De-Para".

Acesse  : RM / Integração / Integração  / Mensagem Única / De-Para.

1. Inlcuir um novo registro
2. Para criar o De-Para  , preencher os campos  conforme especificado a seguir:

* **Tabela RM:** GCOLIGADA
* **Chave Primária RM:** CODCOLIGADA
* **Valor Chave Primária RM:**  Valor do Código  da Coligada no RM
* **Sistema Integrado:** PROTHEUS
* **Valor Chave Integração:**  Valor do Código da Coligada no RM

**Exemplo :**   
    
 **Tabela RM:** GCOLIGADA  **Chave Primária RM:** CODCOLIGADA **Valor Chave Primária RM:**  1 **Sistema Integrado:** PROTHEUS **Valor Chave Integração:**  1  
     
 **Cadastro do De-Para Manual no Sistema RM para as Filiais**  
    
 O cadastro de  Filial devera ser feito manualmente no RM e no PROTHEUS, atraves da funcionalidade "De-Para".

1. Acesse : RM / Integração / Integração / Mensagem Única / De-Para.
2. Inlcuir um novo registro
3. Para criar o De-Para , preencher os campos conforme especificado a seguir:

* **Tabela RM:** GFILIAL
* **Chave Primária RM:** CODCOLIGADA|CODFILIAL   (Ficar atento ao caracter **PIPE  ,** localizado ao lado esquerdo da letra Z no Teclado **)**
* **Valor Chave Primária RM:** Valor do Código da Coligada no RM  **PIPE** Valor do código  da Filial no RM
* **Sistema Integrado:** PROTHEUS
* **Valor Chave Integração:** Valor do Código da Coligada no  sistema Protheus **PIPE** Valor do código da Filial no sistema Protheus

**Exemplo :**  
  
**Tabela RM:** GFILIAL  
**Chave Primária RM:** CODCOLIGADA|CODFILIAL   
**Valor Chave Primária RM:** 1|30 **Sistema Integrado:** PROTHEUS **Valor Chave Integração:** 01|14  
  
**Observações :**

* Devido a restrições no EAI, o RM.Host.Service.exe não deve ser executado na lista de serviços ativos do Windows, pois estão ocorrendo erros de acesso a arquivos e DLLs das extensions. Para que não ocorra erros é necessário executar o RM.Host.exe.
* Outro ponto importante é que o configurador do RM não atualiza os mapeamentos de entidades e as transformações que já estão incluídas e são alteradas posteriormente. Para atualizar será necessário excluir o mapeamento ou a transformação desejado e executar o configurador novamente.
* Para que  o envio dos processos  de manutenção sejam enviados  do Protheus SigaMNT ao Linha RM, pode  ser necessária a desativação de autenticação do Webservice, gerado ao instalar o produto TOTVS Business Connect.

Saiba mais sobre **Configuração do Tipo de Movimento**.  
    
 Para mais detalhes sobre as configurações do sistema RM, acesse o Boletim Técnico.

---

**Recursos Adicionais**

###### **TDN - Boletim Técnico :** [Ativar integração Linha RM x Protheus SigaMNT.pdf](http://tdn.totvs.com/download/attachments/76251244/BT+-+Ativa%c3%a7%c3%a3o+da+integra%c3%a7%c3%a3o++Backoffice+RM+x+Protheus+SigaMNT.pdf?version=1&modificationDate=1380031597000)

###### **TDN - Boletim Técnico :** [Configurar URL do WebService Protheus no Sistema RM.pdf](http://tdn.totvs.com/download/attachments/76251244/BT+-++Ajuste+de+URL++de+Integra%c3%a7%c3%a3o+RM.pdf?version=1&modificationDate=1380031599000)

###### **TDN - Boletim Técnico :** [Importar Fórmulas Visuais no sistema RM.pdf](http://tdn.totvs.com/download/attachments/76251244/BT+-Importa%c3%a7%c3%a3o+das+f%c3%b3rmulas+visuais.pdf?version=1&modificationDate=1380031598000)

**TDN - Boletim Técnico** : [**De-Para Coligada e Filial.pdf**](http://tdn.totvs.com/download/attachments/76251244/DE+PARA+Coligada+e+Filial.pdf?version=1&modificationDate=1380203109664)
