---
article_id: 360015971151
category: Rescisão
content_hash: 579b644ee83d5a820a79b2ac900fb454a1fda5b9d157de593646e21fe31cacbd
fetched_at: '2026-06-28T22:46:55.382403+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - Rescisão: Discriminar médias de 13º na rescisão'
type: support-article
updated_at: '2024-06-18T12:25:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015971151-RH-RM-FOP-Rescis%C3%A3o-Discriminar-m%C3%A9dias-de-13%C2%BA-na-rescis%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24255882679703)**Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**  
Como parametrizar um evento específico para o pagamento de médias de 13º na rescisão?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para parametrizar médias discriminadas do 13º na rescisão, siga os passos abaixo:  
  
1. Acesse: **Administração de Pessoal | Eventos | Eventos** e cadastre novos eventos com os seguintes códigos de cálculo:  
  
[Código de Cálculo 48](https://tdn.totvs.com/pages/viewpage.action?pageId=452718487) - Média de XXXX de 13º Salário rescisão  
[Código de Cálculo 97](https://tdn.totvs.com/pages/viewpage.action?pageId=452718387) - Diferença de Média de XXXX de 13º salário rescisão  
  
**Importante**  
O código XXXX utilizado acima representa eventos de horas-extras, comissões ou adicionais. Para o cálculo de médias de 13º na rescisão, é necessário que todos os eventos criados possuam um código de cálculo vinculado, mesmo que para médias discriminadas.   
  
2. Acesse: **Administração de Pessoal | Sindicatos** e depois acesse a aba **13º salário**. Na aba inferior **Eventos p/ pag. de Média de 13º na rescisão**, é necessário parametrizar os grupos de médias e informar os eventos para pagamento das médias específicas.  
  
Para que o pagamento das médias ocorra separadamente em um evento específico, informe um grupo de médias a partir do grupo 1. Isso é necessário, pois ao informar o grupo 0 as médias serão somadas ao evento de pagamento de 13º rescisão com código de cálculo 48.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10578067448855)  
  
3. Após parametrizar os grupos de médias nos **Eventos p/ pagamento de Média de 13º na rescisão**, é necessário informar a incidência de média no cadastro dos eventos pagos ao funcionário. Acesse **Administração de Pessoal | Eventos | Eventos** edite o evento que deseja informar a incidência das médias e vá em **Anexos | Eventos de Média**.  
  
Cadastre a incidência em 13º salário rescisão e o grupo de média utilizado, conforme explicado nos passos anteriores. Lembrando que este evento deverá estar lançado e com valores no período estabelecido nas parametrizações da média de férias para que as médias sejam corretamente lançadas. Desta forma, ao calcular a rescisão para o funcionário, o evento informado para pagamento de médias do grupo 4 será lançado no envelope rescisório.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10578121724311)
