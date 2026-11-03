---
article_id: 360026447291
category: Escrita Fiscal - Impostos - IPI
content_hash: 308aa73dc3e05a701e9b36fc6256f446a7569f7a7194d784f7573f11cb9a44e9
fetched_at: '2026-06-28T22:39:28.952849+00:00'
product: protheus
section_id: 1500001538641
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como atualizar código
  de ajustes/lançamentos manuais da apuração de IPI?
type: support-article
updated_at: '2024-07-16T11:52:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026447291-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-atualizar-c%C3%B3digo-de-ajustes-lan%C3%A7amentos-manuais-da-apura%C3%A7%C3%A3o-de-IPI
---

**Dúvida**

Como atualizar código de ajustes manuais da apuração de IPI?  
  
**Ambiente**

Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Para alimentar ou atualizar a tabela  de Ajustes manuais de apuração de IPI é necessário seguir os seguintes passos.

1. Acesse site da receita:   
<http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal>

2. Selecionar as tabelas desejadas

3. Baixar as tabelas de código de Ajuste da Apuração de IPI (Arquivo TXT)

4. Coloque o Arquivo TXT dentro da pasta System

5. Execute o U\_IMPSPED

6. Durante o processo será feita pergunta (deseja efetuar a importação das informações cadastrais do SPED?) selecione botão SIM

7. selecione a pasta que esta o arquivo TXT (System)

Após continuar processo será exibido relatório com as tabelas atualizadas.
