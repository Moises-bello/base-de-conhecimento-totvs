---
article_id: 37947139113239
category: Integrações Nativas
content_hash: 99f4c9dfa43d58687a954be2f45a8e2e9d47ced644746134ef8cd8cb7e9d1a95
fetched_at: '2026-06-28T22:42:35.477436+00:00'
product: protheus
section_id: 360012117933
source: central-protheus
title: Manufatura - Linha Protheus - MNT - O produto digitado nao faz parte da Estrutura
  do Produto XXXXXXXX da OP 999999OS001
type: support-article
updated_at: '2026-01-28T12:12:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37947139113239-Manufatura-Linha-Protheus-MNT-O-produto-digitado-nao-faz-parte-da-Estrutura-do-Produto-XXXXXXXX-da-OP-999999OS001
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37947139076631) Tempo aproximado para leitura: **00:01:15 min**  
  
**Ocorrência**  
Ao incluir um **Movimento de estoque ou realizar a baixa de uma S.A. -** relacionado a uma **O.S. - Ordem de Serviço** do módulo de **Manutenção de Ativos** ou **Gestão de Frotas** é apresentada a ocorrência **O produto digitado nao faz parte da Estrutura do Produto XXXXXXXX da OP 999999OS001. Confirma movimentação?**  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integrações Nativas - Versão 12  
  
**Causa**  
Esse incidente ocorre, o produto que está sendo movimentado não está na estrutura do produto da **O.P. - Ordem de Produção** informado no parâmetro **MV\_PRODMNT - Item de estoque para ordem de produção do SIGAMNT**, que é utilizado apenas como um item de controle para relacionamento da **O.S. - Ordem de Serviço** com a **O.P.**  
  
**Solução**  
Para que essa mensagem não seja exibida, implemente o ponto de entrada [**SD3VESR - Validação do componente na requisição**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087853)  
  
**Importante**  
Essa mensagem não depende do conteúdo **MV\_CBCFSG1 - Confere se o produto a ser requisitado pertence a estrutura do PI ou PA a ser produzido**, que é utilizado somente no módulo **SIGAACD - Automação e Coleta de Dados**
