---
article_id: 5279686211095
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 85837a74cb8bfb5e84f9230a6db244b9fc0b83c78461836bcec698bd5547aae4
fetched_at: '2026-06-28T22:37:22.766786+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Exemplo de configuração
  de servidor REST HTTP para uso do Dashboard de Contratos do SIGAGCT
type: support-article
updated_at: '2022-08-17T17:20:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5279686211095-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Exemplo-de-configura%C3%A7%C3%A3o-de-servidor-REST-HTTP-para-uso-do-Dashboard-de-Contratos-do-SIGAGCT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:10:00**min****Dúvida**Como configurar o servidor rest HTTP manualmente para uso do Dashboard de GCT  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - A partir da release 12.1.27  
  
**Solução**Para que consiga acessar o servidor HTTP do Dashboard de Contratos do SIGAGCT, um exemplo de configuração da ferramenta REST pode ser realizado conforme a configuração abaixo:

**Obs.:**

A pasta HTTP-ROOT deve fazer parte do path da seção HTTP , pois os arquivos serão descompactados nesse diretório. Caso não possua a pasta, deve criar a mesma dentro da pasta Protheus Data, assim como esta no caminho da Tag patch.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5280832364311/mceclip0.png)

**1 -** Habilitar a Seção http do TOTVS Application Server e configurar as chaves Patch com o endereço de onde a aplicação deverá ser hospedada (abaixo exemplo de configuração).

**[HTTP]**  
*;EnableCors=1*  
*ENABLE=1*  
*PORT=8063*  
*ENVIRONMENT=P12.1.33\_NOVO --<> **Alterar para o nome do seu ambiente***  
*PATH=C:\Protheus 33\PROTHEUS 33\Protheus33\protheus\_data\http-root --<> **Alterar para o caminho da sua pasta http-root***

**[ONSTART]**  
*JOBS=HTTPJOB*  
*REFRESHRATE=120*

**[HTTPJOB]**  
*MAIN=HTTP\_START*  
*ENVIRONMENT=P12.1.33\_NOVO --<> **Alterar para o nome do seu ambiente***

**[HTTPV11]**  
*Enable=1*  
*Sockets=HTTPREST*

**[HTTPREST]**  
*Port=8084*  
*;IPsBind=*  
*URIs=HTTPURI*  
*Security=0*  
*;verbose=1*

**[HTTPURI]**  
*URL=/rest*  
*PrepareIn=All*  
*PrepareIn=T1,D MG 02*  
*dasboardInstances=1,2*  
*Instances=4,4,1,1*  
*CORSEnable=1*  
*AllowOrigin=\**

***IMPORTANTE:***

Este é apenas um exemplo de configuração do REST, sendo que caso não tenha sucesso e necessite de apoio na configuração do REST, orientamos a verificação junto à Equipe de Framework para o devido apoio, que é a equipe que presta este suporte à ferramenta REST do sistema.

**2-** Habilitar o parâmetros MV\_GCTPURL com o endereço do servidor da aplicação.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5317134232343/mceclip0.png)

Nesse parâmetro você vai configurar de acordo com a porta da seção HTTP.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5280873145495/mceclip1.png)

**3-** Habilitar o parâmetro MV\_BACKEND com o endereço do servidor do serviço REST.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5316753651351/mceclip1.png)

Nesse parâmetro você vai configurar de acordo com a Tag do HTTPREST, seguindo a mesma porta.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5279655758231/mceclip3.png)

**3.a-** Pode verificar se o WS esta subindo no navegador com o endereço do REST acima:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5317710736791/mceclip2.png)

**4-** Configurar no menu do modulo de gestão de contratos a chamada da rotina CNTA330:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5317219634583/mceclip1.png)

**5-** É possível verificar se o servidor HTTPREST foi ativado corretamente pelo console.log conforme abaixo:

![](https://tdn.totvs.com/download/attachments/507006974/image2020-4-22_16-28-29.png?version=1&modificationDate=1587583709967&api=v2)

**6-** Após a configuração acima, acessar o modulo de gestão de contratos ( 69 ) no caminho: Atualizações -> contratos -> dashboard:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5318141132055/mceclip0.png)

**Saiba mais:**

* [Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
* [MP - SIGAGCT - Dashboard de Contratos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036517133-MP-SIGAGCT-Dashboard-de-Contratos?source=search)
