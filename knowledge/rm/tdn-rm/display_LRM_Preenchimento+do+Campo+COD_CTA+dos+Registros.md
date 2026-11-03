---
content_hash: 84a7995af8a05120707a720a45c04ab99c9962e701f7df1f5324eff421455e6c
fetched_at: '2026-06-29T00:09:19.599133+00:00'
page_id: '422545621'
product: rm
source: tdn-rm
title: Preenchimento do Campo COD_CTA dos Registros
type: documentation
url: https://tdn.totvs.com/display/LRM/Preenchimento+do+Campo+COD_CTA+dos+Registros
version: 4
---

Blocos que consistente o preenchimento do COD\_CTA:

* Bloco A: A170
* Bloco C: C170, C175, C381, C385, C396, C481, C485, C501, C505, C601, C605, C870, C880.
* Bloco D: D100, D101, D105, D201, D205, D300, D350, D501, D505, D601, D605.
* Bloco F: F100, F500, F510, F525, F550.
* Bloco P: P100.
* Bloco M: M400, M410, M800, M810.
* Bloco 1: 1900

***Observação:*** Os blocos A,C, D e M e registro F550 ( gerado através de lançamento fiscal ) seguem a seguinte regra de geração do campo COD\_CTA. Vide "**Regra de seleção de dados contábeis**"

**Regra do Bloco F, exceto o registro F550 (gerado através de lançamento fiscal) que respeita a regra anterior**

Na tela de cadastro de Processos do F100\F500 será habilitado o campo conforme abaixo:

* Caso o sistema esteja integrado com o RM Saldus, aparecerá um campo lookup para o cadastro de Conta Contábil.
* Caso a integração entre RM Liber e RM Saldus esteja desabilitada aparecerá um campo texto para ser informado a Conta Contábil.

**Regra de geração do campo no bloco P**

No encerramento do tributo, buscar o COD\_CTA de acordo com as regras atuais que implementamos para os demais registros conforme "**Regra de seleção de dados contábeis**". Na tabela DPERIODOCONTRIBPREV, armazenar o código da conta no campo CAMPOLIVRE1 que passa a ser chave do registro.

**Regra de geração do campo no registro 1900**

O campo do registro 1900 será gerado com os dados dos registros F500 e F550 que tiverem sido gerados no arquivo do EFD - Contribuições.

**Regra de seleção de dados contábeis**

1. Será considerado a Conta Contábil informada no Item do Lançamento Fiscal  ***(A partir da versão 12.1.25)***
2. Senão, Será considerado o Default Contábil informado no CFOP (Natureza de Operação) associado ao Lançamento Fiscal que possua a Classificação "SPED" informada.
3. Senão for encontrado um Default Contábil na CFOP, será selecionado o Default no *Cadastro do Produto/Serviço* que possua a Classificação "SPED" informada.
4. Não existindo Default Contábil no *Cadastro do Produto/Serviço* será utilizada a conta contábil informada no Cadastro – Produto - Dados Fiscais.

***Importante!*** Contas cadastradas como Débito, serão para os lançamentos fiscais de entrada, e por sua vez, as contas cadastradas como Crédito serão para os lançamentos de saída.

É necessário ter o campo Classificação da Conta preenchido com "SPED"(Em caixa ALTA). - No carregamento do Default contábil será considerado o código da filial também e será priorizado o Default com a filial igual a filial do lançamento e classificação da conta igual a SPED. - Se tiver parametrizado filial no Default contábil com classificação "SPED" e está filial não é a mesma do lançamento a conta contábil será desconsiderada no item daquele lançamento.  
   
**Dispensa de ECD - IN RFB nº 1.774/2017**

Foi modificado a geração do arquivo magnético da EFD Contribuições para gerar a informação "Dispensa de ECD - IN RFB nº 1.774/2017" sempre que no cadastro da Filial, Anexo Dados Fiscais, o campo "**Empresa obrigada - ECD**" estiver **desmarcado** e o campo "Lucro Presumido", na tela de geração da rotina, estiver com opção **diferente** de "Não se aplica".  
Neste caso será criado um registro 0500 fictício e o campo COD\_CTA dos registros abaixo serão afetados.

**Dados do registro 0500 fictício:**

* Campo 02 DT\_ALT: Data de Inclusão fixo 01/11/2017
* Campo 03 COD\_ NAT\_CC: Código da Natureza da Conta igual a 09- outras
* Campo 04 IND\_CTA : Indicador do Tipo da Conta fixo S - Sintética
* Campo 05 NÍVEL: Nível igual a "0"
* Campos 06 COD\_CTA e 07 NOME\_CTA: Código Conta e Descrição fixo "**Dispensa de ECD - IN RFB nº 1.774/2017**"

**Registros Afetados (Conforme Guia Pratico EFD Contribuições Versão 1.27)**

* A170 campo 17
* C170 campo 37
* C175 campo 17
* C381 campo 10
* C385 campo 10
* C396 campo 14
* C481 campo 10
* C485 campo 10
* C501 campo 8
* C505 campo 8
* C601 campo 7
* C605 campo 7
* C870 campo 14
* C880 campo 14
* D100 campo 23
* D101 campo 9
* D105 campo 9
* D201 campo 7
* D205 campo 7
* D300 campo 19
* D350 campo 23
* D501 campo 8
* D505 campo 8
* D601 campo 9
* D605 campo 9
* F100 campo 17
* F120 campo 16
* F130 campo 19
* F500 campo 15
* F510 campo 15
* F525 campo 11
* F550 campo 15
* M400 campo 04
* M410 campo 04
* M800 campo 04
* M810 campo 04
* 1900 campo 13
* P100 campo 11
* 1101 campo 18
