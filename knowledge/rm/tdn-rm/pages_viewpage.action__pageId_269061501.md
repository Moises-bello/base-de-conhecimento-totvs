---
content_hash: de291d9e15109c97469d6c5754b76a57871c16eef0dac6c63c0559992d6df37d
fetched_at: '2026-06-29T00:08:21.606249+00:00'
page_id: '269061501'
product: rm
source: tdn-rm
title: RMFIS00002_Apuração de Tributos - INSS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269061501
version: 8
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.1.X |
| **Ocorrência:** | Parametrização - Tributo INSS |
| **Ambiente:** |  |
| **Passo a passo:** | **IMPORTANTE**: O  RM Liber apura apenas o tributo INSS relacionado aos lançamentos fiscais. A apuração do tributo INSS de Pessoa Física é de responsabilidade do aplicativo RM Labore. Mesmo que a empresa trabalhe com o RM Nucleus, os movimentos devem ser escriturados ao RM Liber.    **\*\* A DATA BASE PARA APURAÇÃO DO TRIBUTO INSS, É A DATA DE EMISSÃO DOS LANÇAMENTOS FISCAIS \*\***        **Informações no lançamento fiscal.**  O sistema consistirá no lançamento fiscal de entrada, na aba Outros Tributos do item, a existência do tributo INSS, e o mesmo deve conter base, alíquota, valor e código da receita.    **Geração de guia**  Após encerrar o período de apuração, gere as guias de Apuração. **Acesse: Processo -> Geração de Guias Automaticamente**. Estas estarão visíveis em **Anexos -> Guias GPS**.        Confirme se há integração entre os sistema RM Liber e o RM Fluxus, para a Geração do Lançamento Financeiro da Guia. **Acesse: Ambiente | Parâmetros -> Integração de Sistemas - RM Liber <-> RM Fluxus e RM Fluxus <-> RM Liber**. Ambos os *flags*  **Integração**e **Aplicar para todas as Coligadas**, devem estar marcados. Em seguida, execute o processo de geração.         Informe os dados da Fatura e finalize o processo, criando o documento financeiro. |
| **Observações:** |  |
