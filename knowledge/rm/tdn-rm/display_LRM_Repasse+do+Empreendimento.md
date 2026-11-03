---
content_hash: 4dbb72eb2ca274425ed5c3664e0f84a7844aa2563bdc64d2a30e308f1d53bc28
fetched_at: '2026-06-29T00:09:47.614092+00:00'
page_id: '435105028'
product: rm
source: tdn-rm
title: Repasse do Empreendimento
type: documentation
url: https://tdn.totvs.com/display/LRM/Repasse+do+Empreendimento
version: 8
---

**Repasse do Empreendimento**

---

O usuário deverá seguir os seguintes passos para geração do lançamento a pagar:

**1**. Parametrização do tipo de parcela que gera repasse: localizado em Venda/ Plano / Tipos de Parcelas, após abrir esta janela deve-se então selecionar o tipo de parcela que irá gerar o repasse clicar em Anexos e Selecionar a opção Parâmetros para o Tipo de Parcela, em seguida na janela Opcionais do Tipo de Parcela deve ser selecionada a opção Sim para o campo Gera Repasse;

**2**. Parametrização do percentual de repasse no TOTVS Incorporação: Este percentual de repasse é configurado na Subunidade, Unidade, ou Empreendimento, nesta ordem de prioridade, e é feito através do Anexo Dados de Repasse. Com isso, basta clicar no botão Novo e definir o Percentual em seu respectivo campo e o Cliente/Fornecedor através do campo Código cliente/fornecedor, sendo que o Cliente/Fornecedor escolhido deve ser do tipo "Fornecedor" ou "Ambos". Observação: Uma vez cadastrado um Dado de Repasse do Empreendimento, unidade ou subunidade, e gerados lançamentos financeiros referentes a Vendas, o cadastro de Dado de Repasse do Empreendimento não poderá ser editado e nem excluído;

**3**. Geração dos lançamentos financeiros, através do TOTVS Incorporação, neste momento as informações de repasse serão inseridas no sistema financeiro. Para definição do percentual de repasse o sistema irá buscá-lo na seguinte ordem: Subunidade; Unidade; Empreendimento. A primeira ocorrência encontrada será utilizada na geração dos dados de repasse ([Repasse com Multa, Juros e Desconto](https://tdn.totvs.com/x/fT7dKQ));

**4**. A partir da versão 12.1.19 o TOTVS Incorporação tratará também o FIDEICOMISO, que é um arranjo legal que permite a participação de mais de uma empresa nos ganhos financeiros, ao invés de gerar lançamentos financeiros, serão gerados movimentos no módulo de Gestão de Compras e Materiais (Somente versão México).

**Observação:**

No momento que o sistema imobiliário gera os lançamentos financeiros, o processo insere automaticamente os lançamentos de repasse. Esta geração não necessita ser executada manualmente no financeiro.   
No momento que o TOTVS Incorporação cancelar uma parcela, a integração dos sistemas imobiliário/financeiro irá cancelar o lançamento financeiro e excluirá o(s) lançamento(s) de repasse associados.

**Observação:**

A parametrização do tipo de parcela que gera repasse e do percentual de repasse é fundamental para a geração do lançamento de repasse. Os lançamentos de repasse a pagar são associados aos lançamentos a receber de origem pela tabela FREPASSE. Não ocorrendo a parametrização corretamente o TOTVS Incorporação não irá gerar os lançamentos de repasse. - Além das consistências presentes no processo de repasse atual; A política de repasse aplicada será idêntica a atual utilizada pelo TOTVS Gestão Financeira; O lançamento gerado pelo repasse só poderá ser baixado após a baixa do lançamento a receber que gerou o repasse;
