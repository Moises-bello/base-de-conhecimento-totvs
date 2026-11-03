---
article_id: 360018760551
category: Call Center - Dúvidas Gerais
content_hash: 91cbcc5c9ed6b751fed9598444237c38a095d45fee2103519a6c80b8f5b104e9
fetched_at: '2026-06-28T22:41:26.683002+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - Mensagem de configuração
  incorreta de tabelas de Atendimento Call Center
type: support-article
updated_at: '2024-04-25T14:20:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018760551-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Mensagem-de-configura%C3%A7%C3%A3o-incorreta-de-tabelas-de-Atendimento-Call-Center
---

**Dúvida**

 Ao tentar entrar no cadastro de grupo de atendimento, está acusando que as tabelas devem estar todas em um mesmo modo de compartilhamento.   
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGATMK - A partir da release 12  
  
**Solução**

Ao entrar no grupo de atendimento, surge a tela abaixo:

![image2017-5-10 11:58:28.png](http://tdn.totvs.com/download/attachments/274306395/image2017-5-10%2011%3A58%3A28.png?version=1&modificationDate=1494428900000&api=v2)

Isso indica que uma das tabelas (**SU7, SU0,AGI, AGJ, AG9,SKK**) pode estar com o modo de compartilhamento exclusivo e as demais tabelas com a opção compartilhada, ou vice e versa. Essas tabelas interagem entre si e não podem ter o sx2\_modo diferente uma da outra.

Desta forma, para resolver a questão é necessário deixar o sx2\_modo de todas as tabelas compartilhadas ou todas exclusivas, avaliando a regra de negócio de cada empresa, para saber qual desses modos é mais adequado para sua operação.

Para realizar a alteração, entre no **Configurador, Base de Dados, Dicionário, Bases de Dados**, localize cada tabela indicada no aviso e edite, altere os campos AC.Filial, AC.Unidade, AC.Empresa com o modo adequado (Exclusivo ou Compartilhado).
