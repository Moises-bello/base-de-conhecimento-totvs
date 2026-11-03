---
article_id: 360028777051
category: Manutenção de Ativos (SIGAMNT)
content_hash: 146c520ed35a65eff9827d29e54409a1d890b0f6c3f6734e50bdc9ae4e010ebe
fetched_at: '2026-06-28T22:42:34.482643+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Substituição de O.S
type: support-article
updated_at: '2025-02-21T20:47:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028777051-Manufatura-Linha-Protheus-MNT-Substitui%C3%A7%C3%A3o-de-O-S
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30154818926359)*Tempo aproximado para leitura: **00:04:00 min****Dúvida**Como utilizar o processo de Substituição de **O.S - Ordem de Serviço**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**A **Substituição** **de O.S.** ocorre em manutenções similares, ou seja, manutenções para o mesmo bem, serviço e com a mesma característica de tipo de acompanhamento, que compartilham das tarefas, insumos e etapas. Normalmente utilizado em manutenções preventivas de fábrica.  
  
Exemplo: As manutenções de sequência 1 2 e 3 possuem tarefas, insumos e etapas. Podemos concluir que nas manutenções similares, todas as tarefas, etapas e insumos da sequência 1 estão contidas na sequência 2 bem como as de sequência 2 na de sequência 3.  
  
Os objetivos de utilizar esse conceito são:

* Reduzir o volume de **O.S.**;
* Reduzir custos com insumos;
* Maximizar a utilização do bem e produtividade;
* Evitar a duplicidade de tarefas.

Para utilizar esta funcionalidade é necessário informar na**Manutenção - STF** o campo de **Subst. O.S. - TF\_SUBSTIT**, neste campo basta informar a sequência separada por vírgula.  
  
O processo de substituição é recursivo, ou seja, se for configurado na manutenção de sequência 8, que ele substitui as sequências 5,6,7, o Sistema irá verificar cada uma das sequências informadas e analisar se a mesma também substitui outras. Seguindo no exemplo, ao analisar a sequência 5, e a mesma substituir as sequências 2,3,4, o mesmo processo irá ocorrer.  
  
**Aplicabilidade em Manutenções Planejadas:**  
O processo de substituição ocorre apenas em **O.S.** geradas por meio de um planejamento **Plano de Manutenção - STI** e liberado através da rotina de **Substituição de O.S - MNTA365**.  
  
Ao realizar alguma modificação da **Manutenção - STF** entre as fases de inclusão do plano e liberação, esta alteração não será contemplada no processo de substituição, visto que todas as tarefas, insumos e etapas geradas no planejamento são cópias fiéis do **Plano de Manutenção - STF** no momento da geração do planejamento.  
  
Na liberação do plano de manutenção o Sistema verificará todas as **O.S.** para cada bem e serviço. Com base na manutenção de maior frequência, será atribuída uma margem de segurança de 50% em dias - para mais ou para menos, em relação à manutenção que será liberada.   
  
**Exemplo**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Código do Bem** | **Torno CNC001** | | | | | | |
| **Descrição da Manutenção** | **Sequência** | **Incremento** | **Acumulado** | **Substituição** | **Tarefa** | **Insumo** | **Etapa** |
| Manutenção 5.000 | 1 | 5.000 | 1 |  | TAR001 | Mecânico | Inspecionar |
| Graxa |
| Estopa |
| Manutenção 25.000 | 2 | 25.000 | 1 | 1 | TAR001 | Mecânico | Inspecionar Medir |
| Graxa |
| Estopa |
| Rolamento |
| Óleo |
| Manutenção 50.000 | 3 | 50.000 | 1 | 1,2 | TAR001 | Mecânico | Inspecionar Medir |
| Graxa |
| Estopa |
| Rolamento |
| Óleo |
| TAR002 | Eletricista | Trocar Medir Verificar |
| Fusível |
| Bateria |
| Relé |

Este é um exemplo de manutenção onde temos 3 sequências. Os elementos destacados correspondem a itens novos em relação a manutenção substituída.  
  
**Aplicabilidade em manutenções automáticas:**  
O processo de substituição ocorre quando as ordens de serviços são geradas de forma automática, por meio de reporte de contador, resposta de etapa, *check-list*, entre outros.  
  
Neste momento é verificado no **Plano de Manutenção - STF** se para a **O.S.** gerada automaticamente utiliza do processo de substituição, caso sim, o Sistema irá verificar se existem **O.S.** para o mesmo bem, serviço e com as sequências definidas no plano de manutenção.  
  
**Importante**Manutenção gerada automaticamente, ao identificar uma outra **O.S.** que se enquadre no processo de substituição, o Sistema incorporará as tarefas, insumos e etapas na nova **O.S.** e cancelará a **O.S.** já existente. Não serãoincorporadas as tarefas, etapas e insumos do plano de manutenção em função da possibilidade de ter ocorrido alterações posteriores a geração da **O.S.** existente o qual será cancelada.  
  
**Ordens de Serviço Manual**, para gerar o processo de substituição é possível habilitando o parâmetro **MV\_NG1SUBS -** **Atualiza data da última manutenção**.
