---
article_id: 4406613812247
category: Gestão de Transportes (TMS)
content_hash: 6f2ca0880a715add38b44251328230cd590cc529c8c25c4d1da0422b3439850e
fetched_at: '2026-06-28T22:45:33.388743+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Tabela de frete a receber por KM
type: support-article
updated_at: '2026-03-03T13:00:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406613812247-Log%C3%ADstica-Linha-Protheus-TMS-Tabela-de-frete-a-receber-por-KM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38766681434647) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como configurar uma **tabela de frete a receber por KM - Quilômetro** no **TOTVS Logística TMS**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**  
Para definir um valor de frete por **KM**, você precisa:  
Na rotina **Componentes de Frete - TMSA030**, cadastrar um componente de frete que calcula sobre **KM - DT3\_TIPFAI = 08 - KM.**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406614238871)**

Na rotina **Configuração Tabela de Frete - TMSA130**, criar uma configuração de tabela de frete para o componente por **KM**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406614395287)

Na rotina **Tabela de Frete - TMSA010,** criar uma tabela de frete para a configuração criada. Na tabela de frete, você pode definir faixas por **KM**.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406608291607)

![](https://totvssuporte.zendesk.com/attachments/token/yWotNsaL7GjP3ZIxfGUyvoxmb/?name=inline-1606884738.png)

Ao definir as faixas de **KM**, o Sistema irá calcular o valor definido por faixa de **km** conforme a fração definida. Sempre indicamos que configure um valor por **KM** e indique a fração como 1, para que o Sistema calcule o total do **KM** cobrando o Valor por **KM**.  
  
Após gerar a tabela de frete, deve vinculá-la no **Contrato do Cliente - TECA250** no campo **Tab Frete - DDA\_TABFRE**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406609092887)

Segue exemplo de cálculo que o Sistema realiza conforme a configuração apresentada:

Na **Entrada de documentos - TMSA050**, ao preencher o campo **DTC\_KM**, o Sistema irá calcular o **KM** informado conforme a tabela de frete da seguinte forma:

* Para até 300 **KM**: 300 (**Km** informado) x 2,80 (Valor por **KM**) = 840 reais

![](https://totvssuporte.zendesk.com/attachments/token/8GA8joiZISNU8RmIqRvGqakuR/?name=inline-833047679.png)​

* Para até 500 km: 500 (**Km** informado) x 3,00 (Valor por **KM**)= 1500 reais.

![](https://totvssuporte.zendesk.com/attachments/token/ywpe1bYKJDQzQt1DHRiCu4KW7/?name=inline-1017771928.png)​

* Para acima de 500 **km**: 501 (**Km** informado) x 5,00 (Valor por **KM**)= 2505 reais.

![](https://totvssuporte.zendesk.com/attachments/token/o195u3rE7FWHnQowWrsXmRk9X/?name=inline-410259138.png)

**Saiba mais**  
Para preenchimento do campo **DTC\_KM** de forma automática, verifique os cadastros:

* [Distâncias (TMSA710 - SIGATMS)](https://tdn.totvs.com/pages/viewpage.action?pageId=464949425)
* [Distâncias Por Clientes (TMSA711 - SIGATMS)](https://tdn.totvs.com/pages/viewpage.action?pageId=485434153)
