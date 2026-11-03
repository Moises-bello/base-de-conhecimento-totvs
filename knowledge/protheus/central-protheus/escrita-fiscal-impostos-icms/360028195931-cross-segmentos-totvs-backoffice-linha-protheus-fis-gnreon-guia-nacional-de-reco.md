---
article_id: 360028195931
category: Escrita Fiscal - Impostos - ICMS
content_hash: f16181385c421a44adf082bc920882a43c19abb6735a19e8d24e023f12c71121
fetched_at: '2026-06-28T22:39:25.964029+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- GNREON Guia Nacional
  de Recolhimento de Tributos
type: support-article
updated_at: '2021-07-28T14:03:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028195931-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-GNREON-Guia-Nacional-de-Recolhimento-de-Tributos
---

**Dúvida**Procedimentos de configuração e utilização da GNRE ON   
  
 **Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Disponível a rotina Guia Nacional de Recolhimento de Tributos Estaduais - Online (GNREON), que contempla as operações de vendas interestaduais

sujeitas à substituição tributária.

Esta função tem por objetivo incorporar GNRE's através de um arquivo texto, gerado pelo contribuinte, no formato XML e permitir a impressão das guias.

O limite para o volume de guias por lote é de 50.

**Importante**

Esta melhoria depende de execução do update de base UPDFIS conforme Procedimentos para Implementação.

**Procedimento para Implementação**

Antes de executar o compatibilizador UPDFIS é imprescindível:

a) Realizar o backup da base de dados do produto em que será executado o compatibilizador (\PROTHEUS11\_DATA\DATA) dicionários de dados SXs (\PROTHEUS11\_DATA\SYSTEM).

b) Os diretórios acima mencionados correspondem à instalação padrão do Protheus, portanto, devem ser alterados conforme o produto instalado na empresa.

c) Essa rotina deve ser executada em modo exclusivo, ou seja, nenhum usuário deve estar utilizando o sistema.

d) Se os dicionários de dados possuírem índices personalizados (criados pelo usuário), antes de executar o compatibilizador, certifique-se de que estão identificados pelo nickname. Caso o compatibilizador necessite criar índices, irá adicioná-los a partir da ordem original instalada pelo Protheus, o que poderá sobrescrever índices personalizados, caso não estejam identificados pelo nickname.

e) O compatibilizador deve ser executado com a Integridade Referencial desativada\*.

**Atenção!**

O procedimento a seguir deve ser realizado por um profissional qualificado como Administrador de Banco de Dados (DBA) ou equivalente!

A ativação indevida da Integridade Referencial pode alterar drasticamente o relacionamento entre tabelas no banco de dados. Portanto, antes de utilizá-la, observe atentamente os procedimentos a seguir:

i. No Configurador (SIGACFG), veja se a empresa utiliza Integridade Referencial, selecionando a opção Integridade/Verificação (APCFG60A).

ii. Se não há Integridade Referencial ativa, são relacionadas em uma nova janela todas as empresas e filiais cadastradas para o sistema e nenhuma delas estarão selecionadas. Neste caso, E SOMENTE NESTE, não é necessário qualquer outro procedimento de ativação ou desativação de integridade, basta finalizar a verificação e aplicar normalmente o compatibilizador, conforme instruções.

iii. Se há Integridade Referencial ativa em todas as empresas e filiais, é exibida uma mensagem na janela Verificação de relacionamento entre tabelas. Confirme a mensagem para que a verificação seja concluída, ou;

iv. Se há Integridade Referencial ativa em uma ou mais empresas, que não na sua totalidade, são relacionadas em uma nova janela todas as empresas e filiais cadastradas para o sistema e, somente, a(s) que possui(em) integridade está(arão) selecionada(s). Anote qual(is) empresa(s) e/ou filial(is) possui(em) a integridade ativada e reserve esta anotação para posterior consulta na reativação (ou ainda, contate nosso Help Desk Framework para informações quanto a um arquivo que contém essa informação).

v. Nestes casos descritos nos itens “iii” ou “iv”, E SOMENTE NESTES CASOS, é necessário desativar tal integridade, selecionando a opção Integridade/ Desativar (APCFG60D).

vi. Quando desativada a Integridade Referencial, execute o compatibilizador, conforme instruções.

vii. Aplicado o compatibilizador, a Integridade Referencial deve ser reativada, SE E SOMENTE SE tiver sido desativada, através da opção Integridade/Ativar (APCFG60). Para isso, tenha em mãos as informações da(s) empresa(s) e/ou filial(is) que possuía(m) ativação da integridade, selecione-a(s) novamente e confirme a ativação.

Contate o Help Desk Framework EM CASO DE DÚVIDAS!

Em Microsiga Protheus® Smart Client, digite U\_UPDSIGAFIS no campo Programa Inicial.  
Clique em OK para continuar.  
Após a confirmação é exibida uma tela para a seleção da empresa em que o dicionário de dados será modificado. Selecione o programa U\_UPDSIGAFIS.  
Ao confirmar é exibida uma mensagem de advertência sobre o backup e a necessidade de sua execução em modo exclusivo.  
Clique em Processar. O primeiro passo da execução é a preparação dos arquivos.   
É apresentada uma mensagem explicativa na tela.  
Em seguida, é exibida a janela Atualização concluída com o histórico (log) de todas as atualizações processadas. Nesse log de atualização são apresentados somente os campos atualizados pelo programa. O compatibilizador cria os campos que ainda não existem no dicionário de dados.  
Clique em Gravar para salvar o histórico (log) apresentado.  
Clique em OK para encerrar o processamento.

**Importante**

Para que o processo da geração da GNRE por produto funcione, será necessária a criação das perguntas Gera Título por Produto? e Gera Guia por Produto? – que são criadas automaticamente pelo compatibilizador UPDFAT31.

**Procedimento para Configuração**

No Configurador (SIGACFG) acesse Ambiente/ Cadastros/ Menus e inclua no menu do módulo Livros Fiscais (SIGAFIS) a opção para execução do GNREON, conforme especificação a seguir:

Nome do Menu: Miscelânea

Submenu: Arq. Magnéticos

Nome da Rotina: GNREON

Programa: GNREON

Tabelas: SF6, SA1, SF3

**Importante**

Os campos: UF Favorecida, Receita, Data de Vencimento e Data de Pagamento são obrigatórios para o layout.

Os campos: E/S (F6\_TIPOIMP = 3=ICMS/ST), Tipo do Imp. (F6\_OPERNF = 2=Saída) e Código de Receita (F6\_CODREC) são obrigatórios para Geração do arquivo GNREON XML.

**Tabela SF6 – Guia de Recolhimento**  
  
**Campo: F6\_OPERNF**

Tipo: Caractere

Tamanho: 1

Formato: @!

Cabeçalho: E/S

Descrição: Entrada ou Saída

Opções: 1=Entrada; 2=Saída

Help: Operação de Entrada / Saída

**Campo: F6\_TIPOIMP**

Tipo: Caractere

Tamanho: 1

Formato: @!

Cabeçalho: Tipo do Imp.

Descrição: Tipo do Imposto

Opções:

0=GUIA ESTADUAL;

1=ICMS;

2=ISS;

3=ICMS/ST;

4=FUNRURAL;

5=SIMPLES FEDERAL;

6=FUNDERSUL;

7=SIMPLES NACIONAL;

8=FUST/FUNTTEL;

9=SENAR;

A=FUMA;

B=DIFAL

Help

Tipo do Imposto

**Campo: F6\_EST**

Tipo: Caractere

Tamanho: 2

Formato: @!

Cabeçalho: Estado

Descrição: Estado de Subst.Tribut.

Help: Estado destino de recolhimento

**Campo: F6\_CODREC**   
Tipo: Caractere  
Tamanho: 15  
Formato: @!  
 Cabeçalho: Cod. Receita  
 Descrição: Código da Receita  
 Help: Código da Receita

**Importante**

No layout da GNREON o campo código de receita contém o tamanho de 6 caracteres, porém a tabela SF6 é utilizada no Protheus para outros registros (SPED Fiscal registro E116), por este motivo o campo F6\_CODREC deve ser criado com o tamanho de 15 caracteres.

Códigos de receitas homologados:

100013 – ICMS Comunicação  
100021 – ICMS Energia Elétrica  
100030 – ICMS Transporte  
100048 – ICMS Substituição Tributária por Apuração  
100056 – ICMS Importação  
100080 – ICMS Recolhimentos Especiais  
100099 – ICMS Subst. Tributária por Operação  
100102 - ICMS Consumidor Final não contribuinte outra UF por Operação  
100110 - ICMS Consumidor Final não contribuinte outra UF por Apuração  
100129 - ICMS Fundo Estadual de Combate à Pobreza por Operação  
100137 - ICMS Fundo Estadual de Combate à Pobreza por Apuração

**Campo: F6\_DTVENC**

Tipo: Data

Tamanho:8

Cabeçalho: Vencimento

Descrição: Vencimento da GNR

Help: Data de Vencimento do recolhimento

Campo: F6\_DTPAGTO

Tipo: Data

Tamanho: 8

Cabeçalho: Dt Pagamento

Descrição: Data do Pagamento

Help: Data de pagamento da Guia de Recolhimento

**Campo: F6\_DOC**

Tipo: Caractere

Tamanho: 9

Formato: @!

Cabeçalho: Documento

Descrição: Número do Documento

Help: Número do Documento

**Campo: F6\_VALOR**

Tipo: Numérico

Tamanho: 14

Decimal: 2

Formato: @E 99,999,999,999.99

Cabeçalho: Valor da GNR

Descrição: Valor da GNR

Help: Valor do recolhimento

**Campo: F6\_NUMCONV**

Tipo: Caractere

Tamanho: 30

Formato: @!

Cabeçalho: Num. Convênio

Descrição: N·m.ou Protoc. do Convênio

Help: Número do convênio ou protocolo/mercadoria. (Campo 15 da GNR)

**Campo: F6\_MESREF**

Tipo: Numérico

Tamanho: 2

Formato: 99

Cabeçalho: Mês ref.

Descrição: Mês de referência

Help: Mês de referência do recolhimento

**Campo: F6\_ANOREF**

Tipo: Numérico

Tamanho: 4

Formato: 9999

Cabeçalho: Ano de Ref.

Descrição: Ano de Referência da GNR

Help: Ano de referência da Guia Nacional de Recolhimento (GNR)

**Campo: F6\_ATMON**

Tipo: Numérico

Tamanho: 14

Decimal: 2

Formato: @E 99,999,999,999.99

Cabeçalho: Atualiz.Mon.

Descrição: Atualização Monetária

Help: Informar a atualização monetária

**Campo: F6\_JUROS**

Tipo: Numérico

Tamanho:14

Decimal: 2

Formato: @E 99,999,999,999.99

Cabeçalho: Juros

Descrição: Valor do Juros

Help: Informar o valor dos juros

**Campo: F6\_MULTA**

Tipo: Numérico

Decimal: 2

Tamanho: 14

Formato: @E 99,999,999,999.99

Cabeçalho: Multa

Descrição: Valor da Multa

Help: Informar o valor da multa

**Campo: F6\_PROCESS**

Tipo: Caractere

Tamanho: 1

Formato: @!

Opções: 1=Sim; 2=Não

Cabeçalho: Processa

Descrição: Processa GNRE

Help: Será preenchido com Sim a Guia de Recolhimento cujo Rotinas GNREs já tenham sido processas. Evitando assim duplicidade.

**Campo: F6\_DETRECE**

Tipo: Caractere

Decimal: 0

Tamanho: 6

Formato: @!

Cabeçalho: Deta\_Receita

Descrição: Detalhamento da Receita

Help: Detalhamento da Receita para o cadastro da GNREON.

**Importante**

A partir deste campo Detalhamento da Receita (F6\_DETRECE) será gerado o detalhamento da receita. Atualmente, para os códigos de recolhimento tratado no Microsiga Protheus®, apenas alguns Estados exigem o preenchimento desta informação, tais como: AL/DF/MA/MT/PB/PE/RO/SC/TO. Para os demais Estados que ainda não tenham este detalhamento este campo deve ficar em branco.

**Campo: F6\_TIPODOC**

Tipo: Caractere

Decimal: 0

Tamanho: 6

Formato: @!

Cabeçalho: Tipo Doc.

Descrição: Tipo do Documento

Help: Tipo do documento para geração da GNREON TAG <c28\_tipoDocOrigem>

**Importante**

É necessário o preenchimento do campo Tipo do Documento quando a GNRE for gerada a partir de uma operação onde o código de receita obriga a geração da TAG <c28\_tipoDocOrigem> “Tipo de Documento”.

Se o código de receita for 100013, 100021, 100030 e 100099 e a espécie do documento fiscal for NF, NFA, SPED, CA, NTST, NFCEE, CTR ou CTE e os códigos a cima tiverem informados nos parâmetrosMV\_GNRCOM, MV\_GNRELE, MV\_GNRTRAN e MV\_RECEINF não será necessário preencher este campo. Caso seja 100056 preencher o campo F6\_TIPODOC conforme necessário.

**Campo: F6\_REF**

Tipo: Caractere

Decimal: 0

Tamanho: 1

Formato: @!

Cabeçalho: Referência

Descrição: Intervalo de Referência

Opções:

1= Mensal.

2= 1Quinzena.

3= 2Quinzena.

4= 1 Decêndio.

5= 2 Decêndio.

6= 3 Decêndio.

Help: Informar o Intervalo de referência

**Campo: F6\_CODPROD**

Tipo: Numérico

Decimal: 0

Tamanho: 2

Formato: 99

Cabeçalho: Produto

Descrição: Código do Produto

Help: Informar o código do produto

**Campo: F6\_INF**

Tipo: Caractere

Tamanho: 80

Formato: @!

Cabeçalho: Informações

Descrição: Informações Adicionais

Help: Informações Adicionais

Obs. Preencher este campo para geração de campo extra para o Estado de Alagoas-AL.

**Tabela SF3 – Livros Fiscais**

**Campo: F3\_ESPECIE**

Tipo: Caracter

Tamanho: 5

Formato: @!

Cabeçalho: Espec.Docum.

Descrição: Espécie do Documento

Help: Espécie do Documento Fiscal

Importante

São considerados somente os documentos de espécie: SPED/NFSC/NTSC/NTST/NFCEE/CTA/CTF/CTR/NFST/ CTM/ CTE.

**Campo: F3\_CHVNFE**

Tipo: Caracter

Tamanho: 44

Formato: @!

Cabeçalho: Vl.Es.Cr/Deb

Descrição: Chave da NFe SEFAZ

Help: Número da Chave de acesso da NFe

**Importante**

Para os Estados RR/AP/MS/PE/MT com o código de receita 100099 - ICMS Substituição Tributária por operação os campos extras devem ser preenchidos com o NUM. CHAVE DE ACESSO A NFE (44) Posições conforme o layout, quando obrigatório.  
Para o Estado RR com o código de receita 100048 - ICMS Substituição Tributária por apuração os campos extras devem ser preenchidos com o NUM. CHAVE DE ACESSO A NFE (44) Posições conforme o layout, quando obrigatório.  
A Chave da NFe SEFAZ será preenchida no campo Chave da NFe SEFAZ (F3\_CHVNFE). Para isso será necessária sua transmissão para SEFAZ via WebService.  
Para a geração do código de receita 100030 para o Estado do Amazonas (AM), será necessário informar o Manifesto de Carga em Complementos (F6\_DESCOMP).  
Para o código de receita 100056 só será gerado a GNREON (XML) se a Guia de Recolhimento for emitida manualmente para os estados:AC/AL/AM/AP/DF/GO/MA/MG/MS/MT/PA/PB/PI/RN/RO/RR/RS/SE/TO.  
As informações decorrentes ao Destinatário serão filtradas da tabela SA2 – Fornecedores, após configurar Cliente, Loja e CNPJ/CPF na tabela SF6 – Guia de Recolhimento.

**Tabela SA1 – Cadastro de Cliente**

**Importante**

A tabela Cadastro de Cliente (SA1) será utilizada para o cadastro do contribuinte Destinatário quando necessário.

**Campo: A1\_NOME**

Tipo: Caracter

Tamanho: 40

Formato: @!

Cabeçalho: Nome

Descrição: Nome do cliente

Help: Nome ou razão social do cliente

**Campo: A1\_INSCR**

Tipo: Caracter

Tamanho: 18

Formato: @!

Cabeçalho: Ins. Estad.

Descrição: Inscrição Estadual

Help: Número da inscrição estadual do cliente.

**Importante**

Para os Estado que a Receita exige o Contribuinte Destinatário.

No preenchimento do Contribuinte Destinatário deve-se seguir a seguinte regra, conforme layout do formato do arquivo:

Caso seja inscrito na UF de Sergipe (SE), preencher os seguintes campos :

Inscrição Estadual  
Razão Social  
Caso seja inscrito na UF Favorecida que não seja Sergipe (SE), preencher o seguinte campo. Ou seja, se o campo Inscrição Estadual (A1\_INSCR) estiver preenchido:

Inscrição Estadual  
Caso contrário, preencher os seguintes campos:

Tipo de Identificação  
Documento de Identificação (CNPJ ou CPF)  
Razão Social  
Município (Código do IBGE)

**Campo: A1\_CGC**

Tipo: Caracter

Tamanho: 14

Formato: @R 99.999.999/9999-99

Cabeçalho: CNPJ/CPF

Descrição: CNPJ/CPF do cliente

Help: Digite o CNPJ (Cadastro Nacional da Pessoa Jurídica) ou CPF (Cadastro de Pessoa Física) do cliente.

**Campo: A1\_COD\_MUN**

Tipo: Caracter

Tamanho: 5

Formato: @9

Cabeçalho: Cd.Município

Descrição: Código do Município

Help: Informe o código do município. No Brasil é o código do IBGE de 5 dígito

**Tabela SB5 – Dados Adicionais do Produto**

**Campo: B5\_CODGNRE**

Tipo: Numérico

Tamanho: 2

Formato: 99

Cabeçalho: Cod.Prod

Descrição: Cód. Prod. GNRE

Help: Informar o código do Produto. Consultar na aba Regras de Preenchimento do Manual para Preenchimento do XML de Lotes os códigos válidos para GNRE.

**Importante**

Para que a geração da GNRE por produto seja criada, utilize o campo Cód. Prod. GNRE (B5\_CODGNRE) da tabela Dados Adicionais do Produto (SB5). Para essa funcionalidade não será necessário à utilização do parâmetro MV\_GNREPRO.

No Configurador (SIGACFG) acesse Módulo/ Cadastros/ Parâmetros, observe a configuração dos parâmetros a seguir. Caso não existam, é necessário criá-los conforme a seguinte estrutura:

Nome da Variável: MV\_SUBTRIB

Tipo: Caractere

Descrição: Número da Inscrição Estadual do contribuinte em outro estado quando houver Substituição Tributária

Exemplo Conteúdo: PE18154502270978

Importante

Caso o parâmetro MV\_SUBTRIB não seja suficiente para detalhar todas as Inscrições Estaduais da empresa, deverão ser criados parâmetros com nome MV\_SUBTRI e final numérico sequencial para acrescentar as demais inscrições. Exemplo: MV\_SUBTRI2, MV\_SUBTRI3, etc.

Em uma nova perspectiva, criamos a tabela CLO, Cadastro de Inscrição Estadual. Desta forma, quem não quiser utilizar o parâmetro, poderá utilizar o cadastro, para isso basta incluir as Inscrições e deixar o parâmetro em branco.

Importante

O parâmetro MV\_SUBTRIB verifica se o contribuinte tem IE na UF do recolhimento. Isso é necessário para o preenchimento do campo Inscrição Estadual

do contribuinte emitente.

Conforme o layout, o Contribuinte Emitente é de preenchimento obrigatório. No preenchimento do Contribuinte Emitente siga a regra, conforme abaixo:

Caso seja inscrito na UF Favorecida, preencher o seguinte campo:

Inscrição Estadual  
Caso contrário, preencher os seguintes campos:

Tipo de Identificação  
Documento de Identificação (CNPJ)  
Razão Social  
Endereço  
UF do endereço  
Município (Código do IBGE)  
CEP (não obrigatório)  
Telefone (não obrigatório)

**Nome da Variável: MV\_ESTADO**

Tipo: Caractere

Conteúdo: SP

Descrição: Sigla do estado da empresa usuária do Sistema, para efeito de cálculo de ICMS (7, 12 ou 18%).

**Nome da Variável: MV\_STUF**

Tipo: Caractere

Descrição: Unidades Federativas que devem ser processadas na apuração das entradas e das saídas do ICMS Subst. Tributária.

Exemplo Conteúdo : AC/AL/AM/BA/GO/MA/MG/PB/PE/PI/RN/RO/RS/SC/TO/SE/AP/CE/MS/PA/PR/RR/MT

Nome da Variável: MV\_STUFS

Tipo: Caractere

Descrição: Unidades Federativas que devem ser processadas na apuração das saídas do ICMS Subst. Tributaria.

Exemplo Conteúdo: AC/AL/AM/BA/GO/MA/MG/PB/PE/PI/RN/RO/RS/SC/TO/SE/AP/CE/MS/PA/PR/RR/MT

**Nome da Variável: MV\_UFGNRE**

Tipo: Caractere

Conteúdo

AC/AL/AM/BA/GO/MA/MG/PB/PE/PI/RN/RO/RS/SC/TO/SE/AP/CE/MS/PA/PR/RR/MT

Descrição: Apenas as UF's que possuem GNRE Online.

**Nome da Variável: MV\_RECEINF**

Tipo

Caractere

Descrição

Informe código da receita por Operação

100099 Subst. Tributária por Operação.

Exemplo Conteúdo: 100099

**Nome da Variável: MV\_GNRCOM**

Tipo: Caractere

Descrição: Informe código da receita por Operação 100013 Comunicação

Exemplo Conteúdo: 100013

**Nome da Variável: MV\_GNRELE**

Tipo: Caractere

Descrição: Informe código da receita por Operação 100021 Energia Elétrica.

Exemplo Conteúdo: 100021

**Nome da Variável: MV\_GNRTRAN**

Tipo: Caractere

Descrição: Informe código da receita por Operação 100030 Transporte.

Exemplo Conteúdo: 100030

**Nome da Variável: MV\_RECEAPU**

Tipo: Caractere

Descrição: Informe código da receita por Apuração.

Exemplo Conteúdo: 100048

**Nome da Variável: MV\_GNDIFAL**

Tipo: Caractere

Descrição: Informe código da receita por Operação. 100102 ICMS complementar EC 87

Exemplo Conteúdo: 100102

**Nome da Variável: MV\_GNFPDIF**

Tipo: Caractere

Descrição: Informe código da receita por Operação. 100129 Fundo de Combate Pobreza EC 87

Exemplo Conteúdo: 100129

**Importante**

A Guia de Recolhimento gerada por Apuração não terá informações sobre documentos, código de cliente entre outros. Sendo assim será necessário analisar o layout da GNREON disponibilizado emhttp://www.gnre.pe.gov.br/.   
Caso o código de receita esteja informado no parâmetro a cima a Guia de Recolhimento deverá ser criada com o código automaticamente.

**Nome da Variável: MV\_DATAPAG**

Tipo: Numérico

Descrição: Informar o número de dias úteis que será utilizado para buscar a Data válida de Pagamento.

Exemplo Conteúdo: 9

**Nome da Variável: MV\_GNRENF**

Tipo: Lógico

Descrição: Habilitar o parâmetro para que não seja gerada a, tela GNRE quando a opção Gera Guia de Recolhimento (MATA460A) estiver como Sim.

Importante

Para que as informações sejam preenchidas automaticamente na geração da GNRE será necessário que o parâmetro MV\_GNRENF seja configurado como .T., isso também para geração automática da informação dos demais parâmetros. Atenção: A geração automática da informação dos demais parâmetros ocorre apenas se a GNRE for gerada na operação. Se a mesma for gerada na apuração, estas informações devem ser preenchidas manualmente.

**Nome da Variável: MV\_GNREREF**

Tipo: Caractere

Descrição: Informe a UF e o Detalhamento da Receita para a GNRE Online.

Importante: Este parâmetro é utilizado quando as informações são geradas por apuração.

**Nome da Variável: MV\_GNREPRO**

Tipo: Caractere

Descrição: Informe o código do Produto para a GNRE.

Exemplo Conteúdo: CE99/AL56

Importante: Caso o campo B5\_CODGNRE não esteja preenchido, o sistema irá considerar os produtos informados no parâmetro MV\_GNREPRO identificando assim, que esta informação será gerada por apuração.

**SX5 - Tabela 88 - Cod. Inf. Extra Chave GNREON**

Criada a tabela 88 para que seja possível incluir o código da informação extra referente à chave da NF-e/ CT-e / DF-e caso tenha alguma alteração.

Exemplo de preenchimento.

Chave: MA (UF)

Descrição: 100099-85/

Obs. A estrutura de preenchimento deve ser conforme exemplo de preenchimento para o correto funcionamento.

Importante

Foi criado uma opção na wizard de configuração para permitir que a GNREON seja gerada filtrada por serie de NF, preenchida no campo serie (SF6\_SERIE) da Guia de Recolhimento. Isso possibilita o cliente gerar GNREON separadas por serie.

Exemplo:

Cliente utiliza duas series de NF no faturamento 01 e 02.   
Gera as notas fiscais e guias de ICMS / ST, cada guia com uma serie preenchida 01 e 02.  
 No momento da geração da GNREON o mesmo decide gerar guias separadas por serie, então será gerada uma GNREON para a série 01 e outra para a série 02.  
Para isso na wizard de configuração, basta preencher a série 01 na opção "Para gerar a guia filtrada por série de NF, informe as séries separadas por (;) Ex: 01;02;" e processar a GNREON.  
Depois repetir o processo de geração da GNREON e preencher a série 02 na opção "Para gerar a guia filtrada por série de NF, informe as séries separadas por (;) Ex: 01;02;" e processar a GNREON.  
Importante as series preenchidas nesse campo deverão ser sempre separadas por ponto e vírgula (;). Exemplo de preenchimento: 01;02;03;  
Importante

Para geração do arquivo .XML foi criado a segunda Wizard, possibilitando o cliente selecionar qual Código de Receita deve ser gerado no arquivo .xml. Esta funcionalidade otimiza o processamento da obrigação fiscal.

Informações Técnicas

Tabelas Utilizadas

SA1 – Clientes

SA2 – Fornecedores

SF3 – Livros Fiscais

SF6 – Guias de Recolhimento

SM0 – Empresas

Função Envolvidas

GNREON - Guia Nacional de Recolhimento de Tributos Estaduais

Sistemas Operacionais

Windows®/Linux®

Link contendo os procedimentos:

<http://tdn.totvs.com/display/public/PROT/FIS0017_GNREON_Guia_Nacional_de_Recolhimento_de_Tributos>
