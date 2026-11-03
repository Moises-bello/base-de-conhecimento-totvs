---
article_id: 6683553867159
category: Administração de Pessoal
content_hash: a567270707322779c4ba13ff37fbd649d4d95e6aaa5adf6e876a1a973ef47b21
fetched_at: '2026-06-28T22:47:01.342455+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: 'RH - RM - FOP - Cadastro de evento para desconto de plano de saúde '
type: support-article
updated_at: '2025-03-12T10:04:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6683553867159-RH-RM-FOP-Cadastro-de-evento-para-desconto-de-plano-de-sa%C3%BAde
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:25 min****Dúvida**Como realizar o desconto do plano de saúde no envelope do funcionário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**O desconto de plano de saúde ocorre por um evento específico, através de uma fórmula para cálculo de desconto, seguindo as regras da empresa.    
  
1. Realize o cadastro de um evento com código de cálculo 0, caso tenha dúvida neste cadastro [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412771329815-RH-RM-FOP-Cadastro-de-Eventos)  
  
2. Será necessário o cadastro de uma fórmula para cálculo do valor do desconto, esta fórmula deverá conter a variável **SALVAVALDEP** para que seja cadastrado no histórico de assistência saúde o valor por beneficiário, para correta geração de rotinas como a DIRF e E-social. Veja o modelo da fórmula [neste documento.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009552422-RH-RM-FOP-Parametriza%C3%A7%C3%A3o-do-Plano-de-Sa%C3%BAde-para-grava%C3%A7%C3%A3o-no-hist%C3%B3rico)  
  
3. Após o cadastro da fórmula, acesse o cadastro do evento criado no passo 1 e vincule a fórmula para cálculo de valor.   
  
4. Este evento para desconto de plano de saúde deverá ser lançado via grupo de eventos na movimentação dos funcionários.
