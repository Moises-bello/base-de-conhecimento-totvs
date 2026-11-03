---
article_id: 1500002504701
category: Arquitetura Organizacional (SIGAORG)
content_hash: 562fd67ae43a5a893dba8a5680885b306870fa55a1d5e1edf457e202f3e326dd
fetched_at: '2026-06-28T22:42:52.949195+00:00'
product: protheus
section_id: 1500000904101
source: central-protheus
title: RH - Linha Protheus - ORG - Gerenciamento de Permissões ORGA020
type: support-article
updated_at: '2023-11-27T13:23:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002504701-RH-Linha-Protheus-ORG-Gerenciamento-de-Permiss%C3%B5es-ORGA020
---

**Dúvida**Para que server e como utilizar a rotina Permissões ORGA020?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Arquitetura Organizacional – Todas as versões  
  
**Solução**Esta rotina determina a partir de qual item da estrutura, cadastrada em Visões, o usuário/pessoa terá permissão e acesso aos dados.  
  
Desta forma, determina-se a qual estrutura uma pessoa tem acesso e quais pessoas estão sob a estrutura.  
  
Pelo parâmetro **MV\_ORGSPFL** configura-se a integração das permissões de acesso ao recurso de Super filtro, que valida o usuário no momento do login. Podendo ser preenchido com S ou N.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002479961/mceclip0.png)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002438722/mceclip1.png)  
  
Os usuários aqui são os cadastrados como usuários no sistema, não os funcionários do Cadastro de Funcionários e/ou de Participantes.  
  
**1.** Para configurar as permissões acesse o Módulo 70 **(SIGAORG)**, no seguinte caminho: **Atualizações > Estrutura > Permissão.**  
**2.** Em Permissões, selecione a opção de cadastro, se:  
• **Usuário** - Cadastra a permissão por usuário, apresentado os campos "Usuário" e "Nome".  
• **Grupo** - Cadastra a permissão para um grupo de usuários previamente definido, apresentado os campos "**Grupo**" e "**Descrição**".  
  
**3.** Na pasta **Estrutura Organizacional**, selecione a visão a que o usuário ou o grupo de usuários terá permissão de acesso. Ao confirmar o código da Visão selecionada, monta-se a estrutura das visões na tela.  
  
**4.** Na pasta **Departamentos**, selecione os departamentos aos quais o usuário ou o grupo de usuários terá permissão de acesso. Informe tantos quanto necessário, por linha.  
  
**5.** Em **Ações Relacionadas**, estão disponíveis as opções:  
• **Remover -** Remove o item (visão ou departamento) das permissões do usuário ou grupo de usuários.

• **Conceder -**Concede permissão ao item (visão ou departamento) ao usuário ou grupo de usuários.

• **Negar -**Nega a permissão ao item (visão ou departamento) ao usuário ou grupo de usuários.

• **Salvar-** Salva as permissões concedidas, negadas ou removidas do usuário ou do grupo de usuários  
  
**6.** Acione-as conforme necessidade e confirme.  
Exemplo de cadastro:  
  
![bgwjl0By4c.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360101322374/bgwjl0By4c.gif)  
  
**Saiba Mais**  
[Artigos sobre Arquitetura Organizacional](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206968028-RH-Arquitetura-Organizacional)
