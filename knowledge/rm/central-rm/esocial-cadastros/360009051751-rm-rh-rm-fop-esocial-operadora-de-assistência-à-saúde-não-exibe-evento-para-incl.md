---
article_id: 360009051751
category: eSocial - Cadastros
content_hash: 8de581f4e6056aadc6348e4149c36ba85271a666c366709258b91d52d6c47f4a
fetched_at: '2026-06-28T22:47:14.597202+00:00'
product: rm
section_id: 1500000834341
source: central-rm
title: RM - RH - RM - FOP - eSocial - Operadora de Assistência à Saúde não exibe evento
  para inclusão
type: support-article
updated_at: '2024-12-30T13:18:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360009051751-RM-RH-RM-FOP-eSocial-Operadora-de-Assist%C3%AAncia-%C3%A0-Sa%C3%BAde-n%C3%A3o-exibe-evento-para-inclus%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23953427138583)*****Tempo aproximado para leitura:****00:03:00 min**

**Dúvida**Ao tentar realizar a vinculação de um evento no cadastro de **Operadoras de Assistência à Saúde** o sistema não permite a inclusão apresentando a mensagem **Valor inválido para o campo Evento**.  
O sistema também não apresenta a relação de eventos ao realizar um filtro no cadastro

![Sem_t_tulo_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008199391)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir das versões 12.1.2302.235, 12.1.2306.182, 12.1.2310.116 e superiores.  
  
**Solução**Isso ocorre devido as especificações das rubricas obrigatórias para o eSocial, o sistema apresentará apenas os eventos que possuírem a rubrica 9219 (Desconto de assistência médica ou odontológica) vinculada. Os eventos destinados aos descontos de assistência medica/odontológica obrigatoriamente devem conter a rubrica 9219 associada ao seu cadastro.   
  
Para solucionar este incidente, siga os passos abaixo:  
1. Acesse **Folha de Pagamento | Administração de Pessoal | Eventos**,selecione o evento de assistência à saúde e vincule a rubrica **9219 - Desconto de assistência médica ou odontológica**;

![Sem_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008159332)

2. Após vincular a rubrica no cadastro do evento, o mesmo será apresentado na tela **eSocial | Operadoras de assistência a saúde | Eventos da Operadora**.

![Sem_t_tulo_3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008159432)

**Saiba mais**Para maiores informações acesse  
      • [Operadoras de saúde](http://tdn.totvs.com.br/pages/releaseview.action?pageId=452718733)
