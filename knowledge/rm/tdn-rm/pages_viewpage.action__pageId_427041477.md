---
content_hash: 6691ba51e345625137486f60b19f96f9c28bfeebe58623961c675823b5fd3c98
fetched_at: '2026-06-29T00:09:38.506736+00:00'
page_id: '427041477'
product: rm
source: tdn-rm
title: Entradas e Saídas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=427041477
version: 116
---

**Informamos que os dados pessoais contidos nesta entidade foram colhidos para emissão de documentos fiscais e geração de rotinas legais e são retidos por determinação legal de normas fiscais e de transparência. Os mesmos não poderão ser eliminados em virtude de obrigação legal de retenção. O cumprimento de obrigação legal é hipótese legítima do tratamento dos seus dados conforme a Lei Geral de Proteção de Dados Pessoais (Lei n° 13.709/2018).**

**Para mais informações sobre a LGPD e as soluções oferecidas pela TOTVS consulte nossa página neste link ([https://tdn.totvs.com/pages/releaseview.action?pageId=514427789](https://tdn.totvs.com/pages/releaseview.action?pageId=514427789 "Follow link")).**

#f5f5f5#363636noneEntradas e saídas

## **- Visão Geral**

Através deste cadastro pode-se fazer a manutenção dos Lançamentos Fiscais de Entrada e Saídas.  Neste cadastro também são visualizados os lançamentos originados no processo de Escrituração Fiscal do Gestão de Compras Estoque e Faturamento. Só é permitida a inclusão de Lançamento Fiscal em que o Período de Apuração vinculado ao lançamentos esteja com status aberto. Para um melhor controle e organização dos Lançamentos Fiscais na visão pode-se optar pelo uso de Lotes de Lançamentos.   
O cadastro de Lançamentos é composto de guias verticais que podem ser expandidas ou contraídas para facilitar a visualização e edição das informações. As informações a serem gravadas nos Lançamentos Fiscais dependem do Tipo de Livro (Processo 03.01.01) Parametrizado para a Filial corrente. Para cada lançamento podem ser gravadas as seguintes informações:

LçtoFiscalLançamento FiscalfalseLançamento Fiscalleft0Identificação

## Cabeçalho

Nesta guia devem ser gravados todos os dados obrigatórios para a identificação do Lançamento Fiscal. A informação do Tipo de Documento irá determinar algumas informações que deverão ser preenchidas e também habilitar ou desabilitar campos do cadastro como os de Conhecimento de Transporte Rodoviário de Carga e os dados da . O campo Tipo [CT-e/BP-e/CTe OS](http://tdn.totvs.com/pages/viewpage.action?pageId=450158402) será habilitado para preenchimento quando for informado no Lançamento Fiscal um dos seguintes Tipos de Documento: 57 - CT-e, 63 - BP-e ou 67 - CT-e OS. Quando se tratar de Lançamento Fiscal originado de Escrituração Fiscal este campo será preenchido conforme regra descrita a seguir:

Caso o Tipo de Documento seja  57 ou 67, o mesmo recuperará a informação do campo TIPOCTE da TMOVTRANSP,

Caso o Tipo de Documento seja  63, o mesmo recuperará a informação  do campo TIPOBPE da TMOVTRANSP,

Caso o movimento seja criado a partir da cópia por referência, com motivos: 16 - Conhecimento Transporte Eletrônico (CT-e) – Anulação ou  17 - Conhecimento Transporte Eletrônico (CT-e) – Substituição o lançamento será escriturado com a referência informada no movimento de origem.

Criado o grupo Adquirente na identificação do Lançamento Fiscal que será habilitado somente quando o tipo de documento for igual a 65-Nota Fiscal de Consumidor Final (NFC-e): Grupo composto dos seguintes campos:   
**CNPJ/CPF:**Caso o usuário informe um valor com 11 posições no campo CNPJ/CPF, o sistema identificará que se trata de CPF e irá aplicar a máscara do CPF e validar o mesmo. Da mesma forma o sistema irá se comportar para valores inseridos com 14 posições, identificará que a informação se trata de CNPJ e irá validar o mesmo.  
***Observação*:** Sendo informado valor diferente de 11 (onze) ou 14 (quatorze) posições, irá apresentar a seguinte mensagem "O Valor informado no campo CNPJ/CPF do Adquirente não corresponde à um CNPJ ou CPF válido." Para este tipo de documento o campo é obrigatório.

Lei Geral de Proteção de Dados (LGPD)

## Foram criados provedores de proteção de dados, para os dados do Lançamento Fiscal, Item do Lançamento Fiscal e vinculo do Lançamento de Ajuste com Lanaçamento Fiscal. Eles poderão ser identificados a partir do campo:

* Para Lançamento Fiscal (DLAF) : CNPJ/CPF do Adquirente (CNPJCPFADQUIRENTE)
* Para o Item do Lançamento Fiscal (DITEM): CNPJ do Adquirente (CNPJADQUIRENTE)
* Para o Lanc. Outros Débitos/Créditos (DLDCNF): (CNPJCPFCEI)

Poderão ser anonimizados caso não seja encontrado nenhum registro na Base de dados relacionados ao adquirente.

**Doc. Estrangeiro:**O campo Doc. Estrangeiro poderá ser preenchido com no máximo 20 (vinte) caracteres e o campo não é obrigatório.

**Nome:**Neste campo deve ser preenchido o nome do adquirente. Preenchimento livre de tamanho máximo de 60 caracteres. Campo não obrigatório.  
***Observações:*** Foi adicionado ao campo Presença do Comprador o valor "4 – NFC-e em Operação com entrega em domicílio", valor específico para este tipo de documento.

**Cliente\Fornecedor Origem / Destino:**  
A intenção desde campo é utilizar na Emissão Própria da NFe, onde um cliente / fornecedor ou empresa adicional ao lançamento para atender a lançamentos de importação, devoluções, em que o emitente da nota fiscal é de um estado diferente ao destinatário/remetente da nota fiscal, sendo que, neste caso, a código da operação fiscal estará ligado a este campo. Este campo só aparecerá na tela de lançamentos se em [Opções/Parâmetros Gerais-Tabelas/Lançamentos-Geral](//tdn.totvs.com/IDH_PastaLanGeralParGeraisTabela.htm)., confirmou o campo “Edita Cli/For Origem/Destino”.

Lei Geral de Proteção de Dados (LGPD)

## Foram criados provedores de proteção de dados, para os dados do Cliente/Fornecedor que poderão ser identificados a partir do campo CNPJ/CPF do Participante, e poderão ser anonimizados caso não seja encontrado nenhum registro na Base de dados ao Cliente/Fornecedor.

**Observação**: Este campo interfere na geração do Campo 03 - IND\_EMIT - Indicador do emitente do documento fiscal da Rotina EFD Contribuições.

**Data Entrega:** Este campo pode ser preenchido manualmente pelo usuário ou automaticamente atualizado com as informações de Data de Entrega provenientes do Movimento.

**Finalidade da Nota Fiscal:** Este campo pode ser preenchido manualmente pelo usuário. No caso de Lançamentos Fiscais escriturados a partir do Módulo de Gestão de Compras, Estoque e Faturamento, será preenchido automaticamente de acordo com as informações parametrizadas no Tipo de Movimento que originou o lançamento.  
  
**Tipo da Nota Fiscal:** Este campo pode ser preenchido manualmente pelo usuário. No caso de Lançamentos Fiscais escriturados a partir do Módulo de Gestão de Compras, Estoque e Faturamento, será preenchido automaticamente de acordo com as informações parametrizadas no Tipo de Movimento que originou o lançamento. Cabe ressaltar que as opções de finalidade variam conforme o **Finalidade da Nota Fiscal** selecionado.

1Tributação

## Resumo

Nesta guia será feito um resumo dos valores que forem informados no Lançamento Fiscal. Esta guia não é editável pois será preenchida automaticamente ao salvar o registro.

## Situação Tributária

O conceito de parcelas de lançamento Fiscal foi substituído por Situações Tributárias e nelas devem ser gravadas todas as informações de tributação existentes no documento fiscal. Poderão ser inseridas tantas Situações Tributárias quanto forem as existentes no documento fiscal.

2Transporte

## Identificação

Nesta guia serão informados os dados do da mercadoria transportada como peso bruto/líquido, marca, espécie, distância e também o Tipo do Frete.

## Transportadora

Onde serão informados os dados da transportadora como placa, via de transporte e UF.

## Coleta e Entrega

Nesta guia serão informados o estado de coleta e entrega.

O parâmetro "Coleta/Entrega Não Afeta a Seleção de CFOP" define se a UF do Local de Coleta e Local de Entrega não devem afetar a regra de seleção de CFOP.  Caso o movimento do TOTVS Gestão de Estoque, Compras e Faturamento, campo "Utilizar Endereço de Coleta e Entrega como Destinatário", estiver com a opção "**Usa sem afetar a seleção do CFOP**" , ao executar o processo de Escrituração de Lançamento o campo será habilitado automaticamente.

## LGPD

Foram criados provedores de proteção de dados, para os dados de Coleta/Entrega que poderão ser identificados a partir do campo CNPJ/CPF de Coleta/Entrega, e poderão ser anonimizados caso não seja encontrado nenhum registro na Base de dados vinculado a Lançamentos Fiscais. 

Comportamento do Parâmetro no Gestão de Estoque, Compras e Faturamento

Parâmetro de regra de seleção do CFOP quando se é utilizado Coleta e Entrega, está disponível nos parâmetros do Tipo de Movimento, etapa 19 - Mov - Transporte 2/3, campo "Utilizar Endereço de Coleta e Entrega como Destinatário". O comportamento das opções disponíveis são as seguintes:

**Não usa**: Quando selecionada a pasta “Coleta e Entrega” da aba “Transporte” do movimento no TOTVS Gestão de Estoque, Compras e Faturamento não ficará visível. Neste caso a seleção do CFOP será feita de acordo com a UF do Emitente e Destinatário (Cliente/Fornecedor) selecionados na Identificação do movimento. Validará também o Cliente Origem/Destino informado na pasta Fiscal da aba Integrações do movimento.

**Usa**: A pasta “Coleta e Entrega” da aba “Transporte” do movimento no TOTVS Gestão de Estoque, Compras e Faturamento ficará visível. A consistência de seleção do CFOP ocorrerá de acordo com a UF informada nos dados de Coleta e Entrega.

**Usa Sem Afetar a Seleção de Natureza**: A pasta “Coleta e Entrega” da aba “Transporte” do movimento no TOTVS Gestão de Estoque, Compras e Faturamento ficará visível. A consistência de seleção do CFOP seguir[a conforme a opção “Não Usa”, de acordo UF do Emitente e Destinatário (Cliente/Fornecedor) e também o Cliente Origem/Destino informado na pasta Fiscal da aba Integrações do movimento.

***IMPORTANTE!!!****Este campo está disponível a partir da versão 12.1.26. Nas versões 12.1.23, 12.1.24 e 12.1.25 o campo estará disponível a partir da execução de scripts específicos. Caso precise, entre em contato com o nosso atendimento.*

Motoristas

Onde serão informados os dados do motorista, como Nome e CPF

LGPD - Dados do Motorista

Foram criados provedores de proteção de dados para os dados do Motorista, que poderão ser identificados a partir do campo CPF. Estes dados poderão ser anonimizados caso não seja encontrado nenhum registro na base de dados vinculado a Lançamentos Fiscais.

Remetente/Destinatário

Nesta guia serão informados o tipo do Remetente / Destinatário ,  o tipo de CT-e/ BP- e / CT-e OS,  os dados do Redespacho como transportadora e o "Tipo Frete Redespacho".

Guia habilitada quando selecionado o tipo de documento na guia "Cabeçalho" utilizando um dos códigos abaixo de modelo de documento:

| **Código** | **Descrição** |
| --- | --- |
| 07 | Serviço de Transporte |
| 08 | CTRC |
| 09 | Aquaviário Cargas |
| 10 | Aéreo |
| 11 | Ferroviário Cargas |
| 25 | Manifesto Carga |
| 26 | Multimodal Cargas |
| 27 | NF Transporte Ferroviário Cargas |
| 57 | CT-e |
| 67 | CT-e OS |
| 63 | BP-e |

NFs Carga Transportada

Nesta guia serão informados as NFs que foram transportadas.

Guia habilitada respeitando os mesmos códigos de modelo de documento do Remetente / Destinatário com a exceção do **63 - BP-e**.

2Informações Adicionais

## Dispositivo de Segurança

Onde é informado o número da AIDF  dos Dispositivos de Segurança. Para habilitar esta aba é necessário ter AIDF cadastrada na Base.

## Outros

Disponível os campos Centro de Custo Contábil, Departamento, Número Documento/Dispositivo de Segurança, Data Visto, Nota Fiscal Acoberta Cupom Fiscal, Operação com Consumidor Final, Motivo do Cancelamento e Filial SCP.

## Energia / Comunicação

Guia para informação dos dados da NF de energia  elétrica ou comunicação.

Guia habilitada quando selecionado o tipo de documento na guia "Cabeçalho" utilizando um dos códigos abaixo de modelo de documento:

| Código | Descrição |
| --- | --- |
| 06 | Energia Elétrica |
| 21 | Comunicações |
| 22 | Telecomunicações |
| 66 | NF-e Energia Elétrica |
| 62 | Nota Fiscal Fatura Eletrônica de Serviços de Comunicação |

## Modelo 06/66

## 

## Modelos 21/22/62

## Exportação

**Número Despacho**: tamanho 12 caracteres **(a partir da versão 12.1.31 o campo foi alterado de tamanho, passando de 11 para para 12 caracteres. Código do Script LI.2021.12\_01)**

NF-e Estadual

Guia na qual ficam localizados os Campos de Uso Livre para a Nota Fiscal Eletrônica.  
Os campos podem ser cadastrados nessa guia ou serem importados, caso algum campo default já esteja cadastrado.  
OBS: As alterações dos campos livres de um lançamento escriturado serão refletido no seu respectivo movimento.

2Integrações

## Dados Financeiros

Nesta guia deve ser informado todos os dados relativos ao financeiro.

Situação TributáriafalseSituação Tributárialeft0Dados Fiscais

## Características

Determina qual a operação está sendo efetuada.

[Desabilita regra de seleção de natureza](https://tdn.totvs.com/pages/viewpage.action?pageId=649997959)

## Valor de Mercadoria

Nesta guia deve ser informada a composição do valor da mercadoria do documento fiscal. Este valor está relacionado com a totalização dos itens da Situação Tributária.

## ICMS/IPI e Substituição Tributária

Serão informados de acordo com a parametrização da Regra de ICMS e Regra de IPI associadas ao cadastro da Natureza de Operação que foi informada nas características da Situação Tributária.

***Observações:***Existe a possibilidade de incluir os tributos incidentes no documento fiscal diretamente na Situação Tributária ou em cada um de seus itens. Antes de optar pelo local de gravação dos tributos devem ser verificadas quais Rotinas Legais a Filial deve gerar. Existem rotinas, como é o caso do SPED Fiscal e EFD Contribuições que exigem as informações de tributação no item do documento fiscal.

## Composição do Frete

Nesta guia serão informados os valores componentes do frete quando o mesmo existir no documento fiscal.

## Outros Tributos

Estes tributos são carregados automaticamente da Natureza Fiscal quando a mesma os possui como default ou podem ser incluídos manualmente de acordo com a necessidade.

Regras de habilitação dos campos

**Tipo Recolhimento**: É habilitado para edição quando o tipo tributo for ISS ou IRRFPJ.

**Identificador do Código da Receita**: É habilitado para edição quando o tipo de lançamento for de **saída** ou

tipo de lançamento de **entrada** com tipo tributo diferente de IRRFPJ e COSIRF.

**Código da Receita**: É habilitado para edição quando o tipo de lançamento for de **entrada** com tipo tributo igual a IRRFPJ ou COSIRF.

Natureza de Rendimento

A partir das bibliotecas 12.1.2205.202 e 12.1.2209.143, o campo "Informe da Natureza de Rendimento" foi adicionado nesta aba, bem como em "Outros Tributos" dos itens de uma Situação Tributária.

## Normas Referenciadas

Nesta guia podem ser associadas Normas Legais com as quais o documento fiscal esteja relacionado.Esta informação é utilizada para gerar as Rotinas Legais SPED Fiscal*e* EFD Contribuições.

## Processos Judiciais

Nesta guia podem ser associados Processos Judiciais/Administrativos relacionados ao documento fiscal emitido. Esta informação é utilizada para gerar as Rotinas Legais SPED Fiscal*e* EFD Contribuições.

## Recalculo

Nos casos de cálculo do ICMS monofásico, não deve ser feito recálculo na Situação Tributária.

## Ajuste SPED

Nesta guia serão informados os códigos de ajuste do SPED Fiscal.

Mais informações do cadastro presente em [Código de Ajuste](https://tdn.totvs.com.br/pages/viewpage.action?pageId=427053053).

1Itens

## Itens

Em uma mesma Situação Tributária poderão ser incluídos um ou mais itens.

**Conta Contábil**: Campo disponível na pasta Características do item da Situação Tributária. Este campo deve ser preenchido com o código de conta contábil que será utilizada nas rotinas da EFD Contribuições, SPED Fiscal e Integração com o TAF. Regra de preenchimento do campo Conta Contábil:

1. Será preenchido com o Default Contábil da Natureza (CFOP): caso exista Default Contábil na Natureza e se possui Classificação de Conta como "SPED",
2. Será preenchido com o Default Contábil do Cadastro do Produto/Serviço: caso exista Default Contábil no Cadastro do Produto/Serviço e se possui a Classificação de Conta como "SPED",
3. Será preenchido com o Default Contábil do Cadastro – Produto - Dados Fiscais: será utilizado o Default de Conta Contábil informada no Cadastro – Produto - Dados Fiscais,
4. Se não encontrado Conta Contábil o campo não será preenchido automaticamente e poderá ser incluído manualmente.

IMPORTANTE!!!

* Contas cadastradas como Débito, serão para os Lançamentos Fiscais de Entrada, por sua vez, as contas cadastradas como Crédito serão para os Lançamentos de Saída.
* Se o Default Contábil estiver parametrizado com uma Filial que não seja a mesma Filial do Lançamento Fiscal, a mesma sera desconsiderada.
2Prestação de Serviços

## Prestação de Serviços

Os campos serão preenchidos quando se tratar de deduções na prestação de serviço como valor de sub empreitada e materiais.

## Deduções de Materiais

Selecionar os documentados relacionados as deduções do serviço.

## Deduções Sub Empreitada

Selecionar os documentados relacionados as deduções da sub empreitada do serviço.

2Informações Adicionais

## Campos Opcionais

São informados os dados da SISIF

## Outros Dados

Nesta guia são gravados o número do livro e folha na qual o Lançamento Fiscal foi impresso. Quando se trata de Lançamento do Cupom Fiscal o campo Mapa Resumo será alimentado. Estes campos serão preechidos automaticamente quando da emissão dos Livros Fiscais de Entrada/Saída e o Mapa Resumo forem impressos como oficiais. O campo Alíquota DAPI deverá ser preenchido quando houver necessidade da geração da Rotina Fiscal DAPI para o estado de Minas Gerais. Este campo só será exibido quando: O Estado da Filial ativa for Minas Gerais, O parâmetro Usa Alíquota DAPI estiver habilitado e o campo Usa Alíquota DAPI no cadastro da Natureza de Operação associada a Situação Tributária estiver marcado.

## Campos Complementares

São os campos criados pelo usuário para que ele possa informar dados que não existem na base de dados do produto. Estes campos podem ser utilizados para a geração de relatórios. Para mais informações sobre Campos Complementares consulte: [Campos Complementares (Fiscal)](https://tdn.totvs.com/pages/viewpage.action?pageId=440831722)

## Enquadramento Siscoserv

Nesta guia são informados as operações que envolvem o comércio exterior para registro das informações relativas às transações realizadas entre residentes ou domiciliados no Brasil e residentes ou domiciliados no exterior que compreendam serviços.

Guia habilitada quando utilizado naturezas de saída iniciadas com "7" ou naturezas de entrada iniciadas com "3".

Local Operação

Nesta guia, informamos  o estado e o município para fins de apuração e distribuição do IBS (imposto sobre Bens e Serviços) .

Referências

Este grupo é habilitado quando o CFOP informado na Situação Tributária possui Guia e/ou Documento referenciado.

---

**LANÇAMENTOS FISCAIS**

Nesta aba são informados os documentos referenciados. Segue informações dos campos:  
  
**Documento Fiscal**: Campo para vinculação do documento fiscal referenciado;  
**Motivo Referência:** Código do Motivo de Referência conforme detalhamento na documentação "[Motivo de Referência](https://tdn.totvs.com/pages/releaseview.action?pageId=423937926)";  
**Observação:**Campo livre para inserção de alguma observação;  
**Chave de Acesso:**Campo criado para atender a NT 2022.003, onde será possível enviar a chave de acesso de forma sigilosa, sem o código numérico, nas rotinas fiscais. Nos casos em quem este campo não esteja preenchido o sistema buscará a informação do campo chave de acesso, informada na aba "Informações Adicionais - Outros" do lançamento fiscal referenciado.

Exemplo

---

**NOTAS FISCAIS TERCEIROS**

Nesta guia são informados os documentos emitidos por terceiros.

Exemplo

---

**GUIAS DE RECOLHIMENTO**

Nesta guia são informados as guias de recolhimento.

Exemplo

---

**NOTAS EMPENHO**

Nesta guia são informadas as notas de empenho.

ExemploRateios

## Centros de Custo e Departamentos

Utilize estas guias se desejar ratear o valor do seu Lançamento Fiscal para seu Centro de Custo e Departamento. Estas guias podem ser desabilitadas na etapa 8 do processo 03.03.01 - Escrituração e Controle Fiscal do parametrizador do RM. Estes rateios poderão ser utilizados para gerar o rateio da contabilização do Lançamento Fiscal quando a mesma for feita pelo Processo Fiscal e por Evento Contábil.

Integrações

## Contábil

Nesta guia devem ser informados os dados para a contabilização do Lançamento Fical, Lote Contábil, data de contabilização, evento, etc. A contabilização poderá ser feita em cada Situação Tributária do Lançamento Fiscal ou ser agrupada na última quando existir mais de uma. O agrupamento de contabilização poderá ser habilitados nos parâmetros da Integração Contábil.

Na inclusão manual e na importação de Lançamentos Fiscais, o campo Contábil e a pasta de Integração Contábil serão apresentados apenas se o campo "Integração Contábil Ativa" estiver habilitado através Parâmetro acesse Ambiente | Parâmetros | 03.05 - Integrações | 03.05.01 - Contábil | Dados Gerais. Além do parâmetro, o campo Contabilidade da pasta Integrações do CFOP informado no Lançamento Fiscal, deverá estar habilitado e possuir um Evento Contábil Gestão Fiscal selecionado. O sistema já apresentará o campo contábil marcado e irá tentar fechar a contabilização do lançamento adicionando as contas Débito / Crédito sem que haja necessidade de acessar a pasta de Integrações | Contábil.

ItensfalseItensleftPara cada Item podem ser gravadas as seguintes informações:2Dados Fiscais

## Características

Insira nesta guia todas as informações para a correta identificação do Produto*.*

**Campo: Descrição do Produto no Fornecedor**

Campo para ser informado a Descrição do Produto que vem da Nota Fiscal de Entrada do Fornecedor.

obs.: Este Campos só e visível para Lançamentos Fiscais de Entrada.

Disponível a partir da Versão 12.1.2205

O campo pode ser informado no módulo de Faturamento e escriturado para o módulo Fiscal, para mais detalhes sobre o preenchimento no movimento [clique aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=574890054)

## Valores ICMS e Valores IPI

Informe nesta guia os valores para estes tributos de acordo com as Regras de ICMS e Regra de IPI associadas a Natureza de Operação informada na Situação Tributária.

Alíquota AD Rem

Para o cálculo do ICMS Monofásico, os valores da Alíquota AD Rem e Valor do ICMS devem ser inseridos de forma manual pelo usuário.

## Outros Tributos

São informados nesta guia outros [Tributos](http://tdn.totvs.com.br/pages/viewpage.action?pageId=422546150) que incidem no documento fiscal. Informações para a apuração do INSS e FUNRURAL.

Os tributos incluídos nesta pasta terão a **Base de Calculo** definidas como **Valor Unitário** x **Quantidade** (Valor Bruto do Item) independente de como foi configurado o cadastro do tributo.

Natureza de Rendimento

A partir das bibliotecas 12.1.2205.202 e 12.1.2209.143, o campo "Informe da Natureza de Rendimento" foi adicionado nesta aba, bem como em "Outros Tributos" da Situação Tributária.

## Prestação de Serviço

São informados a UF, município e o Código do Serviço.

## Ajuste SPED

Nesta guia serão informados os códigos de ajuste do SPED Fiscal.

Mais informações do cadastro presente em [Código de Ajuste](https://tdn.totvs.com.br/pages/viewpage.action?pageId=427053053).

## Tributo Discutido

Nesta guia serão informados os Processos Judiciais e os Tributos Discutidos dos itens no lançamento.

Os dados cadastrados aqui serão utilizados para a geração do registro 1011 na EFD PIS/COFINS

Transporte

## Dados do Transporte

Nesta guia serão informados os dados de transporte como veículo, origem, destino e indicador da natureza do frete.

Guia habilitada quando selecionado o tipo de documento na guia "Cabeçalho" utilizando um dos códigos abaixo de modelo de documento:

| Código | Descrição |
| --- | --- |
| 07 | Serviço de Transporte |
| 08 | CTRC |
| 09 | Aquaviário Cargas |
| 10 | Aéreo |
| 11 | Ferroviário Cargas |
| 25 | Manifesto Carga |
| 26 | Multimodal Cargas |
| 27 | NF Transporte Ferroviário Cargas |
| 57 | CT-e |
| 67 | CT-e OS |
| 63 | BP-e |

2Informações Adicionais

## Outros Dados

Nesta guia é gravada a observação do item do documento fiscal e os dados utilizados para a geração da rotina EFD Contribuições.

## Referências

Esta guia é habilitada quando o CFOP informado na Situação Tributária possui Guia e/ou Documento referenciado. São apresentados registros incluídos manualmente ou escriturados quando o tipo de referência for Devolução ou Movimento de Exportação

## Campos Complementares

São os campos criados pelo usuário. Estes campos podem ser utilizados para a geração de relatórios e também para que se possa informar dados que não existem na base de dados e que são necessários para atender obrigações acessórias, como por exemplo EFD Contribuições. A medida que estes campos complementares são migrados para campos da base eles são transferidos para a guia Outros Dados. Quando a migração ocorrer, o usuário deve desativar o campo complementar para que somente o campo da base seja preenchido e não gere inconsistências na rotina por falta destas informações.

Para mais informações sobre Campos Complementares consulte: [Campos Complementares (Fiscal)](https://tdn.totvs.com/pages/viewpage.action?pageId=440831722)

## Exportação

Nesta guia será informado os dados de exportação como "Número do Registro de Exportação" e "Data do Registro de Exportação".

Guia habilitada quando utilizado naturezas de saída iniciadas com "7" ou naturezas de entrada iniciadas com "3".

## Recalculo

Se o CST for 002, e o campo AliquotaADREM (usada no cálculo do ICMS monofásico) estiver preenchida o recalculo dos valores de ICMS não será realizado.

## NF-e Estadual

Guia na qual ficam localizados os Campos de Uso Livre para a Nota Fiscal Eletrônica.  
Os campos podem ser cadastrados nessa guia ou serem importados, caso algum campo default já esteja cadastrado.  
OBS: As alterações dos campos livres de um lançamento escriturado serão refletido no seu respectivo movimento.

#f5f5f5#363636noneCadastros prévios

Para a correta utilização dos Lançamentos Fiscais, os seguintes cadastros deverão ter sido previamente e concluídos:

* [Natureza de Operação](https://tdn.totvs.com/pages/viewpage.action?pageId=422545982)
* Tipo de Documento
* [Regra de ICMS](https://tdn.totvs.com/display/LRM/Regra+de+ICMS)
* [Regra de IPI](https://tdn.totvs.com/display/LRM/Regra+de+IPI)
* Produtos
* Cliente/Fornecedor
* Outros Tributos
