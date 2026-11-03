---
article_id: 29254709846807
category: Originação de Grãos (OG)
content_hash: 44ade95eed1c50055d462b946e5738de809d7ec46fe5378d1cb84c020b1c1156
fetched_at: '2026-06-28T22:45:44.825536+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Romaneio de Saída na Gestão Agroindústria - Manutenção
type: support-article
updated_at: '2025-06-24T14:38:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29254709846807-Agro-Linha-Protheus-AGR-Romaneio-de-Sa%C3%ADda-na-Gest%C3%A3o-Agroind%C3%BAstria-Manuten%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29254720226071) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como cadastrar um Romaneio de Saída na Gestão Agroindústria - Manutenção?  
  
**Ambiente**TOTVS Agro – TOTVS Agro – Comercialização (Linha Protheus) - Originação de Grãos (OG) – Versão 12  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:

**1.** Veja na tabela os **Dados Gerais**;

| Linha de Produto: | Microsiga Protheus |
| --- | --- |

| Segmento: | Agroindústria |
| Módulo: | SIGAAGR |
| Função: | AGRA750 - Romaneio de Saída |
| Ticket: | 7375354 |
| Requisito/Story/Issue (informe o requisito relacionado) : | DAGROINDUSTRIA-6716 |

**2.** Acesse a **Solução/Requisito**;  
Foi identificado uma lentidão ao realizar a consulta de tickets de pesagem pendentes.

**3.** Verifique a **Solução**.  
Foi refatorada a função responsável pelo filtro de consulta, sendo necessário ajustar o metadados **"SXB"** conforme orientação abaixo.  
**4.** Acesse **Metadados "SXB" - Consultas Padrão** através do **Configurador**;

**5.** Pesquise a consulta padrão "**DX9DXS**";

![DX9DXS.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29254720234519)

**6.** Solicite a edição da consulta;

![DX9DXS 1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29254720240663)

**7.** Navegue até o filtro da consulta e alterar a função **"AGRA750FPS()",** adicionando o operador**"#"**, deixando o filtro com o seguinte conteúdo**"#AGRA750FPS()".**

![DX9DXS 2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29254709810583)
