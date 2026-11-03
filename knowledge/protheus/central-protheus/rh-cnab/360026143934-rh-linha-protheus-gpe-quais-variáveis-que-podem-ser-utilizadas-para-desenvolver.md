---
article_id: 360026143934
category: RH - CNAB
content_hash: d1b420c2b5a4bcc56c8ddc7eed8d3ea0c5fab933da1063519811df63c2b01382
fetched_at: '2026-06-28T22:43:39.334547+00:00'
product: protheus
section_id: 360004833653
source: central-protheus
title: RH - Linha Protheus - GPE - Quais variáveis que podem ser utilizadas para desenvolver
  um CNAB de Folha de Pagamento
type: support-article
updated_at: '2025-09-19T19:06:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026143934-RH-Linha-Protheus-GPE-Quais-vari%C3%A1veis-que-podem-ser-utilizadas-para-desenvolver-um-CNAB-de-Folha-de-Pagamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32854301130391)**Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Quais variáveis que podem ser utilizadas para desenvolver um CNAB (Folha de Pagamento)?   
(Disponível apenas para CNAB modelo 1 e 2)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Variáveis que podem ser utilizadas na configuração do layout de arquivo CNAB (Folha de pagamento):

* Banco favorecido - **Variável :** cBanco; **Busca:** Tabela SRA - Campo **RA\_BCDEPSA**
* Agência - **Variável :** cBanco; **Busca:** Tabela SRA - Campo **RA\_BCDEPSA**
* Conta - **Variável :** cConta; **Busca:** Tabela SRA - Campo **RA\_CTDEPSA**
* Dac - **Variável :** cConta; **Busca:** Tabela SRA - Campo **RA\_CTDEPSA**
* Nome Favorecido - **Variável :** cNome; **Busca:** Tabela SRA - Campo **RA\_NOMECMP** (Nome completo).
* Data Pagamento - **Variável :** Gravadata(M->dDatapgto,.F.,5) **Busca:** Data de pagamento informada no campo "Data de Crédito" informada no grupo de perguntas da rotina GPEM080 (Geração de Arquivo líquido)
* Valor Pagamento - **Variável :** NVALOR; **Busca:** Tabelas do roteiro selecionado (SRC - folha aberta / SRD - folha fechada/SRR - cálculo de férias ou rescisão - Retorno do valor da verba de líquido:   
  - Líquido de Folha: verba com ID 0047  
  - Líquido de Férias: verba com ID 0102  
  - Líquido de rescisão: verba com ID 0126  
  - Líquido de 1ª parcela de 13º: verba com ID 0678  
  - Líquido 2ª parcela de 13º : verba com ID 0021  
  - Líquido Adiantamento: verba com ID 0546  
  - Líquido VEX: verba com ID 1411  
  - Líquido PLR: verba com ID 0836
* Número inscrição: **Variável :** CCPF; **Busca:** Tabela SRA - Campo **RA\_CIC**
* **Variáveis para busca na tabela S052** (Dados do banco pagador) :  
  - Código Convênio : CCODCONVE  
  - Agência Empresa : CCODAGENC  
  - Digito Agência : CDIGAGENC  
  - Número Conta: CCODCONTA  
  - Digito da Conta: CDIGCONTA  
  - Sequencial Arquivo:  CNABSEQUENCIA()

**Importante:** Como apoio na configuração e validação do arquivo CNAB podem ser utilizados os arquivos anexos de acordo com o layout selecionado (modelo 1, modelo 2 e SISPAG).

**Saiba Mais:**

[Artigos - CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833653-RH-CNAB)
