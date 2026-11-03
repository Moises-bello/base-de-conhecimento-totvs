---
article_id: 360053485714
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: aa877e2980eca03d9191d68b946c55cebcee7143f18c9ec5e8621dd92b060ebd
fetched_at: '2026-06-28T22:42:10.860627+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - DUB-ICMS - Alíquota
  - Operações com Produtos de Importação RJ
type: support-article
updated_at: '2022-08-17T20:30:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053485714-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-DUB-ICMS-Al%C3%ADquota-Opera%C3%A7%C3%B5es-com-Produtos-de-Importa%C3%A7%C3%A3o-RJ
---

**Dúvida**DUB-ICMS - Alíquota - Operações com Produtos de Importação RJ

**Ambiente**Microsiga Protheus - Livros Fiscais - a partir da versão 11.80

**Solução**Em regra geral  os produtos importados cuja origem tenha sua definição 1, 2 ou 3 é aplicada a alíquota de 4%.

1 = Estrangeira - Importação direta, exceto a indicada no código 6

2 = Estrangeira - Adquirida no mercado interno, exceto a indicada no código 7

3 = Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% (quarenta por cento) e inferior ou igual a 70% (setenta por cento)

Para as situações  que fogem à regra geral, devem ser tratadas cada caso via exceção fiscal, através da rotina Exceções Fiscais (MATA540).

É importante frisar que para a operação ser eleita para entrar com valor no relatório **FISR001**, é necessário que o campo de "**Calcula ICMS**" (**F4\_ICM**) no cadastro de **TES** esteja como "**S -Sim**" e o "**L.Fisc.ICMS**" (**F4\_LFICM**) como "**I - Isento**" ou "**O - Outros**", dessa forma a operação estará correta, pois terá o **cálculo de ICMS** que servirá para o relatório e não irá gerar **débitos** ou **créditos** no **Livro Fiscal**.

Informações Adicionais:

Exceções Fiscais (MATA540)

<https://tdn.totvs.com/pages/releaseview.action?pageId=539703381>

DUB ICMS

<https://tdn.totvs.com/pages/releaseview.action?pageId=195297491>

<https://tdninterno.totvs.com/pages/releaseview.action?pageId=557344795>

<https://tdn.totvs.com/pages/releaseview.action?pageId=561847819>
