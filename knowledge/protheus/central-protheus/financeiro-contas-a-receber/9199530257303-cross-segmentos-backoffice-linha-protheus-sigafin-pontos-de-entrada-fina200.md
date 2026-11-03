---
article_id: 9199530257303
category: Financeiro - Contas a Receber
content_hash: 7f5d912cb5884766f72d785586f94f26a4ce57ec519740817638b02b9e60a107
fetched_at: '2026-06-28T22:38:14.128754+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Pontos de entrada FINA200
type: support-article
updated_at: '2022-11-28T15:22:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9199530257303-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Pontos-de-entrada-FINA200
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:10:00 min**

**Dúvida**Quais os pontos de entrada da rotina FINA200?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA200 - Todas as versões  
  
**Solução**Para customização dos pontos de entrada na rotina **FINA200** existem as opções abaixo:

**F200PORT - Definição de banco na baixa**O ponto de entrada **F200PORT** é utilizado para definir o banco a ser utilizado na baixa do título no retorno **CNAB a Receber .T.** = Utiliza o portador do título, ignorando o banco do retorno CNAB (padrão caso não exista o ponto de entrada) .F. = Utiliza o banco do retorno CNAB   
Para maiores informações, consulte: [F200PORT - Definição de banco na baixa](https://tdn.totvs.com/pages/releaseview.action?pageId=6070980)  
  
**200GEMBX**O ponto de entrada **200GEMBX** tratará os valores dos títulos na rotina de retorno da comunicação bancária. O tratamento deste ponto de entrada é igual ao do ponto de entrada padrão do financeiro F200VAR, onde o array com os valores dos títulos pode ser manipulado dentro do ponto de entrada.  
Para maiores informações, consulte: [200GEMBX](https://tdn.totvs.com/display/public/mp/200GEMBX)  
  
**F200VAR - Manipular variáveis no processamento do retorno**O ponto de entrada **F200VAR** do **CNAB a receber** será executado após carregar os dados do arquivo de recepção bancaria e será utilizado para alterar os dados recebidos.  
Para maiores informações, consulte :[F200VAR - CNAB Receber - Manipular variáveis no processamento do retorno](https://tdn.totvs.com/pages/releaseview.action?pageId=235308494)  
  
**F200AVL - Prevê retorno de valor lógico VF**  
O Array passado como parâmetro permitirá que qualquer exceção ou necessidade seja tratada através do ponto de entrada. No momento da chamada do ponto de entrada, as tabelas **SEE** e **SA6** estão posicionadas. O ponto de entrada prevê retorno de um valor lógico (verdadeiro ou falso) sendo: quando retorno for verdadeiro, continua a execução da rotina normalmente; quando retorno for falso, a rotina executará um "Loop", ou seja, o processamento da linha atual do arquivo de retorno será abortado e a rotina continuará executando a partir da linha seguinte. Estrutura do Array:[01] - Número do Título[02] - Data da Baixa[03] - Tipo do Título[04] - Nosso Número[05] - Valor da Despesa[06] - Valor do Desconto[07] - Valor do Abatimento[08] - Valor Recebido[09] - Juros[10] - Multa[11] - Outras Despesas[12] - Valor do Crédito[13] - Data Crédito[14] - Ocorrência[15] - Motivo da Baixa[16] - Linha Inteira[17] - Data de Vencto.  
Para maiores informações, consulte: [F200AVL - Preve retorno de valor lógico VF](https://tdn.totvs.com/pages/releaseview.action?pageId=6071394)  
  
**F200POS - Processa dados de CNAB a receber**O ponto de entrada **FA200POS** é inserido após o posicionamento do **SEB (Ocorrências bancárias)**, chamado no processamento de todas as linhas do arquivo de retorno, antes da execução das ações correspondentes à ocorrência e da localização / posicionamento do título correspondente no **SE1**. Para a localização do Título correspondente no **SE1**, foram disponibilizadas as seguintes variáveis: cNumTit: Contém o Prefixo + Número + Parcela do título; cEspecie: Contém o Tipo do Título.  
Para maiores informações, consulte: [FA200POS - Processa dados de CNAB a receber](https://tdn.totvs.com/display/public/mp/FA200POS+-+Processa+dados+de+CNAB+a+receber+--+11957)  
  
**FA200SEB - Análise das ocorrências**Ponto de entrada para análise das ocorrências, para permitir a execução de um tratamento diferenciado  
Para maiores informações, consulte: [FA200SEB - Análise das ocorrências](https://tdn.totvs.com/pages/releaseview.action?pageId=6071390)  
  
**FA200FIL  - Substitui pesquisa**Ponto de entrada executado em substituição à rotina de pesquisa padrão do título do arquivo de retorno do banco, na tabela de contas a receber **SE1**, que realiza o **IDCNAB** ou chave do título. Nesta rotina de pesquisa padrão, também é realizada a validação da espécie do título com a **tabela 17**.    
Para maiores informações, consulte: [FA200FIL - Substitui pesquisa](https://tdn.totvs.com/display/public/mp/FA200FIL+-+Substitui+pesquisa+--+11956)  
  
**F200ABAT - Tratamento de abatimento e desconto**O ponto de entrada **F200ABAT** trata de abatimento e desconto.  
Para maiores informações, consulte: [F200ABAT - Tratamento de abatimento e desconto](https://tdn.totvs.com/display/public/mp/F200ABAT+-+Tratamento+de+abatimento+e+desconto+--+24110)  
  
**FINA200 - Executado antes da gravação dos dados**O ponto de entrada **FINA200** será executado antes da gravação dos dados dos títulos que serão baixados .Algumas variáveis poderão ter seu conteúdo alterado: **nValRec**: Valor total recebido - **nTotAbat**: Valor total abatimento - **dDataCred**: Data do Crédito.  
Para maiores informações, consulte: [FINA200 - Executado antes da gravação dos dados](https://tdn.totvs.com/pages/releaseview.action?pageId=6071287)  
  
**FA200\_02 - Confirma entrada de título**O ponto de entrada **FA200\_02** é executado após a gravação dos dados de um título que teve a entrada confirmada (**ocorrência = 02**).  
Para maiores informações, consulte: [FA200\_02 - Confirma entrada de título](https://tdn.totvs.com/pages/releaseview.action?pageId=6071193)  
  
**F200TIT - Tratamento de dados após baixa de títulos no recebimento de cobranças**O ponto de entrada **F200TIT** do **CNAB a receber**, será executado após o Sistema ler a linha de detalhe e gravar todos os dados.  
Para maiores informações, consulte: [F200TIT – Tratamento de dados após baixa de títulos no recebimento de cobranças.](https://tdn.totvs.com/x/SrKFJw)  
  
**FA200F1 - Grava dados CNAB a receber**O ponto de entrada **FA200F1** é executado após a gravação da linha de lançamento contábil no arquivo de Contra-Prova.Só será executado se o ponto de entrada **FA200FIL** também existir.  
Para maiores informações, consulte: [FA200F1 - Grava dados CNAB a receber](https://tdn.totvs.com/display/public/mp/FA200F1+-+Grava+dados+CNAB+a+receber+--+11955)  
  
**F200FIM - Gravação de linha de lançamento**O ponto de entrada **F200FIM** do CNAB a receber será executado após gravar a linha de lançamento contábil no arquivo de contra-prova.  
Para maiores informações, consulte:[F200FIM - Gravação de linha de lançamento](https://tdn.totvs.com/pages/releaseview.action?pageId=6070979)  
  
**F200BXAG - CNAB a receber**O ponto de entrada **F200BXAG** será utilizado no **CNAB a receber**, após gravar o movimento de baixa aglutinada no **SE5**.  
Para maiores informações, consulte: [F200BXAG - CNAB a receber](https://tdn.totvs.com/display/public/mp/F200BXAG+-+CNAB+a+receber+--+11712)  
  
**F200IMP**O ponto de entrada **F200IMP** permite a gravação dos dados adicionais no momento do recebimento do arquivo em comunicação bancária/retorno cobrança.  
Para maiores informações, consulte: [F200IMP](https://tdn.totvs.com/display/public/PROT/F200IMP)  
  
**FA200RE2**O ponto de entrada **FA200RE2** é executado antes da gravação dos dados quando um registro é rejeitado.  
Para maiores informações, consulte: [FA200RE2 - Rejeita registros - CNAB a receber](https://tdn.totvs.com/display/public/mp/FA200RE2+-+Rejeita+registros+-+CNAB+a+receber+--+11958)  
  
**FA200REJ - Rejeita registros CNAB a receber  
CNAB RECEBER**   Executado após a gravação do registro rejeitado.  
Para maiores informações, consulte:[FA200REJ - Rejeita registros CNAB a recber](https://tdn.totvs.com/display/public/mp/FA200REJ+-+Rejeita+registros+CNAB+a+recber+--+11959)  
  
**F200DB1 - CNAB a receber**O ponto de entrada **F200DB1** utilizado no **CNAB a receber**, será executado após gravar as despesas bancarias no **SE5**.  
Para maiores informações, consulte :[F200DB1 - CNAB a receber](https://tdn.totvs.com/display/public/mp/F200DB1+-+CNAB+a+receber+--+11713)  
  
**F200DB2 - CNAB a receber**O ponto de entrada **F200DB2**, utilizado no **CNAB a receber**, será executado após gravar as outras despesas bancarias no **SE5**.  
Para maiores informações, consulte: :[F200DB2 - CNAB a receber](https://tdn.totvs.com/display/public/mp/F200DB2+-+CNAB+a+receber+--+11714)  
  
**F060SEA - Alteração das informações adicionais na tabela SEA**O ponto de entrada **F060SEA** será executado durante a gravação dos dados do **borderô (SEA)** na transferência.  
Para maiores informações, consulte:: [DT\_F060SEA\_Gravação\_de\_dados\_do\_borderô](https://tdn.totvs.com/pages/releaseview.action?pageId=465391018)  
  
**F060SEA2 - Alteração das informações adicionais na tabela SEA**O ponto de entrada **F060SEA2** altera antes de gravar, ou grava informações adicionais na tabela **SEA** na geração do Borderô.  
Para maiores informações, consulte: [F060SEA2 - Alteração das informações adicionais na tabela SEA](https://tdn.totvs.com/pages/releaseview.action?pageId=6071651)  
  
**F200CUS E F650CUS NAO VALIDA\_TIPO\_DE\_REGISTRO**Pontos de entradas criados para ignorar o tipo de registro lido. Válido apenas para modelo 1.  
Para maiores informações, consulte:  
[DT\_F200CUS\_E\_F650CUS\_NAO\_VALIDA\_TIPO\_DE\_REGISTRO](https://tdn.totvs.com/display/public/PROT/DT_F200CUS_E_F650CUS_NAO_VALIDA_TIPO_DE_REGISTRO)  
  
**F200CNAB Aglutinação dos títulos do borderô**  
O ponto de entrada **F200CNAB** retorna se os títulos do borderô serão, ou não, aglutinados.  
Para maiores informações, consulte: [DT\_F200GLOG\_gravacao\_de\_log\_recebimento\_CNAB](https://tdn.totvs.com/display/public/PROT/DT_F200GLOG_gravacao_de_log_recebimento_CNAB)  
  
**F200GLOG gravação de log recebimento CNAB**  
Criado ponto de entrada para informar se será gravado as tabelas de LOG de **CNAB** para todos processados ou somente para as baixas efetivadas.   
Para maiores informações, consulte: [DT\_F200GLOG\_gravacao\_de\_log\_recebimento\_CNAB](https://tdn.totvs.com/display/public/PROT/DT_F200GLOG_gravacao_de_log_recebimento_CNAB)  
  
**F200OCR Gravação complementar outros créditos**  
**Comunicação Bancaria**   
Para maiores informações, consulte: [DT\_F200OCR\_Gravacao\_complementar\_outros\_creditos](https://tdn.totvs.com/display/public/PROT/DT_F200OCR_Gravacao_complementar_outros_creditos)
