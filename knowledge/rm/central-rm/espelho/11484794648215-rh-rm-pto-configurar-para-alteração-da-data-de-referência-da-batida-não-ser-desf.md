---
article_id: 11484794648215
category: Espelho
content_hash: 4dcc809d566f5e8d9d2ea83cccddec22f8887dfad277f2834dc1fcf855461d6d
fetched_at: '2026-06-28T22:46:31.266258+00:00'
product: rm
section_id: 6045459696023
source: central-rm
title: RH - RM - PTO - Configurar para alteração da data de referência da batida não
  ser desfeito
type: support-article
updated_at: '2025-01-09T16:47:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11484794648215-RH-RM-PTO-Configurar-para-altera%C3%A7%C3%A3o-da-data-de-refer%C3%AAncia-da-batida-n%C3%A3o-ser-desfeito
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15860891471255) Tempo aproximado para leitura: **00:01:30min** **Dúvida**Após ajustar a data de referência da(s) batida(s) de forma manual, ao realizar o recálculo do ponto ou uma nova importação de batidas a alteração é desfeito, o que fazer?  
  
**Ambiente**RH - RH (Linha RM) - TOTVS Automação de Ponto- 12.1.18 e superiores  
  
**Solução**

Para que não ocorra a desconfiguração das batidas já corrigidas, siga os passos abaixo:

1. Acesse o menu Configurações | Parametrizador ao abrir o assistente clique em avançar e selecione o processo **08.01- Iniciais** e avance.
2. Será aberto um novo assistente e avance até a **Etapa 2 - Importação** e marque q flag do parâmetro "**Considera a alteração da data de referência no recálculo"****.**  
   ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11484578015383)  
   Ao marcar o parâmetro, irá manter a alteração da data de referência das batidas ao realizar o recálculo, evitando o deslocamento de batidas.  
     
   Observação: Mesmo que faça o recálculo com todos os parâmetros marcados , incluindo o **Atualiza jornada de referencia das batidas,** a alteração não será desfeita**.**
3. ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11484854119959)

**Saiba Mais:**  
Informações sobre o parâmetro: [Alteração de data de referência](https://tdn.totvs.com/pages/releaseview.action?pageId=528453522)  
Mais detalhes sobre as demais parametrizações: [Parâmetros da Importação](https://tdn.totvs.com/pages/viewpage.action?pageId=452719611)  
[Batidas com jornada de referencia errada após realização de recalculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11467075990807)
