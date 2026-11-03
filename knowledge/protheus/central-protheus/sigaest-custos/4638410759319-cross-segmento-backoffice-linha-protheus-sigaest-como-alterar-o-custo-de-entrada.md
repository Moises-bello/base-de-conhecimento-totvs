---
article_id: 4638410759319
category: SIGAEST - CUSTOS
content_hash: 7a6694beb37a48bf326fcb3933f78b6d401569ce33183c61d3b350d92bc250a8
fetched_at: '2026-06-28T22:39:00.308705+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como alterar o custo
  de entrada na transferência entre filiais
type: support-article
updated_at: '2026-05-11T17:35:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4638410759319-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-alterar-o-custo-de-entrada-na-transfer%C3%AAncia-entre-filiais
---

É possível alterar o custo de entrada da filial destino em transferências entre filiais no TOTVS Protheus configurando o parâmetro MV\_CUSTRON = .F., que calcula o custo conforme a TES de entrada e impostos. Para efeito correto, o recalculo do custo médio (rotina MATA330) deve ser feito individualmente por filial, especialmente se usar as rotinas facilitadoras MATA310/MATA311. Caso contrário, o custo da filial destino será igual ao da origem.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36881613753111) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**

É possível alterar o custo de entrada, da filial destino, sob um processo de transferência entre filiais?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Atualmente, a possibilidade para que o custo da filial DESTINO, não seja trazido o mesmo custo que a filial ORIGEM, pode-se utilizar o parâmetro [**MV\_CUSTRON**](https://tdn.totvs.com/pages/releaseview.action?pageId=573531070) **= .F.**, dessa forma o custo da filial DESTINO será calculado mediante a TES de entrada na filial, agregando assim os impostos configurados. **Além** do parâmetro MV\_CUSTRON também é importante avaliar o [**parâmetro MV\_M330TRF**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410108955415-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Diverg%C3%AAncia-de-custo-entre-Filial-Origem-e-Filial-Destino-ao-efetuar-Transfer%C3%AAncia-entre-Filiais) indicado [***nesse link***](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410108955415-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Diverg%C3%AAncia-de-custo-entre-Filial-Origem-e-Filial-Destino-ao-efetuar-Transfer%C3%AAncia-entre-Filiais) da FAQ.

**Porém**, isso terá efeito desejado, somente se durante a execução da rotina **MATA330 "Recalculo do custo médio"**, for feita de forma individual para cada filial, ou seja, não pode ser executado para **"ambas as filiais".**

***Caso utilize as rotinas facilitadoras MATA310/MATA311 para realização da transferência,**pois se tratam de rotinas facilitadoras para o processo de transferência.*

* **Por que?** Se o processamento do custo médio for para "ambas filiais", a característica da rotina é executar **conjugadamente em duas ou mais filiais** a fim descarregar o **custo igualmente entre elas no processo de transferência independente do MV\_CUSTRON ser .F. ou .T..** **"Pois se trata dessa forma, um movimento interno".**

**Para um melhor entendimento, abaixo segue:**

**1- O processamento do custo médio, para "ambas filiais"**

considerando o MV\_CUSTRON = .T., e .F. note que o custo de DESTINO, é o mesmo da origem, sempre, pois foi gravado como um movimento interno, de acordo [**TRB\_ORDEM**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005800542-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Como-%C3%A9-feita-a-ordena%C3%A7%C3%A3o-dos-movimentos-no-Rec%C3%A1lculo-do-Custo-M%C3%A9dio-) **300**, por conta do processamento do custo médio, ser para ambas filiais.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4638004847127)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4638048355479)

**2- Processando de forma "individual":**

considerando o parâmetro MV\_CUSTRON = .F. e .T., note que como **.F.** se processado de forma individual, a filial destino, não assumo o custo da **ORIGEM**, e sim é calculado de acordo a TES de entrada, com a configuração de imposto aglutinado, que nesse caso se trata do ICMS, mas caso o parâmetro esteja ATIVO = .T. ele vai assumir o custo **"online"** ou seja, da Origem.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4638126995351)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4638280566295)

Então caso queira alterar o custo de entrada, na transferência entre filiais, **se deve configurar o parâmetro MV\_CUSTRON = .F.** e processar o recalculo do custo médio, **de forma individual por filial**, **apenas caso utilize a rotina facilitadora MATA310/MATA311 para realização do processo de transferência entre filiais.**

***Saiba mais:***

[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)

[SIGAEST - Divergência de custo entre Filial Origem e Filial Destino ao efetuar Transferência entre Filiais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410108955415-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Diverg%C3%AAncia-de-custo-entre-Filial-Origem-e-Filial-Destino-ao-efetuar-Transfer%C3%AAncia-entre-Filiais)

[MP - SIGAEST – Custo nas transferências entre filiais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024874171-MP-SIGAEST-Custo-nas-transfer%C3%AAncias-entre-filiais)
