---
article_id: 360010170492
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 238073ef3a588caee958bb499af6b90f711796f99f9e2a67276c157d85dfcaa5
fetched_at: '2026-06-28T22:42:03.690878+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - TOTVS BackOffice Linha Protheus - Arq. Magnéticos - SPED
  FISCAL - REGISTRO C190, C195 e C197
type: support-article
updated_at: '2025-06-18T18:05:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010170492-Cross-Segmentos-TOTVS-BackOffice-Linha-Protheus-Arq-Magn%C3%A9ticos-SPED-FISCAL-REGISTRO-C190-C195-e-C197
---

#### 

**Dúvida**

Como gerar os registros C190, C195 e C197 do Sped Fiscal?

**Ambiente**

Protheus - Livros Fiscais - a partir de 12.1.17

**Solução**

#### **REGISTRO C190: REGISTRO ANALÍTICO DO DOCUMENTO (CÓDIGO 01, 1B, 04, 55 e 65)**

Este registro é gerado a partir do Livro Fiscal e é composto de notas fiscais dos seguintes modelos:

* Nota Fiscal Modelo 1 ou 1-A – Espécie “NF ou NFE”.
* Nota Fiscal Avulsa, Modelo 1B - Espécie ="NFA".
* Nota Fiscal de Produtor, Modelo 4 - Espécie="NFP".
* Nota Fiscal Eletrônica, Modelo 55 – Espécie “SPED”.
* Nota Fiscal Eletrônica ao Consumidor Final, Modelo 65 - Espécie="NFCE".

#### **REGISTRO C195: Observações do Lançamento Fiscal (Código 01, 1B, 04 e 55)**

Este registro é gerado a partir do livro fiscal, fazendo o relacionamento do documento com a observação lançada no**registro 0460**, quando o documento tiver algum lançamento de Apuração ou quando tiver as informações lançadas na coluna **Observação** na escrituração dos Livros Fiscais de Entradas e Saídas.

Ao utilizar o parâmetro **MV\_SPDTC95**, verifique o efeito na geração do registro (padrão 1). Este parâmetro indicará qual o método de preenchimento do campo 03 – TXT\_COMPL para os registros C195 e D195.

**Regra parâmetro MV\_SPDTC95**

Preenchimento do campo complementar do código de observação: 1 = CCE / SFT 2 = CCE; 3 = SFT; 4 = vazio.

SPED Fiscal considera seguinte regra para compor registro C195.

Se campo preenchido F4\_CODOBSE sistema irá considerar campo F4\_CODOBSE

Se MV\_SPDTC95 = 1 ou 3

                Se campo FT\_FORMULA preenchido, sistema irá considerar campo FT\_FORMULA

  Se MV\_SPDTC95 = 1 ou 2

                Sistema irá considerar campo CCE\_DESCR

Se MV\_SPDTC95 = 4 sistemas irá considerar F4\_CODOBSE

**Importante:**

Para a correta geração deste registro, o módulo **Livros Fiscais** disponibiliza dois recursos:

1. Ao configurar um lançamento fiscal automático pelo TES, informe o código da observação do documento fiscal pelo campo **Obs. Lanc. Fis.** e gere o documento;
2. Configure o código adequado pela rotina **Complementos de Documentos Fiscais**, disponibilizado na Nota Fiscal de Entrada, e/ou Saída, opção **Informações Complementares**, para cada documento gerado.
3. Para cada documento que tiver informações lançadas na coluna **Observação** dos Livros Fiscais de Entradas ou Saídas, inclua na rotina **Informações Compl. (tabela CCE)** um código e uma descrição correspondente à mensagem da escrituração lançada na coluna **Observação**. Informe também o código correspondente ao cadastro no campo do TES**Cód. Observ. (F4\_CODOBSE)**, fazendo uma correspondência entre o código da observação com o TES da operação.

Ao utilizar o parâmetro **MV\_SPDTC95**, verifique o efeito na geração do registro (padrão 1). Este parâmetro indicará qual o método de preenchimento do campo 03 – TXT\_COMPL para os registros C195 e D195.

Quando selecionar **1**, o SPED priorizará as informações da Informação Complementar (CCE)  e caso não encontre utilizará a Observação de Livro Fiscal (SFT) junto coma formula se conter.

Quando selecionar **2** apenas utilizará o cadastro de informação complementar (CCE).

Quando selecionar **3** apenas utilizará o livro fiscal (SFT)

Quando selecionar **4** sempre será vazio (branco).

#### **REGISTRO C197: Outras Obrigações Tributárias, Ajustes e Informações de Valores Provenientes de Documento Fiscal**

Este registro é gerado a partir dos lançamentos do **Documento Fiscal (CDA)** para apuração. O campo **Lançamentos de Apuração de ICMS (CDA\_TPLANC)** passa a ser obrigatório quando inserido manualmente no documento fiscal.

Para códigos de lançamento iniciados por "9" é possível configurar o valor a ser gravado através do campo "Vl.Reg.197" (CE0\_VL197) no cadastro de códigos de reflexo (FISA072), determinando sua gravação no campo 07-VL\_ICMS ou 08-VL\_OUTROS.

**Cadastro de TES:**

Devem ser preenchidos os campos abaixo:

Cod Lan (CC7\_CODLAN) = Código de ajuste da tabela CC6.

Obs. Lan Fis (CC7\_IFCOMP) = Informações do livro da tabela CCE

Lembrando que o campo Cod Lan (CC7\_CODLAN) deverá ser preenchido na TES e será considerado o cálculo informado no reflexo para tratamento do código de ajuste.

O campo Obs. Lan Fis (CC7\_IFCOMP) poderá ser informado no cadastro de TES ou no complemento da nota fiscal na Rotina MATA910/MATA920 – Opção – Informações complementares, campo Inf Compl. (CDT\_IFCOMP)

Verificar se o código de ajuste é um código valido, caso não seja preencher o campo na TES: Cód.Reflexo(CC7\_CODREF):= (CONFORME SUA NECESSIDADE).

**TES CC7**

![](http://tdn.totvs.com/download/attachments/238035285/image2016-7-7%2020%3A10%3A16.png?version=1&modificationDate=1467933016000&api=v2)

CDA aba Livros fiscais

![](http://tdn.totvs.com/download/attachments/238035285/image2016-7-7%2020%3A10%3A31.png?version=1&modificationDate=1467933031000&api=v2)

**Importante**

Deverá ser realizado a importação dos códigos de ajustes do site da receita SPED

CC6 – 5.3 Publicada no site do SPED como Ajustes e Informações de Valores Provenientes de

Para alimentar ou atualizar a tabela CC6 - Ajustes e Informações de Valores Provenientes de Documento Fiscal.

Acesse site da receita: <http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal>

\*Selecione as Tabelas de Seu Estado.

(Caso Estado selecionado não possua códigos de Ajuste de ICMS (Exemplo estado de São Paulo), poderá ser utilizado Tabela Genérica de ICMS "Selecionar Tabelas Genéricas - ICMS").

\*Baixar Ajustes dos Saldos da Apuração do ICMS (Arquivo TXT).

\*Coloque o Arquivo TXT dentro da pasta Protheus\_data/ System.

\*Inicialize Protheus utilizado "programa inicial" como U\_IMPSPED.

\*Durante o processo será feita pergunta (deseja efetuar a importação das informações cadastrais do SPED?) selecione botão SIM.

\* Selecione a pasta que está o arquivo TXT (Protheus\_data / System).

\*Após isso será exibido relatório com as tabelas atualizadas.

\*As tabelas CC7 e SF4 deverão conter o mesmo tipo de compartilhamento, senão o sistema não reconhece o cadastro de reflexo ao visualizar a SF4

 A tabela CC6 está atualizada conforme TXT.

 Para mais informações sobre a rotina FISA072, consulte o boletim:

<https://tdn.totvs.com/pages/releaseview.action?pageId=640907320>

Para mais informações sobre o Sped Fiscal acessar:  
<http://tdn.totvs.com/pages/releaseview.action?pageId=238035285>

Estamos em processo de unificação no **Configurador de Tributos**, caso possua alguma particularidade referente a apresentação **C195/C197**, orientamos que seja feita a configuração via **FISA170**:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/32109932224151-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Registros-C195-e-C197-via-Configurador-de-Tributos-FISA170>

Complementar:

[https://tdn.totvs.com/display/public/PROT/CFGTRIB++Frete+Pauta+considerado+nos+registros+C195+e+C197](https://tdn.totvs.com/display/public/PROT/CFGTRIB+-+Frete+Pauta+considerado+nos+registros+C195+e+C197)

Demais informações para o **Configurador de Tributos**, acesse a documentação:

<https://tdn.totvs.com/display/public/PROT/CFGTRIB+-+Configurador+de+Tributos+-+P12>
