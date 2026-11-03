---
article_id: 360054064254
category: RH - Benefícios
content_hash: ba3926ea17a2d9539307700623574765cc404b27d7ce4ec5fd324c5660f5c1c4
fetched_at: '2026-06-28T22:44:03.702097+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular benefício VT/VR/VA apenas para dias
  Não trabalhados - Não úteis
type: support-article
updated_at: '2025-10-02T13:40:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054064254-RH-Linha-Protheus-GPE-Como-calcular-benef%C3%ADcio-VT-VR-VA-apenas-para-dias-N%C3%A3o-trabalhados-N%C3%A3o-%C3%BAteis
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26956175491351) Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Como calcular benefício VT/VR/VA **apenas** para dias Não trabalhados - Não úteis?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**O que pode ser feito para comprar apenas para os dias não úteis - Final de Semana nesse exemplo, é amarrar o turno do funcionário no Cadastro de Período (Aba Calendário), e deixar com sim para VT/VR/VA somente para os finais de semana.

Para isso, siga este passo a passo, o qual utilizamos como exemplo o cálculo de VT: 

**1-** Acessar em **Atualizações> Definições de Cálculo> Períodos;**  
![](https://totvssuporte.zendesk.com/attachments/token/e7Zx2z1txP8U8BXLIjLKeKfe4/?name=inline1471449854.png)​

**2-** Selecionar o período correspondente ao cálculo e clique em **Alterar**;  
![](https://totvssuporte.zendesk.com/attachments/token/uTvaYJUvLlA524lkZYbEFK0ja/?name=inline419776218.png)​

**3-** Clicar na aba **Calendário;**  
![](https://totvssuporte.zendesk.com/attachments/token/DTzgzMQXQEsvmMJYIOUy2C8vX/?name=inline-1521110856.png)​

**4-** No Grid superior, crie mais uma linha (seta para baixo), e informe o turno do funcionário;  
![](https://totvssuporte.zendesk.com/attachments/token/NpjZYDddsGDfiOI9vFpypUSxF/?name=inline-1804642406.png)​

**5-** No Grid inferior, altere para Não os campos referente a VT/VR/VA para os dias da semana e altere para Sim os campos para os finais de semana (Nesse exemplo vou usar o VT mas o conceito é o mesmo para qualquer um deles) e salve;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33145163998359)  
​​  
  
  
**6-** Após isso, entre na atualização do Benefício e informe o código do benefício, coloque 1 no campo Qt. Vale D Util (Apenas para que tenha a informação) e a quantidade necessária no campo Qt. Vale D N Util, que nesse exemplo considerei que ele usa 2 meios por dia, e salve;  
![](https://totvssuporte.zendesk.com/attachments/token/qcJ5QfLI3rmRLRODI8uNeMUru/?name=inline-2133765010.png)​  
  
  
**7-** Efetue o cálculo, onde sistema processará o cálculo apenas para os Finais de semana, visto que são os únicos dias que estão com Sim para VT/VR/VA;  
![](https://totvssuporte.zendesk.com/attachments/token/NWb3gbb5hF6bWHlW3CRbIp26L/?name=inline2053860601.png)​

![](https://totvssuporte.zendesk.com/attachments/token/Bn5asU1hco1LE6eKZreL28SS8/?name=inline-1044884126.png)​

![](https://totvssuporte.zendesk.com/attachments/token/r4pkRiQ4XKFUhn1AHwbDwRnhg/?name=inline462193213.png)​

**8-** Consulta do Cálculo: Veja que para os dias Úteis ficou com 0 visto que configuramos com Não para VT no Calendário para esses dias, e para os dias Não Úteis, ficou com 8 conforme também configuramos o calendário, e o total de vales 16, visto que são 2 vales por dia - 8 (Dias) \* 2 (Vales por dia) = 16 vales no total.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093064773)

**Saiba Mais**[RH - Linha Protheus - GPE - Como utilizar parâmetro MV\_CVTPROP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014665512-RH-Linha-Protheus-GPE-Como-utilizar-par%C3%A2metro-MV-CVTPROP?source=search)  
[RH - Linha Protheus - GPE - Rotinas envolvidas nos cálculos de Benefícios (VT/VR/VA)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050523113-RH-Linha-Protheus-GPE-Rotinas-envolvidas-nos-c%C3%A1lculos-de-Benef%C3%ADcios-VT-VR-VA)  
[RH - Linha Protheus - GPE - Cálculo avulso para Vale Transporte, Vale Refeição e Vale Alimentação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049769114-RH-Linha-Protheus-GPE-C%C3%A1lculo-avulso-para-Vale-Transporte-Vale-Refei%C3%A7%C3%A3o-e-Vale-Alimenta%C3%A7%C3%A3o?source=search)
