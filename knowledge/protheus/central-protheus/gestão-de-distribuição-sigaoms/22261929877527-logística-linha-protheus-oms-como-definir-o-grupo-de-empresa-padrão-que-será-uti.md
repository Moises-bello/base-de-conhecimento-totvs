---
article_id: 22261929877527
category: Gestão de Distribuição (SIGAOMS)
content_hash: 2444d5a9a49c564380fb7036032e46cae621af056ee0f3f78611f52b227def69
fetched_at: '2026-06-28T22:45:49.647040+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Como definir o Grupo de Empresa Padrão que
  será utilizada na integração TOTVS OMS x TOL/TRE
type: support-article
updated_at: '2024-06-07T13:40:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22261929877527-Log%C3%ADstica-Linha-Protheus-OMS-Como-definir-o-Grupo-de-Empresa-Padr%C3%A3o-que-ser%C3%A1-utilizada-na-integra%C3%A7%C3%A3o-TOTVS-OMS-x-TOL-TRE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22261948748695) Tempo aproximado para leitura: **00:01:42 min** **Dúvida**Como definir o **Grupo de Empresa Padrão** que será utilizada na integração **TOTVS OMS x TOL/TRE**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**Para definir o **Grupo de Empresa Padrão** que será utilizada na integração **TOTVS OMS x TOL/TRE**, deverá informar a a *tag* **DefaultCompany** na seção **[NEOLOG]** do arquivo **APPSERVER.INI** do Protheus do **ambiente Web Service.** A *tag* **DefaultCompany** possui os seguintes comportamentos:

Se a *tag* **DefaultCompany Não for informada** no arquivo **APPSERVER.INI**:

1. O ambiente **possue** o cadastro de configuração da Filial com as informações da **Empresa,Unidade de Negócio e Filial**. O elemento do arquivo **XML** irá receber o conteúdo igual a  **EEUUFF-Sequência da integração**. Esse é **conceito de Gestão de Empresas**. Para maiores informações, acesse o *link* indicado logo abaixo no **Saiba Mais.**
2. O ambiente **Não possue** a informação da empresa no *layout* dos campos de Filial das tabelas. Com isso, será enviado o **Grupo de empresas - tabela SM0**,  no qual está sendo enviado o cadastro ou Pedido de Vendas no **TOTVS OMS**. O elemento do arquivo **XML** irá receber o conteúdo igual a  **GrupoFilial-Sequência da integração**

Se a *tag* **DefaultCompany for informada** no arquivo **APPSERVER.INI**:

1. Será enviado apenas o código da Filial.  
   O elemento do arquivo **XML** irá receber o conteúdo igual a **FILIAL-Sequência da integração**

**Exemplo de utilização da Seção NEOLOG:**Configuração integração com o **TOL/TRE**:  
  
**[NEOLOG]**  
DefaultCompany=01  
  
**Saiba mais**   
Mais informações poderão ser acessadas no *link* abaixo:  
[Logística - Linha Protheus - OMS - Integração Protheus TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061123194-Log%C3%ADstica-Linha-Protheus-OMS-Integra%C3%A7%C3%A3o-Protheus-TOTVS-OMS-x-TOL-TRE)  
[Logística - Linha Protheus - OMS - Configurações e documentações para Integração do TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9685990528407-Log%C3%ADstica-Linha-Protheus-OMS-Configura%C3%A7%C3%B5es-e-documenta%C3%A7%C3%B5es-para-Integra%C3%A7%C3%A3o-do-TOTVS-OMS-x-TOL-TRE)  
[Conceito e Criação de Empresas e Filiais](https://tdn.totvs.com/pages/releaseview.action?pageId=271174732)  
  
**Glossário**  
**TOL** - TOTVS Otimização Logística  
**TRE** - TOTVS Roteirização e Entrega  
**TOTVS OMS** - Order Management System  
  
**Anexo**  
Acesse o exemplo de arquivo **Appserver.ini,** com as configurações acima.
