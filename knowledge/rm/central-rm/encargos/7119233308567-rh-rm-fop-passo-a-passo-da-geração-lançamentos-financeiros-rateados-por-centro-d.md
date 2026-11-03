---
article_id: 7119233308567
category: Encargos
content_hash: c21678971194709c05b680ea35e387ff2a915652db8bb5f9649a728e648b5011
fetched_at: '2026-06-28T22:46:52.515852+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Passo a passo da geração lançamentos financeiros rateados por
  Centro de Custo
type: support-article
updated_at: '2024-10-11T20:22:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7119233308567-RH-RM-FOP-Passo-a-passo-da-gera%C3%A7%C3%A3o-lan%C3%A7amentos-financeiros-rateados-por-Centro-de-Custo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como realizar a geração dos lançamentos financeiros rateados por centro de custo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**

1 - Acesse: **Configurações | Parametrizador | Folha normal | calculo 2/2** e certifique-se que a flag esta marcada conforme print abaixo.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11376858862743)

2 - Certifique-se que os eventos no envelope estão rateados com o mesmo centro de custo localizado dentro do cadastro do funcionário, conforme exemplo abaixo.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11376863015319)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11376864909975)

3 - Após acesse: **Encargos | Cadastros financeiros | Parâmetros** e localize o parâmetro que deseja gerar, no meu exemplo utilizei o parâmetro **liquido salarial.**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11376878509463)

4 - Verifique se a **Natureza Orçamentária Financeira** esta parametrizada conforme exemplo a seguir no mesmo parâmetro.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11376884850711)

5 - Após realizar as conferencias acima, acesse: **Encargos | Geração de lançamentos**

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11376879956119)

Atente-se a parametrização inicial, se existe algum filtro que possa impactar no processo de geração, e marque a flag **Gerar lanctos rateados por centro de custo,** Caso a mesma não esteja sendo apresentada, segue abaixo documentação para habilitar a mesma.

[RH - RM - FOP - Gerar lançamentos financeiros rateados por Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412577197847-RH-RM-FOP-Gerar-lan%C3%A7amentos-financeiros-rateados-por-Centro-de-Custo?source=search)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11376881293719)

No meu exemplo, eu gerei o lançamento financeiro somente para a chapa 00003, e veja o log de conclusão.

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11376918796055)

6 - Após acesse: **Encargos | lançamentos | Lançamento (gestão financeira ) ou Lançamento (folha de pagamento)**

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11376919640343)

Detalhamento do rateio.

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11376974967447)

**Saiba mais**  
[RH - RM - FOP - Parametrização dos Lançamentos Financeiros](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414130953111-RH-RM-FOP-Parametriza%C3%A7%C3%A3o-dos-Lan%C3%A7amentos-Financeiros)  
[RH - RM - FOP - Preenchimento de centro de custo na Capa do Lote Lançamento Financeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7136366292247-RH-RM-FOP-Preenchimento-de-centro-de-custo-na-Capa-do-Lote-Lan%C3%A7amento-Financeiro)
