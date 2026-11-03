---
article_id: 11944742266647
category: SIGAEST - CUSTOS
content_hash: e4d42a198055cdc2c01db8a0c7eec1dedf90076aee8b392779ab682eebadf329
fetched_at: '2026-06-28T22:39:02.109851+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Como funciona
  o Custo Médio Offline por Filial?
type: support-article
updated_at: '2025-03-12T12:23:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11944742266647-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Como-funciona-o-Custo-M%C3%A9dio-Offline-por-Filial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:21min****Dúvida**  
Como funciona o calculo de custo, aglutinado por Filial?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Neste métodos de valorização do custo médio, todos os armazéns de uma mesma filial possuem o mesmo custo médio unitário, ou seja, qualquer alteração no custo médio de um armazém é, automaticamente, repassado para todos os armazéns de uma mesma filial, portanto a contabilização dos movimentos gerados para este armazém obedecerá ao custo gerado para cada filial.

|  |
| --- |
| **Help_buttonImportante:**  Este método pode ser utilizado por todos os bancos de dados homologados pela TOTVS, com exceção do Codebase. |

**Exemplo:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11944651612055)

Observe que o custo médio unitário para a filial 01 é igual em todos os armazéns (valor 1,25), ou seja, o custo médio foi unificado por filial. Observe, também, que na filial 02, o custo médio unitário é igual em todos os armazéns (valor 1,55), ou seja, o custo médio também foi unificado por filial.

**Para utilizar a opção On-line:**

1. Altere os seguintes parâmetro: [MV\_CUSMED](https://tdn.totvs.com/pages/viewpage.action?pageId=433254045) = O e [MV\_CUSFIL](https://tdn.totvs.com/pages/viewpage.action?pageId=433254045) = A;
2. Execute a rotina [Saldo Atual](https://tdn.totvs.com/pages/viewpage.action?pageId=435099299)para atualizar os custos da tabela [SB2 - Saldos Físico e Financeiro](https://tdn.totvs.com/pages/viewpage.action?pageId=433254058).
3. Essa é a forma de calculo "Online", definido a necessidade no momento de implantação da regra de custos na empresa, caso existe a possibilidade de efetuar alteração por algum motivo, acionar o ESN - Gerente de contas, para disponibilização de uma analista consultor, especialista em estoque custos, visando verificar a melhor opção de acordo sua regra de negócios.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://tdn.totvs.com/pages/releaseview.action?pageId=393356051)*

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Como funciona o Custo Médio por Empresa?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11945935810839)*

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Como funciona o Custo Médio Offline por Armazém?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11944424817047)
