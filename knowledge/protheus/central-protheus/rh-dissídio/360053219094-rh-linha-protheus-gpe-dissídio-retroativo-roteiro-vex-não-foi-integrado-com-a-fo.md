---
article_id: 360053219094
category: RH - Dissídio
content_hash: 3bb1ab3bc79543e9a0c0d3aa45500bd3e6b156ffa2edbedf5c700519b0f69b9f
fetched_at: '2026-06-28T22:43:43.331365+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Dissídio retroativo - Roteiro VEX não foi integrado
  com a folha de pagamento
type: support-article
updated_at: '2025-08-05T19:47:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053219094-RH-Linha-Protheus-GPE-Diss%C3%ADdio-retroativo-Roteiro-VEX-n%C3%A3o-foi-integrado-com-a-folha-de-pagamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33964626834711)** Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**Ao executar o dissídio, o Sistema gera somente a verba 000 - Salário para algum ou todos os meses definidos nos parâmetros de cálculo. No log é apresentado a seguinte mensagem:  
  
"Competência calculada XXXX/XX  
Existem roteiros que não foram integrados com a folha. Execute a interação antes do cálculo.   
VEX - Valores extras."  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Causa**  
Dentro da competência (Atualizações/ Definições de cálculo/ Períodos) apontada pelo sistema no log de ocorrências o roteiro VEX está sem data de integração.  
  
**Solução**1. Confirme se em Atualizações/ Definições de cálculo/ Roteiros de cálculo/ VEX o campo "Integra?" está com o conteúdo igual a Sim. Caso positivo a execução do dissídio irá validar se existe no roteiro VEX uma data de integração;  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089718713)  
Utilização do roteiro VEX: <https://tdn.totvs.com/x/LHaWDg>  
  
2. Inclua uma data de integração no roteiro VEX dentro das competências apontadas pelo sistema no log de ocorrência via banco de dados.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088571014)  
  
**Saiba mais:**  
[RH - Dissidio](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio)
