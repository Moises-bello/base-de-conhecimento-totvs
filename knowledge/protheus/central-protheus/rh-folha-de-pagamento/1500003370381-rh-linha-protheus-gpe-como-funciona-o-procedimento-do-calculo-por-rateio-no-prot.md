---
article_id: 1500003370381
category: RH - Folha de Pagamento
content_hash: 2de181e992c97d8df9d254b5ad1e208eb2fc807700b0e7644640351a85f5c82f
fetched_at: '2026-06-28T22:44:13.522425+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como funciona o procedimento do calculo por rateio
  no Protheus
type: support-article
updated_at: '2025-08-11T21:05:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003370381-RH-Linha-Protheus-GPE-Como-funciona-o-procedimento-do-calculo-por-rateio-no-Protheus
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26337610305303) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**Como funciona o procedimento do calculo por rateio no Protheus?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução** **1.** Em Atualizações -> Cadastros -> Centros de Custos:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360104597953)

- As informações desta rotina serão armazenadas na tabela **CTT**.

**2.** Em Atualizações -> Funcionário -> Funcionários:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360104598073)

- Observe que o centro de custo original do empregado é 01.

As informações desta rotina serão armazenadas na tabela **SRA**.

**3.** Em Atualizações -> Funcionários -> Programação de Rateio:

Para que as colunas Item Contábil e Classe Valor sejam apresentadas na tela de rateio, deverá estar com o **MV\_ITMCLVL** habilitado, esta nova funcionalidade permitirá efetuar o rateio por item e classe de valor.

- Quando este parâmetro estiver habilitado o sistema apresentará os campos Item e Classe no cadastro do funcionário para que seja informado.

- No cenário deste TESTE o MV\_ITMCLVL está desabilitado pois faremos o rateio apenas por CC.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102419454)

- As informações desta rotina serão armazenadas na tabela**RHQ.**

**4.** Em SIGACFG modulo configurador: Ambiente -> Cadastros -> Parâmetros:

- Esse parâmetro permite o rateio das verbas na Folha e na Provisão.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003539482)

- As informações desta rotina serão armazenadas na tabela **SX6**.

**5.** Em Atualizações -> Cadastros -> Verbas:

No campo **RV\_ENCARCC**da aba **Contabilização** temos as seguintes opções de preenchimento:

**- "B"** para as verbas que formarão a base da divisão para rateio de centro de custo.

**- "S"** para as verbas que serão rateadas por centro de custo.

**- "N"** para as verbas que não serão rateadas por centro de custo.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360104598293)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003539522)

- As informações desta rotina serão armazenadas na tabela **SRV.**

No exemplo abaixo utilizamos as verbas de **salário** e de **férias** configuradas com **B** no campo **RV\_ENCARCC**e **S** para as demais que gostaríamos que fossem rateadas no cálculo.

**6.** Em Miscelânea -> Cálculos -> Por Roteiro:

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003539542)

**7.** Em Atualizações -> Consultas -> Cálculos -> Por Funcionário:

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360104598333)

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003539582)

**Resumo do cálculo:**

O sistema está gerando 50% para o centro de custo 01 e 02 conforme informamos no GPEA056- Programação do rateio por centro de custo.

Com isto, observe que a soma: **1.481,42 verba 001 (cc01) + 1.481,43 verba 002 (cc02) + 1.693,06 verba 027 (cc01) + 1.693,06 verba 027 (cc02)= 6.348,97** que refere-se ao valor total do salário do empregado.

Assim será realizado para as demais verbas.

**- Cálculo das férias para conferência das demais verbas:**

**![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003587241)**

**Saiba Mais**

[RH - Linha Protheus - GPE - Como realizar a programação de rateio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018658931-RH-Linha-Protheus-GPE-Como-realizar-a-programa%C3%A7%C3%A3o-de-rateio)

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
