---
article_id: 4403157819287
category: RH - Cálculo PLR
content_hash: f5d7eafa3c6a154b100bf4c5d87aa05d0cc5c05485bc559402b4d5104ea60e12
fetched_at: '2026-06-28T22:43:12.856439+00:00'
product: protheus
section_id: 360010855894
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular PLR no roteiro PLR para funcionários
  demitidos
type: support-article
updated_at: '2025-04-07T18:50:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403157819287-RH-Linha-Protheus-GPE-Como-calcular-PLR-no-roteiro-PLR-para-funcion%C3%A1rios-demitidos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24999619381271) Tempo aproximado para leitura: **00:03:00 min**  
**Dúvida**Como calcular PLR no roteiro PLR para funcionários demitidos?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**Criação do parâmetro [MV\_PLRDEM](https://tdn.totvs.com/pages/viewpage.action?pageId=431674489#id-2793857DRHPAG-17915DTPLR-C%C3%A1lculoparademitidos-parametros) para definir se o PLR deverá ser calculado para funcionários demitidos no período de cálculo mas que estavam ativos no período de referência do PLR.

Se o parâmetro estiver com conteúdo "N" (Padrão), ao realizar o cálculo será verificado se a data de demissão do funcionário é igual ou inferior ao período de cálculo, em caso positivo, o cálculo não será feito e nenhuma outra ação é tomada. Neste caso, se for necessário o pagamento de PLR para um funcionário demitido, este deverá ser feito lançando a verba de PLR na rescisão complementar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24999642165271)

Se o parâmetro estiver com "S", ao realizar o cálculo será verificado se a data de demissão do funcionário é inferior ao primeiro dia do ano de referência do PLR, em caso afirmativo o cálculo não é realizado, de outra forma o cálculo será efetuado normalmente como se o funcionário ainda estivesse ativo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24999619390359)

Após o cálculo, o pagamento poderá ser efetuado através de um título de PLR, como para os funcionários ativos, ou ainda através da rescisão complementar, para isto basta calcular uma rescisão complementar no mesmo período de cálculo do PLR que as verbas geradas para o roteiro de PLR serão automaticamente carregas no cálculo da rescisão.

A rotina de fechamento também foi tratada para que, quando o parâmetro estiver ativo, não filtre apenas funcionários ativos para exclusão dos dados da SRC e gravação na SRD. Neste caso os registros de funcionários demitidos também serão atualizados, evitando que o cálculo da PLR não seja movido para o histórico.  
  
**IMPORTANTE:**

Caso seja necessário criar o parâmetro segue abaixo a configuração para inclusão:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403157799191)  
  
  
**Saiba mais:**  
<https://tdn.totvs.com/pages/viewpage.action?pageId=431674489>

[RH - Cálculo PLR](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010855894-RH-C%C3%A1lculo-PLR)
