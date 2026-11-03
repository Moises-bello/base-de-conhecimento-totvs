---
content_hash: f9d754578bfe4de241c1d9e0763da40c0e265b606f160c405b2d40d262e150dd
fetched_at: '2026-06-29T00:09:21.846491+00:00'
page_id: '422545925'
product: rm
source: tdn-rm
title: Bloco  F (EFD Contribuições)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545925
version: 106
---

## Demais Documentos e Operações

Informações de documentos que não geram escrituração fiscal como Recibos, RPA´s, receitas de juros, multas.  
São geradas neste bloco informações das retenções de PIS e COFINS, as informações dos créditos sobre depreciação e aquisição de bens do imobilizado e receitas da atividade imobiliária.

Bloco FleftF001**Registro F001 – Abertura do Bloco F**  
Este registro informa se houve movimentação no bloco F.F010**Registro F010 – Identificação do Estabelecimento**  
Gerado para cada filial que possui movimentação no período da escrituração.F100

**Registro F100 – Demais Documentos e Operações Geradora de Contribuições e Créditos**  
Para a geração deste registro são selecionados lançamentos financeiros a pagar e a receber ou lançamentos contábeis conforme regras a seguir:

Origem Financeira

***Observação:*** Para a correta seleção dos lançamentos financeiros Foi criado um processo no qual serão informados os tipos de documento utilizados no TOTVS Gestão Financeira que irão gerar informações  de Contribuição/Crédito.

Parametrização 

Para a geração do F100, deve-se acessar o Módulo de Gestão Fiscal, na aba Cadastros Específicos e acessar o formulário referente aos [Parâmetros de Processo](https://tdn.totvs.com/x/3Ls_HQ), dentro do cadastro, selecione Anexos | Filtro de Operações. Dentro da aba, preencha os parâmetros da operação de acordo com a seguinte documentação: [F100 - Filtro de Operações](https://tdn.totvs.com/pages/viewpage.action?pageId=499103675).

Ao criar o processo deverá ser informado o Tipo de Operação, a Natureza da base de Cálculo do Crédito e se o documento será selecionado pela Data de Emissão, Data de Baixa ou Data de Vencimento. Para cada tipo de documento deverão ser incluídos os Tributos PIS e COFINS com os respectivos CST.

Foi criado o Campo Conta Contábil do Sped no Parâmetro do Processo - Sub Pasta Tipo de Documento. Se houver integração contábil, apresentar lookup para o Cadastro de Plano de Contas da Coligada do contexto e contas globais, se não houver integração apresentar o campo texto para digitação.

Cálculo das Contribuições Docs Não Escriturados

O processo é disparado no sistema Gestão Fiscal no menu Utilitários | Cálculos | [Cálculo das Contribuições Docs Não Escriturados](https://tdn.totvs.com/pages/viewpage.action?pageId=427048633).

Este processo deverá ser executado sempre antes de ser disparada a geração da rotina para que a informação dos tributos seja inserida nos lançamentos financeiros. O processo poderá ser executado sempre que for feita a inclusão de novos lançamentos ou os mesmos sofrerem alteração em seus valores.

Em relação aos parâmetros na Geração da Rotina no Layout do gerador de saídas (Os valores de CST devem ser preenchidos separadas por (;) Ponto e Virgula):

**CST Não Gerar Valores para Notas Sem Direito a Crédito (PIS/COFINS)**: Os registros serão gerados porém sem os valores de PIS/COFINS.

**CST Não Gerar Operações Sem Direito a Crédito (PIS/COFINS)**: Esta opção não será aplicada neste registro.

**Registro F100 - Aplicações Financeiras Consideradas**

Para a geração do F100 considerando Aplicações Financeiras, deve-se acessar o Módulo de Gestão Fiscal, na aba Cadastros Específicos e acessar o formulário referente aos [Parâmetros de Processo](https://tdn.totvs.com/x/3Ls_HQ), dentro do cadastro, selecione Anexos | Filtro de Operações. Dentro da aba, preencha os parâmetros da operação de acordo com a seguinte documentação: [F100 - Aplicação Financeira](https://tdn.totvs.com/x/Y6W5Iw).

***Observação:*** Para a geração do registro F100 sobre aplicações financeiras não é necessário executar o processo do Cálculo dos Documentos não Escriturados. O sistema irá considerar os rendimentos de suas aplicações encerradas dentro do período da geração da rotina automaticamente.

**Registro F100 - Rendimentos Registrados no Extrato de Caixa**

Para a geração do F100 pelo Extrato de caixa, deve acessar o Cadastros | Parâmetros de Processos:

Em anexos | Filtro de Operações , efetue o cadastro e selecione a origem que será considerada no cálculo, o tipo da operação e a  Base de Cálculo. Em anexos | Filtro Tributo, informe os tributos PIS e COFINS com CST correspondente**.**

Aviso

Para geração do F100 por extrato de caixa, será considerado apenas pela operação de "Rendimento Financeiro":

Origem Contábil10Passo 1

Realizar o cadastro de operações contábeis no menu Cadastros | Parâmetros de Processos:

1Passo 2

Encerrar os períodos de apuração PIS/COFINS e conferir os valores do anexo: Detalhamento da Apuração:

Detalhamento da Apuração10Passo 1

Os dados do registro F100 são gerados no arquivo após serem gravados no anexo Detalhamento da Apuração dentro do Período de Apuração.

Para gravar os dados da geração do registro F100 no Detalhamento da Apuração, é necessário encerrar o Período de Apuração;

Encerrando do Período de ApuraçãoDados gravados no anexo Detalhamento da ApuraçãoAVISO

O Cálculo no encerramento do Período de Apuração continua considerando os Parâmetros de Processo, porém os valores sempre serão gerados considerando o tributo principal informado nos parâmetros de rotina conforme documentação: [Parâmetros Rotina](https://tdn.totvs.com/pages/viewpage.action?pageId=842699260)

Outras Documentações

[Rotina Fiscal - Linha RM - TDN (totvs.com)](https://tdn.totvs.com/display/LRM/Rotina+Fiscal)

1Passo 2

Após o detalhamento da apuração ser preenchido, basta executar a rotina EFD-Contribuições para o registro F100 apresentar os dados;

Exemplo do registro F100 geradoF120

**Registro F120 – Bens Incorporados ao Ativo Imobilizado – Operações de Créditos com Base nos Encargos de Depreciação e Amortização**

Registro específico para a escrituração dos créditos determinados com base nos encargos de depreciação de bens incorporados ao Ativo Imobilizado da pessoa jurídica, adquirido para utilização na produção de bens destinados à venda, ou na prestação de serviços, bem como de encargos de amortização relativos a edificações e benfeitorias em

imóveis próprios ou de terceiros.InformaçõesA partir da versão 12.1.27 ao ser gerado o Registro F120, o campo 16 terá como valor considerado a Conta de Depreciação cadastrada no Grupo de Contas.Informações

A partir da versão 12.1.32 é possível realizar a implementação do Registro F120 da EFD Contribuições utilizando o cadastro de Parâmetros de Processos na nova MDI.

Para mais informações acesse seguinte link:

[Parâmetros de Processos](https://tdn.totvs.com/pages/viewpage.action?pageId=490650588)

F130

**Registro F130 – Bens Incorporados ao Ativo Imobilizado – Operações Geradoras de Crédito com Base no Valor de Aquisição/Contribuição**  
Estes registros são gerados com base nas informações dos bens do Imobilizado que estão cadastrados no TOTVS Gestão de Patrimônio.  
Para que as informações sejam selecionadas deverá ser criado um processo através do menu Opções | Parâmetros | Processos – Registro F120 e F130 – Crédito Ativo Imobilizado. Neste processo deve ser informado o Método de Apropriação do Crédito, a Identificação dos bens, Sua utilização e o número de parcelas para aproveitar o crédito caso seja feita a opção pela data de aquisição (F130).  
No filtro de bens devem ser informados quais bens do ativo irão ser declarados e destes quais irão gerar o crédito e quais não irão gerar. Para cada filtro de bem criado deverão ser informados os Tributos PIS e COFINS com seus respectivos CST.  
Para a geração dos campos VL\_OPER\_AQUISICAO e PARC\_OPER\_NAO\_BC\_CRED existe, no cadastro dos parâmetros do processo, as opções:

**C.Aquis (Vr. Base Depreciação): Selecionando esta opção os campos 07 e 08 do F130 serão gerados com base no valor informado no campo VALOR BASE DE DEPRECIAÇÃO do cadastro de patrimônio. Neste campo é informado o valor do Patrimônio com as suas deduções.**

**C.Aquis (vr.Aquisição) :  Ao escolher este opção será verificado se o campo IPATRIMONIOMOEDA.AQUISCAO é maior que zero. Se sim os campos 07 e 08 do F130 serão gerados com base neste valor. Senão, será carregado o valor constante no campo IPATRIMONIO.AQUISICAO para a geração dos campos 07 e 08 do F130.**

***Observação:***Para que os bens sejam selecionados o período no TOTVS Gestão Patrimonial deverá estar liberado para o ano na qual a declaração está sendo gerada.   
Para todos os bens deverá existir a informação do fornecedor.  
Este processo é somente configurado não sendo necessária sua execução  
Se existirem bens para os quais deverão ser carregados valores distintos deverão ser criados quantos processos forem as variações de carga de valor. Ex.: Se existem bens para os quais o registro deva ser gerado com o valor base da depreciação e bens para os quais o registro deva ser gerado com o valor da aquisição deverão ser criados dois processos com a mesma periodicidade.

Informações

A partir da versão 12.1.32 é possível realizar a implementação do Registro F130 da EFD Contribuições utilizando o cadastro de Parâmetros de Processos na nova MDI.

Para mais informações acesse seguinte link:

[Parâmetros de Processos](https://tdn.totvs.com/pages/viewpage.action?pageId=490650588)

F200

**Registro F200 - Operações da Atividade Imobiliária - Unidade Imobiliária Vendida**

F210**Registro F210 - Operações da Atividade Imobiliária – Custo Orçado da Unidade Vendida.**  
Estes registros são gerados com as informações das Unidades Imobiliárias Vendidas e seus custos. Este controle é feito através do TOTVS Incorporação.  
Para a correta geração deste é necessário que seja incluído no processo de seleção das informações menu Opções | Parâmetros | Processos – Registros F200 – Créditos da Atividade Imobiliária os tipos de documento utilizados na geração das informações financeiras das unidades vendidas. Para cada tipo de documento devem ser incluídos os Tributos PIS e COFINS com seus respectivos CST. Este processo é semelhante ao do F100 e também necessita de execução para geração dos tributos nos lançamentos financeiros.  
Para mais informações acesse: Atividades Imobiliárias  
Para informações a respeito do controle das unidades imobiliárias o Help do TOTVS Incorporação deverá ser consultado.F500

**Registro F500 - Consolidação das operações da pessoa jurídica submetida ao regime de tributação com base no lucro presumido - Incidência do PIS/COFINS pelo regime de caixa**  
Uma vez que os dados deste registro representam as receitas efetivamente recebidas no período, serão selecionados os [Lançamentos Financeiros](http://tdn.totvs.com/Registro F130 – Bens Incorporados ao Ativo Imobilizado – Operações Geradoras de Crédito com Base no Valor de Aquisição/Contribuição Estes registros são gerados com base nas informações dos bens do Imobilizado que estão cadastrados no TOTVS Gestão de Patrimônio. Para que as informações sejam selecionadas deverá ser criado um processo através do menu Opções | Parâmetros | Processos – Registro F120 e F130 – Crédito Ativo Imobilizado.Neste processo deve ser informado o Método de Apropriação do Crédito, a Identificação dos bens, Sua utilização e o número de parcelas para aproveitar o crédito caso seja feita a opção pela data de aquisição (F130). No filtro de bens devem ser informados quais bens do ativo irão ser declarados e destes quais irão gerar o crédito e quais não irão gerar. Para cada filtro de bem criado deverão ser informados os Tributos PIS e COFINS com seus respectivos CST. Para a geração dos campos VL_OPER_AQUISICAO e PARC_OPER_NAO_BC_CRED existe, no cadastro dos parâmetros do processo, as opções:) a receber baixados no período informado na tela de geração da rotina cujos [Tipos de Documento](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388695) tenham sido informado no processo F100/F500 criado para a parametrização da rotina. Será gerado um registro para cada combinação de Código de Modelo de Documento, CST e alíquota. Neste registro só serão selecionados lançamentos que possuam na informação dos Tributos os CST: 01, 02, 04, 05, 06, 07, 08, 09, 49 ou 99.  
Foi criado o Campo Conta Contábil do Sped no Parâmetro do Processo - Sub Pasta Tipo de Documento Se houver integração contábil, apresentar lookup para o Cadastro de Plano de Contas da Coligada do contexto e contas globais, se não houver integração apresentar o campo texto para digitação.

A partir do release 12.1.31

Para a geração do F500 , deve acessar a MDI em Cadastros | Parâmetros de Processos:

Selecionar o F500:

Em anexos | Filtro de Operações , efetue o cadastro e selecione a origem que será considerada no cálculo, o tipo da operação e a  Base de Cálculo. Em anexos | Filtro Tributo, informe os tributos PIS e COFINS com CST correspondente**.**

F509

**Registro F509 - Processo Referenciado**  
Este registro não será gerado pois hoje não é possível fazer a associação de processos aos Lançamentos Financeiros.

F510

**Registro F510 - Consolidação das operações da pessoa jurídica submetida ao regime de tributação com base no lucro presumido - Incidência do PIS/COFINS pelo regime de caixa (Apuração da contribuição por unidade de medida do produto - alíquota em reais)**  
Este registro não será gerado. Hoje não é possível associar itens aos lançamentos financeiros.

F550

**Registro F550 - Consolidação das Operações da Pessoa Jurídica Submetida ao Regime de Tributação com Base no Lucro Presumido - Incidência do PIS/PASEP da COFINS pelo Regime de Competência**  
Este registro deve ser gerado quando o contribuinte utilizar o regime de competência. O "Regime de Competência – Escrituração consolidada" com base nos Blocos "A", "C", "D" (Lançamentos Fiscais). E em relação os lançamentos financeiros será gerado com base no Bloco "F100" (Baseado nos Lançamentos Financeiros) considerando a observação do registro F100 citado anteriormente.

Para geração dos campos 04 - VL\_DESC\_PIS e 09 - VL\_DESC\_COFINS, referentes a devolução de venda, será considerado os lançamentos fiscais de entrada, onde na natureza de operação esteja marcada como "Devolução" e dentro do próprio período de geração da rotina mais os valores da diferença entre o valor contábil do lançamento e a base de cálculo dos tributos PIS e COFINS respectivamente.

F525

**Registro F525 - Composição da receita escriturada no período - Detalhamento da receita recebida pelo regime de caixa.**  
Este registro deve ser gerado quando o contribuinte utilizar o regime de caixa para a apuração das contribuições. O total das receitas relacionadas nos registros F525 deverá corresponder ao total das receitas rebebidas, relacionadas no registro F500. O campo 3 (IND\_REC) é preenchido com o valor fixo 01 - Clientes. A chave deste registro é composta pelo CNPJ, CST do PIS, CST da COFINS. A geração deste registro não exige a geração do registro 0150 - Dados dos participantes dos documentos declarados no arquivo.  
Quando houver troca do tipo de regime na empresa (de Competência para regime Caixa), o sistema irá considerar a data informada no campo "Lucro Presumido - Data da Alteração do regime de Competência para Caixa" na tela de geração da rotina. Serão considerados apenas lançamentos financeiros que possuem a data de emissão posterior a data informada.  
Em relação ao parâmetro "Lucro Presumido com base nas informações do Lançamento Fiscal ou Movimento", o sistema irá considerar movimentos do [TOTVS Gestão de Estoque, Compra e Faturamento](http://tdn.totvs.com.br/pages/viewpage.action?pageId=198948835) integrados com o [TOTVS Gestão Financeira](http://tdn.totvs.com.br/pages/viewpage.action?pageId=198948854) e além disso, os Lançamento Fiscais também integrados com o financeiro.

**Operação que não geram valor ou não devem ser consideradas:**

Foram Adicionados dois parâmetros de texto na tela de geração da rotina para que o usuário possa informar os CST's Sem Direito a Crédito e Sem Direito a Debito a ser considerado na Rotina.

**CST - Não Gerar Valores para Notas Sem Direito a Crédito (PIS/COFINS)**

**CST - Não Gerar Operações Sem Direito a Crédito (PIS/COFINS)**

Caso seja informado mais de um CST, é necessário separar os mesmo por  ponto e vírgula "**;**" conforme exemplo abaixo e sem espaços entre os mesmos:

Veja Também

Geração do registro F525 por documentos agrupados por CST - Código da Situação Tributária.

F559

**Registro F559 - Processo referenciado**

Este registro não será gerado. Hoje não é possível associar itens aos lançamentos financeiros.

F560

**Registro F560 - Consolidação das operações da pessoa jurídica submetida ao regime de tributação com base no lucro presumido - Incidência do PIS/COFINS pelo regime de competência (Apuração da contribuição por unidade de medida do produto - alíquota em reais)**  
Este registro não será gerado. Iremos atender através da escrituração detalhada já utilizada pelas empresas optantes pelo Lucro Real.

F569

**Registro F569 - Processo Referenciado**  
Este registro não será gerado porque não é possível associar processos aos [Lançamentos Financeiros](http://tdn.totvs.com.br/pages/viewpage.action?pageId=435104976).

Registro 1900 e 0120

Clique aqui para consultar as informações do registro 1900  
Clique aqui para consultar as informações do registro 0120

F600

**Registro F600 - Contribuições Retidas na Fonte – PIS COFINS**

Neste registro devem ser informados pela pessoa jurídica beneficiária da retenção/recolhimento os valores da contribuição para o PIS/COFINS retidos na Fonte.

InformaçãoEste Registro só será gerado a partir da **Versão 12.1.2406**.Origem Financeira

Este registro tem origem do(s) [lançamento(s) financeiro(s)](https://tdn.totvs.com/pages/viewpage.action?pageId=421388578) a receber que são controlados pelo [TOTVS Gestão Financeira](https://tdn.totvs.com/pages/viewpage.action?pageId=198948854).

Aviso

Para geração do F600, será selecionado somente lançamentos que estiverem baixados e possuam as retenções.

**Valores do lançamento | Tributos**

**Lançamento das retenções**

Aviso

Para que a geração do F600 ocorra com sucesso, o  [tributo](https://tdn.totvs.com/display/LRM/Tributos) inserido deve ter o código da receita preenchido.

**Indicador da Natureza da Receita**

Aviso

Selecione essa opção de acordo com o regime de apuração dos tributos PIS/COFINS informado na retenção acima.

Detalhamento da Apuração10Passo 1

Os dados do registro F600 são gerados no arquivo após serem gravados no anexo Detalhamento da Apuração dentro do Período de Apuração.

Para gravar os dados da geração do registro F600 no Detalhamento da Apuração, é necessário encerrar o Período de Apuração;

Encerrando do Período de ApuraçãoDados gravados no anexo Detalhamento da Apuração

Ao encerrar o período de apuração dos tributos PIS/COFINS, será calculado também as retenções.

O sistema utiliza o campo Indicador da Natureza da Receita do lançamento financeiro para determinar se o valor retido corresponde a uma receita do regime cumulativo ou do regime não cumulativo, conforme exemplo na imagem abaixo:

O Cálculo no encerramento do Período de Apuração continua considerando os Parâmetros de Processo.

Outras Documentações

[Rotina Fiscal - Linha RM - TDN (totvs.com)](https://tdn.totvs.com/display/LRM/Rotina+Fiscal)

1Passo 2Exemplo do registro F600 geradoLayout do Registro

02-IND\_NAT\_RET

* Gerado com a Natureza Retenção Fonte do Período de Apuração\Sub Pasta Detalhamento da Apuração.

03-DT\_RET

* Gerado com a Data da Operação do Período de Apuração\Sub Pasta Detalhamento da Apuração.

04-VL\_BC\_RET

* Gerado com o Valor da Base de Cálculo do Período de Apuração\Sub Pasta Detalhamento da Apuração

05-VL\_RET

* Gerado com o Valor da Operação do Período de Apuração\Sub Pasta Detalhamento da Apuração

06-COD\_REC

* Gerado com o Código da Receita do Período de Apuração\Sub Pasta Detalhamento da Apuração

07-IND\_NAT\_REC

* Gerado com a Natureza da Receita do Período de Apuração\Sub Pasta Detalhamento da Apuração.

08-CNPJ

* Gerado com o CNPJ da Fonte Pagadora do Período de Apuração\Sub Pasta Detalhamento da Apuração.

09-VL\_RET\_PIS

* Gerado com o Valor do Imposto do Período de Apuração\Sub Pasta Detalhamento da Apuração.

10-VL\_RET\_COFINS

* Gerado com o Valor do Imposto do Período de Apuração\Sub Pasta Detalhamento da Apuração.

11-IND\_DEC

* Gerado com a Condição Pessoa Jurídica Declarante do Período de Apuração\Sub Pasta Detalhamento da Apuração.
F700

**Registro F700 - Deduções Diversas**  
Neste registro devem ser informadas as deduções diversas previstas na legislação tributária, inclusive os créditos que não sejam específicos do regime não-cumulativo, passiveis de dedução na determinação da contribuição social a recolher, nos registros M200 (PIS/Pasep) e M600 (COFINS).  
Estas informações serão tratadas como Outros Débitos/Créditos e devem afetar a apuração dos Tributos PIS e COFINS.

F990

**Registro F990 - Encerramento do Bloco F**  
Este registro é gerado automaticamente com a quantidade de linhas existentes no Bloco F.
