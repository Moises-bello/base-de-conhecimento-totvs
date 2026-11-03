---
content_hash: d56e41a6267bf3a3411248d64a1196b93265ed9bdacb1af98fe1e96afdc8d711
fetched_at: '2026-06-29T00:10:27.751619+00:00'
page_id: '516642298'
product: rm
source: tdn-rm
title: Cadastros Contas de Custos
type: documentation
url: https://tdn.totvs.com/display/LRM/Cadastros+Contas+de+Custos
version: 1
---

## 

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela inicial**
   1. **Outras Ações / Ações relacionadas**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

A abordagem de custeio por absorção compreende a conceituação da contabilidade de custos. Utilizam-se as expressões de custos diretos e indiretos. Quando se identifica o centro de custo como unidade de acumulação de custos, toda a identificação deve levar em consideração este ponto de referência.

A atenção à unidade de segmentação utilizada é importante no processo de acumulação e apropriação dos custos. Muitas vezes um custo é direto quando utiliza a unidade de centro de custo, porém se torna indireto quando a unidade é um serviço, como por exemplo, um tratamento ou um paciente-dia específico.

Para cadastrar uma conta de custo (menu Cadastros/Contas de Custo) é preciso antes ter um plano de conta de custo para o mesmo.

## **02. EXEMPLO DE UTILIZAÇÃO**

Gestão de custos > cadastros >  contas de custos

## **03. TELA INICIAL**

**Outras Ações / Ações relacionadas**

| Ação | Descrição |
| --- | --- |
| Procedimento para inclusão | 1. Clique em Incluir (Página em branco) para incluir um novo plano de contas de custo 2. No campo Código Plano de Conta de Custo informe um código numérico que será referência ao plano de conta de custo. 3. No campo Vigência informe o início do período de vigência no formato ano/mês. 4. No campo Plano de Conta de Custo informe uma breve descrição. 5. No campo Máscara é definida através de níveis hierárquicos que atendem ao modelo de gestão do Hospital e ela deverá ser preenchida utilizando os caracteres “.” (ponto) e “#” (sustenido). Exemplo: (#.#.##.###). 6. Clique em OK. |

## **04. TABELAS UTILIZADAS**

* Tela plano de contas de custos

A tela de cadastro de contas de custo é chamada a partir da opção da tela Plano de Contas de Custo / Anexos / Contas de Custo. Verifique abaixo a tela de cadastro de contas de custo.

A partir da seguinte tela é possível visualizar a relação de registros das contas de custo, se houver. Verifique a tela que exibe a relação de cadastros de Contas de Custo efetuados de acordo com a máscara especificada.

**Cadastrando Conta de Custo**

1. Clique em Incluir (Página em branco) para incluir um novo cadastro de contas de custo.
2. No campo Código Conta Custo para a sua inclusão deverá ser respeitada a máscara informada no cadastro do plano de conta de custo. Exemplo: Para uma máscara (#.#.###) devemos cadastrar primeiro os dois primeiros níveis sintéticos (1.\_.\_\_\_) e (1.1\_\_\_\_) e em seguida cadastrar o nível analítico (1.1.001) sucessivamente.
3. No campo Conta de Custo informe uma breve descrição.
4. No campo Aplicação selecione uma das opções disponíveis para indicar o tipo de distribuição da conta (Receita (Geral), Receita, Dedução Receita, Custos, Direta ou Indireta).

   1. Receita (Geral): Utilizado para cadastrar um nível sintético de Receita para a identificação das contas de custo receita e dedução de receita.
   2. Receita: Contas que acumulam receita para a empresa. Exemplo: Diárias UTI, Diárias Internação, Materiais e Medicamentos, etc.
   3. Deduções Receita: Contas que armazenam os valores de dedução para pagamentos de impostos. Exemplos: Imposto sobre Serviços, etc.
   4. Custos: Utilizado para cadastrar um nível sintético de Custo, para a identificação das contas de custo direto e indireto.
   5. Direta: Custos diretos consistem em custos utilizados nas atividades do Hospital, cuja identificação com um centro de custos seja possível, sem a utilização de qualquer instrumento de apropriação ou rateio. Exemplo: Salários, Encargos Sociais, Materiais de Consumo, etc.
   6. Indireta: Os custos indiretos correspondem aos que não possibilitam a identificação direta com um centro de custo em particular. Portanto, para apropriação desses custos aos centros de custos é necessária à utilização de instrumento de apropriação ou rateio que estabeleçam proporções adequadas de distribuição desses insumos aos centros de custos. Exemplo: Depreciação, Seguro, Água, Energia Elétrica, etc.
5. Informe Sim ou Não para o campo Desconsidera Honorários, utilizado nos cálculos das informações de relatórios do sistema.
6. No campo Grupo de Conta selecione uma das opções disponíveis para agrupar informações que serão utilizadas nos relatórios do sistema (Serviços, MatMed, Honorários Médicos ou S.A.D.T).
7. Informe Sim ou Não para o campo Desconsidera MatMed, que é utilizado nos cálculos das informações de relatórios do sistema.
8. Em Sub. Grupo selecione uma das opções disponíveis para agrupar informações que serão utilizadas nos relatórios do sistema (Pessoal, Materiais, Medicamentos, Gerais ou Indiretos).
9. Selecione Sim ou Não para o campo Ativo.
10. Clique em OK.
