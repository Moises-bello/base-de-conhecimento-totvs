---
article_id: 21579782591639
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 30f0dc294b7c9d1be5508d6ac99b29d0e756b475c4ab21b544c865ffd77377f0
fetched_at: '2026-06-28T22:42:08.845920+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: '   Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - GISS ON
  - Como gerar o Leiaute H6 - Construção Civil - Serviço Tomado de Prestador Residente
  no País com Nota Fiscal - Com Obra ( H | 6) ?'
type: support-article
updated_at: '2024-02-26T10:56:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21579782591639--Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-GISS-ON-Como-gerar-o-Leiaute-H6-Constru%C3%A7%C3%A3o-Civil-Servi%C3%A7o-Tomado-de-Prestador-Residente-no-Pa%C3%ADs-com-Nota-Fiscal-Com-Obra-H-6
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21579797703959) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**

Como gerar o **Leiaute H6** - **Construção Civil - Serviço Tomado de Prestador Residente no País com Nota Fiscal - Com Obra ( H | 6)** no arquivo **GISS *ONLINE***?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**  
Para gerar o arquivo **GISS *ONLINE*** com **leiaute H6** , você precisa seguir os passos abaixo:

**1.** Crie o campo **A2\_CODOBR2** e preencha com um **Código de Obra**:

*Print*:

![](https://totvssuporte.zendesk.com/attachments/token/PDU2SyT0EYu1wbtURs0cAiV2N/?name=image.png)

**2.** Vincule esse campo ao parâmetro **MV\_CODOBR2**:

*Print*:

![](https://totvssuporte.zendesk.com/attachments/token/m7RNg7eKIZhMfh7uCmZ5w8P6y/?name=inline-1449817087.png)

**3.** Na *wizard* do arquivo, indique o leiaute correto :  
  
**Leiaute H6 - Construção Civil - Serviço Tomado de Prestador Residente no País com Nota Fiscal - Com Obra ( H | 6)**

*Print*:

****![](https://tdn.totvs.com/download/attachments/643306559/image2021-10-4_19-8-7.png?version=1&modificationDate=1633385287830&api=v2)****

Atente-se ao parâmetro de **"Instr.Normativa?"** e também ao parâmetro de **"Arq Destino"** para colocar a extensão **.DAT** que é exigido no **leiaute 22º da GISS *ONLINE***.  
Após confirmação, aparecerá uma nova tela de parâmetros nas quais, deverá ser apresentada conforme *prints* abaixo:

![](https://tdn.totvs.com/download/attachments/643306559/image2021-10-4_19-8-40.png?version=1&modificationDate=1633385320280&api=v2)

**4.** Com essas configurações, o arquivo será gerado corretamente:

![](https://totvssuporte.zendesk.com/attachments/token/L90IOKxIZ3NWgUu406zOkevyd/?name=image.png)  
 

=============  
  
Segue também especificações do campo e parâmetro:

*Print:*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21579987464087)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21579987486359)

Mais informações:

<https://tdn.totvs.com/pages/releaseview.action?pageId=643306559>

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410625338647-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-GISS-ON-LINE-Manual-da-rotina-Giss-Online-novo-leiaute?source=search>
