---
article_id: 360038098114
category: Financeiro - Contas a Pagar
content_hash: df8e13c5e448cd2c32d081e114e49ae0fe156142125188aab455e779708fccec
fetched_at: '2026-06-28T22:38:07.277690+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - F100 - Desconto Condicional
  e Desconto Incondicional
type: support-article
updated_at: '2022-04-18T18:05:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038098114-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-F100-Desconto-Condicional-e-Desconto-Incondicional
---

**Dúvida**Como gerar o registro F100 com Desconto Condicional e Desconto Incondicional.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA080 - A partir da versão 11.8  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
1. Configurar o parâmetro **MV\_RENTRIB = .T.**2. Configurar o parâmetro **MV\_NATDNT**= Preencher com a **Natureza** criada que será utilizada para cálculo de despesas não tributáveis no SPED.  
3. Incluir um título do **Contas a Pagar** rotina **FINA750** ou **FINA050.**4. Exemplo da **Natureza** para o título principal  
Campo **Apur. Pis (ED\_APURPIS)** conteúdo= CREDITO  
Campo **Apur. Cofins (ED\_APURCOF)** conteúdo= CREDITO  
Campo **% Ap. PIs (ED\_PCAPPIS)** conteúdo = 1,65  
Campo **% Ap. Cofins (ED\_PCAPCOF)** conteúdo = 7,60  
Campo **Tipo Naturez (ED\_TIPO)** conteúdo = 2 - Analítico  
Campo **Cond Naturez (ED\_COND)** conteúdo = Despesas  
Campo **Tp Reg (ED\_TPREG)** conteúdo = 1 - Não cumulativo  
Campo **CST Cofins (ED\_CSTCOF)** conteúdo = 50 a 66  
Campo **CST Pis (ED\_CSTPIS)** conteúdo = 50 a 66  
Campo **Ind Cmulat (ED\_INDCMLT)** conteúdo = 2 - Não cumulativo  
5. A natureza criada preenchida no parâmetro **MV\_NATDNT** exemplo de configuração abaixo.  
Campo **Apur. Pis (ED\_APURPIS)** conteúdo= DEBITO  
Campo **Apur. Cofins (ED\_APURCOF)** conteúdo= DEBITO  
Campo **% Ap. PIs (ED\_PCAPPIS)** conteúdo = 0,65  
Campo **% Ap. Cofins (ED\_PCAPCOF)** conteúdo = 4,00  
Campo **Tipo Naturez (ED\_TIPO)** conteúdo = 2 - Analítico  
Campo **Cond Naturez (ED\_COND)** conteúdo = Despesas  
Campo **Tp Reg (ED\_TPREG)** conteúdo = 1 - Não cumulativo  
Campo **CST Cofins (ED\_CSTCOF)** conteúdo = 02  
Campo **CST Pis (ED\_CSTPIS)** conteúdo = 02  
Campo **Ind Cmulat (ED\_INDCMLT)** conteúdo = 2 - Não cumulativo  
6. Na rotina **Baixas a Pagar Manual**, informar o valor do desconto no título e selecione o tipo de desconto, **Condicional** ou **Incondicional.**7. Gerar Apuração via rotina **FISA001** nova apuração **PIS, COFINS** no modulo de **Livros fiscais**.  
**Parâmetros de geração do arquivo**  
**Regime PIS/COFINS** = 1- N.Cumulativo Comp.  
8 - Gerar arquivo TXT no modulo **FISA008**  
**Parâmetros de geração do arquivo**  
**Regime PIS/COFINS** = 1- N.Cumulativo  
**Indicador do regime cumulativo** = Caixa  
  
**Saiba mais:**<https://tdn.totvs.com/pages/releaseview.action?pageId=651685109>
