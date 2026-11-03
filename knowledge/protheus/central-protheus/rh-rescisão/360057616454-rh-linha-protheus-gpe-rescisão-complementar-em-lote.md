---
article_id: 360057616454
category: RH - Rescisão
content_hash: f49bc225ff0d06bead5f57f987490b2a1b69333116a8bc083733ce775a071e62
fetched_at: '2026-06-28T22:43:54.430237+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Rescisão Complementar em Lote
type: support-article
updated_at: '2025-05-07T21:07:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057616454-RH-Linha-Protheus-GPE-Rescis%C3%A3o-Complementar-em-Lote
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19349262864279)**Tempo aproximado para leitura: **00:01:30 min**

**Dúvida**Como calcular Rescisão Complementar em Lote?

**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.

**Solução**

Visando atender as necessidades de nossos clientes no tocante ao cálculo de múltiplas rescisões complementares, estamos disponibilizando a nova rotina "**Rescisão Complementar em Lote**" (GPEM040C), que deverá ser incluída no menu, e que possibilitará a seleção dos funcionários aos quais a rescisão deverá ser calculada.

A nova rotina trará todos os funcionários demitidos existentes na base para seleção.

Após selecionar e clicar em "Calcular", uma tela solicitando a data de geração (que será incluída no campo RG\_DATAGER do novo cálculo) e a data de pagamento (que será usada para o pagamento da rescisão (RG\_DATAHOM), além de um checkbox para informar se a complementar será calculada por dissídio.  
  
Exemplo:  
![](https://tdn.totvs.com/download/attachments/851303763/image-2024-6-28_13-5-50.png?version=1&modificationDate=1719590751090&api=v2)  
  
![](https://tdn.totvs.com/download/attachments/851303763/image-2024-6-28_13-6-35.png?version=1&modificationDate=1719590795893&api=v2)

As informações incluídas nesta tela serão utilizadas para cálculo de todos os funcionários selecionados.

Caso não exista período aberto do roteiro de rescisão para algum dos funcionários, será informado no log que eles não foram calculados.

Exemplo:  
![](https://tdn.totvs.com/download/attachments/851303763/image-2024-6-28_13-7-20.png?version=1&modificationDate=1719590840630&api=v2)

Importante

As informação necessárias para cálculo da rescisão complementar, seja lançamento de verbas na RGB ou SRK, seja aumento salarial ocasionado por dissídio ou qualquer outra situação, deverão ser incluídas no sistema antes da execução do cálculo.

O sistema não efetuará o cálculo se for selecionado a opção "Complementar por dissídio" e não for encontrado nenhum cálculo de dissídio, apresentando uma mensagem no log de ocorrência:  
  
Exemplo:  
![](https://tdn.totvs.com/download/attachments/851303763/image-2024-6-28_13-10-32.png?version=1&modificationDate=1719591032780&api=v2)  
  
Neste cenário o cálculo deverá ser feito pela rotina padrão de rescisão (GPEM040). Da mesma forma o sistema não irá efetuar recálculo da rescisão, para este cenário também deve ser utilizada a rotina padrão.

**Saiba mais**Para adquirir maior conhecimento acesse o *link* abaixo:

<https://tdn.totvs.com/pages/releaseview.action?pageId=851303763>

[RH - Linha Protheus - GPE - Como calcular rescisão coletiva](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgtfsvTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBgGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAzNTYxNDI1My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jYWxjdWxhci1yZXNjaXMlQzMlQTNvLWNvbGV0aXZhBjsIVDoOc2VhcmNoX2lkSSIpNDI3NzRmYmMtNjkwYS00YmRhLTlkNGQtNzk0NTI0MTY1YzBjBjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSJBUkggLSBMaW5oYSBQcm90aGV1cyAtIEdQRSAtIENvbW8gY2FsY3VsYXIgcmVzY2lzw6NvIGNvbGV0aXZhBjsIVDoScmVzdWx0c19jb3VudGkC3wY%3D--da1f43f617ad1f852df34fb7600ca3548a54f882) 

[RH - Linha Protheus - GPE - É possível integrar roteiros na rotina Múltiplas Rescisões](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12998234878231-RH-Linha-Protheus-GPE-%C3%89-poss%C3%ADvel-integrar-roteiros-na-rotina-M%C3%BAltiplas-Rescis%C3%B5es-?source=search)

[RH - Linha Protheus - GPE - Como calcular rescisão complementar no Protheus sem ser por Dissídio retroativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021889631-RH-Linha-Protheus-GPE-Como-calcular-rescis%C3%A3o-complementar-no-Protheus-sem-ser-por-Diss%C3%ADdio-retroativo?source=search)
