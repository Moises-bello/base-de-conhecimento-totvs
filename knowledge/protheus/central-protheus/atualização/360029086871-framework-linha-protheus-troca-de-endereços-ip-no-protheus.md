---
article_id: 360029086871
category: Atualização
content_hash: eb2295447c50057422e809991e8e9de2f13ea15bf7889f9a75c5d372a92a9eda
fetched_at: '2026-06-28T22:42:21.279731+00:00'
product: protheus
section_id: 360000076747
source: central-protheus
title: Framework - Linha Protheus  - Troca de endereços IP no Protheus
type: support-article
updated_at: '2025-01-22T17:17:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029086871-Framework-Linha-Protheus-Troca-de-endere%C3%A7os-IP-no-Protheus
---

**Dúvida**  
Em quais locais de configuração do Protheus preciso alterar informações de IP quando há mudanças dos mesmos nos servidores?  
  
**Ambiente**  
Protheus - AppServer, Smartclient e DBAccess - Todas as versões  
  
**Solução**  
Existem 3 locais principais que são afetados com trocas de IP de servidores: AppServer, SmartClient e DBAccess.  
  
**AppServer:**  
O arquivo de alterações de configurações do AppServer é o appserver.ini, que fica na pasta do executável do appserver.exe. Neste arquivo, os principais apontamentos de IP de servidores são:  
- Servidor de Licenças, na seção [LICENSESERVER], linha Server=  
- DBAccess (que geralmente fica no mesmo servidor que o Banco de Dados), na seção [DBACCESS], linha Server= (ou na seção do ambiente, na linha DBServer=)  
  
**Smartclient:**  
O arquivo de alterações de configurações do SmartClient é o smartclient.ini, na pasta do executável smartclient.exe. Neste arquivo, o principal apontamento de IP de servidor é:  
- Servidor de Aplicação, na seção [TCP], linha Server=  
  
**DBAccess:**  
O arquivo de alterações de configurações do DBAccess é o dbaccess.ini, que fica na pasta de instalação do DBAccess, com o executável dbaccess.exe (ou dbaccess64.exe). Neste arquivo, o principal apontamento de IP de servidor é:  
- Servidor de Licenças, na seção [General], linha LicenseServer=
