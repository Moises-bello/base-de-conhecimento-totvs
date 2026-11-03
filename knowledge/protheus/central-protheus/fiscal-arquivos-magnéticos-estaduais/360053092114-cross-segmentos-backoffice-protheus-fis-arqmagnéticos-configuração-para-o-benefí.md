---
article_id: 360053092114
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 99a90b1850736f6339cae9739f767a36dc96d4897323d0603af1a3a00da535b5
fetched_at: '2026-06-28T22:42:10.391597+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Configuração
  para o benefício Crédito Presumido ser considerado no relatório DUB ICMS (FISR001)
type: support-article
updated_at: '2022-08-17T20:06:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053092114-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Configura%C3%A7%C3%A3o-para-o-benef%C3%ADcio-Cr%C3%A9dito-Presumido-ser-considerado-no-relat%C3%B3rio-DUB-ICMS-FISR001
---

**Dúvida**

Qual a configuração para o benefício Crédito Presumido ser considerado no relatório DUB ICMS?

**Ambiente**Microsiga - Livros Fiscais - a partir da versão 11.80

**Solução**

É importante frisar que para a operação ser eleita para entrar com valor no relatório **FISR001**, é necessário que o campo de "**Calcula ICMS**" (**F4\_ICM**) no cadastro de **TES** esteja como "**S -Sim**" e o "**L.Fisc.ICMS**" (**F4\_LFICM**) como "**I - Isento**" ou "**O - Outros**", dessa forma a operação estará correta, pois terá o **cálculo de ICMS** que servirá para o relatório e não irá gerar **débitos** ou **créditos** no **Livro Fiscal**.

**Tipo DUB (F4\_TIPODUB)** - Indica o Tipo do Ato Legal utilizado no DUB-ICMS.

1=Convênio;

2=Lei;

3=Decreto;

4=Protocolo;

5=Resolução;

6=Portaria.

**Benefic. DUB (F4\_BENDUB)** - Indica a Espécie do benefício utilizado no DUB-ICMS.

5=Cred. Presumido;

**Num./Ano DUB (F4\_NUMDUB)** - Indica o Número de identificação do Ato Legal e o Ano de Publicação utilizado no DUB-ICMS. Deve ser preenchido com o Número do Ato Legal / Ano do Ato Legal. Exemplo: 12345/2008.

**Crédito Presumido**

Os valores são obtidos através dos campos **Crd. Pres.** (F3\_CRDPRES) ou **Crd.Transp.** (F3\_CRDTRAN). Para gerar o crédito presumido na operação das notas fiscais, os campos **Crd.Pres.** (F4\_CRDPRES) ou **Crd.Transp.** (F4\_CRDTRAN), no cadastro de TES, deve ser preenchido com o percentual do crédito presumido a ser aplicado na operação.

Informações adicionais:

<https://tdninterno.totvs.com/pages/releaseview.action?pageId=557344795>

<https://tdn.totvs.com/pages/releaseview.action?pageId=195297491>

DUB-ICMS - Alíquota - Operações com Produtos de Importação RJ  
<https://tdn.totvs.com/pages/releaseview.action?pageId=561847819>
