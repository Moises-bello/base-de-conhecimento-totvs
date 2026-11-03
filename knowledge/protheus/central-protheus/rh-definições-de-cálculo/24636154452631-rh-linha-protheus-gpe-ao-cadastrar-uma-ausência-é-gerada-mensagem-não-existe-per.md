---
article_id: 24636154452631
category: RH - Definições de Cálculo
content_hash: 1e87f00c2422c26b3af5c44aa82d2d2ad4bde80480cb0218033bc629dd42acd6
fetched_at: '2026-06-28T22:43:22.212647+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: 'RH - Linha Protheus - GPE -  Ao cadastrar uma Ausência, é gerada mensagem:
  "Não existe período cadastrado para esta data ou o período não está aberto"'
type: support-article
updated_at: '2026-06-26T16:40:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24636154452631-RH-Linha-Protheus-GPE-Ao-cadastrar-uma-Aus%C3%AAncia-%C3%A9-gerada-mensagem-N%C3%A3o-existe-per%C3%ADodo-cadastrado-para-esta-data-ou-o-per%C3%ADodo-n%C3%A3o-est%C3%A1-aberto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24636116788759) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**No lançamento de Ausências, ao informar a data do Afastamento é apresentada mensagem de que **Não existe período aberto cadastrado para esta data ou o período não está aberto.**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/24951443301399)** **Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**A mensagem é gerada quando **não existe o cadastro do Período ou do roteiro FOL** para a data em que o Afastamento precisa ser cadastrado.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
**1.** Após a tentativa de inclusão de um Afastamento para o mês de Março/24, é apresentada a mensagem informando a **inexistência do período**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24941913802391)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24941920376343)

**2.** Em **Atualizações> Definições de Cálculo> Períodos,** veja que **não há período** criado para esta competência:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24941920380183)

**3.** Faça a **inclusão do Período** e do **roteiro FOL** correspondente a data de lançamento da Ausência, neste caso, do mês de Março/24:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24941913816727)

**4.** Após a criação do **Período**, o lançamento é efetuado corretamente:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24941920387735)

**Saiba Mais:**  
[Artigos - Ausências](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011967353-RH-Tipos-de-Aus%C3%AAncias)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
