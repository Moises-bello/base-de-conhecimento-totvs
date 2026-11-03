---
article_id: 360021349131
category: Financeiro - Contas a Receber
content_hash: 99f66e5c9a8afe633438bb21017cbf0622edc80dbdf49469c5773012c5bfffdc
fetched_at: '2026-06-28T22:38:13.937925+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA040 - Gerar registro
  F100 pelo Contas a Receber
type: support-article
updated_at: '2025-10-20T17:20:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021349131-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA040-Gerar-registro-F100-pelo-Contas-a-Receber
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20769205098647)**Tempo aproximado para leitura: **00:06:00 min**

**Dúvida**Como gerar o registro F100 pelo Contas a Receber?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release 12.1.33  
  
**Solução**Para incluir o registro **F100** no **Contas a Receber** realize os seguintes passos.  
  
1. Acesse o módulo **Financeiro - Atualizações - Cadastro - Naturezas.**

Exemplo:Aba **Dados da Natureza**Campo **Cond Naturez (ED\_COND)** conteúdo = Receita   
Campo **Tipo Naturez (ED\_TIPO)** conteúdo = 2 - Analítico  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360017912691)  
  
Aba **Imposto**Campo **Tp Reg (ED\_TPREG)** conteúdo = 1 - Não cumulativo  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018030192)  
  
Aba **Fiscal**Campo **Apur. Pis (ED\_APURPIS)** conteúdo= D - Débito.    
Campo **Apur. Cofins (ED\_APURCOF)** conteúdo= D - Débito  
Campo **CST Cofins (ED\_CSTCOF)** conteúdo = Conforme a necessidade  
Campo **CST Pis (ED\_CSTPIS)** conteúdo = Conforme a necessidade  
Campo **% Ap. PIs (ED\_PCAPPIS)** conteúdo = 1,65  
Campo **% Ap. Cofins (ED\_PCAPCOF)** conteúdo = 7,60  
Campo **Ind Cmulat (ED\_INDCMLT)** conteúdo = 2 - Não cumulativo  
  
![2019-07-11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040994154)

2. Incluir um título no **Contas a Receber** respeitando a configuração da **Natureza.**

3. Gerar apuração via rotina **FISA001** nova apuração PIS, COFINS no módulo de livros fiscais.  
**Parâmetros de geração do arquivo:**  
**Regime PIS/COFINS** = 1- N.Cumulativo Comp  
**PIS Folha de Salario ?** = 2- Não  
**Sociedade Cooperativa ?** = 2- Não  
**Instituição Financeira ?** = 2- Não  
**Diferimento ?** = 2- Não  
**Cupom Fiscal ?** = 2- Não  
  
4. Configuração de exemplo dos parâmetros na rotina **FISA001**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22374127467287)  
  
5 - Gerar arquivo TXT no módulo **FISA008**  
**Parâmetros de geração do arquivo**  
**Regime PIS/COFINS** = 1- N.Cumulativo  
**Indicador do regime cumulativo** = 1-Consolidado
