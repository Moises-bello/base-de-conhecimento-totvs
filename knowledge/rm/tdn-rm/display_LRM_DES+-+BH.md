---
content_hash: b4e1b1ea9c74390900eaa51685e77eeac5f1c5eb737df6db0e5e9500532f9649
fetched_at: '2026-06-29T00:09:21.416409+00:00'
page_id: '422545881'
product: rm
source: tdn-rm
title: DES - BH
type: documentation
url: https://tdn.totvs.com/display/LRM/DES+-+BH
version: 53
---

#FFA500#FFFACD#FFE766dashedAviso Importante:1%99%

Com o objetivo de proporcionar uma melhor experiência e alinhamento às atualizações mais recentes dos nossos produtos, informamos que a funcionalidade **DES-BH (Declaração Eletrônica de Serviços - Belo Horizonte)****,** já disponível no Módulo Gestão Fiscal, não será mais suportada no produto **RM Liber.exe** a partir da **versão 12.1.2502**

Reforçamos que essa alteração faz parte do nosso processo de evolução tecnológica, com a descontinuidade gradual de funcionalidades no **RM** **Liber.exe**. Para garantir a continuidade do uso e acesso à funcionalidade DES-BH, recomendamos que a geração seja feita diretamente no **Módulo Gestão Fiscal**.

# Conteúdo

2Conteúdo

# 1. Introdução

A **DES-BH (Declaração Eletrônica de Serviços - Belo Horizonte)** foi instituída pela Prefeitura de Belo Horizonte por meio do **Decreto 11.467/2003**. A entrega da DES-BH ao Fisco Municipal é obrigatória e deve ser feita mensalmente, até o dia 20 de cada mês.

Este documento tem como objetivo oferecer uma visão detalhada sobre a DES-BH, abordando os processos necessários para a correta geração do arquivo no Módulo Gestão Fiscal, que posteriormente será importado no programa da Prefeitura de Belo Horizonte.

  

# 2. Regras Gerais

#### Operações a serem informadas na DES:

* **Serviços prestados, tomados ou vinculados a terceiros**, sejam acobertados ou não por documentos fiscais, sujeitos ou não ao ISSQN;
* **Documentos fiscais cancelados, extraviados ou com validade expirada**;
* **Identificação de todos os documentos fiscais emitidos**, autorizados pelo Fisco Municipal, relacionados à prestação de serviços.

> **Importante:** Todos os documentos fiscais autorizados pelos Fiscos Municipal e Estadual devem ser informados na DES. Isso inclui o valor total da nota fiscal emitida e o valor do serviço prestado, quando aplicável.

#### Registro das Operações:

* **Serviços prestados**: no mês de emissão do documento fiscal;
* **Serviços prestados a órgãos públicos**: no mês do efetivo recebimento;
* **Serviços tomados**: no mês do pagamento ou crédito, o que ocorrer primeiro.

#### Guias de Recolhimento

As guias de recolhimento do ISSQN são geradas através do software da DES e devem ser obtidas diretamente pelos contribuintes e responsáveis tributários.

# 3. Geração do arquivo

A geração da DES deve ser realizada a partir do [Gerador de Saídas](https://tdn.totvs.com/pages/viewpage.action?pageId=237383341), para utilizá-la basta baixar o layout **FISLAY0030 - DES-BH.TotvsGen** mais recente disponível no [TOTVS Compartilhamento](https://tdn.totvs.com/pages/viewpage.action?pageId=348297816).

Ao executar serão solicitados os seguintes dados: 

* **Filial**: Selecionar a filial que será incluída no arquivo.
* **Período**: Informar a data inicial e final dos lançamentos, considerando que a geração é mensal.
* **Versão do layout**: Informar a palavra "VERSÃO" seguida do número da versão (ex: "VERSÃO300").
* **Classificações**: Usar as classificações corretas para a codificação do Município e do País.
* **Gerar Centralizada**: Marcar essa opção caso as filiais tenham a mesma Inscrição Municipal e estejam no mesmo município. Caso contrário, desmarcar para gerar o arquivo apenas com as informações da filial selecionada.

**Observação**: Se a Filial selecionada for órgão público, marcar a opção "Órgão Público". O preenchimento deste campo impacta na geração do campo 2 "Data de pagamento ou reconhecimento do crédito" do Registro Tipo "R" - Serviços Tomados, como veremos adiante.

# 4. Seleção de Lançamentos

A seleção dos Lançamentos Fiscais de Entrada e Saída será realizada de acordo com os parâmetros definidos no TOTVS Gestão Fiscal (Processo 03.02.03 - Etapa "Apur. ISS por Filial" | **Datas Apuração do ISS**). As opções são:

* Data de Emissão;
* Data de Entrada/Saída;
* Data de Pagamento/Vencimento.

Utilizando a opção "Data de Pagamento/Vencimento", o sistema se comportará da seguinte forma:

* Se existir integração com sistema de Gestão Financeira, serão selecionados os Lançamentos Fiscais cujo Lançamento Financeiro associado esteja baixado no período informado na tela da rotina (Data de Baixa);
* Se não existir integração com sistema de Gestão Financeira, serão selecionados os Lançamentos Fiscais cuja Data de Vencimento (aba "Dados Financeiros") esteja no período informado na tela da rotina.

Essa parametrização deve ser feita para cada tipo de operação:

* Lançamentos de Entrada;
* Lançamentos de Saída – Entidade Privada (Cliente/Fornecedor);
* Lançamentos de Saída – Entidade Pública (Cliente/Fornecedor).

***Importante!*** Se a Filial estiver parametrizada para utilizar município por item, as informações de Alíquota, Tipo de Recolhimento, Base de Cálculo e Valor do Imposto serão preenchidos conforme os dados informados na aba "Outros Tributos" dos Itens do Lançamento Fiscal. Se a Filial for parametrizada para não usar o município por item, esses campos serão preenchidos conforme os dados informados na aba "Outros Tributos" do Lançamento Fiscal.

# 5. Registros

A geração do arquivo da DES-BH pelo Módulo Gestão Fiscal da linha RM **não inclui** os registros **T (Transmissão de Imóveis)** e **I (Adquirente)**, portanto, não serão gerados.

Os demais registros serão gerados de acordo com as regras detalhadas abaixo.

registrosregistro-hRegistro H2

### Registro H - Identificação

|  |  |  |
| --- | --- | --- |
| **Posição** | **Campo** | **Origem dos Dados** |
| 01 | Tipo do Registro | Identificação do registro. Caractere fixo "H". |
| 02 | Inscrição Municipal | Cadastro da Filial |
| 03 | CNPJ | Cadastro da Filial |
| 04 | Versão do sistema | Informado pelo usuário na tela de geração da rotina. |

registro-eRegistro E2

### Registro E - Serviços Prestados

registro-dRegistro D2

### Registro D - Dedução De Materiais, Serviços Ou Repasses

registro-rRegistro R2

### Registro R - Serviços Tomados
