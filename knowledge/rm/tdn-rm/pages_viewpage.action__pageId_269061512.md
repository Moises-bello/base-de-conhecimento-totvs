---
content_hash: 7fca228cedc02fb08bcdbe4230040aa8596ebc468451f7fd4d60c454db53e0a1
fetched_at: '2026-06-29T00:08:21.611166+00:00'
page_id: '269061512'
product: rm
source: tdn-rm
title: RMFIS00005_Apuração de Tributos - IRRF PJ
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269061512
version: 11
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.1.18 |
| **Ocorrência:** | Parametrização - Tributo IRRF PJ |
| **Ambiente:** |  |
| **Passo a passo:** | **IMPORTANTE**: O RM Liber apura apenas o tributo IRRF PJ relacionado aos lançamentos fiscais, escriturados no TOTVS Gestão Fiscal.  Serão selecionados os lançamentos fiscais de entrada com o tributo IRRF-PJ no período conforme parâmetro financeiro "Geração do IRRF para fornecedores Pessoa Jurídica" o campo "Data Base para Geração".  **Se o parâmetro "Data Base para Geração" for diferente de Emissão (DLAF.DATAEMISSAO) ou Vencimento (DLAF.VENCIMENTO) os lançamentos fiscais serão carregados pela Data Documento(DLAF.DATALF).**      **Informações no lançamento fiscal.**     O sistema consistirá no lançamento fiscal, na aba Outros Tributos, a existência do tributo IRRF PJ, e o mesmo deve conter base, alíquota, valor, Tipo de Recolhimento e código da receita.       **Geração de guia**     Após encerrar o período de apuração, gere as guias de Apuração. **Acesse: Processo -> Geração de Guias Automaticamente**. Estas estarão visíveis em **Anexos -> Guias DARF**.      Confirme se há integração entre os sistema RM Liber e o RM Fluxus, para a Geração do Lançamento Financeiro da Guia. **Acesse: Ambiente | Parâmetros -> Integração de Sistemas - RM Liber <-> RM Fluxus e RM Fluxus <-> RM Liber**. Ambos os *flags*  **Integração**e **Aplicar para todas as Coligadas**, devem estar marcados. Em seguida, execute o processo de geração.       Informe os dados da Fatura e finalize o processo, criando o lançamento financeiro. |
| **Observações:** | Existe o controle de Valor Mínimo para a Geração das Guias(Cadastro -> Tributo - Selecione e edite o tributo -> Outros Dados ). Caso os destaques do tributo nos lançamentos fiscais não alcançam o valor estipulado, o sistema irá acumular estes valores e posteriormente, processar as guias acumuladas(Anexos | Guias DARF | Processos -> Processar Guias Acumuladas, no período de apuração). |
