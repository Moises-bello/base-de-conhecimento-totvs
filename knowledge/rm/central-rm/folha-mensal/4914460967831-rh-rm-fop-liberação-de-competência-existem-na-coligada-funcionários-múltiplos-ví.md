---
article_id: 4914460967831
category: Folha Mensal
content_hash: faa64948653ff8ec0e0f7cfead7c26fd3fe6c1f5dd8927384e62d1216ea3651a
fetched_at: '2026-06-28T22:46:59.236789+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Liberação de Competência: Existe(m) na Coligada funcionário(s)
  Múltiplos Vínculos com pendência de recálculo'
type: support-article
updated_at: '2025-01-21T18:23:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4914460967831-RH-RM-FOP-Libera%C3%A7%C3%A3o-de-Compet%C3%AAncia-Existe-m-na-Coligada-funcion%C3%A1rio-s-M%C3%BAltiplos-V%C3%ADnculos-com-pend%C3%AAncia-de-rec%C3%A1lculo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**No módulo Folha de Pagamento, ao realizar a liberação de competência está apresentando a seguinte mensagem de erro:  
  
**Existe(m) na Coligada funcionário(s) Múltiplos Vínculos com pendência de recálculo:**  
**XXXX - xxx xxxx xxxx xxxx****Essas pendências de recálculo podem ocasionar diferenças no cálculo do INSS para o eSocial. Se ainda desejar liberar a competência, poderá marcar o parâmetro "Não bloquear liberação de competência caso exista pendência de recálculo de múltiplos vínculos" no parametrizador."**  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Esse incidente ocorre, pois não foi executado o processo Recálculo Multi-Coligadas ou a flag **Não bloquear liberação de competência caso exista pendência de recálculo de múltiplos vínculos** está desmarcada.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Primeiramente, realize o que se pede no erro. Para isso, acesse:**Folha Mensal | Lançamentos | Recálculo Multi-Coligadas** do funcionário que fora listado no aviso e selecionando as duas coligadas.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4914120739095/mceclip0.png)  
  
Logo, após execução com sucesso, realize o processo da liberação de competência novamente. Caso o erro ainda persista, acesse: **Configurações | Parametrizador | Folha Mensal | Geral**e marque a flag destacada na imagem abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4914054243095/mceclip1.png)  
  
**Saiba Mais**  
[Múltiplos Vínculos que necessitam de Recálculo](https://tdn.totvs.com/pages/releaseview.action?pageId=465386747)
