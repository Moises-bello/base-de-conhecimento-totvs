---
content_hash: 69e7e7c66e4b435f8c3816d46fdad29806aaa5c7cf002b67e6ded37464be15e7
fetched_at: '2026-06-29T00:06:18.455978+00:00'
page_id: '215485345'
product: rm
source: tdn-rm
title: TQXUUY_DT_Cadastro_De_Filiacao
type: documentation
url: https://tdn.totvs.com/display/LRM/TQXUUY_DT_Cadastro_De_Filiacao
version: 127
---

# CADASTRO DE FILIAÇÃO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Educacional** |
| **Módulo:** | **Totvs Gestão Educacional** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Cadastro de Filiação* | **Cadastro de* Filiação* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Cadastrar pai e mãe como responsável financeiro** | ***Cadastrar pai e mãe como responsável financeiro*** | | **Atualização de endereço** | **Atualização de endereço** | |
| **Cadastros Iniciais:** | *Cadastrar aluno* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados Relacionados** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server e Oracle* |
| **Tabelas Utilizadas:** | *VFILIACAO e SPESSOA* |
| **Sistema(s) Operacional(is):** | *Windows 7* |
| **Versões/Release:** | *12.1.8* |

## Descrição

Ajustes no cadastro de aluno para possibilitar o cadastro de famílias multiparentais.

**1.1** **Multiparentalidade**

A multiparentalidade pode ser definida como a possibilidade de uma pessoa ter mais de um pai ou mãe em seu registro civil.

Em decisão inédita no ano de 2012, o Tribunal de Justiça de São Paulo deferiu pedido para acrescentar na certidão de nascimento de jovem de 19 anos o nome da mãe socioafetiva, sem ser retirado o nome da mãe biológica. Esta morreu três dias após o parto, sendo que quando o filho tinha dois anos o pai se casou com outra mulher, postulante da ação em conjunto com o enteado.

(FOLHA DE SÃO PAULO, 2012)

**1.2** **Modelo de Certidão de Nascimento**

Nos modelos anteriores de Certidão de Nascimento, havia apenas dois campos destinados à filiação do aluno: Pai e Mãe. Esses modelos não atendiam as novas possibilidades de multiparentalidade e parentalidade socioafetiva.

Apenas em 2011, os campos destinados ao nome do pai e nome da mãe foram alterados apenas para filiação, que é um campo livre, sem distinção de sexo e quantidade de pessoas.

Modelo Anterior - Certidão de Nascimento utilizada antes de 2010:

Modelo Anterior - Certidão de Nascimento utilizada a partir de 2010:

Modelo Novo - Certidão de Nascimento utilizada a partir de 2011:

**1.3** **Cadastro de Alunos – Versão 12.1.7**

No Educacional só existia a possibilidade de cadastrar um pai e uma mãe para o aluno. Porém existem casos em que o aluno é registrado, em sua certidão de nascimento, com dois pais, duas mães, ou até mesmo um pai e duas mães.

Na guia Responsáveis da tela de Alunos existia apenas a opção de informar um pai e uma mãe para o aluno, e a opção de cadastrar esse pai ou essa mãe como Responsável Financeiro.

Também era possível atualizar o endereço do pai e/ou da mãe através da funcionalidade “Atualização de endereços” da guia Endereço.

**1.4** **Cadastro de Alunos – Versão 12.1.8**

Ao abrir a tela de Alunos irá aparecer a seguinte mensagem:

"A partir da versão 12.1.8, foi implementado o conceito de Multiparentalidade.

Assim, a inclusão de filiação foi alterada no cadastro de alunos e foi criado um anexo de filiação.

A base de dados foi alterada com a criação de uma nova tabela (VFILIACAO).

Os dados registrados nesta nova tabela serão sincronizados com os campos de filiação da SPESSOA para apenas um pai e uma mãe.

**Na necessidade de utilizar este novo conceito os relatórios e consultas SQL devem ser revistos para utilizar a tabela VFILIACAO**”

Na guia Responsáveis da tela de Aluno é exibida uma grid para que seja cadastrado pai e mãe, no lookup pessoa, deve-se selecionar o pai ou a mãe e marcar o tipo de relacionamento (pai ou mãe), após selecionado a pessoa, baseado no sexo sugerimos que seja pai ou mãe para facilitar o cadastro, caso queira o usuário pode alterar o tipo de relacionamento antes de adicionar.

Clicando no botão adicionar o(a) pai/mãe é adicionado na grid mas ainda não é registrado na tabela VFILIACAO, apenas quando o usuário clicar no botão salvar os dados serão enviados para o banco de dados.

O botão remover remove a filiação que estiver selecionada na grid, assim como o botão adicionar os dados só serão registrados no banco após o usuário clicar em salvar.

Validações:

O sistema bloqueia que seja adicionado uma filiação com uma pessoa que já esteja na grid de filiações.

O sistema bloqueia que seja adicionado uma filiação sem tipo de relacionamento selecionado.

O sistema não exibe como resultado do lookup de filiação a pessoa do aluno.

O(s) pai(s) e/ou mãe(s) pode(m) ser cadastrado(s) também através do Anexo Filiação.

Na tela de filiação terá o campo para selecionar a pessoa, e o campo Tipo de Relacionamento para informar se a pessoa é pai ou mãe do aluno. O campo de falecido é apenas informativo e poderá ser alterado apenas no cadastro de pessoas.

Foi criado um botão “Cadastrar PAI/MÃE como responsável”. Ao clicar no botão aparecerá uma tela para selecionar uma pessoa da filiação ou um responsável financeiro ou acadêmico.

Na tela de atualização de endereço virá a lista contendo todas as pessoas da filiação do aluno, além dos responsáveis financeiro e acadêmico

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *(12.1.8)* deste chamado.

divs
