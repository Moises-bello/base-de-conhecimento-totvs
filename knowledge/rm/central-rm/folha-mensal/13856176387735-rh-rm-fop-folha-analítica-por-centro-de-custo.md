---
article_id: 13856176387735
category: Folha Mensal
content_hash: 4e2d0c22744b2f4fd5a72651d1e3501ee0dfba38a20d059a32f8817c2810edd2
fetched_at: '2026-06-28T22:46:58.237604+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Folha Analítica por centro de custo
type: support-article
updated_at: '2024-09-16T18:29:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13856176387735-RH-RM-FOP-Folha-Anal%C3%ADtica-por-centro-de-custo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura:**00:02:00 min****Duvida**Quais parametrizações devo verificar em meu sistema para gerar a folha analítica por centro de custo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
Na geração da Folha Analítica temos que verificar várias parametrizações ao realizar a geração do relatório quando é realizado por Centro de Custo, vou realizar uma listagem para facilita o entendimento, segue:  
  
**1**. Verifique se em **Configurações | Parametrizador | Folha Normal | Cálculo 2/2** temos a flag "**Utiliza Cálculo por Centro de Custo**" marcada. Caso não esteja, é necessário marcá-la.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13856255071639)

​

**2.** Verifique se no envelope do funcionário existe o botão Centro de Custo e ao clicar sobre o botão exibem as verbas rateadas ou se ficará em branco.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13856397024407)

​  
**3.** Caso fique em branco o envelope no passo acima, verifique no cadastro do funcionário em Anexos | Rateio Fixo se existe o Centro de Custo a ser rateado, caso não exista essa informação deve ser preenchida e recalcular o envelope para ser demonstrado como no passo **2**.  
  
**4.** Realizando essas validações, restará verificar no cadastro da seção do funcionário se existe o centro de custo informado na aba Dados Contábeis, segue:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13856456992535)

​  
**5.** Por fim, verifique as máscaras e quebras informadas se estão de acordo com as informações do Código do Centro de Custo desejado marcando a opção Usar Código de Quebra (Experimente também a opção Usar Filtro).  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13856462058903)

**Saiba mais**[RH - RM - FOP - Folha Analítica: cadastro e parametrização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416042752151-RH-RM-FOP-Folha-Anal%C3%ADtica-cadastro-e-parametriza%C3%A7%C3%A3o)[RH - RM - FOP - Centro de Custo: Parametrização inicial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015720892-RH-RM-FOP-Centro-de-Custo-Parametriza%C3%A7%C3%A3o-inicial)
