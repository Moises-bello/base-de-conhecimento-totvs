---
content_hash: 21edee7bfc8c193509fcf81bfe2912a07a14ea0daffa15eb6c54d5a30ff09c6b
fetched_at: '2026-06-29T00:08:41.236416+00:00'
page_id: '286519602'
product: rm
source: tdn-rm
title: RMCTB00007_Classificação Automática da Natureza para emissão do Sped
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286519602
version: 14
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS - Gestão Contábil |
| **Versões:** | 12.1.17 |
| **Ocorrência:** | **Classificação Automática da Natureza da Conta Contábil para emissão do Sped** |
| **Ambiente:** | Novo Modelo BackOffice |
| **Passo a passo:** | **Definição do Processo**  Para gerar o SPED Contábil, todas as contas contábeis, desde as sintéticas até as analíticas, devem ser classificadas de acordo com a sua natureza. Informamos que todas as contas de nível superior deverão ter a mesma natureza das suas subcontas.  Este processo otimiza o preenchimento do campo 'Natureza da conta para emissão do SPED', classificando um grande volume de contas ao mesmo tempo.  Para a geração do Sped Contábil cada conta deve estar classificada corretamente, visto que falhas na classificação, geram diferenças nos valores e outros erros quando da validação no PVA (Programa Validador do SPED Contábil).  **DESENVOLVIMENTO/PROCEDIMENTO**  1 - Para a classificação automática acesse: Cadastros / Contábil / Processos / Classificação Automática da Natureza para emissão do Sped:  2 - Informe os grupos e a natureza da conta para emissão do SPED para que o sistema preencha automaticamente o respectivo campo de todas as sub-contas pertencentes ao Grupo de Contas informado com a nova Natureza que você indicou para o processo.                                          Fique atento quanto às contas de Patrimônio Líquido, quando estas estiverem no grupo do passivo, deve-se executar o processo para todas as contas do passivo e posteriormente classificar as contas do grupo Patrimônio Líquido, como segue abaixo: |
| **Observações:** | O sistema não fará a classificação automática para as contas contábeis que tiverem a data de inclusão em branco. |
