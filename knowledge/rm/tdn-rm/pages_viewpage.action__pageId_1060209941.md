---
content_hash: cfce8c6a4239c287ca60c4943540ab59d485b5694c2813e58a840867f486b19b
fetched_at: '2026-06-29T00:05:52.770415+00:00'
page_id: '1060209941'
product: rm
source: tdn-rm
title: Relatório SAUREL0011 - Termo de Admissão - Procedimento Externo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1060209941
version: 8
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Funcionamento do preenchimento do campo Código Usuário no Relatório**
4. **Tabelas utilizadas**

sumarioVisão Geral

## **01. VISÃO GERAL**

O relatório "SAUREL0011 - Termo de Admissão - Procedimento Externo" é o relatório responsável pela admissão de externos no sistema RM. O relatório comunica uma série de informações referentes ao atendimento do paciente.

O relatório está atualmente no . O relatório possui uma versão para bancos de dados Oracle e uma para bancos de dados SQL. Deve ser feito o download da versão referente ao tipo de base utilizada

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

É importante que todas as consultas estejam marcadas e que o nome do relatório esteja correto.

Caso a importação via TOTVS Compartilhamento tenha sido realizada com sucesso a seguinte mensagem irá aparecer indicando que o processo foi concluído. Após esse passo o relatório poderá ser visualizado na aba de RM Reports.

Para garantir que o relatório foi importado com sucesso, vá para aba RM Reports em Ferramentas de Análise

O relatório estará dentro do dropdown TOTVS Saúde Hospitais e Clínicas → 0 - COLIGADA GLOBAL → SAUREL0011 - Termo de Admissão - Procedimento Externo (Tipo de Base escolhida)

Existem algumas formas de inserir/ter acesso ao relatório no sistema.

É de extrema importância que a associação entre campos e parâmetros seja feita desta forma para não haver inconsistências no relatório.

Assim como é feito para todos os relatórios, existe a definição do grupo de visualização desse relatório podendo estar atrelado apenas a certos grupos de usuários ou para todos.

Ao avançar deverá haver a execução do processo de conclusão de importação do relatório

Caso tudo tenha sido executado com sucesso a seguinte mensagem surgirá

O acesso ao relatório pode ser feito por Atendimento → Registro de Atendimento → selecionar o usuário que se deseja estar com os dados no relatório → Anexos → Relatórios → SAUREL0011 - Termo de Admissão - Procedimento Externo

Após esse processo o relatório será gerado com os dados do paciente.

Outra forma de acessar esse relatório é por meio de Processos → Impressão de formulários

Após esse processo irá surgir uma tela com alguns dados de parâmetros que já estão sendo passados para o relatório, apenas confirme em "ok" e o relatório será gerado

Funcionamento do preenchimento do campo Código Usuário no Relatório

## **03. Funcionamento do preenchimento do campo Código Usuário no Relatório**

**Relação Convênios / Código Usuário**

| Convênios | Código Usuário |
| --- | --- |
| SUS | Número Cartão SUS |
| Particular | Código Usuário |
| Outros convênios | Código Usuário |

É válido ressaltar que essas informações precisam estar cadastradas/preenchidas para serem mostradas no relatório

## **05. TABELAS UTILIZADAS**

Coloque o link das tabelas relacionadas
