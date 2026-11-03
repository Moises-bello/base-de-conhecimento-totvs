---
article_id: 360033770933
category: Manutenção de Ativos (SIGAMNT)
content_hash: 34ecbc591e6824ee0f728a1fce06d49e5c481f51648303092d4ca0fc1f9c9c46
fetched_at: '2026-06-28T22:42:34.290295+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Ordem de Serviço Manual
type: support-article
updated_at: '2023-12-12T19:47:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033770933-Manufatura-Linha-Protheus-MNT-Ordem-de-Servi%C3%A7o-Manual
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:30 min**  
**Dúvida**Para que serve a **Ordem de Serviço Manual**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**Esta rotina permite implantar uma **Ordem de Serviço Preventiva - MNTA410** de forma manual, além daquelas geradas pelo **Plano de Manutenção - MNTA331**, utilizada normalmente quando ocorre a necessidade da realização de uma **O.S. - Ordem de Serviço** preventiva fora do período de acompanhamento informado no **Cadastro de Manutenção - MNTA120**.  
As **Ordens de Serviço** incluídas por meio desta rotina, são consideradas como pertencentes ao **Plano de Manutenção - MNTA331** número **000001**. Quando da implantação da **O.S**, o programa solicita a data de execução prevista para a manutenção, fazendo todo o tratamento de insumos, verificação de disponibilidade, bloqueios e empenhos de materiais.  
Não é permitida a operação de alteração e cancelamento de **O.S**, sendo que quando esta providência for necessária, deve-se cancelar a **O.S** na rotina de **Retorno de Manutenção - MNTA400** e implantá-la novamente. No cancelamento da **O.S**, é permitida esta operação também para aquelas geradas pelo planejamento. Sempre que uma **O.S** for cancelada, os bloqueios, empenhos e providências de suprimentos anteriormente colocadas, são desfeitas automaticamente.
