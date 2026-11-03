---
article_id: 360052015894
category: Financeiro - Contas a Receber
content_hash: 0728d552016661fce5dcca5455ac28ff32935d6015a6e1f8bc27ce0f6a786472
fetched_at: '2026-06-28T22:38:13.957172+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA040 - Pontos de
  entrada
type: support-article
updated_at: '2026-03-27T11:44:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052015894-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA040-Pontos-de-entrada
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25946396908311)** Tempo aproximado para leitura: **00:10:00 min**

**Dúvida**Quais são os pontos de entrada disponíveis na rotina **FINA040**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas versões  
  
**Solução**Segue abaixo a relação dos pontos de entrada da rotina **FINA040:**

**F040BROW** - exibição de dados no *browser*

<http://tdn.totvs.com/pages/releaseview.action?pageId=6070862>

**F040FILB** - para inclusão de filtro no *browse*.  
<http://tdn.totvs.com/display/PROT/TVR071_DT_Criacao_do_PE_F040FILB_Ctas_Receber>

**FA040INC** - será utilizado na validação da **TudoOk** na inclusão do **Contas a Receber**  
<https://tdn.totvs.com/pages/viewpage.action?pageId=780767310>

**F040BLQ** - bloqueio de rotinas  
<http://tdn.totvs.com/display/public/mp/F040BLQ+-+Bloqueio+de+rotinas+--+11581>

**F040DTMV** - valida a data de Inclusão do Título  
<http://tdn.totvs.com/pages/releaseview.action?pageId=6071441>

**F040TRVSA1** - permite travar ou destravar os registros da Tabela de Cliente - **SA1**, na rotina Clientes - **MATA030**. Essa ação é possível mesmo se os registros estiverem sendo utilizados por uma *thread*.  
<http://tdn.totvs.com/pages/viewpage.action?pageId=185737827>

**F040CANVM** - exclusão de título com Correção Monetária  
<http://tdn.totvs.com/pages/releaseview.action?pageId=6071678>

**FA040B01** - será executado após confirmar a exclusão e antes da gravação dos dados complementares. Se o retorno for .F., não se prosseguirá a deleção do título.  
<http://tdn.totvs.com/pages/releaseview.action?pageId=6071095>

**Fa040DEL** -  tem como finalidade permitir executar rotinas personalizadas após o termino do processamento de exclusão do título, a partir da opção '**Excluir**' do cadastro de **Contas a Receber**. Neste ponto de entrada o título a receber já foi excluído da base de dados de contas a receber. Não recebe parâmetros e não retorna nenhum resultado.  
<http://tdn.totvs.com/display/public/mp/FA040DEL+-+Executa+rotinas+personalizadas+--+11842>

**F040ALN** -  permite ou não a alteração da natureza (cálculo de impostos) no **Contas a Receber**, após a contabilização do título.  
<http://tdn.totvs.com/pages/releaseview.action?pageId=6070859>

**F040RECIMP** -  permite que os títulos a receber gerados por outros módulos, ao alterar a data de vencimento, os impostos sejam recalculados.  
<http://tdn.totvs.com/pages/releaseview.action?pageId=6071677>

**F040VENCR** - verifica a data de vencimento informada.  
<http://tdn.totvs.com/display/public/mp/F040VENCR+-+Verifica+Data+de+Vencimento+--+24320>

**F40DELPR** - para que seja definida a utilização do processo de substituição de provisórios com a deleção do título provisório (método antigo).  
<http://tdn.totvs.com/display/public/mp/F40DELPR+--+115725>

**F040PROV** - possibilita a intervenção antes da exclusão do título original na rotina **Contas a Receber** ao utilizar o botão SUBSTITUIR (**FINA040**).  
<http://tdn.totvs.com/pages/releaseview.action?pageId=6071450>

**FA040ALT** - será executado na validação da alteração dos dados do **Contas a Receber**.   
<http://tdn.totvs.com/pages/releaseview.action?pageId=6071094>

**FA40Prot** - executado ao entrar na rotina de Alteração do Contas a Receber. Também é utilizado para visualizar os dados das **Faturas a Recebe**r.  
<http://tdn.totvs.com/display/public/PROT/FA40PROT+-+Visualiza+dados++das+Faturas+a+Receber>

**F040ALT** -  valida os dados da alteração após a confirmação da mesma.  
<http://tdn.totvs.com/pages/releaseview.action?pageId=6070860>

**F04MONTDD** - permite a formatação do desdobramento.  
<http://tdn.totvs.com/display/PROT/DT+ponto+de+entrada+F04MONTDD>

**F40DTDSD** -  acionado no momento da confirmação do desdobramento de um título no **Contas a Receber**, permite alterar a data inicial para geração dos novos títulos.  
<http://tdn.totvs.com/display/PROT/F40DTDSD_DT_Manipulacao_data_inicial>

**F040COM** - executado durante a gravação dos dados do título do contas a receber, com a finalidade de tratar a comissão de títulos **RA**. Só será executado quando **E1\_TIPO =** "**RA**".  
<http://tdn.totvs.com/pages/releaseview.action?pageId=6070864>

**FA040GRV** - executado após a gravação de todos os dados referentes ao título e antes da contabilização.  
<http://tdn.totvs.com/pages/releaseview.action?pageId=6071098>

**FA040FIN** - chamado no programa de inclusão de contas a receber, após o fim do *Begin Transaction*.  
<http://tdn.totvs.com/display/public/mp/FA040FIN+-+Trata+dados+--+11843>

**F040FCR** -  permite a manipulação de dados gravados após a inclusão de um título a receber, inclusive se este título for um abatimento.  
<http://tdn.totvs.com/pages/releaseview.action?pageId=6071590>

**F040NDINC** - inibir a geração dos títulos DDI no **Contas a Receber**  
<http://tdn.totvs.com/pages/viewpage.action?pageId=22480557>

**F040CPO** - utilizado na manipulação dos campos que terão permissão para alteração nos títulos a receber.  
<http://tdn.totvs.com/pages/releaseview.action?pageId=6070865>

**FA040S** - foi substituído pelos pontos de entrada **FA040S1** e **FA040S2**.  
Neste devem ser declarados os campos usando M- de acordo com os campos a serem inicializados. Supondo que tenha um campo com nome **E1\_CAMPO** a sintaxe seria. M- **E1\_CAMPO** := Este campo foi inicializado para substituição.  
<http://tdn.totvs.com/pages/releaseview.action?pageId=6071100>

**FA040SUB** - essa função tem o objetivo de substituir os títulos lançados como **Tipo = PR,** títulos provisórios.  
<http://tdn.totvs.com/pages/releaseview.action?pageId=46078676>

**F040DTDES** - permite alterar a data de emissão dos novos títulos a receber que serão gerados após o desdobramento do título principal.  
<http://tdn.totvs.com/pages/releaseview.action?pageId=6071551>

**F040BUT** -  adiciona botões do usuário na *EnchoiceBar*. Retorna o *array* com os novos botões (*aUsButtons*).  
<http://tdn.totvs.com/pages/releaseview.action?pageId=6070863>

**F040FRT** - manipulação de filiais no cálculo de impostos.  
<http://tdn.totvs.com/pages/releaseview.action?pageId=6071631>

**F040GRCOM** - permite a gravação de dados após a confirmação de ocorrências **CNAB** de documentos a receber do tipo abatimento.  
<http://tdn.totvs.com/pages/releaseview.action?pageId=6071626>

**DEFFI2** - utilizado para definir o tipo de ocorrência **CNAB** padrão. Retorna o *array* *aDefaults* com os tipos de ocorrência. É passado como parâmetro: '**R'**, **aCpos**, **aDados**, **lAbatim**, **lProtesto**, **lCancProt**.  
<http://tdn.totvs.com/display/public/mp/DEFFI2+-+Tipo+de+ocorrencia+CNAB+--+11568>  
<https://tdn.totvs.com/display/PROT/DEFFI2+-+Tipo+de+ocorrencia+CNAB>

**FI040ROT** - inclusão de novos itens no menu **aRotina**   
<http://tdn.totvs.com/pages/viewpage.action?pageId=465401168>

**F040MOV** -  permite gravações complementares no momento de gravar o movimento bancário do **RA**, anterior a atualização dos saldos bancários. Não possui retorno.  
<http://tdn.totvs.com/pages/releaseview.action?pageId=6070872>

**F040ERA** -  executado após o estorno da **PA** na movimentação bancária, como complementar a gravação dos dados no **SE5**.  
<http://tdn.totvs.com/pages/releaseview.action?pageId=6070867>

**F040DELC** -  acionado no cancelamento da liquidação de um título já contabilizado, por default a rotina envia um array (**PARAMIXB**) com as informações do próximo registro que será gravado na **SE5**, além da tabela **SE1** estar posicionada no registro que está sendo cancelado.  
<http://tdn.totvs.com/display/PROT/TVSASN_DT_Documentacao_F040DELC>
