---
content_hash: cbc157b5f17b5c5284e80f7f742fdfdfe0a653306050fbdf9a36d5d06b46a15e
fetched_at: '2026-06-29T00:05:52.815817+00:00'
page_id: '1060235154'
product: rm
source: tdn-rm
title: Solução de conflitos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1060235154
version: 5
---

# **Índice**

---

3Índice

# **Introdução**

---

O objetivo desta página é apresentar como funciona o mecanismo de classificação de ambiente, identificação de conflito e inconsistência entre as informações encontradas na integração RM x SmartLink, referentes ao banco de dados e classificação de ambiente.

# **Funcionamento**

---

Quando um usuário com privilégio de supervisor executa o login via MDI, são realizadas validações de consistência, caso alguma inconsistência seja detectada, o usuário deverá confirmar a classificação do ambiente.

A tela de classificação de ambiente também pode ser exibida pelo menu Tipo de Ambiente.

Para mais informações, *acesse a documentação: **[Tela de classificação de ambiente](https://tdn.totvs.com/x/ysAmO)***.

# **Tipos de Inconsistência**

---

### **01 - Quando a Classificação do Ambiente não foi definida no RM**

* **Será apresentada a tela abaixo para que o usuário confirme a finalidade correta do sistema.**  
  Após a confirmação a classificação selecionada será gravada, todos os dados de configuração do Smartlink serão removidos e o endereço da Base de Dados apresentado na tela será confirmado para integração com o Smartlink.

### **02 - Quando for identificado que houve alguma atualização na integração com o SmartLink**

* **Será apresentada a tela abaixo para que o usuário confirme os dados e selecione novamente a classificação do ambiente.**  
  Após a confirmação existem dois cenários:
  + **Quando a classificação é alterada:**  
    Neste caso, todos os dados de configuração do Smartlink serão removidos e o endereço da Base de Dados apresentado na tela será confirmado para integração com o Smartlink.
  + **Quando a classificação do ambiente é mantida, ou seja, é confirmada a mesma Classificação apresentada junto do Endereço da Base de Dados:**  
    O Wizard do Credential Helper poderá ser aberto e apresentado ao usuário para que um novo ambiente seja integrado. O Wizard poderá decidir conforme as configurações do License Server se as credenciais serão geradas no momento sendo necessáro aguardar, ou se serão geradas por uma tarefa automática.   
    Mais informações em:

### **03 - Quando o endereço da Base de Dados utilizada pela integração com o SmartLink está diferente da utilizada pelo RM**

* **Será apresentada a tela para que o usuário confirme o Endereço e Classificação antigos e selecione um novo.**  
  Após a confirmação, podem existir dois cenários:
  + **Quando a classificação é alterada:**  
    Neste caso, todos os dados de configuração do Smartlink serão removidos e o endereço **Novo** da Base de Dados apresentado na tela será confirmado para integração.
  + **Quando a classificação do ambiente é mantida, ou seja, é confirmada a mesma Classificação apresentada junto do Endereço Antigo da Base de Dados:**  
    Neste caso podem existir outros dois cenários:
    - **Quando for identificado que houve alguma atualização na integração com o Smartlink:**  
      Wizard do Credential Helper poderá ser aberto e apresentado ao usuário para que um novo ambiente seja integrado.
    - **Caso contrário:**  
      As configurações do Smartlink serão removidas e o endereço **Novo** da Base de Dados apresentado na tela será confirmado para integração.

Importante

Em ambientes com vários servidores, ou até mesmo quando existem mais hosts em uma máquina sendo executados, é importante que exista uma padronização nas configurações de banco de dados feitas no *Alias Manager:*

É necessário utilizar a mesma configuração de servidor e banco de dados para todos os hosts de um ambiente, ou seja, utilizar o **mesmo** DNS ou IP para identificar o servidor da base de dados e sua instância. Isto evitará que o sistema entenda que cada host está configurado para um banco de dados diferente, evitando possíveis inconsistências, como as listadas acima.
