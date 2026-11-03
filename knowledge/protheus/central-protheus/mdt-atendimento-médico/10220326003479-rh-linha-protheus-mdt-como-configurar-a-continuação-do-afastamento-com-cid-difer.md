---
article_id: 10220326003479
category: MDT - Atendimento Médico
content_hash: 05774e9e5d6e3b68b184590562e71137b02199e3c8aa598fc64bb952f63e2cde
fetched_at: '2026-06-28T22:44:20.565939+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: RH - Linha Protheus - MDT - Como configurar a continuação do afastamento com
  CID diferente
type: support-article
updated_at: '2025-03-03T18:17:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10220326003479-RH-Linha-Protheus-MDT-Como-configurar-a-continua%C3%A7%C3%A3o-do-afastamento-com-CID-diferente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372808076951) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Como configurar a continuação do afastamento com CID diferente?  
  
**Ambiente**TOTVS RH (Linha Protheus) -Medicina e Segurança do Trabalho –Todas as versões  
  
**Solução**O parâmetro **MV\_NG2COAF** indica se é realizada a continuação ou não de afastamentos com CID **diferentes**.  
  
Parâmetro MV\_NG2COAF **inexistente** ou com conteúdo **em branco**:

* Sistema continua conforme o padrão, ou seja, busca os afastamentos anteriores também com CID diferentes e pergunta ao usuário se deseja continuar ou não estes afastamentos.

Parâmetro MV\_NG2COAF com conteúdo igual a **1**:

* Sistema pergunta ao usuário se deseja continuar ou não afastamentos com CID diferentes.

Parâmetro MV\_NG2COAF com conteúdo igual a **2**:

* Sistema continua os afastamentos anteriores com CID diferentes sem perguntar ao usuário.

Parâmetro MV\_NG2COAF com conteúdo igual a **3**:

* Sistema não continua nenhum afastamento com CID diferentes.

Obs.: Alguns **afastamentos** não podem ser incluídos por vários motivos, como por exemplo o **bloqueio da folha** (melhoria feita pelo time do módulo SIGAGPE), impedindo assim o cadastro do atestado até que a situação seja resolvida. Dito isso, há necessidade de **permitir** o cadastro do atestado e **guardar** o afastamento deste, para ser enviado **posteriormente**.   
  
**Saiba Mais**  
[Artigos sobre Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos sobre Atendimento Médico](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945694-MDT-Atendimento-M%C3%A9dico)  
[Comunicação de Afastamentos](https://tdn.totvs.com/pages/viewpage.action?pageId=640196437)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
