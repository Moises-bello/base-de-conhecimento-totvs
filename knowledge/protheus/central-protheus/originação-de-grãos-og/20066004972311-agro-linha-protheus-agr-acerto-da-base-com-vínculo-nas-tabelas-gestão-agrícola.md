---
article_id: 20066004972311
category: Originação de Grãos (OG)
content_hash: e7836827914345d486f6d3512c8994307cb05ac5a1cf3ec8d53e9af50045943b
fetched_at: '2026-06-28T22:45:36.925212+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Acerto da base com vínculo nas tabelas Gestão
  Agrícola
type: support-article
updated_at: '2025-06-24T19:59:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20066004972311-Agro-Linha-Protheus-AGR-Acerto-da-base-com-v%C3%ADnculo-nas-tabelas-Gest%C3%A3o-Agr%C3%ADcola
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20066004941463) Tempo aproximado para leitura: **00:01:30 min****Ocorrência**  
No módulo **Comercialização (Linha Protheus) - Originação de Grãos (OG)**, ao realizar o processo para executar a atualização do dicionário de dados criando as tabelas de extensão é apresentada a ocorrência **Acerto da base com vínculo nas tabelas Gestão Agrícola**.  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Causa**Esse incidente ocorre, pois é necessário realizar o processo para executar a atualização do dicionário de dados criando as tabelas de extensão.  
  
**Solução**  
Para solucionar essa ocorrência, é necessário executar as rotinas **OGAX002 - Acerto Vinculo Titulo Receber** e **OGAX001 - Acerto Vinculo Pedido Nota**, localizadas no menu do módulo **67**- **Gestão de Agronegócio**, em **Miscelânea**, **Gestão Agrícola**, **Acerto de Base**.  
Para iniciar o processo de atualização e criação das tabelas **N8H** e **N8I** basta executar as rotinas conforme necessidade.

![ACERT.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/20065986002455)![ACERT_2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/20066004944407)

Ao executar a rotina o programa irá buscar todos os registros de romaneio cuja situação estiver diferente de cancelados, e irá gerar o vínculo das tabelas relacionadas quando este ainda não existir. A rotina poderá ser executada mais de uma vez, entretanto, somente irá gerar os registros quando algum dos relacionamentos estiver faltando.  
  
**Importante**Para os novos romaneios, gerados a partir da **versão 12.1.21**, os vínculos para as tabelas relacionadas serão criados por padrão, não sendo necessário executar a rotina.  
Relação de tabelas  
As seguintes tabelas serão gravadas ao executar o processamento da rotina **Registros de Relacionamentos para as Tabelas -** **OGX175**  
**Vinculo docto de Saída SIGAAGR - N8J** Relaciona os registros do pedido:  **Pedido de Venda -** **SC5**  
**Vinculo Itens Ped Vend SIGAAGR - N8I** Relaciona os registros de itens do pedido: **Itens dos Pedidos de Venda -** **SC6**  
**Vinculo Pedido Venda SIGAAGR - N8H** Relaciona os registros da **Nota Fiscal -** **NF**: **Cabeçalho das NF se Saída -** **SF2**  
**Vinc.Intens Doc.Saída SIGAAGR - N8K** Relaciona os registros do item da **NF**: **Itens de Venda da NF -** **SD2**  
**Vinculo Titsa Receber SIGAAGR  - N8L** Relaciona os registros de títulos: **Conta a Receber -** **SE1.**
