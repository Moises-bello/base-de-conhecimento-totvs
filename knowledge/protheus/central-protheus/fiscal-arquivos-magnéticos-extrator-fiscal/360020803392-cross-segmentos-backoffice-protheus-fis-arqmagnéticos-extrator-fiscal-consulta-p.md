---
article_id: 360020803392
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: bfcf7c1c779e09aa39b32b6c1ac7384e6009f7303f011377ab4d81c0d2d3eeb6
fetched_at: '2026-06-28T22:42:07.755735+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Extrator Fiscal
  - Consulta Padrão - "Diretório de Arquivo Destino" Não Cadastrada no SXB
type: support-article
updated_at: '2022-08-18T17:25:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020803392-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Extrator-Fiscal-Consulta-Padr%C3%A3o-Diret%C3%B3rio-de-Arquivo-Destino-N%C3%A3o-Cadastrada-no-SXB
---

**Ocorrência**Ao acionar a opção 'Diretório de Arquivo Destino' no extrator fiscal é apresentado o aviso:

"Esta consulta não está cadastrada no SXB".

**Ambiente**Microsiga Protheus - A partir da versão 12.1.17  
  
**Causa**Esta situação ocorre, pois a sequencia 01 da consulta padrão GTFILE não possui o campo XB\_CONTEM preenchido.   
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o módulo **Configurador**-> **Base de Dados** -> **Dicionário** -> **Base de Dados**;  
2. Posicione o cursor sobre a opção **Consulta Padrão**, localizada no painel a esquerda;  
3. Clique em **Pesquisar**e busque pela consulta **GTFILE**, após clique em**Editar**;  
4. Clique em **Avançar**;  
5. Altere o campo **Tabela** para **SX5 - Tabelas**;   
6. Clique em Finalizar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360017521491/mceclip2.png)
