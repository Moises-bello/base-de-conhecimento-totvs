---
article_id: 360053088574
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 5b2e2441ee98ff7ec8a2a04cd2af751403fb6f32c07b8f13d24a7ff129867143
fetched_at: '2026-06-28T22:42:10.420707+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Configuração
  para o benefício Redução de Base de Cálculo ser considerado no relatório DUB ICMS
  (FISR001)
type: support-article
updated_at: '2022-08-17T20:07:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053088574-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Configura%C3%A7%C3%A3o-para-o-benef%C3%ADcio-Redu%C3%A7%C3%A3o-de-Base-de-C%C3%A1lculo-ser-considerado-no-relat%C3%B3rio-DUB-ICMS-FISR001
---

**Dúvida**Qual a configuração para o benefício de Redução de Base de Cálculo ser considerado no relatório DUB ICMS ?

**Ambiente**

Microsiga Protheus - Livros Fiscais - A partir da versão 11.80

**Solução**É importante frisar que para a operação ser eleita para entrar com valor no relatório FISR001, é necessário que o campo de **"Calcula ICMS" (F4\_ICM)** no cadastro de TES esteja como **"S -Sim"** e o **"L.Fisc.ICMS"** **(F4\_LFICM) como "I - Isento"** ou **"O - Outros"**, dessa forma a operação estará correta, pois terá o cálculo de ICMS que servirá para o relatório e não irá gerar débitos ou créditos no Livro Fiscal.

**Redução de Base de Cálculo**

No caso de operações nas quais a nota fiscal sofre Redução de Base de Cálculo, o valor do ICMS que deixou de ser debitado/recolhido será considerado na impressão do relatório para esse tipo de benefício. Para isso o campo **% Red. Do ICMS** (F4\_BASEICM), no cadastro de TES, deve ser preenchido com o percentual de redução da base de cálculo.

**Tipo DUB (F4\_TIPODUB)** - Indica o Tipo do Ato Legal utilizado no DUB-ICMS.

1=Convênio;  
2=Lei;  
3=Decreto;  
4=Protocolo;  
5=Resolução;  
6=Portaria.

**Benefic. DUB (F4\_BENDUB)** - Indica a Espécie do benefício utilizado no DUB-ICMS.  
4=Red. Bs. Cálculo;

**Num./Ano DUB (F4\_NUMDUB)** - Indica o Número de identificação do Ato Legal e o Ano de Publicação utilizado no DUB-ICMS. Deve ser preenchido com o Número do Ato Legal / Ano do Ato Legal. Exemplo: 12345/2008.

Informações adicionais:

<https://tdn.totvs.com/pages/releaseview.action?pageId=195297491>

<https://tdninterno.totvs.com/pages/releaseview.action?pageId=557344795>

DUB-ICMS - Alíquota - Operações com Produtos de Importação RJ  
<https://tdn.totvs.com/pages/releaseview.action?pageId=561847819>
