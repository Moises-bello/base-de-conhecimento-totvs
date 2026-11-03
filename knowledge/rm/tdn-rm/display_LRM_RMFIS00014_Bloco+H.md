---
content_hash: f7355722304a22f928ba0b521727adc5928de574e275d1044228187cc6d08492
fetched_at: '2026-06-29T00:08:52.653819+00:00'
page_id: '342297670'
product: rm
source: tdn-rm
title: RMFIS00014_Bloco H
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00014_Bloco+H
version: 5
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.X. |
| **Ocorrência:** | Geração do Bloco H. |
| **Ambiente:** |  |
| **Passo a passo:** | Para geração do bloco H do SPED FISCAL o sistema Totvs Gestão Fiscal busca as informações das tabelas **TRELSLD**.  Segue abaixo consistências para geração do registro:  -No cadastro do Produto/ aba Controle Estoque deve possuir unidade de medida cadastrada;        -Cadastro do Produto/ Anexos/ Dados Discal do Produto/ aba Tributação o flag Produto Exige Inventário Fiscal deve estar marcado;        -Cadastro do Produto/ Anexos/ Saldos e Custos - produto deve possuir saldo diferente de 0,00;        -Acesse o menu: Estoque/ Processos/ Regerar Saldos e Custos - Marque o flag Forçar Regeração Total; (Esse processo atualiza o estoque)        -Verifique se o produto saiu na Ficha Fisíca Financeira pelo menu: Estoque/ Consultas e Relatórios/ Relatório de Ficha Fisíca Financeira;        Acesse o menu: Cadastros / Produtos / Editar o produto / Aba Informações por Filial - Verifique se a opção "Produto estocável" está marcada        -Informações gravadas na tabela TRELSLD;        -OBS.: É necessário que os movimentos sejam escriturados para o RM Liber.    -No arquivo do Sped Fiscal, o sistema irá gerar:    |H001|0| |H005|31122017|204000,00|01| |H010|1.01|UN|2000,000|102,000000|204000,00|0|||1.1|204000,00| |H990|4| |
| **Observações:** | Para clientes que não utilizam o RM Nucleus é necessário atualizar a tabela TRELSLD importando arquivo XML através do menu (Aplicativo RMLiber.exe em Delphi) Utilitários / Obrigações Estaduais / SPED Fiscal / Situação de estoque  Mais informações sobre o bloco H clique **[aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=422545624)** |
