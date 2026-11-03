---
article_id: 28502879763223
category: Originação de Grãos (OG)
content_hash: cfdc1a1115880b0aa15447a4928b0ed06267c094b7655d918646b9ae8ac62242
fetched_at: '2026-06-28T22:45:36.950946+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Agrupamento dos Campos na Tela de Contratos no
  SIGAAGR
type: support-article
updated_at: '2025-06-25T19:09:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28502879763223-Agro-Linha-Protheus-AGR-Agrupamento-dos-Campos-na-Tela-de-Contratos-no-SIGAAGR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28502879740695) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como é realizado o **Agrupamento dos Campos na Tela de Contratos no SIGAAGR**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**Para o **Contrato de Armazenagem em Terceiro -** **OGA270** não há um agrupamento de campos definido dentro da rotina, assim sendo, a exibição dos campos em tela ocorrerá conforme definição do dicionário. Contudo, nas demais rotinas **Armazenagem de Terceiro -** **OGA260**,

Contrato de Compra **OGA280**, Contrato de Venda **OGA290**, há agrupamento  de campos definido diretamente na rotina **código fonte** ao qual irá ignorar a ordenação do dicionário, desta forma, a ordenação dos campos será apresentada em tela conforme definido em cada rotina.

Para atender a situação em que deseja utilizar ordenação dos campos em tela conforme dicionário, deverá ser criado via **Configurador** agrupamento dos campos na tabela **NJR** e vincular os campos nestes agrupamentos conforme modelo abaixo.

A partir do momento que houver agrupamento com código **GRA** definido na tabela **NJR** a rotina assumira que será utilizada agrupamento do dicionário.
