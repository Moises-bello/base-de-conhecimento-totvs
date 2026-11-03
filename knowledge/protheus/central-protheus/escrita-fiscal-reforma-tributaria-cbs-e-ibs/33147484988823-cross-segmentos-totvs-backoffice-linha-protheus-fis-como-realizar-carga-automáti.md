---
article_id: 33147484988823
category: Escrita Fiscal - Reforma Tributaria - CBS e IBS
content_hash: d80925a57baabdf0ec040bbbd5a69a0ccf16bd60e0049901bdac65e30e29b960
fetched_at: '2026-06-28T22:39:15.816208+00:00'
product: protheus
section_id: 33305945453079
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como realizar carga
  automática dos Tributos CBS e IBS no Configurador de Tributos?
type: support-article
updated_at: '2025-11-04T21:12:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33147484988823-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-realizar-carga-autom%C3%A1tica-dos-Tributos-CBS-e-IBS-no-Configurador-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33147484970903) Tempo aproximado para leitura: **00:10:00 min**  
**Dúvida**

**Como realizar carga automática dos Tributos CBS e IBS no Configurador de Tributos?**  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

Foi desenvolvida uma funcionalidade para realizar, de forma automática, a carga dos cadastros na **filial logada**, com vigência para o ano de **2026**e **Status (F2B\_STATUS)** = "Em Teste":

A carga automática pode ser executada através do seguinte caminho no sistema: **Regra de Cálculo - Documentos Fiscais → Outras Ações → Carga Regras de Cálculo CBS/IBS**

**![](https://tdn.totvs.com/download/attachments/960010301/image-2025-6-24_17-2-14.png?version=1&modificationDate=1750795334147&api=v2)**

Ao selecionar a opção, será exibida uma tela solicitando a confirmação da operação.

![](https://tdn.totvs.com/download/attachments/960010301/image-2025-6-24_17-13-10.png?version=1&modificationDate=1750795990180&api=v2)

Após o processamento, uma mensagem informará o sucesso na inclusão dos cadastros para a filial.

![](https://tdn.totvs.com/download/attachments/960010301/image-2025-6-24_17-13-20.png?version=1&modificationDate=1750796000330&api=v2)

Perfil de Produto

Nesse perfil todos os produtos serão considerados, porém o mesmo pode ser alterado.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34902015464215)

Perfil de Participante

Nesse perfil serão considerados todos os fornecedores e clientes, porém podem alterar o perfil conforme necessidade.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34902015468567)

Perfil de Origem e Destino

Será utilizado o perfil 000002 -  Todas as UFS onde todos os estados estão configurados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34902015469335)

Perfil de Operação

Será utilizado o perfil 000051 - Todos os CFOPS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34901975117719)

Regra de Base de cálculo CBS/IBS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34902015473175)

A regra da Base de cálculo será a seguinte:

**( O:VAL\_MERCADORIA + O:FRETE + O:SEGURO + O:DESPESAS + O:VAL\_II ) - ( O:DESCONTO + O:VAL\_PS2 + O:VAL\_CF2 + O:VAL\_ICMS + O:VAL\_DIFAL + O:VAL\_FECP + O:VAL\_FCPDIF + O:VAL\_ISS )**

Assim como os demais cadastros, caso necessário a memória da base pode ser alterada para seu cenário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34902015474071)

Regra de Alíquota CBS e IBS

TA0001 - CBSFED

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34901975125655)

TA0002 - IBSEST

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34902015475607)

Regra de cálculo - Documentos Fiscais

TR0001 - CBSFED

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34901975129367)

No campo Escrituração informe a Regra de Escrituração criada para o CBS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34901975130391)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34901975131671)

TR0002 - IBSEST

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34901975133463)

No campo Escrituração informe a Regra de Escrituração criada para o IBS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34901975130391)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34901975131671)

## **ESCRITURAÇÃO DA NOTA COM OPERANDOS LEGADOS NO CONFIGURADOR DE TRIBUTOS**

### 4.1 Operações com operandos legados

Operações com tributos sendo calculados pela TES que afetam a Base de Cálculo.

**Exemplo de aplicação:**

A nota possui os seguintes valores:

* + Valor total **(O:VAL\_MERCADORIA + O:FRETE + O:DESPESAS ): R$ 11.038,45**
  + Valor de ICMS **( O:VAL\_ICMS ): R$ 1.986,92**
  + Valor de PIS **( O:VAL\_PS2 ) : R$ 165,00**
  + Valor de COFINS **( O:VAL\_CF2 ): R$ 760,00**

A Base de Cálculo do CBS cadastrada foi: **( O:VAL\_MERCADORIA + O:FRETE + O:SEGURO + O:DESPESAS + O:VAL\_II ) - ( O:DESCONTO + O:VAL\_PS2 + O:VAL\_CF2 + O:VAL\_ICMS + O:VAL\_DIFAL + O:VAL\_FECP + O:VAL\_FCPDIF + O:VAL\_ISS )**

Aplicando os valores = **R$ 11.038,45 - (R$ 1.986,92 + R$ 165,00 + R$ 760,00) = R$ 8.126,53**

![](https://tdn.totvs.com/download/attachments/960010301/image-2025-6-24_17-19-5.png?version=1&modificationDate=1750796345857&api=v2)

Observe que o ICMS, PIS e COFINS não foram implementados via Configurador de Tributos, mas estão sendo considerados por meio do cadastro da TES. Como os operandos desses tributos foram informados na Base de Cálculo, eles foram incluídos no cálculo normalmente.

### 4.1 Operações com operandos implementados no Configurador de Tributos (Exemplo: ICMS, PIS e COFINS)

Operações com todos os tributos sendo calculados pelo Configurador de Tributos.

**Exemplo de aplicação:**

A nota possui os seguintes valores:

* + - Valor total **(O:VAL\_MERCADORIA ): R$ 10.000,00**
    - Valor de ICMS **( O:VAL\_ICMS ): R$ 1.800,00**
    - Valor de PIS **( O:VAL\_PS2 ) : R$ 165,00**
    - Valor de COFINS **( O:VAL\_CF2 ): R$ 760,00**

A Base de Cálculo do **CBS**e do **IBS** cadastrada foi: **( O:VAL\_MERCADORIA + O:FRETE + O:SEGURO + O:DESPESAS + O:VAL\_II ) - ( O:DESCONTO + O:VAL\_PS2 + O:VAL\_CF2 + O:VAL\_ICMS + O:VAL\_DIFAL + O:VAL\_FECP + O:VAL\_FCPDIF + O:VAL\_ISS )**

Aplicando os valores = **R$ 10.000,00 - (R$ 1.800,00 + R$ 165,00 + R$ 760,00) = R$ 7.275,00**

**![](https://tdn.totvs.com/download/attachments/960010301/image-2025-6-24_17-56-53.png?version=1&modificationDate=1750798613830&api=v2)**

Observe que o ICMS, PIS e COFINS foram implementados via Configurador de Tributos e o cálculo também considera as referências dos operandos como se fossem do Configurador de Tributos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34901975136663)

Para mais informações valide a documentação abaixo:

[**https://tdn.totvs.com/pages/releaseview.action?pageId=960010301**](https://tdn.totvs.com/pages/releaseview.action?pageId=960010301)
