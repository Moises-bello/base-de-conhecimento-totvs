---
content_hash: 91c845fd34b195701177373e021f64cdd487256fd7c7dd8e6e17eb251aa7a5d9
fetched_at: '2026-06-29T00:10:04.128184+00:00'
page_id: '452719200'
product: rm
source: tdn-rm
title: Configuração da Chapa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719200
version: 7
---

Etapa utilizada para configurar a chapa do funcionário

**Campos e Parâmetros**  
Tamanho  
Campo onde é informado a quantidade de caracteres da chapa do funcionário, permitido até 16 caracteres e não podendo ser 0 (zero). Se houver necessidade da empresa aumentar o número de dígitos, as chapas dos funcionários já cadastrados não serão influenciados.   
   
Máscara para a chapa  
Campo onde é definido os tipos que irão compor mascara da chapa do funcionário. Quando é inserido um novo funcionário no sistema é feita a consistência da chapa cadastrada com a máscara definida. A máscara é formada pelos caracteres abaixo:

* #: para campo numérico.
* L: para campo alfabético e de preenchimento obrigatório.
* I: para campo alfabético e de preenchimento facultativo.
* A: para campo alfanumérico e que os dígitos devem ser preenchidos obrigatoriamente.
* a: para campo alfanumérico, podendo ser digitados letras e números.
* Q: Para qualquer caractere, menos os separadores (: . , ; /)

**Observação**  
Para este campo pode ser informado a combinação dos caracteres acima, desde que não ultrapasse a quantidade informada no campo tamanho.  
Também é permitido informar o separador '.' no formato da mascara sendo este contado como um caractere.   
A Máscara da Chapa é obrigatória.  
   
**Exemplo**  
Se a máscara de um código for L#.##, o código poderá ser A1.01, sendo que se digitado a11, o sistema passará a "a" (minúscula) para "A" (maiúscula) e preencherá as outras casas com "0".

Dígito Verificador  
O dígito verificador é utilizado para consistir a chapa do funcionário conforme padrões definidos para ela:

* *Não utiliza o dígito verificador para Chapa*: esta opção indica que a empresa não utiliza o dígito verificador no código da chapa.
* *Somente valida o dígito verificador para Chapa:* marcando esta opção é habilitado o campo 'Fórmula p/ cálculo do dígito verificador' e valida o dígito verificador através de fórmula informada no respectivo campo, no momento da digitação de da chapa no cadastro de funcionários.
* *Gera o dígito verificador para Chapa:* marcando esta opção é habilitado o campo  'Fórmula p/ cálculo do dígito verificador' e gera o dígito verificador através de fórmula informada no respectivo campo, ao finalizar o cadastro de funcionário.

**Observações**  
Para validar ou gerar o dígito verificador, a chapa deve conter somente números.  
O ultimo número da chapa deverá ser o dígito verificador, conforme o exemplo: Chapa com 5 números: NNNND, onde N são os números da chapa e D o dígito verificador.

Fórmula p/ Cálculo do digito verificador  
Este campo é habilitado quando é selecionado o parâmetro 'Somente valida o dígito verificador para Chapa' ou 'Gera dígito verificador para chapa', onde o usuário irá informar um fórmula para cálculo do dígito.

**Exemplo de fórmula para Dígito verificador**  
DECL Soma, Tamanho, Multiplicador;  
SETVAR (Tamanho, TAMSTR(CHAPA)-1); /\* Tamanho recebe o total de dígitos da CHAPA \*/  
SETVAR (Multiplicador, 2); /\* Primeiro multiplicador será 2 \*/  
   
REPITA  
SETVAR (Soma , Soma + (VAL (SUBSTR(CHAPA, Tamanho,1)) \* Multiplicador)); /\* Somará a cada multiplicação \*/  
SETVAR (Multiplicador, Multiplicador + 1); /\* Multiplicação por 2, por 3, por 4, etc \*/  
SETVAR (Tamanho, Tamanho-1)  
ATE Tamanho = 0; /\* Até que não exista mais nenhum número da CHAPA para ser multiplicado \*/  
   
SOMA%10 /\* Resto da divisão por 10 será o dígito verificador \*/

Completar Chapa com zeros à esquerda automaticamente  
Habilitando este parâmetro o sistema irá complementar com zeros à esquerda a chapa digitada, completando o número de dígitos que falta conforme a máscara informada. Não habilitando este parâmetro, o usuário deverá digitar os zeros a esquerda conforme o cadastro de máscara da chapa.   
   
Cadastro automático de chapas sequenciais (exclusivamente numéricas, onde o valor da chapa seja menor que 2147483647)  
Este parâmetro só fica habilitado se o campo máscara for definido todo numérico. Ao marcar este parâmetro, o campo chapa no cadastro de funcionário fica desabilitado para edição na inclusão de um novo funcionário. A chapa é preenchida obedecendo um controle sequencial, automaticamente e individual por coligada, ou seja, cada coligada terá uma sequencia de chapas independente.

**Observação**  
O usuário poderá marcar este parâmetro a qualquer momento, mesmo que já tenha funcionários cadastrados na base. Porém deve ficar atento, pois marcando este parâmetro, caso exista algum funcionário com alguma chapa que faça parte da sequencia que está sendo seguida, pode retornar erro de chave duplicada.   
É recomendado usar esse parâmetro somente se todas as chapas da base estiverem em formato número. Uma mensagem de informação é retornada para o usuário no momento que o mesmo marca este parâmetro.  
Usando este parâmetro só é permitido cadastrar funcionários até atingir o código de chapa de número 2147483647.  
Caso o usuário deseje que a configuração de máscaras seja diferente de numéricas, o sistema desabilitará este parâmetro e os parâmetros filhos deste automaticamente.

Utiliza sequencial global  
Ao marcar o parâmetro para utilizar sequencial global, será feito um controle sequencial global, ou seja, não será feito um controle de sequencia das chapas independente, por coligada.

**Veja também** [DT\_Chapa Sequencial Global](https://tdn.totvs.com.br/display/LRM/DT_Chapa+Sequencial+Global)

**Observação**  
Este parâmetro só fica habilitado quando é marcado o parâmetro 'Cadastro automático de chapas sequenciais (exclusivamente numéricas, onde o valor da chapa seja menor que 2147483647)'.   
Marcando este parâmetro, o parâmetro 'Utiliza máscara no prefixo da chapa fica desabilitado.

Utiliza máscara no prefixo da Chapa  
Este parâmetro permite definir uma mascara no prefixo da chapa. Marcando este parâmetro é habilitado o campo 'Máscara prefixo da chapa', onde o usuário define se prefixo será composta pelo código da coliga ou filial.

**Observação**  
Este parâmetro só fica habilitado quando é marcado o parâmetro 'Cadastro automático de chapas sequenciais (exclusivamente numéricas, onde o valor da chapa seja menor que 2147483647)'.  
O campo 'Mascara prefixo chapa' deve ser informado ou caracteres, em maiúsculo' 'C' e/ou 'F', onde 'C' retorna o código da coligada e 'F' o código da Filial.   
   
**Exemplo**  
Coligada = 8  
Filial = 9  
tamanho da mascara  = 6  
Informo no campo 'Máscara prefixo chapa' = CF  
Ao cadastrar o funcionário o campo chapa ficará '890001'

Incrementar 4 dígitos de controle no final da chapa dos demitidos  
Este parâmetro somente ficará habilitado quando o campo "Tamanho" for menor ou igual 12, devido ao limite deste campo ser de 16 dígitos e o sistema auto incrementar a sequência das transferências com 4 dígitos.  
Esta sequência será no final da chapa do funcionário transferido (situação D) e iniciará sempre com "T" (transferido).  
   
**Exemplo:**   
O campo "Tamanho" está definido com 12 dígitos. A chapa do funcionário a ser transferida é 000100500123.  
Ao transferir o funcionário a chapa do funcionário transferido (situação D) será 000100500123T001, e do ativo continua sendo 000100500123.  
Caso o funcionário seja transferido pela segunda vez a chapa da segunda transferência (situação D) será 000100500123T002 e assim por diante.  
   
**Observação:**   
Este processo será para transferência na mesma coligada ou entre coligadas distintas, para os códigos de demissão 5 - Transferência sem ônus p/ Cedente e 6 - Transferência com ônus p/ Cedente.   
Sequenciamento de Chapa e Registro na Transferência Individual  
   
Não considerar Estagiário no Sequenciamento  
   
Geração de Chapa por Fórmula na Transferência Coletiva

Parâmetro para ativar a geração da chapa do funcionário na coligada destino através da fórmula cadastrada no campo relacionado. Este parâmetro ignorará a geração de chapa, na transferência coletiva, através de cadastro sequencial e levará em consideração o resultado da fórmula.

**Observação**

Quando o parâmetro de geração de chapa por fórmula estiver marcado será obrigatório informar o campo fórmula (validação através de mensagem para o usuário)

* Alteração do processo de cálculo da transferência para validação do novo parâmetro gerado.

No caso do parâmetro de geração de chapa estar selecionado (coligada origem) e o processo ser uma transferência coletiva a geração da chapa do funcionário para a coligada destino respeitará o resultado da fórmula parametrizada.

Foram realizadas as seguintes validações para a nova chapa gerada:

* + Se a nova chapa encontrada pela fórmula existir na coligada destino, o log exibirá a informação: "A Chapa xxx já existe na coligada destino." e a transferência do funcionário não será efetuada.
  + Se não retornar nenhuma chapa pela fórmula, a transferência não será realizada para o funcionário e uma mensagem será informada no log: "Nova Chapa inválida".

Caso o parâmetro "Cadastro Automático de Chapas Sequenciais" estiver selecionado na Coligada Destino e a Nova Chapa gerada for maior que o valor informado no campo CADASTROAUTOMATICOCHAPASSEQUENC da tabela GAUTOINC a nova implementação efetuará o ajuste do valor da tabela GAUTOINC para o correspondente a chapa gerada, não prejudicando o sequenciamento.

Fórmula para Nova Chapa

Informar uma fórmula já cadastrada para realizar a busca da nova chapa (ex. buscar informação de campo complementar, tabela de/para)

**Exemplo**

STR (COLIGADACORRENTE,'00')+ STR(CHAPA, '000'), onde a coligada corrente é 1, e a chapa do funcionário corrente é 00001. O resultado da fórmula será 01001.

Se a configuração de chapa possuir máscara com separador, ##.###, a fórmula deverá compor o caractere:

STR (COLIGADACORRENTE,'00')+ '.'+ STR(CHAPA, '000'), onde o retorno será 01.001

|  |  |
| --- | --- |
|  | Informações Complementares |

---

[<< Retornar para **Folha de Pagamento**](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452718602)
