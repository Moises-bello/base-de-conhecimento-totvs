---
article_id: 4407579428759
category: eSocial - Middleware
content_hash: 80cbb9c7e2d1338611c3473dc2f8683e1728f24b0e8c333efddaa39e754aece7
fetched_at: '2026-06-28T22:47:05.619745+00:00'
product: rm
section_id: 1500000834541
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao editar XML: Não foi possível fazer conexão
  com o servidor'
type: support-article
updated_at: '2024-06-26T19:08:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407579428759-RH-RM-FOP-eSocial-Erro-ao-editar-XML-N%C3%A3o-foi-poss%C3%ADvel-fazer-conex%C3%A3o-com-o-servidor
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24456140336151) Tempo aproximado para leitura: **00:02:30 min**  
  
Ocorrência**Ao realizar a edição de XML ocorre o erro  **Não foi possível fazer conexão com o servidor!**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407578812695)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**Este incidente ocorre por que o servidor e portas **APP** e **API** não estão configurado ou a *tag* **DefaultDB** não está com o nome (Alias) da base de dados para a qual a edição do XML está sendo realizada.  
  
**Solução**Para solucionar este incidente deverá conferir:

1. Se a *tag* **DefaultDB** nos arquivos **RM.Host.Service.exe.config** e **RM.Host.exe.config** estão com o nome (Alias) da base de dados para a qual está fazendo a edição do XML;  
   Exemplo: Nome da Base = ABCDEF  
                   *Tag*: <add key="DefaultDB" value="ABCDEF" />

2. Se as portas APP (*tag* **HttPPort**) e API (**ApiPort**) dos arquivos **RM.Host.Service.exe.config** e **RM.Host.exe.config** estão corretamente informadas no menu **Configurações | Parametrizador | eSocial | Integração com Middleware**, aba **Outros Parâmetros;**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407597507991)

**Saiba Mais**Para mais informações sobre  a configuração para edição do XML acesse:  
    • [Aplicando configuração do DefaultDB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020560172-RM-Frame-Aplicando-configura%C3%A7%C3%A3o-do-DefaultDB)  
    • [O que é e como configurar a HttpPort e ApiPort](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044519633)
