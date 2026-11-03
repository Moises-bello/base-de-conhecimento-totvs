---
article_id: 360015735392
category: Rescisão
content_hash: 5e659c5ac3e244dca73bcfb1a004da9f938027e21c80b949d467a8b5bdff0570
fetched_at: '2026-06-28T22:46:55.391673+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH- RM - FOP - Médias: Discriminando médias de férias na rescisão'
type: support-article
updated_at: '2024-10-23T22:11:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015735392-RH-RM-FOP-M%C3%A9dias-Discriminando-m%C3%A9dias-de-f%C3%A9rias-na-rescis%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:03:23 min****Dúvida**Como parametrizar eventos específicos para o pagamento de médias de férias na rescisão?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para parametrizar as médias discriminadas siga os passos abaixo:  
  
**1.** Acesse a aba **Administração de pessoal | Eventos** e cadastre novos eventos com os seguintes códigos de cálculo:  
  
Código de Cálculo 0 - Média de XXXX de Férias  
Código de Cálculo 0 - Média de XXXX de Férias proporcionais  
  
\* O código XXXX utilizado acima representa eventos de horas-extras, comissões ou adicionais.  
\*Os eventos informados na aba **Eventos para pagamento de médias de férias** não poderão ser utilizados para o pagamento de médias na rescisão, sendo necessário a criação de novos eventos.  
  
**02.** Acesse **Administração de Pessoal | Sindicatos** e depois acesse a aba **Férias**.Nas abas inferiores **Eventos p/ pagamento de Média de Férias na rescisão** e **Eventos p/ pagamento de Média proporcional na rescisão** é necessário parametrizar os grupos de médias e informar os eventos para pagamento das médias específicas.  
  
\*A aba **Eventos p/ pagamento de Média proporcional** será exibida somente se a flag **Separa médias de férias vencidas e proporcionais na rescisão** estiver habilitada no **Parametrizador | Rescisão | Férias.**Para que o pagamento das médias ocorra separadamente em um evento específico, informe um grupo de médias a partir do grupo 1. Isso é necessário, pois ao informar o grupo 0 as médias serão somadas ao evento de pagamento de férias com código de cálculo 38.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9013796122007/mceclip0.png)  
  
**3.** Após parametrizar os grupos de médias nos **Eventos p/ pagamento de Média de Férias na rescisão** e**Eventos p/ pagamento de Média proporcional na rescisão**, é necessário informar a incidência de média no cadastro dos eventos pagos ao funcionário. Acesse **Administração de Pessoal | Eventos | Eventos** edite o evento que deseja informar a incidência das médias e vá em **Anexos | Eventos de Média**.  
Cadastre a incidência em **férias rescisão** e o grupo de média utilizado, conforme explicado nos passos anteriores. Lembrando que este evento deverá estar lançado e com valores no período estabelecido nas parametrizações da média de férias na rescisão para que as médias sejam corretamente lançadas. Desta forma, ao calcular a rescisão para o funcionário, o evento informado para pagamento de médias do grupo 1 será lançado no envelope rescisório.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9013853460375/mceclip2.png)

**Saiba mais:**  
[Férias - Rescisão](https://tdn.totvs.com/pages/releaseview.action?pageId=452719504)  
[Sindicatos](https://tdn.totvs.com/display/public/LRM/Sindicatos)  
[Aba Media Férias Rescisão](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719374)
