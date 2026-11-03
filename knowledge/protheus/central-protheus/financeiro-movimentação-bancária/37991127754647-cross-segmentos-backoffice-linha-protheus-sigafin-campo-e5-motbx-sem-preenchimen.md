---
article_id: 37991127754647
category: Financeiro - Movimentação Bancária
content_hash: 0fda282ffd5ba5a3d59146a82065da87f29e1ccd09de6a91091626aeff0c445b
fetched_at: '2026-06-28T22:38:19.319927+00:00'
product: protheus
section_id: 1500001550402
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Campo E5_MOTBX sem
  preenchimento nas movimentações bancárias
type: support-article
updated_at: '2026-01-28T14:29:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37991127754647-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Campo-E5-MOTBX-sem-preenchimento-nas-movimenta%C3%A7%C3%B5es-banc%C3%A1rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37991127749783) Tempo aproximado para leitura: **00:10 min**  
  
**Dúvida**  
Por que em alguns lançamentos de movimentação bancária o campo Motivo de Baixa (E5\_MOTBX) apresenta-se vazio, enquanto outros são preenchidos com siglas como NOR?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução:**

O campo **E5\_MOTBX** tem como finalidade armazenar o motivo da baixa em movimentações bancárias originadas de processos de previsão, ou seja, títulos que passaram pelas rotinas de Contas a Pagar ou Contas a Receber.

Quando o campo está **vazio**, isso indica que a movimentação bancária ocorreu de forma **direta**, sem passar por um processo de baixa de título. Um exemplo comum é a rotina **Movimentação Bancária (FINA100)**, que alimenta as tabelas **SE5/FK5** diretamente, sem a necessidade de um título precursor.

Caso deseje identificar a origem exata de cada lançamento, deve-se emitir uma consulta genérica na tabela SE5 e validar o conteúdo do campo **E5\_ORIGEM**, que indica qual rotina gerou aquele movimento.

Quando há um processo de baixa, o Protheus utiliza a tabela de **Motivos de Baixa (F7G) para gravação das siglas de identificação da baixa**. Abaixo, listamos os motivos padrão do sistema:

| Motivos de Baixa |
| --- |
| **Normal (NOR)** Utilizado para títulos de pagamentos normais.   * Baixas a pagar: atualiza automaticamente a movimentação bancária quando há geração de cheque. * Baixas a receber: atualiza automaticamente a movimentação bancária. |
| **Devolução (DEV)** Utilizado em recebimentos referentes a devoluções.   * Não atualiza movimentação bancária, tanto em baixas a pagar quanto a receber. |
| **Dação (DAC)** Utilizado quando um bem ou direito é considerado forma de pagamento.   * Não atualiza movimentação bancária, tanto em baixas a pagar quanto a receber. |
| **Vendor (VEN)** Utilizado em pagamentos de títulos via empréstimo bancário.   * O banco passa a ser o beneficiário. * Requer contrato bancário cadastrado. * Atualiza movimentação bancária. * Utilizado somente em baixas a pagar. |
| **Débito em Conta Corrente** Utilizado para debitar automaticamente a movimentação bancária, sem necessidade de gerar cheque.   * Utilizado em baixas a pagar. |
| **Compensação (CMP)** Utilizado na compensação de títulos financeiros das carteiras a pagar e a receber.   * Não movimenta saldo bancário. |
| **Compensação entre Carteiras (CEC)** Utilizado exclusivamente na rotina **FINA450 – Compensação entre Carteiras**.   * Utilizado em ambas as carteiras. * Não movimenta saldo bancário. * Considera cálculo de comissão e gera cheque caso o título seja baixado com cheque informado. |
| **Liquidação (LIQ)** Utilizado exclusivamente nas rotinas:   * **FINA460 – Contas a Receber** * **FINA565 – Contas a Pagar** * Utilizado em ambas as carteiras. * Não movimenta saldo bancário. * Considera cálculo de comissão e gera cheque, caso o título seja baixado com cheque informado. |
| **Aglutinação de Impostos (AGL)** Utilizado na rotina **FINA870 – Aglutinação de INSS**.   * Utilizado em ambas as carteiras. * Não movimenta saldo bancário. * Não considera cálculo de comissão. * Não gera cheque. |
| **Outra Loja (LOJ)** Utilizado em ambas as carteiras.   * Movimenta saldo bancário. * Considera cálculo de comissão e gera cheque, caso o título seja baixado com cheque informado. |
| **Baixa Troco (TRO)** Utilizado na baixa de adiantamentos da reserva quando existe troco.   * Movimenta saldo bancário. * Não considera cálculo de comissão. * Não gera cheque. |
| **Substituição de Título PR (STP)** Utilizado no processo de substituição de títulos provisórios.   * Não movimenta saldo bancário. * Não considera cálculo de comissão. * Não gera cheque. |
| **Faturas (FAT)** Utilizado na baixa de títulos para geração de faturas.   * Não movimenta saldo bancário. * Não considera cálculo de comissão. * Gera cheque. |
| **Baixa Fatura (BFT)** Utilizado na integração com Gestão Hoteleira.   * Baixa de RPS e criação de faturas no Contas a Receber. * Não movimenta saldo bancário. * Não considera cálculo de comissão. * Não gera cheque. |
| **Cancela NF (CNF)** Utilizado no módulo **Pré-Faturamento de Serviços (PFS)**.   * Não movimenta saldo bancário. * Não considera cálculo de comissão. * Não gera cheque. |
| **Mais Negócios (OFF)** Utilizado na integração com **TOTVS Mais Negócios**.   * Não movimenta saldo bancário. * Não considera cálculo de comissão. * Não gera cheque. |
| **Distrato (DIS)** Utilizado no template **GEM – Gestão de Empreendimentos Imobiliários**.   * Baixa por distrato. * Não movimenta saldo bancário. * Não considera cálculo de comissão. * Não gera cheque. |
| **Cessão de Direitos (CDD)** Utilizado no template **GEM**.   * Baixa por cessão de direito. * Não movimenta saldo bancário. * Não considera cálculo de comissão. * Não gera cheque. |
| **Mais Prazo (MPR ou conforme parâmetro MV\_MBXTECF)** Utilizado na integração com **TOTVS Mais Prazo**.   * Utilizado na carteira a pagar. * Não movimenta saldo bancário. * Não considera cálculo de comissão. * Não gera cheque. Caso o parâmetro **MV\_MBXTECF** esteja preenchido no momento da carga inicial da tabela **F7G**, a sigla será criada conforme o parâmetro; caso contrário, assume **MPR**. |
| **Antecipa (ANT ou conforme parâmetro MV\_MOTTECF)** Utilizado na integração com **TOTVS Antecipa**.   * Utilizado na carteira a receber. * Não movimenta saldo bancário. * Não considera cálculo de comissão. * Não gera cheque. Caso o parâmetro **MV\_MOTTECF** esteja preenchido, a sigla será criada conforme o parâmetro; caso contrário, assume **ANT**. |
| **DSD – Desdobramento** Utilizado nos movimentos gerados a partir da operação de desdobramento de títulos.   * Não movimenta saldo bancário. * Não considera cálculo de comissão. * Não gera cheque. |

Saiba Mais

[Cadastro de Motivo de Baixa - FINA490](https://tdn.totvs.com/display/public/PROT/Cadastro+de+Motivo+de+Baixa+-+FINA490)
