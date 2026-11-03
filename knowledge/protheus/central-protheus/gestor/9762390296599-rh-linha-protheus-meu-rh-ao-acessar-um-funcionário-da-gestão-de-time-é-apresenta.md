---
article_id: 9762390296599
category: GESTOR
content_hash: 0fe2667bfdf79528e0563f8593f0245ce73ff355a0046e6aa8d3c0bfe03469c6
fetched_at: '2026-06-28T22:44:35.532403+00:00'
product: protheus
section_id: 10299702833303
source: central-protheus
title: RH - Linha Protheus - MEU RH - Ao acessar um funcionário da Gestão de Time
  é apresentada mensagem "Você está tentando acessar dados de um funcionário que não
  faz parte do seu time"
type: support-article
updated_at: '2026-06-19T17:26:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9762390296599-RH-Linha-Protheus-MEU-RH-Ao-acessar-um-funcion%C3%A1rio-da-Gest%C3%A3o-de-Time-%C3%A9-apresentada-mensagem-Voc%C3%AA-est%C3%A1-tentando-acessar-dados-de-um-funcion%C3%A1rio-que-n%C3%A3o-faz-parte-do-seu-time
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30647676429847) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Ao acessar um **funcionário** da **Gestão de Time** é apresentada mensagem "**Você está tentando acessar dados de um funcionário que não faz parte do seu time**" e não carrega as informações do funcionário em tela, como no exemplo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9761676965399)  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**Esta mensagem indica sempre uma inconsistência no Cadastro e/ou Configuração da Hierarquia entre os Departamentos envolvidos. Para garantir a correção desta mensagem, deve:  
 **1.  Garantir** a **atualização** do ambiente com o pacote de **Expedição Contínua do RH** mais recente, conforme disponível aqui: **[Expedição Contínua Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854)**

**2.  Verificar** o preenchimento dos **campos "Niv Inicial"** e **"Nivs. Aprovac"** de **todos os itens de Menu**, do módulo **SIGATCF**, disponível em **Atualizações -> Configurações -> Menus**, Menu de código **000006**, **Outras Ações -> Menu**. Os campos citados **não podem estar sem preenchimento**

**3.  Validar** o cadastro de **Hierarquia** entre os **departamentos**, se estão respeitando a premissa existente **[aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7917580297623)**. **\*Obs:** Importante verificar principalmente o relacionamento entre os campos de **"Matrícula Responsável"** e **"Departamento Superior"**, onde **uma matrícula** **NÃO** pode estar como **responsável pelo próprio Departamento** em que ela se encontra. **Saiba Mais****[RH - Linha Protheus - MEU RH - Aprenda sobre o MEU RH e como fazer a implantação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036164214)  
[CLIQUE AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)[para acessar mais artigos e FAQs sobre o MEU RH](%20https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[CLIQUE AQUI](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)[para acessar a documentação de referência sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)**
