---
article_id: 360060367133
category: RH - Folha de Pagamento
content_hash: 0e688e183e21aa1d5bf9f7adfcd2458f28d779cb215e8fde01c320d0e375fb80
fetched_at: '2026-06-28T22:44:13.420092+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como é realizado o calculo de salário família proporcional
  admissão para funcionários horista
type: support-article
updated_at: '2025-08-06T17:22:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060367133-RH-Linha-Protheus-GPE-Como-%C3%A9-realizado-o-calculo-de-sal%C3%A1rio-fam%C3%ADlia-proporcional-admiss%C3%A3o-para-funcion%C3%A1rios-horista
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26354443770007) Tempo aproximado para leitura: 00:04:00 min**

**Dúvida**Como é realizado o calculo de salário família proporcional admissão para funcionários horista?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Para realizar o cálculo proporcional do salário família na admissão do empregado para funcionários horista, siga as configurações abaixo:

No **modulo Configurador** realize a configuração dos parâmetros:

**- MV\_SALFP:** Calcula salário família proporcional no mês da admissão ou demissão:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000066762)

**- MV\_SALFD:** Calcula salário família proporcional sobre os dias do mês:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000066982)

No **modulo Gestão de Pessoal** cadastre a tabela S003 em **Atualizações -> Definições Cálculos -> Manutenção Tabelas**:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098942714)

Em **Atualizações -> Funcionários -> Dependentes** realize o cadastro do dependente:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098943334)

O cadastro do funcionário informe os campos abaixo em **Atualizações -> Funcionários -> Funcionários**:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101158313)

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101159813)

Cadastre as verbas referente ao salário família em **Atualizações -> Definições Cálculos -> Verbas**:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098943634)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101158493)

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101158573)

Realize o calculo da folha em **Miscelânea -> Cálculos -> Por Roteiro**:

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101158673)

Consulte o cálculo em **Consultas -> Cálculo -> Por Funcionários:**

**![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000068022)**

**Obs.:**Para realizar o enquadramento da cota de salário família a ser paga ao empregado horista, o Sistema sempre verificará no cadastro de funcionário, campo salário X o campo Hrs mensais, para montar o salário mês do funcionário.

Este campo é que determina se o pagamento do salário família será devido ou não.

Importante é, sempre verifique se o campo de salário do cadastro do funcionário concede ou não o direito ao recebimento do salário família.

O segundo ponto a ser verificado é, se existe verbas com sim para salário família no cadastro de verbas, pois se existir e a soma do salário mais as verbas com sim para salário família for maior que o teto para pagamento da cota, o benefício não será concedido.

Para empresas que querem utilizar para base de cálculo **30** dias no caso de **mensalistas,** o parâmetro **MV\_SALFD** deve ser igual a **N**. Já para empresas que querem utilizar cálculo de acordo com os **dias do mês** (seja 28, 29 ou 31), o parâmetro **MV\_SALFD** deve ser igual a **S**.  
A fórmula de cálculo fica da seguinte forma:

**MV\_SALFD=N** >> Salário mês/ 30 \* dias trabalhados **MV\_SALFD=S** >> Salário mês/ dias do mês \* dias trabalhados

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

<https://tdn.totvs.com/pages/releaseview.action?pageId=555868219>
