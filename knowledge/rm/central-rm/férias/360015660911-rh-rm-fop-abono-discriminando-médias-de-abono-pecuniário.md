---
article_id: 360015660911
category: Férias
content_hash: ab7e071ee7cfbf9c9aba9b34716e413aa33d5e4353b135fb6b6edb757ef7f3cd
fetched_at: '2026-06-28T22:46:56.473587+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: 'RH - RM - FOP - Abono: Discriminando médias de abono pecuniário'
type: support-article
updated_at: '2025-09-02T17:29:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015660911-RH-RM-FOP-Abono-Discriminando-m%C3%A9dias-de-abono-pecuni%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:02:58 min  
  
Dúvida**Como parametrizar um evento específico para o pagamento de médias de abono pecuniário nas férias  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para parametrizar as médias discriminadas siga os passos abaixo:  
  
1. Acesse a aba **Administração de pessoal | Eventos** e cadastre novos eventos com os seguintes códigos de cálculo:  
  
*CC 47 - Média de abono de férias**CC 47 - Média de XXXX de abono de férias*\* O código XXXX utilizado acima representa eventos de horas-extras, comissões ou adicionais.  
\*\* Para o cálculo de médias de abono pecuniário, é necessário que todos os eventos criados possuam um código de cálculo vinculado, mesmo que para médias discriminadas.   
  
2. Acesse **Administração de Pessoal | Sindicatos** e depois acesse a aba **Férias**.Na aba inferior **Eventos p/ pagamento de Média de abono**, é necessário parametrizar os grupos de médias e informar os eventos para pagamento das médias específicas.  
  
Para que o pagamento das médias ocorra separadamente em um evento específico, informe um grupo de médias a partir do grupo 1. Isso é necessário, pois ao informar o grupo 0 as médias serão somadas ao evento de pagamento de férias com código de cálculo 38.  
  
![Sem_t_tulo2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360010614992/Sem_t_tulo2.png)  
  
3. Após parametrizar os grupos de médias nos **Eventos p/ pagamento de Média de abono**, é necessário informar a incidência de média no cadastro dos eventos pagos ao funcionário. Acesse **Administração de Pessoal | Eventos | Eventos** edite o evento que deseja informar a incidência das médias e vá em **Anexos | Eventos de Média**.  
  
\*Para que o evento seja contabilizado para médias de abono pecuniário, o evento deverá ter incidência em férias no mesmo grupo parametrizado para abono no sindicato.  
  
Cadastre a incidência em férias e o grupo de média utilizado, conforme explicado nos passos anteriores. Lembrando que este evento deverá estar lançado e com valores no período estabelecido nas parametrizações da média de férias para que as médias sejam corretamente lançadas. Desta forma, ao calcular as férias para o funcionário, o evento informado para pagamento de médias do grupo 1 será lançado no recibo de férias.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360010548632/mceclip1.png)  
  
**Saiba Mais**  
[Sindicatos](https://tdn.totvs.com/display/public/LRM/Sindicatos)   
[Eventos de Cálculo](https://tdn.totvs.com/pages/releaseview.action?pageId=452719284)
