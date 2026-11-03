---
article_id: 4412598605719
category: Rescisão
content_hash: 3065979288b02052f311e3d16cff1f0669e25b40c9265312fd77de7206d0d0df
fetched_at: '2026-06-28T22:46:54.463655+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: RH - RM - FOP - Rescisão complementar referente a  alteração salarial dentro
  do mês
type: support-article
updated_at: '2024-10-18T15:18:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412598605719-RH-RM-FOP-Rescis%C3%A3o-complementar-referente-a-altera%C3%A7%C3%A3o-salarial-dentro-do-m%C3%AAs
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27166115037591) Tempo aproximado para leitura: **00:06:00 min****Dúvida**Como realizar rescisão complementar de funcionário demitido, onde a alteração salarial refere-se a data base da competência atual?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Quando um funcionário não recebe a totalidade dos seus direitos na demissão seja por falta de dados, por alteração salarial, por convenção coletiva ou por outro motivo, o pagamento de valores complementares será devido. Neste caso, como devo cadastrar a **Rescisão Complementar**  
Para solucionar essa dúvida, realize os seguintes passos:  
  
1.Acesse: Administração de pessoal | Alteração global de salários. A alteração salarial é referente à competência atual, **data base 01/10/2021  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27166115041431)**Informe o percentual de aumento a ser calculado  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27166115043991)  
  
Verifique o histórico salarial e confirme a alteração  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412610072087)  
  
2. Cadastre a rescisão complementar, salve e avance  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27166084640535)  
  
Conferir os lançamentos no envelope da rescisão original   
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412610462871)  
  
Rescisão Complementar da chapa 00052, demitido em 01/10/2021, onde recebeu aumento por dissidio não em Outubro/2021, com percentual de 10%. Valores lançados no envelope  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412597526295)  
  
Na competência da rescisão original do colaborador, que no caso é a atual, são lançadas as verbas de diferença na aba **verbas geradas por diferença  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412618476055)**Ainda na competência atual, serão discriminados | lançados, os eventos de diferença que foram pagos, referentes a alteração salarial, com base na competência atual 10/2021  
  
**![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412610888471)****Importante**Quando há alteração salarial, para rotinas de diferença salarial | férias e rescisão complementar, ocorre dentro do mês, o desconto de INSS será efetuado no código de cálculo 3. É um comportamento padrão do sistema, por se tratar de um ajuste do INSS no mês. Só será lançado no evento de diferença de INSS separado, quando for rescisão complementar por dissídio sim, ou seja alteração salarial referente a data base de competências anteriores.

Após o cálculo da rescisão complementar não será possível realizar alterações no envelope como, por exemplo, editar, inserir ou excluir eventos e recalcular o envelope.

* **Período da rescisão:** Refere-se ao período (mês) em que o funcionário foi demitido. Informe o primeiro e o último dia do mês da competência em que o funcionário foi demitido;
* **Data do último movimento:** Refere-se a data em que o pagamento da Rescisão Complementar será efetivado. Informe uma data no mês caixa atual;
* **Dissídio (Sim ou Não):**Este campo indicará se o pagamento da Rescisão Complementar é devido ao pagamento de dissídio pela empresa. Quando o dissídio for sim, deverá cadastrar os dados do dissídio;
* **Informa total de minutos para eventos do Tipo H**: Visualizar o total de minutos quando os eventos forem do tipo Hora;
* **Calcula somente eventos informados:** Irá calcular somente os eventos informados no campo **“Eventos a serem somados a todas as rescisões complementares”**, mesmo se o funcionário possuir outras verbas para pagamento, como a diferença salarial por exemplo;
* **Eventos a serem somados a todas as rescisões complementares:**Informe neste campo os eventos que desejar informar manualmente para pagamento em todas as rescisões complementares que você for calcular. Verifique se o parâmetro **“Calcula somente eventos informados”** está marcado, pois caso esteja os únicos eventos que serão calculados na Rescisão Complementar são os que serão informados neste campo;
* **Aumentos a não considerar:** Caso o funcionário tenha recebido mais de um aumento salarial e somente um destes aumentos for devido para a Rescisão Complementar, você poderá marcar os tipos de aumento que o funcionário recebeu, mas que **NÃO** deverão ser considerados para o cálculo da Rescisão Complementar;
* **Comportamento dos eventos de diferença:** Neste campo é possível determinar o que fazer caso um evento de diferença já esteja lançado no envelope do funcionário. Caso marque **“adicionar valor”** o sistema irá somar o valor lançado na Rescisão Complementar ao valor lançado no envelope do pagamento do funcionário. Caso marque **“substituir valor”** o sistema irá substituir o valor do envelope do funcionário pelo valor calculado na Rescisão Complementar;
* **Quebra de seção:** Informe a quebra pela qual deseja que as Rescisões Complementares sejam calculadas ou o código da seção que os funcionários estejam alocados;
* **Seleção de funcionários:** Informe a chapa, o filtro de funcionários, a fórmula de seleção ou o conjunto de parametrizações para selecionar o funcionário ou funcionários que deseja lançar a Rescisão Complementar.
* **Calcular todas as diferenças juntas:**Marque essa opção queira que todas as diferenças do funcionário sejam calculadas juntamente com a rescisão ao mesmo tempo, diferença de folha, férias e 13 salario

**Saiba Mais**[Rescisão](https://tdn.totvs.com/pages/releaseview.action?pageId=452718921) [Complementar](https://tdn.totvs.com/pages/releaseview.action?pageId=452718921)  
[RH - RM - FOP - Rescisão Complementar por Dissídio: Códigos de Cálculo 410, 411, 412 e 413](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027380711--RH-RM-FOP-Rescis%C3%A3o-Complementar-por-Diss%C3%ADdio-C%C3%B3digos-de-C%C3%A1lculo-410-411-412-e-413?source=search)
