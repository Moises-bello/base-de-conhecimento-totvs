---
article_id: 360006193052
category: RH - Cadastros
content_hash: dcfcd4e8004c0e32ceade29015333266f3644c52375068d24a5a72157937d6ee
fetched_at: '2026-06-28T22:44:52.785582+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Como alterar o filtro e as informações das visitas
type: support-article
updated_at: '2025-12-16T13:02:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006193052-RH-Linha-Protheus-PON-Como-alterar-o-filtro-e-as-informa%C3%A7%C3%B5es-das-visitas
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34323370742551) Tempo aproximado para leitura: 00:01:30 min***  
  
**Dúvida**  
PONA340 - Como alterar o filtro e as informações dos Visitantes?   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Por padrão, o sistema determina que o filtro de visualização das visitas seja aplicado a qualquer usuário da rotina, mesmo que o código de outro usuário ou grupo esteja relacionado ao filtro.

Quando um filtro é selecionado, os demais usuários apenas visualizarão as visitas que atendam às condições desse filtro. Isso ocorre porque o sistema realiza constantemente uma varredura nas informações, verificando as condições definidas pelo novo filtro.

**Como funciona o filtro, no padrão:**

* Acessando o **SIGAPON**, em **Atualizações > Cadastros de Visitantes > Visitas**, um usuário pode filtrar e deixar ativo que, no filtro, determina que somente as visitas **agendadas** sejam visualizadas.
* Se um segundo usuário acessar a mesma rotina e, pela opção de filtro, selecionar outro em que somente as visitas **não agendadas** possam ser visualizadas, o filtro ativo passa a ser o último selecionado.

Assim, o primeiro usuário, ao retornar para a mesma rotina, visualizará apenas as visitas **não agendadas**.  
Esse processo foi idealizado dessa forma para facilitar a administração de uma equipe que trabalhe sob a mesma regra de negócio, permitindo que a seleção de um filtro tenha reflexo para todos os usuários da rotina.

Quando o parâmetro **MV\_MUDFVIS**, no **Configurador**, possuir conteúdo igual a **N (não)**, o filtro ativo do primeiro usuário não será substituído pelo filtro selecionado pelo segundo. Dessa maneira, cada usuário terá visualizações distintas.

**Alteração de informações de visitantes:**

* No padrão, é possível **consultar** as informações do visitante selecionado através da tecla **F6**.
* Com o parâmetro configurado, é possível **alterar** as informações do visitante selecionado pela tecla **F7**.

Esse recurso é útil, por exemplo, quando no atendimento se verifica que o nome do visitante não está corretamente registrado, permitindo realizar a alteração imediatamente.

**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
