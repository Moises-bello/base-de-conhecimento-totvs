---
content_hash: 507f198455ca647ec8a60c3ccaa903c91e86d9182d2bb470929502957ab67c99
fetched_at: '2026-06-29T00:11:10.444136+00:00'
page_id: '643759944'
product: rm
source: tdn-rm
title: Lançamento Global da Produção Agrária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=643759944
version: 10
---

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela do Lançamento Global da Produção Agrária**
   1. **Principais Campos e Parâmetros**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

É utilizado para lançar produção para os trabalhadores rurais num determinado período devido ao não apontamento na unidade agrária. Seja por motivo de quebra do coletor, corrupção do arquivo ou esquecimento do apontador.

Serão solicitados os dados para lançamento da produção na tela e inseridos na tabela PPRODUCAOAGRARIA em conformidade com as regras definidas na Importação da Produção Agrária.

Deverá cadastrar as informações fundamentais para os processamentos do Lançamento Global da Produção Agrária, a saber:

Parametrizador / Folha Agrária  
Parâmetros Locais do Usuário  
Unidade Agrária de Produção  
Programação Agrária  
Finalidade da Tarefa Agrária  
Tipo de Finalidade da Tarefa Agrária  
Tarefa Agrária  
Regra de Cálculo para Tarefa Agrária  
Associação de Regra de Cálculo e Tarefa Agrária  
Cultura Cultivada  
Vigência do Preço da Cultura Cultivada  
Preço Unitário de Produção Na Unidade Agrária

## **02. EXEMPLO DE UTILIZAÇÃO**

Vamos supor que no mês o arquivo tenha sido importado e ao importar foi verificado alguma inconsistência que fez com que o arquivo tenha sido importado com registros faltosos. O usuário poderá completar as informações a serem inseridas na tabela PPRODUCAOAGRARIA, conforme desejar.

## **03. TELAS DE LANÇAMENTO GLOBAL DE PRODUÇÃO**

**Tela de Gravação de Perfil**

**Tela de Parâmetros**

**Tela de Finalização de Processos**

**Tela de Execução de processos**

**Tela de exibição de resultados do processo**

## **04. TELA DE PARÂMETROS**

****a) Principais Campos e Parâmetros****

| Campo | Descrição |
| --- | --- |
| Código de Quebra | Selecione a quebra |
| Seleção de Funcionários | Selecione os funcionários |
| Operação | Ignorar / Somar / Substituir |
| Forma de exibição do log | Simples / Detalhado |
| Unidade agrária | Informar a unidade agrária, conforme o cadastro efetuado anteriormente. |
| Fração Agrária | Informar a fração agrária, conforme o cadastro efetuado anteriormente. |
| Programação Agrária | Informar a programação agrária, conforme o cadastro efetuado anteriormente. |
| Tarefa | Informar a tarefa, conforme o cadastro efetuado anteriormente. |
| Período de Lançamento | Informar o período para lançamento. Deverá ser observadas as regras abaixo:   * A data final não poderá ser menor que a data inicial; * O período deverá estar compreendido dentro no Período Global, ou na extensão definida nos parâmetros locais do usuário. |
| Quantidade | Informar a quantidade que não poderá ser igual ou menor que zero (0). |
| Horas | Informar o número de horas que deseja ser lançada. Não poderá ser igual ou menor que zero (0). |
| Lançar produção somente em dias trabalhados definidos no Automação de Ponto | Informar se deseja que a produção seja lançada somente em dias trabalhados definidos no sistema de automação de ponto. Será verificado as regras:   * Serão desabilitados os campos  “Lançar produção no Domingo” e “Lançar produção no Feriado”; * Será verificado tem licença para uso para o RM CHRONUS. |
| Lançar produção no domingo | Informar se deseja que a produção seja lançada  para o dia de domingo. Será verificado as regras:   * O campo "Lançar produção somente em dias trabalhados definidos no Automação de Ponto" deverá estar desmarcado. |
| Lançar produção no feriado | Informar se deseja que a produção seja lançada  para o dia de feriado. Será verificado as regras:   * O campo "Lançar produção somente em dias trabalhados definidos no Automação de Ponto" deverá estar desmarcado. |

Alguns campos têm particularidades, veja em Visão Geral (item acima).IMPORTANTE!

## **05. TABELAS UTILIZADAS**

#### PUSRPARAMLOCAL PUNIDADEAGRARIA PPROGRAMACAOAGRARIA PFINALIDADETAREFAAGRARIA GDINAM - PTPFINAGRI VTAREFA PRGRCALCAGRARIA PRGRCALCTAREFAAGRARIA PCULTURAAGRAIA PVIGENCIACULTURA PPRECOPRODUCAO PPRODUCAOAGRARIA
