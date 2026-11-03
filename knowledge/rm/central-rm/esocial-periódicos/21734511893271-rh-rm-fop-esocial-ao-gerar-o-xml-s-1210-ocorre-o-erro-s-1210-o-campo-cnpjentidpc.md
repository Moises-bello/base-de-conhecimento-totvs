---
article_id: 21734511893271
category: esocial - Periódicos
content_hash: 87af87e2541dc1e05a0d14508fa7fd785135fd0b7e6a3b22df4a1463d4a6aefa
fetched_at: '2026-06-28T22:47:09.138668+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: 'RH - RM - FOP - eSocial - Ao gerar o XML S-1210 ocorre o erro: S-1210 - O
  campo ''cnpjEntidPC'' do registro ''previdCompl'' é obrigatório e não está preenchido
  (S.1.2)'
type: support-article
updated_at: '2025-07-02T18:50:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21734511893271-RH-RM-FOP-eSocial-Ao-gerar-o-XML-S-1210-ocorre-o-erro-S-1210-O-campo-cnpjEntidPC-do-registro-previdCompl-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido-S-1-2
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21734533189143) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao gerar o XML S-1210 ocorre o erro: S-1210 - O campo 'cnpjEntidPC' do registro 'previdCompl' é obrigatório e não está preenchido.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21734511868311)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - A partir das versões 12.1.2302.235, 12.1.2306.182, 12.1.2310.116 e Superiores.  
  
**Causa**Esse erro ocorre quando há lançamento de um evento com código de cálculo de previdência complementar no envelope do funcionário, ou há algum evento sem o código de cálculo de previdência complementar e nele consta vinculado a incidência de previdência complementar e, este evento não foi informado no Cadastro da Previdência Complementar.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Identifique qual evento consta com um dos cenários supracitados.  
1.1. Para identificação dos códigos de cálculo da previdência complementar [CLIQUE AQUI](https://tdn.totvs.com/pages/releaseview.action?pageId=452719279) ;  
1.2. Para identificação de qual evento consta com codIncIRRF de previdência complementar, realize a seguinte consulta no banco de dados:  
SELECT TIPOPREVIDENCIACOMPLEMENTAR, \* FROM PEVENTO WHERE TIPOPREVIDENCIACOMPLEMENTAR IS NOT NULL

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21734533192855)

2. Após identificação, realize a vinculação do evento em **eSocial | Previdência Complementar | Cadastro Previdência Complementar**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21734511870615)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21734511871767)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21734533197591)

3. Após, regere o XML S-1210.  
  
**Saiba mais**Para mais informações acesse:  
[RH - RM - FOP - eSocial - Como informar no S-1210 o grupo de Previdência Complementar (S.1.2)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21711814151319-RH-RM-FOP-eSocial-Como-informar-no-S-1210-o-grupo-de-Previd%C3%AAncia-Complementar-S-1-2)
