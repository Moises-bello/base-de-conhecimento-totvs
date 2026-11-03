---
article_id: 9787261136151
category: eSocial - Tabelas/Não Periódicos
content_hash: a5e5f1d9fbc8280475603375255faaab2128b3b0ed5e3cff4432367a94c07893
fetched_at: '2026-06-28T22:47:10.348145+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao gerar S-1000: O campo ''classTrib'' do registro
  ''infoCadastro'' é obrigatório e não está preenchido'
type: support-article
updated_at: '2024-04-05T17:12:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9787261136151-RH-RM-FOP-eSocial-Erro-ao-gerar-S-1000-O-campo-classTrib-do-registro-infoCadastro-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao gerar o XML do evento S-1000 é apresentado o erro: **O campo 'classTrib' do registro 'infoCadastro' é obrigatório e não está preenchido**.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9909549286039)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões.  
  
**Causa**Este erro geralmente ocorre para o evento **S-1000 -** **Informações do Empregador/Contribuinte/Órgão Público** quando não foi criado um registro de **Informações do Empregador**.  
  
**Solução**Para solução, realize os passos a seguir:

1. Acesse o menu **Folha de Pagamento | eSocial | Informações do Empregador**;  
2. Crie um novo registro preenchendo o campo **Classificação Tributária;**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9909313866007)

3. Após inclusão, gere novamente o XML do S-1000.  
  
**Saiba mais**  
Para mais informações, acesse:  
     - [Informações do Empregador](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452718306)
