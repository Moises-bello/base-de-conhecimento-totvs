---
article_id: 360024715313
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 5c1c786f9c1733bfe9181d81ba2d2c1aa43d5e2eba0d4798ef510c3785fe8313
fetched_at: '2026-06-28T22:42:42.049597+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Como registrar a quantidade do MOD
  na estrutura do produto
type: support-article
updated_at: '2021-06-01T17:26:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024715313-Manufatura-Linha-Protheus-SIGAPCP-Como-registrar-a-quantidade-do-MOD-na-estrutura-do-produto
---

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:20 min**  
**Dúvida**No **MATA200 - Cadastro de Estrutura**, como informar a quantidade que será requisitada da **MOD - Mão de Obra**?   
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Ao cadastrar a quantidade que deverá ser requisitada do **MOD** verificar o conteúdo do parâmetro **MV\_TPHR - Define a unidade padrão para tempos utilizados pelo Sistema de PCP e ESTOQUE.** O tipo de hora pode ser **N - Normal** ou **C - Centesimal.**Se o parâmetro **MV\_TPHR** estiver com o valor **N**, o Sistema identificará a quantidade indicada na estrutura como **Normal**, e fará a conversão para centesimal ao empenhar.  
Se o parâmetro **MV\_TPHR** estiver com o valor **C**, o Sistema identificará a quantidade indicada na estrutura como **Centesimal** e não fará a conversão.  
  
**Exemplos**  
1. **MV\_TPHR** = **N  
MOD**na estrutura 0,40  
Ordem de 1 unidade  
Nesta situação o tempo considerado é de 40 minutos, mas como o empenho é trabalhado em centesimal o Sistema irá realizar o cálculo para transformar 40 minutos em centesimal.  
Cálculo realizado: (0,4/60) \* 100 = 0,6667  
  
2. **MV\_TPHR**= **C  
MOD**na estrutura 0,40Ordem de 1 unidade  
Nesta situação o tempo considerado é 0,40 horas, neste caso não é necessário realizar a transformação pois o parâmetro o campo já está sendo trabalhado em centesimal.
