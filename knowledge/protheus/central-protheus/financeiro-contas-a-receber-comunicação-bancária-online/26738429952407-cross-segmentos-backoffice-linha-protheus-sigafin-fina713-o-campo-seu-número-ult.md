---
article_id: 26738429952407
category: Financeiro - Contas a Receber - Comunicação Bancária Online
content_hash: 2425e72419308efff739497392e019a6f7f079b30a566dab6749bbf4dc08d2ff
fetched_at: '2026-06-28T22:37:49.233014+00:00'
product: protheus
section_id: 26656227629847
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA713 - O campo seu
  número ultrapassou o limite permitido (10)
type: support-article
updated_at: '2024-10-01T15:00:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26738429952407-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-O-campo-seu-n%C3%BAmero-ultrapassou-o-limite-permitido-10
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26738414954775) Tempo aproximado para leitura: **00:08:00 min****Ocorrência**No módulo Financeiro, ao tentar realizar a transmissão por meio da rotina FINA713 via API, o sistema exibe uma mensagem de erro. **"O campo seu número ultrapassou o limite permitido (10)"**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26738429922327)**

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Esse incidente ocorre porque, por padrão, o campo E1\_NUM possui 10 caracteres. Caso o valor desse campo exceda esse limite, é necessário ajustá-lo para considerar apenas as 10 primeiras posições.

**Solução**

No *layout* de **Configuração de Contas** no **Novo Painel Gestor**, deve-se aplicar a seguinte regra:

**SUBSTR(SE1->E1\_NUM,1,10)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26738429923351)

**Saiba mais**  
[Contas a receber (Comunicação bancária online)](https://tdn.totvs.com/pages/releaseview.action?pageId=612548392)
