---
article_id: 360025386194
category: NFe - Nota Fiscal Eletrônica
content_hash: 4e1715eb32c9a800bb87cc01784df98b79cdc7816c28a3e0df755a8842dbce12
fetched_at: '2026-06-28T22:40:01.738034+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar as
  TAGs de Difal no XML '
type: support-article
updated_at: '2023-10-11T17:27:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025386194--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-as-TAGs-de-Difal-no-XML
---

**Dúvida**Como gerar as TAGs de Difal no XML ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Para gerar as TAGS do **Difal a nota** precisa ser:

1- Preencher para consumidor final o campo no pedido de vendas **Tipo cliente:**

**C5\_TIPOCLI" = F**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040201233)

**(se nota de devolução com cliente ou utiliza cadastro de cliente)** informar no cadastro de cliente A1\_TIPO = F (consumidor final).

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412652536983)

2- Essa operação deve ser interestadual, ou seja quando a nota é gerada com **CFOP de operação interestadual:**

**Operação fora do Estado**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039357034)

3- Preencher no cadastro de cliente  como não contribuinte **Cadastro de Cliente não contribuinte:**

1- Preencha a inscrição estadual no campo  Ins. Estad. **"A1\_INSCR" ou deixe em Branco (caso não tenha inscrição)**

![](https://totvssuporte.zendesk.com/attachments/token/F28rwEzItrBoQEVD6unisbVWf/?name=inline2138881771.png)​

2- Preencha o campo Destaca IE **"A1\_IECONT"**  1- Sim

![](https://totvssuporte.zendesk.com/attachments/token/mL279biwk84pyy9o3nV2hwcwc/?name=inline135028164.png)

3- Preencha o campo Contribuinte **"A1\_CONTRIB"**  2 - Não

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18198547491223)

* **Saiba mais:**

 Se houver o grupo de combustível na nota e não estiver gerando **o grupo do Difal e a mensagem no XML.**

* **Exemplo:**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087064213)**

Conforme a validação da **rejeição 694**  
  
[MP - NFE - Rejeição - 694: Não informado o grupo de ICMS para a UF de destino](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020228691-MP-NFE-Rejei%C3%A7%C3%A3o-694-N%C3%A3o-informado-o-grupo-de-ICMS-para-a-UF-de-destino?source=search)  
  
  
Só pode ser gerado o grupo do Difal para os **códigos ANP abaixo:**  
  
![](https://totvssuporte.zendesk.com/attachments/token/OHea2uCodlpKHobkcmKmNotOr/?name=inline-1766014642.png)​​

* **NFESEFAZ:**

![](https://totvssuporte.zendesk.com/attachments/token/LrLVS2VUCLmOGGp4gKmw5ssJw/?name=inline315346167.png)​  
  
  
​​  
Se for gerado para **códigos diferentes do acima ocorrerá a rejeição 695.**  
  
[Nota Técnica 2015.003 - v 1.94](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=DRiCiO978HY=)  
  
**Página 19.**  
  
  
Para gerar o grupo do Difal e a mensagem deve ser utilizado um desses código da ANP acima.

* Conforme a Nota técnica **2016.002\_v\_1.61 página 76** os valores do FCP devem ser gerados em  informações adicionais do produto e na TAG infadfisco:

[Nota Técnica 2016.002 - v 1.61 (publicada em 10/09/2018)](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=zfWxcJtOf98=)

**![FECP.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/18198523914135)**

**IMPORTANTE:**

Quando houver Difal + FECP não haverá o mesmo destaque, pois, ao calcular o Difal as TAGS são diferentes do previsto na nota técnica:

* **<vBCUFDest>** **Base do FCP**
* **<pFCPUFDest>** **Percentual do FCP**
* **<vFCPUFDest>****Valor do FCP**

**![CD2_FECP.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/18198510318615)**

* **Exemplo** Grupo do Difal:

**![DIFAL_FECP.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/18198510323991)**

* A única mensagem prevista para esse grupo de **Difal + Fcp** prevista pela Sefaz:

**<infCpl>** Valor do ICMS relativo ao Fundo de Combate a Pobreza - FCP da UF de destino: R$ 20.00. Valor do ICMS  Interestadual para a UF de destino: R$ 48.00. Valor do ICMS

   Interestadual para a UF do remetente: R$ 12.00.**</infCpl>**

* **Saiba mais:**

Existe um parecer da consultoria da TOTVS referente as informações geradas na**TAG infcpl ou infadfisco:**

*[Parecer da consultoria](https://tdn.totvs.com/pages/releaseview.action?pageId=361433612)*

Para gerar uma mensagem diferente do previsto na **Nota técnica,**  para que o XML e o Danfe atenda sua necessidade há**três opções de processos** a ser seguido:

1- Primeira opção podem ser utilizados os **campos padrões do sistema das documentações abaixo:**

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar mensagem em informações complementares (TAG infcpl e infadfisco) do Danfe utilizando fórmula](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026944871)

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar informações na TAG infCpl ou infAdFisco no XML e no DANFE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024950773)

2- Segunda opção pode ser customizado o **NFESEFAZ .**  
  
 *[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Documentos Eletrônicos NFe (Rdmake NFESEFAZ, DANFE) / NFSe / MDFe / MDe](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043005493)*   
  
**Rdmake disponível no link acima.**  
  
3- Terceira opção pode ser aberto **melhoria na Central Colaborativa:**  
  
[***Central Colaborativa TOTVS.***](https://centraldeatendimento.totvs.com/hc/contributions/posts?locale=pt-br)  
Para saber como criar uma sugestão de melhoria clique **[*AQUI.*](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics)**

* Validação da SEFAZ:

![rejei__o_694.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360097338514)
