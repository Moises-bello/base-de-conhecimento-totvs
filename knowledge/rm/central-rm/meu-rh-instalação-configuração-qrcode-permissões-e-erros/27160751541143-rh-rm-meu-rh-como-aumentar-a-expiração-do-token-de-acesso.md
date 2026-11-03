---
article_id: 27160751541143
category: Meu RH - Instalação, configuração, qrcode, permissões e erros
content_hash: 524c075e9629d08ac8ab197951a01a05b38f34ce0bfb05e807d5fd95620ee4ad
fetched_at: '2026-06-28T22:47:29.460588+00:00'
product: rm
section_id: 1500000961062
source: central-rm
title: RH - RM - MEU RH - Como aumentar a expiração do token de acesso
type: support-article
updated_at: '2026-03-25T20:38:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27160751541143-RH-RM-MEU-RH-Como-aumentar-a-expira%C3%A7%C3%A3o-do-token-de-acesso
---

![relogio_tempo_leitura_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27160751524759) Tempo aproximado para leitura: **00:02:10 min**  
  
**Dúvida**  
Como aumentar o tempo de desconexão/logout da sessão do Meu RH?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir da versão 12.1.2310  
  
**Solução**  
Para realizar a alteração da duração do token, realize os seguintes passos:

1. Acesse o diretório ...\FrameHTML\web\app\RH\PortalMeuRH e localize o arquivo **"properties.json".**  Abra-o com um editor de texto e na propriedade **USE\_TOKEN**, atualize o valor para TRUE.

```
"USE_TOKEN": true
```

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27160798553751)

2.  No diretório C:\TOTVS\CorporeRM\RM.Net, edite os arquivos "**RM.Host.exe.config**" e "**RM.Host.Service.exe**". Dentro da tag appSettings, inclua as seguintes tags :

```
 <add key="JWTTokenExpireMinutes" value="60" />
 <add key="JWTRefreshTokenExpireMinutes" value="44000" />
```

#### 

### **Descrição dos parâmetros**

**JWTTokenExpireMinutes:** Define o tempo de validade do token de autenticação, ou seja, o período em que o usuário permanecerá logado no Meu RH sem a necessidade de realizar um novo login. Após a expiração desse tempo, a sessão será encerrada automaticamente, sendo necessário efetuar novo login.

* **Valor mínimo:** 1 minuto
* **Valor máximo:** 43200 minutos (30 dias)

**JWTRefreshTokenExpireMinute:** Define o tempo máximo para renovação automática da sessão (refresh do token), permitindo que o usuário permaneça autenticado sem interrupções durante o período configurado.

Em cenários de autenticação integrada (como Azure ou Identity), após a primeira autenticação com e-mail e senha do provedor, a sessão ficará válida até o prazo definido neste parâmetro. Durante esse período, os próximos acessos poderão ser realizados de forma simplificada, como por biometria ou Face ID, sem a necessidade de informar novamente as credenciais.

* **Valor padrão:** aproximadamente 16 horas (quando não configurado)
* **Valor máximo:** 129600 minutos (90 dias)

**Importante:** Após realizar as alterações, é necessário reiniciar os serviços do RM para que as configurações sejam aplicadas.

**Saiba Mais:**  
Para mais informações, acesse nosso TDN: [Autorização / Autenticação em API's](https://tdn.totvs.com/pages/releaseview.action?pageId=539528505#Autoriza%C3%A7%C3%A3o/Autentica%C3%A7%C3%A3oemAPI's-Dura%C3%A7%C3%A3odoToken)
