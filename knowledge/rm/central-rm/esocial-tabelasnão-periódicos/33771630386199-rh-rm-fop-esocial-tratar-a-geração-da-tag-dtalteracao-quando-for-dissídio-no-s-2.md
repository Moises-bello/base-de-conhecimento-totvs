---
article_id: 33771630386199
category: eSocial - Tabelas/Não Periódicos
content_hash: f840c642c8acd327ae71406192304d0084eeedf10ce91d99bbbb89bbf7c792ca
fetched_at: '2026-06-28T22:47:10.517964+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: RH - RM - FOP - eSocial - Tratar a geração da tag <dtAlteracao> quando for
  dissídio no S-2206
type: support-article
updated_at: '2026-05-27T20:27:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33771630386199-RH-RM-FOP-eSocial-Tratar-a-gera%C3%A7%C3%A3o-da-tag-dtAlteracao-quando-for-diss%C3%ADdio-no-S-2206
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33771603186711) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Como tratar a geração da tag <dtAlteracao> quando for dissídio no S-2206?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial  - Todas as versões  
  
**Solução**  
Permitir que, na alteração salarial por dissídio, seja possível definir a data a ser preenchida no campo "Data de Inclusão", pois atualmente, esse campo é automaticamente preenchido com a data  da execução do aumento (data do sistema operacional). No entanto, em situações onde a alteração não é processada no mesmo dia em que o dissídio foi liberado, a data inserida fica incorreta, resultando em inconsistências na geração do evento S-2206, que utiliza este campo para preencher a tag <dtAlteracao>.  
  
**1.** Acesse o Menu: Administração de Pessoal | Alterações Cadastrais | Alteração de Salários:  
Ao selecionar o motivo "**Dissídio**" no campo "**Motivo alteração salarial**", o parâmetro "**Alterar Data de Inclusão**" será exibido, e:

* Se este parâmetro for marcado, o campo **"Data de Inclusão**" será habilitado, permitindo ao usuário informar a data real de liberação do dissídio:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33771630374167)

Caso o **parâmetro não esteja marcado**, o sistema preencherá automaticamente o campo com a data atual do sistema operacional:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33772266252183)

**ATENÇÃO:**

É obrigatório preencher o campo **"Data de Inclusão"** caso o parâmetro **"Alterar Data de Inclusão"** esteja marcado.  
Por padrão, o campo **"Data de Inclusão"** será preenchido com a data atual do sistema operacional.

2. Ir no Menu  eSocial | Gerar XML:  
Na geração do evento **S-2206**, a tag <dtAlteracao> será preenchida com a data informada no campo **"Data de Inclusão"** presente no histórico salarial do funcionário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33772418694807)

**Saiba Mais:**  
[Alteração Global de Salários](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719361)  
[DT - S-2206 - Tratar a geração da tag <dtAlteracao> quando for dissídio](https://tdn.totvs.com/pages/releaseview.action?pageId=899189200)  
[Mapeamento do evento S-2206](https://tdn.totvs.com/display/LRM/Evento+S-2206)
