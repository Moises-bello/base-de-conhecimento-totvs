---
article_id: 115013033127
category: RH - Rescisão
content_hash: bf3bf2945e7d5f254bece0a15fae72ed30997331ac8b236dfe5449a822047a4b
fetched_at: '2026-06-28T22:43:51.979415+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular PLR para funcionário desligado
type: support-article
updated_at: '2025-06-16T18:47:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115013033127-RH-Linha-Protheus-GPE-Como-calcular-PLR-para-funcion%C3%A1rio-desligado
---

**Dúvida**Como calcular **PLR** - Programa de Participação nos Lucros e Resultados para funcionário desligado?  
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões

**Solução**

Cálculo de PLR na rescisão complementar:

* **GPEA040**- Atualizações/Definições cálculo/Verbas

- Cadastrar uma verba com ID p/ Cálculo**0151** - Pagamento PLR - **Verba de Provento.**  
- Para este caso de**Rescisão Complementar** não deve ser preenchido o campo **Cod.Corresp.** com a verba de Desconto de PLR, pois se este campo estiver preenchido o sistema lançará uma verba de Provento e uma de Desconto.

![](http://tdn.totvs.com/download/attachments/301196059/image2017-10-3_17-25-35.png?version=1&modificationDate=1507064627000&api=v2)

As informações contidas nesta rotina serão armazenadas na tabela**SRV.**

Para efetuar o cálculo do PLR para os funcionários demitidos, deve ser efetuado o cálculo da rescisão complementar, e lançado o valor do PLR:

* **GPEM040:** Miscelânea/Cálculos/Rescisão:

![](http://tdn.totvs.com/download/attachments/301196059/image2017-10-3_17-47-5.png?version=1&modificationDate=1507064626000&api=v2)

Como não é Rescisão Complementar por Dissídio, selecionar a opção "Não":

![](http://tdn.totvs.com/download/attachments/301196059/image2017-10-3_17-47-34.png?version=1&modificationDate=1507064626000&api=v2)

Preencher os campos **Dt.Homologa**, e **Data Geração**:

![](http://tdn.totvs.com/download/attachments/301196059/image2017-10-3_17-50-40.png?version=1&modificationDate=1507064626000&api=v2)

Ir em Outras Ações/Lançamentos por Funcionários:

![](http://tdn.totvs.com/download/attachments/301196059/image2017-10-3_17-51-38.png?version=1&modificationDate=1507064625000&api=v2)

Lançar o Valor do PLR:

![](http://tdn.totvs.com/download/attachments/301196059/image2017-10-3_17-53-16.png?version=1&modificationDate=1507064625000&api=v2)

Calcular Rescisão:

![](http://tdn.totvs.com/download/attachments/301196059/image2017-10-3_17-54-34.png?version=1&modificationDate=1507064624000&api=v2)

Ao lançar a verba de PLR somente ela será calculada nessa complementar.

Impressão do Termo de Rescisão:

* **GPEM040:**Miscelânea/Cálculos/Rescisão, opção Impressão:

![](http://tdn.totvs.com/download/attachments/301196059/image2017-10-4_9-37-5.png?version=1&modificationDate=1507120626000&api=v2)

Preencher os parâmetros:

![](http://tdn.totvs.com/download/attachments/301196059/image2017-10-4_9-38-40.png?version=1&modificationDate=1507120721000&api=v2)

E confirmar a geração:

![](http://tdn.totvs.com/download/attachments/301196059/image2017-10-4_9-40-23.png?version=1&modificationDate=1507120824000&api=v2)  
  
**Saiba Mais**  
Foi criado o parâmetro **MV\_PLRDEM** para definir se o PLR deverá ser calculado para funcionários demitidos no período de cálculo mas que estavam ativos no período de referência do PLR.  
  
Se o parâmetro estiver com conteúdo "N" (Padrão), ao realizar o cálculo será verificado se a data de demissão do funcionário é igual ou inferior ao período de cálculo, em caso positivo, o cálculo não será feito e nenhuma outra ação é tomada. Neste caso, se for necessário o pagamento de PLR para um funcionário demitido, este deverá ser feito lançando a verba de PLR na rescisão complementar.  
  
Se o parâmetro estiver com "S", ao realizar o cálculo será verificado se a data de demissão do funcionário é inferior ao primeiro dia do ano de referência do PLR, em caso afirmativo o cálculo não é realizado, de outra forma o cálculo será efetuado normalmente como se o funcionário ainda estivesse ativo.  
  
Consulte o *link* a seguir para **verificar como criar e utilizar o parâmetro**:   
<https://tdn.totvs.com/pages/releaseview.action?pageId=431674489#id-2793857DRHPAG-17915DTPLR-C%C3%A1lculoparademitidos-parametros>
