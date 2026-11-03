---
article_id: 20446229889943
category: Originação de Grãos (OG)
content_hash: 6c0e61be3eb726b85bea87451d76e011578ba5990e028968fcef03993dace4ed
fetched_at: '2026-06-28T22:45:39.583628+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Grupo bloqueado na tabela de classificação
type: support-article
updated_at: '2025-04-09T19:40:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20446229889943-Agro-Linha-Protheus-AGR-Grupo-bloqueado-na-tabela-de-classifica%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20446229869591) Tempo aproximado para leitura: **00:00:35 min****Ocorrência**  
No módulo **Comercialização (Linha Protheus) - Originação de Grãos (OG)**, ao realizar o processo para incluir um registro no **AGRA035 -****Tabela de Classificação** é apresentada a ocorrência **Grupo bloqueado na tabela de classificação**.  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Causa**  
Esse incidente ocorre, pois é necessário realizar o processo para incluir um registro no **AGRA035 -****Tabela de Classificação** no Sistema.  
  
**Solução**  
Para que o campo **Grupo** seja desbloqueado é necessário acessar o parâmetro **MV\_AGRDES** e alterar o conteúdo. Ao preencher o parâmetro **MV\_AGRDES** com o conteúdo **1**, o código do produto torna-se obrigatório no cadastro da **Tabela de Classificação** e o campo **Grupo é Bloqueado**.   
E informar o conteúdo**2** no parâmetro, o **código do produto** não é obrigatório e o campo **Grupo** é desbloqueado.
