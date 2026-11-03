---
article_id: 19782553571735
category: SIGAEST - CUSTOS
content_hash: ab96c88ab903ff6ab8f1f8299981dcf5e1d250d8f4da265d7b00a5a538b697dc
fetched_at: '2026-06-28T22:39:01.989119+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - InterFunctionCall:
  cannot find function VLDPROCSB2 in AppMap on VERIFYINITAPP'
type: support-article
updated_at: '2025-03-12T12:23:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19782553571735-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-InterFunctionCall-cannot-find-function-VLDPROCSB2-in-AppMap-on-VERIFYINITAPP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19782568055575) Tempo aproximado para leitura: 00:02:00 min**Ocorrência**Ao executar a rotina Acompanha Custos é gerado o errorlog: **InterFunctionCall: cannot find function VLDPROCSB2 in AppMap on VERIFYINITAPP**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/19782598387607)**

**Ambiente:**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**  
Houve uma correção nesse fonte em relação a função **VldProcSB2**, sob o novo parametro MV\_A330SB2 ao processar o custo médio.

Caso queira saber mais sob o novo parâmetro acesse abaixo:  
<https://tdn.totvs.com/pages/viewpage.action?pageId=722655643>  
   
  
**Solução**

Para correção do help siga os passos abaixo:

Em base teste efetue a atualização abaixo, caso esteja desatualizado:  
- Acumulado SIGAEST conforme sua versão:<https://tdn.totvs.com/pages/releaseview.action?pageId=522000602>  
- Central das procedures: <https://suporte.totvs.com/portal/p/10098/download?e=946864>

Após as atualizações, reinstale as procedures 14 a 22 com o novo gestor, conforme exemplo do boletim abaixo.  
[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Procedure Desatualizada e Incompatível, quais as diferenças? É possível utilizar as rotinas?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15131065568791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Procedure-Desatualizada-e-Incompat%C3%ADvel-quais-as-diferen%C3%A7as-%C3%89-poss%C3%ADvel-utilizar-as-rotinas-)

**Importante**: Execute a aplicação do pacote em ambiente de homologação para validação e somente depois de aprovado coloque em produção. (Antes de qualquer ação realize o backup do ambiente).

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
