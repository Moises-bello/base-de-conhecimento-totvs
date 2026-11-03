---
article_id: 9241811164183
category: RH - Rescisão
content_hash: 06e8fc33c6ecb2018f16fd186bcc67ce97dc8bba5c612ea1e36fbcca1be4bc03
fetched_at: '2026-06-28T22:43:49.909307+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: 'RH - Linha Protheus - GPE - Por que rescisão complementar apresenta a mensagem:
  O campo Valor (RR_VALOR) não foi preenchido'
type: support-article
updated_at: '2025-06-12T12:09:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9241811164183-RH-Linha-Protheus-GPE-Por-que-rescis%C3%A3o-complementar-apresenta-a-mensagem-O-campo-Valor-RR-VALOR-n%C3%A3o-foi-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Por que rescisão complementar apresenta a mensagem: O campo Valor (RR\_VALOR) não foi preenchido?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9241611107991/mceclip0.png)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**A mensagem pode ser gerada devido o campo RR\_VALOR estar como obrigatório. Editando para que não seja obrigatório, a mensagem não será exibida.

Acesse o **SIGACFG - Configurador;**

Acesse a rotina Base de Dados pelo caminho **Base de Dados\Dicionário\Base de Dados:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9320956862871)

Pesquise pela tabela **SRG** e clique em **Campos,** busque o campo **RR\_VALOR.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9241782073239/mceclip1.png)

Deixe a opção Obrigat. usuário sem seleção e Salve a alteração:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9241787252503/mceclip2.png)
