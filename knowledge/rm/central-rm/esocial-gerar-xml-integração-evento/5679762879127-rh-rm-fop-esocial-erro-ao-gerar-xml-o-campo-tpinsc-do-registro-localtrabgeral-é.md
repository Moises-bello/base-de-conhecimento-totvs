---
article_id: 5679762879127
category: eSocial - Gerar XML/ Integração Evento
content_hash: c95ff8f2a0b608b880700a0f80297b69708165dc95610b1bf3caf165c512d26c
fetched_at: '2026-06-28T22:47:12.218046+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao gerar XML:  O campo ''tpInsc'' do registro
  ''localTrabGeral'' é obrigatório e não está preenchido'
type: support-article
updated_at: '2024-06-27T19:21:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5679762879127-RH-RM-FOP-eSocial-Erro-ao-gerar-XML-O-campo-tpInsc-do-registro-localTrabGeral-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20767878763543) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao realizar a geração do XML dos eventos S-2200, S-2205 e S-2206 ocorre o erro:   
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5679176540823)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todos os Patches  
  
**Causa**Esse incidente ocorre, quando o histórico da seção não está preenchido, assim as *tags* **tpInsc** e **nrInsc** não carregam a informação corretamente.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5679226464663)

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse **Folha de Pagamento | Administração de Pessoal | Funcionário | Seção;**

**![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5679446240151)**

2. Acesse **Folha de Pagamento | Administração de Pessoal | Funcionário | Anexo | Histórico | Histórico da Seção;**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5679290381847)

3. Crie um novo histórico, preencha de acordo com as informações do item 1 (Seção que o funcionário está alocado);

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5679427432727)

4. Refaça a geração do XML.
