---
article_id: 27794245695895
category: Originação de Grãos (OG)
content_hash: 94e080a526b8c7e344796e4c06f31beb507128f7a61235e1d6b81cb9815f492c
fetched_at: '2026-06-28T22:45:45.257294+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Visão Geral - Configuração/Parâmetros da Rotina
  numa Composição de Preço OGA420
type: support-article
updated_at: '2025-05-19T19:15:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27794245695895-Agro-Linha-Protheus-AGR-Vis%C3%A3o-Geral-Configura%C3%A7%C3%A3o-Par%C3%A2metros-da-Rotina-numa-Composi%C3%A7%C3%A3o-de-Pre%C3%A7o-OGA420
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27794198351127) Tempo aproximado para leitura: **00:01:20 min****Dúvida**Como é realizada uma **Configuração/Parâmetros da Rotina numa Composição de Preço OGA420**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

**Visão Geral:**A rotina de composição de preço permite informar um valor para os componentes que montam o preço do produto no contrato, seja ele de venda ou de compra.  
Ao informar os preços é possível visualizar as conversões de unidades de preço definidas para componente em relação a unidade de preço do contrato, além de conferir aplicação das cotações de moedas, visto que um componente pode ser precificado em moeda estrangeira.  
Informando os valores para os componentes o sistema calcula  automaticamente o valor unitário e total para o contrato. No entanto, assume como oficial para o contrato o valor digitado no campo **Preço Proposto**. No campo **Saldo de Margem** é apresentada a diferença entre o **Calculado e Proposto** para que o usuário possa fazer uma análise. É possível também definir uma margem fixa, onde o Sistema calcula e atribui automaticamente no **Preço Calculado**.  
Esta rotina não está disponível no menu e o acesso ocorre por meio dos programas de c**ontrato de venda**, **contrato de compra**, **gestor de entidade ou na rotina**.  
A sua utilização também está condiciada ao modelo clássico de comercialização.

**Configuração/Parâmetros da Rotina:****Principais parâmetros:**

|  |  |  |
| --- | --- | --- |
| **Parâmetro** | **Descrição** | **Conteúdo padrão** |
| [MV\_SIMB](https://tdn.totvs.com/pages/viewpage.action?pageId=351372556) | Símbolo utilizado pela moeda 1 do Sistema | R$ |

**Pré-requisitos:**

* Possuir os componentes devidamente cadastrados **OGA410**;
* Índices de mercado cadastrados;
* Cotação de índice informada;
* Cotações cadastradas para o moeda estrangeira, caso algum componente tenha seu valor em outra moeda;
