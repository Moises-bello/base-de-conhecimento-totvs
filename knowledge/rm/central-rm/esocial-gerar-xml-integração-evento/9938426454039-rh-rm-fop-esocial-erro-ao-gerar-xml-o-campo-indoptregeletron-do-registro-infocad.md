---
article_id: 9938426454039
category: eSocial - Gerar XML/ Integração Evento
content_hash: 31fb528389fc2844b47330c20dc5c7394287f81562df03602843a4c94ccd1a56
fetched_at: '2026-06-28T22:47:12.227001+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao gerar XML: O campo ''indOptRegEletron''
  do registro ''infoCadastro'' é obrigatório e não está preenchido'
type: support-article
updated_at: '2024-07-01T17:12:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9938426454039-RH-RM-FOP-eSocial-Erro-ao-gerar-XML-O-campo-indOptRegEletron-do-registro-infoCadastro-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24180588325143) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao gerar XML do evento S-1000 é apresentada a inconsistência **O campo 'indOptRegEletron' do registro 'infoCadastro' é obrigatório e não está preenchido.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9938280701975)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões.  
  
**Causa**Este erro ocorre para o evento **S-1000** **Informações do Empregador/Contribuinte/Órgão Público** quando o campo **Indicativo de Optante Pelo Registro Eletrônico** é obrigatório e não está preenchido.  
  
**Solução**Para preenchimento do **Indicativo de Optante Pelo Registro Eletrônico**, realize os passos a seguir:  
1. Acesse o menu **Folha de Pagamento | eSocial | Informações do Empregador;**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24180559906071)**

2. Selecione a empresa desejada e realize o preenchimento do campo obrigatório **Indicativo de Optante Pelo Registro Eletrônico;**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9938431325079)

3. Após ajuste, na fila de eventos gere o XML e envie ao eSocial.
