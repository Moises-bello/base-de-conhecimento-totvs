---
article_id: 4500895030039
category: Materiais - Compras (SIGACOM)
content_hash: cc3800f78b802dab4515d64b6017182585bb7d5dba48105f6fb942773ebb20bd
fetched_at: '2026-06-28T22:41:14.177151+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Ao salvar o pedido
  de compras, o sistema apresenta help A120RESTR
type: support-article
updated_at: '2026-05-12T12:41:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4500895030039-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ao-salvar-o-pedido-de-compras-o-sistema-apresenta-help-A120RESTR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40408252457623) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Ao salvar o pedido de compras, o sistema apresenta help A120RESTR  
  
**Ambiente**  
  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - Todas as Versões  
  
**Solução**  
O help é apresentado , pois, o sistema está configurado para não permitir que usuário Cadastrado como Comprador inclua Pedido de compras sem solicitação de compras conforme cenário atual abaixo:

**1.**Verifique se o usuário possui cadastro único na rotina de Compradores;

**2.** Verifique que o campo "Ped sem SC" (Y1\_PEDIDO) = Não e se necessário altere-o para "Sim".

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4500733587479)

**3.**Parâmetro MV\_RESTINC=N, se necessário altere-o para "S"

**Obs:**

Caso não queira que o help seja apresentado altere o parâmetro **MV\_RESTINC=N** ou altere no cadastro do Comprador rotina (COMA087) no campo **Y1\_PEDIDO = Sim**.

**Saiba Mais:**

* [MP - SIGACOM - O que é o Cadastro de Compradores MATA087 / COMA087 ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024650292-MP-SIGACOM-O-que-%C3%A9-o-Cadastro-de-Compradores-MATA087-COMA087-?source=search)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
