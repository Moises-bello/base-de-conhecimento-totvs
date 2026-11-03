---
content_hash: 609de6df661176a7ca54041b19cbcabb190bc2cfda7faa436249c3b3324d7fb5
fetched_at: '2026-06-29T00:10:56.834605+00:00'
page_id: '593231944'
product: rm
source: tdn-rm
title: Fiscal
type: documentation
url: https://tdn.totvs.com/display/LRM/Fiscal
version: 59
---

CamposFiscalMovleftMunicípio e UF

A partir da versão 12.1.25XX.XXX o campo **Município e UF** estará visivel para todos os movimentos com **tipo dos itens = P****roduto, Serviço e Ambos,** este o comportamento está alinhada às novas regras fiscais, onde a informação de município passa a ser relevante mesmo em movimentos que não possuem incidência de ISS.

Exceção dos movimentos com Tipo de Classificação abaixo que não serão apresentados os campo **Município** e **UF:**

* **Gestão de Estoque (todos as classificações)**
* **Outras Movimentações**
* **Solicitação de Compras (Gestão de Compras)**
* **Exportação e Importação**
Desconsidera Regra de Seleção de Natureza (RSN)

**Desconsidera Regra de Seleção de Natureza (RSN):**

Ao selecionar o campo "Desconsidera Regra de Seleção de Natureza", a regra avançada será desconsiderada, possibilitando ao usuário escolher a natureza que deseja inserir ao movimento.

* Parametrização:

Consumindo WebService

Desconsiderar regra de seleção de natureza: <DESCONSIDERARSNMOV>1</DESCONSIDERARSNMOV>

Considerar regra de seleção de natureza: <DESCONSIDERARSNMOV>0</DESCONSIDERARSNMOV>

Tipo de Documento

**Tipo de Documento:**

O preenchimento do campo indica o **Tipo de Documento Fiscal**, normalmente utilizado para escrituração e/ou geração de documentos eletrônicos.

Apresentação na tela

Campo é apresentado no movimento quando:

Na Etapa 62 - Fiscal - Escrituração fiscal o flag "Gerar Escrituração"  ou

o campo "Código Default" estiver preenchido ou

possuir algum registro na lista de "Outros Códigos" ou

estiver parametrizado na etapa 66 - Fiscal - Nota Fiscal Eletrônica para emitir NF-e ou NFC-e ou for um movimento de remessa simbólica.

Consumindo WebService

Informar o código do tipo de documento:  <CODTDO>55</CODTDO>

Consumidor Final

**Consumidor Final:**

A marcação do flag **Consumidor Final**, indica a operação com consumidor final.

Apresentação na tela

Campo é apresentado no movimento quando:

O flag **"Emite Cupom Fiscal"** na etapa 61 - Fiscal - Dados, nos parâmetros do tipo de movimento esta **desmarcado** e,

na Etapa 62 - Fiscal - Escrituração fiscal o flag "Gerar Escrituração"  ou

o campo "Código Default" estiver preenchido ou

possuir algum registro na lista de "Outros Códigos"

Ou estiver parametrizado na etapa 66 - Fiscal - Nota Fiscal Eletrônica para emitir NF-e ou NFC-e ou

for um movimento de remessa simbólica.

Consumindo WebService

É consumidor final: <OPERACAOCONSUMIDORFINAL>1</OPERACAOCONSUMIDORFINAL>

Não é consumidor final: <OPERACAOCONSUMIDORFINAL>0</OPERACAOCONSUMIDORFINAL>

Intermediador

**Intermediador:**

O preenchimento do campo **Identificador do Intermediador** indica uma operação com intermediador/marketplace.

Para que o campo seja visível, a seguinte regra deve ser respeitada:

1. **Operação Presencial**:
   1. Operação não presencial, pela Internet
   2. Operação não presencial, Tele atendimento
   3. Operação não presencial, outros
   4. NFC-e em Operação com entrega em domicílio
2. **Tipo de Documento**:
   1. O tipo de documento deve possuir o código do modelo de documento igual a 55 (NF-e) ou 65 (NFC-e).
Nº Ato Concessório Regime Drawback

**Nº Ato Concessório Regime Drawback**

Responsável por informar o registro da operação de Drawback.

Nº Ato Concessório Regime Drawback

O campo é apresentado quando o tipo de documento possui um dos seguintes modelos (**Modelo 01, NF-e 55 ou NFC-e 65**)

Local de operação IBS

**Local de Operação IBS (município/estado)**

O **Local da Operação** define onde (município e estado) uma operação de **bens ou serviços** será tributado pelo **IBS** (Imposto sobre Bens e Serviços).

Essa informação é imprescindível para a correta seleção da alíquota que será aplicada na tributação do Item do Movimento.

Apresentação na tela

Para que o campo de **Local da Operação IBS** esteja disponível para preenchimento, é necessário que o **Tipo de Movimento** esteja com o flag "Utilizar Tributação" marcado, no Item ou no Movimento.

Na tela, os campos de **Município** e **Estado** do Local da Operação IBS podem ser preenchidos de duas formas:

1. **Preenchimento Automático**

   * O sistema avalia os dados do movimento, aplica uma **regra específica** (documentada no ) e preenche automaticamente os campos de município e estado.
   * Os principais campos que influenciam nessa definição são:

     + Cliente/Fornecedor
     + Filial
     + Filial Destino
     + Tipo do Local da Operação (configurado como **Operação Presencial** na aba fiscal)
     + Estado/Município de Coleta
     + Estado/Município de Entrega
     + Estado/Município do Imóvel
     + Estado/Município do Destinatário do serviço

       aos serviços listados da LC 116/2003 (e seus correspondentes na NBS):

       - 25.05;
       - 15.09;
       - 17.12;
       - 10.05.
   * Sempre que um desses campos for alterado, ao sair do campo o sistema recalculará a regra e atualizará automaticamente o município e o estado.
2. **Preenchimento Manual**

   * O usuário pode informar diretamente o Município e o Estado.
   * **Atenção**: se algum campo que impacta a definição for alterado (como cliente, filial, coleta ou entrega), o sistema aplicará novamente a regra automática e substituirá os valores informados manualmente.
   * Caso o usuário não informe nada, o preenchimento automático será feito no momento de salvar o movimento.

Obrigatoriedade

Quando o movimento estiver parametrizado para a emissão de qualquer DF-e e houver o tributo **IBS** entre os tributos dos itens, o preenchimento do **Município** e **Estado** no grupo **Local da Operação IBS** torna-se obrigatório.

Caso o cliente seja **internacional** (ou seja, quando o estado vinculado ao cliente não estiver com o campo *“Nacional”* marcado), o preenchimento do campo **Município** no grupo **Local da Operação IBS** deixa de ser obrigatório, permanecendo opcional.

Utilização com serviço, WebService, API, EAI, Conceito

Quando a criação/alteração de movimento é realizado via serviço (API, WebService, EAI, Conceito, integração via serviços e classes tipadas que o sistema disponibiliza) o comportamento é semelhante ao descrito acima excetuando-se a não existência de gatilhos para o preenchimento dos campos no client, isto é, caso os valores não sejam informados no XML/JSON (ou campo específico para tal) então estes serão preenchidos pelo sistema no momento de salvar o registro (o serviço do fiscal é acionado retornando estado/cidade).

    <CODMUNOPER>02404</CODMUNOPER>  
    <CODUFOPER>SC</CODUFOPER>

Atividade de Evento

**Atividade de Evento**

As Atividades de Evento contêm informações sobre prestação de serviços enquadrados como Eventos para fins de emissão de NFS-e Nacional.

Para movimentos que tenham ISS no item e tenha o tributo parametrizado para buscar a alíquota no município o campo Atividade de Evento ficará disponível.

O campo também ficará disponível para movimentos com itens do tipo Produto e que estejam parametrizados para gerar escrituração.

Para mais informações sobre Atividades de Evento consulte a .

Tipo de Operação com Entes Governamentais ou serviços sobre bens imóveis

**Tipo de Operação com Entes Governamentais ou serviços sobre bens imóveis**

Deve ser informado quando se trata de uma compra governamental ou envolva um dos serviços listados na LC 116/2003 (e seus correspondentes na NBS): 

* 25.05;
* 15.09;
* 17.12;
* 10.05.

Para CT-e, este campo ficará visível quando o parâmetro do Tipo de Movimento, Etapa 69, Tipo de Operação do Conhecimento de Transporte for diferente de ""Não Usar CTRC":

Parâmetro do Tipo de Movimento - Etapa 69 - Fis -Conhecimento de Transporte

Para NFS-e, NF-e, NFC-e ou NFCom, este campo ficará visível quando seus respectivos parâmetros do Tipo de Movimento, etapa 67, for diferente de "Não integrado".

Parâmetro do Tipo de Movimento - Etapa 67 - Fis - NF-e

A classificação do tipo de operação possui as seguintes opções:

Para NF-e:

* Nenhum;
* Fornecimento com pagamento posterior;

Para NFS-e:

* Nenhum;
* Fornecimento com pagamento posterior;
* Recebimento do pagamento com fornecimento já realizado;
* Fornecimento com pagamento já realizado;
* Recebimento do pagamento com fornecimento posterior;
* Fornecimento e recebimento do pagamento concomitantes.

Para demais documentos eletrônicos:

* Nenhum;
* Fornecimento com pagamento posterior;
* Recebimento do pagamento com fornecimento já realizado;
* Fornecimento com pagamento já realizado;
* Recebimento do pagamento com fornecimento posterior;
Fique atento!

**A partir da Release 12.1.2606, esta Aba passa a ter uma nova organização de campos!**

Tipo de Documento

**Tipo de Documento:**

O preenchimento do campo indica o **Tipo de Documento Fiscal**, normalmente utilizado para escrituração e/ou geração de documentos eletrônicos.

Apresentação na tela

Campo é apresentado no movimento quando:

Na Etapa 62 - Fiscal - Escrituração fiscal o flag "Gerar Escrituração"  ou

o campo "Código Default" estiver preenchido ou

possuir algum registro na lista de "Outros Códigos" ou

estiver parametrizado na etapa 66 - Fiscal - Nota Fiscal Eletrônica para emitir NF-e ou NFC-e ou for um movimento de remessa simbólica.

Consumindo WebService

Informar o código do tipo de documento:  <CODTDO>55</CODTDO>

CamposFiscalMovGeralCamposFiscalGeralleftMunicípio e UF

A partir da versão 12.1.25XX.XXX o campo **Município e UF** estará visível para todos os movimentos com **tipo dos itens = P****roduto, Serviço e Ambos,** este o comportamento está alinhada às novas regras fiscais, onde a informação de município passa a ser relevante mesmo em movimentos que não possuem incidência de ISS.

Exceção dos movimentos com Tipo de Classificação abaixo que não serão apresentados os campo **Município** e **UF:**

* **Gestão de Estoque (todos as classificações)**
* **Outras Movimentações**
* **Solicitação de Compras (Gestão de Compras)**
* **Exportação e Importação**
Local de operação IBS

**Local de Operação IBS (município/estado)**

O **Local da Operação** define onde (município e estado) uma operação de **bens ou serviços** será tributado pelo **IBS** (Imposto sobre Bens e Serviços).

Essa informação é imprescindível para a correta seleção da alíquota que será aplicada na tributação do Item do Movimento.

Apresentação na tela

Para que o campo de **Local da Operação IBS** esteja disponível para preenchimento, é necessário que o **Tipo de Movimento** esteja com o flag "Utilizar Tributação" marcado, no Item ou no Movimento.

Na tela, os campos de **Município** e **Estado** do Local da Operação IBS podem ser preenchidos de duas formas:

1. **Preenchimento Automático**

   * O sistema avalia os dados do movimento, aplica uma **regra específica** (documentada no ) e preenche automaticamente os campos de município e estado.
   * Os principais campos que influenciam nessa definição são:

     + Cliente/Fornecedor
     + Filial
     + Filial Destino
     + Tipo do Local da Operação (configurado como **Operação Presencial** na aba fiscal)
     + Estado/Município de Coleta
     + Estado/Município de Entrega
     + Estado/Município do Imóvel
     + Estado/Município do Destinatário do serviço

       aos serviços listados da LC 116/2003 (e seus correspondentes na NBS):

       - 25.05;
       - 15.09;
       - 17.12;
       - 10.05.
   * Sempre que um desses campos for alterado, ao sair do campo o sistema recalculará a regra e atualizará automaticamente o município e o estado.
2. **Preenchimento Manual**

   * O usuário pode informar diretamente o Município e o Estado.
   * **Atenção**: se algum campo que impacta a definição for alterado (como cliente, filial, coleta ou entrega), o sistema aplicará novamente a regra automática e substituirá os valores informados manualmente.
   * Caso o usuário não informe nada, o preenchimento automático será feito no momento de salvar o movimento.

Obrigatoriedade

Quando o movimento estiver parametrizado para a emissão de qualquer DF-e e houver o tributo **IBS** entre os tributos dos itens, o preenchimento do **Município** e **Estado** no grupo **Local da Operação IBS** torna-se obrigatório.

Caso o cliente seja **internacional** (ou seja, quando o estado vinculado ao cliente não estiver com o campo *“Nacional”* marcado), o preenchimento do campo **Município** no grupo **Local da Operação IBS** deixa de ser obrigatório, permanecendo opcional.

Utilização com serviço, WebService, API, EAI, Conceito

Quando a criação/alteração de movimento é realizado via serviço (API, WebService, EAI, Conceito, integração via serviços e classes tipadas que o sistema disponibiliza) o comportamento é semelhante ao descrito acima excetuando-se a não existência de gatilhos para o preenchimento dos campos no client, isto é, caso os valores não sejam informados no XML/JSON (ou campo específico para tal) então estes serão preenchidos pelo sistema no momento de salvar o registro (o serviço do fiscal é acionado retornando estado/cidade).

    <CODMUNOPER>02404</CODMUNOPER>  
    <CODUFOPER>SC</CODUFOPER>

Desconsidera Regra de Seleção de Natureza (RSN)

**Desconsidera Regra de Seleção de Natureza (RSN):**

Ao selecionar o campo "Desconsidera Regra de Seleção de Natureza", a regra avançada será desconsiderada, possibilitando ao usuário escolher a natureza que deseja inserir ao movimento.

* Parametrização:

Consumindo WebService

Desconsiderar regra de seleção de natureza: <DESCONSIDERARSNMOV>1</DESCONSIDERARSNMOV>

Considerar regra de seleção de natureza: <DESCONSIDERARSNMOV>0</DESCONSIDERARSNMOV>

370px30

Documento Fiscal eletrônicoCamposFiscalDocsFiscaisleftNº Ato Concessório Regime Drawback

**Nº Ato Concessório Regime Drawback**

Responsável por informar o registro da operação de Drawback.

Nº Ato Concessório Regime Drawback

O campo é apresentado quando o tipo de documento possui um dos seguintes modelos (**Modelo 01, NF-e 55 ou NFC-e 65**)

Intermediador

**Intermediador:**

O preenchimento do campo **Identificador do Intermediador** indica uma operação com intermediador/marketplace.

Para que o campo seja visível, a seguinte regra deve ser respeitada:

1. **Operação Presencial**:
   1. Operação não presencial, pela Internet
   2. Operação não presencial, Tele atendimento
   3. Operação não presencial, outros
   4. NFC-e em Operação com entrega em domicílio
2. **Tipo de Documento**:
   1. O tipo de documento deve possuir o código do modelo de documento igual a 55 (NF-e) ou 65 (NFC-e).
Tipo de Operação com Entes Governamentais ou serviços sobre bens imóveis

**Tipo de Operação com Entes Governamentais ou serviços sobre bens imóveis**

Deve ser informado quando se trata de uma compra governamental ou envolva um dos serviços listados na LC 116/2003 (e seus correspondentes na NBS): 

* 25.05;
* 15.09;
* 17.12;
* 10.05.

Para CT-e, este campo ficará visível quando o parâmetro do Tipo de Movimento, Etapa 69, Tipo de Operação do Conhecimento de Transporte for diferente de ""Não Usar CTRC":

Parâmetro do Tipo de Movimento - Etapa 69 - Fis -Conhecimento de Transporte

Para NFS-e, NF-e, NFC-e ou NFCom, este campo ficará visível quando seus respectivos parâmetros do Tipo de Movimento, etapa 67, for diferente de "Não integrado".

Parâmetro do Tipo de Movimento - Etapa 67 - Fis - NF-e

A classificação do tipo de operação possui as seguintes opções:

Para NF-e/NFC-e:

* Nenhum;
* Fornecimento com pagamento posterior;

Para NFS-e:

* Nenhum;
* Fornecimento com pagamento posterior;
* Recebimento do pagamento com fornecimento já realizado;
* Fornecimento com pagamento já realizado;
* Recebimento do pagamento com fornecimento posterior;
* Fornecimento e recebimento do pagamento concomitantes.

Para demais documentos eletrônicos:

* Nenhum;
* Fornecimento com pagamento posterior;
* Recebimento do pagamento com fornecimento já realizado;
* Fornecimento com pagamento já realizado;
* Recebimento do pagamento com fornecimento posterior;
Atividade de Evento

**Atividade de Evento**

As Atividades de Evento contêm informações sobre prestação de serviços enquadrados como Eventos para fins de emissão de NFS-e Nacional.

Para movimentos que tenham ISS no item e tenha o tributo parametrizado para buscar a alíquota no município o campo Atividade de Evento ficará disponível.

O campo também ficará disponível para movimentos com itens do tipo Produto e que estejam parametrizados para gerar escrituração.

Para mais informações sobre Atividades de Evento consulte a .

Consumidor Final

**Consumidor Final:**

A marcação do flag **Consumidor Final**, indica a operação com consumidor final.

Apresentação na tela

Campo é apresentado no movimento quando:

O flag **"Emite Cupom Fiscal"** na etapa 61 - Fiscal - Dados, nos parâmetros do tipo de movimento esta **desmarcado** e,

na Etapa 62 - Fiscal - Escrituração fiscal o flag "Gerar Escrituração"  ou

o campo "Código Default" estiver preenchido ou

possuir algum registro na lista de "Outros Códigos"

Ou estiver parametrizado na etapa 66 - Fiscal - Nota Fiscal Eletrônica para emitir NF-e ou NFC-e ou

for um movimento de remessa simbólica.

Consumindo WebService

É consumidor final: <OPERACAOCONSUMIDORFINAL>1</OPERACAOCONSUMIDORFINAL>

Não é consumidor final: <OPERACAOCONSUMIDORFINAL>0</OPERACAOCONSUMIDORFINAL>

Energia / Água / TelecomCamposFiscalServicosPrestadorTomadosleftEnergia

Os campos apresentados quando selecionado o Tipo de Documento **Energia**

Telecomunicações

Os campos apresentados quando selecionado o Tipo de Documento **NFCom**
