---
article_id: 21580473870103
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 307971f5297e53c47caede6a7db5f7135961d55486e7607151f28561488dd8ff
fetched_at: '2026-06-28T22:42:08.857509+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: '   Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - GISS ON
  - Como gerar o Leiaute I3 - Construção Civil - Serviço Tomado Prestador Residente
  no País com Nota Fiscal - Sem Obra (I | 3) ?'
type: support-article
updated_at: '2024-02-26T16:40:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21580473870103--Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-GISS-ON-Como-gerar-o-Leiaute-I3-Constru%C3%A7%C3%A3o-Civil-Servi%C3%A7o-Tomado-Prestador-Residente-no-Pa%C3%ADs-com-Nota-Fiscal-Sem-Obra-I-3
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21580473797783) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**

Como gerar o **Leiaute I3** - **Construção Civil - Serviço Tomado Prestador Residente no País com Nota Fiscal - Sem Obra (I | 3)** no arquivo **GISS *ONLINE***?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**  
Para gerar o arquivo **GISS ON** com **leiaute I3** , você precisa seguir os passos abaixo:

**1.** Crie o campo **A2\_CODOBR2** e preenche-lo com o conteúdo = **"SEM CODIGO"** conforme abaixo:

![](https://totvssuporte.zendesk.com/attachments/token/EUp5J6ow9WPzVvmNFHlMFFN9j/?name=inline-1711431085.png)

**2.** Vincule esse campo ao parâmetro **MV\_CODOBR2**:

![](https://totvssuporte.zendesk.com/attachments/token/m7RNg7eKIZhMfh7uCmZ5w8P6y/?name=inline-1449817087.png)

**3.** Na *wizard* do arquivo, indique o leiaute correto :  
  
**Leiaute I3 - Construção Civil - Serviço Tomado Prestador Residente no País com Nota Fiscal - Sem Obra (I | 3)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/21580473799703)**

Atente-se ao parâmetro de **"Instr.Normativa?"** e também ao parâmetro de **"Arq Destino"** para colocar a extensão **.DAT** que é exigido no **leiaute 22º da GISS *ONLINE***.

Depois de confirmar, aparecerá uma nova tela de parâmetros nas quais deverá da forma como está abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21580480862999)

**4.** Com essas configurações o arquivo será gerado corretamente:

![](https://totvssuporte.zendesk.com/attachments/token/KiJnGYKoXPOUpkcBHrl34baXt/?name=inline1937969030.png)  
 

=============  
  
Segue também especificações do campo e parâmetro::

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21580473805975)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21580473807255)

Mais informações:

<https://tdn.totvs.com/pages/releaseview.action?pageId=643306559>

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410625338647-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-GISS-ON-LINE-Manual-da-rotina-Giss-Online-novo-leiaute?source=search>
