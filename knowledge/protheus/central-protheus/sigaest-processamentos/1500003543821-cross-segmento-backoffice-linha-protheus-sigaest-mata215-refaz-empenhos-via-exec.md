---
article_id: 1500003543821
category: SIGAEST - PROCESSAMENTOS
content_hash: 2e9f7c15f295fd28dd49663950ea698196f05ce9ef2ab8dec174535262089326
fetched_at: '2026-06-28T22:39:04.939564+00:00'
product: protheus
section_id: 1500001538861
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA215 - Refaz Empenhos
  via Execauto
type: support-article
updated_at: '2025-03-12T12:28:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003543821-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA215-Refaz-Empenhos-via-Execauto
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22234521356183) Tempo aproximado para leitura: 00:07:00 min**

**Dúvida**Como executar a rotina MATA215 - Refaz Empenhos- Via Execauto (execução automática)?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

**O que é a rotina de Refaz Empenhos, e para que serve?**

O processamento da rotina Refaz empenho, é uma operação concebida para possibilitar aos usuários restaurar empenhos previamente cancelados ou anulados dentro de um período determinado. Esta função é frequentemente empregada para corrigir imprecisões nos registros de empenhos, tais como ajustes em valores por exemplo.

Ao acionar o processamento da rotina de Refaz Empenho, o sistema realiza uma análise nos dados relativos aos empenhos dentro do periodo de apuração, e reconstitui os empenhos anteriormente cancelados ou anulados, após finalização do processamento.

**Os arquivos refletirão os saldos empenhados, reservados e/ou esperando distribuição.**

Utilizada para checar/acertar dados que estejam indevidamente gravados nos arquivos. Os campos a serem avaliados, recalculados e acertados são:  
• saldo de pedidos e pedidos.  
• quantidades empenhadas em pedidos de venda, não classificadas, reservadas e entradas previstas.  
• quantidades do arquivo de reservas.  
• entradas previstas de O.P. e solicitações de compras.  
• saídas previstas e realizadas por pedidos de venda liberados.  
• requisições empenhadas.  
• movimentos com TES que atualize estoque.

É crucial enfatizar que a rotina Refaz Empenhos deve ser realizada com cautela e exclusivamente por indivíduos familiarizados com as nuances técnicas do sistema e entendimento do estoque.

Por padrão a rotina fica localizada em: **Modulo 04 SIGAEST -> Miscelânea -> Refaz Empenhos**.

**Importante:**

Utilize o parâmetro "**MV\_MCUSTO**" para informar qual a moeda utilizada para determinar o limite de crédito dos clientes.

**Existe a possibilidade de execução da rotina Refaz Empenhos de forma automatizada**, entretanto é importante ressaltar que, **a rotina poder ser efetuada somente de forma exclusiva**, conforme o próprio alert da rotina ja informa.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22234473128215)

Caso tente processar a rotina de modo a qual ela não esteja exclusiva, sera apresentado HELP, exemplo:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - HELP MA280FLOCK em Rotinas de Processamentos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002304362-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-HELP-MA280FLOCK-em-Rotinas-de-Processamentos)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22234473138199)

**Mas qual seria então a finalidade de possuir a rotina de forma automatica, uma vez que ela pode ser executada somente de forma exclusiva?**

Este é um questionamento frequentemente levantado, e a resposta reside na necessidade de automatizar o processamento da rotina, juntamente com a viabilidade do recurso Execauto. Essa abordagem visa proporcionar ao usuário a conveniência de não precisar acessar manualmente a rotina para executá-la, permitindo que ela seja processada de maneira autônoma, por exemplo, durante períodos noturnos quando o ambiente não está em uso. É importante destacar que essa rotina tem como objetivo corrigir os saldos empenhados e, portanto, não pode ocorrer simultaneamente com outras operações para evitar conflitos, **por tanto somente de forma Exclusiva**.

**Como configurar a rotina para processamento com o Execauto:**

Esta função pode ser executada através de uma rotina automática.  
No exemplo abaixo, existe a preparação do ambiente para rodar esta rotina,  
que é feita através do comando Prepare Environment.

**// aemp[1] = Empresa (Caracter)**  
**// aemp[2] = Filial (Caracter)**  
**// Administrador = Através de qual usuário irá executar a rotina. (Caracter)**  
**// senha = Senha do usuário (Caracter)**

**User Function jobm215()**  
**Local PARAMIXB := .T.**  
**Local aemp := {"99","01"}**

**PREPARE ENVIRONMENT EMPRESA aemp[1] Filial aemp[2]**  
**USER 'Administrador'**  
**PASSWORD 'senha'**  
**TABLES "SA1","SB2","SC0","SC6","SC7","SC9","SD1","SD4","SE2","VCB"**  
**MODULO "EST"MSExecAuto({|x| mata215(x)},PARAMIXB)RESET ENVIRONMENT**

**Return Nil**

**Descrição das tabelas:**

**SA1** - Arquivo de clientes. Recalcula os campos de saldo de pedido e saldo de pedido liberado.  
**SB2** - Arquivo de saldos físicos e financeiros. Recalcula os campos de quantidade empenhada, quantidades em pedidos de venda, quantidade não classificada em nota fiscal, quantidade reservada, quantidade de entradas previstas, etc.  
**SC0** - Arquivo de reservas. Verifica quantidades reservadas.  
**SC6** - Arquivo de itens dos pedidos de vendas. Verifica quantidades de saídas previstas.  
**SC7** - Arquivo de pedidos de compras. Verifica quantidades de entradas previstas.  
**SC9** - Arquivo de pedidos de vendas liberados. Verifica quantidades de saídas previstas e realizadas.  
**SD1** - Arquivo de Itens das notas fiscais de entrada. Verifica as quantidades de saída.  
**SD4** - Arquivo de requisições empenhadas. Verifica quantidades empenhadas.  
**SE2** - Arquivo de Contas a Pagar  
**SF4** - Arquivo de tipo de entrada e saída. Verifica se os movimentos atualizam ou não o estoque.  
**VCB** - Regiões

**Saiba mais:**

*[MP - SIGAEST - Execução de Schedule Custo Médio (MATA330)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048543893)*

*[Como agendar a execução de Rotinas?](https://tdn.totvs.com/pages/releaseview.action?pageId=271167961)*

*[MP - SIGAEST - MATA300 - Execução via Schedule](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003684662-MP-SIGAEST-MATA300-Execu%C3%A7%C3%A3o-via-Schedule)*

*[Clique aqui e veja mais artigos sobre Processamentos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033442-SIGAEST-PROCESSAMENTOS)*
