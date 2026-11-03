---
article_id: 7081525304471
category: FATURAMENTO - PORTAIS (Cliente, Vendedor)
content_hash: 9c832b5a52a7576cc9c65f2922d7d1d680fbe11f4a1445709ccbe45f70ddb7b0
fetched_at: '2026-06-28T22:38:23.865740+00:00'
product: protheus
section_id: 1500001539321
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Mensagens ao
  acessar o TOTVS Gestão de Vendas (TGV)
type: support-article
updated_at: '2024-02-19T16:39:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7081525304471-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Mensagens-ao-acessar-o-TOTVS-Gest%C3%A3o-de-Vendas-TGV
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16537785696791) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como corrigir a mensagem apresentada ao acessar o TOTVS Gestão De Vendas;

Mensagens:

**"Http failure response for"**

**"Usu?rio sem acesso a empresa/filial.**

**"Falha ao retornar país [object Object]"**

**Erro na validação do usuário**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7081110431767)  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7134714149655)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - a partir da release 12.1.33;  
  
**Solução**

Ao acessar o TGV e apresentar as mensagens:

**Http failure response for**  
**Falha ao retornar país [object Object]**

E devido a configuração do APPSERVER.INI não estar com as chaves configuradas de acordo com a necessidade de utilização do TGV, realize o ajuste conforme a documentação para o acesso correto.

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Configuração do Appserver para utilização TOTVS Gestão de Vendas (TGV)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7008345717527)

Após ajuste das configurações do Appserver.ini, realizar a limpeza do **Cache do Navegador**, para o acesso correto ao sistema.

Quando apresentar as mensagens:

**Usuário****sem acesso a empresa/filial**

**Erro na validação do usuário**

É devido o ALIAS da configuração do TOTVS Mingle, não estar com o Grupo/Empresa e Filial cadastrados corretamente de acordo com a chave **PrepareIn**no Appserver.ini.

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Configuração TOTVS Mingle para implantação do TOTVS Gestão de Vendas (TGV)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7009044495895-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Configura%C3%A7%C3%A3o-TOTVS-Mingle-para-implanta%C3%A7%C3%A3o-do-TOTVS-Gest%C3%A3o-de-Vendas-TGV-)

Ao logar no PGV apresentar a mensagem **"Usuário não autenticado - Verifique se o usuário se encontra bloqueado ou se o mesmo foi cadastrado no Protheus."**

Verifique o IP do REST cadastrado para o Mingle.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16537423113239)

Este incidente ocorre, quando não tem licença disponível para acesso do **WebServices do REST**, sendo assim quando o sistema tenta conectar no Mingle ele não retorna os dados não permitindo o acesso no PGV.

[Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Consumo de Licença Webservice](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018606751-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Consumo-de-Licen%C3%A7a-Webservice)

Quando apresentar as mensagens:

Ao logar no **Portal Gestão de Vendas** apresenta a mensagem **"Bad Request".**

![bad request.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16538437510807)

Esta mensagem é apresentada quando o **IP do Rest** não foi **publicado** na rede para conexão **publica**, ou o serviço do REST **não esta iniciado**.

![localhost.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/16538476385303)
