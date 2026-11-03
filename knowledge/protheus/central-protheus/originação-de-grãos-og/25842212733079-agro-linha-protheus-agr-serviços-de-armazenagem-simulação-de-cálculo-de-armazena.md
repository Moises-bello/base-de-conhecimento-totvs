---
article_id: 25842212733079
category: Originação de Grãos (OG)
content_hash: 1b075b9943c7a219a9ddb2995c496e0475638fa25649e0446260635688e9b850
fetched_at: '2026-06-28T22:45:44.909010+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Serviços de Armazenagem - Simulação de Cálculo
  de Armazenamento
type: support-article
updated_at: '2025-06-21T15:37:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25842212733079-Agro-Linha-Protheus-AGR-Servi%C3%A7os-de-Armazenagem-Simula%C3%A7%C3%A3o-de-C%C3%A1lculo-de-Armazenamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25842234589463) Tempo aproximado para leitura: **00:01:15 min****Dúvida**Como é realizado uma Simulação de Cálculo de Armazenamento em **Serviços de Armazenagem**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**Para realizar a simulação do cálculo de armazenamento é necessário realizar os seguintes passos:

**1.** Acesse: **Armazenagem > Serviços de Armazenagem > Botão Acerto**;

**2.** Selecione os parâmetros que desejam filtrar os registros: **Contrato, Safra, Produto, dados e outros**;

**3.** Selecione a Entidade desejada e acione o botão de **Atualização**.  
  
No botão **Simular** aparecerá a tela abaixo.

![SDAS.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25842234590487)

O campo Contrato o qual deve ser informado que deseja realizar uma simulação. O campo Qtd Retorno é utilizado para selecionar o saldo das notas fiscais de origem, ou seja, a quantidade da nota de entrada que possui saldo em poder de terceiro até esta quantidade.  
  
O Retorno de Dados da simulação é utilizado para gerar conforme a periodicidade informada no cadastro da tarifa até esses dados. O Tipo Controle refere-se ao tipo de romaneio a ser considerado (físico ou simbólico).  
Ao confirmar, você deverá selecionar os movimentos do contrato em conformidade com os parâmetros da tela e gerar o projeto simulado para cobrança da Armazenagem. Obs.: Necessário utilizar um TES que atualize o poder de terceiro para os tipos de Romaneio 3 (remessa) e tipo 6 do romaneio (devolução). Exemplo: Contrato Qtd 100.000 Total Recebido: 80.000  
                Entradas : Romaneio 1- 20.000   
                Romaneio 2 - 20.000 Romaneio 3 - 40.000

Para este cenário serão selecionadas todas as notas de entrada (SD1) com saldo para o contrato (SB6) cuja quantidade e dados são detalhados nos dados informados. Desta forma a quantidade máxima a simular é 80.000 e caso informe 40.000 serão consideradas apenas as duas primeiras entregas.
