---
article_id: 360026396974
category: Escrita Fiscal - Impostos - ICMS - Apuração e Livros Fiscais - Livro - Regime
  de Apuração
content_hash: 3e108f19a0b55e623260e0ab89d390a50b7db078e4eab0c6636077ddb8a3906b
fetched_at: '2026-06-28T22:39:22.147743+00:00'
product: protheus
section_id: 1500001538681
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Atualização tabela
  CDO
type: support-article
updated_at: '2023-04-27T17:45:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026396974-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Atualiza%C3%A7%C3%A3o-tabela-CDO
---

**Dúvida**Como alimentar tabela CDO - Publicada no site do SPED como Ajustes dos Saldos da Apuração do ICMS  
   
 **Ambiente**Exemplo:  
Protheus – Fiscal – A partir da versão 12.1.17  
   
**Solução**  
 Para solucionar essa dúvida, realize os seguintes passos:

Acesse site da receita:

<http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal>

1. Selecionar Tabelas de Seu Estado;  
  
2. Baixar Ajustes dos Saldos da Apuração do ICMS (Arquivo TXT);  
  
3. Coloque o Arquivo TXT dentro da pasta Protheus\_data/ System;  
  
4. Inicialize Protheus utilizado "programa inicial" como U\_IMPSPED;  
  
5. Durante o processo será feita pergunta (deseja efetuar a importação das informações cadastrais do SPED?) selecione botão SIM;  
  
6. Selecione a pasta que esta o arquivo TXT (Protheus\_data / System);  
  
Após continuar processo será exibido relatório com as tabelas atualizadas.  
  
A tabela CDO esta atualizada conforme TXT.
