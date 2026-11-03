---
content_hash: 2479f85ce758ed0e3a35a13d1b8862ed0a6ff329a5249c14f9c633d503dbb92a
fetched_at: '2026-06-29T00:10:45.657445+00:00'
page_id: '553339014'
product: rm
source: tdn-rm
title: RascunhosProcesso Desenvolvimento Ágil | Critérios DoR e DoD - Suporte e Desenvolvimento
  - Backoffice Protheus
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=553339014
version: 1
---

5%90%

Foram definidos como padrão os ***Critérios de DoR e DoD - Suporte e Desenvolvimento*** para o **Backoffice Protheus**, afim de padronizar as entregas do **Suporte para o Desenvolvimento** *(criação das issues)* e do **Desenvolvimento para o Suporte** *(resolução, dúvidas ou rejeição das issues)*.

CRITÉRIOS DE DOR E DOD - SUPORTE PARA DESENVOLVIMENTO E DESENVOLVIMENTO PARA SUPORTE

*O modelo acima pode ser acessado em detalhes no arquivo*

*(**Importante:** este modelo foi desenvolvido no software **XMind**, portante é necessária a sua instalação para visualização).*

## ***1. Suporte > Desenvolvimento - Abertura de Issue***

A equipe de Suporte ao criar uma nova *issue*, deverá seguir os ***Critérios de DoR e DoD - Suporte e Desenvolvimento*** definidos e utilizar o  *(exemplo de preenchimento em **<http://tdn.totvs.com/x/h25YGw>**)*, preenchendo-o com todas as informações que se fizerem necessárias e anexando-o ao *ticket* e a *issue*, para que o Desenvolvimento possa realizar a análise e atuar na sua resolução.

Em qualquer tela do Protheus podem ser pressionadas as teclas **SHIFT + F6** do teclado, simultaneamente, para que seja exibida informações da rotina que você está no sistema, informações do ambiente e ferramentas úteis.

*Se existir alguma situação, no qual, não seja possível a reprodução em ambiente local, o Maestro e/ou Líder do Suporte deverá alinhar com o Product Owner, podendo este aceitar ou não a abertura da issue, diante das evidências.*

**Prazo padrão para retorno do Suporte para o Desenvolvimento:**

Na situação em que o Desenvolvimento, após a análise da *issue* verificar que a *issue* deve ser rejeitada e realizado o alinhamento com o Analista de Atendimento e o Maestro e/ou Líder de Atendimento. Fica estabelecido o prazo de **2 dias úteis** para o retorno do Suporte, não havendo o retorno, o Desenvolvimento irá realizar a rejeição.

## ***2. Desenvolvimento > Suporte - Rejeição e Apoio***

A equipe de Desenvolvimento ao inciar a análise de uma nova *issue*, deverá verificar se os ***Critérios de DoR e DoD - Suporte e Desenvolvimento*** definidos foram seguidos pelo Suporte para criação da *issue* e deverá seguir também os ***Critérios de DoR e DoD*** definidos na atuação de resolução das demandas. *O processo de priorização deve ser alinhado com o Product Owner da Squad*.

*Verificar os procedimentos para os casos onde seja necessária a Devolução / Rejeição da issue, em: **[Instrução de Trabalho - Procedimento Antes de Rejeitar ou Não Rejeitar uma Issue](http://tdn.totvs.com/pages/viewpage.action?pageId=458771487)***

**Prazo padrão para retorno do Desenvolvimento para o Suporte em uma solicitação de Apoio:**

Na situação em que o Suporte, realizar a abertura de uma *issue* do tipo Apoio, o *Product Owner* tem um prazo de **até 15** **dias** para informar a Data de Acordo para o apoio ocorrer *(havendo alguma exceção, o Maestro e/ou Líder do Suporte deverá realizar alinhamento com o Product Owner)*.

## ***3. Processos para Issues sem Posicionamento***

Foram definidos processos de formalização de prazos e planejamento de *issues* através dos campos "**PRIORIZADO**" no *ticket* no Zendesk e "**DATA DE ACORDO**" na *issue* no JIRA. Os fluxos que foram definidos e devem ser seguidos pelo **Suporte** e **Desenvolvimento (*Product Owners*)** são:

Posicionamento do prazo para o Cliente;

Rejeição do prazo pelo Cliente;

Data Acordo Entrega vencida.

Os detalhes de cada um desses processos estão documentados na space da ***Guild* Protheus** em: **[Desenvolvimento Protheus - Issues sem Posicionamento](http://tdn.totvs.com/x/UhAcEQ)**

## ***4. Processo de Padronização para Subida de Fontes***

**4.1.** Documento com o passo a passo de todas as características necessárias para criação da base congelada, conforme o exemplo a seguir:

20px900pxExemplo

**Nome do Caso de Teste:** Nota Fiscal de Entrada - Retorno de mercadoria remetida para industrialização por encomenda em operação interna com ICMS e IPI Suspensos, PIS e COFINS Não Incidentes Regime Não-Cumulativo

**Pré Condições:**

Acessar o Configurador (SIGACFG) ->Cadastros →Parâmetros:

MV\_ESTADO = SP

MV\_ICMPAD = 18

MV\_ESPECIE = 633=SPED

MV\_IPINOBS = SS

**Cadastro de Natureza - Indústria - Venda de Material**

Código (ED\_CODIGO) = IND001

Descrição (ED\_DESCRIC) = VENDA DE MATERIAL

Cond. Natureza (ED\_COND) = RECEITA

**Cadastro de Natureza - Indústria - Compra de Material**

Código (ED\_CODIGO) = IND002

Descrição (ED\_DESCRIC) = COMPRA DE MATERIAL

Cond. Natureza (ED\_COND) = DESPESA

**Cadastro de Fornecedor - Indústria - SP0002 - tipo contribuinte pessoa jurídica**

**Cadastrais:**

Código (A2\_COD) = SP0002

Loja (A2\_LOJA) = 01

Razao Social (A2\_NOME) = FORN SP PJ

N Fantasia (A2\_NREDUZ) = FORN SP PJ

Endereço (A2\_End) = Av. Braz Leme, 100

Bairro (A2\_BAIRRO) = Santana

Estado (A2\_EST) = SP

Cd. Municipio (A2\_COD\_MUN) = 50308

Municipio (A2\_MUN) = SAO PAULO

CEP (A2\_CEP) = 05124-000

Tipo (A2\_TIPO) = Juridico

CNPJ/CPF (A2\_CGC) = 36.528.684/0001-46

Insc. Estadual (A2\_INSCR)= 178.899.484.930

Pais (A2\_PAIS) = 105

**Adm/Financeiro:**

Natureza (A2\_NATUREZ) = IND002

**Fiscais:**

Pais Bacen (A2\_CODPAIS) = 01058

**Cadastro de Conta Contábil - Indústria - Entrada de documentos**

Cod. Conta (CT1\_CONTA) = ENT000001

Desc Moeda 1 (CT1\_DESC01)= CONTA PARA LANC ENTRADA

Classe Conta (CT1\_CLASSE) = 2 - Analítica

Cond. Normal (CT1\_NORMAL) = 2 - Credora

Dt Ini Exist (CT1\_DTEXIS) = 01/01/2017

Nat Cta SPED (CT1\_NTSPED) = 09 - Outras

**Cadastro de Conta Contábil - Indústria - Saída de documentos**

Cod. Conta (CT1\_CONTA) = SAI000001

Desc Moeda 1 (CT1\_DESC01)= CONTA PARA LANC SAIDA

Classe Conta (CT1\_CLASSE) = 2 - Analítica

Cond. Normal (CT1\_NORMAL) = 1 - Devedora

Dt Ini Exist (CT1\_DTEXIS) = 01/01/2017

Nat Cta SPED (CT1\_NTSPED) = 09 - Outras

**Cadastro de Cliente - Indústria - SP0002 - tipo revendedor pessoa jurídica**

**Cadastrais:**

Código (A1\_COD) = SP0002

Loja (A1\_LOJA) = 01

Fisica/Jurid (A1\_PESSOA) = Jurídica

Nome (A1\_NOME) = CLIENTE SP REV PJ

N Fantasia (A1\_NREDUZ) = SP REV PJ

Endereço (A1\_End) = Av. Braz Leme, 100

Tipo (A1\_TIPO) = R- Revendedor

Estado (A1\_EST) = SP

Cd. Municipio (A1\_COD\_MUN) = 50308

Municipio (A1\_MUN) = SAO PAULO

Bairro (A1\_BAIRRO) = Santana

CEP (A1\_CEP) = 10025-100

Pais (A1\_PAIS) = 105

CNPJ/CPF (A1\_CGC) = 07.079.511/0002-70

Ins. Estad. (A1\_INSCR) = 148.538.048.119

**Adm/Financeiro:**

Natureza (A1\_NATUREZ) = IND001

**Fiscais:**

Pais Bacen (A1\_CODPAIS) = 01058

**Vendas:**

Risco (A1\_RISCO) = A - Risco A

Lim. Credito (A1\_LC) = 999.999.999,99

Venc Lim Cre (A1\_VENCLC) = 31/12/2049

**Cadastro de Condição de Pagamento - Indústria - 001 - à vista**

Código (E4\_CODIGO): 001

Tipo (E4\_TIPO): 1

Cond. Pagto (E4\_COND): 0

Descrição (E4\_DESCRI): A VISTA

**Cadastro de TES - Saída - Indústria Filial SP - 514 - Remessa P/ Industrialização Por Encomenda - ICMS Suspenso (CST 50), IPI Suspenso (CST 55), PIS e COFINS Não Incidentes (CST 08)**

Código (F4\_CODIGO) = 514

Cred. ICMS (F4\_CREDICM) = N-Não

Credita IPI (F4\_CREDIPI) = N-Não

Gera Dupl. (F4\_DUPLIC) = N-Não

Atu.Estoque (F4\_ESTOQUE) = S-Sim

Poder Terc (F4\_PODER3) = R-Remessa

Finalidade (F4\_FINALID) = REMESSA PARA INDUSTRIALIZAÇÃO POR ENCOMENDA - ICMS

SUSPENSO, IPI SUSPENSO, PIS COFINS NÃO INCIDENTES

Calcula ICMS (F4\_ICM) = S-SIM

Calcula IPI (F4\_IPI) = N-NÃO

Cód Fiscal (F4\_CF) = 5901

Txt Padrão (F4\_TEXTO) = REM. IND. ENCOMENDA

L. Fisc ICMS (F4\_LFICM) = O-OUTROS

L. Fisc IPI (F4\_LFIPI) = O-OUTROS

Destaca IPI (F4\_DESTACA) = N-NÃO

IPI Na Base (F4\_INCIDE) = N-NÃO

Calc.Dif.Icm (F4\_COMPL) = N-NÃO

Agrega Valor (F4\_AGREG) = S-SIM

SIT. TRIB ICM (F4\_SITTRIB) = 50

Pis/Cofins (F4\_PISCOF) = 3 - AMBOS

Cred. Pis/Cofins (F4\_PISCRED) = 4 - CALCULA

COD. TRIB IPI (F4\_CTIPI)= 55

Tp Reg (F4\_TPREG) = 1 - NÃO CUMULATIVO

SIT. TRIB. PIS (F4\_CSTPIS) = 08

SIT. TRIB. COF (F4\_CSTCOF) = 08

Tab. Nat. Re (F4\_TNATREC) = 4315

Cod. Nat. Rece(F4\_CNATREC) = 999

**Cadastro de TES - Entrada - Indústria Filial SP - 011 - Retorno de Mercadoria Remetida Para Industrialização Por Encomenda - ICMS Suspenso (CST 50), IPI Suspenso (CST 05), PIS e COFINS Não Incidentes (CST 74)**

Código (F4\_CODIGO) = 011

Cred. ICMS (F4\_CREDICM) = N-Não

Credita IPI (F4\_CREDIPI) = N-Não

Gera Dupl. (F4\_DUPLIC) = N-Não

Atu.Estoque (F4\_ESTOQUE) = S-Sim

Poder Terc (F4\_PODER3) = D-Devolução

Finalidade (F4\_FINALID) = RETORNO DE MERCADORIA REMETIDA PARA INDUSTRIALIZAÇÃO

POR ENCOMENDA - ICMS SUSPENSO, IPI SUSPENSO, PIS COFINS NÃO INCIDENTES

Calcula ICMS (F4\_ICM) = S-SIM

Calcula IPI (F4\_IPI) = S-Sim

Cód Fiscal (F4\_CF) = 1902

Txt Padrão (F4\_TEXTO) = RET. REM. IND. ENCOMENDA

L. Fisc ICMS (F4\_LFICM) = O-OUTROS

L. Fisc IPI (F4\_LFIPI) = O-OUTROS

Destaca IPI (F4\_DESTACA) = N-NÃO

IPI Na Base (F4\_INCIDE) = N-NÃO

Calc.Dif.Icm (F4\_COMPL) = N-NÃO

Agrega Valor (F4\_AGREG) = S-SIM

SIT. TRIB ICM (F4\_SITTRIB) = 50

Pis/Cofins (F4\_PISCOF) = 3 - AMBOS

Cred. Pis/Cofins (F4\_PISCRED) = 4 - CALCULA

COD. TRIB IPI (F4\_CTIPI)= 05

Tp Reg (F4\_TPREG) = 1 - NÃO CUMULATIVO

SIT. TRIB. PIS (F4\_CSTPIS) = 74

SIT. TRIB. COF (F4\_CSTCOF) = 74

**Pedido de venda**

**Cabeçalho do Pedido:**

Número (C5\_NUM)= 000009;

Tipo de Pedido: (C5\_TIPO) = B - Utiliza Fornecedor;

Cliente (C5\_CLIENTE) = SP0002;

Loja (C5\_LOJACLI) = 01;

Cli. Entrega (C5\_CLIENT) = SP0002;

Loja Entrega (C5\_LOJAENT) = 01;

Tipo Cliente (C5\_TIPOCLI) = R - Revendedor;

Cond. Pagto (C5\_CONDPAG) = 001;

**Item do Pedido:**

Item (C6\_ITEM): 01;

Produto (C6\_PRODUTO): PA0000000000000000000000000002;

Quantidade (C6\_QTDVEN): 1;

Prc Unitário (C6\_PRCVEN): 2.000,00;

Vlr. Total (C6\_VALOR): 2.000,00;

C6\_CONTA: SAI000001;

Tipo Saída (C6\_TES) 514;

**Para geração da chave do documento fiscal (teste automatizado):**

Código da UF emitente do Documento Fiscal = 35

CNPJ do emitente =

Modelo do Documento Fiscal = 55

**Script de Teste**

**Nota Fiscal de Saída**

**Cabeçalho da Nota Fiscal:**

Tipo da Nota (F1\_TIPO) = Normal

Form. Prop (F1\_FORMUL)= NÃO

Número (F1\_DOC) = XXXXXXXXX

Série (F1\_SERIE) = 199

Fornecedor (F1\_FORNECE) = SP0002

Loja (F1\_LOJA) = 01

Espéc. Doc (F1\_ESPECIE) = SPED

**Item da Nota Fiscal:**

Item NF (D1\_ITEM) = 0001

Produto (D1\_COD) = PA0000000000000000000000000002

Quantidade (D1\_QUANT) = 1

Vlr. Unitário (D1\_VUNIT) = 2.000,00

Vlr. Total (D1\_TOTAL)= 2.000,00

Tipo Entrada (D1\_TES) = 011

C. Contábil (D1\_CONTA) = ENT000001

**<Obter número da NF gerada pelo pedido acima>**

Docto Orig (D1\_NFORI) = XXXXXXXXX

Série Orig (D1\_SERIORI) = 633

It. Doc Orig (D1\_ITEMORI) = 01

**Aba Duplicatas:**

Cond. Pagto (F1\_COND) = 001

Natureza (E2\_NATUREZ) = IND002

**Para geração da chave do documento fiscal (teste automatizado):**

Código da UF emitente do Documento Fiscal = 35

CNPJ do emitente = 36528684000146

Modelo do Documento Fiscal = 55

**Resultado Esperado:**

**SF3**

Data de entrada (F3\_ENTRADA)= Mês anterior a database

Data de emissão (F3\_EMISSAO)= Mês anterior a database

Número da Nota (F3\_NFISCAL)= xxxxxx

Série (F3\_SERIE)= 199

Cliente/Fornecedor (F3\_CLIEFOR)= SP0002

CFOP (F3\_CFO)= 1902

Estado (F3\_ESTADO)= SP

Valor Contábil (F3\_VALCONT) = 2.200,00

Base ICMS (F3\_BASEICM) = 0,00

Valor ICMS (F3\_VALICM) = 0,00

ICMS Isento (F3\_ISENICM) = 0,00

ICMS Outros (F3\_OUTRICM) = 2.000,00

Base IPI (F3\_BASEIPI) = 0,00

Valor IPI (F3\_VALIPI) = 0,00

IPI Outros (F3\_OUTRIPI) = 2.000,00

IPI Isento (F3\_ISENIPI) = 0,00

**SFT**

Número da Nota (FT\_NFISCAL) = xxxxxx

Série (FT\_SERIE) = 199

Data de emissão (FT\_EMISSAO) = Mês anterior a database

Cliente/Fornecedor (FT\_CLIEFOR) = SP0002

Loja (FT\_LOJA) = 01

CFOP (FT\_CFOP) = 1902

Item (FT\_ITEM) = 0001

Alíq ICMS (FT\_ALIQICM) = 0

Valor Contábil (FT\_VALCONT) = 2.200,00

Base ICMS (FT\_BASEICM) = 0,00

Valor ICMS (FT\_VALICM) = 0,00

ICMS Isento (FT\_ISENICM) = 0,00

ICMS Outros (FT\_OUTRICM) = 2.000,00

Base IPI (FT\_BASEIPI) = 0,00

Valor IPI (FT\_VALIPI) = 0,00

IPI Outros (FT\_OUTRIPI) = 2.000,00

IPI Isento (FT\_ISENIPI) = 0,00

Tipo (FT\_TIPO) = EM BRANCO

IPI na Observação (FT\_IPIOBS) = 200,00

Base PIS Apuração (FT\_BASEPIS) = 2.000,00

Valor PIS Apuração (FT\_VALPIS) = 33,00

CST PIS (FT\_CSTPIS) = 74

Base COFINS Apuração (FT\_BASECOF) = 2.000,00

Valor COFINS Apuração (FT\_VALCOF) = 152,00

CST COFINS (FT\_CSTCOF) = 74

Data de cancelamento (FT\_DTCANC) = EM BRANCO

Observação(FT\_OBSERV) = Dev. terc. N.F.ORIG.: ​**Número da NF gerada pelo pedido**

**4.2.** Caso o programa esteja automatizado, evidenciar a execução de todos os Casos de Testes no AdvPR e/ou TIR, demonstrando que mesmo após a alteração proposta, nenhum caso de teste antigo passou a quebrar.

A evidência de execução local ou Smart Test são válidas para este processo.

**4.3.** Anexar o Documento de passo a passo e o Script de Teste Automatizado na Issue. O Script não deverá ser atualizado no TFS até que o time responsável realize a validação e inclusão das informações na Base Congelada.

**4.4.** Fonte alterado com versão e changeset utilizado como base (enviar o fonte compatibilizado com a última alteração na data do envio).

**4.5.** Texto com descritivo do ajuste para Check In.

**4.6.** Sub-task de Codificação da issue (*Squad* que solicita a alteração) onde vai ser realizado o check-in.

**4.7.**No caso de criação de CH, tabelas, índices, campos, gatilhos, consultas padrões, e parâmetros enviar também no documento TODOS OS DETALHES referentes para a criação/alteração dos mesmos, pois os estas informações serão utilizadas para a criação no ATUSX.

Também é válido o relatório do Pacote do ATUSX com as informações dos ajustes realizados.

**4.8.** Após a subida do fonte solicitado, a *issue* deverá ser homologada em até 2 dias uteis pela *Squad* solicitante, pois assim o lock do fonte é liberado. Caso a *issue* não seja homologada neste prazo, a versão do fonte poderá ser descartada para check-in em outro momento.

**4.9. *Importante:*** A criação de funções específicas para módulos que não são os "donos" dos fontes, deve ser realizada em fontes próprios. Ou seja, no fonte (motivo de apoio da subida) somente deverá constar as proteções do módulo/existência da nova função, e a chamada dessa nova função.

Esta observação também é válida quando a situação é específica para uma localização, como por exemplo, Localização Brasil ou Localização Argentina.

**4.10.** Caso apareçam quebras futuras nos Scripts de Testes criados pelos times Solicitante, o time "Dono do Programa" irá avaliar e se tratando de um problema do time Solicitante, será solicitado a sua correção.

## ***5. Processos específicos para******Central Colaborativa***

**5.1. Ponto de Entrada:**

Ponto de Entrada não será considerada como melhoria na Central Colaborativa e deverá seguir o processo abaixo:

**5.1.1. Solicitação do Cliente:**

Suporte abre uma *issue* de Apoio para a solicitação de orçamento;

*Product Owner* avalia se o Ponto de Entrada faz sentido e se deve ser realizado;

*Product Owner* realiza o orçamento em horas de desenvolvimento para os Pontos de Entrada aprovados;

*Product Owner* retorna a *issue* para o Suporte;

Suporte documenta internamente no *ticket* a quantidade de horas e escopo do ponto de entrada para a transferência ao grupo Participativo do Zendesk;

PMO do Suporte (Andrea Coelho/Bianka Pestl) cria a proposta, retorna com o OK do Cliente e transfere o *ticket* para que o Suporte possa abrir a *issue* de Ponto de Entrada ao Produto;

*Product Owner* prioriza a criação do Ponte de Entrada e retorna para o Cliente.

***Importante:*** Caso o *Product Owner* não veja sentido na criação do Ponto de Entrada, o próprio *Product Owner* deve responder para o Cliente.

**5.1.2. Solicitação do time de Serviços:**

Consultor encaminha *e-mail* para o *Produto Owner* com a solicitação de orçamento;

*Product Owner* avalia se o Ponto de Entrada faz sentido e se deve ser realizado;

*Product Owner* realiza o orçamento em horas de desenvolvimento para os Pontos de Entrada aprovados;

*Product Owner* encaminha as informações por *e-mail* para o PMO Produto (Vânia Rehem);

PMO Produto solicita dados financeiros (CC, Item, Classe, Nome aprovador) para criação de WF de cobrança do Ponto de Entrada para o time de serviços, após a aprovação do WF, o time de PMO informa para Time de Serviços e *Product Owner* via *e-mail* que pode iniciar o Ponto de Entrada;

*Product Owner* cria uma *issue* para a realização do Ponto de Entrada;

*Product Owner* prioriza a criação do Ponte de Entrada e retorna para o Consultor.

***Importante:*** Caso o *Product Owner* não veja sentido na criação do Ponto de Entrada, o próprio *Product Owner* deve responder para o Consultor.

**5.2. Definição de Melhoria / Erro de Concepção**

Se a funcionalidade disponibilizada com a documentação, está realizando o resultado documentado, o entendimento é Melhoria.

Se a funcionalidade não está fazendo o que está documentado, então é Erro.

Se o entendimento final não for Erro de Concepção ou Melhoria, deve ser documentado o conceito da funcionalidade e também o que a funcionalidade não irá atender (Exemplo de Artefato: **O que faz | Não Faz | É | Não É**).

***Importante:*** Para conseguir identificar e tratar os casos de Erro de Concepção e Melhoria, quando não houver consenso de entendimento entre Suporte e *Product Owner*, o *Agile Coach* será envolvido e iremos alimentar um documento vivo, com a definição do que é / não é Melhoria.

**5.3. Definição do limite para a primeira interação na Central Colaborativa**

90 dias.

**5.4. Definição de quem pode/deve realizar a interação na Central Colaborativa**

*Product Owner*, *Proxy PO* e Substitutos na ausência do *Product Owner*.

**5.5. Uso de funções padrões em customizações / Documentação da Função**

Não deverá entrar como Central Colaborativa;

Deve ser realizada a abertura de issue do tipo Documentação.

***Importante:*** Funções não disponibilizadas e documentadas, na estrutura TDN > MODULO > Funções, não devem ser utilizadas para customizações, pois, a qualquer momento pode sofrer mudanças e o time não poderá ser responsabilizado. Caso o *Product Owner* definir que a função não pode ser utilizada para customização, o próprio *Product Owner* deve responder para o Cliente.

5%
div.theme-default .ia-splitter #main {
margin-left: 0px;
}
.ia-fixed-sidebar, .ia-splitter-left {
display: none;
}
#main {
padding-left: 10px;
padding-right: 10px;
overflow-x: hidden;
}
.expand-control-text {
color: #000000;
font-size: 13px !important;
font-weight:bold !important;
}
.expand-icon, .aui-icon, .aui-icon-small, .aui-iconfont-chevron-right {
color: #FF8000;
}
.aui-header-primary .aui-nav, .aui-page-panel {
margin-left: 0px !important;
}
.aui-header-primary .aui-nav {
margin-left: 0px !important;
}
]]>
