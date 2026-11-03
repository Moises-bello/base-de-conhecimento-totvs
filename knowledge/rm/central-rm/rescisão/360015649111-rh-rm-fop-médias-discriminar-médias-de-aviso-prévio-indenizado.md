---
article_id: 360015649111
category: Rescisão
content_hash: 3cb04959f12c5e7a8fa50602816529472d66c50fd20540a8436abe1828aaf5f2
fetched_at: '2026-06-28T22:46:55.404717+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH- RM - FOP - Médias: Discriminar médias de aviso prévio indenizado'
type: support-article
updated_at: '2025-01-21T17:59:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015649111-RH-RM-FOP-M%C3%A9dias-Discriminar-m%C3%A9dias-de-aviso-pr%C3%A9vio-indenizado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:02:00 min****Dúvida**  
Como parametrizar um evento específico para o pagamento de médias sobre aviso prévio indenizado?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para parametrizar as médias discriminadas siga os passos abaixo:  
  
1. Acesse a aba **Administração de pessoal | Eventos** e cadastre novos eventos com os seguintes códigos de cálculo:  
  
*CC 62 - Aviso prévio (indenizado)**CC 99 - Diferença de Aviso Prévio**CC 99 - Diferença de Média de **XXXX** de Aviso Prévio*O código **XXXX** utilizado acima representa eventos de horas-extras, comissões ou adicionais.  
  
Para o cálculo de médias de aviso prévio, é necessário que todos os eventos criados possuam um código de cálculo vinculado, mesmo que para médias discriminadas.   
  
2. Acesse **Administração de Pessoal | Sindicatos** e depois acesse a aba **Aviso prévio**.Na aba inferior **Eventos p/ pagamento de Média de aviso prévio**, é necessário parametrizar os grupos de médias e informar os eventos para pagamento das médias específicos.  
  
Para que o pagamento das médias ocorra separadamente em um evento específico, informe um grupo de médias a partir do grupo 1. Isso é necessário, pois ao informar o grupo 0 as médias serão somadas ao evento de pagamento de férias com código de cálculo 38.  
  
![Sem_t_tulo.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360010620551/Sem_t_tulo.png)  
  
3. Após parametrizar os grupos de médias nos **Eventos p/ pagamento de Média de aviso prévio**, é necessário informar a incidência de média no cadastro dos eventos pagos ao funcionário. Acesse **Administração de Pessoal | Eventos | Eventos** edite o evento que deseja informar a incidência das médias e vá em **Anexos | Eventos de Média**.  
  
Cadastre a incidência em aviso prévio e o grupo de média utilizado, conforme explicado nos passos anteriores. Lembrando que este evento deverá estar lançado e com valores no período estabelecido nas parametrizações da média de aviso prévio para que as médias sejam corretamente lançadas. Desta forma, ao calcular a rescisão para o funcionário, o evento informado para pagamento de médias do grupo 1 será lançado no envelope rescisório.  
  
![Sem_t_tulo2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360010620831/Sem_t_tulo2.png)
