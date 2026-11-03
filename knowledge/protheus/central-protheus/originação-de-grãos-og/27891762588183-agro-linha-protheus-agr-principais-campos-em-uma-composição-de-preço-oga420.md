---
article_id: 27891762588183
category: Originação de Grãos (OG)
content_hash: bca3571ab8dc9836a22e2b343e5c912c26d5ba055e46965df786371bdf1d4b7b
fetched_at: '2026-06-28T22:45:43.271509+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Principais Campos em uma Composição de Preço
  OGA420
type: support-article
updated_at: '2024-11-19T13:19:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27891762588183-Agro-Linha-Protheus-AGR-Principais-Campos-em-uma-Composi%C3%A7%C3%A3o-de-Pre%C3%A7o-OGA420
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27891762567959) Tempo aproximado para leitura: **00:01:50 min** **Dúvida**  
Como são os **Principais Campos** **em uma Composição de Preço OGA420**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**

**Principais Campos:**Os principais campos da tela de composição de preço são descritos abaixo.  
Na tabela de componentes as principais colunas são:

| **Campo** | **Descrição** |
| --- | --- |
| **Componente** | Exibe a descrição do componente |
| **Moeda** | Exibe a moeda do componente que foi definida no cadastro de componente. |
| **Cotação** | Permite informar a Cotação da moeda para conversão caso a moeda do componente seja diferente do contrato. Caso tenha cotação para o dia corrente, a cotação é carregada automaticamente. |
| **UM** | Exibe a unidade de medida do componente que foi definida no cadastro de componente. |
| **Vlr. Índice** | Exibe o valor do índice caso exista cotação e índice vinculado ao componente. |
| **Vlr. Compon** | Permite informar o valor do componente. |
| **Moeda**/**UM** | A descrição desse campo é exibida dinamicamente, onde **M*****oeda** é a*moeda do contrato e***UM***é a unidade de medida de preço do contrato.  Exemplo: R$ / SC. |
| **Moeda**/**UM** | A descrição desse campo é exibida dinamicamente, onde ***Moeda** é*a moeda do contrato e***UM***é a unidade de medida do produto.  Exemplo: R$ / KG. |

Na parte inferior direita é exibido o mesmo título para campos com conteúdos diferentes.  Isso ocorre pois são exibidos os valores na **moeda do contrato / unidade de preço do contrato**e outra na  **moeda do contrato / unidade do produto***.*A seguir, exemplos considerando que unidade de medida do produto é KG (quilos):

A - Se o contrato for **moeda (2 - Dólar)** e a **unidade de preço** **(SC)** as colunas exibidas serão: US$/SC e US$/KG.

B - Se o contrato for **moeda (1 - Real)** e a **unidade de preço** **(SC)** as colunas exibidas serão: R$/SC e R$/KG.

| Campo | Descrição |
| --- | --- |
| Preço calculado | Exibe o preço calculado com base nos valores informados para os componentes. |
| Valor da Margem | Exibirá o valor da margem calculado quando existirem componente configurado como Margem. Ver informações no tópico [05. Componente de Margem de Preço](https://tdn.totvs.com/pages/releaseview.action?pageId=547257907#Composi%C3%A7%C3%A3odePre%C3%A7o(OGA420)-margempreco). |
| Preço proposto | Permite informar o preço proposto para o contrato. Este será o valor considerado como valor unitário e base para cálculo do valor total. |
| Saldo da Margem | Diferença entre o valor calculado pelo Sistema e o preço proposto. |
| Total Calculado | Valor total calculado na moeda do contrato e unidade de medida do produto. |
| Total Proposto | Valor total proposto na moeda do contrato e unidade de medida do produto. |

As conversões de unidades de medidas diferentes entre componente, produto e preço do contrato são realizadas por meio das informações do cadastro de [Unidade de Medidas.](https://tdn.totvs.com/pages/viewpage.action?pageId=493634436)

Este programa também está disponível no menu do **SIGAAGR**. Acesse,  **Gestão de Agronegócio (SIGAAGR)** acesse **Atualizações > Cadastros Gerais > Unidades Medidas***.*
