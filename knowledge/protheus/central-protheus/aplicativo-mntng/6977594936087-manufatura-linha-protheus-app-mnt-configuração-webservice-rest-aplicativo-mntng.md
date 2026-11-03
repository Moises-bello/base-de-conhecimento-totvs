---
article_id: 6977594936087
category: 'Aplicativo MNTNG '
content_hash: 34c572eee01093d6dfe29ab0ab4c6b0e5124aa5091a0f12f1fd5318f69410532
fetched_at: '2026-06-28T22:42:37.662737+00:00'
product: protheus
section_id: 360010992174
source: central-protheus
title: Manufatura - Linha Protheus - APP MNT - Configuração WebService Rest - Aplicativo
  MNTNG
type: support-article
updated_at: '2025-04-10T13:42:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6977594936087-Manufatura-Linha-Protheus-APP-MNT-Configura%C3%A7%C3%A3o-WebService-Rest-Aplicativo-MNTNG
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:01:40 min** **Dúvida**Como configurar o **Webservice Rest** do aplicativo **MNTNG**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Aplicativo MNTNG - Todas as versões  
  
**Solução**Para configuração do **REST** como servidor veja [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=185747842).  
Para o aplicativo **MNTNG**, devem ser feitas as seguintes configurações:

```
[ONSTART]  
JOBS=HTTPJOB  
Refreshrate=120  
  
[HTTPJOB]  
MAIN=HTTP_START  
ENVIRONMENT=P12127_MNTNG  
  
[HTTPV11]  
Enable=1  
Sockets=HTTPREST  
TimeOut=120  
  
[HTTPREST]  
Port=8389  
IPsBind=  
URIs=HTTPURI  
security=1  
  
[HTTPURI]  
URL=/rest  
Instances=1,5,2,1  
CORSEnable=1  
AllowOrigin=*  
OnConnect=REST_CONNECT  
OnExit=REST_EXIT  
OnStart=REST_START  
preparein=all  
Stateless=1
```

Algumas ressalvas devem ser feitas:

* Substituir o valor da chave **ENVIRONMENT=P12127\_MNTNG**, pelo ambiente do servidor **Protheus** a ser utilizado;
* Incluir a linha **MAXSTRINGSIZE=10** na seção **[General]**;
* Adicionar duas configurações dentro do **HTTPURI**, os itens a serem adicionados são **CORSEnable=1** e o **AllowOrigin=\***;
* Substituir a linha **Port=8086** pela porta desejada.

Para ter certeza de que a configuração do **REST** está funcionando, deverá aparecer a palavra **REST** escrita no arquivo **console.log**, conforme *print* abaixo: 

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6977598794007/mceclip0.png)

Abaixo está um exemplo da página do serviço do **REST** funcionando que pode ser acessada no endereço **http://localhost:[SUAPORTA]/rest**. Nesta tela são exibidos todos os **Webservices** disponíveis para uso.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6977715820695/mceclip1.png)

**Importante**  
Um ponto que deve ser prestado atenção é que o **endereço** em que será configurado o **Webservice deve conter um IP externo** para poder ser acessado pela aplicação. Sendo assim, uma vez que o **Webservice** estiver configurado, deve repassar a **porta interna** para os **responsáveis de TI** e pedir para torná-lo externo.   
  
**Saiba mais**Acesse a documentação completa no *link* [Configuração de Webservice Rest Aplicativo MNTNG](https://tdn.totvs.com/display/public/PROT/Implementando+o+Mobile+%28MNT+NG%29+-+Protheus#Configura%C3%A7%C3%B5es-1) na aba **Web Service Rest**.
