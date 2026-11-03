---
article_id: 38837328718359
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 216349f7ec701fa4a5ad9b300becc1b3c31ad266ef26270d1219d28062b0262e
fetched_at: '2026-06-28T22:38:55.627853+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Lentidão e Travamento
  na rotina Solicitação ao Armazém como corrigir?
type: support-article
updated_at: '2026-03-19T13:03:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38837328718359-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Lentid%C3%A3o-e-Travamento-na-rotina-Solicita%C3%A7%C3%A3o-ao-Armaz%C3%A9m-como-corrigir
---

O artigo orienta como corrigir lentidão e travamento na inclusão da Solicitação ao Armazém no Protheus, recomendando desabilitar customizações, verificar alterações recentes no sistema e, se o problema persistir, gerar LogProfiler e DBTrace para análise detalhada das funções e queries que causam o travamento.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38837288215191) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Na inclusão da Solicitação ao Armazém, ocorre uma lentidão e travamento como corrigir?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Para avaliar lentidão na rotina Solicitação ao Armazém, é necessário realizar essas etapas para uma análise mais detalhada:

1° Passo - Por gentileza, para garantirmos que não há nenhum customizável influenciando neste comportamento, peço que desabilite os customizáveis presentes no ambiente.  
   
Procedimentos para desativar as customizações:  
1 - [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como desabilitar customizações no Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018286552-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-desabilitar-customiza%C3%A7%C3%B5es-no-Protheus)  
   
2 - E insira também a chave IXBLOG = NORUN no Appserver do Protheus.  
   
OBS: Se o travamento for sanado neste teste, acende-se um alerta para algum ponto de entrada e/ou customização influenciando no travamento  
   
2° Passo - Confirme se houve algum fator no sistema (Exemplo: migração de release, de banco de dados, patch ou compilação de alguma customização) que a partir dela suspeite que pode ter desencadeado o problema. Nos forneça esses detalhes caso tenham ocorrido  
   
3° Passo - Se mesmo com o ambiente livre de customizações persistir travando, vamos gerar o LogProfiler e DBTrace para entender qual função e query que  trava e encaminha o console.log;

* LOGPROFILER e o Log DBTrace : [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como gerar o LogProfiler e Dbtrace?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019902592-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-gerar-o-LogProfiler-e-Dbtrace)

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
