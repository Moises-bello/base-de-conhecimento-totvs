---
article_id: 4418024669591
category: Meu RH - Gestor
content_hash: ed2142a31193136884f3f73d8097290d013b8e2dc9d2ec4181756cf214022b52
fetched_at: '2026-06-28T22:47:32.389934+00:00'
product: rm
section_id: 1500000861742
source: central-rm
title: RH - RM - Meu RH - Erro ao desconsiderar batida do subordinado, não é possível
  excluir batidas coletadas
type: support-article
updated_at: '2024-11-01T17:07:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418024669591-RH-RM-Meu-RH-Erro-ao-desconsiderar-batida-do-subordinado-n%C3%A3o-%C3%A9-poss%C3%ADvel-excluir-batidas-coletadas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22209949449623) Tempo aproximado para leitura: **00:01:30 min****Ocorrência**Quando um Chefe ou Supervisor tenta desconsiderar uma batida via geolocalização, é retornado a mensagem de erro: **Não é possível excluir batidas coletadas**.  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir do release 12.1.29  
  
**Causa**Esse incidente ocorre, pois a parametrização do sistema está para não permitir a exclusão de batidas coletadas.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418037026199)  
  
**Solução**Para que o processo de desconsiderar batida seja executado com sucesso é necessário:   
  
Acessar o parâmetro abaixo no grupo de quiosque do modulo Automação de Ponto associado ao gestor, Automação de ponto / aba configurações / parametrizador / RM portal / edite o grupo de quiosque associado ao funcionário (gestor) e marque o parâmetro destacado abaixo.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418030204951)
