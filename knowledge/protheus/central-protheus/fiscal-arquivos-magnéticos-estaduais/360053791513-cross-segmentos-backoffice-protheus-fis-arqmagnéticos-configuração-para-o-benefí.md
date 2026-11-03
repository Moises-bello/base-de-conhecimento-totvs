---
article_id: 360053791513
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: b88bae9c9ea6452129883c42633a7877c4762f42cdab94ea0a2b24b033b4b20d
fetched_at: '2026-06-28T22:42:10.415952+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Configuração
  para o benefício Outros ser considerado no relatório DUB ICMS (FISR001)
type: support-article
updated_at: '2022-08-17T20:07:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053791513-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Configura%C3%A7%C3%A3o-para-o-benef%C3%ADcio-Outros-ser-considerado-no-relat%C3%B3rio-DUB-ICMS-FISR001
---

**Dúvida**Qual a configuração para o benefício Outros ser considerado no relatório DUB ICMS ?

**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 11.80

**Solução**É importante frisar que para a operação ser eleita para entrar com valor no relatório FISR001, é necessário que o campo de **"Calcula ICMS" (F4\_ICM)** no cadastro de TES esteja como **"S -Sim"** e o **"L.Fisc.ICMS"** **(F4\_LFICM) como "I - Isento"** ou **"O - Outros"**, dessa forma a operação estará correta, pois terá o cálculo de ICMS que servirá para o relatório e não irá gerar débitos ou créditos no Livro Fiscal.

**Outros**

No caso de operações na quais a nota fiscal for escriturada com **Outras**, os valores são obtidos através dos campos F3\_ISENICM e F3\_OUTRICM. Para isso o campo **L. Fisc. ICMS** (F4\_LFICM) , no cadastro de TES deve ser preenchido com conteúdo igual a **I = Isento** ou**O= Outros**.

**Tipo DUB (F4\_TIPODUB)** - Indica o Tipo do Ato Legal utilizado no DUB-ICMS.

1=Convênio;  
2=Lei;  
3=Decreto;  
4=Protocolo;  
5=Resolução;  
6=Portaria.

**Benefic. DUB (F4\_BENDUB)** - Indica a Espécie do benefício utilizado no DUB-ICMS.  
6=Outros.

**Num./Ano DUB (F4\_NUMDUB)** - Indica o Número de identificação do Ato Legal e o Ano de Publicação utilizado no DUB-ICMS. Deve ser preenchido com o Número do Ato Legal / Ano do Ato Legal. Exemplo: 12345/2008.

Informações adicionais:

<https://tdn.totvs.com/pages/releaseview.action?pageId=195297491>

<https://tdninterno.totvs.com/pages/releaseview.action?pageId=557344795>

DUB-ICMS - Alíquota - Operações com Produtos de Importação RJ  
<https://tdn.totvs.com/pages/releaseview.action?pageId=561847819>
