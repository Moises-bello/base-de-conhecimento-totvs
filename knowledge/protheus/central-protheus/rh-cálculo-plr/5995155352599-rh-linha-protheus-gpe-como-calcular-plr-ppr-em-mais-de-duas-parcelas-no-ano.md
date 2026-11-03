---
article_id: 5995155352599
category: RH - Cálculo PLR
content_hash: ec4bf46b0b831d112cc53b7c757d3034a80d14e1a8c5826017a46f3939002d09
fetched_at: '2026-06-28T22:43:12.871257+00:00'
product: protheus
section_id: 360010855894
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular PLR/ PPR em mais de duas parcelas
  no ano
type: support-article
updated_at: '2024-07-18T19:14:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5995155352599-RH-Linha-Protheus-GPE-Como-calcular-PLR-PPR-em-mais-de-duas-parcelas-no-ano
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24991216654743) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como calcular PLR/ PPR em mais de duas parcelas no ano?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

Para calcular o PLR em mais de duas parcelas no ano, é necessário que sejam feitos os seguintes cadastros:

**1.** No cadastro de **Sindicatos** acesse em **Atualizações > Cadastros > Sindicatos (GPEA340)**  preencha **apenas** **o** **ano** e **quantidade de parcelas** que serão realizadas na aba PLR

![](https://tdn.totvs.com/download/attachments/325851863/image2017-12-26_16-7-41.png?version=1&modificationDate=1514316037000&api=v2)![](https://tdn.totvs.com/download/attachments/325851863/image2017-12-26_16-8-4.png?version=1&modificationDate=1514316037000&api=v2)

**2.** No cadastro de **Funcionários** acesse em **Atualizações > Funcionários > Funcionários (GPEA010)**, verifique se o funcionário está com o **sindicato** correto na aba **Funcionais** já configurado no passo anterior. No exemplo abaixo utilizaremos o exemplo do sindicato 01;

![](https://tdn.totvs.com/download/attachments/325851863/image2017-12-26_16-8-56.png?version=1&modificationDate=1514316037000&api=v2)

![](https://tdn.totvs.com/download/attachments/325851863/image2017-12-26_16-9-18.png?version=1&modificationDate=1514316037000&api=v2)

**3.** No **Cadastro de Períodos** acesse em **Atualizações > Definições de Cálculo > Período (GPEA400)**, insira uma nova linha indicando o roteiro **PLR** em **todos** os meses em que houver pagamento. (**Exemplo**: Pagamento será realizado em **10 parcelas** a partir de janeiro, é necessário que seja cadastrado o roteiro PLR do período do mês 01 ao mês 10). No exemplo abaixo será feito pagamento a partir de fevereiro;

![](https://tdn.totvs.com/download/attachments/325851863/image2017-12-26_16-9-56.png?version=1&modificationDate=1514316037000&api=v2)

**4.** Em Manutenção de Tabelas acesse em **Atualizações > Definições de Cálculo  Manutenção de Tabelas (GPEA320)**, cadastre a tabela **S044** de **Imposto** **de Renda para PLR;**

![](https://tdn.totvs.com/download/attachments/325851863/image2017-12-26_16-15-55.png?version=1&modificationDate=1514316037000&api=v2)

**5.** Em **Lançamentos Fixos** acesse em **Atualizações > Lançamentos > Lançamentos Fixos (GPEA550)**, selecione o funcionário e inclua um lançamento com a verba de **PLR** (verba do tipo Provento atrelada ao **id de cálculo 0151**) no roteiro **PLA,** informando data **início e fim** (este período deve ser correspondente aos meses que serão feitos o pagamento das parcelas do PLR);

![](https://tdn.totvs.com/download/attachments/325851863/image2017-12-26_16-14-40.png?version=1&modificationDate=1514316037000&api=v2)

![](https://tdn.totvs.com/download/attachments/325851863/image2017-12-26_16-15-3.png?version=1&modificationDate=1514316037000&api=v2)

**6.** Feito isso, acesse a rotina de **Cálculo por Roteiros** acesse em **Miscelânea > Cálculos > Por Roteiro (GPEM020)**, e preencha os parâmetros para cálculo do período que está aberto para **executar** **o** **cálculo.**![](https://tdn.totvs.com/download/attachments/325851863/image2017-12-26_16-17-0.png?version=1&modificationDate=1514316037000&api=v2)

Para consultar o cálculo, acesse a rotina de Consulta de Cálculo por Funcionário (Consulta > Cálculo > Por funcionário). Selecione o roteiro PLR e pressione Tab no teclado para que sejam apresentadas informações do cálculo feito;![](https://tdn.totvs.com/download/attachments/325851863/image2017-12-26_16-18-26.png?version=1&modificationDate=1514316037000&api=v2)

Para demonstrarmos o processo que utilizamos de exemplo, abaixo temos os recibos de pagamento referente aos meses de fevereiro (parcela 1) e março (parcela 2).

![](https://tdn.totvs.com/download/attachments/325851863/image2017-12-26_16-19-47.png?version=1&modificationDate=1514316037000&api=v2)

![](https://tdn.totvs.com/download/attachments/325851863/image2017-12-26_16-20-23.png?version=1&modificationDate=1514316037000&api=v2)

**IMPORTANTE**

Caso o PLR/PPR seja pago em mais de uma parcela, é necessário que todos os lançamentos referentes a ele estejam com **data de referência** no **primeiro dia do ano** (exemplo: 01/01/2020) para que sejam considerados para mesma base de cálculo do **IRRF** sobre **PLR/PPR.**

Se o lançamento for **informado,** a **data de lançamento** deve ser incluída manualmente com **referência** de **01/01.** Se calculado de forma **automática**, todos os campos do cadastro de **sindicato** da aba **PLR** devem estar preenchidos com o **ano e mês para referência**.

![](https://tdn.totvs.com/download/attachments/325851863/image2020-12-22_16-19-25.png?version=1&modificationDate=1608668367443&api=v2)

Estas informações também podem ser encontradas em: <https://tdn.totvs.com/pages/releaseview.action?pageId=325851863>

**Para Saber Mais**

[RH - Cálculo PLR](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010855894-RH-C%C3%A1lculo-PLR)

[RH - Linha Protheus - GPE - Alteração no cadastro do Sindicato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052464393-RH-Linha-Protheus-GPE-Altera%C3%A7%C3%A3o-no-cadastro-do-Sindicato?source=search)
