---
article_id: 360025548511
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 6515b1a55419cf4a3878fdb3d59c7653f3c5f5786f801f0cd8431256990dba46
fetched_at: '2026-06-28T22:38:58.574349+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: MP - SIGAEST - Error.log "Variable does not exist D3_LOJADOC on { ||D3_LOJADOC}(FWMBROWSE.PRW)"
type: support-article
updated_at: '2021-05-06T18:20:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025548511-MP-SIGAEST-Error-log-Variable-does-not-exist-D3-LOJADOC-on-D3-LOJADOC-FWMBROWSE-PRW
---

**Ocorrência**  
Ao tentar realizar alguma Movimentação Interna (MATA241/MATA261) ou Apontamento de Produção (MATA250), ocorre o error.log: "**Variable does not exist D3\_LOJADOC on { ||D3\_LOJADOC}(FWMBROWSE.PRW)**".

**Ambiente**Protheus – Estoque/Custos – A partir da versão 12.1.17  
  
**Causa** Esse incidente ocorre, pois houve uma falha no Fonte vs Dicionário de Dados relacionado ao campo D3\_LOJADOC.  
  
**Solução**

Para solucionar essa ocorrência, listaremos em passos abaixo.

***OBS:*** ***Orientamos que efetue em ambiente de teste e valide antes de aplicar na produção.***

Por gentileza, siga os procedimentos abaixo em **modo exclusivo**:  
  
- Faça um B*ackup* da tabela SD3;  
- Efetue um *Drop* na tabela SD3;  
- Acesse ao Protheus para que a tabela SD3 seja recriada no Banco de Dados;  
- Realize o processo de *Append* (importação) dos dados originais da tabela SD3;  
- Faça um teste incluindo a movimentação que outrora gerou o problema.

Caso tenha dúvidas como realizar a recriação (backup, drop e append) da tabela, **[clique aqui.](http://tdn.totvs.com/display/PROT/APSDU+-+Backup%2C+Drop+e+Append+de+tabela)**

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*

*[MP - SIGAEST - MATA240 - Movimentação Simples](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026780773)*

*[MP - SIGAEST - MATA241 - Conceito das Movimentações Multiplas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006765772)*
