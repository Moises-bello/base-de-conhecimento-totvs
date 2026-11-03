---
article_id: 4415272426647
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 138e51de4008c36bd973067976bc328a8084ad6410c2a20fdc15df676212a2c3
fetched_at: '2026-06-28T22:38:55.741993+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA106 - Pontos de
  Entrada da rotina Pré-Requisição
type: support-article
updated_at: '2026-03-06T15:40:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415272426647-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA106-Pontos-de-Entrada-da-rotina-Pr%C3%A9-Requisi%C3%A7%C3%A3o
---

A rotina MATA106 do TOTVS Protheus não possui EXECAUTO, apenas pontos de entrada que permitem customizações em diversas etapas, como validações de pré-requisição, geração de pré-requisição, adição de botões no menu, inserção de filtros, manipulação de tabelas e processamento específico do usuário. Cada ponto de entrada atende funções específicas no fluxo de solicitação e pré-requisição.

**Dúvida**  
Quais são os Pontos de Entradas da rotina MATA106?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

|  |
| --- |
| **A rotina MATA106 não dispõe de EXECAUTO, apenas Pontos de Entrada** |

Segue abaixo a relação dos Pontos de Entrada disponíveis na rotina MATA106:

|  |  |  |
| --- | --- | --- |
| [**MA106VLG**](https://tdn.totvs.com/display/public/PROT/PEST07673_MA106VLG_GERAR_PRE_REQUISICAO) | Validações de Pré-Requisição | O ponto de entrada verifica as validações internas de bloqueio orçamentário antes de Gerar a Pré-Requisição. |
| [**MA106GER**](https://tdn.totvs.com/pages/releaseview.action?pageId=6085342) | Geração de Pré-Requisição | Validação de processamento das requisições |
| [**MTA106MNU**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087793) | Adiciona botões ao menu principal | Este Ponto de Entrada é utilizado para adicionar itens no menu principal da rotina |
| [**MT106QRY**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087706) | Insere filtro na Query para Solicitações ao Armazém | Deve ser utilizado para inserir um filtro na query para os Solicitações ao Armazém |
| [**MT106GRV**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087919) | Antes da Pré-Requisição | O ponto de entrada MT106GRV é chamado antes de ser gerada a pre-requisição e antes de baixar o saldo no estoque |
| [**MA106SCQ**](https://tdn.totvs.com/pages/releaseview.action?pageId=6085343) | Conversão de solicitação ao armazém | Função responsável por realizar a conversão de uma solicitação ao armazém em uma Pré-Requisição - Tabela SCQ |
| [**MASAVLSC**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087870) | Geração de Solicitação de Compra | Este ponto de entrada foi criado na função MaSAPreReq para permitir que não seja gerada a solicitação de compras, quando gerada a Pré-Requisição da solicitação ao armazém |
| [**MASAVLOP**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087652) | Permite a geração de Ordem de Produção por Pré-Requisição | Ponto de entrada criado na função MaSAPreReq para permitir a geração de Ordem de Produção pela geração da Pré-Requisição através de customização |
| [**MT106SC1**](https://tdn.totvs.com/display/public/PROT/PEST07697+-+MT106SC1+-+Manipular+a+tabelas+na+SA) | Manipular a tabelas na SA | O ponto de entrada é utilizado após gravar a Solicitação de Compra, para manipular as informações nas tabelas: SC1, SC7, CND, SW1 |
| [**MT106PRE**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087705) | Processamento específico do usuário | Ponto de entrada executado no final da função MaSAPreReq(rotina de conversão de uma Solicitação ao Almoxarifado para uma Pré-Requisição), após todas as gerações de Pré-Requisições (e autorizações de entrega, caso sejam produtos com contratos de parceria - B1\_CONTRAT='S'). Pode ser utilizado para algum processamento específico do usuário |

**Saiba mais:**

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA105 - Pontos de Entrada da rotina Solicitação ao Armazém*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414520997271-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA105-Pontos-de-Entrada-da-rotina-Solicita%C3%A7%C3%A3o-ao-Armaz%C3%A9m?source=search)

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
