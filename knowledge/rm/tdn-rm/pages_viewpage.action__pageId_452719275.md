---
content_hash: 653d2bfded88d0036260a1789fc93fefd8382e2b2ded20301aeba9b31aabdd7c
fetched_at: '2026-06-29T00:10:05.136063+00:00'
page_id: '452719275'
product: rm
source: tdn-rm
title: SEFIP  - Geração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719275
version: 6
---

falseATENÇÃO:

A partir da release **12.1.2606**, esta rotina foi descontinuada, pois sua funcionalidade passou a ser atendida pelo **eSocial**.

Esse é o assistente pelo qual o usuário irá gerar o relatório do SEFIP no layout definido pela CEF (Caixa Econômica Federal). Através da execução desse assistente o arquivo será criado, para a posterior importação no aplicativo SEFIP (disponibilizado pela Caixa Econômica Federal). Para conhecer mais sobre o SEFIP recomendamos o acesso ao site da Caixa Econômica Federal.

Esse assistente é composto de 5 etapas pelas quais o responsável pela a geração dos arquivos passará, definindo a composição dos mesmos, de acordo com o layout e de acordo as informações da folha de pagamento. São essas etapas:Através do cadastro é possível controlar:

**Identificação – SEFIP**

É a tela inicial do assistente de geração do arquivo SEFIP.RE. Aqui, é dado início à geração do arquivo de acordo com layout definido pela CEF (Caixa Econômica Federal). Essa tela é composta dos parâmetros abaixo:

**Caixa "Perfil de Parâmetros"**

Essa caixa é composta de três itens:

**Criar Perfil**

Esse é o local onde são criados novos perfis ou selecionados perfis criados anteriormente. Na primeira execução do assistente é obrigatória a criação de um perfil.Esse botão tem a finalidade de excluir um perfil que não é mais utilizado.Esse Check Box tem a finalidade de indicar que o perfil que está sendo utilizado será modificado durante a execução do assistente e que tais modificações deverão ser gravadas. Ao utilizar um perfil sem a marcação desse parâmetro, caso o mesmo seja modificado durante o processo, essas alterações não serão gravadas. Na criação de um novo perfil esse parâmetro deverá estar marcado.

**Atenção 1:**  
Leia maiores informações no manual do SEFIP Para as empresas que utilizam Tomadores de Serviço o RM Labore buscará a movimentação que estiver distribuída na pasta edição do movimento por Tomador. E para as Empresas que não utilizam Tomadores de Serviço o RM Labore buscará a movimentação diretamente da Ficha Financeira.

**Atenção 2:**  
No arquivo SEFIP. RE será informado o Total de Remuneração do Funcionário (total da incidência em FGTS). Através deste valor e de outras informações, como por exemplo, afastamentos, classe de contribuição, ocorrência, valor retido do segurado (para múltiplos vínculos), e diversas outras informações, o SEFIP.EXE irá calcular os valores do FGTS e do INSS, e gerar as guias GRF e GPS. Portanto é Fundamental que as incidências estejam corretas. No manual do SEFIP existem três tabelas de incidências: Integram a remuneração para fins de cálculos dos valores devidos à Previdência Social e a serem recolhidos para o FGTS. Não integram a remuneração para fins de cálculos dos valores devidos à Previdência Social e ao FGTS. Integram a remuneração exclusivamente para fins de cálculos dos valores a serem recolhidos ao FGTS.

**Recolhimento e declaração\_SEFIP**

Nessa fase serão preenchidos os campos encontrados nos registros de abertura do arquivo SEFIP. RE. São informações da identificação inicial da empresa, do período e do motivo da entrega dos dados do arquivo.

**Competência**

Digite ou selecione o Mês e Ano de competência para geração do arquivo.

**Atenção 1:**

01 – É OBRIGATÓRIO existir o "HISTÓRICO DE SEÇÕES" (em Cadastros | Funcionários | Edição | Pasta Registro) correto para a emissão do SEFIP de meses anteriores.

**Atenção 2:**

Na geração de SEFIP em atraso, de competências anteriores, se o usuário fez alguma transferência de funcionário (s), transferindo também a sua (s) Ficha (s) Financeira (s), no período entre a competência "em atraso" e a atual, o arquivo será gerado com dois registros tipo 30 e não será validado pelo SEFIP. Isso ocorre porque no histórico da seção fica registrada a seção anterior do funcionário e a ficha financeira fica com os valores de todos os meses. Neste caso o usuário deverá acessar o histórico da seção em Cadastros | Funcionários | Edição | Pasta Registro deste funcionário, excluir seção anterior e depois cadastrá-la novamente para que o cadastro fique correto, ou ainda poderá editar o arquivo SEFIP. RE e excluir uma das linhas de registro tipo 30 duplicada.

**Atenção 3:**

Se houver alguma alteração na Ficha Financeira de algum funcionário, não estará garantida a integridade do arquivo do SEFIP, pois os valores encontrados no SEFIP emitido antes da alteração e o SEFIP emitido depois da alteração poderão sofrer mudanças devido às alterações manuais feitas pelo usuário.

**Atenção 4:**

Serão consideradas as seguintes condições para geração do SEFIP de meses anteriores, verificando o histórico de ocorrência: 1 – Para SEFIP no mês atual será considerado o registro da ocorrência em Cadastros | Funcionários | pasta FGTS/SEFIP/INSS; 2 – Para SEFIP de meses anteriores será verificado o histórico de ocorrência para a emissão do arquivo; 3 - Se não houver histórico de ocorrência será considerado o registro da ocorrência em Cadastros | Funcionários | pasta FGTS/SEFIP/INSS; 4 – Caso o primeiro registro do histórico de ocorrência for uma data posterior à admissão do funcionário e houver uma emissão do SEFIP neste período sem registro, será considerada a ocorrência em branco, porque somente o registro em branco não é necessário ser informado no histórico de ocorrência, por se tratar de uma ocorrência inicial de um funcionário.

**Observações:**

01 - Para emitir SEFIP de meses anteriores com as alterações de cadastros dos funcionários feitas nos meses anteriores o usuário NÃO poderá Liberar FLAGS, porque não há histórico para Flags. O que ocorrerá com a não Liberação dos Flags é a emissão destas alterações para cada mês de emissão do SEFIP. 02 - Não existem históricos das alterações de informações de CATEGORIA/ TIPO DE EMPREGADO, por isso no SEFIP referente meses anteriores será considerado a informação atual do funcionário nestes campos. 03 - Para o mês em que houve lançamentos que geraram SEFIP com código de recolhimento 650 o usuário deverá emitir o SEFIP por períodos seguindo as considerações para recolhimento deste código de recolhimento '650'.

**13o Salário**

Sefip para 13º Salário Marque esta opção para a geração do arquivo de competência 13 (13º salário). Vale ressaltar que, este campo não gera nenhum valor de depósito de FGTS. Os depósitos de FGTS, tanto quanto de 13º salário como na folha serão feitos juntos, no SEFIP do final do mês, onde NÃO deve ser usada a opção SEFIP 13º.

**Observação 1:**

Essa opção só fica habilitada quando, no campo Competência, é informada a competência 12 do ano solicitado.

**Observação 2:**

Se o parâmetro "Utiliza Tomadores de Serviço" estiver marcado em Opções | Parâmetros | RM Labore | Parâm. Cálculo, e se os eventos de 13º salário estiverem com o parâmetro "Segue Rateio por Tomador" marcado (exigindo a distribuição destes eventos pelo módulo Movimento | Folha De Pagamento | SEFIP - Distribuição | Distribuir), ao gerar o SEFIP 13, o sistema irá criar os registros do tipo 30, respeitando a distribuição registrada no cadastro do funcionário. Sendo assim, aqueles usuários que acharem que o rateio dos eventos de 13º devem refletir em todo o ano de trabalho, eles deverão cadastrar o rateio por tomador dos funcionários e as fórmulas de proporcionalização para refletir a situação do em todo o ano.

**Atenção 5:**

O SEFIP reconhece somente as categorias de trabalhador com código 01, 04, 05, 07, 11, 12, 19, 20 e 21, para recolhimento de INSS descontado sobre o valor de 13º Salário. Portanto, caso haja pagamento de 13º Salário para funcionários que não se enquadram nessas categorias, o usuário deverá filtrar a geração do SEFIP da competência 13 para que o sistema não gere informações desses funcionários – lembrando que a informação dos mesmos impossibilita a validação do arquivo.

**Seleção de funcionários**

Ao clicar no botão de Seleção de funcionários o sistema abrirá uma janela com os campos onde você poderá selecionar um funcionário digitando sua chapa ou localizando seu nome. Também será possível fazer a seleção de funcionários pela situação, tipo de funcionário e recebimento ou ainda criar Filtros ou Fórmulas de Seleção.

**Considerar 0,01 na transf. sem ônus da Rem. s/13**

Marque esta opção para a geração do arquivo de competência sem 13 (13º salário) com o valor de R$0,01.

**Código de Recolhimento**

Selecione o código de recolhimento que a empresa utilizará.

**Atenção 1:**

Na geração do arquivo do SEFIP com código de recolhimento 650 o usuário deve usar o filtro para retirar os funcionários que estiveram afastados por acidente de trabalho, doença ocupacional, serviço militar ou licença maternidade durante o período do dissídio coletivo. Para estes funcionários deverá ser feito o cálculo manual da diferença salarial referente ao dissídio coletivo para recolhimento de diferença de FGTS, e também no caso da licença maternidade o recolhimento também de GPS parte de empresa e terceiros no SEFIP com código de recolhimento 650.

**Observações:**

01 - Ao gerar o SEFIP no código de recolhimento 650 o usuário deve mudar o "Código de Pagamento GPS", em cadastros | seções | DADOS P/INSS, pelo código válido conforme relação constante da Instrução Normativa INSS/DC nº 02, de 20/10/99 para que o arquivo seja validado pelo Validador do SEFIP. 02 - O SEFIP com código de recolhimento 650 está disponibilizado apenas para recolhimento de dissídio coletivo. 03 - Para gerar o SEFIP com código de recolhimento 650 é necessário que a movimentação referente Diferença Salarial proveniente de dissídio coletivo esteja em envelope diferente da movimentação mensal normal do funcionário. Além disso, o usuário deverá emitir o SEFIP por período, ou seja, no período da movimentação por dissídio coletivo o usuário deve gerar um arquivo SEFIP e validar com código de recolhimento 650 e no período da movimentação normal o usuário deve gerar outro arquivo SEFIP e validar.

**Atenção 2:**

Não deve haver mais o recolhimento de funcionários administrativos em SEFIP com código de recolhimento 115 e tomador de serviços em SEFIP com código de recolhimento 150/155. "Para um mesmo FPAS, é incompatível a informação dos códigos de recolhimento 115 e 150, na mesma competência, bem como a informação dos códigos 115 e 155, também na mesma competência. Caso sejam transmitidas GFIP/SEFIP com códigos 115 e 150, ou 115 e 155, na mesma competência e no mesmo FPAS, será considerada como válida para a Previdência apenas a última GFIP/SEFIP transmitida."

**Atenção 3:**

Ao gerar o SEFIP para tomadores de serviços, o RM Labore emite uma mensagem na tela questionando se funcionários administrativos serão informados naquela geração ou não. Quando a empresa usa mais de um tipo de tomador de serviço o usuário deverá gerar os administrativos de acordo com o parâmetro marcado em Opções | Parâmetros | RM Labore | Parâm. Cálculo.

**Exemplo:**

Se a empresa cedente é "Cessão de mão-de-obra", a parte dos administrativos deverá ser gerada nos códigos de recolhimentos 150. Se a empresa cedente é "Construção civil", a parte dos administrativos deverá ser gerada nos códigos de recolhimentos 155.  
A informação Tipo Tomador, presente no cadastro de Tomador | Tributos | Tipo Tomador, deve estar preenchida corretamente conforme Construção civil e Cessão de mão-de-obra.

**Observações:**

Quando o usuário emitir um arquivo de SEFIP, será registrado neste arquivo, para todos os funcionários que tiverem parametrizados mais de um tipo de tomador de serviço, as ocorrências de múltiplos vínculos, ou seja, ocorrências 05, 06, 07 e 08 correspondentes de 01, 02, 03 e 04, para que a GPS calculada pelo validador do SEFIP fique correta somente com os valores de segurados do tomador de serviço específico. Para a ocorrência "em branco", que é dos funcionários que não estão expostos a agentes nocivos, e nunca estiveram, será emitido o SEFIP por período com a ocorrência 05 por não haver ocorrência equivalente. Somente será considerada a ocorrência cadastrada na pasta do funcionário quando o usuário for emitir o SEFIP com o período "todos".

**Atenção 4:**

Para o cálculo do campo "Dedução 13º Salário Licença Maternidade" quando usa tomador de serviços, o evento de 13º salário com código de cálculo 102 – 2ª parcela 13º salário deve ter distribuição por tomador de serviços.

**Modalidade do Sefip**

Para seleção da modalidade deverá ser observado o tipo de recolhimento que a empresa fará de acordo com o manual do SEFIP.

**Recolhimento do FGTS**

Deverá ser utilizado para identificar se o recolhimento do FGTS será realizado até o dia sete do mês seguinte ao da competência - no prazo ou será feito após esta data em atraso.

**Data de Recolhimento do FGTS** I

ndique se a data efetiva de recolhimento de FGTS, sempre que o recolhimento for realizado em atraso.

**Observações:**

Os campos Código de Recolhimento e Indicador de Recolhimento de FGTS determinam a obrigatoriedade desta data.

**Recolhimento INSS**

Deverá ser definido se o recolhimento da Previdência Social será no prazo ou em atraso.

**Observação:**

Em razão da mudança no SEFIP 8.0 ser o novo tratamento de retificações, o usuário deve se atentar para o campo "Recolhimento do INSS" ser preenchido corretamente. Portanto esse campo passa não ter valor default. Mesmo assim, o usuário, poderá configurar seu valor através de perfil.

**Data de Recolhimento da Previdência:**

Indique a data efetiva de recolhimento do INSS sempre que o recolhimento foi realizado em atraso.

**Responsável - SEFIP**

Preencha esta pasta com os dados que irão identificar a empresa, ou seja, serão levados para o registro 00 - Informações do Responsável na geração do arquivo SEFIP.

**Responsável** Informe o Nome/Razão Social, Inscrição, 'Endereço (Logradouro), Complemento, Bairro, CEP, Município e Estado para geração do arquivo SEFIP.

**Observação 1:**

O arquivo SEFIP de versão igual ou superior a 8.2, a ser transmitido pelo aplicativo "Conectividade Social", será validado apenas se o CNPJ/CEI do Certificado for igual ao CNPJ/CEI informado no campo RESPONSÁVEL do SEFIP. Desta forma, os escritórios de contabilidade deverão informar a sua inscrição (CNPJ/CEI) no campo RESPONSÁVEL do SEFIP, sempre que transmitir o(s) arquivo(s) da(s) empresa(s) pelo aplicativo "Conectividade Social". Caso o arquivo SEFIP seja transmitido pela empresa, o campo RESPONSÁVEL deverá ser preenchido com a inscrição (CNPJ/CEI) da empresa.

**Observação 2:**

O registro 0 (zero) do arquivo consolidado é gerado a partir do registro 0 (zero) da coligada corrente. Todas as coligadas que irão fazer parte do mesmo arquivo consolidado devem possuir os mesmos dados de responsável. **Pasta Contato** Informe o nome do Contato, Endereço Internet e DDD e Telefone.

**Arquivo SEFIP.RE - SEFIP**

Nesta pasta deverão ser informadas as opções para geração do arquivo SEFIP.RE (localização, consolidação, etc).

**Pasta Localização do(s) Arquivos** **Salvar o(s) arquivos na pasta:**

Selecionar a pasta para informar o local de geração do(s) arquivo(s) SEFIP.

**Abrir pasta ao final do processo**

Ao marcar a opção, será aberta a pasta em que foi gerado o(s) arquivo(s).

**P****asta Opções de geração de arquivo**

Selecione neste campo tipo de arquivo a ser gerado.

**Tipo de geração** **Gerar um único arquivo consolidado**

Ao selecionar esta opção, será gerado o SEFIP de várias coligadas em um único arquivo consolidado. Com este parâmetro marcado o sistema gerará um arquivo SEFIPXX.RE da coligada corrente em uma pasta para posterior consolidação dos dados em um arquivo único. Quando este parâmetro for marcado o campo "Salvar o(s) arquivo(s) na pasta" terá a informação do caminho e o nome do arquivo que será gerado para o arquivo a ser consolidado, sendo que cada arquivo terá um nome distinto antes da consolidação. Caso este caminho não seja alterado será criada uma pasta no diretório onde está o executável do sistema para armazenar os arquivos a serem consolidados.

**Atenção:**

1 - Se for gerar o arquivo em outro caminho deverá criar a pasta com o nome SEFIP.

**Exemplo:**

Gerando no diretório C:\ deverá ficar da seguinte maneira - C:\SEFIP\SEFIP.RE 2 – O nome do arquivo gerado para consolidação virá com o número da coligada. Este nome somente poderá conter número para distinção entre eles. O nome do arquivo gerado para uma coligada deve sempre ser diferente de outra para não sobrepor o arquivo.

**Exemplo:**

Coligada 1 – será gerado o arquivo SEFIP1.RE

**Atenção:**

Este recurso somente poderá ser utilizado por empresa que não utilizam seções identificadas por CEI.

**Gerar arquivo(s) exclusivo(s) por cada coligada**

Ao selecionar esta opção, será gerado o SEFIP de cada coligada separadamente.

**Exemplo:**

Gerando no diretório C:\ deverá ficar da seguinte maneira - C:\Coligadax\SEFIP.RE

**Gerar funcionários administrativos**

Neste campo, deverá ser marcado se deseja ou não, gerar o arquivo SEFIP como os funcionários administrativos.

**Exemplo:**

Se um funcionário trabalhou na Empresa "Construtora X" em alguma obra civil "Tomador 1" por 10 dias e este mesmo funcionário trabalhou na limpeza "Tomador 2" por 15 dias, então o usuário deve marcar o campo para gerar os administrativos.

**Atenção:** Maiores informações sobre a geração dos funcionários administrativos, consulte o manual do SEFIP.

**Gerar endereço de todos os funcionários**

Marque este campo caso queira emitir o endereço de todos os funcionários no arquivo de SEFIP(campo auto explicativo).

**Atenção:**

Endereço de todos os funcionários (Para indicar que as empresas querem gerar o endereço de todos os funcionários dentro do arquivo do SEFIP). Categorias permitidas: 01, 02, 03, 04, 05, 06, 07, 11 e 12. 01 - Para as demais categorias não há registro tipo 14. 02 - Não será informado para a competência 13. 03 - Só deve existir um registro tipo 14 por trabalhador (PIS + Data de Admissão + Categoria + Empresa). 04 - Não será informado os códigos de recolhimento 130, 150, 155, 317, 337 e 608 se houver somente informação de endereço no arquivo.

**Seleção de Coligadas -****SEFIP**

Nesta tela deverá ser realizada a seleção das coligadas para geração do arquivo. Será apresentada uma grade com as informações de Código de Coligada, Nome /Razão Social, CNPJ/CEI/CPF.

**Selecionar Todas Coligadas**

Clique para selecionar todas as coligadas disponíveis na grade.

**Cancelar Seleção de Coligadas**

Clique para cancelar a seleção das coligadas disponíveis na grade.

**Adicionar Parâmetros Específicos**

Clique em adicionar parâmetros à coligada para definir parâmetros específicos à coligada na geração do arquivo SEFIP.

**Seleção de Coligadas - SEFIP - Geral** **Campos** **Usar Parâmetros Específicos**

Ao marcar a opção, serão habilitados os demais campos da tela. PS. Se desmarcado, considera todos os funcionários da coligada em questão e utiliza Origem da Movimentação do Funcionário por Ficha Financeira.

**Observação****:**

Somente se este parâmetro estiver marcado, a parametrização determinada nesta, e nas demais pastas existentes nessa janela, será considerada na geração do relatório da SEFIP para a coligada selecionada.

**Seleção de funcionários**

Ao clicar no botão de Seleção de funcionários o sistema abrirá uma janela com os campos onde você poderá selecionar um funcionário digitando sua chapa ou localizando seu nome, fazer a seleção de funcionários pela situação, tipo de funcionário e recebimento ou ainda criar Filtros ou Fórmulas de Seleção.

**Quebra de Seção**

Este campo deve ser utilizado para selecionar o grupo de funcionários pela seção que está cadastrado. Podendo ser informado o código de quebra da seção, quebra padrão, quebra por CNPJ (por Coligada) ou quebra por CEI.

**Recolhimento Centralizado**

Marque este campo caso queira emitir o SEFIP centralizado (campo auto-explicativo).

**Atenção:**

Código de Centralização (Para indicar as empresas que centralizam o recolhimento do FGTS em um único CNPJ) 01 - Só poderá ser 0 (não centraliza), 1 (centralizadora) ou 2 (centralizada). 02 - Deve ser igual a zero (0), para os códigos de recolhimento 130, 135, 150, 155, 211, 317, 337, 608 e para empregador doméstico (FPAS 868). 03 - Quando existir empresa centralizadora deve existir, no mínimo, uma empresa centralizada e vice-versa. 04 - Quando existir centralização, as oito primeiras posições do CNPJ da centralizadora e da centralizada devem ser iguais. 05 - Empresa com inscrição CEI não possui centralização.

**CNPJ Centralizador**

Deverá ser informado o CNPJ da Seção centralizadora.

**CNAE-Preponderante**

Informe o CNAE Preponderante.

**A****tenção:**

O sistema irá fazer um mapeamento com o valor informado nesse campo e o valor do CNAE no cadastro de seção. Caso o CNAE da seção seja o mesmo informado no SEFIP será considerado que ele é preponderante. Para os códigos de Recolhimento 145, 307, 317, 327, 337, 345, e 660 e competências até 05/2008 será considerado apenas o campo "Alterou CNAE". Caso contrário será preenchido com: S se desejar alterar o CNAE e não for preponderante. N se não desejar alterar e não for preponderante. A se desejar alterar e for CNAE preponderante. P se não desejar alterar e for CNAE preponderante.

**Prazos de Recolhimento** **Recolhimento do FGTS**

Deverá ser utilizado para identificar se o recolhimento do FGTS será realizado até o dia sete do mês seguinte ao da competência - no prazo ou será feito após esta data em atraso. **Data Recolhimento FGTS** Indique se a data efetiva de recolhimento de FGTS, sempre que o recolhimento for realizado em atraso.

**Observação:**

Os campos Código de Recolhimento e Indicador de Recolhimento de FGTS determinam a obrigatoriedade desta data

**Data Recolhimento da Previdência**

Indique a data efetiva de recolhimento do INSS sempre que o recolhimento foi realizado em atraso.

**Gerar funcionários administrativos**

Neste campo, deverá ser marcado se deseja ou não, gerar o arquivo SEFIP como os funcionários administrativos.

**Exemplo:**

Se um funcionário trabalhou na Empresa "Construtora X" em alguma obra civil "Tomador 1" por 10 dias e este mesmo funcionário trabalhou na limpeza "Tomador 2" por 15 dias, então o usuário deve marcar o campo para gerar os administrativos.

**Atenção:**

Maiores informações sobre a geração dos funcionários administrativos consulte o manual do SEFIP.

**Gerar endereço de todos os funcionários**

Marque este campo caso queira emitir o endereço de todos os funcionários no arquivo de SEFIP.

**Atenção:**

Endereço de todos os funcionários (Para indicar que as empresas querem gerar o endereço de todos os funcionários dentro do arquivo do SEFIP). Categorias permitidas: 01, 02, 03, 04, 05, 06, 07, 11 e 12. 01 - Para as demais categorias não há registro tipo 14. 02 - Não será informado para a competência 13. 03 - Só deve existir um registro tipo 14 por trabalhador (PIS + Data de Admissão + Categoria + Empresa). 04 - Não será informado os códigos de recolhimento 130, 150, 155, 317, 337 e 608 se houver somente informação de endereço no arquivo.

**Atenção:**

Ao definir um campo comum a outras telas do SEFIP, o sistema irá considerar o campo definido em Parâmetros específicos da Coligada.

**Seleção de Coligadas - SEFIP – Retificação** **Retificação de valores**

Este Check Box é o que determina se o relatório do SEFIP terá caráter de retificação.

**Remuneração complementar**

Marque este parâmetro quando houver pagamento de complemento de FGTS e/ou INSS retificando um valor pago a menor em meses anteriores, inclusive referentes ao 13º salário.

**Restituição**

Marque este parâmetro quando houver restituição de valores de FGTS e/ou INSS retificando um valor pago a maior em meses anteriores, inclusive referentes ao 13º salário.

**Origem dos eventos**

Informe nestes campos o Mês, Ano e Período em que os eventos criados para retificação foram lançados.

**Eventos:**

Cód. Cálculo 188 – INSS Retificação SEFIP Cód. Cálculo 189 – Retificação SEFIP Cód. Cálculo 190 – Retificação SEFIP - 13º Salário Cód. Cálculo 191 – INSS Retificação SEFIP - 13º Salário

**Seleção de eventos para Retificação de FGTS / Previdência:** **Eventos para Retificação - FOLHA**

Marque o(s) evento(s) que será (ão) informado(s) no arquivo de SEFIP para recolhimento/declaração da retificação para FGTS e INSS. Os eventos relacionados aqui têm o "Cód. Cálculo 189 – Retificação SEFIP".

**Dica**

Criar um evento para cada competência a que a retificação se referir.

**Eventos para Retificação - 13o SALÁRIO**

Marque o(s) evento(s) que será (ão) informado(s) no arquivo de SEFIP para recolhimento/declaração da retificação para FGTS13 e INSS13. Os eventos relacionados aqui têm o "Cód. Cálculo 190 – Retificação SEFIP – 13º Salário". **Dica** Criar um evento para cada competência a que a retificação se referir.

**Seleção de Coligadas - SEFIP – Integrações**

Para melhor entendimento do processo aqui descrito, é importante definir se o sistema do qual serão aproveitados dados, na geração do arquivo SEFIP.RE, é um sistema da Linha RM ou não. Clique nas opções abaixo de acordo com o sistema que irá utilizar.

**RM Corpore** **Importar autônomos do RM Fluxus / RM Nucleus**

Através deste parâmetro será informado no arquivo SEFIP.RE os autônomos e seus valores cadastrados no RM Fluxus. Os valores serão informados de acordo com: o tipo de documento no RM Fluxus que deve ser "Gerador de INSS", a data de vencimento do lançamento e o mês de competência do RM Labore. Para que seja considerada a data de emissão do lançamento para informação dos dados no arquivo SEFIP.RE, será necessário marcar o parâmetro "Considerar data de emissão em vez de data de vencimento" em Opções | Parâmetros | RM Labore | Outros Parâmetros | Parâmetros I.

**Observação 1:**

Os dados de número do contribuinte individual, categoria, CBO, ocorrência e Data de Inicio das Atividades deverão estar cadastrados corretamente no RM Fluxus para que possam ser informados no arquivo SEFIP.RE. Cadastrar em Cliente/Fornecedor do RM Fluxus os dados das pastas Cadastros | Cliente/Fornecedores | Impostos/Tributos | Dados relacionados ao INSS e Cadastros | Cliente/Fornecedores | Outros Dados campo Data de inicio das Atividades.

**Observação 2:**

O campo Data de Inicio das Atividades NÃO deve ser informado caso a categoria seja diferente de 01, 03,04,05,06,07,11,12,19,20,21 e 26.

**Observação 3:**

Caso o SEFIP seja gerado com tomadores de serviços a data de emissão ou a data de vencimento que será considerada para autônomos do RM Fluxus deverá ser com a mesma competência da distribuição por tomadores.

**Observação4:**

A ocorrência será cadastrada como número, mas no arquivo SEFIP.RE será informado o valor formatado para validação.

**Importar valores de retenção RM Nucleus (Lei 9711/98)**

Marcando esse parâmetro o sistema irá considerar o valor de retenção (sobre NF) para cálculo da Guia do INSS.

**Observação 1:**

Conforme recomendações do validador do SEFIP os campos "Remuneração" e "Valor descontado do Segurado" deve seguir a seguinte forma: Remuneração e Valor descontado do Segurando: Se informado deve ter 2 casas decimais válidas. Remuneração: Preencher o campo com zeros a esquerda e no máximo 13 dígitos de valor. Valor descontado do Segurando: Preencher o campo com zeros à esquerda e no máximo com 12 dígitos de valor.

**Observação 2:**

As casas decimais do item acima serão consideradas como os dois últimos dígitos informados no arquivo e NÃO devem conter ponto ou vírgula.

**Observação 3:**

O campo Data de Inicio Atividade NÃO deve ser informado caso a categoria seja diferente de 01,03,04,05,06,07,11,12,19,20,21 e 26.

**Observação 4:**

O campo Data de Inicio Atividade deve conter as barras " / " dentro do arquivo para importação.

**Observação 5:**

O campo Valor descontado do Segurado somente será importado caso a ocorrência seja de múltiplos vínculos.

**Observação 6:**

O campo Inscrição do Tomador de Serviços poderá ser preenchido com espaços em branco ou zeros (0).

**Observação 7:**

Para importar o arquivo que contém CEI que tem 12 dígitos, os dois dígitos faltantes devem ser completados com espaço (tanto faz no início ou no fim do número). O mesmo deve ocorrer com CPF que tem 11 dígitos.

**Exemplo de geração de guia de INSS com autônomo não cadastrado no sistema**

Segue um exemplo de quando não há registro de autônomo com categoria 15 no sistema para geração de GPS em Relatórios | Guia de INSS e em Relatórios | SEFIP:

**Guia de INSS**

Em Cadastros | Seções | Dados para INSS - Campo "Remun.autônomos cat. 15 não cadastrados" colocar 1000,00 Em Relatórios | Guia de INSS - Gerar guia de INSS para um funcionário ativo qualquer, acrescentar no campo "Aut. não cadastrados" na pasta Valores da Seção 1000,00 e acrescentar no campo "INSS aut.(M.P 83)" na pasta Valores da Seção 110,00.

**SEFIP**

Em Relatórios | SEFIP - Gerar SEFIP para o mesmo filtro da guia de INSS, marcar na pasta Integrações o parâmetro "Importa arq.Autônomos (Outros Sistemas)" informando o caminho com um arquivo txt com os seguintes dados (conforme layout para importação de autônomos que se encontra no help desta pasta): 21867387000158 1309905977215JOAO JOSE DA SILVA 0223700000000010000005000000000011000 Validar o SEFIP, comparar as guias de INSS gerada pelo sistema e pelo SEFIP.

**Importar valores de retenção de outro Sistema (Lei 9711/98)**

Este parâmetro serve para incluir no arquivo do SEFIP.RE o valor de retenção para que sejam feitos os devidos cálculos. Estes valores serão importados no momento do cálculo do SEFIP e poderão ser editados em Relatórios | SEFIP | Centralizadores | Pasta Valores II campo "Valor de Retenção (Lei 9711/98)". Ao clicar neste parâmetro será apresentado um campo para preencher com a localização e nome do arquivo de autônomos a ser importado. Acessa o diretório onde está localizado o arquivo. Tendo preenchido o campo e existindo o arquivo, será disponibilizado o seguinte botão: Abre arquivo gerado para visualização.

**Layout para importação de retenções de tomadores**

DESCRIÇÃO                                      INI    FIM    TAM    TIPO          MÁSCARA

Inscrição da Empresa                       001    014    14    Numérico    99999999999999

Inscrição do Tomador de Serviço    015    028    14    Numérico     99999999999999

Valor da Retenção                           029    043    15    Numérico     999999999999

**Observação 1:**

No arquivo não pode haver ponto (.) ou vírgula (,). Os dois últimos dígitos do valor de retenção serão considerados como casas decimais.

**Observação 2:**

O SEFIP não aceita valor com mais de 12 dígitos.

**Observação 3:**

Para importar o arquivo que contém CEI que tem 12 dígitos, os dois dígitos faltantes devem ser completados com espaço (tanto faz no início ou no fim do número). O mesmo deve ocorrer com CPF que tem 11 dígitos.

**Outros Sistemas** **Importar autônomos de outro Sistema**

Este parâmetro serve para incluir no arquivo do SEFIP.RE uma relação de autônomos para que sejam feitos os devidos cálculos. Ao clicar neste parâmetro será apresentado um campo para preencher com a localização e nome do arquivo de autônomos a ser importado.

**O layout do arquivo é o seguinte:**

DESCRIÇAO                 INI    FIM    TAM    TIPO        MÁSCARA Inscrição da Empresa                001    014    14    Numérico    99999999999999 Inscrição do Tomador de Serviço        015    028    14    Numérico    99999999999999 CI do Autônomo                029    039    11    Numérico    99999999999 Categoria do Trabalhador        040    041    02    Numérico    99 Nome do Trabalhador            042    111    70    Alfa Numérico CBO                    112    116    05    Alfa Numérico Remuneração                117    131    15    Numérico    00999999999999 Ocorrência                132    133    02    Numérico    99 Valor descontado do Segurado        134    148    15    Numérico    000999999999999 Data de Início Atividade        149    158    10    Alfa Numérico    DDMMAAAA

**Observação 1:**

Conforme recomendações do validador do SEFIP os campos "Remuneração" e "Valor descontado do Segurado" deve seguir a seguinte forma: Remuneração e Valor descontado do Segurando: Se informado deve ter 2 casas decimais válidas. Remuneração: Preencher o campo com zeros a esquerda e no máximo 13 dígitos de valor. Valor descontado do Segurando: Preencher o campo com zeros à esquerda e no máximo com 12 dígitos de valor.

**Observação 2:**

As casas decimais do item acima serão consideradas como os dois últimos dígitos informados no arquivo e NÃO devem conter ponto ou vírgula.

**Observação 3:**

O campo Data de Inicio Atividade NÃO deve ser informado caso a categoria seja diferente de 01,03,04,05,06,07,11,12,19,20,21 e 26.

**Observação 4:**

O campo Data de Inicio Atividade deve conter as barras " / " dentro do arquivo para importação.

**Observação 5:**

O campo Valor descontado do Segurado somente será importado caso a ocorrência seja de múltiplos vínculos.

**Observação 6:**

O campo Inscrição do Tomador de Serviços poderá ser preenchido com espaços em branco ou zeros (0).

**Observação 7:**

Para importar o arquivo que contém CEI que tem 12 dígitos, os dois dígitos faltantes devem ser completados com espaço (tanto faz no início ou no fim do número). O mesmo deve ocorrer com CPF que tem 11 dígitos.

**Exemplo de geração de guia de INSS com autônomo não cadastrado no sistema**

Segue um exemplo de quando não há registro de autônomo com categoria 15 no sistema para geração de GPS em Relatórios | Guia de INSS e em Relatórios | SEFIP:

**Guia de INSS**

Em Cadastros | Seções | Dados para INSS - Campo "Remun.autônomos cat. 15 não cadastrados" colocar 1000,00 Em Relatórios | Guia de INSS - Gerar guia de INSS para um funcionário ativo qualquer, acrescentar no campo "Aut. não cadastrados" na pasta Valores da Seção 1000,00 e acrescentar no campo "INSS aut.(M.P 83)" na pasta Valores da Seção 110,00.

**SEFIP**

Em Relatórios | SEFIP - Gerar SEFIP para o mesmo filtro da guia de INSS, marcar na pasta Integrações o parâmetro "Importa arq.Autônomos (Outros Sistemas)" informando o caminho com um arquivo txt com os seguintes dados (conforme layout para importação de autônomos que se encontra no help desta pasta): 21867387000158 1309905977215JOAO JOSE DA SILVA 0223700000000010000005000000000011000 Validar o SEFIP, comparar as guias de INSS gerada pelo sistema e pelo SEFIP.

**Importar valores de retenção de outro Sistema (Lei 9711/98)**

Este parâmetro serve para incluir no arquivo do SEFIP.RE o valor de retenção para que sejam feitos os devidos cálculos. Estes valores serão importados no momento do cálculo do SEFIP e poderão ser editados em Relatórios | SEFIP | Centralizadores | Pasta Valores II campo "Valor de Retenção (Lei 9711/98)". Ao clicar neste parâmetro será apresentado um campo para preencher com a localização e nome do arquivo de autônomos a ser importado. Acessa o diretório onde está localizado o arquivo. Tendo preenchido o campo e existindo o arquivo, será disponibilizado o seguinte botão: Abre arquivo gerado para visualização.

**Layout para importação de retenções de tomadores**

DESCRIÇÃO            INI    FIM    TAM    TIPO        MÁSCARA Inscrição da Empresa        001    014    14    Numérico    99999999999999 Inscrição do Tomador de Serviço    015    028    14    Numérico    99999999999999 Valor da Retenção        029    043    15    Numérico    999999999999

**Observação 1:**

No arquivo não pode haver ponto (.) ou vírgula (,). Os dois últimos dígitos do valor de retenção serão considerados como casas decimais.

**Observação 2:**

O SEFIP não aceita valor com mais de 12 dígitos.

**Observação 3:**

Para importar o arquivo que contém CEI que tem 12 dígitos, os dois dígitos faltantes devem ser completados com espaço (tanto faz no início ou no fim do número). O mesmo deve ocorrer com CPF que tem 11 dígitos.

**Importar autônomos externos (integrados de outros BackOffices)**

Deverá ser marcado a opção para que seja levado na geração do arquivo SEFIP.RE os autônomos externos importados através da Importação de Dados Folha de Pagamento ou via comunicação Web Services. Esses dados serão inseridos na tabela PPAGTOAUTONOMOEXT e poderam ser visualizados em **RH | Folha de Pagamento | Encargos | Autônomos | Autônomos Externos**.

**Observação 1:**

Na geração do arquivo SEFIP.RE será calculado o valor de 20% (vinte por cento) sobre o valor do campo 'valor da remuneração' para ser levado como base de cálculo de INSS, para os autônomos carreteiros com a categoria 15 e CBO 782510.

**Observação 2:**

Na geração do arquivo SEFIP.RE será somado os valores do campo 'valor da remuneração' nos registros de autônomos que tenham os campos CODFILIAL, CNPJTOMADOR, CEITOMADOR, NROINSCRICAO, CATAUTONOMO, DATAINIATIVIDADE iguais na tabela PPAGTOAUTONOMOEXT.

**Seleção de Coligadas - SEFIP - Dissídio** **Dissídio/ Acordo coletivo** **Data do dissídio**

Ao escolher gerar o SEFIP nos códigos de recolhimento 650 e 660, será disponibilizado o campo "Data do dissídio", que o usuário deve informar com a data de início do cálculo da diferença salarial e esta informação será levada para o arquivo do SEFIP no campo destinado à informação do "mês e ano de início do pleito da Reclamatória Trabalhista/Dissídio Coletivo".

**Retroativo a**

Indique o mês e o ano para gerar a movimentação no arquivo de informações à previdência conforme o código de recolhimento 650 e 660, esta informação deve ser apresentada mês a mês conforme orientação do SEFIP.

**Incluir Reclamatória Trabalhista - CC202**

Através deste campo, poderá ser incluído o valor do evento CC202 - Reclamatória Trabalhista na geração do arquivo SEFIP.RE. (Código de Recolhimento 650).

**Considerar competência do dissídio no registro do responsável**

Ao marcar este parâmetro ao gerar o arquivo sefip.re com o código de recolhimento 650 o campo COMPETÊNCIA do registro 00 será preenchido com o mês e ano da competência referente ao dissídio.

**Observação 1:**

O Evento "Reclamatória Trabalhista" (CC202) deverá ser informado no envelope do(s) funcionário (s).

**Observação 2:**

Deverá ser informado o mês e ano em que estiver lançado o evento para o(s) funcionário(s).

**Gerar arquivo consolidado para Dissídio Coletivo\Reclamatória Trabalhista**  
   
Este parâmetro busca os valores consolidados de dissídio. Se o parâmetro estiver marcado, os valores serão buscados do

**Envelope**

referente ao mês informado no campo 'Competência' do sefip. Caso contrário, os valores serão buscados da

**Ficha financeira | aba Verbas Geradas por Diferença**

do mês informado no campo 'Diferença referente ao mês' da aba 'Parâm. Cálculo'.  
   
**Seleção de coligadas- Sefip \Lançamento Financeiro**   
   
**-Gerar Lançamentos Financeiros**  
Selecionar o tipo de lançamento financeiro do Sefip, já parametrizado em Encargos |Financeiro| Cadastros Financeiros | Parâmetros.  
São visualizados os lançamentos com o tipo:   
15- FGTS conforme SEFIP  
   
**-Gerar Lanctos por centro de custo**  
Este parâmetro somente ficará visível se no parametrizador Folha normal/Calculo/"Utiliza Calculo Por Centro de Custo"  estiver MARCADO e/ou a opção por ratear por centro de custo esteja diferente de "Obrigatória" no Fluxus.  
  Através deste parâmetro será feito o rateio do lançamento financeiro por centro de custo ,buscando o do rateio fixo do cadastro do  funcionário.   
   
**-Gerar lanctos rateados pelo Centro de custo da seção do funcionário**   
 Este parâmetro somente ficará visível se no parametrizador Folha normal/Calculo/"Utiliza Calculo Por Centro de Custo"  estiver DESMARCADO.  
 Através deste parâmetro será feito o rateio do lançamento financeiro por centro de custo ,buscando ao invés do rateio fixo do funcionário o centro de custo cadastrado na seção do funcionário aba Dados Contábeis.  
   
**Observação 1:**   
Quando mais de um funcionário tiver o mesmo tomador cadastrado  os valores serão somados e  gerados os rateios por centro de custo para aquele lançamento. Os rateios podem ser conferidos no menu Lançamento financeiro / Edição /Dados Adicionais / rateio.   
   
           **Observação 2 :**  
Quando a seção do funcionário não tiver cadastrado o centro de custo o sistema emitira uma mensagem informando que a seção está sem Centro de custo   
          **Exemplo:** Os lançamentos financeiros não foram gerados devido o seguintes motivos :  
             A seção COM\_DEP Comercial não possui centro de custo cadastrado .   
   
   
**Parâmetros do SEFIP .Net**

Através deste módulo é possível parametrizar a geração do SEFIP informando a competência, o código de recolhimento, a seção e os tomadores quando aplicável.

**Passo a Passo** 1.

Informe a Competência de geração (mês e ano) 2. Informe o Código de Recolhimento –SEFIP 3. Clique em Inicializar todas as Seções no SEFIP 4. Clique em Inicializar todos os Tomadores no SEFIP (quando aplicável)

**Observação**

Também é possível incluir as seções individualmente através do ícone incluir da barra de ferramentas. Através do cadastro é possível controlar:

**Identificação - Parâmetros do SEFIP .Net**

Esta tela permite visualizar os parâmetros de geração como Competência, Cód Recolhimento, Cód Seção.

**I****nicializar todas as Seções no SEFIP**

Este botão carrega os dados de todas as seções que serão levadas para o SEFIP.

**Observação**

Também é possível inserir as seções individualmente através do ícone inserir na barra de ferramentas.

**Atenção 1**

01 – É OBRIGATÓRIO existir o "HISTÓRICO DE SEÇÕES" em Cadastros | Funcionários | Edição | Pasta Registro correto para a emissão do SEFIP de meses anteriores.

**Atenção 2**

Se o usuário fez alguma transferência, transferindo também a Ficha Financeira do funcionário, no período entre a competência em atraso e a atual, o arquivo será gerado com dois registros tipo 30 e não será validado pelo SEFIP. Porque no histórico da seção fica registrada a seção anterior do funcionário e a ficha financeira fica com os valores de todos os meses.Neste caso o usuário deverá acessar o histórico da seção em Cadastros | Funcionários | Edição | Pasta Registro deste funcionário, excluir seção anterior e depois cadastrá-la novamente para que o cadastro fique correto ou então deve editar o arquivo SEFIP.RE e excluir uma das linhas de registro tipo 30 duplicada.

**Atenção 3**

Se houver alguma alteração na Ficha Financeira de algum funcionário não estará garantida a integridade do arquivo do SEFIP, pois os valores entre o SEFIP emitido antes da alteração e o SEFIP emitido depois da alteração não serão iguais devido às alterações manuais feitas pelo usuário.

**Atenção 4**

Será considerado as seguintes condições para geração do SEFIP de meses anteriores, verificando o histórico de ocorrência: 1 – Para SEFIP no mês atual será considerado o registro da ocorrência em Cadastros | Funcionários | pasta FGTS/SEFIP/INSS; 2 – Para SEFIP de meses anteriores será verificado o histórico de ocorrência para a emissão do arquivo; 3 - Se não houver histórico de ocorrência será considerado o registro da ocorrência em Cadastros | Funcionários | pasta FGTS/SEFIP/INSS; 4 – Caso o primeiro registro do histórico de ocorrência for uma data posterior à admissão do funcionário e houver uma emissão do SEFIP neste período sem registro será considerada a ocorrência em branco, porque somente o registro em branco não será necessário ser registrado no histórico de ocorrência, por se tratar de uma ocorrência inicial de um funcionário e nenhum funcionário altera a ocorrência para branco.

**Atenção 5**

Filtrar a geração do SEFIP quando a competência for 13 e a categoria for diferente das categorias de trabalhador 01, 04, 05, 07, 11, 12, 19, 20 e 21 , porque admite apenas essas categorias de trabalhador.

**Observação**

01 - Para emitir SEFIP de meses anteriores com as alterações de cadastros dos funcionários feitas nos meses anteriores o usuário NÃO poderá Liberar FLAGS, porque não há histórico para FLAGs. O que ocorrerá com a não Liberação dos Flags é a emissão destas alterações para cada mês de emissão do SEFIP. 02 - Não existem históricos das alterações de informações de CATEGORIA/ TIPO DE EMPREGADO, por isso no SEFIP referente meses anteriores será considerado a informação atual do funcionário nestes campos. 03 - Para o mês em que houve lançamentos que geraram SEFIP com código de recolhimento 650 o usuário deverá emitir o SEFIP por períodos seguindo as considerações para recolhimento deste código de recolhimento '650'.

**Valores I - Parâmetros do SEFIP .Net**

Nesta pasta você poderá consultar os valores calculados pelo sistema

**Compensação:** Valor Este campo é usado para informar os valores recolhidos indevidamente ou a maior em competências anteriores que a empresa deseja compensar na atual guia de recolhimento da Previdência Social.

**Per.Início (AAAAMM)**

Este campo é destinado à informação do AAAAMM de início das competência recolhidas indevidamente ou a maior.

**Per.Fim (AAAAMM)**

Este campo é destinado à informação do AAAAMM final das competência recolhidas indevidamente ou a maior.

**Recolhimento de Competências Anteriores** **Valor INSS Folha de Pagam.**

Informe neste campo o valor sobre folha de pagamento de competências anteriores não recolhidas por possuírem valor menor que R$ 25,00 (o valor do campo 6 da GPS).

**Outras Ent. Folha de Pagamento**

Informe neste campo o valor de outras entidades sobre folha de pagamento de competências anteriores não recolhidas por possuírem valor menor que R$ 25,00 (o valor do campo 9 da GPS).

**Receita de Evento Valor de INSS**

Informe neste campo o valor sobre folha de pagamento de competências anteriores não recolhidas por possuírem valor menor que R$ 25,00 (o valor do campo 6 da GPS de código de pagamento 2500).

**C****om. Prod. Rural Valor de INSS**

Informe neste campo o valor sobre folha de pagamento de competências anteriores não recolhidas por possuírem valor menor que R$ 25,00 (o valor do campo 6 da GPS de código de pagamento 2607 ou 2704).

**Com. Prod. Rural Outras Ent.**

Informe neste campo o valor de outras entidades sobre folha de pagamento de competências anteriores não recolhidas por possuírem valor menor que R$ 25,00 (o valor do campo 9 da GPS de código de pagamento 2607 ou 2704).

**Informações de Processo** **Processo**

Informe o número Processo para ser informado no arquivo SEFIP.RE. Este campo aceita somente 11 caracteres.

**Ano do Processo**

Informe o Ano do Processo para ser informado no arquivo SEFIP.RE.

**Vara/JCJ do Processo**

Informe a Vara/JCJ do Processo para ser informado no arquivo SEFIP.RE.

**Período Inicio**

Será apresentado os dados do campo Mês/Ano do Arquivo para que seja declarado no arquivo de SEFIP.RE o mês de informação dos valores de dissídio.

**Período Fim**

Será apresentado os dados do campo Mês/Ano do Arquivo para que seja declarado no arquivo de SEFIP.RE o mês de informação dos valores de dissídio.

**Valores II - Parâmetros do SEFIP .Net**

Nesta pasta é possível editar e visualizar os seguintes campos:

**Outros Valores** **Total Salário Família**

Este campo informa o total de Salário Família pago para os funcionários daquela seção.

**Ded.13º salário. Lic.Maternidade**

Este campo é utilizado para informações do valor do 13° salário proporcional ao período de licença-maternidade (para afastamentos iniciados até 30/11/99, inclusive), contado dia-a-dia, a cargo da Previdência Social, nos seguintes casos: Na competência 13, referente ao valor pago durante o ano; Em qualquer competência, quando houver rescisão de contrato de trabalho, aposentadoria sem continuidade de vínculo ou falecimento.

**Receita Ev.Desportivo/Pat.**

Informe neste campo o valor total da receita bruta de espetáculos desportivos em qualquer modalidade, bem como os valores pagos a título de contrato e patrocínio, licenciamento de marcas e símbolos, publicidade, transmissão de espetáculos celebrados com qualquer associação desportiva que mantenha clube de futebol profissional.

**Salário Maternidade**

O sistema calculará o valor pago pela empresa a título de salário maternidade iniciada até 30/11/1999 no mês em seqüência que será deduzida na GPS.

**Com.Produção Rural PJ**

Este parâmetro informa o valor da comercialização da produção rural realizada no mês de competência por produtor rural pessoa jurídica.

**Observação**

Destinado a descrição das receitas de Evento Desportivo/Patrocínio e produção rural comercializada no mês, nos termos exigidos pelo INSS. A informação prestada neste campo será impressa na GRPS.

**Ind.Origem Receita**

Utilize este campo para indicar a origem da Receita do Evento Desportivo/Patrocínio.

**Com.Produção Rural PF**

Este parâmetro informa o valor da comercialização da produção rural realizada no mês de competência por produtor rural pessoa física.

**Valor Cooperativas**

Informe neste campo o montante da base de cálculo da contribuição previdenciária referentes aos valores pagos à cooperativas de trabalho. Este valor deve ser informado no tipo de registro 10.

**Anexo****s - Parâmetros do SEFIP .Net**

Através deste módulo é possível controlar os seguintes anexos: Neste anexo é possível controlar: Parâmetros Tomadores de Serviço Neste anexo é possível controlar:

**Inicializar todos os tomadores do SEFIP**

Este botão carrega os dados de todos os tomadores de serviço das seções.

**Observação**

Também é possível inserir os tomadores individualmente através do ícone inserir na barra de ferramentas deste anexo.

**I****dentificação** **Código Tomador**

Nesta tela é possível que o usuário informe o tomador de serviço.

**Valores** **Compensação** **Valor**

Este campo é usado para informar os valores recolhidos indevidamente ou a maior em competências anteriores que a empresa deseja compensar na atual guia de recolhimento da Previdência Social.

**Per.Início (AAAAMM)**

Este campo é destinado à informação do AAAAMM de início das competência recolhidas indevidamente ou a maior.

**Per.Fim (AAAAMM)**

Este campo é destinado à informação do AAAAMM final das competência recolhidas indevidamente ou a maior.

**Outros Valores**

Valor de Retenção (Lei 9711/98) Informe a soma o valor da retenção de 11%, valor que será compensado na GPS

**Total Salário Família**

Este campo informa o total de Salário Família pago para os funcionários daquela seção.

**Valor de faturas emitidas para o tomador**

Informe neste campo o montante do valor das faturas emitidas para cada tomador. Este valor deve ser informado no tipo de registro 20.
