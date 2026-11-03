---
article_id: 10084286582679
category: Gestão de Transportes (TMS)
content_hash: 52cba1ebcc63b0011fea2a70efb6d14a87742d739fdc6baa2a2fc25429a81887
fetched_at: '2026-06-28T22:45:33.499906+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Wizard para integração do TMS com TSS
type: support-article
updated_at: '2022-11-08T19:37:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10084286582679-Log%C3%ADstica-Linha-Protheus-TMS-Wizard-para-integra%C3%A7%C3%A3o-do-TMS-com-TSS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:20 min** **Dúvida**Qual o procedimento de configuração do **Wizard** para integração do **TMS** com **TSS** para emissão de **CT-e** e **MDF-e**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) -  Todas as versões  
  
**Solução**Para que seja possível efetuar a transmissão de documentos como **CT-e** e **MDF-e** é necessário integrar o **TMS** com o **TSS**.  
  
A integração entre os produtos deve ser efetuada pela rotina **Cte Sefaz - SPEDCTE**, localizada no módulo **TMS - Miscelanea - Simulado**. Essa rotina tem como objetivo ajudá-lo na configuração da integração do **Protheus** com o **TSS**.  
  
Siga os procedimentos abaixo para essa integração:

* Acessar a rotina **Cte Sefaz - SPEDCTE.** Será apresentada uma tela para escolher qual modelo de transmissão deseja configurar, tendo como opções **1 - CT-e** e **2 - MDF-e;**

**![Sem_t_tulo.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10086988110487)**

* Selecionando o modelo de transmissão desejado, será aberto o **Wizard,** clique em **Avançar;**
* Na tela a seguir, informe a **URL** do servidor do **TSS**. Deve ser informado **servidor:porta**, conforme demonstra imagem abaixo. Essa informação está disponível também no **appserver.ini** do seu **TSS**:

![Screenshot_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10086987923223)

![Screenshot_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10086987927831)

* Após, deverá ser preenchido os dados referente ao ser certificado digital, como tipo do certificado, diretório onde ele está localizado e senha do certificado:

![Screenshot_3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10086987980823)

* Caso tenha informado todos os dados corretamente, ao prosseguir, será apresentada uma tela com o *status* de cada processo, nome da empresa que o certificado está registrado e a validade do certificado:

![Screenshot_5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10090572393751)

* Feito isso, informar os dados para configuração de envio de e-mail:

![Screenshot_4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10086987982359)

* Preenchendo todas as telas, você conclui a integração entre os produtos.

![Screenshot_6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10087005203607)

**Saiba mais**Existe também a possibilidade de realizar o gerenciamento das credenciais geradas pelo **TSS**, com intuito de efetuar a autenticação das requisições recebidas do **ERP**, assim contemplando a **LGPD**. Para maiores informações acessar o *link* [Cross Segmentos - Backoffice Protheus - TSS - Configuração TSS com autenticação - Chave TSSSECURITY](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412593739287--Cross-Segmentos-Backoffice-Protheus-TSS-Configura%C3%A7%C3%A3o-TSS-com-autentica%C3%A7%C3%A3o-Chave-TSSSECURITY?source=search). **Glossário  
CT-e -** Conhecimento de transporte eletrônico **ERP** - *Enterprise Resource Planning***LGPD** *-* Lei Geral de Proteção de Dados**MDF-e** - Manifesto de Documentos Fiscais Eletrônico  
**TMS** - *Transportation Management System*  
**TSS** - TOTVS *Services* SPED  
**URL** - *Uniform Resource Locator*
