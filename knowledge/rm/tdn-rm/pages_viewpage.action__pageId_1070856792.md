---
content_hash: 9a28ea3e0a74920d4c59ab7f4616367ff2d4e8123bc4ad61d7b0b306b86c3240
fetched_at: '2026-06-29T00:05:53.861256+00:00'
page_id: '1070856792'
product: rm
source: tdn-rm
title: Emissão de Nota de Débito e Crédito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1070856792
version: 89
---

![](https://tdn.totvs.com/download/attachments/1070856792/NF-e-Debito-Credito.png?version=1&modificationDate=1781549693873&api=v2)
]]>

# 1. Sobre

## **Nota Fiscal de Débito**

**Instituída pela Nota Técnica 2025.002 e alinhada às diretrizes da Reforma Tributária,** a **Nota Fiscal de Débito** tem a finalidade de registrar ajustes que resultem no aumento do débito de IBS/CBS já apurado pelo contribuinte, podendo, quando previsto na legislação, gerar o correspondente crédito de IBS/CBS para o destinatário.

**Tipos de Nota de Débito:**



## **Nota Fiscal de Crédito**

As notas fiscais de crédito têm por finalidade reduzir o débito de IBS na apuração do contribuinte emitente e, quando aplicável, gerar o correspondente lançamento a crédito na apuração do contribuinte destinatário. 

**Tipos de Nota de Débito:**



# 2. Parametrizações Gerais

ParametrizaçõesRegra do ICMS

**Essa parametrização é padrão para todas as Notas de Débito.**

Cadastros | Natureza Fiscal | Regra Tributária | Situação Tributária | Classificação Tributária | Vigência de Alíquota | CFOP Sem ICMS

Imagem

Período de Apuração para Todos os Tributos parametrizados no Tipo de Movimento.

Conexão NF-e

**Conexão NF-e**

Em Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Dados Fiscais | Parâmetros por Filial | <escolha a Filial que emitirá NF-e> | Conexão NF-e. Devem ser configurados os parâmetros **URL do Servidor TOTVS Service** e os **dados de Autenticação.**

ImagemDicas

Instalação do TSS: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/18590720143639>

Este passo deve ser configurado apenas quando a transmissão for realizada utilizando o TSS

Certificado Digital 1/2

**Certificado Digital**

Em Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Dados Fiscais | Parâmetros por Filial | <escolha a Filial que emitirá NF-e> | Certificado Digital 1/2. Deve ser configurado o certificado Digital para emissão da NF-e

ImagemDicas

Como preparar o certificado digital: [NFE0006\_Preparar\_Certificado\_Digital](https://tdn.totvs.com/display/LRM/NFE0006_Preparar_Certificado_Digital)

Cadastro do certificado digital:

Este passo deve ser configurado apenas quando a transmissão for realizada utilizando o TSS

# 3. Tipos de Nota de Débito

Eventos01 = Transferência de créditos para Cooperativas

transfCreditosEm Desenvolvimento

02 = Anulação de Crédito por Saídas Imunes/Isentas

anulacaoCreditoEm Desenvolvimento

03 - Débitos de notas fiscais não processadas na apuração

debitosNotasEm Desenvolvimento

04=Multa e juros

multasJurosInstituída pela **Nota Técnica 2025.002-RTC** e alinhada às diretrizes da Reforma Tributária , a Nota de com **Finalidade de Emissão (Finalidade 6)** e com **Tipo de Nota de Débito (Tipo 04)** tem a finalidade de registrar ajustes que resultem no aumento do débito de IBS/CBS já apurado pelo contribuinte.

## **O que é a Nota de Debito com finalidade "Multa e Juros"?**

Pense na seguinte situação cotidiana: você realizou uma venda, emitiu a nota fiscal, mas o cliente atrasou o pagamento do boleto. Por causa desse atraso, você precisou cobrar um valor adicional correspondente a multa e juros.

Antes da Reforma Tributária, essa diferença financeira costumava ser ajustada muitas vezes apenas internamente, no sistema financeiro ou por meio de lançamentos contábeis manuais. Agora, sob o rigor do novo modelo do **IVA Dual (IBS e CBS)**, a regra mudou drasticamente: **todo acréscimo ou redução na base de impostos exige um documento fiscal eletrônico que comprove a operação de forma rastreável.**

A **Nota de Débito** é um documento fiscal de ajuste. Ela serve para "avisar" a Receita e a SEFAZ que você recebeu um valor financeiro a mais derivado daquela nota original e que, por consequência, o seu débito tributário (o imposto que você tem a pagar) aumentou.

## **Por que emitir essa nota?**

Com as regras de transição e adequação para o IBS e a CBS, a emissão desta nota deixou de ser uma mera organização administrativa e passou a ser o único caminho de conformidade fiscal: 

* **Composição da Base de Cálculo:** Os juros e multas por atraso integram o valor total da operação e sofrem a incidência proporcional de IBS e CBS.
* **Fim dos Ajustes Manuais:** O Fisco exige que qualquer alteração ou acréscimo no saldo devedor do imposto seja realizado via documento fiscal, extinguindo os lançamentos manuais na apuração.
* **Direito ao Crédito:** A emissão permite que o cliente (destinatário), quando elegível, aproprie regularmente o crédito tributário correspondente a esse acréscimo pago.
* **Regularidade Fiscal:** Evita a omissão de receitas na malha fina fiscal, uma vez que a SEFAZ cruza as informações financeiras de recebimento com os documentos fiscais emitidos.

## **Estrutura Fiscal do XML**

**1. Cabeçalho e Identificação da Nota**

Estas tags definem o que é o documento e a sua natureza perante a SEFAZ:

* **tpNF** **= 1 (Saída):** Como a nota registra um *aumento* no imposto devido por você, a operação deve ser classificada como saída.
* **finNFe** **= 6 (Nota de Débito):** Identifica a finalidade geral do documento eletrônico.
* **tpNFDebito** **= 04 (Multa e Juros):** Especifica qual é o motivo exato desse débito.

**2. Grupo de Referenciamento (DFeReferenciado)**

Como a multa e o juro nascem de uma operação anterior atrasada, é estritamente obrigatório referenciar a origem no XML:

* **chaveAcesso****:** A chave de acesso de 44 dígitos da NF-e (Modelo 55) original.
* **nItem**: O número sequencial do item da nota original sobre o qual a multa ou o juro está sendo cobrado.

xmlExemplo XML: Nota Fiscal de Débito (04 - Multa e Juros)true



35
12345678
Multa e Juros Moratorios
55
1
2
2026-06-15T10:00:00-03:00
1 1
3550308
1
1
0
2
6 04 0
RM\_Fis\_v12.1.2502


CFOP9999
SEM GTIN
Acrescimo Financeiro Referente a Multa e Juros Moratorios
00000000
5949
UN
1.0000
150.0000
150.00
SEM GTIN
UN
1.0000
150.0000
1

35260612345678901234550010000000011234567890
1


000
150.00
10.0000
15.00

000
150.00
8.8000
13.20
]]>

**Guia de Parametrização do Tipo de Movimento**

Para que o sistema gere o XML corretamente, acesse a **Parametrização de Tipos de Movimento** na linha RM e realize as seguintes configurações obrigatórias:

Parâmetros do MovimentofalsefalseParametrizações Tipo MovimentoEtapa 2 - Mov - Emitente/Destinatário

preencha com:

* **Emitente:** Empresa (Própria Filial)
* **Destinatário:** Empresa

ImagemEtapa 6 - Mov - Outros Dados

Para garantir a rastreabilidade da operação que originou a multa/juros, é necessário vincular o documento original:

* Marque a opção **Usar Cópia de Movimentos por referência**.
* No campo **Motivo de Referência**, informe o código **38 - Nota de Débito - Multa e Juros**.

ImagemEtapa 68 - Fis - Tributação Item

### Os impostos legados (como ICMS, IPI, PIS e COFINS) **não devem** ser parametrizados ou incluídos de forma alguma neste tipo de movimento.

A nota deve conter **estritamente o IBS e CBS** (e Imposto Seletivo, se houver)

ImagemEtapa 70 - Fis - NF-e

### Esta parametrização é o coração do documento, pois define as *tags* exatas que serão levadas ao XML enviado à Sefaz/Governo:

* **Finalidade de Emissão (tag `finNFe`):** Deve ser preenchida com o valor **6 - Nota de Débito**.
* **Tipo de Nota de Débito (tag `tpNFDebito`):** Deve ser especificado como **4 - Multa e Juros**.
* No sistema, dentro do quadro "Nota Débito/Crédito", os campos devem refletir exatamente essa configuração (Finalidade: Débito / Tipo: Multa e juros).

Imagem05=Transferência de crédito na sucessão

transfCreditoSucessaoEm Desenvolvimento

pagAntecipado06 = Pagamento antecipado

pagAntecipadoA emissão da **Nota Fiscal de Débito (Finalidade 6)** com o **Tipo de Nota de Débito 06 (Pagamento Antecipado)** faz parte das regras da Reforma Tributária (conforme a Nota Técnica 2025.002-RTC e a Lei Complementar nº 214/2025).

Essa nota foi criada porque o fato gerador do **IBS** e da **CBS** ocorre no momento em que você recebe o dinheiro, mesmo que a mercadoria ou serviço só seja entregue no futuro. O objetivo é destacar e recolher o imposto no mês do recebimento do adiantamento.

* **Finalidade de Emissão (****finNFe****):** Selecione a opção **6** **- Nota de Débito**.
* **Tipo de Nota de Débito (****tpNFDebito****):** Selecione a opção **06** **- Pagamento Antecipado**.
* **Estoque:** Marque a opção para **Não atualizar estoque**. (Como a mercadoria ainda não saiu, essa nota é meramente financeira/fiscal).

## **O Fluxo Completo Da Antecipação à Entrega**

Para não pagar imposto em duplicidade, o processo deve seguir duas etapas claras:

### **Passo 1: O Recebimento (Emissão da Nota de Débito)**

O cliente faz o adiantamento. Você emite a **Nota de Débito (Tipo 06)** sobre o valor recebido. O imposto (IBS/CBS) entra na sua apuração do mês atual.

### **Passo 2: A Entrega Final (Emissão da NF-e Normal)**

Quando a mercadoria for efetivamente enviada ou o serviço concluído, você emitirá uma **NF-e Normal (Finalidade 1)** com o CFOP de remessa/venda.

Deve ser parametrizado no movimento a opção de vincular o Lançamento Financeiro de Adiantamento.

link da documentação - <https://tdn.totvs.com/display/public/LRM/Controle+de+Adiantamento>

**No XML da NF-e Normal:** Seu sistema deverá gerar o grupo de notas de antecipação de pagamento (gPagAntecipado) e preencher a tag **refNFe** informando a **chave de acesso da Nota de Débito** emitida no Passo 1.

**Observação: Compensação:** Isso serve para abater o imposto que você já pagou antecipadamente, garantindo que você só recolha a diferença sobre o saldo restante na nota final.

## **Guia de Parametrização do Tipo de Movimento**

Acesse o menu de **Parametrização de Tipos de Movimento** da linha RM e realize as seguintes configurações:

### **1. Etapa 2 - Movimento - Emitente e Destinatário**

* **Emitente:** Empresa (Própria Filial)
* **Destinatário:** Empresa

Imagem

### **2. Estoque e Financeiro**

* **Estoque:** Configurar para **Não atualizar estoque**.

### **3. Etapa 67 - Fiscal - Tributação - Item**

Configure a matriz de tributos para a Reforma Tributária. **Atenção:** Não inclua os impostos legados (ICMS, IPI, PIS, COFINS).

|  |  |
| --- | --- |
| Tributo | Configuração / Tributo Base |
| CBS | Parametrização Normal de acordo com a alíquota federal |
| IBS MUN | Utilizar o Tributo Base igual a IBS Consolidado |
| IBS UF | Utilizar o Tributo Base igual a IBS Consolidado |

Observação: Conforme a legislação vigente, o XML deve conter estritamente as tags de IBS, CBS e Imposto Seletivo (se houver). Os impostos antigos (como ICMS, IPI, PIS e COFINS) **não devem** ser parametrizados neste tipo de movimento.

Imagem

### **4. Etapa 70 - Fiscal - Nota Fiscal Eletrônica**

* **Finalidade de Emissão (finNFe):** 6 - Nota de Débito
* **Tipo de Nota de Débito (tpNFDebito):** 06 - Pagamento Antecipado

## **Processo de Inclusão do Movimento (Operacional)**

Ao realizar a inclusão manual ou via integração do movimento de Nota de Débito, atente-se ao preenchimento dos seguintes campos nas principais telas:

### **Tela Movimento - Identificação**

Garanta a seleção correta da filial emitente e Filial Destinatária que realizou a transferência..

Imagem

Item do Movimento

Diferente do modelo antigo, em que os adiantamentos não geram nota com destaque de imposto de forma imediata, agora as regras são estritas:

* **Detalhamento dos Itens:** Você deve selecionar o produto ou serviço exato que será entregue no futuro. O fisco exige que você já saiba o que está sendo vendido para aplicar a alíquota correta.

* **Valor do Item:** Informe o valor proporcional ao adiantamento recebido. Se o cliente pagou R$ 100,00 de sinal por um produto de R$ 500,00, o valor total desta Nota de Débito será **R$ 100,00**
* Imagem

  **Tela Item do Movimento - Integração - Dados Fiscais**
* Imagem

  **Tela Item do Movimento - Tributos e Valores - Tributos**
* Imagem

  ## **Resultado Esperado**

  Após a emissão da Nota de Débito Tipo 06:

  + O IBS e o CBS serão apurados no período do recebimento do adiantamento;
  + Não haverá movimentação de estoque;
  + O documento servirá de base para compensação futura na NF-e de venda final.

  Após a emissão da NF-e final:

  + O grupo gPagAntecipado será gerado no XML;
  + O imposto já recolhido antecipadamente será compensado automaticamente;
  + Evita-se recolhimento duplicado de IBS e CBS.
07 = Perda em estoque

perdaEstoque

Instituída pela Nota Técnica 2025.002 e alinhada às diretrizes da Reforma Tributária, a **Nota Fiscal de Débito – Tipo 07 (Perda de Estoque)** deve ser gerada quando o fechamento de inventário aponta divergências negativas na quantidade de produtos.

A finalidade deste documento é realizar o **estorno de créditos**, via apuração assistida, referentes à aquisição de bens que foram baixados por motivo de perda. Vale destacar que essa nota de débito possui aplicação exclusiva para a **CBS e o IBS**, portanto, **não substitui** a NF-e de baixa para fins de ICMS (CFOP 5927), que deve continuar sendo emitida normalmente.

+ **Finalidade de Emissão (finNFe):** Selecione a opção **6 - Nota de Débito**.
+ **Tipo de Nota de Débito (tpNFDebito):** Selecione a opção **07 - Perda em estoque**

* **CST 410**

* **Classificação Tributária (****cClassTrib****)** **410030** Estorno de crédito por perecimento, deterioração, roubo, furto ou extravio.

A legislação tributária exige o estorno proporcional dos créditos apropriados originalmente na compra. 

**Passo a Passo Geral**

1. Identifique a perda: No fechamento do inventário, separe as quantidades baixadas indevidamente por avaria, roubo ou deterioração.
2. Localize as notas originais: Tenha em mãos as chaves de acesso das notas de compra das mercadorias que foram perdidas.
3. Emita a NF-e  preencha os campos obrigatórios com o CFOP 5.927, selecione o grupo de estorno de créditos correspondente e valide a emissão.

Observação:   
Caso o bem perdido tenha sido adquirido de terceiros, deverá ser referenciado na nota fiscal de débito:

* O documento fiscal referente à aquisição do bem;
* O documento fiscal referente aos serviços vinculados à aquisição do bem.

## **Parametrização Tipo de Movimento**

**1 - Etapa 2 - Movimento  - Emitente e Destinatário**

Emitente - Empresa (Própria Filial)

Destinatário - Empresa (Própria Filial)

Imagem

**2 - Etapa 67 - Fiscal  - Tributação - Item**

Tributo CBS

Tributo IBS MUN - deve utilizar o Tributo Base igual a IBS Consolidado

Tributo IBS UF - deve utilizar o Tributo Base igual a IBS Consolidado

**Observação:** Como no **XML d**evem ser informadas **apenas as tags de IBS e CBS** (e Imposto Seletivo, se houver). Conforme a legislação atual, **não** devem ser incluídos os grupos de impostos antigos (como ICMS, IPI, PIS e COFINS), estes impostos não devem ser parametrizados.

Imagem

**3 - Etapa 69 - Fiscal - Nota Fiscal Eletrônica**

Referência Documento

Nota de Débito

Tipo ‘Perda em Estoque’

Imagem

## **Processo de Inclusão do Movimento (Operacional)**

Ao realizar a inclusão manual ou via integração do movimento de Nota de Débito, atente-se ao preenchimento dos seguintes campos nas principais telas:

### **Tela Movimento - Identificação**

Garanta a seleção correta da filial emitente e Filial Destinatária

Imagem

**Tela Movimento - Integração - Dados Fiscais**

Imagem

**Tela Movimento - Integração - Referência Doc**

Devem ser referenciados os documentos fiscais da aquisição original dos produtos perdidos.

Imagem

**Tela Item do Movimento - Tributos  e Valores - Tributo**

Imagem

1 - Grupo Estorno de Crédito - <gEstornoCred>

Este grupo de ser gerado considerando as informações dos tributos informado no Item do Movimento grupo

Issue - <https://jiraproducao.totvs.com.br/browse/DMOTORFISCALRM-748>

2 - Esta Nota deve ser gerada a partir da NF-e de Compra (Aquisição) para automatizar este processo é necessário criar uma cópia por referência.

08 = Desenquadramento do SN

desenquadramentoEm Desenvolvimento

# 3. Tipos de Nota de Crédito

Eventos01 = Multa e juros

multaejurossEm Desenvolvimento

02 = Apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM

apropriacaoCreditoEm Desenvolvimento

03 = Retorno por recusa total na entrega ou por não localização do destinatário na tentativa de entrega

retornoPorRecusa

Deve ser utilizada quando a entrega de um bem material não se concretizar por recusa total do cliente ou por não localização do destinatário. 

Neste processo, o emitente emite a nota para realizar o desfazimento automático do débito destacado na nota original, resolvendo a falta de sincronia entre o fato gerador da circulação e o da entrega efetiva.

Finalidade (finNFe): Código **5 = Nota de crédito**.

Tipo de Nota de Crédito (tpNFCredito): Código **03 = Retorno por Recusa na Entrega ou Por Não Localização do Destinatário na Tentativa de Entrega.**

Natureza da Operação (natOp): Preencher com o texto "Retorno por Recusa ou não localização".

Chave de Acesso Referenciada (refNFe): Informar a chave de acesso da nota fiscal de saída original.

Destinatário: As informações devem ser as mesmas da nota fiscal de saída original.

## Guia de Parametrização do Tipo de Movimento

Acesse o menu de **Parametrização de Tipos de Movimento** da linha RM e realize as seguintes configurações:

1. Etapa 2 - Movimento - Emitente e Destinatário

* **Emitente:** Empresa (Própria Filial)
* **Destinatário:** Empresa

Imagem

### **2. Etapa 6 - Movimento - Outros Dados**

* Usar Cópia de Movimentos por Referência
* Motivo de Referência igual 30 **Devolução por Recusa**

Imagem

### **3. Etapa 63 - Fiscal - Natureza Fiscal**

* Editar cliente\Fornecedor Origem\Destino

Imagem

### **4. Etapa 67 - Fiscal - Tributação - Item**

Configure a matriz de tributos para a Reforma Tributária. **Atenção:** Não inclua os impostos legados (ICMS, IPI, PIS, COFINS).

|  |  |
| --- | --- |
| Tributo | Configuração / Tributo Base |
| CBS | Parametrização Normal de acordo com a alíquota federal |
| IBS MUN | Utilizar o Tributo Base igual a IBS Consolidado |
| IBS UF | Utilizar o Tributo Base igual a IBS Consolidado |

Observação: Conforme a legislação vigente, o XML deve conter estritamente as tags de IBS, CBS e Imposto Seletivo (se houver). Os impostos antigos (como ICMS, IPI, PIS e COFINS) **não devem** ser parametrizados neste tipo de movimento.

Imagem

### **5. Etapa 69 - Fiscal - Nota Fiscal Eletrônica**

* **Finalidade de Emissão (finNFe):** 6 - Nota de Débito
* **Tipo de Nota de Crédito (tpNFCredito):** 03 - Retorno por recusa total na entrega ou por não localização do destinatário na tentativa de entrega
* Habilitar o Campo Referência Documentos

Imagem

## **Processo de Inclusão do Movimento (Operacional)**

A inclusão do movimento poderá ser realizada:

* Manualmente;
* Por meio do Assistente de Cópia por Referência.

Recomenda-se a utilização do Assistente de Cópia por Referência, pois os dados da nota fiscal original serão replicados automaticamente.

**Tela - Movimento - Processo**

Selecionar: **Assistente de Cópia por Referência**

Ao utilizar esse processo, o movimento será criado automaticamente com base na NF-e de saída recusada.

Imagem

### **Tela: Movimento - Identificação**

Garanta a seleção correta da filial emitente e Filial Destinatária a própria Filial

Imagem

### **Tela: Movimento - Integrações - Fiscal  - Documentos Fiscais Eletrônicos**

O Campo Cliente\Fornecedor deve esta preenchido com o cliente da Nota de Saída

Imagem

### **Tela: Movimento - Integrações - Fiscais - Referência Docs**

Deve ser informado as NF-e de Saída que foi recusada

Imagem

**Tela: Item do Movimento - Item**

Imagem

**Tela: Item do Movimento - Integrações Fiscal**

Imagem

**Tela: Item do Movimento - Tributos e Valores**

Imagem

## Resultado Esperado

Após a emissão e autorização da NF-e:

* Será gerada uma Nota de Crédito com Finalidade igual a 5;
* O XML conterá o Tipo de Nota de Crédito 03;
* A NF-e original será referenciada através da tag refNFe;
* Os débitos de IBS e CBS destacados na operação de saída original serão desfeitos automaticamente na apuração assistida da Reforma Tributária;
* A operação ficará regularizada perante o Fisco em razão da não concretização da entrega da mercadoria.
04 = Redução de valores

reducaoValoress**O que é a Nota de Crédito com finalidade "Redução de valores"?**

A Nota de Crédito do tipo 04 - Redução de Valores é um documento fiscal de ajuste. Ela serve especificamente para diminuir o valor da operação ou o valor do imposto (IBS e CBS) de uma nota fiscal de saída original que já foi autorizada e cujo prazo legal de cancelamento já tenha expirado.

## **Por que emitir essa nota?**

A emissão é essencial para manter a sua conformidade fiscal e garantir a correta apuração dos novos tributos (IBS e CBS) quando ocorrem falhas ou imprevistos após a emissão da nota. Você deve emiti-la nos seguintes cenários do dia a dia:

* **Erros de Preço ou Imposto:** Quando houver o destaque de tributos em valor superior ao devido ou erro na composição do valor da operação.
* **Entrega Parcial:** Quando o seu cliente recebe uma quantidade menor do que a que foi originalmente faturada na nota fiscal.
* **Ajustes Diversos:** Quaisquer ajustes de valores que precisem ser feitos após a NF-e já estar autorizada pela Sefaz.

## **Estrutura Fiscal do XML**

**1. Cabeçalho e Identificação da Nota**

Estas *tags* definem a lógica e o propósito do documento perante a SEFAZ:

* **<tpNF>** **= 0 (Entrada):** Como o documento anula ou reduz um imposto que você já havia destacado na saída, a operação no XML deve ser obrigatoriamente de **Entrada**.
* **<finNFe>** **= 5 (Nota de Crédito):** Indica a finalidade geral do documento.
* **<tpNFCredito>** **= 04 (Redução de valores):** Define o motivo específico do crédito.

**2. Grupo de Documento Referenciado (<NFref>)**

Indispensável para que o Fisco saiba qual operação está sendo corrigida:

* **<refNFe>****:** Chave de acesso de 44 dígitos da **NF-e original (Modelo 55)** que receberá o abatimento de valor ou quantidade.

xmlExemplo XML: Nota Fiscal de Crédito (04 - Redução de Valores)true



35
87654321
Credito por Reducao de Valores da Operacao
55
1
3
2026-05-29T14:30:00-03:00
0 1
3550308
1
1
0
2
5 04 0
RM\_Fis\_v12.1.2502

35260512345678901234550010000000011234567890


CFOP9998
SEM GTIN
Credito de Ajuste por Reducao de Valor de Operacao Anterior
00000000
2949
UN
1.0000
500.0000
500.00
SEM GTIN
UN
1.0000
500.0000
1


410 500.00
10.0000
50.00

410
500.00
8.8000
44.00

Nota Fiscal de Credito emitida para regularizacao de valores de IBS e CBS destacados a maior na NFe de referencia, chave de acesso 35260512345678901234550010000000011234567890, devido a erro formal de digitacao.
]]>

## **Guia de Parametrização do Tipo de Movimento**

Parâmetros do MovimentofalsefalseParametrizações Tipo MovimentoEtapa 2 - Mov - Emitente/Destinatáriopreencha com:  

* **Emitente**: Empresa (Própria Filial)
* **Destinatário**: Empresa

ImagemEtapa 6 - Mov - Outros Dados

Para garantir a rastreabilidade da operação que originou a multa/juros, é necessário vincular o documento original:

* Habilitar o campo **Usar Cópia de Movimentos por referência** e preencher com o motivo **27 - NF Complementar com Cópia de Itens**.

ImagemEtapa 63 - Fis - Natureza de Operação

Caso exista a necessidade de emissão para Cliente/Fornecedor Pessoa Física Não Contribuinte, habilite o parâmetro **Edita Cliente/Fornecedor Origem/Destino**.

ImagemEtapa 68 - Fis - Tributação Item

Os impostos legados (como ICMS, IPI, PIS e COFINS) **não devem** ser parametrizados ou incluídos de forma alguma neste tipo de movimento.

A nota deve conter **estritamente o IBS e CBS** (e Imposto Seletivo, se houver)

ImagemEtapa 70 - Fis - NF-e

Esta parametrização é o coração do documento, pois define as *tags* exatas que serão levadas ao XML enviado à Sefaz/Governo:

* **Finalidade de Emissão:** 5 - Nota de Crédito.
* **Tipo de Nota de Crédito:** 04 - Redução de valores.
* Marque o parâmetro **Referência Documentos**.

Imagem

## **Processo de Inclusão do Movimento (Operacional)**

Vá em **Movimento > Processo** e escolha a opção Assistente de Cópia por Referência. O sistema copiará os itens da nota fiscal original automaticamente.

Imagem

Nas abas de **Integração Fiscal > Referência Docs**, você deve referenciar a nota original. Para que a tag refNFe seja gerada corretamente no XML, informe a chave de acesso da nota original que sofrerá a redução ou busque-a pela rotina de referência.

Imagem05=Transferência de crédito na sucessão

transfCreditoSucessaooEm Desenvolvimento

06 = Retorno por recusa parcial na entrega

retornoPorRecusaParcialEm Desenvolvimento

Imagens
