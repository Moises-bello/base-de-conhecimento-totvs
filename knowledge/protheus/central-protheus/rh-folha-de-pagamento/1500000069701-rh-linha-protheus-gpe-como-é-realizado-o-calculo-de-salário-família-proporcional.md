---
article_id: 1500000069701
category: RH - Folha de Pagamento
content_hash: f4c67e3ed52a87e97b9c91486f21e184a4921f86e089edaf55e0b00c32a93cf8
fetched_at: '2026-06-28T22:44:13.426171+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como é realizado o calculo de salário família proporcional
  admissão para funcionários mensalistas
type: support-article
updated_at: '2025-08-12T13:30:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000069701-RH-Linha-Protheus-GPE-Como-%C3%A9-realizado-o-calculo-de-sal%C3%A1rio-fam%C3%ADlia-proporcional-admiss%C3%A3o-para-funcion%C3%A1rios-mensalistas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26354340494871) Tempo aproximado para leitura: **00:04:00 min**

**Dúvida**Como é realizado o calculo de salário família proporcional na admissão para funcionários mensalistas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17

**Solução**Para realizar o cálculo proporcional do salário família na admissão do empregado para funcionários mensalistas, siga as configurações abaixo:

No **modulo Configurador** realize a configuração dos parâmetros em **Ambiente > Cadastros > Parâmetros (CFGX017)**:

**- MV\_SALFP:** Calcula salário família proporcional no mês da admissão ou demissão:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000068501)

**- MV\_SALFD:** Calcula salário família proporcional sobre os dias do mês:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101159493)

No **modulo Gestão de Pessoal** cadastre a tabela S003 em **Atualizações > Definições Cálculos > Manutenção Tabelas (GPEA320)**:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101159633)

Em **Atualizações > Funcionários > Dependentes (GPEA020)** realize o cadastro do dependente:

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098944874)

O cadastro do funcionário em **Atualizações > Funcionários > Funcionários (GPEA010)**:

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000068981)

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098944834)

Cadastre as verbas referente ao salário família em **Atualizações > Definições Cálculos > Verbas (GPEA040)**:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101159893)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098944734)

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000068921)

Realize o calculo da folha em **Miscelânea > Cálculos > Por Roteiro (GPEM020)**:

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000068882)

Consulte o cálculo em **Consultas > Cálculo > Por Funcionários (GPEA090):**

**![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000069081)**

**Obs.:**Para realizar o enquadramento da cota de salário família a ser paga ao empregado o sistema sempre verificará o cadastro de funcionário, campo salário.

Este campo é que determina se o pagamento do salário família será devido ou não.

Importante é, sempre verifique se o campo de salário do cadastro do funcionário concede ou não o direito ao recebimento do salário família.

O segundo ponto a ser verificado é, se existe verbas com sim para salário família no cadastro de verbas, pois se existir e a soma do salário mais as verbas com sim para salário família for maior que o teto para pagamento da cota, o benefício não será concedido.

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
