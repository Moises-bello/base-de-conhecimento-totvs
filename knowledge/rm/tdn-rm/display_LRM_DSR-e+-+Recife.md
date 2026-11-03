---
content_hash: 15b1333171da31b4ca5cedd8e5a735c05571a99996461d15bddbadbb980e3ab1
fetched_at: '2026-06-29T00:09:20.115688+00:00'
page_id: '422545669'
product: rm
source: tdn-rm
title: DSR-e - Recife
type: documentation
url: https://tdn.totvs.com/display/LRM/DSR-e+-+Recife
version: 6
---

Com o intuito de facilitar a substituição do Recibo Provisório de Serviços - RPS por NFS-e, a Prefeitura de Recife-PE permite que sejam transferidas as informações dos contribuintes para a mesmo através de arquivo em formato texto.    
O arquivo conterá a declaração de documentos recebidos por um exclusivo contribuinte, ou seja, uma única inscrição municipal. Caso o contribuinte possua mais de uma inscrição municipal precisará ser gerado 1 (um) arquivo para cada uma das suas inscrições.

**Observações Gerais**

A rotinas será gerada através do Gerador de Saídas com layout específico da rotina através do menu Obrigações Acessórias | Gerador de Saídas.  
Serão validadas as seguintes regras para Seleção dos Lançamento para geração da rotina:

* [Lançamentos de Entrada](http://tdn.totvs.com/pages/viewpage.action?pageId=427041477) que possua pelo menos um produto do Tipo Serviço e o Tributo ISS na aba Outros Tributos do Item do lançamento;
* Lançamentos cujo Fornecedor não seja do tipo "Empresa";
* Não serão selecionados Lançamentos que possuam o status Estorno, Cancelados e Extemporâneos;
* Lançamentos que tenham sido escriturado manualmente, ou seja, possuam as opções "Nota Fiscal Acoberta Cupom Fiscal" e "Operação destinada ao Consumidor Final" marcadas, não serão considerados.

**Registro Tipo 10 - Cabeçalho**  
Este registro contempla os dados referente à Filial no qual o arquivo está sendo gerado. Será gerado de acordo com os dados da Filial selecionado pelo usuário na tela de geração da rotina.

**Registros não tratados pelo sistema**: Tipo 20, 21 e 30.

**Registro Tipo 40 - Declaração Eletrônica de Serviços Recebidos**  
Este registro será gerado somente se existir Lançamentos de Entrada cujo o Fornecedor seja diferente de "Empresa", se possuir produto do tipo Serviço e o Tributo "ISS" em Outros Tributos do Item do Lançamento Fiscal.  
A geração do campo Tipo de Documento é gerada a partir do Modelo ISS informado nos parâmetros do TOTVS Gestão Fiscal acesse, Ambiente | Parâmetros | TOTVS Gestão Fiscal | 03.02 - Apuração de Tributos | 03.02.03 - ISS | Apur. ISS por Filial | editar a filial desejada | Etapa 1 - Modelo de ISS, consistindo o Código Modelo de Documento associado ao Lançamento Fiscal.  
Os campos **Tipo de Tributação dos Serviços** e **Retenção de ISS** serão gerados a partir do tipo de recolhimento do Tributo ISS selecionado no Item do Lançamento Fiscal respeitando a seguinte regra:

|  |  |
| --- | --- |
| **Tipo de Tributação de Serviços** **(DSR-e)** | **Regra de Geração** |
| 01 – Tributável no Município | Tipo de recolhimento do ISS igual Nenhum, Devido, Retido Fonte, Retido Fonte - Deduzido e Depósito Judicial. |
| 02 – Tributável Fora do Município | Será gerado para os tipos de recolhimento Nenhum, Devido, Retido Fonte e Retido Fonte - Deduzido, desde que o município de prestação do serviço informado no item do lançamento seja diferente do município da Filial. |
| 03 – Operação Isenta | Tipo de recolhimento do ISS igual à Isento |
| 04 – Operação Imune | Tipo de recolhimento do ISS igual à Imune |
| 05 - Operação Suspensa por Decisão Judicial | Não será tratado pelo sistema |

|  |  |
| --- | --- |
| **Retenção de ISS** | **Tipo de Recolhimento** |
| 0 - Documentos **sem** ISS Retido | Retido Fonte ou Retido Fonte - Deduzido. |
| 1 - ISS Retido | Nenhum, Devido, Depósito Judicial, Isento e Imune. |

A **Data de Competência** consiste os seguintes campos considerando as seguintes regras:

* Caso o tipo de recolhimento selecionado no tributo do Item do Lançamento Fiscal seja do tipo Retido na Fonte ou Retido na Fonte - Deduzido e houver integração financeira habilitada, o sistema gerará o campo considerando a Data da Baixa informada na aba Integrações | Dados Financeiros do Lançamento Fiscal.
* Caso não haja integração financeira, será gerado com a Data de Vencimento do Lançamento Fiscal informada na aba Integrações | Dados Financeiros.
* Para os demais tipos de recolhimento Nenhum, Devido, Depósito Judicial, Isento e Imune, será preenchido com o a Data de Emissão do Lançamento Fiscal independente das datas informadas na integração financeira.

**Registro Tipo 90 - Rodapé**  
Neste registro será gerado os totalizados dos campos de número de linhas , Valor dos Serviços e Valor total das deduções contidas no registro 40. Demais campos 05-Valor Total dos Descontos Concedidos e 06-Valor Total dos Descontos Incondicionais não serão gerados.

Embasamento Legal

[Manual de Envio de RPS/DSR-e em Lote (Arquivo TXT - Versão 3.0)](https://nfse.recife.pe.gov.br/arquivos/nfse_layout_rps_v3.pdf)
