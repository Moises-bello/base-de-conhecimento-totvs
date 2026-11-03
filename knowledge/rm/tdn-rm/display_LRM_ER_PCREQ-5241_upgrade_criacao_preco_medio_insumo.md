---
content_hash: c5607a924cdb5c34b8d992637c0ce84fc35d66a14732de93d5d567ed5aa3d6b7
fetched_at: '2026-06-29T00:06:11.145858+00:00'
page_id: '203766897'
product: rm
source: tdn-rm
title: ER_PCREQ-5241_upgrade_criacao_preco_medio_insumo
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-5241_upgrade_criacao_preco_medio_insumo
version: 38
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOTVS Gestão de Obras e Projetos |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | R\_C&P\_TOP008 | **IRM1** | PCREQ-5240 |
| **Requisito1** | PCREQ-5241 | **Subtarefa1** | PDR\_CP\_TOP008-38 |
| **Chamado2** | - | | |
| **Release de Entrega Planejada** | 12.1.8 | **Réplica** | - |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** |  | | |

## 

## 

## Objetivo

Gerar o preço médio de insumo(s) a partir de um intervalo de datas.

## Definição da Regra de Negócio

 

* Localização e acesso ao processo de Criação de Preço Médio de Insumos;
  1. Na visão geral de insumos, devem ser selecionados o(s) insumo(s) (local e/ou global) que receberão o preço médio.
     1. Se não houver seleção de insumos, por padrão será sugerido todos os insumos.
  2. O processo pode ser acessado também através da edição de insumos.
* Regra do processo de Criação de Preço Médio de Insumos:
  1. 'Data de Atualização Inicial' e 'Data de Atualização Final':
     1. O processo irá criar o preço médio a partir dos preços que forem encontrados dentro do intervalo das datas informadas;
        1. A data de seleção dos preços, é o campo 'Data Atualização' do cadastro de preço de insumos;
     2. O preço médio será igual ao somatório dos preços dentro do intervalo informado / quantidade dos preços dentro do intervalo informado;
        1. Para cada insumo, o processo irá selecionar os respectivos preços dentro do intervalo de datas e criar um preço médio;
  2. Ativar Preço?
     1. Se o processo for executado com esta opção marcada, o preço médio deve ser criado como ativo,   
        caso contrário, o preço médio deve ser criado como inativo;
  3. A descrição do preço médio criado obedecerá o layout abaixo;
     1. Preço Médio em (Data Atual) do período de (Data de Atualização Inicial) a (Data de Atualização Final);  
        1. Ex.: Preço Médio em 08/10/15 do período de 08/10/14 a 08/10/15;
     2. Se já houver um preço com a mesma descrição, o processo irá atualizar o valor do preço, e o seu preço não será considerado no cálculo;
  4. O processo irá criar o preço médio tanto para insumos locais e quanto para insumos globais.
* A chamada do processo do Delphi em opções, deixará de existir e será gerada uma mensagem informativa, conforme protótipo 02.

## 

## Protótipo de Tela

**Protótipo 01 - Criação de Preço Médio de Insumo**

****Protótipo 02 - Mensagem informativa Delphi****

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
