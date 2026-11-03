---
content_hash: 9dcbff3d44b2b0e412c992c545287b043f71218145d300334d40cb74546fa86a
fetched_at: '2026-06-29T00:11:32.353281+00:00'
page_id: '746514571'
product: rm
source: tdn-rm
title: Senha de Emergência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=746514571
version: 8
---

## Senha de emergência a partir da versão 12.1.2502

A partir desta versão a funcionalidade "Entrar com arquivo existente" foi removido do RM.

IMPORTANTE

Inclusão da Senha Emergência será feita diretamente no servidor de License Server, maiores detalhes [Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=844250371)

## Senha de emergência a partir da versão 12.1.2306

A partir desta versão as funcionalidades de Solicitação de Arquivo de Emergência e Exportação passaram a ser Obsoletas e foram removidas.  
Mantendo apenas o recurso de informar arquivo de Senha de Emergência, botão "Entrar com arquivo existente"

## 

## Processo de solicitação até a versão 12.1.2302

IMPORTANTE

A partir da versão 12.1.2306 as funcionalidades de Solicitação de Arquivo de Emergência e Exportação passaram a ser Obsoletas e foram removidas.

**Objetivo:** Permitir a solicitação da Senha de Emergência  diretamente pelo sistema RM, a partir da versão 11.40.70.

**Desenvolvimento/Procedimento**

São duas formas para realizar o processo de solicitação da Senha de Emergência, conforme enumeradas abaixo.

1. **Solicitação de Senha de Emergência – Tela de aviso Licence Server.**  
     
   Tendo o Licence Server inoperante a visão abaixo será apresentada com as informações de IP e Porta.  
     
     
     
   Clicando em “Solicitar novo arquivo” um Wizard será apresentado para preenchimento de informações necessárias para solicitação da Senha de Emergência.  
     
     
     
   Clique em “Avançar” para escolher qual(is) Empresa(s)/Coligada(s) utilizará(ão) a Senha de Emergência.   
   Clicando no botão “Incluir”, selecione a coligada.  
     
     
     
   Se nenhuma coligada for incluída, não será possível “Avançar”, será exibida a seguinte mensagem; “Selecione pelo menos uma empresa!”. Clique em “Avançar”. Posteriormente será necessário informar o usuário e senha de login no Portal Totvs ([www.suportetotvs.com.br](http://www.suportetotvs.com.br)).  
     
     
     
   Para “Avançar” tela é obrigatório preencher os campos “Usuário” e “Senha”. Depois de feito escolha das coligadas e preenchido os campos de login no Portal Totvs clique no botão “Executar”.  
     
     
     
   Finalizada a execução. O arquivo será gerado e suas informações serão armazenadas diretamente na base de dados. Ao ser interpretado, a liberação das coligadas selecionadas será feita, mediante informações contidas no arquivo. Ao final do processo uma mensagem notifica qual ou quais Empresa(s)/Coligada(s) tiveram êxito na liberação.  
     
     
     

   **2. Solicitação de Senha de Emergência – Tela “Cadastro de Coligadas”.**

        Através da visão de “Cadastro de Coligadas”, após login, selecione o recurso “Serviços Globais”. Guia “Administração / Cadastros”. Ícone “Coligadas”.

        Na visão selecione as Empresa(s)/Coligada(s) que         receberão a Senha de Emergência. Clique no menu “Processos / Solicitar Liberação de Emergência”.

Posteriormente o processo é idêntico ao da Tela do Licence Server, tendo como diferencial a escolha da Empresa(s)/Coligada(s) que é feita antes da apresentação do Wizard.

**Informações Adicionais**

* Este arquivo é gerado a partir de um Web Service da Totvs. Caso este serviço esteja inoperante e/ou alguma informação no processo, como usuário e senha estejam incorretos o arquivo não será gerado.

* Usuários com definição de “Supervisor” não terão restrições para execução deste processo, porém usuários não supervisores dependerão de permissão no recurso “Serviços Globais”.
