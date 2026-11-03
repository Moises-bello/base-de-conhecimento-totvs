---
article_id: 17625489470743
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 2ac6393a51856c06c0680c29780338df2b5d0d2b2a33d7957028f121a80c6844
fetched_at: '2026-06-28T22:38:56.873797+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA185 - Error.log
  type mismatch on compare  on A185ESTORN
type: support-article
updated_at: '2025-03-24T14:08:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17625489470743-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA185-Error-log-type-mismatch-on-compare-on-A185ESTORN
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17625481432343) Tempo aproximado para leitura: **00:02:10 min** **Dúvida**Ao estornar Baixa de Pré-Requisição ocorre o error.log: "*type mismatch on compare on A185ESTORN(MATA185.PRX".* Como corrigir?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Normalmente este erro ocorre na validação do tipo da pergunta 04 **"Quanto ao Estorno"**, tendo as opções "Por Documento" ou "Por Item". Ele está no grupo de perguntas MTA240, conforme print abaixo, onde recomendamos que confronte os dados com relação ao tipo, validação e tamanho:  
   
![image.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30877238462487)  
 Caso esteja diferente deste padrão, efetue um backup do ambiente, faça as edições em ambiente de homologação e tente estornar novamente para que a questão seja devidamente corrigida.  
   
**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA185 - Baixa de SA encerrada não é possível Estornar ou Excluir*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16148728781719-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA185-Baixa-de-SA-encerrada-n%C3%A3o-%C3%A9-poss%C3%ADvel-Estornar-ou-Excluir?source=search)
