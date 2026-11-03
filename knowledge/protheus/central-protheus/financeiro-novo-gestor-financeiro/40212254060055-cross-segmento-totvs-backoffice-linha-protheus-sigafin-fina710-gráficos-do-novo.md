---
article_id: 40212254060055
category: Financeiro - Novo Gestor Financeiro
content_hash: 9a54d75b03ce7de695a4b2af7313378b947f38874d049b0abd0801098b02b243
fetched_at: '2026-06-28T22:37:41.534787+00:00'
product: protheus
section_id: 33830415324183
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - FINA710: Gráficos
  do Novo Gestor Financeiro na aba "Entrada" não atualizam com filtro do Painel de
  Controle'
type: support-article
updated_at: '2026-05-07T20:02:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40212254060055-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-FINA710-Gr%C3%A1ficos-do-Novo-Gestor-Financeiro-na-aba-Entrada-n%C3%A3o-atualizam-com-filtro-do-Painel-de-Controle
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40212269857687) Tempo aproximado para leitura: **02:00 min**  
  
**Dúvida**  
Ao utilizar o Novo Gestor Financeiro (FINA710) e aplicar um filtro no Painel de Controle, os gráficos localizados no caminho "Movimentações Financeiras" -> Aba "Entrada" não são atualizados e não respeitam o filtro aplicado  
  
Exemplo de um filtro criado e print da  Aba "Entrada"   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40212269860631)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40212269867159)  
  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - 2410

**Solução**  
Este é o comportamento padrão da rotina no sistema.

O filtro definido pelo usuário no **Painel de Controle** é aplicado exclusivamente na **aba** “**Geral**”. Não há replicação ou herança deste filtro para as abas de “**Entradas**” e “**Saídas**”.

Consequentemente, os **gráficos** e informações apresentados nessas abas não refletirão o filtro do **Painel de Controle**, operando de forma independente desta parametrização.  
  
**Saiba mais:** [Movimentações Financeiras - FINA710](https://tdn.totvs.com.br/pages/releaseview.action?pageId=622668231%20)
