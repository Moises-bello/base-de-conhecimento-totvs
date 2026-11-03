---
article_id: 26905753460247
category: NFe - Nota Fiscal Eletrônica
content_hash: f94ed24a5e429c70cc595fc36a625f9544bd7f8e490b14299ba1e7322c21d0b0
fetched_at: '2026-06-28T22:40:00.118180+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Implementação dos
  ajustes SINIEF 13/2024 e 14/2024
type: support-article
updated_at: '2026-05-21T14:54:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26905753460247-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Implementa%C3%A7%C3%A3o-dos-ajustes-SINIEF-13-2024-e-14-2024
---

**Dúvida**  
Como adequar o ambiente aos ajustes SINIEF Nºs 13 e 14.

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  Cross Segmentos - Protheus

**Solução**

Para gerar a nota de devolução com a tag finnfe 1, use um CFOP genérico como 1949, 2649, 5949 ou 6949 e insira no parâmetro MV\_DEVCFOP.

Referente a mensagem *"Procedimento autorizado pelo Ajuste SINIEF 13/24 ou 14/24"* pode ser inserida pelo campo C5\_MENNOTA ou via formula:

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar mensagem em informações complementares (TAG infcpl e infadfisco) do Danfe utilizando fórmula](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026944871--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-mensagem-em-informa%C3%A7%C3%B5es-complementares-TAG-infcpl-e-infadfisco-do-Danfe-utilizando-f%C3%B3rmula#:~:text=Solu%C3%A7%C3%A3o.%20Para%20determina%20o%20tratamento%20do%20campo%20F4_FORMULA%20e%20A1_MENSAGE)  
[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar informações na TAG infCpl ou infAdFisco no XML e no DANFE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024950773)

No grupo "prod. - Detalhamento de Produtos e Serviços" as mesmas informações da NF-e original  
de saída. Essa informação vem da descrição do produto, campo B1\_DESC.  
  
No campo *"natOp - Natureza da Operação", o texto "Entrada simbólica - Ajuste SINIEF 14/24".* Para levar essa informação precisa usar esse texto no campo F4\_TEXTO da TES usada na nota.

Para gerar a tag refnfe da nota de origem, a nota de venda deve estar no sistema. Ao criar a devolução simbólica, o tipo deve ser "devolução" e é preciso preencher os campos NF Ori, Série Ori e Item NF Ori na linha do item.

Posteriormente fara uma nova nota de venda, e nessa nova nota precisa referenciar a nota de devolução simbólica e a primeira nota de venda.

Caso precise gerar mais de uma nota referenciada na tag refnfe é necessário criar o parâmetro MV\_VINCCDD:

<https://tdn.totvs.com/pages/releaseview.action?pageId=728644188>

Aplicar as atualizações abaixo no ambiente do Protheus (Aplicação no RPO do Protheus):

12.1.2410 <https://suporte.totvs.com/portal/p/10098/download#detail/1171486>

12.1.2510 <https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1224039>

RDMAKE:

<https://suporte.totvs.com/portal/p/10098/download#detail/1152113>

Após emitir o documento, acesse o módulo Livros Fiscais (09) para referenciá-lo na rotina: **Livros fiscais > Atualizações > Movimentos > Nota fiscal manual de saída**, antes da transmissão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26905742590615)

Selecione a nota no browser e clique em **Outras ações > Complementos**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26905742593303)

Selecione a opção **Documentos Fiscais:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26905753452183)

Preencha os dados da nota de Origem e salve:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26905753454103)

Mais informações: <https://tdn.totvs.com/pages/releaseview.action?pageId=870404095>
