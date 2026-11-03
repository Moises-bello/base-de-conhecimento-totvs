---
article_id: 4402655402391
category: MDFe - Manifesto de Carga
content_hash: 40257fb97ca75d7ab1e8f1af02925edfdb39f23828cb2a77dcfcc3982f572eb3
fetched_at: '2026-06-28T22:40:08.121730+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFE -  578 Rejeição
  : Informações dos tomadores é obrigatória para esta operação'
type: support-article
updated_at: '2025-06-17T17:28:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402655402391-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDFE-578-Rejei%C3%A7%C3%A3o-Informa%C3%A7%C3%B5es-dos-tomadores-%C3%A9-obrigat%C3%B3ria-para-esta-opera%C3%A7%C3%A3o
---

**Dúvida**

Como solucionar a rejeição abaixo:

578 Rejeição : Informações dos tomadores é obrigatória para esta operação?

**Ambiente**Cross Segmentos - Backoffice Protheus - Todas as versões  
  
**Solução**1- Se necessário gerar **Proprietário** e com **CPF** deve gerar  **TAC = 2, no cadastro de Fornecedor campo "Tipo" A2\_TIPO**precisa ser  **F - Físico**

**![TAC_MANUAL.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/32683023868951)**

**![20210614_150651.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32683023873047)**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32683023874071)**

2 - Deve gerar o **Responsável pelo pagamento do Vale-pedágio ou Ciot:**

3 - Para gerar informação do **Ciot realizar a configuração do link abaixo:**

*[Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045209473)*

4- Para gerar a informação referente ao **Responsável pelo pagamento realize** **atualização abaixo:**

[Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402644962967)

Neste capitulo iremos mostrar como é realizado o preenchimento dos campos de Vale Pedágio na rotina de MDF-e (SPEDMDFE) do módulo Faturamento do sistema ERP Protheus.

No módulo Faturamento (SIGAFAT), acessar "Atualizações / NF-e e NFS-e / MDF-e (SPEDMDFE). Informar os filtros e em seguida clicar na operação desejada.

Na aba **Vale-Pedágio** informar os seguintes campos:

* **CNPJ Empresa Fornecedora do Vale-Pedágio:** Informar o CNPJ da empresa fornecedora do vale-pedágio homologada na ANTT.
* **CNPJ/CPF Responsável Pagamento:** Informar o CNPJ ou o CPF do responsável pelo pagamento do vale-pedágio.
* **Número Comprovante de Compra:**Informar o número de ordem do comprovante de compra do Vale-Pedágio fornecido para cada veículo ou combinação veicular, por viagem.
* **Valor do Vale-Pedágio:**Informar o valor do vale-pedágio.
* **Tipo do Vale-Pedágio:**Informar o tipo do vale-pedágio (01 - TAG, 02 - Cupom ou 03 - Cartão).

![](https://tdn.totvs.com/download/attachments/625151508/image2021-6-20_17-8-51.png?version=1&modificationDate=1624219731487&api=v2)

![](https://tdn.totvs.com/download/attachments/625151508/image2021-6-20_17-26-14.png?version=1&modificationDate=1624220774187&api=v2)

Estas informações não são obrigatórias de preenchimento dependendo de sua configuração ou obrigações junto a ANTT. Caso seja necessário, poderão ser informados 1 ou mais vale-pedágios para o MDF-e.

Após informar os campos basta clicar em **Salvar** para gravar as informações do vale-pedágio no MDF-e.

A categoria de combinação Veicular (TAG: **categCombVeic** do XML), é preenchida automaticamente pelo sistema com base na quantidade de eixos informado presente no cadastro do veículo, onde será respeitada a seguinte tabela:

| Numero de Eixos do veículo | Conteúdo da TAG **categCombVeic**do XML |
| --- | --- |
| 2 | 02 |
| 3 | 04 |
| 4 | 06 |
| 5 | 07 |
| 6 | 08 |
| 7 | 10 |
| 8 | 11 |
| 9 | 12 |
| 10 | 13 |
| Maior que 10 | 14 |

Os vale-pedágios são apresentados em DAMDFE após autorização.

![](https://tdn.totvs.com/download/attachments/625151508/image2021-6-21_12-32-17.png?version=1&modificationDate=1624289537543&api=v2)

Ou

1- Caso não tenha proprietário retire do cadastro **de veículo o conteúdo do campo Proprietário  "DA3\_CODFOR"**

![DA3_CODFOR.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4402655635351)

2- Após isso, exclua o **MDFe e gere novamente.**

* **Validação da Sefaz:**

![rejei__o_578.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4402649951383)
