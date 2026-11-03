---
article_id: 22540041473175
category: Originação de Grãos (OG)
content_hash: 8daf0a1dc9b6bf43892de9a1d9702872a9d056cacbde313cdc7a8e84eaa6f1bd
fetched_at: '2026-06-28T22:45:37.779323+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Configuração/Parâmetros da Rotina na Nova Comercialização
type: support-article
updated_at: '2025-06-24T11:35:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22540041473175-Agro-Linha-Protheus-AGR-Configura%C3%A7%C3%A3o-Par%C3%A2metros-da-Rotina-na-Nova-Comercializa%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22540048019095) Tempo aproximado para leitura: **00:01:15 min**

**Dúvida**Como funciona a estrutura de **Configuração/Parâmetros da Rotina na Nova Comercialização**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**  
Para solucionar essa dúvida, realize os pré-requisitos:

* Parâmetros **MV\_AGRO002** habilitados. O parâmetro **MV\_AGRO040** somente é necessário caso deseja incluir o contrato de venda ou compra diretamente, sem utilizar o **Registro de Negócio**;
* Possuir os componentes devidamente cadastrados **OGA410**;
* Necessário ter definido um componente do tipo "**Resultado**" devidamente cadastrados **OGA410**. Este tipo de componente será usado para compor o cálculo.
* Necessário definir a configuração de componentes do componente do tipo "**Resultado**", vinculando os componentes que irão compor o cálculo **OGA490**;
* Cotações cadastradas para a **moeda estrangeira**;
* Bolsa de referência cadastrada;
* Índices de mercado cadastrados;
* Cotação de índice informada.

**Principais parâmetros:**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parâmetro** | **Descrição** | **Conteúdo padrão** | **Conteúdo exigido para esta rotina** |
| [MV\_AGRO002](https://tdn.totvs.com/pages/viewpage.action?pageId=370616326) | Utiliza novo modelo de comercialização. | .F. | .T. |
| [MV\_AGRO209](https://tdn.totvs.com/pages/viewpage.action?pageId=544182058) | Indica se deseja gerar notas fiscais diferentes quando encontra mais de um preço | .F. | (opcional) |
| [MV\_AGRO040](https://tdn.totvs.com/pages/viewpage.action?pageId=519202897) | Retira a obrigatoriedade do Registro de Negócio | .F. | (opcional) |
| [MV\_AGRO003](https://tdn.totvs.com/pages/viewpage.action?pageId=370618087) | Necessidade de Aprovação de negócios | <vazio> | (opcional) |
| [MV\_AGRO006](https://tdn.totvs.com/pages/viewpage.action?pageId=370618885) | Aprovação de banking no cadastro de novos negócios | <vazio> | (opcional) |
