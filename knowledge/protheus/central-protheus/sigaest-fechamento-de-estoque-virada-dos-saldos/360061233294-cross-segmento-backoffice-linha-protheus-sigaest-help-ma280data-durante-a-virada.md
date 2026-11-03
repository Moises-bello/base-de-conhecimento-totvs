---
article_id: 360061233294
category: SIGAEST - FECHAMENTO DE ESTOQUE (VIRADA DOS SALDOS)
content_hash: c40fcb40fc8b59047b4c5a8f8d3310b3410dc772669e621a7d0d48cae1abe8c3
fetched_at: '2026-06-28T22:38:52.743206+00:00'
product: protheus
section_id: 1500001538921
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - HELP MA280DATA durante
  a Virada de Saldos
type: support-article
updated_at: '2026-01-16T18:32:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061233294-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-HELP-MA280DATA-durante-a-Virada-de-Saldos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24764851973143) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Ao processar o Fechamento de Estoque (Virada de Saldos) - MATA280 - Ocorre o HELP MA280DATA. Como corrigir este problema?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24764912783511)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

O **HELP MA280DATA** ocorre quando a rotina Virada de Saldos não está conseguindo finalizar devido à possível existência de registros com a mesma data que está fechando o mês (em muitos casos já foi feito um fechamento)  
  
Nesse caso, avalie se nas tabelas SB9, SBJ e SBK (caso possua produto com controle de lote e endereço) realmente possui registros com a data do fechamento que está tentando efetuar. Caso sim, verificar internamente se poderá reabrir este período gravado no fechamento (alterando também o parâmetro MV\_ULMES para a data anterior ao fechamento) para, após isso, conseguir concluir com o fechamento de estoque.

Valide se não possui algum parametro MV\_ULMES **compartilhado**, caso você esteja definindo o fechamento por filial, onde o sugerido é que cada filial, possua o parametro de forma **exclusiva**. uma vez que voce seta a exclusividade do fechamento para que cada filial tenha o seu fechamento, se houver um parametro compartilhado com data diferente, pode ocasionar o erro.

**Valide se o parametro MV\_DBLQMOV está criado no ambiente e caso não favor criar:**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como realizar o bloqueio de Movimentações no Estoque durante o Fechamento de Estoque?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018844351-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-realizar-o-bloqueio-de-Movimenta%C3%A7%C3%B5es-no-Estoque-durante-o-Fechamento-de-Estoque)

Se necessário efetuar a reabertura, para realizar o fechamento novamente, hoje o Protheus dispõe de uma rotina padrão para reabertura de estoques, "Acompanha Custos > [**Reabertura de Estoque**](https://tdn.totvs.com/display/PROT/Reabertura+de+Estoque)".

**Verifiquei que não existem registros nas tabelas SB9, SBK e SBJ com data igual ou posterior. O que fazer?**

Para corrigir este erro, basta aplicar o pacote de atualização abaixo:

- [Acumulado SIGAEST conforme sua versão](https://tdn.totvs.com/x/2hgdHw)

Após aplicar, basta executar a Virada de Saldos novamente para que esta seja concluída com sucesso.

**Saiba mais:**

[*MP - SIGAEST - Quais os possíveis impactos da Reabertura de Estoque?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002994501)

[*Clique aqui e veja mais artigos sobre Virada de Saldos (Fechamento de Estoque)*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012208793-SIGAEST-FECHAMENTO-DE-ESTOQUE-VIRADA-DOS-SALDOS-)
