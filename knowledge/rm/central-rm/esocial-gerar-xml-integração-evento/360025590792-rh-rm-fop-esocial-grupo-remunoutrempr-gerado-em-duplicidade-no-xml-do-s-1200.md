---
article_id: 360025590792
category: eSocial - Gerar XML/ Integração Evento
content_hash: 30d5a6645332ceda6b54b7c9a7fa5dab55f3d0b1614fe9a790abfbefd20ac5d2
fetched_at: '2026-06-28T22:47:13.045451+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Grupo remunOutrEmpr gerado em duplicidade no XML
  do S-1200
type: support-article
updated_at: '2024-06-05T12:04:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025590792-RH-RM-FOP-eSocial-Grupo-remunOutrEmpr-gerado-em-duplicidade-no-XML-do-S-1200
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23965855863191) Tempo aproximado para leitura: 00:01:00 min**

**Ocorrência**  
Ao gerar o XML do evento S-1200, o grupo remunOutrEmpr é duplicado.![](https://centraldeatendimento.totvs.com/hc/article_attachments/15281291139095)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
 **Causa**   
Geralmente este incidente ocorre quando em **Anexos | Folha de Pagamento | Vínculos Empregatícios com outras Empresas (Terceiros)**, no cadastro do funcionário, é preenchido sobre a remuneração de um funcionário que consta em outra coligada da mesma base de dados. O sistema já realiza automaticamente o preenchimento da remuneração de outro emprego no caso de múltiplos vínculos entre coligadas. O anexo supracitado só deve ser preenchido quando há vínculo com empresas não registradas na base de dados. Com isto, é gerada a duplicidade no XML.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042451093)

**Solução**  
 Para solucionar essa ocorrência, realize os seguintes passos:  
 1. Acesse Administração de Pessoal e selecione o funcionário que apresentou duplicidade;  
2. Selecione **Anexos | Folha de Pagamento | Vínculos Empregatícios com outras Empresas (Terceiros)**e valide qual o registro cadastrado para o funcionário que refere-se à remuneração da outra coligada;  
3. Exclua o registro e gere novamente o XML do S-1200.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042453213)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042459453)

**Importante**  
Nos casos em que os vínculos do funcionário sejam entre coligadas que estejam em bases de dados distintas, o anexo **Vínculos Empregatícios com outras Empresas (Terceiros)**deverá ser preenchido normalmente.
