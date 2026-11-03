---
article_id: 9937785445399
category: eSocial - Tabelas/Não Periódicos
content_hash: cf824ba5648feecf3062e8be147ac1b2e7b08fec8c48efe498db7140e0ed0a21
fetched_at: '2026-06-28T22:47:10.399918+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao gerar XML: O campo ''indDesFolha'' do registro
  ''infoCadastro'' é obrigatório e não está preenchido'
type: support-article
updated_at: '2024-04-05T17:19:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9937785445399-RH-RM-FOP-eSocial-Erro-ao-gerar-XML-O-campo-indDesFolha-do-registro-infoCadastro-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao gerar XML do evento S-1000 é apresentado a inconsistência: **O campo 'indDesFolha' do registro 'infoCadastro' é obrigatório e não está preenchido.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9937795566999)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões.  
  
**Causa**Este erro ocorre para o evento S-1000 **Informações do Empregador/Contribuinte/Órgão Público** quando o campo **Indicativo de Desoneração da Folha** não encontra-se preenchido.  
  
**Solução**Para preenchimento do **Indicativo de Desoneração da Folha**, realize os passos a seguir:  
1. Acesse o menu **Folha de Pagamento | eSocial | Informações do Empregador;**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9799589089175)**

2. Selecione a empresa desejada e realize o preenchimento do campo obrigatório **Indicativo de Desoneração da Folha****;**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9938652183447)

3. Após salvar, na fila de eventos gere o XML e envie ao eSocial.
