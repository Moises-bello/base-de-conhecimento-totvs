---
article_id: 360025682772
category: Manutenção de Ativos (SIGAMNT)
content_hash: 20e049bd22ccd95468182679ccd19d715585f579ee80e59569cc0be11443d79c
fetched_at: '2026-06-28T22:42:33.073797+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Contador fixo
type: support-article
updated_at: '2021-10-29T11:41:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025682772-Manufatura-Linha-Protheus-MNT-Contador-fixo
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:30 min****Dúvida**Qual é o conceito do contador fixo?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**Esta é uma das modalidades de controle de manutenção por contador. A particularidade é que a data de cada manutenção fica pré-estabelecida na implantação da preventiva, podendo ser modificada, caso o usuário modifique o campo de informação de incremento da manutenção. O fato de estar pré-estabelecida a data das próximas manutenções não resulta que o **Manutenção de Ativos -** **SIGAMNT** irá gerar as **O.S. - Ordens de Serviço**.  
   
Os procedimentos de alimentação do contador ou produção, com a consequente atualização dos campos do cadastro de **Bens - ST9**, não sofrem alteração. São os padrões da **NG**.   
  
Assim consideremos o exemplo abaixo, de uma manutenção controlada por contador fixo.  
  
Incremento entre manutenções **2.300**.

|  |  |
| --- | --- |
| **Ordem de Serviço** | **Contador** |
| 000001 | 2.300 |
| 000002 | 4.600 |
| 000003 | 6.900 |

No momento da implantação da **O.S. Preventiva** as posições de contador das próximas manutenções são as acima relacionadas. Para a obtenção da data da próxima manutenção, utiliza-se o procedimento padrão da **NG**.  
  
O estabelecimento rígido do contador da próxima manutenção, não obriga que a execução da **O.S.** tenha que seguir o planejado.  
  
Consideremos que a última **O.S.** que tenha sido executada foi com o contador em 6.000. Com que posição de contador deverá ser executada a próxima **O.S.**?  
  
Para sanar este tipo de problema o **SIGAMNT** aplica um percentual definido pelo parâmetro **MV\_NGCOFIX - Percentual utilizado para calcular o intervalo que compreende a realização da Manutenção de Contador Fixo**, neste exemplo será considerado como **20%**para cima e para baixo, sobre o contador da última manutenção. Neste exemplo obterão os valores **4.800/7.200**.  
  
A manutenção a que se refere a última **O.S.** executada é a prevista para **6.900**. Assim a próxima será a de **9.200**.
