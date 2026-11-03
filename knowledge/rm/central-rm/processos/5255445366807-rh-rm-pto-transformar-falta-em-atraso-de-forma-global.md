---
article_id: 5255445366807
category: Processos
content_hash: bd48e4711cb821d13dfe5bd0603ffe08a5b19fe0bc30c7ec37d9212a06f7c5f9
fetched_at: '2026-06-28T22:46:38.524421+00:00'
product: rm
section_id: 1500000861622
source: central-rm
title: RH - RM - PTO - Transformar Falta em Atraso de forma global
type: support-article
updated_at: '2026-02-04T18:28:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5255445366807-RH-RM-PTO-Transformar-Falta-em-Atraso-de-forma-global
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16503439133719) Tempo aproximado para leitura: **00:01:00  min**  
  
**Dúvida**  
Como transformar Falta em Atraso de forma global?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 12.1  
  
**Solução**  
O processo de **Transformar falta em atraso no espelho** de ponto, evita que o sistema registre a ausência como um “dia perdido” (falta integral). Ao invés disso, ele considera como atraso (horas de ausência), que podem ser compensadas ao longo da semana ou período.  
  
Para transformar Falta em Atraso no módulo de  **Automação de Ponto**, siga os passos abaixo:  
  
1. Acesse o módulo de **Automação de Ponto**, guia **Processos**, menu **Falta em Atraso/ Sobreaviso/Descanso.**

2. Clique no menu **Falta em Atraso/ Sobreaviso/Descanso**, marque o parâmetro de Transforma Falta em Atraso, preencha os dados do lançamento, selecione os funcionários desejados prencha a hora  início e fim e clique em ok.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34550680887575)

Para **cancelar/excluir** os registros lançados, realize os mesmo passos e marque a flag **"Cancelar dados lançados no período"**. Assim o sistema só irá cancelar se informar o intervalo de hora igual ao que foi lançado.

**Importante:** A folga deve ser lançada para funcionários com horário do tipo **flexível** com compensação semanal ou período que não estejam com o parâmetro "Compensa faltas" marcado no parâmetro do funcionário.

**Saiba mais**

Para mais informações sobre transformar Falta em Atraso, acesse a documentação:

[Lançamentos Globais: Autorização / Sobreaviso / Transformar falta em atraso](https://tdn.totvs.com/pages/releaseview.action?pageId=452718926)

[Lançamentos Globais - Transforma falta em atraso](https://tdn.totvs.com/pages/releaseview.action?pageId=452718925)
