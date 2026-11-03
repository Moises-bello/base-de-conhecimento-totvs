---
content_hash: 15475abeb090a9a09f6cd119e69bf85002a3718ab76c26ca2042afae09c820df
fetched_at: '2026-06-29T00:09:36.431604+00:00'
page_id: '425459515'
product: rm
source: tdn-rm
title: Importação de inscrições anônimas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459515
version: 8
---

**A importação de inscrições anônimas deverá ocorrer da seguinte forma**:  
1º - A instituição de ensino gera as fichas de inscrições anônimas, baseadas no lote de inscrições gerado pelo processo Gerar Inscrições Anônimas. Cada ficha estará vinculada a um número de inscrição deste lote. Nas fichas deverão conter todos os campos necessários para se realizar uma inscrição.

2º - Depois do preenchimento das fichas de inscrições a instituição despacha as mesmas para uma gráfica. A gráfica através de leitura óptica lê as fichas preenchidas e gera um arquivo TXT com layout pré-definido, onde cada linha deste arquivo irá corresponder a uma inscrição. Cada linha será composta de várias colunas separadas pelo caractere ';' (ponto e vírgula).

3º - O usuário do sistema utiliza o processo que estamos abordando; "Importar Inscrições Anônimas"; para importar as inscrições anônimas contidas no arquivo TXT gerado pela gráfica.

**Os passos descritos acima ilustram como funciona o processo tanto na vida real quanto em termos de sistema. Agora vamos discutir especificamente sobre a parte funcional do processo:**  
Após informar o Processo Seletivo,  o campo "Local de realização da prova" deverá ser informado pelo usuário. A definição deste campo é importante, pois se em alguma ficha de inscrição o candidato não tiver marcado o local de realização da prova o sistema colocará como default o local informado neste campo.

No passo seguinte será necessário utilizar o arquivo TXT com as inscrições e em seguida clicar no botão "Ler arquivo". Neste momento o processo fará uma consistência do arquivo, verificando se há campos obrigatórios em branco, se há campos com valores incompatíveis com os definidos ou até mesmo com valores maiores que os definidos.

**Obs.:** O arquivo de importação deverá ser criado no formato ANSI.

Este arquivo TXT deve obedecer a um layout de colunas definido pelo sistema:

|  |  |  |  |
| --- | --- | --- | --- |
| **Coluna** | **Descrição** | **Obrigatório?** | **Formato/Tamanho** |
| CODCOLIGADA | Código da coligada | Sim | Numérico |
| IDPS | Código do processo seletivo | Sim | Numérico |
| NUMEROINSCRICAO | Número da inscrição | Sim | Numérico |
| NOME | Nome do candidato | Sim | Texto (120 caracteres) |
| DTNASCIMENTO | Data de nascimento do candidato (dd/mm/aaaa) | Sim | Texto (8 caracteres) |
| NATURALIDADE | Cidade natal do candidato | Sim | Texto (32 caracteres) |
| ESTADONATAL | Estado natal do candidato (MG, PR etc) | Sim | Texto (2 caracteres) |
| SEXO | Sexo do candidato (M ou F) | Sim | Texto (1 caracteres) |
| RUA | Endereço do candidato | Não | Texto (140 caracteres) |
| NUMERO | Endereço do candidato | Não | Texto (8 caracteres) |
| COMPLEMENTO | Endereço do candidato | Não | Texto (60 caracteres) |
| BAIRRO | Endereço do candidato | Não | Texto (80 caracteres) |
| CEP | Endereço do candidato | Não | Texto (9 caracteres) |
| CIDADE | Endereço do candidato | Não | Texto (32 caracteres) |
| ESTADO | Endereço do candidato (MG, PR etc). **Para que o campo país seja preenchido é necessário que esse campo esteja preenchido** | Não | Texto (2 caracteres) |
| TELEFONE1 | Telefone residencial do candidato | Não | Texto (15 caracteres) |
| TELEFONE2 | Telefone profissional do candidato | Não | Texto (15 caracteres) |
| INSCRICAOENEM | Número de inscrição no ENEM | Não | Texto (15 caracteres) |
| ANOREFERENCIAENEM | Ano de referência no ENEM | Não | Inteiro |
| CARTIDENTIDADE | Número da carteira de identidade | Sim | Texto (15 caracteres) |
| ORGEMISSORIDENT | Órgão emissor da carteira de identidade | Não | Texto (15 caracteres) |
| UFCARTIDENT | Estado da carteira de identidade (MG, PR etc) | Não | Texto (2 caracteres) |
| CPF | CPF do candidato | Não | Texto (11 caracteres) |
| EMAIL | E-mail do candidato | Não | Texto (60 caracteres) |
| PRIMEIRAOPCAO | Área de interesse ofertada escolhida como primeira opção | Sim | Inteiro |
| SEGUNDAOPCAO | Área de interesse ofertada escolhida como segunda opção | Não | Inteiro |
| CODIDIOMA | Idioma escolhido na inscrição | Não | Inteiro |
| DEFAUDITIVA | Portador de deficiência auditiva? (T ou F) | Sim | Texto (1 carácter) |
| DEFVISUAL | Portador de deficiência visual? (T ou F) | Sim | Texto (1 carácter) |
| DEFFISICA | Portador de deficiência física? (T ou F) | Sim | Texto (1 carácter) |
| DEFMULTIPLA | Portador de deficiência múltipla? (T ou F) | Sim | Texto (1 carácter) |
| DEFOUTRAS | Portador de outras deficiências? (T ou F) | Não | Texto (1 carácter) |
| DEFMOTIVOOUTRAS | Descrição de outras deficiências | Não | Texto (100 caracteres) |
| ENSINOMEDIO | O candidato estará com o ensino médio concluído na data de matrícula? (T ou F) | Não | Texto (1 carácter) |
| CODMUNICIPIO | Código do município escolhido para realização das provas | Não | Texto (20 caracteres) |
| CODETDMUNICIPIO | Código do estado onde fica o município escolhido para realização das provas (MG, PR etc) | Não | Texto (2 caracteres) |
| IDCAMPUS | Código do campus escolhido para realização das provas. | Não | Numérico |
| CORRACA | Código da Cor/Raça do candidato, este campo deverá receber código referente a cor/raça, e não a descrição da mesma. Este campo poderá ser encontrado no caminho: Serviços Globais\Administração\Tabela Dinâmica\Sistema: Folha de Pagamento\IN46 - Cor\Raça | Não | Numérico |

**Exemplo de uma linha do arquivo** :

1;59;103;Enzo Gonzales 2;01/02/1983;Belo Horizonte;MG;M;;;;;;;;;;;;12345671;;;58727418472;jonas.fonseca@totvs.com.br;56;;;F;F;F;F;;;;;;   
**Importante** : Caso o script de marcação CN.2018.03\_03 seja executado, o arquivo TXT deve obedecer a um layout de colunas definido pelo sistema como o modelo abaixo:

|  |  |  |  |
| --- | --- | --- | --- |
| **Coluna** | **Descrição** | **Obrigatório?** | **Formato/Tamanho** |
| CODCOLIGADA | Código da coligada | Sim | Numérico |
| IDPS | Código do processo seletivo | Sim | Numérico |
| NUMEROINSCRICAO | Número da inscrição | Sim | Numérico |
| NOME | Nome do candidato | Sim | Texto (120 caracteres) |
| DTNASCIMENTO | Data de nascimento do candidato (dd/mm/aaaa) | Sim | Texto (8 caracteres) |
| NATURALIDADE | Cidade natal do candidato | Sim | Texto (32 caracteres) |
| ESTADONATAL | Estado natal do candidato (MG, PR etc) | Sim | Texto (2 caracteres) |
| SEXO | Sexo do candidato (M ou F) | Sim | Texto (1 caracteres) |
| RUA | Endereço do candidato | Não | Texto (140 caracteres) |
| NUMERO | Endereço do candidato | Não | Texto (8 caracteres) |
| COMPLEMENTO | Endereço do candidato | Não | Texto (60 caracteres) |
| BAIRRO | Endereço do candidato | Não | Texto (80 caracteres) |
| CEP | Endereço do candidato | Não | Texto (9 caracteres) |
| CIDADE | Endereço do candidato | Não | Texto (32 caracteres) |
| ESTADO | Endereço do candidato (MG, PR etc). **Para que o campo país seja preenchido é necessário que esse campo esteja preenchido** | Não | Texto (2 caracteres) |
| TELEFONE1 | Telefone residencial do candidato | Não | Texto (15 caracteres) |
| TELEFONE2 | Telefone profissional do candidato | Não | Texto (15 caracteres) |
| INSCRICAOENEM | Número de inscrição no ENEM | Não | Texto (15 caracteres) |
| ANOREFERENCIAENEM | Ano de referência no ENEM | Não | Inteiro |
| CARTIDENTIDADE | Número da carteira de identidade | Sim | Texto (15 caracteres) |
| ORGEMISSORIDENT | Órgão emissor da carteira de identidade | Não | Texto (15 caracteres) |
| UFCARTIDENT | Estado da carteira de identidade (MG, PR etc) | Não | Texto (2 caracteres) |
| CPF | CPF do candidato | Não | Texto (11 caracteres) |
| EMAIL | E-mail do candidato | Não | Texto (60 caracteres) |
| PRIMEIRAOPCAO | Área de interesse ofertada escolhida como primeira opção | Sim | Inteiro |
| SEGUNDAOPCAO | Área de interesse ofertada escolhida como segunda opção | Não | Inteiro |
| CODIDIOMA | Idioma escolhido na inscrição | Não | Inteiro |
| DEFAUDITIVA | Portador de deficiência auditiva? (T ou F) | Sim | Texto (1 carácter) |
| DEFVISUAL | Portador de deficiência visual? (T ou F) | Sim | Texto (1 carácter) |
| DEFFISICA | Portador de deficiência física? (T ou F) | Sim | Texto (1 carácter) |
| DEFFALA | Portador de deficiência na fala? (T ou F) | Sim | Texto (1 carácter) |
| DEFMENTAL | Portador de deficiência mental? (T ou F) | Sim | Texto (1 carácter) |
| DEFINTELECTUAL | Portador de deficiência intelectual? (T ou F) | Sim | Texto (1 carácter) |
| BRPDH - Reabilitado (BR) | Portador de deficiência BRPDH (T ou F) | Sim | Texto (1 carácter) |
| DEFOUTRAS | Portador de outras deficiências? (T ou F) | Não | Texto (1 carácter) |
| DEFMOTIVOOUTRAS | Descrição de outras deficiências | Não | Texto (1 carácter) |
| ENSINOMEDIO | O candidato estará com o ensino médio concluído na data de matrícula? (T ou F) | Não | Texto (1 carácter) |
| CODMUNICIPIO | Código do município escolhido para realização das provas | Não | Texto (20 caracteres) |
| CODETDMUNICIPIO | Código do estado onde fica o município escolhido para realização das provas (MG, PR etc) | Não | Texto (2 caracteres) |
| IDCAMPUS | Código do campus escolhido para realização das provas. | Não | Numérico |
| CORRACA | Código da Cor/Raça do candidato, este campo deverá receber código referente a cor/raça, e não a descrição da mesma. Este campo poderá ser encontrado no caminho: Serviços Globais\Administração\Tabela Dinâmica\Sistema: Folha de Pagamento\IN46 - Cor\Raça | Não | Numérico |

**Exemplo de uma linha do arquivo** :   
   
1;7;7;Enzo Gonzales 2;01/02/1983;Belo Horizonte;MG;M;;;;;;;;;;;;5465469;;;66917941417;;10;;;T;T;T;T;T;T;T;T;DEF OUTRA;;;;   
O que não for de preenchimento obrigatório poderá ficar em branco separando as colunas com ' ; ' ponto e vírgula . Se houver algum erro na leitura do arquivo o processo irá notificá-los. Se o arquivo TXT lido estiver correto, ou seja, não houverem inconsistências detectadas, então o processo poderá prosseguir e após sua execução será exibido um Log com o resultado do processamento.

O processo de criação das inscrições anônimas verifica se já existe uma cadastro na PPESSOA para a inscrição anônima que estiver sendo importada. Essa verificação é feita através dos campos chaves de unicidade de pessoa que são Nome, Data de nascimento, naturalidade e estado natal. Quando for constatado que a pessoa já existe não será criado um novo registro sendo usado o que já existia.

Se algum candidato tiver realizado a inscrição pelo Portal ou pela secretaria (WinForms) e por conseqüência também preenchido a ficha de inscrição anônima, então no momento da importação o processo irá identificar a duplicidade de inscrições, mantendo a já existente e não concluirá a da ficha.

Assim que as inscrições forem importadas será possível visualizar e consultar as mesmas através do serviço de Inscrição do Candidato.

**Observação: Fim do conteúdo adicionado**:

     a) O processo Gerar Inscrições Anônimas deve ter sido executado previamente.

    b) Ter cadastrado previamente os Locais de Processo Seletivo.

Novidades O processo de importação de inscrição anônima foi evoluído para detectar se a pessoa a ser importada já existe na tabela PPESSOA, se sim, irá reaproveitar o cadastro dessa pessoa através da chave de unicidade Nome, Data de Nascimento, Naturalidade e Estado Natal do candidato.

O que não for de preenchimento obrigatório poderá ficar em branco separando as colunas com ' ; ' ponto e vírgula . Se houver algum erro na leitura do arquivo o processo irá notificá-los.  Se o arquivo TXT lido estiver correto, ou seja, não houverem inconsistências detectadas, então o processo poderá prosseguir e após sua execução será exibido um Log com o resultado do processamento.

O processo de criação das inscrições anônimas verifica se já existe uma cadastro na PPESSOA para a inscrição anônima que estiver sendo importada. Essa verificação é feita através dos campos chaves de unicidade de pessoa que são Nome, Data de nascimento, naturalidade e estado natal. Quando for constatado que a pessoa já existe não será criado um novo registro sendo usado o que já existia.

Se algum candidato tiver realizado a inscrição pelo Portal ou pela secretaria (WinForms) e por conseqüência também preenchido a ficha de inscrição anônima, então no momento da importação o processo irá identificar a duplicidade de inscrições, mantendo a já existente e não concluirá a da ficha.

Assim que as inscrições forem importadas será possível visualizar e consultar as mesmas através do serviço de Inscrição do Candidato.

**Pré-requisitos do processo**:

   a) O processo Gerar Inscrições Anônimas ter sido previamente executado.

 b) Ter cadastrado previamente os Locais de Processo Seletivo.

Novidades O processo de importação de inscrição anônima foi evoluído para detectar se a pessoa a ser importada já existe na tabela PPESSOA, se sim, irá reaproveitar o cadastro dessa pessoa através da chave de unicidade Nome, Data de Nascimento, Naturalidade e Estado Natal do candidato.
