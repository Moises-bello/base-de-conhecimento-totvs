---
content_hash: 4a7a56b26c999d9d700c95766493594c23bbb9905c0ec45c7a9a35e27a1b3e23
fetched_at: '2026-06-29T00:09:17.054799+00:00'
page_id: '421388567'
product: rm
source: tdn-rm
title: Geração do Nosso Número
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388567
version: 12
---

A geração do nosso número permite a criação do nosso número que será gravado no "Boleto Bancário". O nosso número é gerado conforme as regras estabelecidas pela rede bancária.

**Validações do Processo de Geração de Nosso Número**

Parametrização Geral

Número Oficial do banco: Número oficial (Código Febraban) deve ser informado na tela de cadastro do banco quando o mesmo for inserido no sistema;

Tamanho do nosso número: Tamanho do nosso número deve ser informado no layout bancário, aba "Retorno de Cobrança";

Data de Vencimento: Data de vencimento do boleto deve ser informada.

Parametrização por Banco

**Banco Unicredi – 091**  
Cobrança Registrada  
A montagem do nosso número será YYNNNNNNNND, onde:

* YY é o Ano;
* EE é o número da carteira definido no convênio;
* NNNNNNNN é a base do nosso número calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.
* D é o dígito verificador.

**Banco do Brasil – 001, 655**  
Carteira 13

* Número do convênio: Convenio cadastrado para o banco deve ter o número do convênio definido;
* Espécie CNAB: Espécie CNAB, informada no cadastro do tipo do documento utilizado pelos lançamentos do boleto, não atende as especificações do banco para a carteira quando for diferente de 7 ou 14.

Carteira 15

* Número do convênio: Convenio cadastrado para o banco deve ter o número do convênio definido.

Carteira 16

* Número do convênio: Convenio cadastrado para o banco deve ter o número do convênio definido;
* Convênio não atende as especificações do banco para a carteira quando não tem tamanho 4 ou 6.

Carteira 17

* Número do convênio: Convenio cadastrado para o banco deve ter o número do convênio definido.

Carteira 18

* Número do convênio: Convenio cadastrado para o banco deve ter o número do convênio definido.

Demais Carteiras

* Não atende as especificações do banco.

**Banco Itaú – 341**  
Carteira 198

* Número da conta corrente: Número da conta corrente deve ser informado no cadastro da conta caixa utilizado pelo convênio;
* Número da agência: Número da agência deve ser informado no cadastro da conta caixa utilizada pelo convênio;
* Carteira: Carteira deve ser informada no cadastro do convênio utilizado pelo banco;
* Número do convênio: Convenio cadastrado para o banco deve ter o número do convênio definido.

Demais Carteiras

* Número da agência: Número da agência deve ser informado no cadastro da conta caixa utilizada pelo convênio.
* Carteira: Carteira deve ser informada no cadastro do convênio utilizado pelo banco;
* Número do convênio: Convenio cadastrado para o banco deve ter o número do convênio definido.

**Banco JSafra – 074**  
Carteira 06

* Carteira: Carteira deve ser informada no cadastro do convênio utilizado pelo banco.

Carteira 09

* Código Cedente: Código cedente deve ser informado no cadastro do convênio utilizado pelo banco;
* Carteira: Carteira deve ser informada no cadastro do convênio utilizado pelo banco.

Demais carteiras

* Não atendem as especificações do banco.

**Banco Nossa Caixa – 151**

* Número da conta corrente: Número da conta corrente, informado no cadastro da conta caixa utilizada pelo convênio, deve ser informado com 8 dígitos, sendo 2 dígitos da modalidade da conta e 6 dígitos do número da conta.

**Processamento de Geração do Nosso Número**  
  Parâmetros Gerais

Montagem do nosso número base depende do valor do tipo de nosso número.

* Tipo de nosso número: Informado no convênio utilizado pelo Banco, define o modo como será gerado o nosso número;
* Boleto: A referência do boleto será a base do nosso número gerado. Caso o lançamento não esteja vinculado a um boleto, será exibida a mensagem "O Lançamento não possui Boleto vinculado, portanto não é possível gerar Nosso Número através do Boleto. Utilize outro modo de geração do Nosso Número ou gere Boleto no Lançamento";
* Sequencial: Número sequencial, pertencente a faixa do limite inferir e limite superior, será a base do nosso número. Se o número sequencial for maior que o limite superior, o limite inferior será considerado como o próximo número sequencial. Quando o número sequencial gerado estiver fora da faixa definida no convênio (limite inferior e limite superior), será exibida a seguinte mensagem "O número sequencial não está dentro da faixa para geração do nosso número. Por favor, verificar cadastro de convênio";
* Geração Banco: Base do nosso número é gerada pelo banco.

Parametrização por Banco

**Banco do Brasil – 001 ou 655**  
Carteira11  
A montagem do nosso número será 00000000000, onde 00000000000 é um valor fixo.  
Carteira 13  
Espécie CNAB, informada no cadastro do tipo do documento utilizado pelos lançamentos do boleto, igual a 7 ou igual a 14, a montagem do nosso número será CCCCCCNNN01D, onde:

* CCCCCC é o número do convênio informado no cadastro do convênio;
* NNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* 01 é um valor fixo;
* D é o dígito verificador calculado. Digito verificador depende das demais partes descritas.

Carteira 15  
A montagem do nosso número será CCCCCCNNNNND, onde:

* CCCCCC é o número do convênio informado no cadastro do convênio;
* NNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado. Digito verificador depende das demais partes descritas.

Carteira 16  
Tamanho do nosso número, definido no layout bancário, aba "Retorno de Cobrança, 17 e comprimento do número do convênio igual a 7. A montagem do nosso número será CCCCCCNNNNNNNNNN, onde:

* CCCCCCC é o número do convênio informado no cadastro do convênio;
* NNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.

Tamanho do nosso número, definido no layout bancário, aba "Retorno de Cobrança, 17 e o comprimento do número do convênio diferente de 7. A montagem do nosso número será NNNNNNNNNNNNNNNNN, onde:

* NNNNNNNNNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.

Tamanho do nosso número, definido no layout bancário, aba "Retorno de Cobrança, 11 e o comprimento do número do convênio igual a 4. A montagem do nosso número será CCCCNNNNNNND, onde:

* CCCC é o número do convênio informado no cadastro do convênio;
* NNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado. Digito verificador depende das demais partes descritas.

Tamanho do nosso número, definido no layout bancário, aba "Retorno de Cobrança, 11 e o comprimento do número do convênio igual a 6. A montagem do nosso número será CCCCCCNNNNND, onde:

* CCCCCC é o número do convênio informado no cadastro do convênio;
* NNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado. Digito verificador depende das demais partes descritas.

Carteira 17  
Tamanho do nosso número, definido no layout bancário, aba "Retorno de Cobrança, 17 e o comprimento do número do convênio igual a 7. A montagem do nosso número será CCCCCCNNNNNNNNNN, onde:

* CCCCCCC é o número do convênio informado no cadastro do convênio;
* NNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.

Tamanho do nosso número, definido no layout bancário, aba "Retorno de Cobrança, 17 e o comprimento do número do convênio diferente de 7. A montagem do nosso número será NNNNNNNNNNNNNNNNN, onde:

* NNNNNNNNNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.

O comprimento do número do convênio igual a 4, e tamanho do nosso número, definido no layout bancário, aba "Retorno de Cobrança, igual a 11. A montagem do nosso número será CCCCNNNNNNND, onde:

* CCCC é o número do convênio informado no cadastro do convênio;
* NNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado. Digito verificador depende das demais partes descritas.

O comprimento do número do convênio igual a 4, e tamanho do nosso número, definido no layout bancário, aba "Retorno de Cobrança, diferente de 11. A montagem do nosso número será CCCC00NNNNND, onde:

* CCCC é o número do convênio informado no cadastro do convênio;
* 00 é um valor fixo;
* NNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado. Digito verificador depende das demais partes descritas.

O comprimento do número do convênio diferente de 4, e tamanho do nosso número, definido no layout bancário, aba "Retorno de Cobrança, diferente de 17. A montagem do nosso número será CCCCCCNNNNND, onde:

* CCCCCC é o número do convênio informado no cadastro do convênio;
* NNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado. Digito verificador depende das demais partes descritas.

Carteira 18  
Tamanho do nosso número, definido no layout bancário, aba "Retorno de Cobrança, 17 e o comprimento do número do convênio igual a 7. A montagem do nosso número será CCCCCCNNNNNNNNNN, onde:

* CCCCCCC é o número do convênio informado no cadastro do convênio;
* NNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.

Tamanho do nosso número, definido no layout bancário, aba "Retorno de Cobrança, 17 e o comprimento do número do convênio diferente de 7. A montagem do nosso número será NNNNNNNNNNNNNNNNN, onde:

* NNNNNNNNNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.

Tamanho do nosso número, definido no layout bancário, aba "Retorno de Cobrança, diferente de 17. A montagem do nosso número será CCCCCCNNNNND, onde:

* CCCCCC é o número do convênio informado no cadastro do convênio;
* NNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado. Digito verificador depende das demais partes descritas.

Carteira 31

* A montagem do nosso número será 00000000000, onde 00000000000 é um valor fixo.

Carteira 51

* A montagem do nosso número será 00000000000, onde 00000000000 é um valor fixo.

**Banco América do Sul – 215**

A montagem do nosso número será NNNNNNND, onde:

* NNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado pelo seguinte formato AAAA02CCCCCCCCNNNNNNN, onde;
* AAAA é o número da agência definido no cadastro da conta caixa;
* 02 é um valor fixo;
* CCCCCCCC é o código cedente definido no convênio;
* NNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.

**Banco Bandepe (Banco do Estado de Pernambuco) – 024**

Nosso número base menor que 10000000, a montagem do nosso número será NNNNNNND, onde:

* NNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.
* D é o dígito verificador calculado.

Digito verificador é calculado pelo seguinte formato AAACCCCCCCNNNNNNN, onde:

* AAAA é o número da agência definido no cadastro da conta caixa;
* CCCCCCC é o código cedente definido no convênio;
* NNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;

Nosso número base maior que 10000000, a montagem do nosso número será NNNNNNNNNNND, onde:

* NNNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado. Digito verificador depende das demais partes descritas.

**Banco Banese (Banco do Estado de Sergipe) – 047**

A montagem do nosso número será NNNNNNNND, onde:

* NNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado pelo seguinte formato AAANNNNNNNN, onde:
* AAA é o número da agência definido na conta caixa utilizada pelo convênio;
* NNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.

**Banco Banestado (Banco do Estado do Paraná) – 038**

A montagem do nosso número será NNNNNNNNND, onde:

* NNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado. Digito verificador depende das demais partes descritas.

**Banco Banestes (Banco do Estado do Espírito Santos) – 021**

A montagem do nosso número será NNNNNNNNDD, onde:

* NNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o primeiro dígito verificador calculado. O dígito verificador depende das demais informações citadas acima;
* D é o segundo dígito verificador calculado. O dígito verificador depende do número base calculado e do primeiro dígito citado acima.

**Banco Banrisul – 041**

A montagem do nosso número será NNNNNNNNDD, onde:

* NNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o primeiro dígito verificador calculado. O dígito verificador depende das demais informações citadas acima;
* D é o segundo dígito verificador calculado. O dígito verificador depende do número base calculado e do primeiro dígito citado acima.

**Banco Basa (Banco da Amazônia S.A.) – 003**

A montagem do nosso número será NNNNNNNNNNNNNNNN, onde:

* NNNNNNNNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.

Banco BCN – 291

A montagem do nosso número será NNNNNNND, onde:

* NNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado. Digito verificador depende das demais partes descritas.

**Banco Besc (Banco do Estado de Santa Catarina) – 027**

Carteira 25  
A montagem do nosso número será NNNNNNNNNNNNND3D, onde:

* NNNNNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o primeiro dígito verificador calculado. O dígito verificador depende das demais informações citadas acima;
* 3 é um valor fixo;
* D é o segundo dígito verificador calculado. O dígito verificador depende das demais informações citadas acima.

Carteira 06  
A montagem do nosso número será YNNNNNNNNN000D3D, onde:

* Y é o último dígito do ano da data corrente formatado com dois dígitos;
* NNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* 000 é um valor fixo;
* D é o primeiro dígito verificador calculado. O dígito verificador depende das demais informações citadas acima;
* 3 é um valor fixo;
* D é o segundo dígito verificador calculado. O dígito verificador depende das demais informações citadas acima.

Demais carteiras  
A montagem do nosso número será NNNNNN1D, onde:

* NNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* 1 é um valor fixo;
* D é o primeiro dígito verificador calculado. O dígito verificador depende das demais informações citadas acima.

**Banco Bic – 320**

A montagem do nosso número será NNNNNND, onde:

* NNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado pelo seguinte formato AAANNNNNN, onde;
* AAA é o número da agência definido na conta caixa utilizada pelo convênio;
* NNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.

**Banco Bilbao Vizcaya – 641**

A montagem do nosso número será CCCCCCENNNNNNNDD, onde:

* CCCCCC é o código cedente definido no convênio;
* E é o dígito verificador do cedente definido no convênio;
* NNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o primeiro dígito verificador calculado. O dígito verificador depende do nosso número base;
* D é o segundo dígito verificador calculado. O dígito verificador depende das demais informações citadas acima.

**Banco BMC – 394**

Carteira 1  
A montagem do nosso número será NNNNNNNNNND, onde:

* NNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o primeiro dígito verificador calculado. O dígito verificador depende das demais informações citadas acima.

Carteira 3  
A montagem do nosso número será NNNNNNNNNND, onde:

* NNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o primeiro dígito verificador calculado. O dígito verificador depende das demais informações citadas acima.

Demais carteiras

* A montagem do nosso número será 00000000000, onde  00000000000 é um valor fixo.

**Banco BNB (Banco do Nordeste Brasileiro) – 004**

A montagem do nosso número será NNNNNNND, onde:

* NNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado. O dígito verificador depende das demais informações citadas acima.

**Banco Boston – 479**

A montagem do nosso número será NNNNNNNND, onde:

* NNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado. O dígito verificador depende das demais informações citadas acima.

**Banco Bradesco – 237 e****Banco Grafeno - 274**

A montagem do nosso número será NNNNNNNNNNND, onde:

* NNNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado pelo seguinte formato CCNNNNNNNNNNN, onde:
* CC é o número da carteira definido no convênio;
* NNNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.

**Banco BRB (Banco de Brasília) – 070**

A montagem do nosso número será CNNNNNN070DD, onde:

* C é o número da carteira definido no convênio;
* NNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* 070 é um valor fixo;
* D é o primeiro dígito verificador calculado pelo seguinte formato 000AAACCCCCCDENNNNNN070, onde:
* 000 é um valor fixo;
* AAA é o número da agência definido no cadastro da conta caixa utilizada pelo convênio;
* CCCCCC é o número da conta corrente definido no cadastro da conta caixa;
* D é o dígito da conta corrente definido no cadastro da conta caixa utilizada pelo convênio;
* E é o número da carteira definido no convênio;
* NNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* 070 é um valor fixo;
* D é o segundo dígito verificador calculado. O dígito verificador depende do primeiro dígito citado acima, e tem o mesmo formato para cálculo.

**Banco BVA – 044**

A montagem do nosso número será CCCCCCNNNNND, onde:

* CCCCCC é o número da conta corrente definido no cadastro da conta caixa utilizada pelo convênio;
* NNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado pelo seguinte formato EECCCCCCNNNNN, onde;
* EE é o número da carteira definido no convênio;
* CCCCCC é o número da conta corrente definido no cadastro da conta caixa utilizada pelo convênio;
* NNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.

**Banco Caixa Econômica Federal – 104**

Carteira 01  
A montagem do nosso número será 9NNNNNNNNNNNNNNNNND, onde:

* 9 é um valor fixo;
* NNNNNNNNNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o primeiro dígito verificador calculado. O dígito verificador depende das demais informações citadas acima.

Carteira 11  
A montagem do nosso número será 00000000000D, onde:

* 00000000000 é um valor fixo.
* D é o primeiro dígito verificador calculado. O dígito verificador depende das demais informações citadas acima.

Carteira 12  
A montagem do nosso número será 9NNNNNNNNND, onde:

* 9 é um valor fixo;
* NNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o primeiro dígito verificador calculado. O dígito verificador depende das demais informações citadas acima.

Carteira 14  
Tamanho do nosso número, definido no layout bancário, aba "Retorno de Cobrança, igual a 17, a montagem do nosso número será CCNNNNNNNNNNNNNNND, onde:

* CC é o número da carteira definido no convênio;
* NNNNNNNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o primeiro dígito verificador calculado. O dígito verificador depende das demais informações citadas acima.

Tamanho do nosso número, definido no layout bancário, aba "Retorno de Cobrança, diferente de 17, e o código cedente igual a 870, a montagem do nosso número será 8NNNNNNNNNNNNNND, onde:

* 8 é um valor fixo;
* NNNNNNNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o primeiro dígito verificador calculado. O dígito verificador depende das demais informações citadas acima.

Tamanho do nosso número, definido no layout bancário, aba "Retorno de Cobrança, diferente de 17, e o código cedente diferente de 870, a montagem do nosso número será 8NNNNNNNNND, onde

* 8 é um valor fixo;
* NNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o primeiro dígito verificador calculado. O dígito verificador depende das demais informações citadas acima.

Carteira 24  
Tamanho do nosso número, definido no layout bancário, aba "Retorno de Cobrança, igual a 17, a montagem do nosso número será CCNNNNNNNNNNNNNNND, onde:

* CC é o número da carteira definido no convênio;
* NNNNNNNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o primeiro dígito verificador calculado. O dígito verificador depende das demais informações citadas acima.

Carteira 82  
A montagem do nosso número será 82NNNNNNNND, onde:

* 82 é um valor fixo;
* NNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o primeiro dígito verificador calculado. O dígito verificador depende das demais informações citadas acima.

Demais carteiras

* Não atende as especificações do banco.

**Banco Cidade – 244**

Carteira 4  
A montagem do nosso número será NNNNNNAAAD, onde:

* NNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* AAA e o número da agência definido no cadastro da conta caixa utilizada pelo convênio;
* D é o primeiro dígito verificador calculado. O dígito verificador depende das demais informações citadas acima.

Demais Carteiras

* Não atende as especificações do banco.

**Banco Citibank – 745**

A montagem do nosso número será 66NNNNNNNNND, onde:

* 66 é um valor fixo;
* NNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado. O dígito verificador depende das demais informações citadas acima.

**Bancoob (Banco Cooperativo do Brasil) – 756**

A montagem do nosso número será NNNNNNND, onde:

* NNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado pelo seguinte formato AAAACCCCCCCCCDNNNNNNN, onde;
* AAAA é o número da agência definido no cadastro da conta caixa utilizada pelo convênio;
* CCCCCCCCC é o código cedente definido no convênio (deve-se usar o campo Cliente-DV);
* D é o dígito verificador do código cedente definido no convênio;
* NNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.

**Banco Credibel – 721**

Padrão

* A montagem do nosso número será 00000000, onde 00000000 é um valor fixo.

Carteira 6

* O nosso número é vazio.

**Banco Daycoval – 707**

Carteira 06

* A montagem do nosso número será NNNNNNNN, onde NNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.

Carteira 03

* O nosso número é vazio.

Carteira 04  
A montagem do nosso número será NNNNNNNNNNND, onde:

* NNNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado pelo seguinte formato CCNNNNNNNNNNN, onde;
* CC é o número da carteira definido no convênio;
* NNNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.

Carteira 121  
Sejam eles:  
AAAA = código da agência do título, sem DV  
CCC = código da carteira  
NNNNNNNNNN = o nosso número, sem DV.

Multiplica-se cada algarismo do número formado pela composição dos campos acima pela sequência de multiplicadores 2,1,2,1,2,1,2 (posicionados da direita para a esquerda). . Se a multiplicação resultar > 9 (por exemplo = 12), somar os dígitos (1 + 2). A seguir, soma-se os algarismos dos produtos e o total obtido é dividido por 10. O DV é a diferença entre o divisor (10) e o resto da divisão: 10 - (RESTO DA DIVISAO) = DV. Se o resto da divisão for zero, o DV é zero.

EXEMPLO: Agência: 0001.9, Carteira = 121, Nosso Número = 0004309540. O Nosso Número será a concatenação do código da agência (com DV), da carteira, do nosso número e do DV do nosso número. No exemplo: 00019/121/0004309540-8

Demais carteiras

* A montagem do nosso número será 00000000, onde 00000000 é o um valor fixo.

**Banco Fibra – 224**

* A montagem do nosso número será NNNNNNNN, onde NNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.

**Banco HSBC – 399**

Cobrança registrada  
A montagem do nosso número será CCCCCNNNNND, onde:

* CCCCC é o número do convênio definido no cadastro do convênio;
* NNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado. O dígito verificador depende das demais informações citadas acima.

Cobrança não registrada  
Tamanho no nosso número, definido no layout bancário, aba "Retorno de Cobrança, igual a 13, a montagem do nosso número será NNNNNNNNNNNNNDTD, onde:

* NNNNNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o primeiro dígito verificador calculado. O dígito verificador depende das demais informações citadas acima;
* T é o tipo identificador. O tipo de identificador será 5 se a data de vencimento do boleto for menor ou igual 01/01/1900, ou boleto for contra apresentação. Caso contrário o tipo de identificador será 4;
* D é o segundo dígito verificador calculado. O dígito verificador depende das demais informações citadas acima.

Tamanho do nosso número igual a 6, a montagem do nosso número será NNNNNNDTD, onde:

* NNNNNN é o nosso número base;
* D é o primeiro dígito verificador calculado. O dígito verificador depende das demais informações citadas acima;
* T é o tipo identificador. O tipo de identificador será 5 se a data de vencimento do boleto for menor ou igual 01/01/1900, ou boleto for contra apresentação. Caso contrário o tipo de identificador será 4;
* D é o segundo dígito verificador calculado. O dígito verificador depende das demais informações citadas acima.

Tamanho no nosso número diferente de 13 e 6.

* Não atende as especificações do banco

**Banco Itaú – 341**

Carteira 126  
A montagem do nosso número será NNNNNNNND, onde:

* NNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado pelo seguinte formato CCNNNNNNNN, onde;
* CC é o número da carteira definido no convênio;
* NNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.

Carteira 150  
A montagem do nosso número será NNNNNNNND, onde:

* NNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado pelo seguinte formato CCNNNNNNNN, onde;
* CC é o número da carteira definido no convênio;
* NNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.

Carteira 168  
A montagem do nosso número será NNNNNNNND, onde:

* NNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado pelo seguinte formato CCNNNNNNNN, onde;
* CC é o número da carteira definido no convênio;
* NNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.

Carteira 198  
A montagem do nosso número será NNNNNNNNNNND, onde:

* NNNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado pelo seguinte formato AAAACCCCCEEENNNNNNNNNNN, onde;
* AAAA é o número da agência definido no cadastro da conta caixa utilizada pelo convênio;
* CCCCC é o número conta corrente definido no cadastro da conta caixa utilizada pelo convênio;
* EEE é o número da carteira definido no convênio;
* NNNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.

Demais carteiras  
A montagem do nosso número será NNNNNNNNNNND, onde:

* NNNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado pelo seguinte formato AAAACCCCCEEENNNNNNNNNNN, onde;
* AAAA é o número da agência definido no cadastro da conta caixa utilizada pelo convênio;
* CCCCC é o número código cedente definido no convênio;
* EEE é o número da carteira definido no convênio;
* NNNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.

**Banco JSafra – 074**

Carteira 06

* A montagem do nosso número será 000000000000, onde 000000000000 é um valor fixo.

Carteira 09  
A montagem do nosso número será CCCCNNNNNNND, onde:

* CCCC é o código cedente definido no convênio;
* NNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado pelo seguinte formato EECCCCNNNNNNN, onde;
* EE é o número da carteira definido no convênio;
* CCCC é o código cedente definido no convênio;
* NNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.

Demais carteiras

* Não atende as especificações do banco.

**Banco Mercantil do Brasil – 389**

Cobrança Registrada  
A montagem do nosso número será CCEENNNNNND, onde:

* CC é o número do convênio informado no cadastro do convênio;
* EE é o número da carteira definido no convênio;
* NNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado pelo seguinte formato AAAACCEENNNNNND, onde;
* AAAA é o número da agência definido no cadastro da conta caixa utilizada pelo convênio;
* CC é o número do convênio informado no cadastro do convênio;
* EE é o número da carteira definido no convênio;
* NNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.

Cobrança Não Registrada  
A montagem do nosso número será CC06NNNNNND, onde:

* CC é o código cedente definido no convênio;
* 06 é um valor fixo;
* NNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado pelo seguinte formato AAAACC06NNNNNND, onde;
* AAAA é o número da agência definido no cadastro da conta caixa utilizada pelo convênio;
* CC é o código cedente definido no convênio;
* 06 é um valor fixo;
* NNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.

**Banco Mercantil de São Paulo – 392**

A montagem do nosso número será CCYNNNNNNNDD, onde:

* CC é o número da carteira definido no convênio;
* Y é o último dígito do ano da data de corrente, definido no cadastro da conta caixa, formatado com dois dígitos;
* NNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o primeiro dígito verificador calculado. O dígito verificador depende das demais informações citadas acima;
* D é o segundo dígito verificador calculado. O dígito verificador depende das demais informações citadas acima;

**Banco Nossa Caixa – 151**

Carteira 1

* A montagem do nosso número será 0NNNNNNNND, onde:
* 0 é um valor fixo;
* NNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado pelo seguinte formato AAAAMMCCCCCCCD0NNNNNNNN, onde;
* AAAA é o número da agência definido no cadastro da conta caixa utilizada pelo convênio;
* MM é a modalidade da conta corrente que são os dois primeiros números presente no número da conta corrente definido no cadastro da conta caixa utilizada pelo convênio;
* CCCCCCC é o número da conta corrente que são os sete últimos números presente no número da conta corrente definido no cadastro da conta caixa utilizada pelo convênio;
* D é o dígito da conta corrente definido no cadastro da conta caixa utilizada pelo convênio;
* 0 é um valor fixo;
* NNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.

Carteira 5  
A montagem do nosso número será 9NNNNNNNND, onde:

* 9 é um valor fixo;
* NNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado pelo seguinte formato AAAAMMCCCCCCCD9NNNNNNNN, onde;
* AAAA é o número da agência definido no cadastro da conta caixa utilizada pelo convênio;
* MM é a modalidade da conta corrente que são os dois primeiros números presente no número da conta corrente definido no cadastro da conta caixa utilizada pelo convênio;
* CCCCCCC é o número da conta corrente que são os sete últimos números presente no número da conta corrente definido no cadastro da conta caixa utilizada pelo convênio;
* D é o dígito da conta corrente definido no cadastro da conta caixa utilizada pelo convênio;
* 9 é um valor fixo;
* NNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.

Demais carteiras  
A montagem do nosso número será 99NNNNNNND, onde:

* 99 é um valor fixo;
* NNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado pelo seguinte formato AAAAMMCCCCCCCD99NNNNNNN, onde;
* AAAA é o número da agência definido no cadastro da conta caixa utilizada pelo convênio;
* MM é a modalidade da conta corrente que são os dois primeiros números presente no número da conta corrente definido no cadastro da conta caixa utilizada pelo convênio;
* CCCCCCC é o número da conta corrente que são os sete últimos números presente no número da conta corrente definido no cadastro da conta caixa utilizada pelo convênio;
* D é o dígito da conta corrente definido no cadastro da conta caixa utilizada pelo convênio;
* 99 é um valor fixo;
* NNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.

**Banco Real – 275, 356**

Cobrança Registrada

* A montagem do nosso número será NNNNNNN, onde NNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.

Cobrança Não Registrada

* Tamanho do nosso número, definido no layout bancário, aba "Retorno de Cobrança, igual a 7, a montagem do nosso número será NNNNNNN, onde NNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.
* Tamanho do nosso número, definido no layout bancário, aba "Retorno de Cobrança, igual a 8, a montagem do nosso número será NNNNNNNN, onde  NNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.
* Tamanho do nosso número, definido no layout bancário, aba "Retorno de Cobrança, igual a 9, a montagem do nosso número será NNNNNNNNN, onde  NNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.
* Tamanho do nosso número, definido no layout bancário, aba "Retorno de Cobrança, igual a 10, a montagem do nosso número será NNNNNNNNNN, onde  NNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.
* Tamanho do nosso número, definido no layout bancário, aba "Retorno de Cobrança, igual a 11, a montagem do nosso número será NNNNNNNNNNN, onde  NNNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.
* Tamanho do nosso número, definido no layout bancário, aba "Retorno de Cobrança, igual a 12, a montagem do nosso número será NNNNNNNNNNNN, onde  NNNNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.
* Tamanho do nosso número, definido no layout bancário, aba "Retorno de Cobrança, igual a 13, a montagem do nosso número será NNNNNNNNNNNNN, onde  NNNNNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.
* Tamanho do nosso número, definido no layout bancário, aba "Retorno de Cobrança, fora da faixa 7 a 13, a montagem do nosso número será NNNNNNN, onde  NNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.

**Banco Rural – 453, 749**  
A montagem do nosso número será NNNNNNND, onde:

* NNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado pelo seguinte formatos abaixo.

Se o número do contrato estiver preenchido 0AAATTCCCCCCCDNNNNNNN, onde:

* 0 é um valor fixo;
* AAA é o número da agência, definido no cadastro da conta caixa utilizada pelo convênio, removido o primeiro dígito;
* TT é o tipo de conta definido no convênio;
* CCCCCCC é o número da conta corrente definido no cadastro da conta caixa utilizada pelo convênio;
* D é o dígito da conta corrente definida no cadastro da conta caixa utilizada pelo convênio;
* NNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.

Se o número do contrato não estiver preenchido AAAANNNNNNN, onde:

* AAAA é o número da agência, definido no cadastro da conta caixa utilizada pelo convênio, removido o primeiro dígito;
* NNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.

**Banco Safra – 422**

A montagem do nosso número será NNNNNNNND, onde:

* NNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o primeiro dígito verificador calculado. O dígito verificador depende das demais informações citadas acima.

**Banco Santander – 008, 033, 353**

Regras de formatação do campo livre nas posições 20 a 44  
Tamanho do nosso número  
Campo Tamanho do nosso número, definido no layout bancário, aba "Retorno de Cobrança, número igual a sete, a montagem do nosso número será AAANNNNNNND, onde:

* AAA é o número da agência definido no cadastro da conta caixa utilizada pelo convênio;
* NNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado. O dígito verificador depende das demais informações citadas acima.

Campo Tamanho do nosso número, definido no layout bancário, aba "Retorno de Cobrança, igual a oito, a montagem do nosso número será NNNNNNND, onde:

* NNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado. O dígito verificador depende das demais informações citadas acima.

Padrão  
A montagem do nosso número será NNNNNNNNNNNND, onde:

* NNNNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado. O dígito verificador depende das demais informações citadas acima.

**Banco Sicredi (Banco Cooperativo Sistema de Crédito Cooperativo) – 748**

A montagem do nosso número será YYMNNNNND, onde:

* YY é o ano da data atual formatado com dois dígitos;
* M é o mês da data atual formatado com um dígito. Se for o mês de janeiro será 2, mês de outubro será 3, mês de novembro será 4 e mês de dezembro será 5;
* NNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado pelo seguinte formato. AAAAAACCCCCYYMNNNNN, onde;
* AAAAAA é o número da agência definido no cadastro da conta caixa utilizada pelo convênio;
* CCCCC é o código cedente definido no convênio;
* YY é o ano da data atual formatado com dois dígitos;
* M é o mês da data atual formatado com um dígito. Se for o mês de janeiro será 2, mês de outubro será 3, mês de novembro será 4 e mês de dezembro será 5;
* NNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.

**Banco Sofisa – 637**

Carteira 6

* A montagem do nosso número será NNNNNNNN, onde NNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.

Demais carteiras

* Não atende as especificações do banco.

**Banco Sudameris – 347**

Cobrança registrada

* A montagem do nosso número será NNNNNNN, onde NNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.

Cobrança Não Registrada

* Tamanho do nosso número, definido no layout bancário, aba "Retorno de Cobrança, igual a 7, a montagem do nosso número será NNNNNNN, onde NNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.
* Tamanho do nosso número, definido no layout bancário, aba "Retorno de Cobrança, igual a 8, a montagem do nosso número será NNNNNNNN, onde NNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.
* Tamanho do nosso número, definido no layout bancário, aba "Retorno de Cobrança, igual a 9, a montagem do nosso número será NNNNNNNNN, onde NNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.
* Tamanho do nosso número, definido no layout bancário, aba "Retorno de Cobrança, igual a 10, a montagem do nosso número será NNNNNNNNNN, onde NNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.
* Tamanho do nosso número, definido no layout bancário, aba "Retorno de Cobrança, igual a 11, a montagem do nosso número será NNNNNNNNNNN, onde NNNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.
* Tamanho do nosso número, definido no layout bancário, aba "Retorno de Cobrança, igual a 12, a montagem do nosso número será NNNNNNNNNNNN, onde NNNNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.
* Tamanho do nosso número, definido no layout bancário, aba "Retorno de Cobrança, igual a 13, a montagem do nosso número será NNNNNNNNNNNNN, onde NNNNNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.
* Tamanho do nosso número, definido no layout bancário, aba "Retorno de Cobrança, fora da faixa 7 a 13, a montagem do nosso número será NNNNNNN, onde NNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.

**Banco Unibanco – 409**

Carteira 20  
A montagem do nosso número será NNNNNNNNNNNNNND, onde:

* NNNNNNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado. O dígito verificador depende das demais informações citadas acima.

Demais carteiras  
A montagem do nosso número será NNNNNNNNNND, onde:

* NNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio.
* D é o dígito verificador calculado. O dígito verificador depende das demais informações citadas acima.

Banco Unicredi – 091  
Cobrança Registrada  
A montagem do nosso número será YYNNNNNNNND, onde:

* YY é o Ano;
* NNNNNNNN é a base do nosso número calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado pelo seguinte formato YYNNNNNNNND, onde:
* YY é o número da carteira definido no convênio (2);
* NNNNNNNN é a base do nosso número (8);
* **D** é o dígito verificador (1).

**Banco ABC – 246**

A montagem do nosso número será NNNNNNNNNND, onde:

* NNNNNNNNNN é o nosso numero base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio;
* D é o dígito verificador calculado. Digito verificador é calculado (Módulo 10) pelo seguinte formato AAAACCCNNNNNNNNNN, onde:
* AAAA é o número da agência sem o dígito verificador definido no convênio (4);
* CCC é o código da carteira definido no convênio (3);
* NNNNNNNNNN é o nosso número base calculado a partir do "Tipo nosso número" definido no cadastro do Convênio (10).

**Banco Crefisa - 069**

A montagem para cálculo do DV do nosso número para o banco Crefisa é definido como AAAACCCNNNNNNNNNN, onde:

* AAAA é o código da agência do título, sem DV;
* CCC é o código da carteira (por exemplo, 121);
* NNNNNNNNNN é o nosso número, sem DV.

Rotina Para Cálculo do DV do Nosso Número para o Banco Crefisa - 069:

* Multiplica-se cada algarismo do número formado pela composição dos campos acima pela sequência de multiplicadores 2,1,2,1,2,1,2 (posicionados da direita para a esquerda);
* Se a multiplicação resultar > 9 (por exemplo = 12), somar os dígitos (1 + 2);
* A seguir, somam-se os algarismos dos produtos e o total obtido é dividido por 10;
* O DV é a diferença entre o divisor (10) e o resto da divisão: 10 - (RESTO DA DIVISAO) = DV;
* Se o resto da divisão for zero, o DV é zero.

**Banco Cecred – 085**

Montagem para geração do nosso número para o banco CECRED de acordo com o "Manual Técnico de Cobrança Bancária – Sistema CECRED – padrão CNAB 240 posições – versão 07 (agosto 2016)."  
O nosso número será composto por 17 dígitos incluindo o dígito verificador da conta corrente e deve ser gerado por meio de sequenciais diferentes, não podendo retroagir ou repetir numeração já processada, utiliza-se o número do boleto (nosso número) como critério sequencial.   
A montagem do nosso número será CCCCCCCdNNNNNNNNN, Onde:  
   
CCCCCCC – é a Conta corrente   
D -  é o DV do cooperado (Sempre será fixo)  
NNNNNNNNN – é o Número do boleto (Sequencial)  
   
**Principais Tabelas envolvidas no Processo de Geração de Nosso Número**

FCONVENIO  
GBANCO  
FCONTA  
FBANCOLAYOUTS  
FBOLETO  
FLAN

 Veja Também
