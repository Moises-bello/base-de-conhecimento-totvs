---
article_id: 6961930290455
category: esocial - Periódicos
content_hash: 2cebe1d8c4671889d3fe8c266d6510c216e1297d3610a18aa16f3b023925eb38
fetched_at: '2026-06-28T22:47:09.314420+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao gerar S-1200: Erro ao calcular campo CampoCodLotacao'
type: support-article
updated_at: '2024-06-26T13:06:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961930290455-RH-RM-FOP-eSocial-Erro-ao-gerar-S-1200-Erro-ao-calcular-campo-CampoCodLotacao
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao gerar o XML do evento S-1200 é apresentada mensagem **Erro ao calcular campo CampoCodLotacao - System.ArgumentNullException: Value cannot be null**.**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**O erro geralmente ocorre quando a coligada está configurada para utilizar tomadores de serviços e o sistema não encontra informação da **Lotação Tributária** correspondente.  
  
**Solução**  
Para solucionar esse erro, realize os seguintes passos:

1. Acesse o menu eSocial | Lotação Tributária;  
2. Clique em Processos | Gerar Lotação Tributária;  
3. Após conclusão do processo, gere novamente o XML do S-1200;

Se o problema persistir, entre em contato com o atendimento técnico para análise, enviando evidências (print, videos, logs, etc) do cadastro das lotações, rateio do funcionário, etc.  
  
**Saiba mais**  
Para mais informações, acesse:  
     - [Histórico de rateio por tomador de serviços](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026677233)
