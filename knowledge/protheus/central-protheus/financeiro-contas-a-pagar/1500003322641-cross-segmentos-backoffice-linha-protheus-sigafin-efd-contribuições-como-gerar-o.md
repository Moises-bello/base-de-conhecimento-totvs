---
article_id: 1500003322641
category: Financeiro - Contas a Pagar
content_hash: c27f1ece9425b6e56c71350a46e205fe08b5e799eb5033e8c7426f126c06f48d
fetched_at: '2026-06-28T22:38:07.083036+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - EFD CONTRIBUIÇÕES -
  Como gerar o registro F100 de multa e juros no Financeiro
type: support-article
updated_at: '2025-05-20T19:00:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003322641-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-EFD-CONTRIBUI%C3%87%C3%95ES-Como-gerar-o-registro-F100-de-multa-e-juros-no-Financeiro
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23995070256151)**Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**Como gerar o registro F100 de multa e juros no Financeiro?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
**Solução**Para sanar essa dúvida, realize os seguintes passos:1. Configurar os parâmetros  
**MV\_RENTRIB = .T.  
MV\_NATRNT=** Preencher com a Natureza criada para multa e juros.  
  
2. Incluir um título do **Contas a Receber** rotina**FINA740** - **FINA040 ou**

2.1 Incluir um título do **contas a pagar rotina FINA750 - FINA050**3. Exemplo da **Natureza** para o título principal  
Campo **Apur. Pis (ED\_APURPIS)**conteúdo= DEBITO  
Campo **Apur. Cofins (ED\_APURCOF)**conteúdo= DEBITO  
Campo **% Ap. PIs (ED\_PCAPPIS)** conteúdo = 1,65  
Campo **% Ap. Cofins (ED\_PCAPCOF)** conteúdo = 7,60  
Campo **Tipo Naturez (ED\_TIPO)**conteúdo = 2 - Analítico  
Campo **Cond Naturez (ED\_COND)** conteúdo = Receita  
Campo **Tp Reg (ED\_TPREG)** conteúdo = 1 - Não cumulativo  
Campo **CST Cofins (ED\_CSTCOF)** conteúdo = 01  
Campo **CST Pis (ED\_CSTPIS)** conteúdo = 01  
Campo **Ind Cmulat (ED\_INDCMLT)** conteúdo = 2 - Não cumulativo  
  
**Importante**

Se a natureza do título principal não seguir as configurações acima, obrigatoriamente o campo F100 Juros **(ED\_JURSPD)** deve ficar com conteúdo = Sim

4. Crie uma natureza no módulo financeiro para multa e juros que foi informada no parâmetro **MV\_NATRNT**, preenchendo os campos conforme abaixo:  
  
Campo **Apur. Pis (ED\_APURPIS)**conteúdo= DEBITO  
Campo **Apur. Cofins (ED\_APURCOF)**conteúdo= DEBITO  
Campo **% Ap. PIs (ED\_PCAPPIS)** conteúdo = 0,65  
Campo **% Ap. Cofins (ED\_PCAPCOF)** conteúdo = 4,00  
Campo **Tipo Naturez (ED\_TIPO)**conteúdo = 2 - Analítico  
Campo **Cond Naturez (ED\_COND)** conteúdo = despesa  
Campo **Tp Reg (ED\_TPREG)** conteúdo = 1 - Não cumulativo  
Campo **CST Cofins (ED\_CSTCOF)** conteúdo = 02  
Campo **CST Pis (ED\_CSTPIS)** conteúdo = 02  
Campo **Ind Cmulat (ED\_INDCMLT)** conteúdo = 2 - Não cumulativo  
Campo **F100 Juros (ED\_JURSPD)** conteúdo = Sim

5. Na rotina **FINA070** **Baixas a Receber**, informar o valor de **Multa** e **Tx. Permanência**

5.1 Na rotina **FINA080 Baixas a Pagar, informar o valor de Multa e Tx. Permanência**

6. Gerar Apuração via rotina **FISA001** nova apuração **PIS, COFINS** no módulo de**Livros fiscais**.  
**Parâmetros de geração do arquivo**  
**Regime PIS/COFINS** = 1- N.Cumulativo Comp.  
  
7 - Gerar arquivo TXT no módulo **FISA008**  
**Parâmetros de geração do arquivo**  
**Regime PIS/COFINS** = 1- N.Cumulativo  
**Indicador do regime cumulativo** = Caixa  
  
**Observação**

Se o parâmetro **MV\_NATRNT1** estiver com algum conteúdo não ira gerar o registro F100 de multa e juros esse parâmetro deve manter sem conteúdo.  
  
**Saiba mais**[Descontos, multas e juros no SPED PIS/COFINS](https://tdn.totvs.com/pages/releaseview.action?pageId=651685109)
