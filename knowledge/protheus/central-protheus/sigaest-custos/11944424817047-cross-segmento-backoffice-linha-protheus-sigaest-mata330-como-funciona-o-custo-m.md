---
article_id: 11944424817047
category: SIGAEST - CUSTOS
content_hash: 5689f7d4a56d9bf35015623eedc466669d6abbed21196d225919a19f2749f791
fetched_at: '2026-06-28T22:39:02.104479+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Como funciona
  o Custo Médio Offline por Armazém?
type: support-article
updated_at: '2025-03-12T12:23:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11944424817047-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Como-funciona-o-Custo-M%C3%A9dio-Offline-por-Armaz%C3%A9m
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:50min** **Dúvida**  
Como funciona o calculo de custo, aglutinado por armazém?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Neste método de valorização do custo médio, cada armazém cadastrado no ambiente Estoque e Custos terá o seu custo médio unitário individualizado, ou seja, se um produto for cadastrado em mais de um armazém, cada armazém terá um custo médio unitário diferente e, portanto a contabilização dos movimentos gerados para este armazém, obedecerá ao custo gerado para cada armazém.

**Exemplo:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11944555909271)

Observe que o custo unitário para cada armazém é individualizado, ou seja, **será sempre diferente**.

O parâmetro [MV\_A330GRV](https://tdn.totvs.com/pages/viewpage.action?pageId=312165032) indica se todos os produtos/armazéns terão seu saldo inicial calculado no início do processamento do custo médio:

* .T. (True/Verdadeiro) = Todos os registros.
* .F. (False/Falso) = somente os registros que possuem saldo inicial ou movimentação.

**Para utilizar a opção On-line:**

1. Altere os seguintes parâmetro: [MV\_CUSMED](https://tdn.totvs.com/pages/viewpage.action?pageId=433254045) = O e [MV\_CUSFIL](https://tdn.totvs.com/pages/viewpage.action?pageId=433254045) F;
2. Execute a rotina [Saldo Atual](https://tdn.totvs.com/pages/viewpage.action?pageId=435099299)para atualizar os custos da tabela.
3. Essa é a forma de calculo "Online", definido a necessidade no momento de implantação da regra de custos na empresa, caso existe a possibilidade de efetuar alteração por algum motivo, acionar o ESN - Gerente de contas, para disponibilização de uma analista consultor, especialista em estoque custos, visando verificar a melhor opção de acordo sua regra de negócios.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://tdn.totvs.com/pages/releaseview.action?pageId=393356051)*

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Como funciona o Custo Médio Offline por Filial?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11944742266647)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Como funciona o Custo Médio por Empresa?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11945935810839)
