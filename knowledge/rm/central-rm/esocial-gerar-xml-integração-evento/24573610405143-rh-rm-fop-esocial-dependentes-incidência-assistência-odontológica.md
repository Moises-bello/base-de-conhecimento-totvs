---
article_id: 24573610405143
category: eSocial - Gerar XML/ Integração Evento
content_hash: 2504372667e7c45d05c56a422ee6c5b1c78182c933f50211e7f22cad8d7b0e4d
fetched_at: '2026-06-28T22:47:12.076412+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Dependentes - Incidência Assistência Odontológica
type: support-article
updated_at: '2026-03-03T18:09:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24573610405143-RH-RM-FOP-eSocial-Dependentes-Incid%C3%AAncia-Assist%C3%AAncia-Odontol%C3%B3gica
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24573605019031) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Como parametrizar o cadastro de dependentes para desconto de assistência odontológica?   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**  
Foi criado um parâmetro na aba de incidências possibilitando que o usuário marque a opção Assistência Odontológica, conforme apresentado abaixo. Ao marcar este parâmetro, o sistema passa a enviar as informações dos dependentes para o eSocial. 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24573605021079)

Processos que passam a levar os dados do dependente (não possuí tag especifica para a assistência odontológica no xml do eSocial) considerando o novo campo:

* Geração do evento S-2200 e S-2205
* Geração do XML em lote S-2205
* Importação e exportação do dependente do funcionário
* Histórico de Assistência Médica flag “Somente com Incidência”, será considerado na seleção do beneficiário.

**Saiba mais**  
[DT - Dependentes - Incidência Assistência Odontológica](https://tdn.totvs.com/pages/releaseview.action?pageId=852297417)
