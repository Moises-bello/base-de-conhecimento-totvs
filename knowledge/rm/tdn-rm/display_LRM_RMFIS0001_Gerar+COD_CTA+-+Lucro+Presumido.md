---
content_hash: c7af9c87545051d3b4a19dac0c5e84d6a59e05733989cc43419232b864896a48
fetched_at: '2026-06-29T00:09:09.247098+00:00'
page_id: '393355967'
product: rm
source: tdn-rm
title: RMFIS0001_Gerar COD_CTA - Lucro Presumido
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS0001_Gerar+COD_CTA+-+Lucro+Presumido
version: 2
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.1 |
| **Ocorrência:** | Preenchimento do campo COD\_CTA para PJ tributadas pelo Lucro Presumido |
| **Ambiente:** | CorporeRM |
| **Passo a passo:** | De acordo com o manual da EFD Contribuições: As pessoas jurídicas tributadas com base no lucro presumido não sujeitas à obrigatoriedade da ECD, nos termos da IN RFB nº 1.774/2017, poderão, opcionalmente, informar nos campos "COD\_CTA" dos registros da EFDContribuições, para os fatos geradores a partir de novembro/2017, inclusive, a informação "Dispensa de ECD - IN RFB nº 1.774/2017".    O sistema irá verificar se a Flag "Empresa obrigada - ECD" está desmarcado.  Cadastros - Filial - Anexos - Dados Fiscais - Dados Adicionais.      Na tela de geração da rotina a opção Lucro Presumido deve estar diferente de "Não se aplica".      Dessa forma o sistema criará um registro 0500 fictício com a seguinte configuração:   1. Dados do registro 0500 fictício     1. Campo 02 DT\_ALT: Data de Inclusão fixo 01/11/2017    2. Campo 03 COD\_ NAT\_CC: Código da Natureza da Conta igual a 09- outras    3. Campo 04 IND\_CTA : Indicador do Tipo da Conta fixo S - Sintética    4. Campo 05 NÍVEL: Nível igual a "0"    5. Campos 06 COD\_CTA e 07 NOME\_CTA: Código Conta e Descrição fixo "**Dispensa de ECD - IN RFB nº 1.774/2017**"     Ex: |***0500|01112017|09|S|11|Dispensa de ECD - IN RFB nº 1.774/2017|Dispensa de ECD - IN RFB nº 1.774/2017|||***    Os campos COD\_CTA dos registros citados abaixo serão preenchidos da seguinte forma:  Ex: |C501|50|1000,00|07|1000,00|0,65|6,50|***Dispensa de ECD - IN RFB nº 1.774/2017|***    Registros Afetados (Conforme Guia Pratico EFD Contribuicoes Versao 1.27)   * Bloco A: A170 campo 17 * Bloco C: C170 campo 37, C175 campo 17, C381 campo 10, C385 campo 10, C396 campo 14, C481 campo 10, C485 campo 10, C501 campo 8, C505 campo 8, C601 campo 7, C605 campo 7, C870 campo 14, C880 campo 14. * Bloco D: D100 campo 23, D101 campo 9, D105 campo 9, D201 campo 7, D205 campo 7, D300 campo 19, D350 campo 23, D501 campo 8, D505 campo 8, D601 campo 9, D605 campo 9. * Bloco F: F100 campo 17, F120 campo 16, F130 campo 19, F500 campo 15, F510 campo 15, F525 campo 11, F550 campo 15. * Bloco M: M400 campo 04, M410 campo 04, M800 campo 04, M810 campo 04. * Bloco 1: 1900 campo 13, 1101 campo 18. * Bloco P: P100 campo 11. |
| **Observações:** |  |
