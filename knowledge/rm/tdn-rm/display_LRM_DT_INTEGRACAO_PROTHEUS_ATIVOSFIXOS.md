---
content_hash: 94fa34852c283e089f0fe447cdbb6818a6a2bc152db5cffd77c95926464e84bb
fetched_at: '2026-06-29T00:06:17.010216+00:00'
page_id: '212903404'
product: rm
source: tdn-rm
title: DT_INTEGRACAO_PROTHEUS_ATIVOSFIXOS
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_INTEGRACAO_PROTHEUS_ATIVOSFIXOS
version: 124
---

# Integração de Ativos Fixos (Patrimônios) através da integração por Mensageria Única

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Gestão Patrimonial* |
| **Módulo:** | *BackOffice* |
|  |  |

## Descrição

Foi disponibilizado através do pacote de integração "TOTVS Educacional x BackOffice Protheus" a sincronização de cadastro de Ativos Fixos (Patrimônio) realizados no sistema Protheus.

Módulo Integração: **Ferramentas | Configurar**

As informações serão trafegadas utilizando a estrutura da mensagem única "Assets" na versão 1.001:

| Tag XML | Descrição | Tamanho | Campo | Observações |
| --- | --- | --- | --- | --- |
| CompanyId | Código da empresa |  | IPatrimonio.CodColigada |  |
| BranchId | Código da filial |  | IPatrimonio.CodFilial |  |
| CompanyInternalId | InternalId da chave completa de empresa do produto |  |  |  |
| Code | Código do ativo | 25 |  |  |
| InternalId | InternalId do Code |  |  |  |
| PropertyCode | Código do bem | 25 | IPatrimonio.CodPatrimonio |  |
| ItemNumber | Número do item dentro do código do bem. |  |  | Obs.: O TOTVS Gestão Patrimonial não irá utilizar esse campo. |
| PurchaseDate | Data de aquisição do bem |  | IPatrimonio.DataAquisicao |  |
| Description | Descrição sintética do bem | 240 | IPatrimonio.Descricao |  |
| Amount | Quantidade do ativo |  | IPatrimonio.Quantidade |  |
| CardAssets | Número da placa de patrimônio |  | IPatrimonio.Patrimonio |  |
| StatusAssets | Status atual do ativo |  | IPatrimonio.Ativo | | Mensagem XML | TOTVS Gestão Patrimonial | | --- | --- | | 1 - Ativo | 1 - Ativo | | 2 - Inativo | 0 - Inativo | |
| VendorCode | Código do fornecedor |  | IPatrimonio.CodFornecedor |  |
| VendorInternalId | InternalId do VendorCode |  |  |  |
| ListOfSalesAndValuesAssets | Saldos e valores | | | |
| SalesAndValuesItem | | | | |
| InternalId | InternalId do saldo e valores - chave do filho |  |  |  |
| TypeAssets | Tipo do ativo |  |  | | Mensagem XML | TOTVS Gestão Patrimonial | | --- | --- | | 01 - Aquisição |  | | 02 - Reavaliação |  | | 03 - Adiantamento |  | | 04 - Lei 8.200 |  | | 05 - Reavaliação Negativa |  | | 06 - Depr. Acelerada Específica |  | | 07 - Depr. Acelerada |  | | 08 - Depr. Incentivada Positiva |  | | 09 - Depr. Incentivada Reversa |  | | 10 - Depreciação Gerencial com Metodo Linear |  | | 11 - Valor Recuperável de Ativo |  |   Obs.: O TOTVS Gestão Patrimonial não irá utilizar esse campo. |
| TypeOccurrence | Tipo de ocorrência |  | IPatrimonio.TipoOcorrencia | | Mensagem XML | TOTVS Gestão Patrimonial | | --- | --- | | 0 - Ativo | 0 - Sem Ocorrência | | 1 - Baixado: Ativo vendido, doado ou sucateado. | 99 - Baixado no Periodo | |
| Observation | Observação (Histórico) |  | IPatrimonio.Observacoes |  |
| AssetAccount | Conta contábil do bem | 20 |  |  |
| CostCenterCode | Centro de custo |  | IPatrimonio.CodCentroCusto |  |
| CostCenterInternalId | InternalId do CostCenterCode |  |  |  |
| DepreciationStartDate | Data início de depreciação |  |  |  |
| CurrencyCode | Código da moeda |  |  |  |
| CurrencyInternalId | InternalId do CurrencyCode |  |  |  |
| OriginalValueCurrency | Valor original moeda |  |  |  |
| AnnualRateCurrencyDepreciation | Taxa anual de depreciação na moeda |  |  |  |
| MethodDepreciation | Método de depreciação |  |  | | Mensagem XML | TOTVS Gestão Patrimonial | | --- | --- | | 1 - Linear |  |   Obs.: O TOTVS Gestão Patrimonial não irá utilizar esse campo. |
| BalanceType | Tipo de saldo |  |  | | Mensagme XML | TOTVS Gestão Patrimonial | | --- | --- | | 0 - Orcado |  | | 1 - Real |  | | 2 - Previsto |  | | 3 - Gerencial |  | | 4 - Empenhado |  | | 9 - Pre-Lancamento |  |   Obs.: O TOTVS Gestão Patrimonial não irá utilizar esse campo. |
| IsCalculated | Informa se o ativo sofrerá contabilização |  |  |  |
| BalanceDepreciation | Valor da depreciação acumulada |  |  |  |

##### **Importante:**

Os ativos cadastrados no sistema Protheus serão sincronizados com o TOTVS Gestão Patrimonial e disponibilizados para consultas.

As operações de inserção, alteração e exclusão devem ser realizadas no Protheus.

Os patrimônios cadastrados podem ser visualizados em: **BackOffice | Gestão Patrimonial | Cadastros | Patrimônio**

Com a instalação da integração, o TOTVS Gestão Patrimonial passará a utilizar o parâmetro interno "**NAOVALIDAMASCARA**" ativado. Ele será utilizado para que o sistema TOTVS Gestão Patrimonial ignore a máscara cadastrada em seus parâmetros e passe a aceitar o código enviado da Integração independente da forma cadastrada. Esse parâmetro é definido por Coligada, por isso, caso haja a ativação de outras coligadas após a instalação, esse parâmetro deve ser inserido na "**IPARAMETROS**" manualmente.

Para cadastro do Patrimônio é exigido pelo sistema a informação de um "Grupo de Patrimônio", porém essa não é fornecido pelo XML da mensagem de integração. Será utilizado um parâmetro de integração para a definição de um grupo padrão, por coligada, para o cadastro desses Patrimônios.

Os parâmetros de integração serão incluídos juntamente com a instalação da integração e o parâmetro "**IDGRUPOPATRIMONIO**" deverá ser configurado com o id do grupo padrão para a coligada referente. Caso hajam ativações de coligadas após a instalação da integração, deve ser incluso novo parâmetro para a nova coligada com o id do grupo referente, manualmente.

## Procedimento para Implantação

1. No arquivo de configuração do Host, inserir as tags "**DefaultDB**" e "**HttpPort**" para definição do Alias e da porta de comunicação que serão utilizados pelo Webservice da integração.  

   ***<add key="DefaultDB" value="NomeAlias" />***  
    ***<add key="HttpPort" value="8051" /> (Porta Padrão)***
2. Reiniciar o Host para que as alterações tenham efeito
3. Instalar o pacote de integração "***TOTVS Educacional x BackOffice Protheus***" através do processo de configuração de integração.
4. Configurar e ativar a integração para que reconheça a mensagem "Assets".
5. Configurar os parâmetros da integração instalados nos anexos da visão de integraçãoes: "**Parâmetros de Integração**"

#### Manual da integração

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. TOTVS Gestão Patrimonial  
   1. Os parâmetros abaixo não poderão ser utilizados, quando houver integração com o BackOffice Protheus (Deverão estar desmarcados):
      1. "Preencher nº do patrimônio com zeros a esquerda"
      2. "Código de patrimônio único"
      3. "Geração do nº do patrimônio = código do patrimônio"
      4. "Mensagem de valor mínimo imobilizado no cadastro de patrimônios"
2. Integração 
   1. Integração "TOTVS Educacional x BackOffice Protheus":
      1. O campo "Ativo?" deve ser marcado para ativar a integração
      2. O campor "URL WebService" deve ser preenchido com o endereço WSDL do webservice do Protheus.
      3. O campo "Usuário Autenticação" deve conter o usuário de acesso as funcionalidades do WebService informado.
      4. O campo "Senha Autenticação" deve conter a senha do usuário informado.
   2. Parâmetros da integração "TOTVS Educacional x BackOffice Protheus":
      1. Parâmetro "IDGRUPOPATRIMONIO" com o ID do grupo de patrimônio que será utilizado para cadastrar os Patrimônios.

divs
