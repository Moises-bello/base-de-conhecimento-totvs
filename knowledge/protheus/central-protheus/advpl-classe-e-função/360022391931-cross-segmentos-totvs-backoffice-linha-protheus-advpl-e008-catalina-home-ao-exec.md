---
article_id: 360022391931
category: ADVPL - Classe e Função
content_hash: 717a59b2130c7dbc3598fdc314228d643f4020dfbe7eeec9d256986d1b6d57fe
fetched_at: '2026-06-28T22:40:18.304949+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - E008_CATALINA_HOME
  ao executar relatório birt
type: support-article
updated_at: '2022-01-06T18:59:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022391931-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-E008-CATALINA-HOME-ao-executar-relat%C3%B3rio-birt
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Ocorrência**Ao executar o relatório CTBR817 ( Birt ) ocorre o erro abaixo

E008\_CATALINA\_HOME:Variável de ambiente CATALINA\_HOME não foi definida no servidor do Protheus Server. on GETVIEWERDIR(BIRTREPORT.PRW)  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Causa**Esse erro ocorre porque não foi configurado a variável de ambiente do sistema CATALINA\_HOME, esse erro ocorre tanto em em relatório padrão e customizado.   
  
**Solução**

É necessário configurar a variável de ambiente CATALINA\_HOME conforme documentação abaixo.

[BIRT | Instalação e Configuração](http://tdn.totvs.com/pages/viewpage.action?pageId=175865862)

```
Esse erro ocorre se não for criado a variável catalina home na Variável do Sistema   
E008_CATALINA_HOME:Variável de ambiente CATALINA_HOME não foi definida no servidor do Protheus Server. on GETVIEWERDIR(BIRTREPORT.PRW)  
  
Atenção  
Caso tenha criado e persistiu o erro, certifique-se que a variável criada é a do sistema e não do usuário, pois do usuário só irá funcionar localmente em seguida reinicie o appserver , as configurações da seção Reportservice também podem influenciar
```

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020635232/mceclip1.png)

```
Esse erro ocorre se o valor da variável estiver incorreto na variável catalina home  
argument #1 error, expected C->U, function fwrite on CREATECONFIGFILE(BIRTREPORT.PRW)
```

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020635212/mceclip0.png)
