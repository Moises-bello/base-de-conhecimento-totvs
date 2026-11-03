---
article_id: 30806044526487
category: ACOMPANHA CUSTOS - JORNADA DE FECHAMENTO (NOVO)
content_hash: a90ad93240cf2136c337e07ff84b7333f09a613ebcf7bd8385a8fa483bbfa307
fetched_at: '2026-06-28T22:38:48.237995+00:00'
product: protheus
section_id: 5367899706647
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA038 - Qual o conceito
  sobre os status dos campos das tabelas D3X/D3Y/D3W
type: support-article
updated_at: '2025-03-21T18:25:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30806044526487-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA038-Qual-o-conceito-sobre-os-status-dos-campos-das-tabelas-D3X-D3Y-D3W
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30806069538583) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Qual é a nomemclatura do conteudo campos D3Y\_POSITI, D3Y\_STATUS e demais status das tabelas D3X e D3W no processo de uso da rotina Acompanha custos?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Protheus Release 12.1.33.  
  
**Solução**

**Não será disponibilizado um documento contendo a descrição detalhada desses Status**, pois isso poderia induzir os usuários a realizarem alterações manuais inadequadas, impactando negativamente o funcionamento do produto.

A jornada de fechamento no sistema Protheus envolve uma série de controles e códigos internos para garantir a efetivação correta dos processos. Esses controles estão distribuídos entre diversas tabelas do sistema, sendo de uso exclusivo do código-fonte. Dessa forma, qualquer alteração manual nesses registros pode comprometer a integridade e o funcionamento da jornada de fechamento.

**Status das tabelas D3X/D3Y/D3W**   
As tabelas **D3X**, **D3Y** e **D3W** possuem campos de status internos que são utilizados pelo sistema para controlar o fluxo da jornada de fechamento. Como exemplo, **D3Y\_POSITI = EXEMPLO**, que é um dos códigos utilizados pelo sistema para validar etapas do processamento.

Reforçamos que **nenhuma alteração manual deve ser realizada nas tabelas e códigos da jornada de fechamento**. Esses dados fazem parte do funcionamento interno do sistema e qualquer intervenção pode resultar em inconsistências operacionais, comprometendo o correto processamento dos **fechamentos/reaberturas/cancelamentos.**

**Mas como acompanhar os status sem saber sua função?**  
Caso seja necessário acompanhar o status dos processos na jornada de fechamento, a própria rotina **Acompanha Custos** exibe os status diretamente na interface do sistema. Os status disponíveis são:  
- Concluído  
- Cancelado  
- Em Processamento  
- Reabertura

Dessa forma, todas as informações necessárias para acompanhamento podem ser obtidas diretamente pela interface do sistema, sem necessidade de acesso direto às tabelas internas.

**Saiba mais sobre a jornada de fechamento e suas funcionalidades aqui:** [Novo Fechamento - Jornada de Fechamento](https://tdn.totvs.com/x/S64fIg)

O suporte está à disposição para esclarecer quaisquer dúvidas e auxiliar na utilização correta da jornada de fechamento. Caso o cliente enfrente dificuldades durante o processo, ou algum erro de processamento que envolva esse conceito, recomendamos entrar em contato para uma análise detalhada e suporte adequado.

**Saiba mais**:

*[Clique aqui e veja mais artigos sobre a Nova Jornada de Fechamento no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/5367899706647-ACOMPANHA-CUSTOS-JORNADA-DE-FECHAMENTO-NOVO-)*
