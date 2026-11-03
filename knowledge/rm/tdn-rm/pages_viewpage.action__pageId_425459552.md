---
content_hash: c0613f6fa7384de81ed8d7dc0914df79f817084d9adf37cff7d26839800cff5f
fetched_at: '2026-06-29T00:09:37.005007+00:00'
page_id: '425459552'
product: rm
source: tdn-rm
title: Backoffice RM x Protheus SigaMNT - Configurações Protheus SigaMNT
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459552
version: 15
---

**Backoffice RM x Protheus SigaMNT - Configurações Protheus SigaMNT**

---

**Configuração de Grupo de Empresas no Protheus**   
    
 O Protheus deve utilizar grupo de empresas para refletir a hierarquia de empresas configurada no BackOffice RM, contendo somente um grupo e  a divisão de empresas sendo representada pelo respectivo conjunto "empresa" +" unidade".  
    
 **Exemplo:**

|  |  |  |  |
| --- | --- | --- | --- |
| **Grupo de Empresas** | **Empresa** | **Unidade de Negócio** | **Filial** |
| 01 | 01 | 010 | 01 |
| 01 | 01 | 010 | 02 |
| 01 | 02 | 010 | 01 |
| 01 | 02 | 020 | 01 |

**Configuração de compartilhamento de cadastros entre Empresas e Filiais.**

**1**.   Para o funcionamento da Integração Linha RM x Protheus SigaMNT é necessária a configuração  de compartilhamento de registros  nas tabelas do Protheus SigaMNT.  
 **2**.   Para configurar o compartilhamento   acesse : Protheus  SigaCFG  
 **3**.   Acesse : Base de dados  / Dicionário de Dados  / Base de Dados / Empresa / Dicionário de Dados.  
 **4**.   Pesquise pela tabela   e a configure  conforme especificado na tabela abaixo.

|  |  |  |  |
| --- | --- | --- | --- |
| **Entidade** | **Empresa** | **Filial** | **Tabela Protheus** |
| Currency | Compartilhado | Compartilhado | CTO |
| UnitOfMeasure | Compartilhado | Compartilhado | SAH |
| CostCenter | Exclusivo | Compartilhado | CTT |
| Project | Exclusivo | Exclusivo | AF8 |
| SubProject | Exclusivo | Exclusivo | AFC |
| TaskProject | Exclusivo | Exclusivo | AF9 |
| StepProject | Exclusivo | Exclusivo | AFC |
| PaymentCondition | Exclusivo | Compartilhado | SE4 |
| Item | Exclusivo | Compartilhado | SB1 |
| CustomerVendor | Exclusivo | Compartilhado | SA1 (Cliente)    SA2 (Fornecedor) |
| Assets | Exclusivo | Exclusivo | SN1 |
| Employee | Exclusivo | Compartilhado | SRA | SRF | SR3 | SR7 |
| Warehouse | Exclusivo | Exclusivo | NNR |
| FinancialNature | Exclusivo | Compartilhado | SED |

**5**. Clique em atualizar base de dados para salvar as alterações.

**Observações :**  
   
**1**: Independentemente se for utilizado produto global no RM, a tabela referente no Protheus deve ser exclusiva por empresa, ficando a cargo do RM replicar os produtos globais para cada filial no Protheus.  
**2**: Mesmo que a empresa não utilize Cliente/Fornecedor global no RM, deve-se compartilhar a tabela referente no Protheus por empresa. Será enviado concatenado ao código do cliente/fornecedor o código da coligada, conforme a mascara "\[CODCOLIGADA\]|\[CODCFO\]".  
  
Executar o Programa U\_UPDPMS no SmartClient Protheus\*

**1**: Executar o programa U\_UPDPMS  
**2**: Executar o programa Protheus Smart Client informando U\_UPDPMS ao campo Starting Program .   
**3**: Clique em Sim , para confirmar a mensagem de execução do programa.   
**4**: Após a finalização do processamento verificar se a data gerada é superior a 19/09/2012.  
   
Alterar o Dicionário de Dados - inicializar os campos SA\_COD de Cliente e Fornecedor

**1**: Acessar o Protheus , Módulo SigaCFG.  
**2**: Acessar : Base de dados / Dicionário / Bases de Dados.  
**3**: Acessar : Empresas / Dicionario de dados.  
**4**: Pesquisar por SA1.  
**5**: Selecione a tabela e clique em Editar.  
**6**: Acesse : Clientes / Campos.  
**7**: Pesquisar pelo campo código do cliente (A1\_COD).  
**8**: Selecionar o campo A1\_COD e clicar no ícone Editar.  
**9**: Informar o valor GETSXENUM("SA1", "A1\_COD") ao campo Inic.Padrão localizado na aba Opções e Confirmar.  
**10**: Pesquisar pela Tabela SA2.  
**11**: selecionar a Tabela e clicar no ícone Editar .  
**12**: Acessar: Fornecedores / Campos .   
**13**: Selecionar o campo A2\_COD e clicar em Editar .  
**14**: Informar o valor GETSXENUM("SA2", "A2\_COD") ao campo Inic.Padrão localizado na aba Opções e Confirmar.

Alterar o Dicionário de Dados - inicializar os campos SA\_LOJA de Cliente e Fornecedor

**1**: Acessar o Protheus , Módulo SigaCFG  
**2**: Acessar: Base de dados / Dicionário / Bases de Dados.  
**3**: Acessar: Empresas / Dicionario de dados.  
**4**: Pesquisar por SA1 . Selecione a tabela e clique em editar.  
**5**: Clique em Editar.  
**6**: Acesse : Clientes / Campos.  
**7**: Pesquisar pelo campo do cliente (A1\_LOJA).  
**8**: Selecionar o campo A1\_LOJA e clicar no ícone Editar.  
9: Informar o valor "01" (As aspas são necessárias) ao campo Inic.Padrão localizado na aba Opções e Confirmar.  
**10**: Pesquisar pela Tabela SA2.  
**11**: Selecionar a Tabela e clicar no ícone Editar.  
**12**: Acessar: Fornecedores / Campos .  
**13**: Selecionar o campo A2\_Loja e clicar em Editar.  
**14**: Informar o valor "01" (As aspas são necessárias) ao campo Inic.Padrão localizado na aba Opções e Confirmar.   
   
Criação de Calendário Default.

**1**: Acessar o Protheus , Módulo SigaMNT.  
**2**: Acessar: Base Atualizações / Cadastros Básicos / Calendários.  
**3**: Incluir um novo calendário.  
**4**: Informar o código 001 ao calendário para que ele seja referenciado e selecionar os horários.

**Observação:**

A seleção de horas é replicada aos outros dias da semana . O projeto utiliza somente uma referência a este calendário, não importando os horários marcados.  
   
Cadastro de rotinas dos Adapters Protheus SigaCFG

**1**: Acessar : Ambiente / Schedule / Adapter E.a.I.

**2**: Incluir uma nova Rotina para os adapters do sistema Protheus

**3**: Configurar a Rotina do Adapter de acordo com os dados abaixo fornecidos e que já foram pré estabelecidos na aplicação do patch de atualização do Protheus :

* Mensagem única: Sim
* Rotina: Nome do adapter  com a ultima letra  referenciando o programa (A)
* Mensagem: Nome da mensagem única  que o Adapter EAI  espera receber.
* Descrição: Identificação da mensagem
* Recebe: SIM
* Método: Síncrono
* Operação: TODAS
* Canal de Envio  : EAI

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **MENSAGEM** **ÚNICA** | **ROTINA** **PROTHEUS** | **MENSAGEM** | **DESCRIÇÃO** | **ENVIA** | **RECEBE** | **METODO** **PROTHEUS** | **OPERAÇÃO** | **CANAL DE** **ENVIO** | **ADAPTER****PROTHEUS** |
| SIM | CTBA140 | Currency | Moeda | NÃO | SIM | SÍNCRONO | TODAS | EAI | CTBI140 |
| SIM | QIEA030 | UnitOfMeasure | Unidade de Medida | NÃO | SIM | SÍNCRONO | TODAS | EAI | QIEI030 |
| SIM | CTBA030 | CostCenter | Centro de Custos | NÃO | SIM | SÍNCRONO | TODAS | EAI | CTBI030 |
| SIM | MATA360 | PaymentCondition | Condição de Pagamento | NÃO | SIM | SÍNCRONO | TODAS | EAI | MATI360 |
| SIM | MATA010 | Item | Produto | NÃO | SIM | SÍNCRONO | TODAS | EAI | MATI010 |
| SIM | MATA030 | CustomerVendor | Cliente | NÃO | SIM | SÍNCRONO | TODAS | EAI | MATI030 |
| SIM | MATA020 | CustomerVendor | Fornecedor | NÃO | SIM | SÍNCRONO | TODAS | EAI | MATI020 |
| SIM | PMSA200 | Project | Projeto | NÃO | SIM | SÍNCRONO | TODAS | EAI | PMSI200 |
| SIM | PMSA201A | StepProject | Etapa (EDT) | NÃO | SIM | SÍNCRONO | TODAS | EAI | PMSI201 |
| SIM | PMSA201 | SubProject | Obra (EDT) | NÃO | SIM | SÍNCRONO | TODAS | EAI | PMSI201 |
| SIM | PMSA203 | TaskProject | Tarefa | NÃO | SIM | SÍNCRONO | TODAS | EAI | PMSI203 |
| SIM | ATFA010 | Assets | Ativo Fixo | NÃO | SIM | SÍNCRONO | TODAS | EAI | ATFI010 |
| SIM | GPEA010 | Employee | Funcionário | NÃO | SIM | SÍNCRONO | TODAS | EAI | GPEI010 |
| SIM | AGRA045 | Warehouse | Local de Estoque | NÃO | SIM | SÍNCRONO | TODAS | EAI | AGRI045 |
| SIM | NGMUMNTSUP | MaintenanceSupplyContract | Contrato de Fornecimento | SIM | SIM | SÍNCRONO | TODAS | EAI |  |
| SIM | NGMUVALVEN | ValidateCustomerVendor | Validação de Inadimplência | SIM | SIM | SÍNCRONO | TODAS | EAI |  |

**Configuração do De-Para  para  as Empresas e Filiais**

O cadastro de Empresas e Filiais deve  ser feito manualmente no PROTHEUS, atraves da funcionalidade "De-Para".

**1**.Para  cadastrar o De-Para  das Empresas  e Filiais no Protheus acesse : Protheus / SigaCFG / Ambiente / Schedule / Emp.fil Msg. Unica

**2**. Incluir um novo registro

**3**. Preencher os campos conforme  os valores a seguir  :

* **Referência**: RM
* **Company :** Código da Coligada RM  a integrar.
* **Branch:** Código da Filial RM a integrar
* **Emp. Protheus:** Código da Empresa no Protheus a integrar com o sistema RM
* **Fil. Protheus:** Código da Filial no Protheus  a integrar com o sistema  RM

**Exemplo :**   
    
 **Referência**: RM  
 **Company :** 4  
 **Branch:** 20  
 **Emp. Protheus:** 01  
 **Fil. Protheus:** 0101005

---

---

**Recursos Adicionais**

**TDN - Boletins Técnicos :**

[Atualização de Dicionario de Dados Protheus campo edt tarefa.pdf](http://tdn.totvs.com/download/attachments/76251246/BT+-+Atualiza%c3%a7%c3%a3o+de+Dicionario+de+Dados+Protheus++campo+edt+tarefa.pdf?version=1&modificationDate=1380032000000)

[Alterar dicionario de dados SA\_LOJA de cliente e fornecedor.pdf](http://tdn.totvs.com/download/attachments/76251246/BT+-+Alterar+dicionario+de+dados++SA_LOJA+de+cliente++e+fornecedor.pdf?version=1&modificationDate=1380031999000)

[Criacao de calendario protheus de projeto , obra etapa tarefa.pdf](http://tdn.totvs.com/download/attachments/76251246/BT+-+Criacao+de++calendario+protheus++de++projeto+%2c+obra+etapa+tarefa.pdf?version=1&modificationDate=1380031998000)

[Executar a Rotina U\_UPDPMS.pdf](http://tdn.totvs.com/download/attachments/76251246/BT+-++U_UPDPMS.pdf?version=1&modificationDate=1380031998000)

[Alterar dicionario de dados SA\_COD de cliente e fornecedor.pdf](http://tdn.totvs.com/download/attachments/76251246/BT+-+Alterar+dicionario+de+dados++SA_COD+de+cliente++e+fornecedor.pdf?version=1&modificationDate=1380031998000)

[Cadastro das Rotinas dos Adapters Protheus.pdf](http://tdn.totvs.com/download/attachments/76251246/BT+-+Cadastro+das+Rotinas+dos+Adapters+Protheus.pdf?version=1&modificationDate=1380031994000)

[Cadastro das Rotinas dos Adapters Protheus.pdf](http://tdn.totvs.com/download/attachments/76251246/BT+-+Cadastro+das+Rotinas+dos+Adapters+Protheus.pdf?version=1&modificationDate=1380031994000)

[Atualização de todo o dicionário de dados da empresa Protheus.pdf](http://tdn.totvs.com/download/attachments/76251246/BT+-+Atualiza%c3%a7%c3%a3o+de+todo++o+dicion%c3%a1rio+de+dados+da+empresa+Protheus.pdf?version=1&modificationDate=1380031993000)

[Normalizar Base de Dados Protheus .pdf](http://tdn.totvs.com/download/attachments/76251246/Normalizar+Base+de+Dados+Protheus+.pdf?version=1&modificationDate=1380036776000)
