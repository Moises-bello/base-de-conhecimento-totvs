---
content_hash: b7cd572fcf7837bb99f013e3f77dae529a4557e56a2a57bed0fa283decff22d3
fetched_at: '2026-06-29T00:09:15.577934+00:00'
page_id: '421385417'
product: rm
source: tdn-rm
title: Integração com RM Labore
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385417
version: 2
---

---

Objetivo: Gerar arquivo de apropriação de funcionários, inclusive de substituição de funcionários, no RM Solum para ser importado pelo RM Labore. O RM Labore visa a realização das rotinas de processamento da folha de pagamento, de modo consistente e em conformidade com CLT, e Legislação Complementar, com flexibilidade para adaptar-se às alterações necessárias. A nível operacional, a integração se resume principalmente em informar a função de cada insumo, efetuar as apropriações dos funcionários no RM Solum, gerar o arquivo de exportação das apropriações, importá-lo no RM Labore e processar a folha de pagamento.

**Parametrizar o RM Solum**

Através do menu Opções | Parâmetros | RM Solum | Projetos | Pasta Integrações, ativar a integração com o RM Labore.

**Parametrizar o RM Labore**

Não há nenhuma exigência quanto à parametrização do RM Labore.

Insumos x Funcionários

Na janela de edição de insumo, informar a "Função" correspondente ao insumo que tenha incidência de leis sociais, ou seja, que seja do grupo de mão-de-obra.

Apropriação de Insumos (Funcionários)

No menu Cadastros | Apropriação de Insumos, na janela de edição é possível apropriar um funcionário para um insumo que tenha incidência de leis sociais, ou seja, que seja do grupo de mão-de-obra. Essa apropriação só pode ser efetuada para funcionários que tenham a função informada no cadastro de insumos. Informe qual o funcionário atual e o que está sendo substituído. O valor unitário da apropriação é o valor do salário do funcionário dividido pelo número de horas da jornada de trabalho.

Exportar Movimentos para o RM Labore

Através do menu Opções | Geração de Movimentos para o RM Labore pode-se gerar o arquivo de substituição de funcionários, movimentos ou ambos. O nome do arquivo de substituição gerado é SUBSTITUICAO.TXT. O nome do arquivo de movimento gerado é MOVIMENTO.TXT. Se for solicitada a geração de ambos, serão gerados os dois arquivos. Para gerar o arquivo é necessário informar o intervalo de datas de apropriação e onde o arquivo será gerado. Na geração do arquivo de movimentos é necessário informar também o evento (provento).

Importação de arquivos no RM Labore

O arquivo de controle de substituição de funcionários será importado, pelo RM Labore, através do menu Utilitários | Importação de Dados. Na pasta Parâmetros, marque a opção 'Funcionários'. Na pasta Funcionários, marque a opção 'Controle de Substituição'. Clique no botão 'Importar'. As substituições ficam disponíveis na Ficha Financeira do Funcionário. Para visualizá-la, abra a visão de funcionários, clique no ícone 'Ficha Financeira', selecione a pasta Substituição. O arquivo de movimento será importado, pelo RM Labore, através do menu Movimento | Folha de Pagamento | Importações | Importação de Movimentos. Caso ocorra algum erro, eles serão registrados no log de erros.

---
