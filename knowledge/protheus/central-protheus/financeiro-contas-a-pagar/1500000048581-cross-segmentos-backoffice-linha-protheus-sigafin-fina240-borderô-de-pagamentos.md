---
article_id: 1500000048581
category: Financeiro - Contas a Pagar
content_hash: 58c23b209f4ad498199bb65d9f457343fd59966a93dddf985c2d38b69cd8e413
fetched_at: '2026-06-28T22:38:09.605835+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA240 - Borderô de
  Pagamentos - Ponto de Entrada
type: support-article
updated_at: '2022-08-17T22:41:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000048581-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA240-Border%C3%B4-de-Pagamentos-Ponto-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min**  
**Dúvida**Quais os Pontos de Entrada  da rotina FINA240 ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA240 - Todas as versões  
  
**Solução**Os pontos de entrada da rotina **FINA240** são:

**F240BROWSE - Filtro abertura do browse**Ponto de entrada que permite realizar um filtro na abertura do browse de borderô de pagamentos.  
Para maiores informações, consulte: [F240BROWSE - Filtro de browse no borderô de pagamentos](https://tdn.totvs.com/pages/releaseview.action?pageId=641154226)

**F240ADCM - Customização de browse de borderô**O ponto de entrada F240ADCM permite customizar a browse de borderôs, incluindo campos a serem exibidos junto aos já configurados padrão, alimentando uma array contendo esses campos.Exemplo:User Function F240ADCM()Local aCamposADCM := {}aAdd(aCamposADCM,'E2\_CODBAR')Return aCamposADCM  
Para maiores informações, consulte: [F240ADCM - Customização de browse de borderô](https://tdn.totvs.com/pages/releaseview.action?pageId=6071345)  
  
**F240SEMA - Não uso de semáforo no borderô**O ponto de entrada F240SEMA tem como finalidade permitir ao usuário não utilizar o semáforo na preparação do borderô de pagamentos.  
Recomenda-se muito cuidado ao utilizar este ponto de entrada, pois o semáforo tem a função de inibir o uso da rotina por mais de um usuário, evitando a marcação de um mesmo titulo por dois usuários diferentes.  
Para maiores informações, consulte: [F240SEMA - Não uso de semáforo no borderô](https://tdn.totvs.com/pages/releaseview.action?pageId=6070993)

**F240BOR - Inibe a utilização do campo número na rotina de b****orderô**Ponto de entrada para inibir a utilização do campo Numero na rotina de Borderô de Pagamentos.  
Para maiores informações, consulte: [F240BOR - Inibe a utilização do campo número na rotina de Bordero](https://tdn.totvs.com/pages/releaseview.action?pageId=6071454)  
  
**F240GAVE - Manipula Filtro para montagem de borderô**Ponto de entrada para manipulação dos dados de filtro para montagem do borderô.  
Para maiores informações, consulte: [F240GAVE - Manipula Filtro para montagem de borderô](https://tdn.totvs.com/pages/releaseview.action?pageId=6071420)  
  
**F240FIL - Montagem de filtro**O ponto de entrada F240FIL sera utilizado para montar o filtro para Indregua apos preenchimento da tela de dados do bordero. O filtro retornado pelo ponto de entrada será anexado ao filtro padrão do programa.  
Para maiores informações, consulte: [F240FIL - Acrescenta filtro na seleção de títulos para borderôs de pagamento](https://tdn.totvs.com/pages/releaseview.action?pageId=632830662)  
  
**F240MARK - Altera posição de campos em FINA240**O ponto entrada F240MARK altera as posições dos campos de tela MarkBrowse  
Para maiores informações, consulte: [F240MARK - Altera posição de campos em FINA240](https://tdn.totvs.com/pages/releaseview.action?pageId=6071372)

**F240BTN - Novos botões**Ponto de entrada permite incluir novos botões na enchoice bar da tela de seleção de titulo para a geração de borderô de pagamentos.  
Para maiores informações, consulte: [F240BTN - Novos Botões](https://tdn.totvs.com/pages/releaseview.action?pageId=6071709)

**F240TDOK - Geração do borderô**O ponto de entrada F240TDOK é utilizado para validações complementares dos títulos selecionados na geração do borderô, será executado apenas se for confirmada esta geração.  
Para maiores informações, consulte: [F240TDOK - Validação dos títulos selecionados para o borderô](https://tdn.totvs.com/pages/releaseview.action?pageId=641439209)

**F240TBOR - Borderô de pagamento**O ponto de entrada F240TBOR sera executado após a gravação dos dados do borderô de pagamento.  
Para maiores informações, consulte: [F240TBOR - Borderô de pagamento](https://tdn.totvs.com/pages/releaseview.action?pageId=6070994)

**F240BORD - Tratamento complementar**O ponto de entrada F240BORD sera utilizado para tratamento complementar, apos a gravação do borderô.  
Para maiores informações, consulte: [F240BORD - Tratamento complementar](https://tdn.totvs.com/display/public/mp/F240BORD+-+Tratamento+complementar+--+11721)

**F240NBOR - Valida número borderô**Ponto de Entrada F240NBOR serve para validar o numero do borderô digitado.  
Para maiores informações, consulte: [DT\_ F240NBOR\_valida\_numero\_borderô](https://tdn.totvs.com/pages/viewpage.action?pageId=248579306)

**F240OK - Controle de cancelamento de borderô**O ponto de entrada F240OK faz um controle de cancelamento de borderô permitindo ou não cancela-lo.  
Para maiores informações, consulte: [F240OK - Controle de cancelamento de borderô](https://tdn.totvs.com/pages/releaseview.action?pageId=6070991)

**F240PCB - Cancelamento de borderô**

O ponto de entrada F240PCB esta relacionado ao cancelamento de borderô, verificando se este pode ser cancelado ou não.  
Para maiores informações, consulte: [F240PCB - Cancelamento de borderô](https://tdn.totvs.com/pages/releaseview.action?pageId=6070992)

**F240CAN - Tratamento de cancelamento de borderô**

O ponto de entrada F240CAN sera utilizado no tratamento complementar do cancelamento do borderô e sera executado apos excluir o registro no arquivo de borderôs (SEA).  
Para maiores informações, consulte: [F240CAN - Tratamento de cancelamento de borderô](https://tdn.totvs.com/pages/releaseview.action?pageId=6070986)

**F240FPGT - Retorno expressão para índice condicional**

**F240GER - Efetua verificação para gerar SISPAG**O ponto de entrada F240GER faz a verificação e permite gerar ou não o SISPAG.  
Para maiores informações, consulte: [F240GER - Efetua verificação para gerar SISPAG](https://tdn.totvs.com/pages/releaseview.action?pageId=6070989)

**F240ARQ - Informação do borderô**O ponto de entrada F240ARQ sera executado assim que o usuário informar o borderô e antes de se posicionar nele. Sera utilizado para verificar a existência de arquivo com o mesmo nome contido no parâmetro MV\_PAR03 (nome do arquivo de saída a ser gerado).  
Para maiores informações, consulte: [F240ARQ - Informação do borderô](https://tdn.totvs.com/pages/releaseview.action?pageId=6070984)

**F240BCO - Banco ITAU**Ponto de Entrada F240BCO irá identificar se o banco é ITAU.  
Para maiores informações, consulte: [DT\_PE\_F240BCO\_Banco\_ITAU](https://tdn.totvs.com/display/PROT/DT_PE_F240BCO_Banco_ITAU)

**F240ALMOD - Alteração de conteúdo**O ponto de entrada F240ALMOD sera utilizado para alterar o conteúdo do EA\_MODELO na geração do Sispag. Passa como parâmetro o cModelo, que contem o valor do EA\_MODELO. Recebe como retorno o cModelo.  
Para maiores informações, consulte: [F240ALMOD - Alteração de conteúdo](https://tdn.totvs.com/pages/releaseview.action?pageId=6070983)

**F240FILTC - Expressão complementar para filtro**

O ponto de entrada F240FILTC é utilizado para montar o filtro para Indregua após o preenchimento da tela de dados do borderô na geração do(s) arquivo(s) do SISPAG (FINA300). O filtro retornado pelo ponto de entrada será anexado ao filtro padrão do programa.  
Para maiores informações, consulte: [F240FILTC - Expressão complementar para filtro](https://tdn.totvs.com/pages/releaseview.action?pageId=641154842)

**F240SUM - SISPAG Somavalor F240SUM**O ponto de entrada F240SUM permite alterar o valor recebido no somavalor  
Para maiores informações, consulte: [SISPAG - Somavalor F240SUM](https://tdn.totvs.com/display/public/PROT/SISPAG+-+Somavalor+F240SUM)

**F240SUMA**  
**F240SUMD**  
**F240ICNB - Tratamento icnab**O Ponto de entrada F240ICNB permite tratamento da variável cIdCnab

**F240GRV - Geração de complemento de arquivo SISPAG**O ponto de entrada F240GRV gera complemento de gravação para arquivo de envio Sispag.  
Para maiores informações, consulte: [F240GRV - Geração de complemento de arquivo SISPAG](https://tdn.totvs.com/pages/releaseview.action?pageId=6070990)

**F240TGRV - Término da gravação do arquivo SISPAG**Ponto de entrada que permite customizar regra após o término do processamento e gravação do arquivo de envio SISPAG.  
Para maiores informações, consulte: [F240TGRV - Término da gravação do arquivo SISPAG](https://tdn.totvs.com/pages/releaseview.action?pageId=6071692)

**FA240NAR - Alterar variavel**Ponto de entrada para alterar o nome da variável cArqSaida

**F240TIT - Borderô de pagamento**O ponto de entrada F240TIT sera executado durante a marcação dos títulos que irão compor o borderô de pagamento.  
Para maiores informações, consulte: [F240TIT - Borderô de pagamento](https://tdn.totvs.com/pages/releaseview.action?pageId=6070996)

**F240OK2 - Valida dados do borderô de pagamentos**Criado ponto de entrada F240OK2 que valida os dados do borderô de pagamentos e será ativado pelo clique em OK na rotina Borderô de pagamento.  
Para maiores informações, consulte: [F240OK2 - Validação dos dados do borderô de pagamentos](https://tdn.totvs.com/pages/releaseview.action?pageId=641438714)

**FA240PA - Seleciona PA com movimento bancário**O ponto de entrada FA240PA permite a seleção de PA com movimento bancário na tela de Borderô de pagamento.  
Para maiores informações, consulte: [FA240PA - Seleciona PA com movimento bancário](https://tdn.totvs.com/pages/viewpage.action?pageId=150635423)

**F240IND - Alteração no índice**O ponto de entrada F240IND tem como principal finalidade permitir ao usuário fazer alteração do índice para apresentação dos títulos para a geração do borderô de pagamentos.  
Para maiores informações, consulte: [F240IND - Alteração no índice de exibição dos títulos](https://tdn.totvs.com/pages/releaseview.action?pageId=639938866)

**F240CONF - Confirma geração de borderô**O ponto de entrada F240CONF permite a confirmação da geração do borderô na tela de seleção de títulos a pagar.  
Para maiores informações, consulte: [F240CONF - Confirma geração de borderô](https://tdn.totvs.com/pages/releaseview.action?pageId=6071557)
