---
article_id: 360020756171
category: Folha Mensal
content_hash: 67f1d0282e9302f79c648f203b084cb463675a0c8039ee6c9fed2905111b0cb1
fetched_at: '2026-06-28T22:46:59.554868+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - 13º Salário: Segunda Parcela com Licença Maternidade'
type: support-article
updated_at: '2024-09-16T19:36:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020756171-RH-RM-FOP-13%C2%BA-Sal%C3%A1rio-Segunda-Parcela-com-Licen%C3%A7a-Maternidade
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:04:40 min  
  
Ocorrência**Para atender às novas regras do eSocial foram criados novos códigos de cálculo que deverão ser utilizados no processamento da **2° Parcela do 13° Salário** para funcionárias que tiveram afastamento de **Licença Maternidade** durante o ano.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Quando ocorre afastamento por Licença Maternidade durante o ano, este é lançado em Dezembro no evento de **Código de Cálculo 102** (2ª parcela 13º Salário) com o valor total de 13º salário, incluindo o valor referente ao período da licença, que será deduzido na Guia de INSS. Também é lançado um evento do tipo base de cálculo com o código de cálculo 322 (segunda parcela 13º salário licença maternidade), que tem por finalidade apenas demonstrar o valor a ser deduzido na guia.  
  
Entretanto, o **eSocial** exige que sejam informados os proventos separados de **13º Salário** pago pela Empresa e o 13º Salário referente ao **Salário Maternidade**.  
  
**Sol****ução**Por esse exigência do eSocial, deverá ser criado os novos eventos com os códigos de cálculo abaixo:  
  
**371 - SEGUNDA PARCELA 13º LICENÇA MATERNIDADE PROVENTO**: Ao criar o evento, deverá ser do tipo provento e valor, devendo ter as mesmas incidências do **Código de Cálculo 102**.  
  
**372 - DIFERENÇA 13º SALÁRIO LICENÇA MATERNIDADE PROVENTO** (será utilizado somente para diferenças de 13°): Ao criar o evento, deverá ser do tipo provento e valor, devendo ter as mesmas incidências do **Código de Cálculo 180**.  
  
O novo código de cálculo 371 irá substituir o evento do tipo base que era lançados na 2° parcela de 13º salário com códigos de cálculo 322.  
  
Como o novo evento para o 13º referente à licença maternidade será provento, o seu respectivo valor será abatido no valor do evento de 13º salário a ser pago pela Empresa, com códigos de cálculo 102 (segunda parcela 13º salário).  
  
Caso a Empresa já tenha Lançado a 2° Parcela de 13° Salário sem o novo código de cálculo, basta cancelar a movimentação e lançar novamente a 2° parcela estando nos Patch's implementados.  
**Saiba mais**Para saber mais sobre exemplos de cálculo antes e depois da implementação, proporcionalização do cálculo das médias, DCTFWeb, etc, [CLIQUE AQUI](http://tdn.totvs.com/pages/releaseview.action?pageId=440857942) acessar a documentação do TDN.
