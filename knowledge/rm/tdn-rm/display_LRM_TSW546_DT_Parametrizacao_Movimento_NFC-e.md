---
content_hash: b85c9116e1ec65f011fa422fd9d90cb93eeec6d4d9589a71b96e09262f12a0fa
fetched_at: '2026-06-29T00:06:05.773933+00:00'
page_id: '201727197'
product: rm
source: tdn-rm
title: TSW546_DT_Parametrizacao_Movimento_NFC-e
type: documentation
url: https://tdn.totvs.com/display/LRM/TSW546_DT_Parametrizacao_Movimento_NFC-e
version: 6
---

# Parametrização Movimento NFC-e

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **Gestão de Compras, Estoque e Faturamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Mov.321407* | *NOTA FISCAL DE SAIDA* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Mov.321348** | *PARAMETRIZACAO POR TIPO DE MOVIMENTO* | | **PAR.014** | *PARAMETRIZACAO - TIPO DE MOVIMENTO* | | *FIS.451627* | *NF-E PARAMETRIZACAO DE MOVIMENTO RELACIONADO A NF-E* | | *MOV.013* | *COPIA A PARTIR DE OUTRO MOVIMENTO* | | *Mov.321412* | *COPIA DE MOVIMENTO A PARTIR DE MOVIMENTO SELECIONADO* | | *MOV.002* | *EDICAO DE MOVIMENTO* | | *MOV.003* | *EXCLUSAO DE MOVIMENTO* | | *MOV.001* | *INCLUSAO DE MOVIMENTO* | |
| **Cadastros Iniciais:** | *Não se aplica* |
| **Parâmetro(s):** | *Não se aplica* |
| **Ponto de Entrada:** | *Não se aplica* |
| **Chamados relacionados** | *Não se aplica* |
| **Requisito (ISSUE):** | *Não se aplica* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server e Oracle* |
| **Tabelas utilizadas:** | *TParFilial, TTMV, TTMvExt, TMov* |
| **Sistema(s) operacional(is):** | *Não se aplica.* |
| **Versões/Release:** | *12.1.7* |

## Descrição

Parametrização da Filial a usar a integração e do Tipo de Movimento a ser utilizado para emissão da Nota Fiscal de Consumidor Eletrônica (NFC-e).

Emissão da NFC-e.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *(12.1.7)* deste chamado.

## Procedimento para Configuração

* # Parametrização da Filial

A configuração é realizada através do módulo BackOffice >> “Gestão de Estoque, Compras e Faturamento” >> Ambiente >> Parâmetros, item “Gestão de Estoque, Compras e Faturamento”, acessar o processo referente a "Integrações >> Fiscais >> Dados Fiscais", selecionar "Parâmetros por Filial" e parametrizar a Filial desejada.

 

 Para o "Ambiente NFC-e", informar:

* + **Ambiente e Modalidade:** Se o ambiente será de Homologação ou Produção. Importante: A modalidade deverá ser tratada na visão de envio da NFC-e através de processo específico.
  + **Versões do Layout:** Especifique a versão;
  + **Segurança:** Neste grupo de informações teremos os dados referentes a:
    - **URL do QRCode;**
    - **URL da SEFAZ para Consulta da NFC-e;**
    - **Código de Segurança:** Código Segurança Contribuinte;
    - **ID do Código de Segurança:** ID do Código Segurança Contribuinte.

* # Parametrização do Tipo de Movimento

**Importante:**A identificação do consumidor não é obrigatória na emissão da NFC-e. Sendo assim, deve-se observar as seguintes regras:

* + **Com identificação:** registrar consumidor no cadastro de Cliente/Fornecedor para seleção no movimento;
  + **Sem identificação:** utilizar registro de Cliente/Fornecedor fictício (Exemplo: “Cliente de Balcão”) para selecionar no movimento já que o campo é de preenchimento obrigatório.

 A configuração é realizada através do módulo BackOffice >> “Gestão de Estoque, Compras e Faturamento” >> Ambiente >> Parâmetros, item “Gestão de Estoque, Compras e Faturamento”, acessar o processo referente ao movimento desejado (Vendas ou Outras Movimentações), selecionar o tipo de movimento e solicitar para parametrizar.

 Abaixo estão relacionados os principais processos diretamente ligados à NFC-e:

* + **Etapa “Mov – Emitente/Destinatário”:** Se a integração não usar a identificação do consumidor deve-se informar o “Cliente/Fornecedor Destino Default” do “Cliente de Balcão”;
  + **Etapa “Fis – Escrituração 1/2”:** Informe o tipo de documento escrituração modelo “65” (NFC-e);
  + **Etapa “Fis - NF-e”:** No grupo de dados para emissão de NFC-e informe:
    - **Tipo da Integração:** “Não integrado”, “Integrado NFC-e”.
    - **Formato da Impressão:** “DANFE NFC-e em Mensagem Eletrônica”, “DANFE NFC-e”.
    - **Relatório .Net Default:** Report .Net da NFC-e.

 

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [PAR.014 – Parametrização Tipo de Movimento] | [Alteração] | [Ambiente -> Parâmetros -> TOTVS Gestão de Estoque, Compras e Faturamento -> Tipo de Movimento] | - |
| [MOV.001 – Inclusão de Movimento] | [Envolvida] | [Vendas -> Faturamento] | - |
| [PAR.008 – Parametrização - Integrações] | [Envolvida] | [Ambiente -> Parâmetros -> TOTVS Gestão de Estoque, Compras e Faturamento -> Integrações -> Fiscal -> Dados Fiscais] | - |

***Tabelas Utilizadas***

* GCOLIGADA – Coligadas
* GFILIAL – Filiais
* TPAR – Parâmetros Gerais
* TPARFILIAL – Parâmetros por Filial
* TTMV – Tipos de Movimento
* TTMVEXT – Tipos de Movimento
* TMOV – Movimentos
* RRPTREPORT - Relatórios .NET

## Procedimento para Utilização

* # Emissão do Movimento

Através do módulo BackOffice >> “Gestão de Estoque, Compras e Faturamento” >> Vendas >> Faturamento, “SPED NF-e (Estadual)”, selecionar o movimento devidamente parametrizado para emissão da NFC-e.

A integração deverá consistir se o tipo de documento é o “65” para liberação dos campos dos dados da NFC-e.

Os campos para CPF/CNPJ/ID Estrangeiro e Nome deverão ficar disponíveis se a integração NFC-e estiver habilitada, caso contrário os campos deverão ficar indisponíveis. Por padrão será consistido o preenchimento dos campos e, caso estejam vazios, o consumidor será identificado pelo Cli/For selecionado no movimento.

**Observações:**

* + O CPF/CNPJ será consistido no mesmo campo com a verificação da quantidade de caracteres sendo desprezados os caracteres especiais de máscara (TMov.CNPJCPFAdquirente);
  + O “ID Estrangeiro” terá um campo próprio (TMov.DocEstrangeiroAdquirente) – a definição do nome do campo obedeceu a mesma regra da antiga rotina de Cupom Fiscal (tabela TCupomFiscal);
  + O consumidor pode ser identificado apenas pelo campo de CPF/CNPJ ou ID Estrangeiro, sendo opcional o preenchimento do campo Nome (TMov.NomeAdquirente). Desta forma, na geração do XML somente suas respectivas tags serão preenchidas (sem informação de endereço);
  + Para consumidor não identificado o valor máximo permitido é de R$10.000,00 (dez mil reais). Acima desse valor o consumidor obrigatoriamente deverá ser identificado;

 

* # Envio da NFC-e

Através do módulo BackOffice >> “Gestão de Estoque, Compras e Faturamento” >> Vendas >> Faturamento >> “SPED NF-e (Estadual)”, selecione o filtro desejado e execute o processo “Enviar  NF-e\NFC-e”.

Para cada movimento selecionado será gerado o XML e registrado na tabela TNFeEstadual, conforme a modalidade em uso no momento (Normal, Contingência EPEC ou Contingência Offline). Se o envio obter sucesso o registro terá o status “Pendente” (default) e deverá ser executado o processo para consultar a autorização, caso contrário o registro terá o status “Inconsistente” e será informado ao usuário para correção do problema e retransmissão.

O reenvio da NFC-e será permitida para registros no status “Inconsistente” ou “Rejeitada”.

Se foi gerada NFC-e para o movimento ele não poderá ser alterado, exceto quando a NFC-e estiver com status “Inconsistente” ou “Rejeitada”.

**Importante:**

* + Ao enviar NFC-e é necessário consistir se os campos de Código de Segurança do Contribuinte e seu respectivo ID estão preenchidos, pois os mesmos devem ser informados na alteração de parametrização do Ambiente NFC-e da Filial (homologação/produção);
  + As NFC-es emitidas em contingência não serão enviadas para a SEFAZ. Os documentos deverão ser reenviados em um prazo de 24h (vinte e quatro horas) para obter a autorização e possibilitar ao consumidor a consulta da Chave de Acesso na base de dados da SEFAZ. Na impressão deverá constar a mensagem “EMITIDA EM CONTINGÊNCIA”;
  + Na impressão de NFC-e emitido em ambiente de homologação é obrigatório constar na área de Mensagem Fiscal o termo “EMITIDA EM AMBIENTE DE HOMOLOGAÇÃO – SEM VALOR FISCAL”;
  + Na impressão de NFC-e emitido sem identificação do consumidor deverá constar em seu respectivo quadro a expressão “CONSUMIDOR NÃO IDENTIFICADO”.

* # Cancelamento da NFC-e

O cancelamento da NFC-e poderá ser realizada em um prazo de 30 (trinta) minutos após sua autorização.

 

* # Inutilização da NFC-e

A inutilização da NFC-e segue os mesmos princípios da NF-e (processo de evento).
