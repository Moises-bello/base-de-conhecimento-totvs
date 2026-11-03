---
article_id: 4958578773655
category: Materiais - Compras (SIGACOM)
content_hash: 61c9acd3f5b9893d08f2943611290f9795be651e692a692ba5ce4449d1d3ae88
fetched_at: '2026-06-28T22:41:16.151782+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Protheus - SIGACOM - Configuração padrão
  dos impostos no Importador XML/ Totvs Colaboração  para o documento de entrada.
type: support-article
updated_at: '2024-06-11T12:52:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4958578773655-Cross-Segmentos-TOTVS-Backoffice-Protheus-SIGACOM-Configura%C3%A7%C3%A3o-padr%C3%A3o-dos-impostos-no-Importador-XML-Totvs-Colabora%C3%A7%C3%A3o-para-o-documento-de-entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24100343232791) Tempo aproximado para leitura: **5 min** **Dúvida**Configuração padrão dos impostos no Importador XML/ Totvs Colaboração para o documento de entrada.

**Ambiente**Protheus – Compras – A partir da versão 12

**Solução**

Quando o XML a ser importado na rotina "Importador XML/TOTVS Colaboração" possuir cálculo de impostos (Exemplo ICMS ST), será apresentado na aba "Impostos" da rotina Monitor (COMXCOL).

Lembrando que os valores apresentados na aba refere-se ao item da linha selecionada, Exemplo:

Linhas 001:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4960032199703)

Nesse exemplo, na linha 001 não possui ICMS ST e não apresenta o cálculo na aba imposta. Os impostos vão apresentar com base da linha selecionada.

Linha 002:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4960170905239)

Nesse outro Exemplo, veja que na linha 002 o cálculo do imposto ICMS ST e apresenta da aba impostos, isso porque a linha selecionada possui ICMS ST.

Caso a TES seja informada no monitor (COMXCOL), o sistema irá calcular os impostos conforme as configurações definidas:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4958203182359)

Esse mesmo cálculo será levado para o documento de entrada:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4958252563991)

Quando não informar o TES no monitor (COMXCOL), o sistema não executará o cálculo de impostos:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4958495927319)

**Importante:** O sistema não preenche os impostos com base no XML na rotina do documento de entrada (MATA103), ele apenas vai gerar o calculo caso tenha TES informada.

**Link para auxílio:**

* [CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Configuração padrão do ICMS-ST](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027787051-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Configura%C3%A7%C3%A3o-padr%C3%A3o-do-ICMS-ST)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML)
* [Importador XML - Guia de Referencia (SIGACOM)](https://tdn.totvs.com/pages/releaseview.action?pageId=485858148)
* [Pontos de Entrada disponíveis nas funções](http://tdn.totvs.com/display/public/PROT/IX02+-+Pontos+de+Entrada)
* [Parâmetros Envolvidos](http://tdn.totvs.com/pages/releaseview.action?pageId=485869217)
* [Tabelas e rotinas](http://tdn.totvs.com/pages/releaseview.action?pageId=485869224)
* [Códigos de Erros](http://tdn.totvs.com/pages/releaseview.action?pageId=485869227)
* [Diferenças TOTVS Colaboração e Importador XML](http://tdn.totvs.com/pages/releaseview.action?pageId=501478281)
* [Importador XML ou Totvs Colaboração: Como executar as funções de carga SEM utilizar o schedule](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040549593-MP-SIGACOM-Importador-XML-ou-Totvs-Colabora%C3%A7%C3%A3o-Como-executar-as-fun%C3%A7%C3%B5es-de-carga-SEM-utilizar-o-schedule)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
