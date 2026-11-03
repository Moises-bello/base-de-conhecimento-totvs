---
article_id: 360020989071
category: SIGAACD - Automação e Coleta de Dados
content_hash: 37beea4ddeb00b66456badd98c32fb5db18292d89aaac2f65f6f12432c664ab1
fetched_at: '2026-06-28T22:39:12.723220+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Existe relatório para
  Ordem de Separação?
type: support-article
updated_at: '2025-07-29T17:12:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020989071-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Existe-relat%C3%B3rio-para-Ordem-de-Separa%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24762569716375) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**  
No modulo de ACD - Existe relatório para Ordem de Separação?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**  
Para a impressão de OS temos o relatório "Impressão das Ordens de Separação" (**ACDR100**).  
Essa rotina por padrão não está no Menu, caso necessario efetuar a configuração via Configurador (**SIGACFG**) no cadastro de Menu e adicionar a rotina ao menu que deseja.

* **Relação:** **MV\_ACDR100**  
  Define se será apresentado o relatório de Ordem de Separação - ACDR100 ao selecionar a opção impressão na rotina de Ordem de Separação.  
  Obs.: executado somente se o ponto de entrada ACD100RE - Substituição da função de impressão de relatório não existir.  
  DEFAULT .F.

**Saiba Mais:**  
[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23970894011799-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Configurar-Local-de-impress%C3%A3o-ACDA060-para-utilizar-na-impress%C3%A3o-de-Etiquetas#:~:text=Saiba%20Mais%3A,Coleta%20de%20Dados)
