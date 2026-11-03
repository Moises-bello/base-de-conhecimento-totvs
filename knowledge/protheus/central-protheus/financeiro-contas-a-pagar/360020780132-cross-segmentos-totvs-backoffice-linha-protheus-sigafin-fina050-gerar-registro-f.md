---
article_id: 360020780132
category: Financeiro - Contas a Pagar
content_hash: 95885d923cf07e5644af6beafb3d99035d1ea023edb98be95f770893133c8b2e
fetched_at: '2026-06-28T22:38:09.864109+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - SIGAFIN - FINA050 - Gerar
  registro F100 pelo Contas a Pagar
type: support-article
updated_at: '2024-06-05T21:08:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020780132-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-FINA050-Gerar-registro-F100-pelo-Contas-a-Pagar
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:01:30 min  
  
Dúvida**Como gerar o registro **F100** pelo **Contas a Pagar**?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - Contas a Pagar - A partir da versão 11.  
  
**Solução**Para incluir o registro **F100** no **Contas a Pagar** realize os seguintes passos:  
  
1. Incluir um título no **Conta a Pagar** respeitando a configuração da **Natureza**2. Configuração da **Natureza acesso o modulo Financeiro - Atualizações - Cadastro - Naturezas.**  
ExemploAba **Dados da Natureza**Campo **Cond Naturez (ED\_COND)** conteúdo = Despesa  
Campo **Tipo Naturez (ED\_TIPO)** conteúdo = 2 - Analítico

![foto1.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4411771446295/foto1.JPG)

Aba **Imposto**Campo **Tp Reg (ED\_TPREG)** conteúdo = 1 - Não cumulativo

![foto2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411766041623/foto2.png)

aba **Fiscal**Campo **Apur. Pis (ED\_APURPIS)** conteúdo= C - Credito   
Campo **Apur. Cofins (ED\_APURCOF)** conteúdo= C - Credito  
Campo **CST Cofins (ED\_CSTCOF)** conteúdo = 50 a 66  
Campo **CST Pis (ED\_CSTPIS)** conteúdo = 50 a 66  
Campo **% Ap. PIs (ED\_PCAPPIS)** conteúdo = 1,65  
Campo **% Ap. Cofins (ED\_PCAPCPF)** conteúdo = 7,60  
Campo **Ind Cmulat (ED\_INDCMLT)** conteúdo = 2 - Não cumulativo

![foto3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411766041367/foto3.png)

3. Gerar Apuração via rotina **FISA001** nova apuração **PIS COFINS** no módulo de livros fiscais.  
Perguntas ***Wizard***  
**Regime PIS/COFINS** = 1- N.Cumulativo Comp  
  
4 - Gerar arquivo TXT no módulo **FISA008**  
Perguntas da ***Wizard***  
**Regime PIS/COFINS** = 1- N.Cumulativo  
Indicador do regime cumulativo = 1- Caixa  
  
**Saiba mais**  
EFD Contribuições: [MP - FIS - EFD CONTRIBUIÇÕES - Como gerar o registro F100 por Documentos de Entrada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016077872)
