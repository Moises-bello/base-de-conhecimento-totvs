---
article_id: 360060623353
category: Configurações
content_hash: 06bad7c1c61cae2429252afdfaa079e03c89e760b0ba40a8f07ab228dfd0f4d9
fetched_at: '2026-06-28T22:46:49.590822+00:00'
product: rm
section_id: 1500000834621
source: central-rm
title: RH - RM - FOP - Configurações de chapa
type: support-article
updated_at: '2022-09-23T12:15:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060623353-RH-RM-FOP-Configura%C3%A7%C3%B5es-de-chapa
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:10:00 min****Dúvida**Quais são os parâmetros disponíveis no Parametrizador para cadastro de chapas de funcionários no RM?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
 **Solução**Presente em **Configurações | Parametrizador | 06.01.02 - Funcionário | Configuração da Chapa**, há diversas opções para configuração.  
  
**Tamanho**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9062517031063/mceclip0.png)  
  
Campo onde é informada a quantidade de caracteres da chapa do funcionário, permitido até 16 caracteres e não podendo ser 0 (zero). Se houver necessidade da empresa aumentar o número de dígitos, as chapas dos funcionários já cadastrados não serão influenciados.  
  
**Máscara para a chapa**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9062521436439/mceclip1.png)  
  
Campo onde é definido os tipos que irão compor mascara da chapa do funcionário. Quando é inserido um novo funcionário no sistema é feita a consistência da chapa cadastrada com a máscara definida. A máscara é formada pelos caracteres abaixo:

* #: para campo numérico.
* L: para campo alfabético e de preenchimento obrigatório.
* I: para campo alfabético e de preenchimento facultativo.
* A: para campo alfanumérico e que os dígitos devem ser preenchidos obrigatoriamente.
* a: para campo alfanumérico, podendo ser digitados letras e números.
* Q: Para qualquer caractere, menos os separadores (: . , ; /)

Para este campo pode ser informado a combinação dos caracteres acima, desde que não ultrapasse a quantidade informada no campo tamanho.  
Também é permitido informar o separador '.' no formato da mascara sendo este contado como um caractere. A Máscara da Chapa é obrigatória.

Por exemplo, se a máscara de um código for L#.##, o código poderá ser A1.01, sendo que se digitado a11, o sistema passará a "a" (minúscula) para "A" (maiúscula) e preencherá as outras casas com "0".  
  
**Dígito Verificador**  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9062594213143/mceclip2.png)  
  
O dígito verificador é utilizado para consistir a chapa do funcionário conforme padrões definidos para ela:

* *Não utiliza o dígito verificador para Chapa*: esta opção indica que a empresa não utiliza o dígito verificador no código da chapa.
* *Somente valida o dígito verificador para Chapa:* marcando esta opção é habilitado o campo 'Fórmula p/ cálculo do dígito verificador' e valida o dígito verificador através de fórmula informada no respectivo campo, no momento da digitação de da chapa no cadastro de funcionários.
* *Gera o dígito verificador para Chapa:* marcando esta opção é habilitado o campo  'Fórmula p/ cálculo do dígito verificador' e gera o dígito verificador através de fórmula informada no respectivo campo, ao finalizar o cadastro de funcionário.

Para validar ou gerar o dígito verificador, a chapa deve conter somente números. O ultimo número da chapa deverá.  
  
**Fórmula p/ Cálculo do digito verificador**  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9062612371863/mceclip3.png)  
  
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
  
**Completar Chapa com zeros à esquerda automaticamente:**  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9062632787479/mceclip4.png)  
  
Habilitando este parâmetro o sistema irá complementar com zeros à esquerda a chapa digitada, completando o número de dígitos que falta conforme a máscara informada. Não habilitando este parâmetro, o usuário deverá digitar os zeros a esquerda conforme o cadastro de máscara da chapa.  
  
**Cadastro automático de chapas sequenciais (exclusivamente numéricas, onde o valor da chapa seja menor que 2147483647):**  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9062638634391/mceclip5.png)  
  
Este parâmetro só fica habilitado se o campo máscara for definido todo numérico. Ao marcar este parâmetro, o campo chapa no cadastro de funcionário fica desabilitado para edição na inclusão de um novo funcionário. A chapa é preenchida obedecendo um controle sequencial, automaticamente e individual por coligada, ou seja, cada coligada terá uma sequencia de chapas independente.  
  
O usuário poderá marcar este parâmetro a qualquer momento, mesmo que já tenha funcionários cadastrados na base. Porém deve ficar atento, pois marcando este parâmetro, caso exista algum funcionário com alguma chapa que faça parte da sequencia que está sendo seguida, pode retornar erro de chave duplicada.  
É recomendado usar esse parâmetro somente se todas as chapas da base estiverem em formato número. Uma mensagem de informação é retornada para o usuário no momento que o mesmo marca este parâmetro.  
Usando este parâmetro só é permitido cadastrar funcionários até atingir o código de chapa de número 2147483647.  
Caso o usuário deseje que a configuração de máscaras seja diferente de numéricas, o sistema desabilitará este parâmetro e os parâmetros filhos deste automaticamente.  
  
**Utiliza sequencial global**  
Ao marcar o parâmetro para utilizar sequencial global, será feito um controle sequencial global, ou seja, não será feito um controle de sequencia das chapas independente, por coligada. Este parâmetro só fica habilitado quando é marcado o parâmetro 'Cadastro automático de chapas sequenciais (exclusivamente numéricas, onde o valor da chapa seja menor que 2147483647)'.  
Marcando este parâmetro, o parâmetro 'Utiliza máscara no prefixo da chapa fica desabilitado.  
  
**Utiliza máscara no prefixo da Chapa**  
Este parâmetro permite definir uma mascara no prefixo da chapa. Marcando este parâmetro é habilitado o campo 'Máscara prefixo da chapa', onde o usuário define se prefixo será composta pelo código da coliga ou filial. Este parâmetro só fica habilitado quando é marcado o parâmetro 'Cadastro automático de chapas sequenciais (exclusivamente numéricas, onde o valor da chapa seja menor que 2147483647)'.  
O campo 'Mascara prefixo chapa' deve ser informado ou caracteres, em maiúsculo' 'C' e/ou 'F', onde 'C' retorna o código da coligada e 'F' o código da Filial.  
   
**Exemplo:**  
Coligada = 8  
Filial = 9  
tamanho da mascara  = 6  
Informo no campo 'Máscara prefixo chapa' = CF  
Ao cadastrar o funcionário o campo chapa ficará '890001'  
  
**Transferência - Incrementar 4 dígitos de controle no final da chapa dos demitidos**  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9062697577111/mceclip6.png)  
  
Este parâmetro somente ficará habilitado quando o campo "Tamanho" for maior ou igual 12, devido ao limite deste campo ser de 16 dígitos e o sistema auto incrementar a sequência das transferências com 4 dígitos.  
Esta sequência será no final da chapa do funcionário transferido (situação D) e iniciará sempre com "T" (transferido).  
   
**Exemplo**  
O campo "Tamanho" está definido com 12 dígitos. A chapa do funcionário a ser transferida é 000100500123.  
Ao transferir o funcionário a chapa do funcionário transferido (situação D) será 000100500123T001, e do ativo continua sendo 000100500123.  
Caso o funcionário seja transferido pela segunda vez a chapa da segunda transferência (situação D) será 000100500123T002 e assim por diante.  
   
**Importante**  
Este processo será para transferência na mesma coligada ou entre coligadas distintas, para os códigos de demissão 5 - Transferência sem ônus p/ Cedente e 6 - Transferência com ônus p/ Cedente.
