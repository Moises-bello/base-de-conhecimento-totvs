---
article_id: 360024944634
category: RH - Fechamentos
content_hash: fb3cdbac64bd21b3ea31e5fdbfde8afc3f6c983f3b9eb163f5b4af1b42cd19bc
fetched_at: '2026-06-28T22:44:48.826943+00:00'
product: protheus
section_id: 32419231682455
source: central-protheus
title: RH - Linha Protheus - PON - Acesso Exclusivo no Fechamento do Ponto
type: support-article
updated_at: '2025-06-16T12:06:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024944634-RH-Linha-Protheus-PON-Acesso-Exclusivo-no-Fechamento-do-Ponto
---

**Dúvida**É possível fazer o fechamento do Ponto com usuários utilizando tabelas relacionadas?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**

O fechamento do ponto eletrônico não pode ser realizado sem acesso exclusivo às tabelas do sistema, pois este processo envolve a migração dos registros das tabelas de períodos abertos para as de períodos fechados. Durante essa operação, o sistema cria automaticamente uma tabela temporária no banco identificada como PN090LOCK+filial, indicando o período em que o fechamento está sendo executado.

Essa linha de bloqueio criada na PN090LOCK+filial impede que outros usuários acessem ou modifiquem os dados do mesmo período de apontamento, garantindo a integridade e a segurança das informações. Somente após a conclusão do fechamento mensal e da migração dos dados, é que o acesso ao ponto para aquele período será liberado.

Portanto, é fundamental que nenhum outro usuário realize manutenção no ponto durante o processo de fechamento, a fim de evitar inconsistências e garantir a precisão dos dados migrados.

Veja a relação DE/PARA das tabelas que serão migrados os registros no fechamento mensal:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32839694145559)  
  
**Saiba mais:**[RH - Linha Protheus - PON - Migração de dados no Fechamento Mensal do Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013084192-RH-Linha-Protheus-PON-Migra%C3%A7%C3%A3o-de-dados-no-Fechamento-Mensal-do-Ponto)[Como Efetuar Fechamento do Ponto por filial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006267372)  
[Como efetuar o Fechamento Mensal do Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004103232)  
**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854)**
