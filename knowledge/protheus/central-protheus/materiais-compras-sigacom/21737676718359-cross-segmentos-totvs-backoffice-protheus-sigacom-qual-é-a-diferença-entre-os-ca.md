---
article_id: 21737676718359
category: Materiais - Compras (SIGACOM)
content_hash: 054191fdbf7e4ba5da17c58046b04e4ecdc87ba3893c4404ad50f92179508f96
fetched_at: '2026-06-28T22:41:24.276053+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Qual é a diferença
  entre os campos: A2_ID_FBFN e A2_FABRICA ?'
type: support-article
updated_at: '2024-03-01T16:40:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21737676718359-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-%C3%A9-a-diferen%C3%A7a-entre-os-campos-A2-ID-FBFN-e-A2-FABRICA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21737689514135) Tempo aproximado para leitura: **00:02 min** **Dúvida**Qual é a diferença entre os campos: A2\_ID\_FBFN e A2\_FABRICA ?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - versão 12

**Solução**

No cadastro de Fabricante/Fornecedor "**SA2**", dentro dos módulos de Compras, você pode definir no campo **A2\_ID\_FBFN** o tipo de cadastro que está sendo realizado. Aqui está a explicação dos valores possíveis para o campo **A2\_ID\_FBFN**:

1. **Fabricante**: Indica que o cadastro se refere a um fabricante.
2. **Fornecedor**: Indica que o cadastro se refere a um fornecedor.
3. **Todos**: Indica que o cadastro é válido para ambos, fabricante e fornecedor.
4. **Exportador**: Indica que o cadastro se refere a um exportador.
5. **Beneficiário**: Indica que o cadastro se refere a um beneficiário.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21737676690583)

O campo **A2\_FABRICA** é necessário para informar a função do fornecedor, conforme definido na tabela de consulta F3. Este campo provavelmente contém um código ou valor que indica a função específica do fornecedor, como fabricante, distribuidor, revendedor, etc.

Ao preencher o campo **A2\_FABRICA**, você pode especificar a função do fornecedor de acordo com os códigos ou valores estabelecidos na tabela de consulta F3. Isso permite uma classificação adequada dos fornecedores com base em suas funções específicas dentro do sistema.

***Saiba Mais :***

* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
