---
article_id: 360031234634
category: Financeiro - Contas a Pagar
content_hash: 4d8519f4d2df596f08f733ac1a64d63a2ff758a673ed6da740947a7fd1a832d5
fetched_at: '2026-06-28T22:38:09.561961+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA050 - Pontos de
  Entrada
type: support-article
updated_at: '2025-11-07T20:24:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360031234634-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA050-Pontos-de-Entrada
---

**Dúvida**Quais os Pontos de Entrada  da rotina FINA050?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução:**Os pontos de entrada da rotina **FINA050** são:

**FINALEG -** Utilizado para alterar as legendas de diversas rotinas do financeiro como FINA040, FNA050, FINA740, FINA750 entre outras. Documentação: [FINALEG - Manipula legendas financeiro](https://tdn.totvs.com/display/public/PROT/FINALEG+-+Manipula+legendas+financeiro) **F50PERGUNT** - permite alterar a configuração dos perguntes via rotina automática - *ExecAuto.*  
Documentação: [h](http://tdn.totvs.com/pages/viewpage.action?pageId=203752262)[TTGYM4\_DT\_F50PERGUNT - Configuração de perguntes via ExecAuto](http://tdn.totvs.com/pages/viewpage.action?pageId=203752262)  
  
**F050BROW -** Pré valida dados.  
Documentação: [F050BROW - Pre valida dados](http://tdn.totvs.com/pages/viewpage.action?pageId=6070878)  
  
**F050FILB -**Permite inserir filtro direto no *browse* da rotina.  
Documentação: [TVJQD8\_DT\_Inclusão\_do\_ponto\_de\_entada\_F050FILB](http://tdn.totvs.com/pages/viewpage.action?pageId=241697546)  
  
**FA050UPD -**Utilizado como pre-validação da inclusão / alteração / exclusão.   
Documentação:[FA050UPD - Pré valida inclusão alteração e exclusão](http://tdn.totvs.com/pages/releaseview.action?pageId=6071119)  
  
**FA050INC -** Será executado na validação da tudo *Ok* na inclusão do **Contas a Pagar**.  
Documentação: [FA050INC - Validação ctas a pagar](http://tdn.totvs.com/pages/releaseview.action?pageId=6071109)

**F050ADPC -**Valida a inclusão de um título de adiantamento, quando incluído do pedido de compras no módulo **SIGACOM**.  
Documentação: [F050ADPC - Validar inclusão](http://tdn.totvs.com/pages/releaseview.action?pageId=6071668)

**F050CAN -**Regra ao selecionar o botão "**Cancelar**" na tela de inclusão de títulos a pagar.  
Documentação: [F050CAN - Regra ao cancelar a inclusão de título a pagar](http://tdn.totvs.com/pages/releaseview.action?pageId=6071659)

**FA050Del -**Será executado logo após a confirmação da exclusão do título.  
Documentação: [FA050DEL - Confirmação de exclusão de títulos](http://tdn.totvs.com/pages/releaseview.action?pageId=6071105)

**F050DEL1 -**Valida a permissão da exclusão do título principal (a pagar), cujos títulos filhos (impostos) tenham sofrido baixa.  
Documentação: [F050DEL1 - Exclusão de título principal](http://tdn.totvs.com/pages/releaseview.action?pageId=6071350)

**FA050B01 -**Será executado após a confirmação da exclusão e antes da própria exclusão de contabilização.  
Documentação: [FA050B01 - Confirmação de exclusão](http://tdn.totvs.com/pages/releaseview.action?pageId=6071104)

**FA050RAT -** Será executado quando na exclusão do título houver lançamento padrão. Não terá retorno.  
Documentação: [Fa050RAT - Exclui título com lançamento padrão](http://tdn.totvs.com/pages/releaseview.action?pageId=6071113)  
  
**F050DSE3 -**Permite a manipulação de registros da tabela **SE3**.  
Documentação: [F050DSE3 - Manipulação de Registros na Tabela SE3](http://tdn.totvs.com/pages/releaseview.action?pageId=6071433)

**F050VIS -**Ponto de Entrada acionado ao fechar a tela em modo visualização.  
Documentação: [TVDXDX\_DT\_Documentacao\_pe\_F050VIS](http://tdn.totvs.com/display/PROT/TVDXDX_DT_Documentacao_pe_F050VIS)

**F50DELPR -**Deleta títulos provisórios ao invés de baixa-los.  
Documentação: [F50DELPR - Deleta títulos provisórios em vez de baixar](https://tdn.totvs.com/pages/releaseview.action?pageId=649306210)  
  
**F050PROV -**Permite a alteração do Título provisório na rotina de Substituir o título no **Contas a Pagar.**Documentação: [TVDXID\_DT\_Documentacao\_Pe\_F050PROV](http://tdn.totvs.com/display/PROT/TVDXID_DT_Documentacao_Pe_F050PROV)

**FA050SCL -**Permite a alteração da ordem de classificação dos títulos apresentados para seleção.  
Documentação: [FA050SCL - Alteração na ordem de classificação dos títulos](http://tdn.totvs.com/pages/releaseview.action?pageId=6071386)

**F050LRAT -** Executado após digitar a linha do rateio online para validar a digitação**.**Documentação:[F050LRAT - Linha do rateio on-line](http://tdn.totvs.com/display/public/mp/F050LRAT+-+Linha+do+rateio+on-line+--+11617)  
  
**F050RAT -** Executado durante a validação da aCols no **Rateio** de **Contas a Pagar**.  
Documentação: [F050RAT - Ponto de Entrada executado durante a validação da aCols](http://tdn.totvs.com/pages/viewpage.action?pageId=57410083)

**F050ATP -** Utilizado para definir a aplicação ou não da tabela progressiva de **IRRF** para fornecedores pessoa física.  
Documentação: [F050ATP - Definição de tabela progressiva de IRRF](http://tdn.totvs.com/pages/releaseview.action?pageId=6070877)  
  
**F050CIRF -**Alteração de base de calculo do **IRRF.**Documentação: [TTCOMR\_DT\_F050CIRF\_Alteração\_de\_base\_de\_calculo\_do\_IRRF](http://tdn.totvs.com/pages/viewpage.action?pageId=210046512)

**FA050ALT -**Será executado na validação da tudo *Ok* na alteração dos dados do **Contas a Pagar**.  
Documentação: [FA050ALT - Alteração de dadoscontas a pagar](http://tdn.totvs.com/pages/releaseview.action?pageId=6071103)

**F050ALT -** Utilizado para validação pós confirmação de alteração, executado antes de atualizar saldo do fornecedor.  
Documentação: [F050ALT - Valida alteração](http://tdn.totvs.com/pages/releaseview.action?pageId=6070876)

**FINCDRET -**Retorna os códigos de retenção que devem ser tratados como código único de retenção.  
Documentação: [FINCDRET - Retorna códigos de retenção](http://tdn.totvs.com/pages/releaseview.action?pageId=6071455)

**F050CHEQ -**Permite ao usuário verificar o cheque de PA**.**Documentação: [F050CHEQ - Verificação de cheque de PA](http://tdn.totvs.com/pages/releaseview.action?pageId=6070879)  
  
**F050ACOL -**Executado após a montagem da aCols, para inicializa-la na opção de rateios de **Contas a Pagar**.  
Documentação:[F050ACOL - Inicia opção de rateios de conta a pagar](http://tdn.totvs.com/pages/releaseview.action?pageId=6070875)

**F050HST -**Utilizado na contabilização da exclusão rateada do **Contas a Pagar** passando o histórico do rateio.  
Documentação:[F050HST - Contabilização de exclusão](http://tdn.totvs.com/pages/releaseview.action?pageId=6070885)  
  
**F050ORI -**Permite na exclusão de **Contas a Pagar** com rateio na emissão, manipular a origem deste.  
Documentação:[F050ORI - Exclusão com rateio](http://tdn.totvs.com/pages/releaseview.action?pageId=6070894)  
  
**F050NPROV -**Será executado na rotina de substituição de títulos provisórios.  
Documentação: [F050NPROV - Substituição de títulos provisorios](http://tdn.totvs.com/pages/releaseview.action?pageId=6070893)

**F05MONTDD** - Validação de preenchimento do Campo Desdobramento (**E2\_DESDOBR**) com o Valor Sim.  
Documentação: [DT ponto de entrada F05MONTDD](https://tdn.totvs.com/pages/releaseview.action?pageId=6070903)

**F50DTDSD -**Manipula data inicial para cálculo das parcelas do desdobramento.  
Documentação:[F50DTDSD - Calcula parcelas do desdobramento](http://tdn.totvs.com/display/public/mp/F50DTDSD+-+Calcula+parcelas+do+desdobramento+--+11824)

**F050PRPC -**Utilizado para manipular a aplicação ou não do período inter parcela sobre a primeira parcela.  
Documentação: [F050PRPC - Manipulação de periodo](http://tdn.totvs.com/pages/releaseview.action?pageId=6070897)

**F050AISS -**Executado ao preencher manualmente o campo **E2\_ISS** na inclusão de um titulo a pagar.  
Documentação: [F050AISS - manipular variaveis](http://tdn.totvs.com/display/public/mp/F050AISS+-+manipular+variaveis+--+93303)

**FinVldIns -**Permite validar se a retenção de **INSS** será efetuada ou não baseando-se no parâmetro **MV\_VLRETIN.**Documentação: [FinVldIns - Validação de retenção de INSS](http://tdn.totvs.com/pages/releaseview.action?pageId=6071683)

**F050GRVL -**Executado pelo **X3\_VALID** do campo Título a Pagar (**E2\_VALOR**).  
Documentação: [F050GRVL - Resgate do valor informado no campo E2\_VALOR](http://tdn.totvs.com/display/public/mp/F050GRVL+-+Resgate+do+valor+informado+no+campo+E2_VALOR+--+113276)

**F050PISS -**Permite que o usuário possa informar uma alíquota de ISS diferente da informada no parâmetro **MV\_ALIQISS.**Documentação:[F050PISS - Alíquota de ISS diferente](http://tdn.totvs.com/pages/releaseview.action?pageId=6070896)  
  
**F050INBR -**Utilizado no cálculo do **INSS** com base reduzida, que será executado na inclusão do título ao digitar a natureza.  
Documentação: [F050INBR - Cálculo de INSS](http://tdn.totvs.com/pages/releaseview.action?pageId=6070886)  
  
**F050FCTC** - Despreza contratos a serem acumulados para compor base de cálculo de **IRRF**.  
Documentação:[MP - TMS - Ponto de entrada F050FCTC Despreza Contratos de Carreteiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007376931-MP-TMS-Ponto-de-entrada-F050FCTC-Despreza-Contratos-de-Carreteiro)

**F050INC -**Será utilizado após confirmar a gravação de **Contas a Pagar**, antes da contabilização.  
Documentação: [F050INC - Gravação de contas a pagar](http://tdn.totvs.com/pages/releaseview.action?pageId=6070887)

**FA050GRV -**Utilizado após a gravação de todos os dados (na inclusão do título) e antes da sua contabilização.  
Documentação:<http://tdn.totvs.com/display/public/mp/FA050GRV+-+Grava+dados+--+11855>

**FA050CT -**Permite a execução de comandos na inclusão de um título de **Contas a Pagar** após a criação dos registros na tabela **SEV** e **SEZ.**Documentação:[FA050CT - Executa comandos](http://tdn.totvs.com/display/public/mp/FA050CT+-+Executa+comandos++--+110920)

**FA050FIN -** Possibilita a visualização dos dados da tabela temporária **TMP1**, que contém as informações do rateio (campos da tabela **CTJ**).  
Documentação: [FA050FIN - Trata dados contas a pagar](http://tdn.totvs.com/display/PROT/FA050FIN+-+Tratamento+dos+dados+no+Contas+a+Pagar+--+11854)

**F050IRF -**É chamado antes de ser criada (caso não exista), a natureza de **IRF** no arquivo **SED**Documentação: [F050IRF - Atualização de titulos a pagar](http://tdn.totvs.com/pages/releaseview.action?pageId=6070889)

**F050ISS -**É chamado antes de ser criada (caso não exista), a natureza de **ISS**<br>no arquivo **SED.**Documentação: [F050ISS - Natureza de ISS](http://tdn.totvs.com/display/public/mp/F050ISS+-+Natureza+de+ISS+--+11615)

**F050SES -**Permite à alteração de títulos após a confirmação gravação do título **SEST**.  
Documentação: [DT\_F050SES\_Alteracao\_titulos\_apos\_gravacao\_sest](http://tdn.totvs.com/display/PROT/DT_F050SES_Alteracao_titulos_apos_gravacao_sest)

**F050MCP -** Permite incluir novos campos na opção **Alterar** da rotina **FINA050**.  
Documentação:[DT\_F050MCP\_Adiciona\_campos\_na\_alteracao\_do\_Contas\_a\_pagar](http://tdn.totvs.com/display/PROT/DT_F050MCP_Adiciona_campos_na_alteracao_do_Contas_a_pagar)

**F050TMP1 -** Permite efetuar o rateio customizado.  
Documentação: [F050TMP1 - Rateio Customizado](https://tdn.totvs.com/display/PROT/F050TMP1+-+Rateio+Customizado)

**F050RAUT -** Permite a gravação do rateio pre-configurado na inclusão do contas a pagar via *execauto.*Documentação: [DT\_F050RAUT\_Rateio\_automatico](http://tdn.totvs.com/display/PROT/DT_F050RAUT_Rateio_automatico)

**F050HEAD -** Adiciona novos campos no Rateio. É usado na opção **Substituição** da rotina de **Contas a Pagar**.  
Documentação: [F050HEAD - Inclusão de novos campos.](http://tdn.totvs.com/pages/releaseview.action?pageId=6071707)

**F50CARTMP1 -**Permite incluir campos de usuários na carga do rateio simples pre-configurado.  
Documentação: [F50CARTMP1 - Inclusão de campos no rateio simples](http://tdn.totvs.com/pages/releaseview.action?pageId=6071327)  
  
**F050LRCT -**Utilizado para validar a linha do rateio online.  
Documentação: [F050LRCT - Validação da linha do rateio](http://tdn.totvs.com/pages/viewpage.action?pageId=63864943)  
  
**F0502RAT -**Permite adicionar validações no rateio **Contas a Pagar** sem desviar das validações do padrão.  
Documentação:[F0502RAT - Validação no rateio](http://tdn.totvs.com/pages/releaseview.action?pageId=6070874)  
  
**F050VLCOD -**Rateio de **Contas a Pagar** com **multi-naturezas**.  
Documentação: [F050VLCOD - Rateio de Contas a Pagar com multi-naturezas.](http://tdn.totvs.com/pages/viewpage.action?pageId=146966736)  
  
**F050VLRAT -** Valida as informações em Rateio, quando utilizada a opção de centro de custo.  
Documentação: [F050VLRAT - Validação de informações em Rateio](http://tdn.totvs.com/pages/releaseview.action?pageId=6071649)

**F050TPRV -** Permite utilizar a natureza ou outras informações do título provisório no momento da substituição.  
Documentação: [http://tdn.totvs.com/display/PROT/F050TPRV](https://tdn.totvs.com/display/PROT/F050TPRV)  
  
**FA050SUB -** Executado após a confirmação da substituição**.**Documentação: [FA050SUB - Determina campos de títulos de substituição](http://tdn.totvs.com/pages/releaseview.action?pageId=6071118)

**F050DESD -****INCLUSÃO** - **Contas a Pagar**.  
Documentação: [F050DESD - Contas a pagar](http://tdn.totvs.com/display/public/mp/F050DESD+-+Contas+a+pagar+--+11606)

**FA050DES -** Permite a manipulação das parcelas no desdobramento**.**Documentação: [FA050DES - Manipula parcela no desdobramento](http://tdn.totvs.com/display/public/mp/FA050DES+-+Manipula+parcela+no+desdobramento+--+91038)

**F050DESIMP -** Para a gravação do conteúdo que foi incluído no campo Aprovador (**E2\_APROVA**), na inclusão de um título no **Contas a Pagar**.  
Documentação: [F050DESIMP - Geração de conteúdo no campo Aprovador](http://tdn.totvs.com/pages/releaseview.action?pageId=6071552)

**FA050PAR -** Chamado no programa de inclusão do **Contas a Pagar**.  
Documentação: [F050ROT- Inclui opções no menu](http://tdn.totvs.com/display/public/mp/FA050PAR+-+Efetua+tratamento+de+dados+--+11859)  
  
**F050BUT -** Permite inclusão de botão, para ativar rotinas especificas, na *Enchoicebar.*Documentação:[F050BUT - Inclusão de botão para ativar rotinas específicas](http://tdn.totvs.com/pages/releaseview.action?pageId=6071309)

**F050MDVC -** Permite calcular sua própria data de vencimento de impostos**.**Documentação: [F050MDVC - Cálculo da data de vencimento de impostos](http://tdn.totvs.com/pages/viewpage.action?pageId=6070892)

**F50TFINS -** Inclusão de títulos no Financeiro com configurações para cálculo de **INSS.**Documentação:[F50TFINS - Considera lista na retenção de INSS](http://tdn.totvs.com/pages/releaseview.action?pageId=6071446)  
  
**FA050RTF -** Utilizado para avaliação das filiais da empresa (SM0) a serem consideradas para verificação dos valores de notas com vencimento no período de retenção dos impostos **PCC**.  
Documentação:[FA050RTF - Avalia filiais](http://tdn.totvs.com/display/public/mp/FA050RTF+-+Avalia+filiais+--+11861)  
  
**FA050FOR -** Verifica o total de notas do fornecedor pela raiz do CNPJ que vencem no mesmo mês.  
Documentação:[FA050FOR - Verifica notas de Fornecedor](http://tdn.totvs.com/display/public/mp/FA050FOR+-+Verifica+notas+de+Fornecedor+--+24305)

**F050CALIR -**Acumula cálculo de **IR**.  
Documentação:[F050CALIR- Acumula cálculo de IR](https://tdn.totvs.com/display/PROT/F050CALIR-+Define+a+cumulatividade+do+calculo+de+IRRF)

**FIN050IR -**Incremento de *Query* no Cálculo de **IR**.  
Documentação: [FIN050IR - Incremento de Query no Cálculo de IR](http://tdn.totvs.com/pages/viewpage.action?pageId=59441644)

**F050ROT -**Inclui itens de menu.  
Documentação:[F050ROT- Inclui opções no menu](https://tdn.totvs.com/pages/viewpage.action?pageId=515670644)

**FA050Fil -** Será executado na montagem do filtro na substituição de títulos.  
Documentação:[FA050FIL - Montagem de filtro.](http://tdn.totvs.com/display/public/mp/FA050FIL+-+Montagem+de+filtro.+--+11853)

**FA050BRO -** Permite a alteração do índice.  
Documentação: [FA050BRO - Alteração de índice](http://tdn.totvs.com/pages/releaseview.action?pageId=6071444)

**FA050VLS -** Substituição de títulos provisórios.  
Documentação: [FA050VLS - Substituição de titulos provisórios](http://tdn.totvs.com/pages/releaseview.action?pageId=6071373)  
  
**F050DOCS -** Após gravação da manutenção dos documentos vinculados ao título.  
Documentação: [F050DOCS - Após gravação da manutenção dos documentos vinculados ao título](http://tdn.totvs.com/pages/releaseview.action?pageId=6071566)

# **FA750BRW** **-** Adição de itens no menu da mBrowse

[Adição de itens no menu da mBrowse](https://tdn.totvs.com/pages/releaseview.action?pageId=6071251)
