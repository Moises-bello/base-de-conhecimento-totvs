---
article_id: 5023139966359
category: eSocial - Gerar XML/ Integração Evento
content_hash: 461861a9869387156ef5ce221b3c099d4c4a0cc7c507f03dc3ea29fd34c8153f
fetched_at: '2026-06-28T22:47:13.175610+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - TAF -  Erro código 1801: O FAP do estabelecimento
  não foi localizado na base'
type: support-article
updated_at: '2024-12-30T15:06:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5023139966359-RH-RM-FOP-eSocial-TAF-Erro-c%C3%B3digo-1801-O-FAP-do-estabelecimento-n%C3%A3o-foi-localizado-na-base
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24396374171543) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao enviar o evento S-1005 de uma alteração do FAP é apresentado "**Erro código 1801: O FAP do estabelecimento não foi localizado na base**.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**Mediante a [notícia publicada no site do eSocial no dia 26/07/2021](https://www.gov.br/esocial/pt-br/noticias/ajuste-no-procedimento-de-informacao-do-fap-em-s-1005-versao-s-1.0), foi realizado um ajuste no procedimento de informação do FAP no evento S-1005 para a versão S-1.0.

Conforme orientações recebidas no grupo de homologação oficial do eSocial, esse ajuste será temporário até que a situação no ambiente do governo seja regularizada, uma vez que somente deve preencher os campos GILRAT e FAP quando houver processo judicial/administrativo com decisão/sentença favorável à utilização de alíquota GILRAT ou do FAP diferentes do que é definido pela administração, nos demais casos, os referidos campos não devem ser preenchidos (ver item 3.1 no Manual de Orientação do eSocial).

É importante lembrar também que, a situação ocorre apenas para alguns CNPJs.

Diante disso, caso ao enviar o S-1005 para o governo apresente o erro supracitado, o usuário deverá seguir as instruções abaixo:  
  
**Solução**1 - Acesse **RH | Folha de Pagamento | eSocial | Fila de Eventos**;

![](https://tdn.totvs.com/download/attachments/632113829/image2021-8-2_15-51-34.png?version=1&modificationDate=1627933877110&api=v2)

 2 - Verifique que o evento na fila foi rejeitado;

![](https://tdn.totvs.com/download/attachments/632113829/image2021-8-2_16-28-50.png?version=1&modificationDate=1627933876653&api=v2)

3 - Acesse o TAF e o menu **Atualizações | Eventos eSocial | Tabelas | Estab, Obras ou Unid. Org. Públicos;**

![](https://tdn.totvs.com/download/attachments/632113829/image2021-8-3_8-35-2.png?version=1&modificationDate=1627990502783&api=v2)

4 - Selecione o estabelecimento e clique em **Alterar;**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5023122062615)

5 - Cadastre o FAP e salve as alterações.

![](https://tdn.totvs.com/download/attachments/632113829/image2021-8-3_8-38-18.png?version=1&modificationDate=1627990698727&api=v2)

6 - Após o cadastro faça o reenvio do evento S-1005 e atualize status novamente no RM.
