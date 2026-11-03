---
article_id: 360009804692
category: RH - Rescisão
content_hash: c9ad469c47cd61d564c85d957f2f875b6588722b90344149f729f046bb205f97
fetched_at: '2026-06-28T22:43:48.360937+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE -  Como fazer a contagem dos avos de férias vencidas
  e proporcionais na rescisão
type: support-article
updated_at: '2025-07-22T11:32:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360009804692-RH-Linha-Protheus-GPE-Como-fazer-a-contagem-dos-avos-de-f%C3%A9rias-vencidas-e-proporcionais-na-rescis%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26670456541719)***Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como fazer a contagem dos avos de férias vencidas e proporcionais na rescisão  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

**1. Conferência:**

Para contagem dos avos de férias, que é demonstrado na referência das verbas de férias, deve ser feito da seguinte forma: Total de dias demonstrado no cabeçalho / 2,5 – dias por avos.

Caso esse valor seja quebrado, o avo demonstrado é arredondado para um número maior ou menor de acordo com a casa após a virgula.

Para efeito de conferência dos valores de férias, não é correto pegar o salário / 12 \* avos, pois se houver faltas, os valores não serão apresentados de acordo.

O correto é utilizar a seguinte fórmula: base de cálculo das férias, que pode ou não ter verbas incorporadas / 30 \* dias de férias vencidas ou dias de férias proporcionais que constam no cabeçalho da rescisão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360008260572)

Calculo dos avos: **Férias vencidas** 30 dias / 2,5 avos = 12 avos – **Férias proporcionais** 12,5 / 2,5 avos= 5 avos

Calculo dos valores: **Férias vencidas** 12.258,00 / 30 dias mês \* 30 dias de férias= 12.258,00 – **Férias proporcionais** 12.258,00 / 30 dias mês \* 12,5 dias de férias= 5.107,50

**2. Avos de férias sobre o aviso:**Os campos Dias Férias Sobre Aviso Prévio Indenizado (RG\_DFERAVI) e Tipo Aviso (RG\_TPAVISO), tem a finalidade de facilitar a conferência do cálculo das férias na rescisão.

O identificador de cálculo de Férias sobre Aviso Prévio Indenizado é o id 0230.

Quando calculada uma rescisão com **aviso prévio indenizado**, os dias de férias que o funcionário passa a ter direito, devido à projeção dos dias de aviso prévio indenizado na data de demissão, serão gravados separadamente no campo Dias Fer Aviso (RG\_DFERAVI) e, não mais, com as férias proporcionais ou vencidas, campos Dias Fer Prop (RG\_DFERPRO) e Dias Fer Ven (RG\_DFERVEN).

**2.1 Informações que você precisa saber:**Saber qual o período aquisitivo do funcionário - Controle de dias de direito.

1. Saber quantos dias de aviso será projetado - cabeçalho da rescisão.
2. Sabendo o período aquisitivo do funcionário e quantos dias será projetado, você saberá quantos avos o funcionário terá direito por ter trabalhado e quantos avos o funcionário terá direito devido a projeção do aviso.

**2.2 Exemplo:** **![](https://centraldeatendimento.totvs.com/hc/article_attachments/360008303091)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360008303571)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360008303651)**

**3. Faltas dentro do período de férias:**As faltas informadas no momento da rescisão ou existente em outros meses, sempre serão consideradas para o cálculo dos dias de férias proporcionais e, caso o funcionário não tenha direito ao período aquisitivo proporcional, será considerado no período de férias vencidas, e nunca do período indenizado, obtido pela projeção do aviso.

**Importante lembrar que**, para reduzir os dias de férias em decorrência a quantidade de faltas, o sistema verifica a existência de verbas vinculadas ao identificador 0054 dentro da tabela SRD – acumulados, dentro do período de férias proporcional do funcionário.

Para apurar a quantidade faltas, é possível imprimir no item relatórios, o relatório de acumulado, selecionando nos parâmetros a verba de falta vinculada ao identificador 0054 e data inicio e fim do período de férias vencidas ou proporcionais. Veja se a quantidade de faltas demonstrada nesse filtro e veja se o funcionário deve perder algum avo de férias através da tabela: <http://www.ebs.com.br/treinamento/cursos/Ferias/co/ferias_normais_exemplo2.html>

Dentro das rotinas de programação de férias (V11) e controle de dias de direito (V12) existe campos para demonstrar a quantidade de faltas dentro do período aquisitivo do funcionário, que são **apenas para demonstração**, visto que o sistema realiza a verificação e efetiva o desconto através dos registros no acumulado (folhas já calculas- tabela SRD).

**Os campos são**: Faltas Férias Vencidas (RF\_DFALVAT) e Faltas Férias Proporcionais (RF\_DFALAAT).

No caso de migração para o sistema, caso hajam faltas, elas devem ser importadas para o acumulado (tabela SRD).  
  
**4. Afastamento no período aquisitivo de férias:**  
Necessário verificar em definições de ausências se o afastamento abate os avos de férias através dos campos:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000628981)

**Observação:**Os avos demonstrados no cabeçalho da rescisão, já estão corrigidos levando em conta as faltas existentes no período aquisitivo do funcionário, não sendo necessário realizar nenhuma outra conta para chegar à quantidade.  
  
**Saiba Mais**[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
