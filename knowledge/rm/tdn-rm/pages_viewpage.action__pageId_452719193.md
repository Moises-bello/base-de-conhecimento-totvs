---
content_hash: b0679a1a46424fdf6870e859ddbeea65da14ec0a5d896e25de69bdf666bec18e
fetched_at: '2026-06-29T00:10:04.074667+00:00'
page_id: '452719193'
product: rm
source: tdn-rm
title: Importação MIMS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719193
version: 2
---

Esta importação consiste na integração do RM Labore com o sistema de Recursos Humanos, MIMS, desenvolvido pela Mincom  
 S.A. Este sistema fornecerá as informações necessárias, através de arquivos texto, que serão importadas para a base de dados  
 da linha RM, de modo a facilitar o processamento da folha de pagamento. Esta funcionalidade de importação MIMS verifica se o  
 registro já existe na base, alterando-o em caso positivo.

**As seguintes entidades poderão ser importadas:**

**MF810**, referente a dados pessoais do funcionário;  
 **MF760**, referente a dados do funcionário e;  
 **MF761**, referente a dados dos dependentes do funcionário.  
 Para a realização da importação, deverão ser informados três arquivos do tipo **.txt** (arquivos do tipo texto) a partir dos seguintes  
 campos:

**Arquivo de Layout**  
 Neste arquivo deverá estar definido o layout com todos em campos de cada entidade a ser importada, onde cada linha deverá ser  
 identificada pela entidade. Desta forma, o usuário poderá definir quais campos serão importados.  
 Sua estrutura deverá ser a seguinte:  
 **<nome da entidade>;<1º campo>;<2º campo>;<3º campo>;<4º campo>...**

**Onde:**  
 O <nome da entidade> pode ser: MF810, MF760 ou MF761  
 Cada campo deve ser obrigatoriamente o nome de uma coluna de uma das tabelas PFUNC, PESSOA ou PFDEPEND, existentes  
 na base de dados da RM.

**Observação:**  
 O delimitador de campos é "**;**" (**ponto-e-vírgula**).

**Exemplo:**  
 MF810;CODCOLIGADA;CHAPA;NOME;DTNASCIMENTO;SEXO;NACIONALIDADE  
 MF760;CODCOLIGADA;CHAPA;NOME;CODTIPO;DTNASCIMENTO;DATAADMISSAO  
 MF761;CODCOLIGADA;CHAPA;NRODEPEND;NOME;DTNASCIMENTO;SEXO

**Arquivo De/Para**  
 Neste arquivo deverão ser definidos os campos que existem no MIMS cujo código está definido de forma diferente no RM Labore,  
 por exemplo, a nacionalidade "Brasileiro" tem o código igual a 10 no RM Labore e pode ter outro código diferente de 10 no MIMS.  
 Para a realização da importação, esse valor deverá ser convertido, pelo sistema, em um valor existente no RM Labore.  
 Sua estrutura deve ser a seguinte:  
 **<nome da coluna no RM Labore>;<valor "DE" existente no MIMS >;<valor "PARA" existente no RM Labore>**  
 Observe que o delimitador de campos é "**;**" (**ponto-e-vírgula**).

**Exemplo:**  
 SEXO;M;M  
 SEXO;F;F  
 SEXO;U;M  
 NACIONALIDADE;XX;10  
 NACIONALIDADE;YY;20  
 O campo "nome da coluna no RM Labore" deve ser obrigatoriamente o nome de uma coluna de uma das  
 tabelas PFUNC, PESSOA ou PFDEPEND, existentes na base de dados da RM.

**Arquivo a ser importado**  
 Neste arquivo devem estar os registros que serão importados. A estrutura deste arquivo deve seguir as seguintes regras:  
 Cada linha deverá ser identificada pela entidade a ser importada: **MF810**, **MF760** ou **MF761**;  
 3.1 A ordem dos campos de cada linha, ou seja, entidade a ser importada, deverá ter a mesma ordem dos campos definidos no  
 arquivo de layout, referente àquela entidade.  
 3.2 O número de campos de cada linha, ou seja, entidade a ser importada, deve ser igual ao número de campos definido no  
 arquivo de layout, referente àquela entidade.  
 3.3 Os formatos dos campos a serem importados devem ser os seguintes:  
 3.4 Campos do tipo DATA devem ter o seguinte formato: **DDMMAAAA**

**Onde:** DD corresponde ao dia, com dois dígitos;  
 MM corresponde ao mês, com dois dígitos e;  
 AAAA corresponde ao ano, com quatro dígitos.  
 3.4.1 Campos do tipo REAL devem ter o seguinte formato: **99999999,99**, onde o separador decimal deve ser **vírgula.**

**Exemplo:**  
 De acordo com o layout abaixo (definido no exemplo do item 1),  
 MF810;CODCOLIGADA;CHAPA;NOME;DTNASCIMENTO;SEXO;NACIONALIDADE  
 MF760;CODCOLIGADA;CHAPA;NOME;CODTIPO;DTNASCIMENTO;DATAADMISSAO  
 MF761;CODCOLIGADA;CHAPA;NRODEPEND;NOME;DTNASCIMENTO;SEXO  
 O arquivo a ser importado deverá ter a seguinte estrutura:  
 MF810;1;00001;JOSÉ DA SILVA QUEIROZ;01051943;M;10  
 MF810;1;00002;MARIA APARECIDA CARDOSO;23021972;F;10  
 MF810;1;00003;FERNANDA FERREIRA;12101975;F;10  
 MF760;1;00004;2;CARLOS AUGUSTO NUNES;06091956;05101997  
 MF761;1;00001;2;MARIANA DA SILVA QUEIROZ;08071984;F  
 MF761;1;00001;2;BRUNO DA SILVA QUEIROZ;15111988;M  
 MF760;00004;CARLOS;AUGUSTO;NUNES;N;06091956;05101997  
 MF761;00001;1;MARIANA DA SILVA QUEIROZ;08071984;F  
 MF761;00001;1;BRUNO DA SILVA QUEIROZ ;15111988;M

**Observação:**  
 O delimitador de campos é "**;**" (**ponto-e-vírgula**).  
 Existe uma opção para a geração de um **arquivo de LOG**, que irá reportar todos os erros e avisos  
 que possam vir a ocorrer durante a importação. Para que o arquivo de log seja gerado, selecione a  
 opção "Gera Arquivo de Log" e informe o caminho deste arquivo. Caso o caminho do arquivo de log  
 não seja informado, o sistema irá gerá-lo no mesmo diretório de instalação do RM Labore. Para  
 iniciar a importação, após ter informado todos os parâmetros necessários, clique no botão  
 "Importar". Se houver algum erro ou aviso durante a importação, os mesmos serão reportados no  
 arquivo de Log.

**Observações importantes:**  
 Todos os arquivos deverão ter seus campos separados por "**;**" (**ponto-e-vírgula**);  
 O campo definível **Código da Coligada** deverá ser informado em todas as entidades a serem  
 importadas.  
 Serão importados apenas os registros cujo **Código da Coligada** é igual ao **Código da Coligada**  
 **corrente**. Para que os registros referentes à outra coligada existente na base de dados sejam  
 importados, o usuário terá que trocar de coligada antes de realizar a importação.  
 Todos os campos existentes no arquivo de layout e no arquivo De/Para devem existir nas tabelas  
 PPESSOA, PFUNC ou PFDEPEND. Estas tabelas referem-se às entidades importadas.  
 Para a **inserção** de novos funcionários, os campos **Nome** e **Data de nascimento** devem ser  
 informados. Novos funcionários podem ser inseridos via importação das entidades **MF810** e  
 **MF760**. Caso não haja como inserir estes campos nos registros do tipo MF810 e MF761, os dados  
 dos funcionários que estiverem sendo importados apenas poderão ser atualizados, ou seja, estes  
 funcionários já deverão estar cadastrados na base de dados. Estes campos são necessários para  
 que o sistema reconheça uma pessoa sem duplicá-la no cadastro.  
 A situação atual do registro sempre deve ser informada no arquivo a ser importado. Por exemplo,  
 se apenas um campo tiver sido modificado, os valores dos outros campos não poderão ser  
 enviados como NULOS. Seus valores devem ser informados, mesmo se não tiverem sido alterados.  
 Para preencher o conteúdo do campo "Número da Ficha de Registro do Funcionário", o sistema  
 precisa validá-lo de acordo com o código da filial em que este funcionário está sendo cadastrado.  
 Para isto, antes de iniciar a importação, cadastre as filiais referentes à cada coligada cadastrada.  
 **Observação:**  
 Se o parâmetro "Número da ficha de registro gerada pelo sistema" em OPÇÕES | PARÂMETROS |  
 RM LABORE | OUTROS PARÂMETROS | PARÂMETROS II estiver marcado o arquivo não precisará  
 desta informação, mas se não estiver marcado o sistema precisa da informação no arquivo para a  
 importação.  
 **Caminho Default**  
 Neste campo você deverá indicar o caminho do diretório onde os arquivos a serem importados se encontrarão. Este deverá ser o  
 primeiro procedimento a ser seguido para a importação de dados.  
 **Exemplo:**  
 C:\ temp  
 Para procurar o diretório, clique no botão **Seta Caminho Default**.  
 **Observação:**  
 Quando o usuário seta um diretório Default este caminho permanece gravado.  
 **Gerar log**  
 Deixe esta opção selecionada se pretender gerar arquivo listando eventuais erros na importação. Esse arquivo conterá também  
 avisos ("warnings"), que não afetam o processamento. A listagem de erros ajuda a entendê-los e é importante também caso você  
 venha a consultar o suporte técnico da TOTVS.  
 Com esta opção selecionada, será disponibilizada também:  
 **Substituir arquivo**  
 Selecionando esta opção, o conteúdo do arquivo será sobreposto pelo movimento que está sendo agora cancelado  
 **Adicionar cancelamento no final do arquivo**  
 Selecionando esta opção, o conteúdo do arquivo informado será preservado e o novo cancelamento será apenas adicionado ao  
 seu final.  
 **Importar**  
 Clique neste botão para realizar a importação.  
 **Observação:**  
 Após a importação do arquivo MIMS, o sistema apresentará a mensagem de finalização da  
 importação podendo haver advertências durante a mesma e perguntando ao usuário se ele deseja  
 ou não verificar o Log de erros. Caso não ocorram advertências, o sistema informará que a  
 importação foi realizada com sucesso.
