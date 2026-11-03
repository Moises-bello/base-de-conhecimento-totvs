---
article_id: 360007744371
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 0bad1cbf3eb4d3292d30c5c852ac4904b56c05833ef7b4b2b856afe7b15243bd
fetched_at: '2026-06-28T22:40:44.434258+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade Gerencial
  - ECD: Registro I150 não gerado ou Valor Esperado I150'
type: support-article
updated_at: '2026-03-18T14:17:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007744371-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Contabilidade-Gerencial-ECD-Registro-I150-n%C3%A3o-gerado-ou-Valor-Esperado-I150
---

## Dúvida

Ao importar o arquivo .txt da ECD, é apresentado o erro de validação no PVA: **"Registro I150 não gerado ou Valor Esperado I150"**. Adicionalmente, verifica-se que algumas contas do Plano de Contas que possuem movimento contábil não foram geradas no registro I155.

## Ambiente

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade Gerencial - A partir da Versão 12.

## Solução

Esse incidente ocorre devido a configurações incorretas nas naturezas das contas contábeis, falhas na apuração de resultados (contas de resultado com saldo), problemas na amarração da visão gerencial ou desatualização nos saldos consolidados do período.

### Passos

1. **Validação de Cadastros e Parâmetros:**

   * Certifique-se de que o parâmetro **MV\_CTBSPRC** esteja habilitado (configuração da Procedure da ECD).
   * Confirme as configurações do parâmetro **MV\_ATUSAL**.
   * Verifique se o calendário contábil do período em questão está aberto.
   * Valide no cadastro do Plano de Contas se os campos de **Natureza para Emissão do SPED Contábil** (`CT1_NTSPED` ou `CT1_NATCTA`) estão devidamente preenchidos e corretos.
   * Certifique-se de que o campo `CT1_SPEDST` esteja preenchido **apenas nas contas sintéticas** (com valor 0 ou 1).
   * No Plano de Contas Referencial, valide os campos: Classe da Conta (`CVD_CLASSE`), Natureza da Conta (`CVD_NATCTA`) e Conta Superior (`CVD_CTASUP`).
2. **Estrutura da Visão Gerencial e Tabelas:**

   * Verifique as amarrações da visão gerencial com o livro contábil (`Nivel_AGL`, `VL_CTA` e `COD_AGL`), bem como a ordenação do relatório (DRE e Balanço) versus o esperado na ECD (Registros J000 e J150).
   * Valide o compartilhamento das tabelas envolvidas na geração, em especial as tabelas de saldos (a tabela `CT2` continua em uso na versão 12):

     + **CQA:** Fila de saldos
     + **CQ0** e **CQ1:** Saldos Planos de Contas
     + **CQ2** e **CQ3:** Saldos Centro de Custo
     + **CQ8** e **CQ9:** Saldos Totais por Entidade
     + **CQI:** Movimentos das apurações
3. **Auditoria da Apuração de Resultados:**

   * A apuração de resultado deve ser realizada exclusivamente pelo sistema (inclusive a apuração de contas transitórias para contas de patrimônio).
   * Verifique se as contas de Receita e Despesa estão com os **saldos zerados**.
   * Se a ECD foi gerada considerando Centro de Custo, certifique-se de que eles também estão devidamente apurados.
   * Valide as flags e datas de apuração: `CQ0_LP=Z`, `CQ0_DTLP`, `CQ1_LP=Z`, `CT2_DTLP` e verifique se o campo `CSA_INDTIP` está preenchido com "E" para datas de apuração.
   * Confirme na rotina **CTBA007** ou na Tabela **CW0** se a chave LP possui registro com a descrição da apuração.
4. **Conferência de Balancete e Fechamento:**

   * Emita um balancete na data em que a diferença ou erro ocorre.
   * Observe se o total de Débito e Crédito estão corretos e se o valor da diferença apontada corresponde ao balancete. Caso não estejam batendo, identifique o lançamento através do valor da diferença e corrija a conta contábil/natureza utilizada.
   * Execute a rotina de **Fechamento Contábil** (`CTBA960`) pelo caminho **Miscelânea > Encerramentos > Fechamento Contábil**, para repor e atualizar os saldos gerados nas tabelas CQ.
5. Após concluir as análises e ajustes, gere um novo arquivo `.TXT` da escrituração e efetue a importação no PVA.

## Saiba Mais

* [MP - SIGACTB - ECD NÃO GERA REGISTROS I350 - I355 - I150 - I155](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044528493)
* [Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECD : I155 Pelo menos um dos campos deve conter valor diferente de zero](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35707320972439)
* [Compartilhamento de Tabelas - SIGACTB](https://tdn.totvs.com/display/public/PROT/CTB0012_Compartilhamento_de_tabelas_SIGACTB)
