---
article_id: 37066082894999
category: Financeiro - Novo Gestor Financeiro
content_hash: b8722c0450b8fcdadafef8e81e495635da87002c79efc57677cd7dfa2b53dbbb
fetched_at: '2026-06-28T22:37:41.568352+00:00'
product: protheus
section_id: 33830415324183
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA710 - Acesso exclusivo
  a comunicação TechFIn
type: support-article
updated_at: '2025-12-16T17:09:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37066082894999-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA710-Acesso-exclusivo-a-comunica%C3%A7%C3%A3o-TechFIn
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37066091721751) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Como dar acesso ao usuário para comunicação techfin sem ter o acesso do gestor financeiro?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**  
Atualmente foi criado um **submenu chamado “Comunicação TechFin”** dentro do **Gestor Financeiro**.

Dentro do padrão do sistema, **não é possível acessar essa funcionalidade fora do Gestor Financeiro**, uma vez que ela está **associada à substituição do processo atual de boletos do Contas a Receber**.

No entanto, é possível **restringir o acesso do usuário**, permitindo que ele tenha **apenas o permissionamento para utilização do TechFin**.

Para realizar essa configuração, siga os passos abaixo:  
  
Acesse:

* Configurador > Usuários > Senhas > Usuários  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37066091723543)
* Acesse a aba **“Restrição de acessos”** > **“Ambientes”** e selecione o módulo **Financeiro:**  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37066082867479)
* Clique em **“Outras Ações”** > **“Restrição de Rotina do Menu”**, para habilitar ou desabilitar os itens de menu;  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37066082871191)
* Localize o **Gestor Financeiro (FINA710)** e clique em **“Acessos”**, selecionando apenas os menus que deverão ficar visíveis ao usuário.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37066082873111)

Para exibir somente as funcionalidades relacionadas à **TechFin**, recomendamos habilitar apenas os menus vinculados ao **boleto híbrido**.

Após concluir os ajustes, é necessário que o usuário **acesse novamente o sistema**, para que as novas permissões sejam aplicadas corretamente.

Com isso, o novo acesso passará a demonstrar apenas as funcionalidades do Gestor conforme a configuração realizada.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37066091733655)
