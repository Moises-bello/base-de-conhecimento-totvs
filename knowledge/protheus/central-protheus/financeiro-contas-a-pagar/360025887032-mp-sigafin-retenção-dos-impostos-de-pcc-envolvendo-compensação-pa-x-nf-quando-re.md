---
article_id: 360025887032
category: Financeiro - Contas a Pagar
content_hash: 4821eb8e51d9232607ca3cb79c6a828d284693707c46e84ecc57a223e1731320
fetched_at: '2026-06-28T22:38:09.962047+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: MP - SIGAFIN - Retenção dos impostos de PCC envolvendo compensação PA X NF
  quando retenção destes impostos é na emissão
type: support-article
updated_at: '2021-04-28T15:18:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025887032-MP-SIGAFIN-Reten%C3%A7%C3%A3o-dos-impostos-de-PCC-envolvendo-compensa%C3%A7%C3%A3o-PA-X-NF-quando-reten%C3%A7%C3%A3o-destes-impostos-%C3%A9-na-emiss%C3%A3o
---

**Dúvida**Retenção dos impostos de PIS/COFINS/CSLL envolvendo compensação PA X NF quando retenção destes impostos é na emissão?

**Ambiente**Microsiga Protheus – Financeiro – A partir da versão 12  
   
**Solução**Sabendo que o fato gerador da retenção dos impostos de PCC (PIS/COFINS/CSLL) é o **pagamento**, ou seja, a retenção dos impostos deverá ocorrer obrigatoriamente na **inclusão do pagamento antecipado(PA)**, pois neste momento ocorre a saída do dinheiro do caixa da empresa.

O parâmetro **MV\_BX10925**=**1**(Baixa), a retenção neste caso será na baixa do título, mas conforme a explicação acima, assim que incluir o PA será criado os títulos **TX** correspondente a cada imposto. No exemplo abaixo, foi incluído PA do valor de R$10.000,00, e o valor gerado para visualização deste **PA** será valor liquido devido o parâmetro: **MV\_PABRUTO** estar com conteúdo 2, sendo assim é aconselhável que os parâmetros abaixo estejam preenchidos da seguinte maneira visto que o **MV\_PABRUTO** = **2**:

* **MV\_COMPCP** = **.T.** - Indica se na compensação de uma NF com um PA os impostos serão proporcionalizados.
* **MV\_BP10925** = **2** - Considera valor Líquido na baixa Parcial descontados os impostos.
* **MV\_PAPRIME**= **1** - Considera provisionamento de impostos para PA Líquido.

![](http://tdn.totvs.com/download/attachments/361453196/image2018-5-17_9-53-28.png?version=1&modificationDate=1526561611000&api=v2)

Quando emitir a nota fiscal do valor que é R$10.000,00. Quando realizar a Compensação(FINA340) embora o valor do PA esteja apresentando valor líquido, compensará o valor total da nota fiscal:

![](http://tdn.totvs.com/download/attachments/361453196/image2018-5-18_16-17-30.png?version=1&modificationDate=1526671051000&api=v2)

Após compensação do PA do valor R$9.535,00 com NF R$10.00,00 tanto PA quanto a NF serão compensados sobre valor total, conforme prints da posição de título abaixo deixando saldo 0 em ambos os títulos:

![](http://tdn.totvs.com/download/attachments/361453196/image2018-5-18_16-26-32.png?version=1&modificationDate=1526671593000&api=v2)

![](http://tdn.totvs.com/download/attachments/361453196/image2018-5-18_16-30-31.png?version=1&modificationDate=1526671832000&api=v2)

**Cenário 2 Valor Bruto do PA:** Conforme podemos observar, não gerou TX quando baixou a NF após a compensação, pois não há como reter os impostos no momento da compensação. Pois caso houvesse essa possibilidade, seria uma duplicidade de retenção. Pois os títulos TX já foram gerados mo momento da inclusão do PA(Pagamento Antecipado), lembrando que o fator gerador é o pagamento., por isso que é gerado os títulos de impostos de PCC(PIS/COFINS/CSLL) na inclusão do PA.

Quando o parâmetro **MV\_PABRUTO** estiver igual a **1** (Bruto)  ao gerar títulos do tipo PA (Pagamentos Antecipados), é gerado com o valor bruto, não descontando os valores de impostos que podem ser retidos na inclusão. Então a compensação de uma NF com uma PA, deveria ser pelo valor bruto configurando os parâmetros conforme abaixo:

* **MV\_PABRUTO** = 1 - Bruto e **MV\_BX10925** = 1 Imposto na baixa ou **MV\_BX10925=2** Imposto na emissão
* **MV\_BP10925** = 1  - Considera valor Bruto na baixa Parcial sem descontar os impostos.
* **MV\_PAPRIME** = 2 - Não considera provisionamento de impostos para PA Líquido.

Através da configuração dos parâmetros acima, conforme imagem abaixo, foi gerado um PA com valor bruto R$6.000,00 e não foi descontado os impostos sobre o valor do PA.

![](http://tdn.totvs.com/download/attachments/361453196/image2018-5-24_15-8-41.png?version=1&modificationDate=1527185322000&api=v2)

Observação.:

O parâmetro **MV\_COMPCP** não influencia caso o parâmetro **MV\_PABRUTO** esteja com o valor em **1**. Independente do **título** possuir **impostos**, ou não, é necessário a parametrização.

Se tratando do cenário **BRUTO**, acesse também a nossa FAQ abaixo:  
[FIN0071\_CPAG\_Compensação\_CP\_BRUTO](http://tdn.totvs.com/pages/viewpage.action?pageId=269089955)

**Importante:**Geração de impostos no pagamento antecipado e compensação de adiantamento  
<http://tdn.totvs.com.br/pages/releaseview.action?pageId=73083918>

A **compensação** entre **NF** x **PA**, partindo tanto da **NF** como do **PA**, não é permitida caso o parâmetro **MV\_PABRUTO** = 2 (**líquido**) e as naturezas estiverem diferentes.

#
