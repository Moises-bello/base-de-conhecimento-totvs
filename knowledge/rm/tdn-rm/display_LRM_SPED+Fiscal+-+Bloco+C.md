---
content_hash: 52f89d1ebfb30be6d29dbd84a95e072c31523eb4d79890d0c16be48bed450567
fetched_at: '2026-06-29T00:09:22.681669+00:00'
page_id: '422546009'
product: rm
source: tdn-rm
title: SPED Fiscal - Bloco C
type: documentation
url: https://tdn.totvs.com/display/LRM/SPED+Fiscal+-+Bloco+C
version: 208
---

#f5f5f5#363636noneRegistrosBLOCOCleftC100C100

**Nota Fiscal (código 01), Nota fiscal avulsa (Código 1B) nota Fiscal de Produtor Rural (Código 04), NF-e ( Código 55) e NFC-e (Código 65)**

Este Registro será gerado com as informações das Notas Fiscais modelos 01, 1B, 04 e 55 e 65 Neste caso deverão ser consideradas as notas fiscais recebidas e emitidas.

Informações Adicionais

Para este registro, não deve ser gerada a NF-e denegada e Numeração inutilizada a partir de 2023.

* **Campo** **SER:**

O campo série será completado com zeros a esquerda quando necessário.

Exemplo:

Série: 3

Arquivo Gerado: SER → 003

* **Campo VL\_ABAT\_NT:**

Ajuste na geração do campo VL\_ABAT\_NT, do registro C100 no SPED, onde agora será consistido o novo parâmetro "ICMS Deson. NÃO afeta Valor Contábil", na Regra de ICMS da CFOP. Caso ela esteja marcada, o valor do ICMS Desonerado não será considerada na totalização deste campo.

Imagem

* **Campo IND\_PGTO:**

Ao Gerar o SPED Fiscal, O Registro C100, campo 13 IND\_PGTO (Indicador de Pagamento) será preenchido com o valor:

* Dado que um Lançamento Fiscal é proveniente de movimento:  
  + E, no movimento existe pelo menos uma parcela com o meio de pagamento “Sem Pagamento”:
    - 2 (“Outros”)\*
  + Se não existe nenhuma parcela com meio de pagamento "Sem Pagamento":
    - Se a condição de pagamento for igual a "Outros": 2 (“Outros”)\*
    - Se a condição de pagamento for igual à Vista: 0 ("À Vista")
    - Se a condição de pagamento for igual à Prazo: 1 ("À prazo")
* Se não for proveniente de movimento:
  + Se não houver data de vencimento: 2 (“Outros”)\*
  + Se a data de vencimento for maior que a data de emissão: 1 ("À prazo")
  + Senão: 0 ("À Vista")

Observação

Para o caso de geração referente à período igual ou anterior à "01/07/2012, será gerado com código 9 ("Sem Pagamento") ao invés de 2 ("Outros").

* **Campo VL\_MERC:**Valor total das mercadorias e serviços.
  + Para os lançamentos de saída o valor será **Quantidade x Preço**.
  + Para os lançamentos de entrada será **Quantidade x Preço + Valor Substituição tributária**.

Observação

Foi criado um novo Tipo de Natureza no cadastro da CFOP, este tipo é referente a Devolução por Recusa.

Se na Natureza o campo Tipo Natureza(Rotinas Legais) for Devolução por Recusa, as informações geradas no registro C100 do SPED Fiscal será considerado o Emitente/Destinatário Filial.

Veja como parametrizar Devolução por Recusa: <https://tdn.totvs.com/x/-lYrIw>

* **Campo VL\_ICMS:**

Ao gerar o Registro C100 o campo 22 VL\_ICMS será preenchido caso o Tipo ICMS da natureza de Operação seja definido como Tributado ou Outros

ImagemC110C110

**Informação complementar da Nota Fiscal (Código 01; 1B, 04 e 55 e 65)**

Este Registro é gerado com base no campo Complementar do Lançamento Fiscal "InfComplDocFiscal", gerada no registro 0450

**Campos de Uso Livre  NF-e**

Também é possível gerar o  a partir dos Campos de Uso Livre.

Gerando a partir dos Campos de Uso Livre, o C110 irá pegar o Valor xTexto.

Mais informações na página do [Registro 0450](https://tdn.totvs.com/pages/viewpage.action?pageId=422546008#BLOCO0-0450).

C111C111

**Processo referenciado**

Este registro é gerado com informações do Processo Judicial informados no Lançamento Fiscal.

C112C112

**Documento de Arrecadação referenciado**

Este Registro será gerado com base nas informações de Guias vinculadas ao Lançamento Fiscal.

A UF a ser considerada na geração deste registro será a UF da Guia.

C113C113

**Documento Fiscal referenciado**

Este registro deve ser apresentado, obrigatoriamente, quando o lançamento fiscal possuir um ou mais lançamentos relacionados e que sejam de modelos diferentes a 02, 2D, 2E ou 59.

| N° | Campo | Descrição | Origem da Informação | Observações |
| --- | --- | --- | --- | --- |
| 01 | REG | Texto fixo contendo "C113" | Não se aplica |  |
| 02 | IND\_OPER | Indicador do tipo de operação: 0- Entrada/aquisição; 1- Saída/prestação | DLAF.TIPOLF | Tipo de lançamento Entrada ou Saída |
| 03 | IND\_EMIT | Indicador do emitente do título: 0- Emissão própria; 1- Terceiros | DLAF.FLAGCFO | Lançamento de Saída => Emissão Própria; Lançamento de Entrada onde Emitente = Filial e é Regime Especial => Emissão Terceiros; Lançamento de Entrada onde Emitente = Filial => Emissão Própria; Lançamento de Entrada onde Emitente <> Filial => Emissão Terceiros |
| 04 | COD\_PART | Código do participante emitente (campo 02 do Registro 0150) do documento referenciado. | DLAF.EMITENTECFO | Código do Cliente/Fornecedor do lançamento referenciado. |
| 05 | COD\_MOD | Código do documento fiscal, conforme a Tabela 4.1.1 | FTDO.CODMODDOC | Código do modelo de documento vinculado ao lançamento referenciado. |
| 06 | SER | Série do documento fiscal | DLAF.SERIEDOC | Série do documento fiscal referenciado. |
| 07 | SUB | Subsérie do documento fiscal | DLAF.SUBSERIE | Subsérie do documento fiscal referenciado. |
| 08 | NUM\_DOC | Número do documento fiscal | DLAF.DOCINI | Número do documento fiscal referenciado. |
| 09 | DT\_DOC | Data da emissão do documento fiscal. | DLAF.DATAEMISSAO | Data da emissão do documento fiscal referenciado. |
| 10 | CHV\_DOCe | Chave do Documento Eletrônico | DLAFREFERENCIA.CHAVEACESSO ou DLAF.CHAVEACESSONFE ou TNFEESTADUAL.CHAVEACESSO | Será gerado com o campo "Chave de Acesso" da aba de referência do lançamento fiscal, caso este campo não esteja preenchido o comportamento segue o mesmo tratamento existente no Campo 09 - Chave de Acesso do Registro C100 - que é gerado com a chave preenchida no lançamento fiscal e caso não esteja preenchida é gerado com a chave da tabela TNFEESTADUAL |

C114C114

**Cupom Fiscal referenciado**

Este registro deve ser apresentado, obrigatoriamente, quando o lançamento fiscal possuir uma ou   outros lançamentos relacionados a ele que sejam do modelo igual a 02, 2D ou 2E.

C115C115

**Local de Coleta e Entrega**

Este registro tem por objetivo informar o local de coleta, quando este for diferente do endereço do emitente do documento fiscal e o local de entrega, quando este for diferente do endereço do destinatário do documento fiscal, além de informar a modalidade de transporte utilizada. As informações prestadas referem-se a transporte próprio ou de terceiros.

C120C120

**Operações de Importação**

Este registro tem por objetivo informar detalhes das operações de importação, que estejam sendo documentadas pela nota fiscal escriturada no registro C100, quando o campo IND\_OPER for igual a "0" (zero), indicando operação de entrada.  
Não podem ser informados, para um mesmo documento fiscal, dois ou mais registros com o mesmo conteúdo no campo NUM\_DOC\_\_IMP. Todos os lançamentos de ENTRADA que forem do modelo 01, 55 (importação) devem gerar este registro.

O registro será gerado somente se o Número da Declaração de Importação estiver preenchido, caso contrário será informado no Log da rotina que o registro não foi gerado.

C120C120

**Operações de Importação**

Este registro tem por objetivo informar detalhes das operações de importação, que estejam sendo documentadas pela nota fiscal escriturada no registro C100, quando o campo IND\_OPER for igual a "0" (zero), indicando operação de entrada.  
Não podem ser informados, para um mesmo documento fiscal, dois ou mais registros com o mesmo conteúdo no campo NUM\_DOC\_\_IMP. Todos os lançamentos de ENTRADA que forem do modelo 01, 55 (importação) devem gerar este registro.

O registro será gerado somente se o Número da Declaração de Importação estiver preenchido, caso contrário será informado no Log da rotina que o registro não foi gerado.

C130C130

**ISSQN, IRRF e PREVIDÊNCIA SOCIAL**

Este registro tem por objetivo informar dados da prestação de serviços sob não-incidência ou não tributados pelo ICMS e ainda detalhes sobre a retenção de Imposto de Renda Retido na Fonte (IRRF) e de contribuições previdenciárias. Essas três situações possuem características próprias e tratamentos específicos na legislação, não guardando entre elas nenhuma relação.

C140C140

**Dados da Fatura**

Este registro deverá ser gerado quando um lançamento for do modelo 01, o tipo de pagamento do mesmo for considerado A PRAZO e o lançamento estiver sido escriturado do movimento (DLAF.IDMOV deve conter algum valor referente a um movimento).  
Este registro tem por objetivo informar dados da fatura comercial, sempre que a aquisição ou venda de mercadorias for a prazo. Devem ser consideradas as informações quando da emissão do documento fiscal, incluindo a parcela paga no ato da operação, se for o caso.

C141C141

**Vencimento da Fatura**

Este Registro deve ser apresentado, obrigatoriamente, sempre que for informado o registro C140, devendo ser discriminando o valor e a data de vencimento de cada uma das parcelas.  
***Observação***: Não podem ser informados dois ou mais registros com o mesmo conteúdo para o campo NUM\_PARC.

C160C160

**Volumes transportados**

Este registro tem por objetivo informar detalhes dos volumes, do transportador e do veículo empregado no transporte nas operações de saída.  
Este registro será gerado para os lançamentos de saída, que possuem transportadora relacionada, e forem do modelo 01, 04 ou 55.

C170C170

**Itens do Documento**  
Registro obrigatório para discriminar os itens da nota fiscal, inclusive em operações de entrada de mercadorias acompanhada de Nota Fiscal Eletrônica (NF-e) de emissão de terceiros. Conforme item 2.4.2.2.1 do Ato COTEPE nº 09/08, o termo "item" é aplicado às operações fiscais que envolvam mercadorias, serviços, produtos ou quaisquer outros itens concernentes às transações fiscais suportadas pelo documento. Exemplo: nota fiscal complementar.  
Não podem ser informados, para um mesmo documento fiscal, dois ou mais registros com o mesmo conteúdo no campo NUM\_ITEM.

**Observações Gerais:**

* ***Campo 2-******NUM\_ITEM***:  este campo é gerado respeitando a sequência crescente do NUM\_ITEM da tabela DLAF .

* **Campo 04 DESCR\_COMPL -** é gerado de acordo com a Observação do Item do Lançamento Fiscal. A partir da versão 12.1.2205, será considerado o valor do campo "Descrição do produto do fornecedor" para lançamentos de Entrada.  
    
  Regras de geração:  
    
  **1 -** Caso o campo não seja preenchido o valor continua sendo gerado de acordo com a Observação do Item.  
    
  **2 -** Caso ambos os campos estejam preenchidos será considerado o campo Descrição do produto do fornecedor.

  O campo pode ser informado no módulo de Faturamento e escriturado para o módulo Fiscal, para mais detalhes sobre o preenchimento no movimento [clique aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=574890054)

Campo Descrição do Produto do FornecedorDisponível nos Lançamentos de Entrada a partir da versão 12.1.2205.  
Campo Observação

* **Geração do Campo 20:** do registro C170: Campo referente ao CST do IPI, este campo somente será gerado se a Flag "Contribuinte IPI" disponível no cadastro da Filial >> Anexo Dados Fiscais >> Aba Tributos, estiver marcada.

O CST é gerado com a informação do campo 'Situação Tributária' informado na regra do IPI, que está associado à natureza de operação vinculada ao lançamento fiscal."

* ***Campo 38 - VL\_ABAT\_NT:*** Valor do abatimento não tributado e não comercial  
  Quando na regra de ICMS o campo *"ICMS Deson. Não afeta Valor Contábil"* não estiver marcado, será gerado com o valor do campo *"ICMS Desonerado"* do Item .  
  Obs.: Mesma Regra para preenchimento do campo no Registro C100.

### ICMS Monofásico

* **Campo 13 (VL\_BC\_ICMS):** Valor da base de cálculo do ICMS  
  Quando, no lançamento de entrada, os dois últimos caracteres do campo "CST\_ICMS" forem preenchidos com os valores "02", "15", "53" ou "61", o campo "VL\_BC\_ICMS" será gerado com o valor "0".

* **Campo 14 (ALIQ\_ICMS):** Alíquota do ICMS  
  Para os lançamentos de entrada, se os dois últimos caracteres do campo "CST\_ICMS" forem:  
  -  "02", "15" ou "53": o campo "ALIQ\_ICMS" será preenchido com o valor da "Alíquota Ad Rem";  
  - "61": o campo "ALIQ\_ICMS" será "0".  
  Para o ICMS monofásico, será trazido o valor do campo "Alíquota Ad Rem", presente junto aos valores do ICMS do item do lançamento.

  Campo "Alíquota Ad Rem"

* **Campo 16 (VL\_BC\_ICMS\_ST):** Valor da base de cálculo referente à substituição tributária  
  Mesma regra do campo "VL\_BC\_ICMS".  
  Quando, no lançamento de entrada, os dois últimos caracteres do campo "CST\_ICMS" forem preenchidos com os valores 02", "15", "53" ou "61", o campo "VL\_BC\_ICMS\_ST" será gerado com o valor "0".

* **Campo 17 (ALIQ\_ST):** Alíquota da substituição tributária  
  Para lançamentos de entrada, se os dois últimos caracteres do campo "CST\_ICMS" forem:  
  - "02" ou "61": o campo "ALIQ\_ST" será preenchido com o valor "0";  
  - "15" ou "53": o campo "ALIQ\_ST" será preenchido com o valor da "Alíquota Ad Rem".

Precisão da alíquota

É possível preencher o valor do campo "Alíquota Ad Rem" com quatro casas decimais. Porém, ao gerar o SPED, ela será retornada considerando apenas as primeiras duas casas decimais, sem arredondamento.

CSTs 02, 15, 53 e 61

Estes CSTs não são preenchidos automaticamente. É necessário informá-los manualmente.

C171C171

**Armazenamento de Combustíveis**

Este registro deverá ser gerado quando um lançamento for do modelo 01 ou 55 e o lançamento estiver sido escriturado do movimento (DLAF.IDMOV deve conter algum valor referente a um movimento).  
Deve ser apresentado pelas empresas do segmento de combustíveis, somente nas operações de entrada, para informar o volume recebido (em litros), por item do documento fiscal, conforme Livro de Movimentação de Combustíveis (LMC), Ajuste SINIEF 01/92.  
Não podem ser informados para um mesmo documento fiscal, dois ou mais registros com o mesmo conteúdo no campo NUM\_TANQUE.  
Este registro será gerado se o "Tipo de Operação com combustíveis" da Filial for "Posto Varejista"

C172C172

**Operações com ISS**

Este registro tem por objetivo informar os dados Prestação de serviços.

C173C173

**Operações com medicamentos**

O modelo do documento deve ser 01 ou 55 - O produto deve possuir lote - Em cadastro do Produto, Anexo Dados Fiscais do Produto e Aba Tributação o campo Produto sujeito regulações sanitárias deve estar habilitado. - Registro da Anvisa Preenchido no Cadastro Produto, (Anexo do Saúde ou Dados do Produto Aba Integração)

C174C174

**Operações com Armas de Fogo (Código 01)**

**Registro não gerado**

C175C175

**Operações com Veículos Novos (código 01 e 55)**

**Registro não gerado**

C176C176

**Ressarcimento de ICMS em Operações com Substituição Tributária**

Conforme o manual, a obrigatoriedade e a forma de escrituração deste registro serão definidas pela UF de domicílio do contribuinte.  
  
A inclusão da Referência do Item é somente para Gerar o Registro C176, por este motivo não vamos tratar no processo de Escrituração e no "TOTVS Gestão de Estoques, Compras e Faturamento".  A Referencia do Item deve ser incluída manualmente ou através do processo de [Associação Lançamentos de Saída](https://tdn.totvs.com/pages/viewpage.action?pageId=438273534).  
  
Este Registro deve ser gerado para todos os lançamentos de saída interestaduais e que tenha destaque do valor do ICMS ST. O registro filho do Registro C170, então será necessário para o Tipo de Documento 55(NF-e), será necessário gerar o Registro C170 somente para os Item que tem referência preenchida e que esteja marcado o parâmetro na tela da rotina "Gerar C176".

***O**bservação****:* Atualmente já geramos este registro para os lançamentos de entrada ou saída que possuem lançamento referenciados com os seguintes CFOP's: 5.603, 6.603, 1.603 e 2.603.

* **Lançamento Fiscal**
  + Habilitado no Item do Lançamento Fiscal, a Sub Pasta Referência (Tabela DITEMREFERENCIA) somente para:
  + Lançamento de Saída;
  + Com CFOP do Grupo 6.4xx - Saídas de Mercadoria Sujeitas ao Regime de Substituição;
  + Regra de ICMS – Tipo de Operação "Substituição Tributaria";
* **Importação de Lançamento Fiscal Delphi**

Este novo campo não será importado no processo Delphi, apenas na importação .Net (Web Service).

* **Geração do Registro C176 no SPED Fiscal (código 01, 55)**

Alterada a consistência existente  na geração do Registro C176. Este Registro deve ser gerado somente para os Itens que geram direito ao Ressarcimento da ST e que a Referência por Item esteja informada.

Ao gerar os Registros C100 e C190 dos Lançamentos de Saída com o Tipo de Documento 55(NFe), será gerado o Registro C170 somente dos Itens que tem Referência informado. Este registro deve ser informado quando da escrituração de documento fiscal, que acoberte operação que represente desfazimento de substituição tributária realizada em operações anteriores.

O documento informado neste registro deverá ser diferente do documento informado no registro pai (C100), pois é o documento referente à(s) última(s) aquisição(ões) da mercadoria e à retenção do imposto. A obrigatoriedade e a forma de escrituração deste registro serão definidas pela UF de domicílio do contribuinte, inclusive sobre a apresentação dos campos: CHAVE\_NFE\_RET; COD\_PART\_NFE\_RET; SER\_NFE\_RET; NUM\_NFE\_RET;ITEM\_NFE\_RET.  
  
Este registro não se aplica a contribuintes que utilizam o SCANC. 

Alíquota ICMS

Caso o valor da **Alíquota ICMS** seja igual a zero no Lançamento Fiscal, o sistema buscará o valor da alíquota definido na **Regra de ICMS**, nos Dados da Natureza.

***Observação***: Os campos 09, 12, 13, 14, 15 e 17 do registro C176 são gerados com base no valor unitário do item. O valor final calculado será dividido pela quantidade de itens.  
Este registro será gerado para todas as referências do mesmo item.

Este registro será gerado para todas as operações de saída em quem o parâmetro "Operação com Ressarcimento de ST na Compra" estiver habilitado na Natureza de Operação (CFOP) associado ao Lançamento ao Lançamento Fiscal.

**Novos campos Layout 2019:**

* **Registro C176: Ressarcimento de ICMS e Fundo de Combate a Pobreza (FCP) Em operações com ST (Código 01, 55)**

Incluída a opção "6 – Venda interna para Simples Nacional" no campo 19 - COD\_MOT\_RES (Código do motivo do ressarcimento).  
  
O preenchimento desse campo é realizado junto a Referência informada no Item do Lançamento Fiscal:

Inclusão do campo 27 - VL\_UNIT\_RES\_FCP\_ST (Valor unitário do ressarcimento (parcial ou completo) de FCP decorrente da quebra da ST).  
Campo gerado de acordo com o campo VlrICMSItemFCPEstDEST do Item do Lançamento Fiscal.  
  
Gerado com a informação do campo "Valor ICMS FCP"

[Portaria CAT 158 de 2015 - Ressarcimento ICMS Retido por Sujeição Passiva de Substituição Tributaria](https://portal.fazenda.sp.gov.br/servicos/st/Paginas/Ressarcimento-de-Substitui%C3%A7%C3%A3o-Tribut%C3%A1ria-do-ICMS.aspx).

C177C177

**Operações com Produtos sujeitos a selo de controle de IPI**

Para gerar este registro o código de selo IPI do produto deve estar preenchido (dados fiscais do produto)  
Registrar o tipo e a quantidade de selo de controle utilizado pelo contribuinte na saída dos produtos sujeitos ao selo de controle. Ex. bebidas quentes, cigarros e relógios. Se o produto vendido está sujeito à selagem, o registro é obrigatório. O registro não deve ser informado nas operações de aquisição de produtos. Os códigos dos selos de controle constam indicados na Tabela 4.5.2 do Ato COTEPE nº 09/08.

**Complemento de Item - Outras Informações (Código 01, 55) - Válido a partir de 01/01/2019**

Será gerado com as informações do novo [Cadastro de Códigos de Ajuste](http://tdn.totvs.com.br/pages/viewpage.action?pageId=427053053) que estiverem associados a Lançamentos Fiscais ou Itens de Lançamentos Fiscais.

**Localização do Cadastro**

O cadastro do Código de Ajuste deve ser realizado no módulo do BackOffice→ Gestão Fiscal em CADASTROS → MAIS → CÓDIGO DE AJUSTE

Imagem

### Formulário Cadastro de Ajuste:

A informação do C177 - complemento do Item será proveniente do Código de Ajuste informado no Item do Lançamento Fiscal.  
Quando o campo REGISTRO for preenchido com C177 apenas os campos ESTADO, DESCRIÇÃO COMPLEMENTAR DO AJUSTE E CÓDIGO DE AJUSTE vão ficar disponíveis para preenchimento.

Imagem**Observação**: Ao selecionar a opção C177 do campo *Registro* o código do campo Código de Ajuste deverá constar na Tabela 5.6 do SPED Fiscal, conforme determinação da UF da Filial declarante.

No arquivo texto gerado o campo 02 (COD\_INF\_ITEM) será o código informado no campo Código de Ajuste.

### Formulário Ajuste SPED no Lançamento:

No item do Lançamento Fiscal está disponível a opção Ajuste SPED, onde deve ser informado o Código de Ajuste cadastrado anteriormente. Informar o código no Item do Lançamento Fiscal:

Imagem

Ao gerar o SPED Fiscal dos modelos de documentos 01 ou 55 no exercício maior ou igual a 2019, o registro C177 do Item será gerado com o Código de Ajuste informado.

> **Para gerações anteriores a 01/01/2019:**
>
> Para gerar este registro o código de selo IPI do produto deve estar preenchido (dados fiscais do produto)  
> Registrar o tipo e a quantidade de selo de controle utilizado pelo contribuinte na saída dos produtos sujeitos ao selo de controle. Ex. bebidas quentes, cigarros e relógios. Se o produto vendido está sujeito à selagem, o registro é obrigatório. O registro não deve ser informado nas operações de aquisição de produtos. Os códigos dos selos de controle constam indicados na Tabela 4.5.2 do Ato COTEPE nº 09/08.

C178C178

**Operações com produtos sujeitos a tributação de IPI por Unidade ou quantidade de Produto**

O registro tem por objetivo fornecer informações adicionais sobre os produtos das posições 24022000 (cigarros) e 2204, 2205, 2206 e 2208 (bebidas quentes), relacionados na Tabela 4.5.1 do Ato COTEPE nº 09/08, cuja forma de tributação do IPI, fixada em reais, é calculada por unidade ou por determinada quantidade de produto, conforme tabelas de classes de valores.

C179C179

**Informações complementares ST**

Este registro tem por objetivo informar operações que envolvam repasse, dedução e complemento de ICMS\_ST nas operações interestaduais e nas operações com substituído intermediário

C180C180

**Informações Complementares das Operações de Entrada de Mercadorias Sujeitas à Substituição Tributária (Código 01, 1B, 04 e 55)**

O Registro C180 é “filho” do registro C170 que são os itens do Lançamento Fiscal. Para gerar esse arquivo é necessário marcar o Parâmetro "**Gerar ressarcimento/complemento ICMS ST**" na tela de geração do SPED Fiscal.

O parâmetro "**Utilizar unidade de Controle do Estoque nos registros do ressarcimento do ICMS ST**" deverá ser marcado quando a UF solicitar que a unidade de controle do produto seja do Estoque em vez da unidade de comercialização.

Atenção!

Todos os campos de valores deste registro serão gerados considerando essa unidade, utilizando o fator de conversão informado.

Serão selecionados os Lançamentos Fiscais que atendam às seguintes regras:

* Lançamentos de entrada;
* CFOP associado esteja marcado como operação que controla ressarcimento/complemento do ST (DCFOP.OPERACAOSTCOMPRA)
* Modelos de documentos “01”, “1B”, “04” e “55”;
* Produto estiver marcado como tributado pelo ICMS ST nos Dados Fiscais por UF, considerando a UF da Filial (TPRDCODFISCAL.TRIBUTADOICMSST)
* Exista Lançamento de Ajuste para o Registro C185 associado ao Item do Lançamento

O preenchimento dos campos desse registros, seguem as seguintes regras:

**Campo 02** (COD\_RESP\_RET) - Código que indica o responsável pela retenção do ICMS-ST:

1-Remetente Direto   
2-Remetente Indireto   
3-Próprio declarante

Esse campo será gerado de acordo com o campo "**Situação da Retenção ICMS ST**" na pasta Dados ICMS ST da Regra do ICMS (DREGRAICMS.RETENCAOICMSST):

* Substituto Tributário = 1
* Não Se Aplica = 2
* Antecipação = 3

**Campo 03** (QUANT\_CONV) – Quantidade do item convertida na unidade de controle de estoque informada no registro 0200 ou a unidade de comercialização, a critério de cada UF.

Se o parâmetro "**Utilizar unidade de Controle do Estoque nos registros do ressarcimento do ICMS ST**" estiver marcado então será considerado o **Fator** da Unidade de Controle do Estoque TPRODUTODEF.CODUNDCONTROLE em relação a Unidade do Item do Lançamento Fiscal (**DITEM.QTDEPRD x Fator**)

Senão Será gerado com a quantidade informada no Item do Lançamento Fiscal (DITEM.QTDEPRD). 

Os campos abaixo vão considerar o **Fator**encontrado para o calculo unitário dos tributos.

**Campo 04** (UNID) - Unidade adotada para informar o campo QUANT\_CONV.

Se "**Utilizar unidade de Controle do Estoque nos registros do ressarcimento do ICMS ST**" então TPRODUTODEF.CODUNDCONTROLE

Senão DITEM.CODUND

**Campo 05** (VL\_UNIT\_CONV) – Valor unitário líquido do item/produto (considerando descontos e acréscimos incondicionais aplicados sobre o valor bruto) considerando a unidade utilizada para informar o campo “QUANT\_CONV”.

Será calculado pelo sistema utilizando o fator de conversão entre a unidade do lançamento e a unidade informada no campo "UNID", se for caso.

**Atenção!** Preencher corretamente o a Unidade Base no Cadastro da Unidade para correta conversão.

(DITEM.VALORMERC - DITEM.DESCONTOITEM + DITEM.VALORDESPESA +DITEM.VLRFRETE + DITEM.VALORSEGURO) / QUANT\_CONV)

**Campo 06** (VL\_UNIT\_ICMS\_OP\_CONV) - Valor unitário do ICMS operação própria que o informante teria direito ao crédito caso a mercadoria estivesse sob o regime comum de tributação, considerando unidade utilizada para informar o campo “QUANT\_CONV”.

Corresponde

Nos casos em que a nota do fornecedor vier preenchida com CST 60 e CSOSN 500 (ICMS cobrado anteriormente por substituição tributária), o valor desse campo não corresponde ao valor preenchido no campo N26b (vICMSSubstituto), Valor  
do ICMS próprio do Substituto.

(DITEM.VLRICMSPRD / QUANT\_CONV)

**Campo 07** (VL\_UNIT\_BC\_ICMS\_ST\_CONV) - Valor unitário da base de cálculo do imposto pago ou retido anteriormente por substituição, considerando a unidade utilizada para informar o campo “QUANT\_CONV”, aplicando-se redução, se houver.

(DITEM.BASEICMSSTPRD / QUANT\_CONV)

**Campo 08** (VL\_UNIT\_ICMS\_ST\_CONV) - Preenchimento: Informar o valor unitário do ICMS ST pago ou retido limitado à parcela do ICMS ST correspondente ao fato gerador presumido que ainda não se realizou. Corresponde ao campo 07  
(VL\_UNIT\_BC\_ICMS\_ST \_CONV), aplicada a redução de base de cálculo se houver, multiplicada pela alíquota interna (com o adicional de FCP), estabelecida pela legislação da UF, subtraída do campo 06 (VL\_UNIT\_ICMS\_OP\_CONV).

( Campo 07 (VL\_UNIT\_BC\_ICMS\_ST \_CONV), com redução, conforme a legislação da UF \* alíq. interna (incluindo o adicional de FCP) ) - Campo 06 (VL\_UNIT\_ICMS\_OP\_CONV) = Campo 08 (VL\_UNIT\_ICMS\_ST\_CONV)

(DITEM.VLRICMSSTPRD / QUANT\_CONV)

**Campo 09** (VL\_UNIT\_FCP\_ST\_CONV) – Preenchimento: Informar o valor unitário do Fundo de Combate à Pobreza (FCP) vinculado à substituição tributária que compõe o campo “VL\_UNIT\_ICMS\_ST\_CONV”, considerando a unidade  
utilizada para informar o campo “QUANT\_CONV”, conforme previsão das legislações das UF. 

(DITEM.VLRICMSITEMFCPESTDEST / QUANT\_CONV)

**Campo 10** (COD\_DA) - Código do modelo do documento de arrecadação:  
0 – Documento estadual de arrecadação  
1 – GNRE

Não será gerado no primeiro momento.

**Campo 11** (NUM\_DA) - Número do documento de arrecadação estadual, se houver.

Não será gerado no primeiro momento.

C181C181

**Informações Complementares das Operações de Devolução de Saídas de Mercadorias Sujeitas à Substituição Tributária (Código 01, 1B, 04 e 55)**

O Registro C181 é “filho” do registro C170 que são os itens do Lançamento Fiscal. Para gerar esse arquivo é necessário marcar o Parâmetro "**Gerar ressarcimento/complemento ICMS ST**" na tela de geração do SPED Fiscal.

O parâmetro "**Utilizar unidade de Controle do Estoque nos registros do ressarcimento do ICMS ST**" deverá ser marcado quando a UF solicitar que a unidade de controle do produto seja do Estoque em vez da unidade de comercialização.

Serão selecionados os Lançamentos Fiscais que atendam às seguintes regras:

* Lançamentos de Entrada (Devolução de Venda);
* CFOP associado esteja marcado como operação que controla ressarcimento/complemento do ST (DCFOP.OPERACAOSTCOMPRA)
* CFOP com o Tipo “Devolução” habilitado (DCFOP.TIPODEVOLUCAO)
* Produto estiver marcado como tributado pelo ICMS ST nos Dados Fiscais por UF, considerando a UF da Filial (TPRDCODFISCAL.TRIBUTADOICMSST)
* Exista Lançamento de Saída referenciado
* Informações geradas baseado no Lançamento de Saída referenciado (Registro C185).

Informação

*Situação não deve gerar o* ***Registro C180****.*

Registro será gerado a partir de 2021.

*O preenchimento dos campos desse registros, seguem as seguintes regras:*

**Campo 02** (COD\_MOT\_REST\_COMPL) - Código do motivo da restituição ou complementação conforme Tabela 5.7.

Este campo será gerado com conteúdo do campo "*Código de Ajuste*" do cadastro de Ajustes do Registro C181 vinculado ao Item do Lançamento Fiscal.

Atenção!

Se o terceiro caractere do código preenchido no campo “COD\_MOT\_REST\_COMPL” for:

a) igual a 5, os campos 16 a 21 não devem ser preenchidos.  
b) igual a 6, os campos 13, 14, 15, 16, 20 e 21 devem ser preenchidos e os campos 17, 18 e 18 não devem ser preenchidos.

c) igual a 7, os campos 13, 14, 15, 17, 20 e 21 devem ser preenchidos e os campos 18 e 19 não devem ser preenchidos.

d) igual a 8, os campos 13, 14, 15, 16, 18 e 19 devem ser preenchidos e os campos 17, 20 e 21 não devem ser preenchidos.

**Campo 03** (QUANT\_CONV) – Quantidade do item convertida na unidade de controle de estoque informada no registro 0200 ou a unidade de comercialização, a critério de cada UF.

Se o parâmetro "**Utilizar Unidade de Controle do Estoque nos registros do ressarcimento do ICMS ST**" estiver marcado será utilizado o fator de Conversão entre a Unidade do Item do Lançamento e a Unidade de Controle do Produto para calcular o valor a ser gerado neste campo.

**Campo 04** (UNID) - Unidade de medida adotada para o controle de ressarcimento/restituição de ICMS ST.

Se o parâmetro "**Utilizar Unidade de Controle do Estoque nos registros do ressarcimento do ICMS ST**" estiver marcado, este campo será gerado com a Unidade de Controle do Produto. Caso contrário, será gerado com a Unidade do Item do Lançamento Fiscal.

**Campo 05** (COD\_MOD\_SAIDA) - Código do modelo do documento fiscal de saída, conforme a tabela indicada no item 4.1.1

**Campo 06** (SERIE\_SAIDA) - Número de série do documento de saída em papel.

**Campo 07** (ECF\_FAB\_SAIDA) - Número de série de fabricação do equipamento ECF.

**Campo 08** (NUM\_DOC\_SAIDA) - Número do documento fiscal de saída.

**Campo 09** (CHV\_DFE\_SAIDA) - Chave do documento fiscal eletrônico de saída.

**Campo 10** (DT\_DOC\_SAIDA) - Data da emissão do documento fiscal de saída.

**Campo 11** (NUM\_ITEM\_SAIDA) - Número do item em que foi escriturada a saída em um registro C185, C380, C480 ou C815.

**Campo 12** (VL\_UNIT\_CONV\_SAIDA) -  Valor unitário da mercadoria, considerando a unidade utilizada para informar o campo “QUANT\_CONV” (considerando descontos e acréscimos incondicionais aplicados sobre o valor bruto). 

O campo será gerado com o Valor de Mercadoria do Item, retirados os Descontos e acrescidas as Despesas o Frete e o Seguro. Se o parâmetro "**Utilizar Unidade de Controle do Estoque nos registros do ressarcimento do ICMS ST**" estiver marcado será utilizado o fator de Conversão entre a Unidade do Item do Lançamento e a Unidade de Controle do Produto para calcular o valor a ser gerado neste campo.

**Campo 13** (VL\_UNIT\_ICMS\_OP\_ESTOQUE\_CONV\_SAIDA) - Informar o valor médio unitário de ICMS OP, das mercadorias em estoque obtido através do cálculo a partir do estoque inicial de ICMS declarado no H030 (Campo 02 – VL\_ICMS\_OP) adicionado às informações de ICMS declarado nos registros C180 (Campo 06 - VL\_UNIT\_ICMS\_OP\_CONV) ocorridas até a data da saída do documento declarado no C185. 

O período para o cálculo do valor médio deve atender à legislação de cada UF. Ex. diário, mensal etc

**Campo 14**  (VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV\_SAIDA) - Informar o valor médio unitário do ICMS ST, incluindo FCP ST, pago ou retido, das mercadorias em estoque. Quando a mercadoria estiver sujeita ao FCP adicionado ao ICMS ST, neste campo deve ser informado o valor médio unitário da parcela do ICMS ST + a parcela do FCP. Obtido através do cálculo a partir do estoque inicial de ICMS declarado no H030 (Campo 04 – VL\_ICMS\_ST) adicionado às informações de ICMS declarado nos registros C180 (Campo 08 - VL\_UNIT\_ICMS\_ST\_CONV) ocorridas até a data da saída do documento declarado no C185.

O período para o cálculo do valor médio deve atender à legislação de cada UF. Ex. diário, mensal etc.

**Campo 15** (VL\_UNIT\_FCP\_ICMS\_ST\_ESTOQUE\_CONV\_SAIDA) - Informar o valor médio unitário da parcela do FCP adicionado ao ICMS que tenha sido informado no campo “VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV”.

**Campo 16** (VL\_UNIT\_ICMS\_NA\_OPERACAO\_CONV\_SAIDA) - Valor correspondente à multiplicação da alíquota interna (incluindo FCP) da mercadoria pelo valor correspondente à operação de saída que seria tributada se não houvesse ST, considerando a unidade utilizada para informar o campo “QUANT\_CONV”, aplicando-se a mesma redução da base de cálculo do ICMS ST na tributação, se houver.

**Campo 17** (VL\_UNIT\_ICMS\_OP\_CONV\_SAIDA) - Nos casos de devolução em que houve direito a crédito do imposto pela não ocorrência do fato gerador presumido e desfazimento da ST, e a legislação da UF do informante adota o preenchimento desse campo, informar o valor preenchido no campo de mesmo nome na escrituração do documento de saída.

Para as UFs em que a legislação estabelecer que o valor desse campo corresponderá ao mesmo valor expresso no campo 13 (VL\_UNIT\_ICMS\_OP\_ESTOQUE\_CONV\_SAIDA), seu preenchimento será facultativo.

O valor deste campo, quando obrigatório na UF, será utilizado para o cálculo do valor do estorno do ressarcimento/restituição do campo (VL\_UNIT\_ICMS\_ST\_CONV\_COMPL), conforme fórmula abaixo:

*Campo 13 (VL\_UNIT\_ICMS\_OP\_ESTOQUE\_CONV\_SAIDA) + Campo 14 (VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV\_SAIDA) - Campo 17 (VL\_UNIT\_ICMS\_OP\_CONV\_SAIDA) = Campo 20 (VL\_UNIT\_ICMS\_ST\_CONV\_COMPL)*

**Campo 18** ( VL\_UNIT\_ICMS\_ST\_CON)V\_REST) - Valor do estorno do complemento cobrado em saída anterior cuja devolução é escriturada no Registro C181.

Quando o preenchimento dos campos 13, 14, 15 e 16 for obrigatório de acordo com a legislação da UF, o valor do estorno do complemento é calculado conforme as orientações a seguir:

*Campo 16 (VL\_UNIT\_ICMS\_NA\_OPERACAO\_CONV\_SAIDA) - Campo 13 (VL\_UNIT\_ICMS\_OP\_ESTOQUE\_CONV\_SAIDA) - Campo 14 (VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV\_SAIDA)*

*= Campo 18 VL\_UNIT\_ICMS\_ST\_CONV\_REST)*

**Campo 19** (VL\_UNIT\_FCP\_ST\_CONV\_REST) - Informar o valor unitário do Fundo de Combate à Pobreza (FCP) vinculado à substituição tributária que compõe o campo “VL\_UNIT\_ICMS\_ST\_CONV\_REST”, considerando a unidade utilizada para informar o campo “QUANT\_CONV”, conforme previsão das legislações das UF.

**Campo 20** (VL\_UNIT\_ICMS\_ST\_CONV\_COMPL) - O estorno do valor ressarcido / restituído em operação de saída anterior, cuja devolução é escriturada no Registro C181, é calculado conforme as orientações a seguir:

a) Nos casos em que **não houve ocorrência do fato gerador presumido**:

       a.1) Quando o preenchimento dos campos 13, 14, 15 e 17 for obrigatório de acordo com a legislação da UF, correspondente ao seguinte cálculo, considerando a unidade utilizada para informar o campo “QUANT\_CONV”:

*Campo 13((VL\_UNIT\_ICMS\_OP\_ESTOQUE\_CONV\_SAIDA) + Campo 14((VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV\_SAIDA) - Campo 17 (VL\_UNIT\_ICMS\_OP\_CONV\_SAIDA) = Campo 20 (VL\_UNIT\_ICMS\_ST\_CONV\_COMPL)*

*a.2) Quando o campo 17 (VL\_UNIT\_ICMS\_OP\_CONV\_SAIDA) não for obrigatório e o preenchimento do campo 14 for obrigatório, de acordo com a legislação da UF, corresponde ao valor no campo 14  
(VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV\_SAIDA).*

*b) Nos casos em que houve direito ao crédito do imposto, calculada com base no valor de saída da mercadoria inferior ao valor da BC ICMS ST, quando o preenchimento dos campos 13, 14, 15 e 16 for obrigatório de  
acordo com a legislação da UF, informar o valor unitário de ICMS correspondente ao seguinte cálculo,**considerando a unidade utilizada para informar o campo “QUANT\_CONV”:*

*Campo 13 (VL\_UNIT\_ICMS\_OP\_ESTOQUE\_CONV\_SAIDA) + Campo 14 (VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV\_SAIDA) - Campo 16 (VL\_UNIT\_ICMS\_NA\_OPERACAO\_CONV\_SAIDA)*

*= Campo 20 (VL\_UNIT\_ICMS\_ST\_CONV\_ COMPL)*

**Campo 21** (VL\_UNIT\_FCP\_ST\_CONV\_COMPL) - Valor unitário correspondente à parcela de ICMS FCP ST que compõe o campo “VL\_UNIT\_ICMS\_ST\_CONV\_COMPL”, considerando unidade utilizada para informar  
o campo “QUANT\_CONV”.

C185C185

**Informações Complementares das Operações de Saída de Mercadorias Sujeitas à Substituição Tributária (Códigos 01, 1B, 04, 55 e 65)**

O Registro C185 é “filho” do registro C100 que é o próprio Documento Fiscal. Para gerar esse arquivo é necessário marcar o Parâmetro "**Gerar ressarcimento/complemento ICMS ST**" na tela de geração do SPED Fiscal.

Será preciso informar, também na tela de geração do SPED Fiscal, qual é o critério de informação da unidade para o Estado que está sendo gerado a rotina: se pela unidade do estoque (0200) ou pela unidade de comercialização (unidade informada nos Lançamentos Fiscais).

Atenção!

Todos os campos de valores deste registro serão gerados considerando essa unidade, utilizando o fator de conversão informado.

Serão selecionados os Lançamentos Fiscais que atendam às seguintes regras:

* Lançamentos de saída;
* CFOP associado esteja marcado como operação que controla ressarcimento/complemento do ST (DCFOP.OPERACAOSTCOMPRA)
* Modelos de documentos “01”, “1B”, “04”, “55” e "65";
* Produto estiver marcado como tributado pelo ICMS ST nos Dados Fiscais por UF, considerando a UF da Filial (TPRDCODFISCAL.TRIBUTADOICMSST)
* Exista Lançamento de Ajuste para o Registro C185 associado ao Item do Lançamento

IMPORTANTE!

Para correta geração desse registro é imprescindível que o processo de associação já tenha sido executada. Para saber mais sobre este processo, consulte este link: [Associação Lançamentos de Saída](https://tdn.totvs.com/pages/viewpage.action?pageId=438273534).

O preenchimento dos campos desse registros, seguem as seguintes regras:

**Campo 02** (NUM\_ITEM) - Número sequencial do item no documento fiscal.

**Campo 03** (COD\_ITEM) - Código do item (campo 02 do Registro 0200).

**Campo 04** (CST\_ICMS) – Código da Situação Tributária referente ao ICMS.

**Campo 05** (CFOP) - Código Fiscal de Operação e Prestação que consta no documento fiscal.

**Campo 06** (COD\_MOT\_REST\_COMPL) - Código do motivo da restituição ou complementação conforme Tabela 5.7.

Este campo será gerado com conteúdo do campo "*Código de Ajuste*" do cadastro de Ajustes do Registro C185 vinculado ao Item do Lançamento Fiscal.

Atenção!

Se o terceiro caractere do código preenchido no  
campo “COD\_MOT\_REST\_COMPL” for:  
a) igual a 0, os campos 12, 13 e 14 devem ser preenchidos e os campos 10, 11 e 15 a 18 **não** devem ser preenchidos.  
b) igual a 1, os campos 10, 12, 13, 14, 15 e 16 devem ser preenchidos e os campos 11, 17 e 18 **não** devem ser preenchidos  
c) igual a 2, os campos 12, 13, 14, 15 e 16 devem ser preenchidos e os campos 10, 17 e 18 **não** devem ser preenchidos. O campo  
11 pode ser preenchido de acordo com a legislação de cada UF.  
d) igual a 3, os campos 10, 12, 13, 14, 17 e 18 devem ser preenchidos e os campos 11, 15 e 16 **não** devem ser preenchidos.

**Campo 07** (QUANT\_CONV) – Quantidade do item convertida na unidade de controle de estoque informada no registro 0200 ou a unidade de comercialização, a critério de cada UF.

Se o parâmetro "**Utilizar Unidade de Controle do Estoque nos registros do ressarcimento do ICMS ST**" estiver marcado será utilizado o fator de Conversão entre a Unidade do Item do Lançamento e a Unidade de Controle do Produto para calcular o valor a ser gerado neste campo.

**Campo 08** (UNID) - Unidade de medida adotada para o controle de ressarcimento/restituição de ICMS ST.

Se o parâmetro "**Utilizar Unidade de Controle do Estoque nos registros do ressarcimento do ICMS ST**" estiver marcado, este campo será gerado com a Unidade de Controle do Produto. Caso contrário, será gerado com a Unidade do Item do Lançamento Fiscal.

**Campo 09** (VL\_UNIT\_CONV) – Valor unitário da mercadoria, considerando a unidade utilizada para informar o campo “QUANT\_CONV” (considerando descontos e acréscimos incondicionais aplicados sobre o valor bruto).

O campo será gerado com o Valor de Mercadoria do Item, retirados os Descontos e acrescidas as Despesas o Frete e o Seguro. Se o parâmetro "**Utilizar Unidade de Controle do Estoque nos registros do ressarcimento do ICMS ST**" estiver marcado será utilizado o fator de Conversão entre a Unidade do Item do Lançamento e a Unidade de Controle do Produto para calcular o valor a ser gerado neste campo.

**Campo 10** (VL\_UNIT\_ICMS\_NA\_OPERACAO\_CONV) – Valor correspondente à multiplicação da alíquota interna (incluindo FCP) da mercadoria pelo valor correspondente à operação de saída que seria tributada se não houvesse ST, considerando a unidade utilizada para informar o campo “QUANT\_CONV”, aplicando-se a mesma redução da base de cálculo do ICMS ST na tributação, se houver.

**Campo 11** (VL\_UNIT\_ICMS\_OP\_CONV) – Nos casos de direito a crédito do imposto pela não ocorrência do fato gerador presumido e desfazimento da ST, corresponde ao valor do ICMS da operação própria do sujeito passivo por substituição do qual a mercadoria tenha sido recebida diretamente ou o valor do ICMS que seria atribuído à operação própria do contribuinte substituído do qual a mercadoria tenha sido recebida, caso estivesse submetida ao regime comum de tributação, calculado conforme a legislação de cada UF, considerando unidade utilizada para informar o campo “QUANT\_CONV”.

Para as UFs em que a legislação estabelecer que o valor desse campo corresponderá ao mesmo valor expresso no campo 12 (VL\_UNIT\_ICMS\_OP\_ESTOQUE\_CONV), seu preenchimento será facultativo. O valor deste campo, quando obrigatório  
na UF, será utilizado para o cálculo do valor do ressarcimento/restituição do Campo 15 (VL\_UNIT\_ICMS\_ST\_CONV\_REST), conforme fórmula abaixo:

*Campo 12 (VL\_UNIT\_ICMS\_OP\_ESTOQUE\_CONV) + Campo 13 (VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV) - Campo 11 (VL\_UNIT\_ICMS\_OP\_CONV) = Campo 15 (VL\_UNIT\_ICMS\_ST\_CONV\_REST)*

**Campo 12** Valor médio unitário do ICMS que o contribuinte teria se creditado referente à operação de entrada das mercadorias em estoque caso estivesse submetida ao regime comum de tributação, calculado conforme a legislação de cada UF, considerando a unidade utilizada para informar o campo “QUANT\_CONV”.

Registro C185 - Exemplos

O período para o cálculo do valor médio deve atender à legislação de cada UF. Ex. diário, mensal etc. 

**Campo 13** (VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV) - Informar o valor médio unitário do ICMS ST, incluindo FCP ST, pago ou retido, das mercadorias em estoque. Quando a mercadoria estiver sujeita ao FCP adicionado ao ICMS ST, neste campo deve ser informado o valor médio unitário da parcela do ICMS ST + a parcela do FCP.

O período para o cálculo do valor médio deve atender à legislação de cada UF. Ex. diário, mensal etc.

**Campo 14** (VL\_UNIT\_FCP\_ICMS\_ST\_ESTOQUE\_CONV) - Informar o valor médio unitário da parcela do FCP adicionado ao ICMS que tenha sido informado no campo “VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV”.

**Campo 15** (VL\_UNIT\_ICMS\_ST\_CONV\_REST) – Salvo disposição em contrário de legislação de cada UF, o valor a ser ressarcido / restituído é calculado conforme as orientações a seguir.

a) Nos casos de direito ao crédito do imposto, por não ocorrência do fato gerador presumido:

a.1) Quando o campo 11 (VL\_UNIT\_ICMS\_OP\_CONV) for obrigatório, de acordo com a legislação da UF, correspondente ao seguinte cálculo, considerando a unidade utilizada para informar o campo “QUANT\_CONV”:

*Campo 12 (VL\_UNIT\_ICMS\_OP\_ESTOQUE\_CONV) + Campo 13 (VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV) - Campo 11 (VL\_UNIT\_ICMS\_OP\_CONV) = Campo 15 (VL\_UNIT\_ICMS\_ST\_CONV\_REST)*

a.2) Quando o campo 11(VL\_UNIT\_ICMS\_OP\_CONV) não for obrigatório, de acordo com a legislação da UF, corresponde ao valor no campo 13 (VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV)

b) Nos casos de direito ao crédito do imposto, calculada com base no valor de saída da mercadoria inferior ao valor da BC ICMS ST, informar o valor unitário de ICMS correspondente ao seguinte cálculo, considerando a unidade utilizada para informar o campo “QUANT\_CONV”:

*Campo 12 (VL\_UNIT\_ICMS\_OP\_ESTOQUE\_CONV) + Campo 13 (VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV) - Campo 10 (VL\_UNIT\_ICMS\_NA\_OPERACAO\_CONV) = Campo 15 (VL\_UNIT\_ICMS\_ST\_CONV\_REST)*

**Campo 16** (VL\_UNIT\_FCP\_ST\_CONV\_REST) – Informar o valor unitário do Fundo de Combate à Pobreza (FCP) vinculado à substituição tributária que compõe o campo “VL\_UNIT\_ICMS\_ST\_CONV\_REST”, considerando a unidade utilizada para informar o campo “QUANT\_CONV”, conforme previsão das legislações das UF.

**Campo 17** (VL\_UNIT\_ICMS\_ST\_CONV\_COMPL) – Nos casos de complemento, informar o valor unitário de ICMS correspondente ao cálculo a seguir. Salvo disposição em contrário de legislação de cada UF, o valor a ser ressarcido / restituído é calculado conforme as orientações a seguir

*Campo 10 (VL\_UNIT\_ICMS\_NA\_OPERACAO\_CONV) - Campo 12 (VL\_UNIT\_ICMS\_OP\_ESTOQUE\_CONV) - Campo 13 (VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV) = Campo 17 (VL\_UNIT\_ICMS\_ST\_CONV\_COMPL)*

**Campo 18** (VL\_UNIT\_FCP\_ST\_CONV\_COMPL) – Informar o valor unitário do Fundo de Combate à Pobreza (FCP) vinculado à substituição tributária que compõe o campo 17 “VL\_UNIT\_ICMS\_ST\_CONV\_COMPL”, considerando a unidade utilizada para informar o campo “QUANT\_CONV”, conforme previsão das legislações das UF.

C186C186

**Informações Complementares das Operações de Devolução de Entradas de Mercadorias Sujeitas à Substituição Tributária (Código 01,1B, 04 e 55).**

O Registro C186 é “filho” do registro C100 que é o próprio Documento Fiscal. Para gerar esse arquivo é necessário marcar o Parâmetro "**Gerar ressarcimento/complemento ICMS ST**" na tela de geração do SPED Fiscal.

Será preciso informar, também na tela de geração do SPED Fiscal, qual é o critério de informação da unidade para o Estado que está sendo gerado a rotina: se pela unidade do estoque (0200) ou pela unidade de comercialização (unidade informada nos Lançamentos Fiscais).

Atenção!

Todos os campos de valores deste registro serão gerados considerando essa unidade, utilizando o fator de conversão informado.

5.7 - Tabela de Código de Motivos de Restituição e Complementação de ICMS 

Os dois primeiros caracteres (UF) referem-se à unidade da federação do estabelecimento. O caractere seguinte (numérico) refere-se ao tipo do motivo, onde: 

4 - Devolução de entradas.

Serão selecionados os Lançamentos Fiscais que atendam às seguintes regras

* Lançamentos de Saída (Devolução de Compra);
* CFOP associado esteja marcado como Operação que controla ressarcimento/complemento do ST (DCFOP.OPERACAOSTCOMPRA)
* CFOP com o Tipo “Devolução” habilitado (DCFOP.TIPODEVOLUCAO)
* Produto estiver marcado como tributado pelo ICMS ST nos Dados Fiscais por UF, considerando a UF da Filial (TPRDCODFISCAL.TRIBUTADOICMSST)
* Exista Lançamento de Entrada referenciado
* Informações geradas baseado no Lançamento de Entrada referenciado (Registro C180).

Observação: Situação não deve gerar o Registro C185.

**Campo 02** (NUM\_ITEM) - Número sequencial do item no documento fiscal.

**Campo 03** (COD\_ITEM) - Código do item (campo 02 do Registro 0200).

**Campo 04** (CST\_ICMS) - Código da Situação Tributária referente ao ICMS no documento fiscal de saída

**Campo 05** (CFOP) - Código Fiscal de Operação e Prestação.

**Campo 06** (COD\_MOT\_REST\_COMPL) - Código do motivo da restituição ou complementação conforme Tabela 5.7.

**Campo 07** (QUANT\_CONV) - Quantidade do item.

**Campo 08** (UNID) - Unidade adotada para informar o campo QUANT\_CONV.

**Campo 09** (COD\_MOD\_ENTRADA) - Código do modelo do documento fiscal de saída, conforme a tabela indicada no item 4.1.1

**Campo 10** (SERIE\_ENTRADA) - Número de série do documento de entrada em papel.

**Campo 11** (NUM\_DOC\_ENTRADA) - Número do documento fiscal de entrada.

**Campo 12** (CHV\_DFE\_ENTRADA) - Chave do documento fiscal eletrônico de entrada.

**Campo 13** (CHV\_DFE\_ENTRADA) - Chave do documento fiscal eletrônico de entrada.

**Campo 14** (NUM\_ITEM\_ENTRADA) - Item do documento fiscal de entrada.

**Campo 15** (VL\_UNIT\_CONV\_ENTRADA) - Valor unitário líquido do item/produto (considerando descontos e acréscimos incondicionais aplicados sobre o valor bruto) considerando a unidade utilizada para informar o campo “QUANT\_CONV”, correspondente ao valor do campo VL\_UNIT\_CONV, preenchido na ocasião da entrada.

Será calculado pelo sistema utilizando o fator de conversão entre a unidade do lançamento e a unidade informada no campo "UNID", se for caso.

Atenção!Preencher corretamente o a Unidade Base no Cadastro da Unidade para correta conversão.

(DITEM.VALORMERC - DITEM.DESCONTOITEM + DITEM.VALORDESPESA +DITEM.VLRFRETE + DITEM.VALORSEGURO) / QUANT\_CONV)

**Campo 16** (VL\_UNIT\_ICMS\_OP\_CONV\_ENTRADA) - Valor unitário do ICMS operação própria que o informante teria direito ao crédito caso a mercadoria estivesse sob o regime comum de tributação, considerando unidade utilizada para informar o campo “QUANT\_CONV”. Correspondente ao valor do campo VL\_UNIT\_ICMS\_OP\_CONV, preenchido na ocasião da entrada

Corresponde

Nos casos em que a nota do fornecedor vier preenchida com CST 60 e CSOSN 500 (ICMS cobrado anteriormente por substituição tributária), o valor desse campo não corresponde ao valor preenchido no campo N26b (vICMSSubstituto), Valor  
do ICMS próprio do Substituto.

(DITEM.VLRICMSPRD / QUANT\_CONV)

**Campo 17** - (VL\_UNIT\_BC\_ICMS\_ST\_CONV\_ENTRADA) - Valor unitário da base de cálculo do imposto pago ou retido anteriormente por substituição, considerando a unidade utilizada para informar o campo “QUANT\_CONV”, aplicando-se redução, se houver.  Correspondente ao valor o campo VL\_UNIT\_BC\_ICMS\_ST\_CONV, preenchido na ocasião da entrada

(DITEM.BASEICMSSTPRD / QUANT\_CONV)

**Campo 18** - (VL\_UNIT\_ICMS\_ST\_CONV\_ENTRADA) - Preenchimento: Informar o valor unitário do ICMS ST pago ou retido limitado à parcela do ICMS ST correspondente ao fato gerador presumido que ainda não se realizou.  Correspondente ao valor do campo VL\_UNIT\_ICMS\_ST\_CONV, preenchido na ocasião da entrada.

Corresponde ao campo 07(VL\_UNIT\_BC\_ICMS\_ST \_CONV), aplicada a redução de base de cálculo se houver, multiplicada pela alíquota interna (com o adicional de FCP), estabelecida pela legislação da UF, subtraída do campo 06 (VL\_UNIT\_ICMS\_OP\_CONV).

( Campo 07 (VL\_UNIT\_BC\_ICMS\_ST \_CONV), com redução, conforme a legislação da UF \* alíq. interna (incluindo o adicional de FCP) ) - Campo 06 (VL\_UNIT\_ICMS\_OP\_CONV) = Campo 08 (VL\_UNIT\_ICMS\_ST\_CONV)

(DITEM.VLRICMSSTPRD / QUANT\_CONV)

**Campo 19** (VL\_UNIT\_FCP\_ST\_CONV\_ENTRADA) - Preenchimento: Informar o valor unitário do Fundo de Combate à Pobreza (FCP) vinculado à substituição tributária que compõe o campo “VL\_UNIT\_ICMS\_ST\_CONV”, considerando a unidade utilizada para informar o campo “QUANT\_CONV”, conforme previsão das legislações das UF.  Correspondente ao valor do campo VL\_UNIT\_FCP\_ST\_CONV, preenchido na ocasião da entrada.

(DITEM.VLRICMSITEMFCPESTDEST / QUANT\_CONV)

C190C190

**Registro Analítico do Documento (Código 01, 1B, 04, 55 e 65)**

Este registro tem por objetivo representar a escrituração dos documentos fiscais totalizados por CST, CFOP e Alíquota de ICMS.  
Este registro é um registro com dados consolidados do lançamento fiscal.

falseDesconto Condicional (Abatimento ICMS OU Despesa Condicional maiores que zero):

Quando houver desconto condicional no lançamento, e no lançamento houver um ou mais itens, o sistema realizará o seguinte cálculo:

false

**Valor Absoluto da Diferença =**

**(**

Valor da Mercadoria do lançamento

Frete do lançamento

Seguro do lançamento

Acréscimo do lançamento

Outros Acréscimos do lançamento

Descontos do lançamento

Outros Descontos do lançamento

Abatimento ICMS do lançamento

Despesa Condicional do lançamento

Valor IPI do lançamento

**)**

Valor Contábil do lançamento

Caso haja diferença no cálculo dos valores para mais ou para menos o Campo 05 do C190:

false

***VL\_OPR*** = **Valor Absoluto da Diferença**

* **Campo VL\_ICMS:**

Ao gerar o Registro C190 o campo 07 VL\_ICMS será preenchido caso o Tipo ICMS da natureza de Operação seja definido como Tributado ou Outros quando houver uma nota fiscal complementar.

Imagem

### ICMS Monofásico

* **Campo 04 (ALIQ\_ICMS):** Alíquota do ICMS  
  Itens com CST cujos dois últimos números sejam "02", "15" ou "53": o campo "ALIQ\_ICMS" será preenchido com o valor do campo "Alíquota Ad Rem".

* **Campo 06 (VL\_BC\_ICMS):** Valor da base de cálculo do ICMS  
  Itens com CST cujos dois últimos números sejam "02", "15", "53" ou "61": o campo "VL\_BC\_ICMS" será preenchido com o valor "0".

* **Campo 07 (VL\_ICMS):** Valor do ICMS  
  Para o CST "53", o campo "VL\_ICMS" será preenchido com o valor do campo "ICMS Próprio".

* **Campo 08 (VL\_BC\_ICMS\_ST):** Valor da base de cálculo do ICMS da substituição tributária  
  Itens com CST cujos dois últimos números sejam "02", "15", "53" ou "61": o campo "VL\_BC\_ICMS\_ST" será preenchido com o valor "0"
C191C191

**Informações do Fundo de Combate à Pobreza - FCP na NF-e (Código 55 e 65)**

Este registro presta informações do Fundo de Combate à Pobreza (FCP)  e veio com o objetivo de acompanhar a atualização de layout proposto pela versão 4.0 da NF-e que possui campo específico para informar os valores referentes ao Fundo de Combate a Pobreza (FCP), tanto para as operações próprias (FCP) quanto para as operações que envolvam substituição tributária (FCP ST).

Este registro foi incluído com a seguinte estrutura:

Um Registro para cada C190. Nível hierárquico 4.

**Observações Sobre o Preenchimento**

* **Campo 01 (REG): Valor Válido:**[C191].
* **Campo 02 (VL\_FCP\_OP): Preenchimento:**informar o valor total do Fundo de Combate à Pobreza (FCP) vinculado à operação própria, relativo aos itens com mesma combinação de CST\_ICMS, CFOP e alíquota do ICMS informada no registro pai, C190.

***Validação***:Só pode ser preenchido quando o campo CST\_ICMS do registro C190 assumir o valor x00,x10,x20,x51,x70 ou x90.

* **Campo 03 (VL\_FCP\_ST): Preenchimento:**informar o valor do Fundo de Combate à Pobreza (FCP) vinculado à operação de substituição tributária, relativo aos itens com mesma combinação de CST\_ICMS, CFOP e alíquota do ICMS informada no registro pai, C190.

***Validação***: Só pode ser preenchido quando o campo CST\_ICMS do registro C190 assumir o valor x10, x30, x70, x90, 201, 202, 203 ou 900.

* **Campo 04 (VL\_FCP\_RET): Preenchimento:**informar o valor do Fundo de Combate à Pobreza (FCP) retido anteriormente, relativo aos itens com mesma combinação de CST\_ICMS, CFOP e alíquota do ICMS informada no registro pai, C190.

***Validação***:Só pode ser preenchido quando o campo CST\_ICMS do registro C190 assumir o valor x60 ou 500.

***Observações***:

* A geração do Registro C191 está sujeita aos Modelos de Documento 55 e 65.
* Quando os valores do FECP Estado de Destino e o FECP Próprio estão zerados o Registro C191 não é gerado
* O cálculo do Registro é feito prioritariamente por Item, caso não exista Itens no Lançamento o cálculo é feito por Situação Tributária.
* A geração do Registro C191 acontecerá para Lançamentos feitos com o modelo de documento 55 será a partir de 2019.
* A geração do Registro C191 acontecerá para Lançamentos feitos com o modelo de documento 65 será a partir de 2020.
C195C195

**Observações do Lançamento Fiscal**

Este registro deve ser informado quando, em decorrência da legislação estadual, houver ajustes nos documentos fiscais, informações sobre diferencial de alíquota, antecipação de imposto e outras situações.  
Sempre que ocorrer um ajuste (lançamentos referentes aos impostos que têm o cálculo detalhado em Informações Complementares da NF; ou aos impostos que estão definidos na legislação e não constam na NF; ou aos recolhimentos antecipados dos impostos), deve, conforme dispuser a legislação estadual, ocorrer uma observação.

**Campos de Uso Livre  NF-e**

Também é possível gerar o  a partir dos Campos de Uso Livre.

Gerando a partir dos Campos de Uso Livre, o C110 irá pegar o Valor xTexto.

Mais informações na página do [Registro 0460](https://tdn.totvs.com/pages/viewpage.action?pageId=422546008#BLOCO0-0460).

C197C197

**Outras obrigações tributárias, ajustes e informações de Valores provenientes de documento fiscal**

Este registro tem por objetivo informar para detalhar outras obrigações tributárias, ajustes e informações de valores do documento fiscal do registro C195, que podem ou não alterar o cálculo do valor do imposto. Gerado atualmente se o código do ajustes tiver tamanho 10 e estiver marcado o parâmetro na tela da rotina "Gera C197".

Para atender o Início do conteúdo adicionado Fim do conteúdo adicionado [Lei 6.374/89, Art. 59 RICMS/2000-SP, conforme citado no artigo](http://www.praticacontabil.com/ricms_sp.htm) disponibilizado o parâmetro "ICMS Interestadual" e "ICMS Interno" na aba "Personalização" da Parametrização da Rotina do SPED Fiscal. Caso haja lançamento de entrada com destaque do Diferencial de Alíquota para filial do estado de São Paulo, será gerada duas linhas do registro C197 com o código de ajuste default da parametrização da rotina e com as seguintes descrição:

* Código de Ajuste SP40090207 Descrição: Entrada de mercadoria, oriunda de outro Estado, destinada a uso, consumo ou integração no ativo imobilizado ou utilização de serviço iniciado fora do território paulista - Diferencial de alíquota. Artigo 117, II do RICMS/00
* [Código de Ajuste SP10090718](http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal)Descrição: Entrada de mercadoria, oriunda de outro Estado, destinada a uso, consumo ou integração no ativo imobilizado, ou utilização de serviço iniciado noutro Estado - Diferencial de alíquota. Artigo 117, I do RICMS/00

Este registro é gerado a partir dos Lançamentos de Ajustes associados ao Lançamento Fiscal. Consulte a documentação: [Código de Ajuste associado na Natureza de Operação](https://tdn.totvs.com/pages/viewpage.action?pageId=448601553).

**IPI Não Tributado**

Para a correta geração deste registro deverão ser criados dois campos complementares no item do Lançamento Fiscal, com as características abaixo. Estes campos podem ser criados também no Lançamento. A informação deverá constar somente no item ou somente no lançamento, caso contrário, a informação será duplicada.

| Nome da Coluna | Descrição | Tamanho | Tipo |
| --- | --- | --- | --- |
| CODAJUSTESPEDIPI | Código Ajuste Sped IPI | 10 | Alfanumérico |
| DESCAJUSTESPEDIPI | Descrição do Ajuste Sped IPI | texto | - |

***Observação***: Caso o lançamento fiscal seja proveniente do TOTVS Gestão de Estoque, Compras e Faturamento, os campos complementares acima também deverão ser criados no movimento / item do Tipo de Movimento.

C300C300

**Resumo diário das notas fiscais de venda a consumidor ( Código 02)**

Este registro deve ser apresentado pelos contribuintes que utilizam notas fiscais de venda ao consumidor não emitidas por cupom fiscal. Trata-se de um resumo diário, por série e subsérie do documento fiscal, de todas as operações praticadas. Existirão tantos registros C300 quantos forem os agrupamentos de séries e subséries dos documentos fiscais emitidos no dia. Os valores de documentos fiscais cancelados não devem ser computados no valor total dos documentos (campo VL\_DOC).

C310C310

**Documentos cancelados de notas fiscais de venda a consumidor**

Este registro tem por objetivo informar os números dos documentos fiscais cancelados do modelo 02

C320C320

**Resumo analítico do resumo diário das notas Fiscais de venda a consumidor**

Este registro tem por objetivo informar a consolidação diária dos valores das notas fiscais de venda ao consumidor não emitidas por ECF e deve ser apresentado, de forma agrupada, pela combinação CST\_ICMS, CFOP e Alíquota de ICMS.

C321C321

**Itens do resumo diário dos documentos**

Este registro é o detalhamento, por itens de mercadoria, da consolidação diária dos valores das notas fiscais de venda ao consumidor não emitidas por ECF.

C350C350

**Nota fiscal de Venda a consumidor**

Este registro tem por objetivo informar os dados de todas as notas fiscais modelo 02 emitidas ao consumidor

C370C370

**Itens do documento**

Este registro é um detalhamento dos itens da nota fiscal modelo 02 informada no registro C350

C390C390

**Registro analítico das notas Fiscais de Venda a consumidor**

Este registro tem por objetivo informar a consolidação dos valores das notas fiscais de venda ao consumidor modelo 02 (presentes do registro C350) e deve ser apresentado, de forma agrupada, pela combinação CST\_ICMS, CFOP e Alíquota de ICMS.

C400C400

**Equipamento ECF**

Este registro tem por objetivo identificar os equipamentos de ECF, e deve ser informado por todos os contribuintes que utilizem tais equipamentos na emissão de documentos fiscais.

C405C405

**Redução Z - Modelos 02 e 02D**

Este registro deve ser apresentado com as informações da Redução Z de cada equipamento em funcionamento na data das operações de venda à qual se refere a redução. Inclui todos os documentos fiscais totalizados na Redução Z, inclusive as operações de venda realizadas durante o período de tolerância do Equipamento ECF.

C410C410

**Tributos PIS e COFINS totalizados no dia**

Este registro deve ser apresentado sempre que houver produtos totalizados na Redução Z que acarretem valores de PIS e COFINS a serem informados.

C420C420

**Totalizadores da Redução Z**

Este registro tem por objetivo discriminar os valores por código de totalizador da Redução Z.

C425C425

**Resumo de itens do movimento diário**

Este registro tem por objetivo identificar os produtos comercializados na data da movimentação relativa à Redução Z informada

C490C490

**Registro analítico do movimento diário**

Este registro tem por objetivo representar a escrituração dos documentos fiscais emitidos por ECF e totalizados pela combinação de CST, CFOP e Alíquota.

C495C495

**Resumo mensal de itens do ECF por estabelecimento**

Este registro deve ser apresentado pelo contribuinte domiciliado no estado da Bahia, resumindo todas as informações num único registro por item de mercadorias, não dispensando a apresentação do registro C400 e registros filhos .

C500C500

**Nota Fiscal/Conta de Energia Elétrica (Código 06), Nota Fiscal de Energia Eletrônica - NF3e (Código 66) e Nota Fiscal Consumo Fornecimento de Gás (Código 28)**

Este registro deve ser apresentado, nas operações de saída, pelos contribuintes do segmento de energia elétrica e não enquadrados no Convênio ICMS 115/03, pelos contribuintes do segmento de fornecimento de gás e, nas operações de entrada, por todos os contribuintes adquirentes.

A partir de janeiro de 2020, deve ser apresentado também pelos contribuintes que emitirem a NF3e (modelo 66), mesmo que obrigados ao Convênio 115/03.

**IMPORTANTE:** para documentos de entrada, os campos de valor de imposto, base de cálculo e alíquota só devem ser informados se o adquirente tiver direito à apropriação do crédito (enfoque do declarante).

Novos campos gerados em **2022** a partir da versão **12.1.32**:

Os campos serão gerados sem informações. 

Campos que não vão ser gerados a partir de **2022**:

C510C510

**Itens do documento de Nota fiscal/Conta de energia elétrica, Nota fiscal/Conta de fornecimento d'agua canalizada e nota fiscal de fornecimento de gás.**

C520C520

**Complemento do documento – Dados adicionais**

C590C590

**Registro analítico do documento – Nota Fiscal de energia elétrica, Nota Fiscal/Conta de Fornecimento d'água canalizada e Nota fiscal consumo fornecimento de gás**

Este registro representa a escrituração dos documentos fiscais dos modelos especificados no C500, totalizados pelo agrupamento das combinações dos valores de CST, CFOP e Alíquota dos itens de cada documento. Deve haver um registro C590 para cada combinação de valores de CST, CFOP e Alíquota que existir nos itens (registro C510), totalizando estes itens .

C591C591

**Informações do Fundo de Combate à Pobreza – FCP na NF3e (código 66)**

Este registro tem por objetivo prestar informações do Fundo de Combate à Pobreza (FCP), constante na NF3e. Os valores deste registro são meramente informativos e não são contabilizados na apuração dos registros no bloco E. A obrigatoriedade e forma de apresentação de cada campo deste registro deve ser verificada junto às unidades  
federativas.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem da Informação** | **Observação** |
| 01 | REG | Texto fixo contendo "C591” |  |  |
| 02 | VL\_FCP\_OP | Valor do Fundo de Combate à Pobreza (FCP) vinculado à operação própria, na combinação de CST\_ICMS, CFOP e alíquota do ICMS | Gerado com o valor do FECP do ICMS  Próprio do Lançamento Fiscal | Será gerado quando o campo CST\_ICMS do registro C590 assumir o valor x00 ou x20, com valor relativo aos itens com mesma combinação de CST\_ICMS, CFOP e alíquota do ICMS informada no registro pai, C590. |
| 03 | VL\_FCP\_ST | Valor do Fundo de Combate à Pobreza (FCP) vinculado à operação de substituição tributária, na combinação de CST\_ICMS, CFOP e alíquota do ICMS. | Gerado com o valor do FECP do ICMS  ST do Lançamento Fiscal | Será gerado quando o campo CST\_ICMS do registro C590 assumir o valor x10, com valor relativo aos itens com mesma combinação de CST\_ICMS, CFOP e alíquota do ICMS informada no registro pai, C590. |

Informações Adicionais

Este registro será gerado somente a partir de 2020

C595C595

**Observações do Lançamento Fiscal (códigos 06, 28, 29 e 66)**

Este registro deve ser informado quando, em decorrência da legislação estadual, houver ajustes nos documentos fiscais eletrônicos, informações sobre diferencial de alíquota, antecipação de imposto e outras situações. Estas informações equivalem às observações que são lançadas na coluna “Observações” dos Livros Fiscais previstos no Convênio SN/70 – SINIEF, art. 63, I a IV. Sempre que existir um ajuste (lançamentos referentes aos impostos que têm o cálculo detalhado em Informações Complementares da NF; ou aos impostos que estão definidos na legislação e não constam na NF; ou aos recolhimentos antecipados dos impostos), deve, conforme dispuser a legislação estadual, ocorrer uma observação

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem da Informação** |
| 01 | REG | Texto fixo contendo "C595” |  |
| 02 | COD\_OBS | Código da observação do lançamento fiscal (campo 02 do Registro 0460) | Referência o registro 0460. Deve conter o valor do campo 2 do registro 0460 para fazer relacionamento com o mesmo. |
| 03 | TXT\_COMPL | Descrição complementar do código de observação. | Referência o registro 0460. Deve conter o valor do campo 3 do registro 0460 para fazer relacionamento com o mesmo. |

Informações Adicionais

Este registro será gerado somente a partir de 2020

C597C597

**REGISTRO C597 - OUTRAS OBRIGAÇÕES TRIBUTÁRIAS, AJUSTES E INFORMAÇÕES DE VALORES PROVENIENTES DE DOCUMENTO FISCAL**

Incluído com o objetivo de promover ajuste junto a apuração para os documentos(Códigos 06, 28, 29 E 66), criado na mesma estrutura do Registro C197 que trabalha a partir do código de ajuste e seus 3º e 4º dígito para determinar a influência a crédito ou a débito junto a apuração.

Deve haver um Registro C595.

Informações Adicionais

Este registro será gerado somente a partir de 2020

C600C600

**Consolidação diária de notas fiscais/Contas de energia elétrica, Nota fiscal/conta de fornecimento d'agua canalizada e nota fiscal/conta de fornecimento de gás**

Este registro deve ser apresentado na consolidação diária de Notas Fiscais/Conta de Energia Elétrica (código 06 da Tabela Documentos Fiscais do ICMS), Notas Fiscais de Fornecimento D'Água (código 29 da Tabela Documentos Fiscais do ICMS) e Notas Fiscais/Conta de Fornecimento de Gás (código 28 da Tabela Documentos Fiscais do ICMS) para empresas não obrigadas ao Convênio ICMS 115/2003.

C610C610

**Itens dos documentos Consolidados de notas fiscais/Contas de energia elétrica, Nota fiscal/conta de fornecimento d'agua canalizada e nota fiscal/conta de fornecimento de gás**

Este registro tem por objetivo discriminar por item os registros consolidados apresentados no C600.

C690C690

**Registro analítico dos documentos (Notas Fiscais/Contas de Energia Elétrica (Código 06), Nota Fiscal/Conta de Fornecimento d´água CANALIZADA (código 29) e Nota Fiscal/Conta de Fornecimento de Gás (Código 28)**

Este registro tem por objetivo representar a escrituração dos documentos fiscais dos modelos especificados no C600, totalizados pelo agrupamento das combinações dos valores de CST, CFOP e Alíquota dos itens de cada registro consolidado.  
Existirá um registro C690 para cada combinação de valores de CST, CFOP e Alíquota que existir nos itens (registro C610), totalizando estes itens.

C700C700

**Consolidação dos Documentos NF/Conta Energia Elétrica (Cód 06), Emitidas em via Única (Empresas Obrigadas à entrega do arquivo previso no convênio 115/03) e Nota Fiscal/Conta de Fornecimento de Gás canalizado (Cód. 28)**

**Este registro não é gerado**

C790C790

**Registro Analítico dos Documentos (Cód. 06 e 28)**

**Este registro não é gerado**

C791C791

**Registro de Informações de ST por UF (Cód. 06)**

**Este registro não é gerado**

C800C800

**C800 - CUPOM FISCAL ELETRÔNICO - SAT (CF-E-SAT) (CODIGO 59)**

Para geração do C800 vão ser consideradas as notas fiscais de Saída com o modelo de documento 59.

**IMPORTANTE:** Este registro será gerado apenas para o ***Perfil - A*** (O perfil é definido na tela de geração da rotina). 

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem da Informação** |
| 01 | REG | Texto fixo contendo "C800” |  |
| 02 | COD\_MOD | Código do modelo do documento fiscal, conforme a tabela 4.1.1 | Gera com o Campo Código do Modelo do Documento - FTDO.CODMODDOC |
| 03 | COD\_SIT | Código da situação do documento fiscal, conforme a Tabela 4.1.2 | Status do lançamento fiscal. |
| 04 | NUM\_CFE | Número do Cupom Fiscal Eletrônico | Doc. Inicial DLAF.DOCINI |
| 05 | DT\_DOC | Data da emissão do Cupom Fiscal Eletrônico | Data de Emissão do lançamento fiscal - DLAF.DATAEMISSAO |
| 06 | VL\_CFE | Valor total do Cupom Fiscal Eletrônico | Gerado a Partir do valor contábil do lançamento fiscal - DLAFAGRUP.VALORCONT |
| 07 | VL\_PIS | Valor total do PIS | Gerado com o Valor de PIS do Item ou do Lançamento Fiscal - DTRBITEM.VALORTRB ou DTRBLAF.VALORTRB |
| 08 | VL\_COFINS | Valor total da COFINS | Gerado com o Valor de COFINS do Item ou do Lançamento Fiscal - DTRBITEM.VALORTRB ou DTRBLAF.VALORTRB |
| 09 | CNPJ\_CPF | CNPJ ou CPF do destinatário | Gerado com o Valor do campo CNPJ/CPF do Adquirente - DLAF.CNPJCPFADQUIRENTE (Campo não será gerado a partir de Janeiro de 2023) |
| 10 | NR\_SAT | Número de Série do equipamento SAT | Gerado com o Valor do campo Número de Série do equipamento SAT DLAF.NROSAT |
| 11 | CHV\_CFE | Chave do Cupom Fiscal Eletrônico | Gerado com o Valor do campo chave de acesso do lançamento fiscal - DLAF.CHAVEACESSONFE |
| 12 | VL\_DESC | Valor total de descontos | Gerado com o Valor total dos descontos do lançamento fiscal - DLAF.DESCONTOS |
| 13 | VL\_MERC | Valor total das mercadorias e serviços | Gerado com o Valor da mercadoria - DLAF.VALORMERC |
| 14 | VL\_OUT\_DA | Valor total de outras despesas acessórias e acréscimos | Gerado com o Valor total de despesas - valor de outros acréscimos + valor seguro + valor Frete |
| 15 | VL\_ICMS | Valor do ICMS | Gerado com o Valor ICMS do Lançamento Fiscal - DLAF.VALORICMS |
| 16 | VL\_PIS\_ST | Valor total do PIS retido por subst. trib. | Gerado com o Valor fixo = 0 |
| 17 | VL\_COFINS\_ST | Valor total da COFINS retido por subst. trib. | Gerado com o Valor fixo = 0 |

C850C850

**C850 - REGISTRO ANALÍTICO DO CF-E-SAT (CODIGO 59)**

Para geração do C850 vão ser consideradas as notas fiscais de Saída como modelo de documento 59.

**IMPORTANTE:** Este registro será gerado apenas para o ***Perfil - A*** (O perfil é definido na tela de geração da rotina). 

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem da Informação** |
| 01 | REG | Texto fixo contendo "C850” |  |
| 02 | CST\_ICMS | Código da Situação Tributária, conforme a Tabela indicada no item 4.3.1 | Gerado a partir do campo CST da regra de ICMS - DREGRAICMS.SITTRIBUTARIA |
| 03 | CFOP | Código Fiscal de Operação e Prestação do agrupamento de itens | Gerado com a CFOP do Lançamento Fiscal - DLAF.IDNAT |
| 04 | ALIQ\_ICMS | Alíquota do ICMS | Gerado com a Alíquota do Lançamento Fiscal - DLAF.ALIQICMS |
| 05 | VL\_OPR | “Valor total do CF-e” na combinação de CST\_ICMS, CFOP e alíquota do ICMS, correspondente ao somatório do valor líquido dos itens. | Gerado com o Valor Total da ST do Lançamento Fiscal - DLAF.VALORCONT |
| 06 | VL\_BC\_ICMS | Valor acumulado da base de cálculo do ICMS, referente à combinação de CST\_ICMS, CFOP, e alíquota do ICMS. | Gerado a Partir do Campo DLAF.BASEICMS |
| 07 | VL\_ICMS | Parcela correspondente ao “Valor do ICMS” referente à combinação de CST\_ICMS, CFOP e alíquota do ICMS. | Gerado com o Valor ICMS do Lançamento Fiscal - DLAF.VALORICMS |
| 08 | COD\_OBS | Código da observação do lançamento fiscal (campo 02 do registro 0460) | Gerado de acordo com o campo 02 do Registro 0460 |

C855C855

**REGISTRO C855: OBSERVAÇÕES DO LANÇAMENTO FISCAL (CÓDIGO 59)**

Para geração do C855 vão ser consideradas as observações informadas nas notas fiscais de Saída com modelo de documento 59.

* Este registro será gerado a partir do ano **2023.**
* Este registro será gerado apenas para o ***Perfil - A*** (O perfil é definido na tela de geração da rotina).
* O modelo de documento 59 não gera o registro 0450.
* Disponível a partir dos **Patchs 12.1.2205.165 | 12.1.2209.108**

O registro pode ser gerado a partir do campo Observação da Situação Tributária:

Imagem

Caso o lançamento tenha mais de uma Situação Tributária é considerada apenas a primeira.

E também será gerado a partir dos campos de uso Livre que possuam cadastro de "Informações Fiscais Adicionais vinculados" e este esteja parametrizado para geração do registro 0460:

Imagem

Deverá ser gerado nos registro C855 o texto preenchido no campo livre (xTexto) fazendo referência a mensagem do 0460.

No registro 0460, deverá ser gerado o código e descrição preenchidos no cadastro do campo Informações Fiscais Adicionais

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem da Informação** |
| **01** | **REG** | **Texto fixo contendo "C855”** |  |
| **02** | **COD\_OBS** | **Código da Situação Tributária, conforme a Tabela** **indicada no item 4.3.1** | Código da observação do lançamento fiscal, gerado sequencialmente para o campo Observação da Situação Tributária ou gerado com o código informado no cadastro dos Dados Adicionais.  DINFOFISCAISADICIONAIS.CODIGO |
| **03** | **TXT\_COMPL** | **Código Fiscal de Operação e Prestação do** **agrupamento de itens** | Descrição complementar do código de observação.  DNFECADCAMPOSLIVRES.VALORTEXTODEF |

C857C857

**REGISTRO C857: OUTRAS OBRIGAÇÕES TRIBUTÁRIAS, AJUSTES E INFORMAÇÕES DE  
VALORES PROVENIENTES DE DOCUMENTO FISCAL**

Esse registro é filho do Registro C800 tem por objetivo detalhar outras obrigações tributárias, ajustes e informações de valores do documento fiscal do registro C855, que podem ou não alterar o cálculo do valor do imposto.

* Este registro será gerado a partir do ano **2023.**
* Este registro será gerado apenas para o ***Perfil - A*** (O perfil é definido na tela de geração da rotina).
* Este registro será gerado apenas para registros C855 gerados a partir do campo Observação da Situação Tributária.

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem da Informação** |
| 01 | REG | Texto fixo contendo "C857” |  |
| 02 | COD\_AJ | Código do ajustes/benefício/incentivo, conforme tabela indicada no item 5.3 | Gerado com os Dados da Sub Pasta Ajuste Sped do Lançamento Fiscal – Código de Ajuste associado ao  DLAFAJUSTESPED.IDCODIGOAJUSTE |
| 03 | DESCR\_COMPL\_AJ | Descrição complementar do ajuste do documento fiscal | Gerado com os Dados da Sub Pasta Ajuste Sped do Lançamento Fiscal DLAFAJUSTESPED.DESCRICAOCOMPLEMENTAR |
| 04 | COD\_ITEM | Código do item (campo 02 do Registro 0200) | Se o ajuste for associado a um item, o campo vai receber o código do produto daquele item. Se associado a situação tributária, esse campo ficará vazio. |
| 05 | VL\_BC\_ICMS | Base de cálculo do ICMS ou do ICMS ST | Gerado com os Dados da Sub Pasta Ajuste Sped do Lançamento Fiscal DLAFAJUSTESPED.BASECALCULO |
| 06 | ALIQ\_ICMS | Alíquota do ICMS | Gerado com os Dados da Sub Pasta Ajuste Sped do Lançamento Fiscal DLAFAJUSTESPED.ALIQUOTA |
| 07 | VL\_ICMS | Valor do ICMS ou do ICMS ST | Gerado com os Dados da Sub Pasta Ajuste Sped do Lançamento Fiscal DLAFAJUSTESPED.VALORICMSICMSST |
| 08 | VL\_OUTROS | Outros valores | Gerado com os Dados da Sub Pasta Ajuste Sped do Lançamento Fiscal DLAFAJUSTESPED.OUTROSVALORES |

C860C860

**C860: IDENTIFICAÇÃO DO EQUIPAMENTO SAT-CF-E**

Para a Geração do Registro C860 serão consideradas as Notas Fiscais de Saída com modelo de documento 59.

**IMPORTANTE:** Este registro será gerado apenas para o ***Perfil - B*** (O perfil é definido na tela de geração da rotina). 

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem da Informação** |
| 01 | REG | Texto fixo contendo "C860” |  |
| 02 | COD\_MOD | Código do modelo do documento fiscal, conforme a tabela 4.1.1 | Gera com o Campo Código do Modelo do Documento - FTDO.CODMODDOC |
| 03 | NR\_SAT | Número de série do equipamento SAT | Gera com o Campo Número de Série do equipamento SAT - DLAF.NROSAT |
| 04 | DT\_DOC | Data de emissão dos documentos fiscais | Gera com o Campo do Lançamento Fiscal - DLAF.DATAEMISSAO |
| 05 | DOC\_INI | Número do documento inicial | Gera com o Campo Doc. Inicial do Lançamento Fiscal - DLAF.DOCINI |
| 06 | DOC\_FIM | Número do documento final | Gera com o Campo Doc. Inicial do Lançamento Fiscal - DLAF.DOCFIM |

C870C870

**ITENS DO RESUMO DIÁRIO DOS DOCUMENTOS (CF-E-SAT) (CÓDIGO 59)**

Este registro é filho do C860 (perfil B) e traz o detalhamento dos itens contidas no   
Resumo Diário Dos Documentos (Cf-E-Sat) (Código 59).

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem da Informação** |
| 01 | REG | Texto fixo contendo "C870” |  |
| 02 | COD\_ITEM | Código do item (campo 02 do Registro 0200) | Gerado com o Código do Produto TPRD.CODIGOPRD |
| 03 | QTD | Quantidade do item | Gerado com a Quantidade do Item do Lançamento Fiscal - DITEM.QTDEPRD |
| 04 | UNID | Unidade do item (Campo 02 do registro 0190) | Gerado com a Quantidade do Item do Lançamento Fiscal - DITEM.CODUND |
| 05 | CST\_ICMS | Código da Situação Tributária referente ao ICMS | Gerado com o ST do Item do Lançamento Fiscal - DITEM.CST |
| 06 | CFOP | Código Fiscal de Operação e Prestação | Gerar com a CFOP associada ao Lançamento Fiscal - DNATUREZA.CODNAT |

Informações Adicionais

* Quando a flag "Gerar ressarcimento/complemento ICMS ST" estiver marcada.
C890C890

**RESUMO DIÁRIO DO CF-E (CÓDIGO 59) POR EQUIPAMENTO SATCF-E**

O Registro C890 é gerado apenas quando o Registro C860 (Perfil B) também for gerado, e tem por objetivo identificar os equipamentos SAT-CF-e.

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem da Informação** |
| 01 | REG | Texto fixo contendo "C890” |  |
| 02 | CST\_ICMS | Código da Situação Tributária, conforme a Tabela indicada no item 4.3.1 | Gerado a partir do campo CST da regra de ICMS - DREGRAICMS.SITTRIBUTARIA |
| 03 | CFOP | Código Fiscal de Operação e Prestação do agrupamento de itens | Gerado com a CFOP do Lançamento Fiscal - DLAF.IDNAT |
| 04 | ALIQ\_ICMS | Alíquota do ICMS | Gerado com a Alíquota do Lançamento Fiscal - DLAF.ALIQICMS |
| F05 | VL\_OPR | “Valor total do CF-e” na combinação de CST\_ICMS, CFOP e ALÍQUOTA DO ICMS, correspondente ao somatório do valor líquido dos itens. | Gerado com o Valor Total da ST do Lançamento Fiscal - DLAF.VALORCONT |
| 06 | VL\_BC\_ICMS | Valor acumulado da base de cálculo do ICMS, referente à combinação de CST\_ICMS, CFOP e ALÍQUOTA DO ICMS. | Gerado com a Base ICMS do Lançamento Fiscal - DLAF.BASEICMS |
| 07 | VL\_ICMS | Parcela correspondente ao "Valor do ICMS" referente à combinação de CST\_ICMS, CFOP e alíquota do ICMS. | Gerado com o Valor ICMS do Lançamento Fiscal - DLAF.VALORICMS |
| 08 | COD\_OBS | Código da observação do lançamento fiscal (campo 02 do registro 0460) | não é gerado |

C895C895

**REGISTRO C895: OBSERVAÇÕES DO LANÇAMENTO FISCAL (CÓDIGO 59)**

Para geração do C895 vão ser consideradas as observações informadas nas notas fiscais de Saída com modelo de documento 59.

* Este registro será gerado a partir do ano **2023.**
* Este registro será gerado apenas para o ***Perfil - B*** (O perfil é definido na tela de geração da rotina).
* O modelo de documento 59 não gera o registro 0450.
* Disponível a partir dos **Patchs 12.1.2205.165 | 12.1.2209.108**

O registro pode ser gerado a partir do campo Observação da Situação Tributária:

Imagem

E também será gerado a partir dos campos de uso Livre que estiverem parametrizados para gerar o 0460:

Imagem

Deverá ser gerado nos registro C895 o texto preenchido no campo livre (xTexto) fazendo referência a mensagem do 0460.

No registro 0460, deverá ser gerado o código e descrição preenchidos no cadastro do campo Informações Fiscais Adicionais

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem da Informação** |
| **01** | **REG** | Texto fixo contendo "C895” |  |
| **02** | **COD\_OBS** | Código da Situação Tributária, conforme a Tabela indicada no item 4.3.1 | Código da observação do lançamento fiscal, gerado sequencialmente para o campo Observação da Situação Tributária ou gerado com o código informado no cadastro dos Dados Adicionais.  DINFOFISCAISADICIONAIS.CODIGO |
| **03** | **TXT\_COMPL** | Código Fiscal de Operação e Prestação do agrupamento de itens | Descrição complementar do código de observação.  DNFECADCAMPOSLIVRES.VALORTEXTODEF |

C897C897

**REGISTRO C897: OUTRAS OBRIGAÇÕES TRIBUTÁRIAS, AJUSTES E INFORMAÇÕES DE  
VALORES PROVENIENTES DE DOCUMENTO FISCAL**

Esse registro é filho do Registro C800 e tem por objetivo detalhar outras obrigações tributárias, ajustes e informações de valores do documento fiscal do registro C895, que podem ou não alterar o cálculo do valor do imposto. 

* Este registro será gerado a partir do ano **2023.**
* Este registro será gerado apenas para o ***Perfil - B*** (O perfil é definido na tela de geração da rotina).
* Este registro será gerado apenas para registros C895 gerados a partir do campo Observação da Situação Tributária.

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem da Informação** |
| 01 | REG | Texto fixo contendo "C897” |  |
| 02 | COD\_AJ | Código do ajustes/benefício/incentivo, conforme tabela indicada no item 5.3 | Gerado com os Dados da Sub Pasta Ajuste Sped do Lançamento Fiscal – Código de Ajuste associado ao  DLAFAJUSTESPED.IDCODIGOAJUSTE |
| 03 | DESCR\_COMPL\_AJ | Descrição complementar do ajuste do documento fiscal | Gerado com os Dados da Sub Pasta Ajuste Sped do Lançamento Fiscal DLAFAJUSTESPED.DESCRICAOCOMPLEMENTAR |
| 04 | COD\_ITEM | Código do item (campo 02 do Registro 0200) | Se o ajuste for associado a um item, o campo vai receber o código do produto daquele item. Se associado a situação tributária, esse campo ficará vazio. |
| 05 | VL\_BC\_ICMS | Base de cálculo do ICMS ou do ICMS ST | Gerado com os Dados da Sub Pasta Ajuste Sped do Lançamento Fiscal DLAFAJUSTESPED.BASECALCULO |
| 06 | ALIQ\_ICMS | Alíquota do ICMS | Gerado com os Dados da Sub Pasta Ajuste Sped do Lançamento Fiscal DLAFAJUSTESPED.ALIQUOTA |
| 07 | VL\_ICMS | Valor do ICMS ou do ICMS ST | Gerado com os Dados da Sub Pasta Ajuste Sped do Lançamento Fiscal DLAFAJUSTESPED.VALORICMSICMSST |
| 08 | VL\_OUTROS | Outros valores | Gerado com os Dados da Sub Pasta Ajuste Sped do Lançamento Fiscal DLAFAJUSTESPED.OUTROSVALORES |

#f5f5f5#feac0enoneVídeos

**Aprenda na prática com os nossos Vídeos:**

Base Legal

[Guia Prático da Escrituração Fiscal Digital - EFD ICMS/IPI da Receita Federal do Brasil](http://sped.rfb.gov.br/item/show/2761)
