---
article_id: 29473841475351
category: Originação de Grãos (OG)
content_hash: 1b1ee572cdc06900cdb94ad07b4962084637ab2ffca4913182b7a016d66e14ee
fetched_at: '2026-06-28T22:45:37.786361+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Configuração/Parâmetros da Rotina na Nova Comercialização
  Precificação de Grãos
type: support-article
updated_at: '2025-04-30T15:12:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29473841475351-Agro-Linha-Protheus-AGR-Configura%C3%A7%C3%A3o-Par%C3%A2metros-da-Rotina-na-Nova-Comercializa%C3%A7%C3%A3o-Precifica%C3%A7%C3%A3o-de-Gr%C3%A3os
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29473841455767) Tempo aproximado para leitura: **00:01:20 min** **Dúvida**  
Como funciona uma estrutura **Configuração/Parâmetros da Rotina na Nova Comercialização Precificação de Grãos**?  
  
**Ambiente**TOTVS Agro – TOTVS Agro – Comercialização (Linha Protheus) - Originação de Grãos (OG) – Versão 12  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

**Principais parâmetros**;

|  |  |  |  |
| --- | --- | --- | --- |
| **Parâmetro** | **Descrição** | **Conteúdo padrão** | **Conteúdo exigido para esta rotina** |
| [MV\_AGRO002](https://tdn.totvs.com/pages/viewpage.action?pageId=370616326) | Utiliza novo modelo de comercialização. | .F. | .T. |
| [MV\_AGRO209](https://tdn.totvs.com/pages/viewpage.action?pageId=544182058) | Indica se deseja gerar notas fiscais diferentes quando encontra mais de um preço | .F. | (opcional) |
| [MV\_AGRO040](https://tdn.totvs.com/pages/viewpage.action?pageId=519202897) | Retira a obrigatoriedade do Registro de Negócio | .F. | (opcional) |
| [MV\_AGRO003](https://tdn.totvs.com/pages/viewpage.action?pageId=370618087) | Necessidade de Aprovação de negócios | <vazio> | (opcional) |
| [MV\_AGRO006](https://tdn.totvs.com/pages/viewpage.action?pageId=370618885) | Aprovação de banking no cadastro de novos negócios | <vazio> | (opcional) |

**Pré-requisitos:**

* Parâmetros [MV\_AGRO002](https://tdn.totvs.com/pages/viewpage.action?pageId=370616326)  habilitados. O parâmetro [MV\_AGRO040](https://tdn.totvs.com/pages/viewpage.action?pageId=519202897) somente é necessário caso deseja incluir o contrato de venda ou compra diretamente, sem utilizar o **Registro de Negócio**;
* Possuir os componentes devidamente cadastrados **(OGA410)**;
* Necessário ter definido um componente do tipo **"Resultado"** devidamente cadastrados **(OGA410)**. Este tipo de componente será usado para compor o calculo.
* Necessário definir a configuração de componentes do componente do tipo **"Resultado"**, vinculando os componentes que irão compor o calculo  **(OGA490)**;
* Cotações cadastradas para o moeda estrangeira;
* Bolsa de referência cadastrada;
* Índices de mercado cadastrados;
* Cotação de índice informada.
