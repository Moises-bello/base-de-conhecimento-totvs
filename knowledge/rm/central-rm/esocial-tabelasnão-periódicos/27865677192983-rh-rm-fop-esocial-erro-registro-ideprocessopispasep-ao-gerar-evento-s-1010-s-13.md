---
article_id: 27865677192983
category: eSocial - Tabelas/Não Periódicos
content_hash: 05070baf1ef1764ea15f783bfb18a8f2ca59ff589f2a09d7656931d4d53cef40
fetched_at: '2026-06-28T22:47:10.456169+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: RH - RM - FOP - eSocial - Erro registro 'ideProcessoPisPasep' ao gerar evento
  S-1010 (S-1.3)
type: support-article
updated_at: '2026-06-01T14:01:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27865677192983-RH-RM-FOP-eSocial-Erro-registro-ideProcessoPisPasep-ao-gerar-evento-S-1010-S-1-3
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27865677188887)**Tempo aproximado para leitura: **00:02:00 min**

**Ocorrência**Ao gerar evento S-1010, é apresentada mensagem: **Erro Registro 'ideProcessoPisPasep': Em caso de isenção de incidência é necessário informar o processo judicial com decisão/sentença favorável no cadastro da Rubrica em 'Anexos | Processo Suspensão de Incidência'**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27865706206231)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões  
  
**Causa**  
Esse erro geralmente ocorre quando foi informado um código de incidência de PIS/PASEP de suspensão judicial, porém não foi informado o processo relacionado.  
  
**Solução**  
Para correção, é importante verificar se a incidência está corretamente informada e, se sim, indicar qual o processo vinculado à suspensão judicial.

* **Correção da incidência**

Caso a verba não tenha incidência suspensa, acesse o menu **Administração de Pessoal | Eventos**. Na aba **Inc. Proventos** ou **Inc. Descontos** (conforme tipo da verba) e valide o campo **Incidência PIS/PASEP**. Para as incidência **91** e **92** é necessário informar o número do processo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27865840506007)

* **Informar o número do processo**

Para informar o número do processo judicial ligado à suspensão da incidência do PIS/PASEP, acesse o menu **Administração de Pessoal | Eventos | Anexos | Processo de Suspensão de incidência** e inclua um novo registro do tipo de tributo **PIS/PASEP**. 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27865814322455)

Ao gerar o XML do evento S-1010, será exibido o grupo ***ideProcessoPisPasep*** com o número do processo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27865924596247)

**Saiba mais**  
Para mais informações, acesse:  
     -  [Leiaute Versão S-1.3 e NT 01/2024](https://tdn.totvs.com/pages/releaseview.action?pageId=862114556)
