---
article_id: 360015758812
category: Rescisão
content_hash: 3e47e4988af823a57e0a3d08b23e7139ff397c9682520c10d2cb256687e744a7
fetched_at: '2026-06-28T22:46:55.387061+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - 2ª Parcela do 13º Salário: discriminação de médias'
type: support-article
updated_at: '2025-01-22T19:07:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015758812-RH-RM-FOP-2%C2%AA-Parcela-do-13%C2%BA-Sal%C3%A1rio-discrimina%C3%A7%C3%A3o-de-m%C3%A9dias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29426376096407)Tempo aproximado para leitura: **00:01:20 min  
  
Dúvida**  
Como parametrizar um evento específico para o pagamento de médias de 13º?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para parametrizar as médias discriminadas na 2º parcela do 13º siga os passos abaixo:  
  
1. Acesse: **Administração de pessoal | Eventos** e cadastre novos eventos com os seguintes códigos de cálculo:  
  
**Código de Cálculo 102** - Média de XXXX de 2ª Parcela de 13º salário  
**Código de Cálculo 66** - Diferença de Média de XXXX de 2ª parcela de 13º  
  
O código XXXX utilizado acima representa eventos de horas-extras, comissões ou adicionais.  
  
2. Acesse: **Administração de Pessoal | Sindicatos** e depois acesse a aba **13º salário**.Na aba inferior **Eventos p/ pag. de Média de 13º na 2º parcela**, é necessário parametrizar os grupos de médias e informar os eventos para pagamento das médias específicas.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29426376100503)  
  
Para que o pagamento das médias ocorra separadamente em um evento específico, informe um grupo de médias a partir do grupo 1. Isso é necessário, pois ao informar o grupo 0 as médias serão somadas ao evento de pagamento de 2ª parcela de 13º com [Código de Cálculo 102.](https://tdn.totvs.com/pages/releaseview.action?pageId=452719068)  
  
![Sem_t_tulo.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360011105991)  
  
3. Após parametrizar os grupos de médias nos **Eventos p/ pagamento de Média de Férias**, é necessário informar a incidência de média no cadastro dos eventos pagos ao funcionário. Acesse **Administração de Pessoal | Eventos | Eventos** edite o evento que deseja informar a incidência das médias e vá em **Anexos | Eventos de Média**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29426389538199)  
  
Cadastre a incidência em 13º salário e o grupo de média utilizado, conforme explicado nos passos anteriores. Lembrando que este evento deverá estar lançado e com valores no período estabelecido nas parametrizações da média de 13º salário para que as médias sejam corretamente lançadas. Desta forma, ao calcular a segunda parcela do 13º para o funcionário, o evento informado para pagamento de médias do grupo 1 será lançado no envelope de pagamento.  
  
![Sem_t_tulo.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360011075492)  
  
**Importante**  
A discriminação de médias na 1º parcela pode ser realizada apenas através de fórmulas. Para maiores informações, [CLIQUE AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014800711-RM-FOP-13%C2%BA-Sal%C3%A1rio-Discrimina%C3%A7%C3%A3o-de-m%C3%A9dia-no-pagamento-da-1%C2%AA-parcela) acessar o informativo.  
  
**Saiba Mais**[RH - RM - FOP - 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020075531-RM-FOP-13%C2%BA-Sal%C3%A1rio)
