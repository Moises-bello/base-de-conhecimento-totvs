---
article_id: 360050095774
category: RH - Folha de Pagamento
content_hash: 0ed4fe50de24750c310ae77285174b0d6445e154bd79cc9b4643b89517da47f3
fetched_at: '2026-06-28T22:44:13.638645+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como parametrizar folha de pagamento e rescisão
  com rateio
type: support-article
updated_at: '2025-06-13T18:32:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050095774-RH-Linha-Protheus-GPE-Como-parametrizar-folha-de-pagamento-e-rescis%C3%A3o-com-rateio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22647161537815) Tempo aproximado para leitura: 00:03:00 min

Dúvida  
Como parametrizar folha de pagamento e rescisão com rateio?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**A folha de pagamento pode ser rateada por centro de custo, item contábil e classe valor (*MV\_ITMCLVC*) conforme necessidade da empresa. Para que o cálculo do rateio seja habilitado, o sistema valida as seguintes informações:  
  
1. Atualizações/Cadastros/Centros de Custos:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077413833)

As informações desta rotina serão armazenadas na tabela **CTT**.  
  
2. Atualizações/Funcionário/Funcionários:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076229154)

Observe que o centro de custo original do empregado é 01. As informações desta rotina serão armazenadas na tabela **SRA**.  
  
3. Atualizações/Funcionários/Programação de Rateio:

Para que as colunas Item Contábil e Classe Valor sejam apresentadas na tela de rateio, o cliente deverá estar com o MV\_ITMCLVL habilitado, esta funcionalidade permitirá ao cliente efetuar o rateio por item e classe de valor. Quando este parâmetro estiver habilitado o sistema apresentará os campos Item e Classe no cadastro do funcionário para que seja informado.  
  
No cenário deste TESTE o MV\_ITMCLVL está desabilitado pois faremos o rateio apenas por CC.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26080544395927)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077432993)

As informações desta rotina serão armazenadas na tabela**RHQ.**4. **SIGACFG**: Ambiente/Cadastros/Parâmetros:  
Esse parâmetro permite o rateio das verbas na Folha e na Provisão.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077398793)

As informações desta rotina serão armazenadas na tabela **SX6**.  
  
5. Atualizações/Cadastros/Verbas:

No campo **RV\_ENCARCC** da aba **Contabilização** informar a opção **B** apenas para a verba de salário ou verbas que farão base para o rateio e as demais, deverão estar como **S**ou**N** (caso não queira efetuar o rateio).  
  
O que significa cada opção do campo RV\_ENCARCC:

**- "B"** para as verbas que formarão a base da divisão para rateio de centro de custo.

**- "S"** para as verbas que serão rateadas por centro de custo.

**- "N"** para as verbas que não serão rateadas por centro de custo.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076248754)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077411113)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077412933)

As informações desta rotina serão armazenadas na tabela **SRV.**6.Miscelânea/Cálculos/Por Roteiro:

**![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077411573)**

7.Atualizações/Consultas/Cálculos/Por Funcionário:

**![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076247414)**

**![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077411893)**

**Resumo do cálculo:**O sistema está gerando 50% para o centro de custo 01 e 02 conforme informamos no GPEA056- Programação do rateio por centro de custo.  
Com isto, observe que a soma: **1.481,42 verba 001 (cc 01) + 1.481,43 verba 001 (cc 02) + 1.693,06 verba 027 (cc 01) + 1.693,06 verba 027 (cc 02)= 6.348,97** que refere-se ao valor total do salário do empregado. Assim será realizado para as demais verbas.  
  
**Cálculo das férias para conferência das demais verbas:**

**![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077411933)**

**![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077411993)**

Após parametrizar o rateio ao calcular rescisão a mesma será rateada.

Obs: O campo **RV\_ENCARCC**  das verbas do calculo da rescisão devem estar parametrizadas conforme demonstrado no item 5 em Atualizações/Cadastros/Verbas.

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077412093)

![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077412133)

**Saiba mais**[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
