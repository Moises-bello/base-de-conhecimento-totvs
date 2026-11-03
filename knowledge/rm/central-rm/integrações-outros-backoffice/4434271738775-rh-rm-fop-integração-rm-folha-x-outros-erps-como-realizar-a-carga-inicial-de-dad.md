---
article_id: 4434271738775
category: Integrações Outros BackOffice
content_hash: 499a8f318a26422d2da314e6e3a49c6c87a6a9804e385180ad256d1db07e5b17
fetched_at: '2026-06-28T22:46:42.182959+00:00'
product: rm
section_id: 4410716084503
source: central-rm
title: RH - RM - FOP - Integração RM Folha x Outros Erps, como realizar a carga inicial
  de dados
type: support-article
updated_at: '2025-02-10T17:41:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4434271738775-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Folha-x-Outros-Erps-como-realizar-a-carga-inicial-de-dados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:20 min** **Dúvida**Quando é realizado uma integração do RM Folha de Pagamento com outro ERP via EAI 2.0, é necessário realizar uma carga inicial, por exemplo, enviar todos os funcionário do RM para outro ERP, ou cadastro de funções e etc... Porém como realizar esse procedimento no RM?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir da versão 12.1.28  
  
**Solução**No RM temos a rotina chamada Carga de Dados, ela tem como objetivo sincronizar/enviar todos os cadastros de uma determinada entidade para outro sistema Totvs, como por **exemplo,**enviar todos os funcionário do RM para o Protheus.  
  
Este processo está disponível para a integração com o EAI 2.0, no módulo "Integração | EAI 2.0 | Ferramentas | Carga de Dados" e pode ser acessado pelo usuário que possui permissão de acesso ao menu.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4434256830871/mceclip0.png)  
  
A tela de visualização do processo é composta por 05 (cinco) componentes principais:  
  
![](https://tdn.totvs.com/download/attachments/544210843/03.PNG?version=1&modificationDate=1584991195050&api=v2)

### **1- Aplicativo**

Neste componente, deve-se selecionar qual a aplicação será utilizada para a sincronização das informações com o RM.  
Serão listados todos os aplicativos presentes, que integrem com esse sistema (Protheus, Datasul, ...).

### **2- Lista de pacotes de integração**

Após a seleção do Aplicativo, o componente "02. Lista de Pacotes de Integração" disponibilizará cada um dos Pacotes Instalados que estejam migrados para o EAI 2.0.

![](https://tdn.totvs.com/download/attachments/544210843/04.PNG?version=1&modificationDate=1584992256210&api=v2)  
  
**3- Lista de Adapter's**Selecionado o pacote de integração na etapa anterior, serão listados todos os Adapter's do tipo "Cadastro", que estejam mapeados para este pacote.

![](https://tdn.totvs.com/download/attachments/544210843/05.PNG?version=2&modificationDate=1585023914010&api=v2)

Apenas 01 (um) adapter poderá ser selecionado por vez, ou seja, a carga será realizada apenas para uma única entidade por execução.

### **4- Filtros de itens de entidade**

Com a entidade selecionada, é possível incluir filtros personalizados, utilizando os componentes de filtro presentes em todos os módulos da MDI, para especificar um conjunto de informações conforme as necessidades do usuário.

Pode seguir sem filtro? - Se o filtro não retornar nada? ...

![](https://tdn.totvs.com/download/attachments/544210843/06%20A.PNG?version=1&modificationDate=1584997028187&api=v2)

### **5- Opção de reenvio**

Com esta opção selecionada, serão reenviados todos os itens da entidade selecionada, não apenas os não integrados. Caso o insumo que esteja sendo enviado, com esta opção selecionada, já possua um registro de sincronização, o mesmo será sobrescrito.

Será validado o reenvio apenas dos itens selecionados no filtro personalizado?

![](https://tdn.totvs.com/download/attachments/544210843/06.PNG?version=1&modificationDate=1584999743070&api=v2)  
  
**Saiba mais**

[Maiores informações sobre a Carga Inicial de dados, clique aqui.](https://tdn.totvs.com/display/public/LRM/Carga+de+Dados+EAI+2.0+-+Envio)
