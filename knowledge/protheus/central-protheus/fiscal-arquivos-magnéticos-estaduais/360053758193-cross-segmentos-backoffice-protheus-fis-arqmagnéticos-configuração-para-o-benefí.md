---
article_id: 360053758193
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 71874ec11094cdac1930fd2aac025a304eb4704c8912198e985d6884f28b0e0d
fetched_at: '2026-06-28T22:42:10.398562+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Configuração
  para o benefício Diferimento ser considerado no relatório DUB ICMS (FISR001)
type: support-article
updated_at: '2022-08-17T20:07:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053758193-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Configura%C3%A7%C3%A3o-para-o-benef%C3%ADcio-Diferimento-ser-considerado-no-relat%C3%B3rio-DUB-ICMS-FISR001
---

**Dúvida**Qual a configuração para o benefício Diferimento ser considerado no relatório DUB ICMS?

**Ambiente**Microsiga Protheus - Livros Fiscais - a partir da versão 11.80

**Solução**É importante frisar que para a operação ser eleita para entrar com valor no relatório **FISR001**, é necessário que o campo de "**Calcula ICMS**" (**F4\_ICM**) no cadastro de **TES** esteja como "**S -Sim**" e o "**L.Fisc.ICMS**" (**F4\_LFICM**) como "**I - Isento**" ou "**O - Outros**", dessa forma a operação estará correta, pois terá o **cálculo de ICMS** que servirá para o relatório e não irá gerar **débitos** ou **créditos** no **Livro Fiscal**.

**Tipo DUB (F4\_TIPODUB)** - Indica o Tipo do Ato Legal utilizado no DUB-ICMS.

1=Convênio;

2=Lei;

3=Decreto;

4=Protocolo;

5=Resolução;

6=Portaria.

**Benefic. DUB (F4\_BENDUB)** - Indica a Espécie do benefício utilizado no DUB-ICMS.

1=Dif. Compra Ativ. Imobilizado;

2=Dif. Pag. Futuro;

**Num./Ano DUB (F4\_NUMDUB)** - Indica o Número de identificação do Ato Legal e o Ano de Publicação utilizado no DUB-ICMS. Deve ser preenchido com o Número do Ato Legal / Ano do Ato Legal. Exemplo: 12345/2008.

**Diferimento na Compra de Bens do Ativo Imobilizado**

Os valores são obtidos através do campo **ICM Diferido** (F3\_ICMSDIF), desde que os CFOPs para essa operação sejam informados corretamente no parâmetro MV\_CFOATIV.

**Diferimento para Pagamento Futuro**

Os valores são obtidos através do campo **ICM Diferido** (F3\_ICMSDIF), desde que os CFOPs para essa operação sejam informados corretamente no parâmetro MV\_CFOPFUT.

Com relação ao  benefício mencionado acima, para que o Diferimento do ICMS seja gerado, o campo **ICM Diferido** (F4\_ICMSDIF), no cadastro de TES, deve ser preenchido com conteúdo igual a **1 = Diferido**.

É imprescindível para impressão dos valores correspondentes aos benefícios, que os campos acima sejam preenchidos corretamente no Cadastro do Tipo de Entrada/Saída.

Informações adicionais:

<https://tdninterno.totvs.com/pages/releaseview.action?pageId=557344795>

<https://tdn.totvs.com/pages/releaseview.action?pageId=195297491>

DUB-ICMS - Alíquota - Operações com Produtos de Importação RJ  
<https://tdn.totvs.com/pages/releaseview.action?pageId=561847819>
