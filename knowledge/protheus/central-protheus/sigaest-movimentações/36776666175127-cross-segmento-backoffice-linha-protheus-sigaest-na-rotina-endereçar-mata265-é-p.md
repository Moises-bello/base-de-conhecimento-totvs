---
article_id: 36776666175127
category: SIGAEST - MOVIMENTAÇÕES
content_hash: e275deb3c8a64487add1087d81041606532836ef3ba719d1a62615d546107a63
fetched_at: '2026-06-28T22:38:57.215651+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Na rotina Endereçar
  (MATA265), é permitido o endereçamento de produtos com o campo DB_LOCALIZ (Endereço)
  vazio?
type: support-article
updated_at: '2025-12-04T16:15:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36776666175127-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Na-rotina-Endere%C3%A7ar-MATA265-%C3%A9-permitido-o-endere%C3%A7amento-de-produtos-com-o-campo-DB-LOCALIZ-Endere%C3%A7o-vazio
---

No Protheus, o controle de produtos pode ser feito por Número de Série ou Endereço de Armazenamento, sendo obrigatório o preenchimento de um dos dois campos. O sistema permite o endereçamento com o campo DB\_LOCALIZ vazio se o Número de Série estiver preenchido, oferecendo flexibilidade para diferentes processos e garantindo uma gestão eficiente do estoque.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36776666168343) Tempo aproximado para leitura: **02:00:00 min**  
  
**Dúvida**  
Na rotina Endereçar (MATA265), é permitido o endereçamento de produtos com o campo DB\_LOCALIZ (Endereço) vazio, mesmo o campo sendo obrigatório.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) -Estoque/Custos - Todas as versões.  
  
**Solução**

**Controle de Produtos no Protheus: Número de Série vs. Endereço**

No sistema Protheus, a gestão eficiente de estoque é fundamental para a operação bem-sucedida de qualquer empresa. Para garantir uma administração precisa dos produtos, o Protheus oferece duas abordagens distintas para o endereçamento e rastreamento de itens em estoque: **Número de Série** e **Endereço de Armazenamento (A obrigatoriedade trata-se de um, ou de outro)**.

#### **Número de Série**

O **Número de Série** é uma identificação única atribuída a cada unidade de produto. Esse método de controle permite um rastreamento detalhado e individualizado de cada item, oferecendo vantagens como:

* **Rastreamento Detalhado**: Cada unidade é identificada de forma exclusiva, facilitando a gestão de garantias, manutenção e histórico de vida do produto.
* **Controle Preciso**: Ideal para produtos onde a individualidade é crucial, como equipamentos de alto valor ou com regulamentações específicas.

#### **Endereço de Armazenamento**

Por outro lado, o **Endereço de Armazenamento** refere-se à localização física onde o produto é armazenado dentro do estoque. Esse método oferece:

* **Organização do Estoque**: Permite a organização dos produtos em diferentes locais dentro do armazém, facilitando a logística e o gerenciamento de espaço.
* **Eficiência Operacional**: Ideal para ambientes com grandes volumes de produtos, onde o controle físico das localizações pode melhorar a eficiência das operações de entrada e saída.

#### **Flexibilidade no Controle**

No Protheus, você pode optar por usar **Número de Série** ou **Endereço de Armazenamento** para o controle dos produtos, conforme as necessidades específicas da sua operação. Em situações onde o produto é endereçado através do número de série, o sistema pode permitir o registro mesmo que o campo de **Endereço de Armazenamento** não esteja preenchido. Essa flexibilidade é projetada para:

* **Atender a Diferentes Processos**: Permitir que empresas escolham o método mais adequado de acordo com seus processos e requisitos operacionais.
* **Facilitar a Operação**: Garantir que o sistema se adapte a diferentes situações sem comprometer a precisão do controle de estoque.

Ao utilizar o número de série ou o endereço de armazenamento, o Protheus proporciona uma gestão de produtos eficiente e adaptável, alinhada às necessidades e à dinâmica operacional da sua empresa.

**Exemplo (obrigatoriedade):**

Preenchimento apenas do Endereço ou Número de Série. Nota-se abaixo a regra de obrigatoriedade, sendo ela, Endereço ou Número de Série.

![](https://tdn.totvs.com/download/attachments/864345603/num%20serie%20ou%20endere%C3%A7o.png?version=1&modificationDate=1724678769843&api=v2)

**Exemplo, sem Endereço ou Número de Série:**

![](https://tdn.totvs.com/download/attachments/864345603/erro%20caso%20nenhum.png?version=1&modificationDate=1724678769770&api=v2)

Então, apenas reforçando, apesar do campo se tratar como obrigatório, pode haver regras envolvendo outros campos, como no caso do Endereço e Número de Série!

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
