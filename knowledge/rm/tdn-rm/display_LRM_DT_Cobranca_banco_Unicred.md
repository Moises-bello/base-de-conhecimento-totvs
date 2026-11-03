---
content_hash: f07f80a7d6155eb9558d1b83a6250d8bbf4e9cdf0050137ff40d5230b7ca997e
fetched_at: '2026-06-29T00:08:21.491075+00:00'
page_id: '268826327'
product: rm
source: tdn-rm
title: DT_Cobranca_banco_Unicred
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Cobranca_banco_Unicred
version: 119
---

# REMESSA BANCÁRIA BANCO UNICRED

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Função:** | *Geração Boleto e Remessa Bancária* |
| **Situação/Requisito:** |  |
| **Solução/Implementação:** |  |
| **Requisito (ISSUE):** |  |

**Descrição**

Esta funcionalidade tem como objetivo disponibilizar a geração de boletos e remessa bancária a partir de lançamentos financeiros para a instituição bancária Unicred.

**Procedimento para Configuração**

1 - No menu Movimentações bancárias| Controle bancário | Bancos e Agências do TOTVS Gestão Financeira deverão ser criados os cadastros referente ao banco Unicred com dados do banco, agência e conta corrente conforme demonstrado a seguir:

Figura 1- Cadastro do banco

Figura 2 - Cadastro de agência (Anexo Agência do cadastro de banco)

Figura 3 - Cadastro de conta corrente (Anexo Conta Corrente do cadastro de agência)

2 – No menu Movimentações bancárias| Controle bancário | Contas/Caixa deverá ser cadastrada a Conta Caixa que será vinculada ao cadastro de convênio e posteriormente esse vinculado ao lançamento financeiro para geração de boleto e remessa bancária.

Figura 4 - Cadastro de Conta Caixa

3 - No menu Movimentações bancárias | Controle bancário | Convênio deverá ser cadastrado o convênio que será utilizado pela Conta Caixa.

Figura 5 - Cadastro de convênio

**Procedimento para Utilização**

1 – Lançamento Financeiro

Ao criar o lançamento financeiro, a Conta Caixa cadastrada para o banco Unicred deverá ser vinculada na pasta Valores | Gerais. O Convênio será preenchido automaticamente após a seleção da Conta Caixa.

2 – Geração do boleto bancário

Pelo processo Contas a Pagar/Receber | Lançamentos | Processos | Boleto | Inclusão de boleto realize a inclusão do boleto. Após a geração o mesmo pode ser acessado pelo menu Contas a Pagar/Receber | Lançamentos | Anexos | Boleto, e para consolidar a geração é necessário gerar o código de barras acessando o menu Processos | Processo de geração de código de barras.

3 – Geração da remessa bancária

No book de sistema  estão disponíveis os layouts de remessa *"FINLAY0053 - Cob. Unicred (CNAB 240).TotvsGen"*, *"FINLAY0058 - Cob. Unicred 136 (Cnab240).TotvsGen"* e o *"FINLAY0059 - Cob. Unicred 136 (CNAB 400).TotvsGen".* Ao escolher o layout que irá ser utilizado na remessa, o mesmo deve ser parametrizado no cadastro do Convênio utilizado para o banco Unicred:

Para geração da remessa bancária basta utilizar o menu Contas a Pagar/Receber | Boleto | Processos | Remessa cobrança Eletrônica. O arquivo texto com os dados da remessa será salvo em local a ser definido no processo.

divs
