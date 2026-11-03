---
article_id: 8918986083223
category: ADVPL - Classe e Função
content_hash: 918186669dfa7022a72c960b243bf3497cb490feeefcdba4108787ba9090bf9f
fetched_at: '2026-06-28T22:40:20.707734+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Erro no parâmetro
  FWFormModel: A estrutura principal obrigatoriamente não pode ser uma estrutura que
  não sofre modificações'
type: support-article
updated_at: '2022-09-16T14:36:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8918986083223-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-no-par%C3%A2metro-FWFormModel-A-estrutura-principal-obrigatoriamente-n%C3%A3o-pode-ser-uma-estrutura-que-n%C3%A3o-sofre-modifica%C3%A7%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Ao criar uma rotina em MVC e o cabeçalho dessa rotina vir com os campos preenchidos automaticamente, sem interação do usuário.  
  
Ocorre a mensagem:  
"erro no parâmetro **FWFormModel**: A estrutura principal obrigatoriamente não pode ser uma estrutura que não sofre modificações"  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Todas as versões  
  
**Solução**Por mais que os campos estejam preenchidos automaticamente, o modelo nunca foi alterado, logo o MVC compreende que você está tentando incluir um registro sem efetuar qualquer interação com a tela.  
Para situações como essa, você deve efetuar uma alteração no modelo.  
Nos exemplos do MVC, existe o exemplo de MVC só com grid.  
Nesse exemplo é possível ver uma forma de fazer isso, onde no *activate* do modelo, é feito um **setValue** (via **FWFldPut**).  
  
**Saiba mais**[Criando uma tela MVC só com GRID](https://tdn.totvs.com.br/pages/releaseview.action?pageId=544183102)
