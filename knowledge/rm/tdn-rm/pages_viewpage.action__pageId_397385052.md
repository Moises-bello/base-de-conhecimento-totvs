---
content_hash: 5338b95160c415e86256be51214c16cedc167c601f3c1f09c4ecdb15b92a06b6
fetched_at: '2026-06-29T00:09:10.444622+00:00'
page_id: '397385052'
product: rm
source: tdn-rm
title: Concessão de Aposentadoria Especial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=397385052
version: 14
---

# CONCESSÃO DE APOSENTADORIA ESPECIAL

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Obras e Projetos |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Tarefas | Tarefas | | Insumos | Insumos |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Alteração geral de insumos | Alteração geral de insumos | | Atualização de Múltiplos Registros | Atualização de Múltiplos Registros | |
| **Cadastros Iniciais:** | Tarefas, Insumos |
| **Parâmetro(s):** | Permite Concessão de Aposentadoria Especial |
| **Ponto de Entrada:** | Não se aplica |
| **Tickets relacionados** | Não se aplica |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [TOPORCAPLAN001-4614](http://jiraproducao.totvs.com.br/browse/TOPORCAPLAN001-4614) |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas Utilizadas:** | MPARAM, MISM e MTAREFA |
| **Sistema(s) Operacional(is):** | Windows |
| **Pacote:** | Não se aplica |

## Descrição

Possibilidade de emissão de um relatório que apresentará os valores dos serviços prestados por segurados em condições especiais e cuja atividade permita concessão de aposentadoria especial.

**Procedimento para Utilização**

No cadastro das tarefas (utilizadas nas planilhas de atividades e serviços do Projeto), na aba Outros, existe o campo “**Permite Concessão de Aposentadoria Especial**”, no qual para cada tarefa o usuário poderá selecionar uma das seguintes opções:

* Não se aplica;
* Permite após 15 anos de contribuição;
* Permite após 20 anos de contribuição;
* Permite após 25 anos de contribuição.

O campo existe também no cadastro de Insumos, na aba Identificação, e tem as mesmas opções de preenchimento acima, ou seja, as mesmas do cadastro de tarefas. Pode ser alterado de forma agrupada no cadastro de Insumos através da “Alteração Geral de Insumo" e na tarefa através do processo “Atualização de Múltiplos Registros”.

* Insumos:

* Alteração Geral de Insumos:

* Atualização de Múltiplos Registros:

Nos parâmetros do projeto pode-se definir se o campo “Permite Concessão de Aposentadoria Especial” estará vinculado à tarefa, ao insumo ou ambos. Com base na informação constante deste campo e nas medições/consumos efetuados para as tarefas/insumos nos contratos (exceto contratos com a finalidade Fornecimento de Material), tanto a pagar como a receber, o TOTVS Obras e Projetos permitirá a emissão de um relatório que apresentará os valores dos serviços prestados por segurados em condições especiais e cuja atividade permita concessão de aposentadoria especial.

**Importante:**

* **O preenchimento deste campo não é obrigatório em nenhum dos cadastros.**

Caso o projeto esteja parametrizado para que a informação esteja em ambos os cadastros para cálculo e geração do relatório e exista diferença entre a informação da tarefa e a informação no cadastro de algum insumo que faça parte da mesma, o sistema leva em consideração o tipo de aposentadoria especial que possui o maior adicional de alíquota do INSS, conforme o exemplo abaixo:

* Se a Tarefa possui a informação “Não se Aplica” e qualquer insumo constante da mesma possuir informação para permitir após X anos de contribuição, para esses insumos o sistema realizará o cálculo, e o valor correspondente ao seu consumo dos mesmos será apresentado na respectiva coluna de aposentadoria especial do relatório, enquanto que para os demais insumos prevalecerá a informação da tarefa;
* Se a Tarefa possui a informação “Permite após XX anos de contribuição” e a informação nos seus insumos não está preenchida, ou está preenchida com “Não se Aplica”, o sistema considerará a informação da tarefa para todas as suas medições, bem como para todos os insumos consumidos na mesma;
* Se a Tarefa possui a informação “Permite após 25 anos de contribuição” e alguns dos insumos consumidos na mesma possuem a informação para permitir após 20 ou 15 anos de contribuição, para esses insumos o sistema realizará o cálculo e o valor correspondente ao seu consumo será apresentado na respectiva coluna de aposentadoria especial do relatório (15 ou 20 anos), enquanto que para os demais insumos prevalecerá a informação da tarefa (25 anos) na geração do relatório;
* Se a Tarefa possui a informação “Permite após 15 anos de contribuição” e alguns dos insumos consumidos na mesma possuem a informação para permitir após 20 ou 25 anos de contribuição, na geração do relatório, prevalecerá a informação da tarefa (15 anos) para todos os insumos, visto que o adicional de alíquota relativo à aposentadoria especial com 15 anos de contribuição é maior do que os demais.

Conforme o exemplo, algumas informações do cálculo prevalecem sobre outras. Sendo:

* A informação “Permite após 15 anos de contribuição” prevalece sobre todas as demais;
* A informação “Permite após 20 anos de contribuição” prevalece sobre “Permite após 25 anos de contribuição” e sobre “Não se Aplica”;
* A informação “Permite após 25 anos de contribuição” prevalece apenas sobre “Não se Aplica”.

Como em grandes obras é comum que, conforme a disponibilidade financeira do cliente, um contrato fique vários períodos sem ser liberado, ou seja, fique vários meses sem ter gerado nota fiscal, e durante esse tempo, com o avanço do projeto, como uma mesma tarefa/insumo pode ter seu risco alterado, as informações relativas à concessão de aposentadoria especial serão gravadas pelo TOTVS Obras e Projetos no momento em que for gravada a **medição/consumo** das tarefas/itens.

Mesmo que durante um período contratual podem ocorrer alterações no cadastro da tarefa na informação referente à aposentadoria especial, o sistema checa e grava apenas a informação existente no momento em que for efetuada a medição. Assim, o Totvs Obras e Projetos garante que seja preservada esta informação, por isso, é imprescindível que as medições sejam atualizadas no sistema a cada período contratual, independente do momento em que a nota fiscal do cliente/fornecedor será gerada.

Exemplo do Relatório:

Exemplo do Cubo:

O relatório demonstrado acima, está disponível nos objetos gerenciais e para utilizá-lo, deve-se importar para a base.

O relatório pode ser exportado e importado, para que o próprio usuário possa alterar a sua consulta sql ou manipular colunas e filtros, conforme o exemplo abaixo:
