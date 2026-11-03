---
article_id: 4407757428247
category: SIGAEST - LEGAIS
content_hash: 00debc2a386b550834923c92da3f736af4a780e413be205dd1bd2d9883418aaa
fetched_at: '2026-06-28T22:38:51.617178+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Bloco K - Registro
  K275 - Conceito e Informações
type: support-article
updated_at: '2021-09-03T14:59:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407757428247-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Bloco-K-Registro-K275-Conceito-e-Informa%C3%A7%C3%B5es
---

**Dúvida**O que é o registro K275 do SPED Fiscal e como ele é montado?  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

O registro K275 do SPED Fiscal tem o objetivo de escriturar correção de apontamento de período de apuração anterior, relativo ao Registro-filho, por tipo de Registro e por período de apuração em que o apontamento será corrigido. Em suma, ele aponta negativamente ou positivamente o estoque dos insumos envolvidos nos registros K215, K220, K235, K255 e K265.

Por se tratar de um registro filho do K270, recomendamos fortemente a leitura do artigo do Registro K270 para correta compreensão da montagem deste registro filho.

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Bloco K - Processo para geração do registro K270](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022630231)

**Exemplo**

Existem situações onde o cliente possui uma Ordem de Produção que é trabalhada durante vários períodos (meses), caso em um período seja realizada uma requisição para produção. (Exemplo: 100 unidades), e no período seguinte exista apenas uma devolução (Exemplo: 30 unidades), o registro K235 apresentará uma quantidade negativa devido a composição "requisições - devoluções". Essas devoluções são automaticamente registradas nesse registro (K275).

Observação para Tratamento do registro K270: Caso ocorra correção de apontamento apenas do **registro-filho (K275)**, este registro será informado com os campos de quantidade zerados.

OBS: Ao utilizar o ponto de entrada [PEST07692 - MT240DVL - Validação das Informações do Movimento](https://tdn.totvs.com/pages/viewpage.action?pageId=455807265) para permitir uma devolução com OP maior que o saldo requisitado, pode afetar diretamente na geração do registro. Para clientes que estiverem utilizando este ponto de entrada o comportamento do exemplo da Ordem de Produção acima muda, será retirado o Insumo negativo deixando a tratativa de correção por conta do ponto de entrada desenvolvido.

**Posso definir quais movimentos e estornos devem ser considerados na composição do Registro K270 e K275?**

Lembrando que os demais blocos devido ao fato de as rotinas de movimentação de estoque do Protheus não possuírem funcionalidade de alteração ou correção, este registro não é gerado automaticamente para o **Bloco K**. Caso o cliente possua um processo automatizado/customizado ou deseje informar manualmente este registro, disponibilizamos o ponto de entrada **[REGK27X](https://tdn.totvs.com/display/public/PROT/PEST07669_REGK27X_Registros_K270_K275_Bloco_K),** onde é possível realizar a gravação do arquivo de trabalho do Registro K275 durante o processamento do **Bloco K**. Devido ao ponto de entrada dar acesso direto ao arquivo de trabalho, não são realizadas validações das informações gravadas.

No arquivo temporário do Registro K275 existe o campo **COD\_OP\_OS**, que não faz parte do registro, onde deve ser informado o mesmo código gravado no campo **COD\_OP\_OS** do Registro K270 pai.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Tipo** | **Tam** | **Dec** | **Obrig** |
| 01 | REG | Texto fixo contendo "K275" | C | 4 | - | O |
| 02 | COD\_ITEM | Código da mercadoria (campo 02 do Registro 0200) | C | 60 | - | O |
| 03 | QTD\_COR\_POS | Quantidade de correção positiva de apontamento ocorrido em período de apuração anterior | N | - | 6 | OC |
| 04 | QTD\_COR\_NEG | Quantidade de correção negativa de apontamento ocorrido em período de apuração anterior | N | - | 6 | OC |
| 05 | COD\_INS\_SUBST | Código do insumo que foi substituído, caso ocorra a substituição, relativo aos Registros K235/K255 | C | 60 | - | OC |

**Saiba mais:**

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Bloco K - Processo para geração do registro K270](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022630231)*

*[Clique aqui e veja mais artigos sobre arquivos e relatórios Legais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)*
