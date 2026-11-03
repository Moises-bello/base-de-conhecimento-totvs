---
article_id: 16148728781719
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 2d1881a69c665b43ef2604d836d5a71cb5a681d6636c42114048b227f79a3014
fetched_at: '2026-06-28T22:38:55.799908+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA185 - Baixa de
  SA encerrada não é possível Estornar ou Excluir
type: support-article
updated_at: '2025-08-07T16:45:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16148728781719-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA185-Baixa-de-SA-encerrada-n%C3%A3o-%C3%A9-poss%C3%ADvel-Estornar-ou-Excluir
---

O artigo aborda a dificuldade em estornar ou excluir uma baixa de solicitação ao armazém quando esta está encerrada no sistema TOTVS Backoffice (Linha Protheus). Quando o status é alterado para "encerrada", não é possível realizar ações de estorno. A solução proposta é copiar a solicitação na rotina MATA105 e criar uma nova conforme necessário, permitindo a geração de novas solicitações.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16148733897623) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Ao tentar Estornar ou Excluir uma Baixa de Solicitação ao Armazém que foi encerrada (legenda Azul), não permite e apresenta os ***Helps A185ESTORNO e A185EXCL***? Como efetuar o processo de Baixa quando a Legenda igual a Encerrada?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16148920260119)  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**  
Para esse cenário, ***não é possível*** ***Estornar ou Excluir*** a Baixa da Solicitação ao Armazém, quando alterada o Status para encerrada (campo CP\_STATUS = E).  
  
Nesse cenário o mais adequado é: **na rotina MATA105 copiar a Solicitação ao Armazém e criar uma nova SA conforme a necessidade específica de forma que possa gerar novas solicitações**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16149659017751)

***Saiba Mais:***  
[*Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)

[*Solicitação, Pré-Requisição e Baixa da Pré-Requisição - MATA105 - MATA106 - MATA185*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018562511-MP-SIGAEST-Solicita%C3%A7%C3%A3o-Pr%C3%A9-Requisi%C3%A7%C3%A3o-e-Baixa-da-Pr%C3%A9-Requisi%C3%A7%C3%A3o-MATA105-MATA106-MATA185?source=search)
