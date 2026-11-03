---
article_id: 360007713171
category: Encargos
content_hash: 7d5afebfe45c346121b34edd45154d5dab24fe600f4e32e29cc8532c4a9c48a2
fetched_at: '2026-06-28T22:46:53.410377+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: 'RH - RM - FOP - SEFIP: Já existe o mesmo PIS/PASEP/CI'
type: support-article
updated_at: '2025-03-05T18:56:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007713171-RH-RM-FOP-SEFIP-J%C3%A1-existe-o-mesmo-PIS-PASEP-CI
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:20 min  
  
Ocorrência**Ao importar o arquivo da SEFIP o sistema apresenta a seguinte mensagem de erro:   
**Já existe o mesmo PIS/PASEP/CI cadastrado com código de ocorrência que não permite múltiplos vínculos**.![Sem_t_tulo.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360007967172/Sem_t_tulo.png)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**O incidente ocorre porque o funcionário foi demitido e readmitido no mesmo mês e o campo **Código da Ocorrência** que se encontra na aba **FGTS/SEFIP** está diferente nos cadastros, tanto no cadastro do funcionário demitido quanto na nova chapa.  
  
Acesse: **Administração de Pessoal | Funcionários** editando o funcionário em questão, na aba **FGTS/SEFIP**, campo **SEFIP:****![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10960179640215)**  
**Solução**Para solucionar esta ocorrência, realize os seguintes passos:  
1. Acesse o cadastro do funcionário demitido, acesse a aba de FGTS/SEFIP e altere o código da ocorrência para 5;  
2. Acesse o novo cadastro do funcionário, acesse a aba de FGTS/SEFIP e altere o código da ocorrência também para 5;  
3. Feitos os passos anteriores, realize novamente a geração da SEFIP e importe o arquivo no validador do SEFIP.
