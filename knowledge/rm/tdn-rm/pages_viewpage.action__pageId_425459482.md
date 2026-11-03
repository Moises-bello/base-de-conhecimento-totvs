---
content_hash: c64610d235842b7c6c8bbcdc14c6e29f2f4935be85ed0f70b289a2150c079ec2
fetched_at: '2026-06-29T00:09:36.198759+00:00'
page_id: '425459482'
product: rm
source: tdn-rm
title: Integração Linha RM x Microsoft Dynamics CRM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459482
version: 6
---

**Linha RM x Microsoft Dynamics CRM**

---

**A Integração**

A integração entre a Linha RM com o Microsoft Dynamics CRM (MS CRM) proporciona a sincronização de cadastros e processos através do TOTVS Business Conector (TBC).  
O TBC é o sistema responsável por integrar os dados entre a Linha RM e MS CRM (Versão 4.0 e 2011). Ele verifica os dados no sistema origem, coleta os dados, verifica o sistema destino e atualiza ou cria um novo registro. Dessa forma é possível garantir que os dados entre os sistemas estarão sempre atualizados.  
  O TBC permite a integração de entidades do MS CRM, mesmo as novas entidades customizadas e os novos atributos.   
     
 **Módulos Integrados**

Na Linha RM, foram integrados os módulos: Gestão de Estoques, Compras e Faturamento; Imobiliário; Gestão Financeira; Educacional. Segue os cadastros e processos que integram cada módulo, bem como as Entidades no MS CRM que fazem parte da integração.  
    
   
 ***Notas:***

* *Alguns cadastros existem em mais de um módulo RM. Por exemplo, é possível realizar o cadastro de Cliente/Fornecedor no módulo Gestão Financeira, no módulo Gestão do Relacionamento com o Cliente, etc. Independente em qual módulo seja realizado o cadastro, o mesmo será sincronizado para o MS CRM.*
* *Algumas das entidades apresentadas são criadas no MS CRM durante a configuração e parametrização da integração.*

**Arquitetura**

Utiliza a arquitetura de Conceito para comunicação entre a Linha RM e o MS CRM. A integração faz uso de 28 conceitos para realizar o sincronismo dos dados entre os aplicativos. Os conceitos que devem ser agendados são os que tem como origem a Linha RM. Os demais conceitos são consumidos pelo MS CRM. A comunicação ocorre de duas formas, de acordo com o sentido do fluxo que está sendo processado.  
    
  

* **Linha RM para MS CRM:** Quando o sentido da sincronização dos dados é do RM para o MS CRM a comunicação ocorre através do Agendamento de Conceito.  ***Nota:*** *O agendamento dos conceitos é abordados na parte de Configuração e Parâmetros da Linha RM.*
* **MS CRM para Linha RM:** Referente aos cadastros, o sincronismo do MS CRM para a Linha RM está disponível para as entidades Conta (Cliente/Fornecedor) e Contato.

**Clique nos links abaixo para mais informações desta integração.**

* **Pré-requisitos**
* **Configuração e Parâmetros Linha RM**
* **Configuração e Parâmetros Microsoft Dynamics CRM**
* **Cadastros**
* **Processos**
