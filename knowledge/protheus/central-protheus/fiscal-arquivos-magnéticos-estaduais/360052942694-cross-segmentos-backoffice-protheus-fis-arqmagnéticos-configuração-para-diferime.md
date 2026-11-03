---
article_id: 360052942694
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: a61eb57306398f9d9e281f10bdcfc76fc7e386de1207aa6a4463241e2051fa4d
fetched_at: '2026-06-28T22:42:10.385789+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Configuração
  para Diferimento no relatório DUB ICMS (FISR001)
type: support-article
updated_at: '2022-08-17T20:05:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052942694-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Configura%C3%A7%C3%A3o-para-Diferimento-no-relat%C3%B3rio-DUB-ICMS-FISR001
---

**Dúvida**Qual a configuração para ICMS Diferido ser considerado no relatório DUB ICMS?  
  
**Ambiente**Microsiga Protheus - Livros Ficais - a partir da versão 11.80  
  
**Solução**Nessa situação é importante frisar que para a operação ser eleita para entrar com valor no relatório FISR001, é necessário que o campo de "Calcula ICMS" (F4\_ICM) no cadastro de TES esteja como "S -Sim" e o "L.Fisc.ICMS" (F4\_LFICM) como "I - Isento" ou "O - Outros", dessa forma a operação estará correta, pois terá o cálculo de ICMS que servirá para o relatório e não irá gerar débitos ou créditos no Livro Fiscal.

Tipo DUB (F4\_TIPODUB) - Indica o Tipo do Ato Legal utilizado no DUB-ICMS.

Benefic. DUB (F4\_BENDUB) - Indica a Espécie do benefício utilizado no DUB-ICMS.

1=Dif. Compra Ativ. Imobilizado;

2=Dif. Pag. Futuro;

Num./Ano DUB (F4\_NUMDUB) - Indica o Número de identificação do Ato Legal e o Ano de Publicação utilizado no DUB-ICMS. Deve ser preenchido com o Número do Ato Legal / Ano do Ato Legal. Exemplo: 12345/2008.

**Diferimento na Compra de Bens do Ativo Imobilizado**

Os valores são obtidos através do campo **ICM Diferido** (F3\_ICMSDIF), desde que os CFOPs para essa operação sejam informados corretamente no parâmetro MV\_CFOATIV.

**Diferimento para Pagamento Futuro**

Os valores são obtidos através do campo **ICM Diferido** (F3\_ICMSDIF), desde que os CFOPs para essa operação sejam informados corretamente no parâmetro MV\_CFOPFUT.

Informações adicionais:

<https://tdninterno.totvs.com/pages/releaseview.action?pageId=557344795>

<https://tdn.totvs.com/pages/releaseview.action?pageId=195297491>
