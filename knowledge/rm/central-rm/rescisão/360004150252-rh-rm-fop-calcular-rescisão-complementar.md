---
article_id: 360004150252
category: Rescisão
content_hash: d4adea169bef4490cce2bfb7c01929fd7540997f73cc155d019bea1882a6bc14
fetched_at: '2026-06-28T22:46:55.437408+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: RH - RM - FOP - Calcular Rescisão Complementar
type: support-article
updated_at: '2024-09-13T18:35:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004150252-RH-RM-FOP-Calcular-Rescis%C3%A3o-Complementar
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22850600763671)**Tempo aproximado para leitura: **00:04:35 min  
  
Dúvida**Quando um funcionário não recebe a totalidade dos seus direitos na demissão seja por falta de dados, por alteração salarial, por convenção coletiva ou por outro motivo, o pagamento de valores complementares será devido. Neste caso, como devo cadastrar e calcular a Rescisão Complementar?**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para solucionar essa dúvida, acesse: menu **Rescisão | Complementar** para acessar a rotina. Na rotina de Rescisão Complementar você encontrará diversos campos parametrizáveis, conforme imagem abaixo. Verifique a descrição de cada campo e faça sua parametrização conforme necessário.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12627397833751)

* **Período da rescisão:** Refere-se ao período (mês) em que o funcionário foi demitido. Informe o primeiro e o último dia do mês da competência em que o funcionário foi demitido.
* **Data do último movimento:** Refere-se a data em que o pagamento da Rescisão Complementar será efetivado. Informe uma data no mês caixa atual.
* **Dissídio Sim ou Dissídio Não:** Este campo indicará se o pagamento da Rescisão Complementar é devido ao pagamento de dissídio pela empresa. Quando o dissídio for sim, deverá cadastrar os dados do dissídio.
* **Informa total de minutos para eventos do Tipo H**: Visualizar o total de minutos quando os eventos forem do tipo Hora.
* **Calcula somente eventos informados:** Irá calcular somente os eventos informados no campo **Eventos a serem somados a todas as rescisões complementares**, mesmo se o funcionário possuir outras verbas para pagamento, como a diferença salarial, por exemplo.
* **Eventos a serem somados a todas as rescisões complementares:** Informe neste campo os eventos que desejar informar manualmente para pagamento em todas as rescisões complementares que você for calcular. Verifique se o parâmetro **Calcula somente eventos informados** está marcado, pois caso esteja os únicos eventos que serão calculados na Rescisão Complementar são os que serão informados neste campo.
* **Aumentos a não considerar:** Caso o funcionário tenha recebido mais de um aumento salarial e somente um destes aumentos for devido para a Rescisão Complementar, você poderá marcar os tipos de aumento que o funcionário recebeu, mas que não deverão ser considerados para o cálculo da Rescisão Complementar.
* **Comportamento dos eventos de diferença:** Neste campo é possível determinar o que fazer caso um evento de diferença já esteja lançado no envelope do funcionário. Caso marque **adicionar valor** o sistema irá somar o valor lançado na Rescisão Complementar ao valor lançado no envelope do pagamento do funcionário. Caso marque **substituir valor** o sistema irá substituir o valor do envelope do funcionário pelo valor calculado na Rescisão Complementar.
* **Quebra de seção:** Informe a quebra pela qual deseja que as Rescisões Complementares sejam calculadas ou o código da seção que os funcionários estejam alocados.
* **Seleção de funcionários:** Informe a chapa, o filtro de funcionários, a fórmula de seleção ou o conjunto de parametrizações para selecionar o funcionário ou funcionários que deseja lançar a Rescisão Complementar.
* **Calcular todas as diferenças juntas:** Marque essa opção queira que todas as diferenças do funcionário sejam calculadas juntamente com a rescisão ao mesmo tempo, diferença de folha, férias e 13º salário.

**Importante**Após o cálculo da rescisão complementar não será possível realizar alterações no envelope como, por exemplo, editar, inserir ou excluir eventos e recalcular o envelope.  
  
**Saiba Mais**  
[Rescisão Complementar](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452718921)
