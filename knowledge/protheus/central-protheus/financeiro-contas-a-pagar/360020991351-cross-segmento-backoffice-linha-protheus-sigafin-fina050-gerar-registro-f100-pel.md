---
article_id: 360020991351
category: Financeiro - Contas a Pagar
content_hash: ee8bb0c4a7d264c382abea509787c631a7b53d0fcc2533e005a7f2a34d1ad832
fetched_at: '2026-06-28T22:38:08.230817+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA050 – Gerar registro
  F100 pelo Contas a Pagar
type: support-article
updated_at: '2023-09-11T19:54:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020991351-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA050-Gerar-registro-F100-pelo-Contas-a-Pagar
---

**Dúvida**Como gerar o registro F100 pelo Contas a Pagar?  
  
**Ambiente**Cross Segmento - BackOffice (Linha Protheus) – Contas a Pagar – A partir da versão 11  
  
**Solução**Para incluir o registro **F100** no **Contas a Pagar** realize os seguintes passos.  
  
1. Incluir um título no **Conta a Pagar** respeitando a configuração da **natureza**  
2. Configuração da **natureza acesso o modulo Financeiro - Atualizações - Cadastro - Naturezas**Aba **Dados da Natureza**Campo **Cond Naturez (ED\_COND)** conteúdo = Despesa  
Campo **Tipo Naturez (ED\_TIPO)** conteúdo = 2 - Analítico  
  
![Aba_dados_natureza.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360017432571)  
  
Aba **Imposto**Campo **Tp Reg (ED\_TPREG)** conteúdo = 1 - Não cumulativo  
   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360017433391)  
  
aba **Fiscal**Campo **Apur. Pis (ED\_APURPIS)** conteúdo= C - Credito   
Campo **Apur. Cofins (ED\_APURCOF)** conteúdo= C - Credito  
Campo **CST Cofins (ED\_CSTCOF)** conteúdo = 50 a 66  
Campo **CST Pis (ED\_CSTPIS)** conteúdo = 50 a 66  
Campo **% Ap. PIs (ED\_PCAPPIS)** conteúdo = 1,65  
Campo **% Ap. Cofins (ED\_PCAPCPF)** conteúdo = 7,60  
Campo **Ind Cmulat (ED\_INDCMLT)** conteúdo = 2 - Não cumulativo  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360017549592)  
  
  
3. Gerar Apuração via rotina **FISA001** nova apuração PIS COFINS no modulo de livros fiscais  
Perguntas Wizard  
Regime PIS/COFINS = 1- N.Cumulativo Comp  
  
4 - Gerar arquivo TXT no modulo **FISA008**  
Perguntas da Wizard  
Regime PIS/COFINS = 1- N.Cumulativo  
Indicador do regime cumulativo = 1- Caixa
