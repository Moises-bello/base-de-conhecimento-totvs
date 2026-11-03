---
article_id: 4406938574487
category: Administração de Pessoal
content_hash: 98ccd62934ae77f3d3237c4437b66f377da05d5b2c7cfa824734a095ee757dc4
fetched_at: '2026-06-28T22:47:02.128028+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: RH - RM - FOP - Cadastro e Cálculo do Vale Transporte
type: support-article
updated_at: '2025-03-13T11:13:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406938574487-RH-RM-FOP-Cadastro-e-C%C3%A1lculo-do-Vale-Transporte
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:30 min****Dúvida**Como cadastro e confiro o cálculo de Vale Transporte?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**A solução para esta dúvida elenca um determinado processo e alguns cadastros já documentados em outros artigos. Siga os passos abaixo acessando tais artigos quando solicitado:  
  
1. Em primeiro lugar, é necessário configurar o sindicato em **Administração de Pessoal | Sindicatos.**  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406932495767/mceclip0.png)  
  
Nestes campos, temos:

* **% de desconto**: Informar o percentual de desconto de vale-transporte definido para os funcionários ligados a este sindicato.
* **Desconto único**: Habilitar caso queira que seja feito o cálculo de desconto de vale-transporte considerando o valor encontrado nos lançamentos do acumulado mensal, ou seja, o somatório de todos os períodos. Não o habilitando, o sistema fará o cálculo para desconto de vale-transporte considerando o valor encontrado nos lançamentos apenas do período.
* **Usa 30 dias p/ desconto**: Habilitar caso queira que o percentual de desconto do vale-transporte seja aplicado sobre o salário do funcionário. Se o campo não estiver marcado, será aplicado o percentual de desconto sobre o número de dias úteis constantes no cadastro do funcionário.

2. Em seguida, é necessário que haja Tarifa de Transporte cadastrada. Para este cadastro, basta conferir esta documentação: [RH - RM - FOP - Vale Transporte: Tarifas de Transporte](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022273692-RH-RM-FOP-Vale-Transporte-Tarifas-de-Transporte)

3. De mesmo modo, deve-se cadastrar a Linha de Transporte. Como o cadastro da Linha depende da Tarifa, reforçamos a necessidade de fazer o passo 2 antes do 3. Também está a disposição a documentação para este cadastro no link: [RH - RM - FOP - Vale Transporte: Linhas de Transporte](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022456451-RH-RM-FOP-Vale-Transporte-Linhas-de-Transporte)  
  
4. No cadastro do funcionário, na seção **Informações para o Cálculo |** pasta **Parâmetros**, faça o cadastro do Histórico de Vale Transporte do funcionário:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406933161111/mceclip1.png)  
  
Nele, será necessário incluir a data de validade, a linha e o número de viagens. O campo Valor da Tarifa é auto preenchido ao salvar este cadastro, uma vez que o cadastro da Linha já conta com o valor da Tarifa vinculada.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406933248663/mceclip2.png)  
  
5. Para que os eventos de vale transporte sejam lançados no envelope, basta marcar o flag **Lançar Vale Transporte** no grupo de eventos utilizados para lançar sua Folha.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406929703575/mceclip3.png)  
  
O flag automatiza o lançamento dos eventos de código de cálculo 6, 32 e 104, conforme demonstrados respectivamente neste envelope de exemplo.  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406929849367/mceclip4.png)  
  
**Importante**  
Em **Configurações | Parametrizador | Folha Normal | Vale transporte**, haverá o parâmetro **Utiliza Salário Nominal**. Com este parâmetro marcado, o valor da incidência do vale transporte na aba **Incidências** do envelope mostrará o valor do salário base do funcionário. Caso contrário, o valor da incidência será a soma dos eventos que incidem em Vale Transporte no período.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4420465895575/mceclip0.png)  
  
**Saiba mais**Para o uso da rotina Gerar Compra de Vale Transporte, consulte: [RH - RM - FOP - Utiliza Histórico de compra de Vale Transporte.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001636782-RM-FOP-Utiliza-Hist%C3%B3rico-de-compra-de-Vale-Transporte)  
  
Para a rotina Alteração Global de Dias Úteis de Vale Transporte, que ajusta os dias úteis do mês no cadastro dos funcionários, consulte: [RM - FOP - Vale Transporte: Alteração de dias úteis.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020440091-RM-FOP-Vale-Transporte-Altera%C3%A7%C3%A3o-de-dias-%C3%BAteis)
