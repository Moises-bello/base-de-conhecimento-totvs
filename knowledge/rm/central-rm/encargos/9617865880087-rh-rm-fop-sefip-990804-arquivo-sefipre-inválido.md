---
article_id: 9617865880087
category: Encargos
content_hash: f0fa7741fba07530df88095ebea9e3ee27d3726ceaae15afbf7868d82a679651
fetched_at: '2026-06-28T22:46:52.422482+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: 'RH - RM - FOP - SEFIP: 990804 - Arquivo SEFIP.RE Inválido'
type: support-article
updated_at: '2025-03-11T11:08:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9617865880087-RH-RM-FOP-SEFIP-990804-Arquivo-SEFIP-RE-Inv%C3%A1lido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:15 min****Ocorrência**No módulo Folha de Pagamento, ao gerar a SEFIP está apresentando o seguinte erro: **990804 - Arquivo SEFIP.RE inválido.**  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9617750753047)  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Esse incidente ocorre, devido o sistema RM não realizar a geração do SEFIP sem movimento.  
  
**Solução**O sistema RM não realiza a geração do SEFIP sem movimento. Esse processo será realizado dentro do próprio validador do SEFIP.   
  
Segue caminho a ser realizado na plataforma do Validador do SEFIP para a geração do arquivo sem movimento:

1. Acesse: **Arquivo | Novo | Recolhimento/Declaração.**   
2. Logo, informe a competência e ano do fato gerador.  
3. Feito isso, coloque o código de recolhimento e informe que o Fato gerador é sem movimento.  
  
![](https://totvssuporte.zendesk.com/attachments/token/3ti0mkwVQzMmwTToFgyawSDC8/?name=image.png)  
  
**Importante**  
O suporte padrão da Totvs não orienta a plataforma do validador do SEFIP. Assim, orientamos que a empresa entre em contato com a Caixa, para que eles possam instruir melhor esse processo.
