---
article_id: 4419405622679
category: RH - Migração
content_hash: d6fcce641d7556dde54918791eb4c9eb2b330ba93f748a45aa9cdc761d1d3e20
fetched_at: '2026-06-28T22:43:46.730402+00:00'
product: protheus
section_id: 360001597531
source: central-protheus
title: RH - Linha Protheus - GPE - RHIMP01 - Migrador Logix / Protheus - Pré-Requisitos
  para migração dos dados
type: support-article
updated_at: '2022-01-18T11:46:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4419405622679-RH-Linha-Protheus-GPE-RHIMP01-Migrador-Logix-Protheus-Pr%C3%A9-Requisitos-para-migra%C3%A7%C3%A3o-dos-dados
---

**Dúvida** **RHIMP01** - Migrador Logix / Protheus - Pré-Requisitos para migração dos dados  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 11.0  
  
**Solução**- Sistema **Logix, a partir da versão 10.02** e sistema **Protheus, a partir da versão 11.0**  
  
- Informe no cadastro de Empresas Logix -**LOG00083**, a Empresa\Filial Protheus que refere-se a empresa Logix. Para informar estes valores no LOG00083, preencha com o **valor S**, no cadastro de Parâmetro Logix  
  
- **LOG00087** o parâmetro que encontra-se em: Administração **Logix -> Controle Geral -> Integração entre Sistemas** - Permite informar empresa/filial externa no cadastro de empresas  
  
- O Sistema **Protheus deve ser instalado em um** **SGBD - Sistema Gerenciador de Banco de Dados**. Não poderá ser utilizado este processo em arquivos DBF  
  
- O **código da Matrícula do Funcionário no Sistema Logix pode conter até 8 posições**. No Protheus este campo é r**estrito a 6 posições**. Caso este campo no Logix for superior a 6 posições, deve ser **redefinido este código** para ser gerado sequencialmente ou gerar uma codificação, sendo composta por uma máscara a partir da matrícula existente  
  
- Se o código do **Centro de Custo** que vier no arquivo **tiver mais de 9 posições**, deve ser **alterado no Configurador Protheus para aumentar o tamanho do campo para até 10 posições**. Somente será importado o registro para a tabela SRA - Funcionários, se o tamanho do campo no Protheus for suportado pelo tamanho do campo vindo no arquivo texto  
  
- Caso venha o **valor da Área e Linha de Negócio do sistema Logix**, que será relacionada com o campo Item Contábil do Funcionário, deverá habilitar o parâmetro **MV\_ITMCLVL** para utilizar o conceito de Item Contábil no Protheus  
  
- O **Banco e a Agência** que são feitos os **depósitos de salário** do funcionário **devem ser previamente cadastrados no sistema Protheus pelo usuário**, pois não haverá integração deste cadastro  
  
- O **Banco e a Agência** que são feitos os **depósitos de FGTS** do funcionário **devem ser previamente cadastrados no sistema Protheus pelo usuário**, pois não haverá integração deste cadastro  
  
- Verifique se os **códigos de Categorias Salariais cadastrados no Logix** são compatíveis com os códigos fixos do Protheus. Caso não seja, o usuário deve cadastrar **DE-PARA manual no Logix**, através do programa **VDP10141 – Cadastro de DE-PARA** Geral, para enviar o código que é referente ao Protheus  
  
- Na importação no **sistema Protheus não está previsto o conceito de Gestão de Corporativa**. Dessa forma, deve-se utilizar somente o conceito de Empresa/Filial  
  
- No Protheus, **devem ser retiradas as seguintes validações** no arquivo SX3, campo X3\_VALID, da tabela SRA, devido haver restrições na importação de funcionários demitidos:  
  
1 - Campo **RA\_DEMISSA**: Retirar a validação: ChkDtDe(M->RA\_ADMISSA,M->RA\_DEMISSA) .and. ( Empty( M->RA\_DEMISSA ) .or. fChkDtDem(M->RA\_DEMISSA) )  
  
2 - Campo **RA\_SITFOLH**: Retirar a validação: If(Inclui.And.M->RA\_SITFOLH#" ",.F.,EXISTCPO("SX5","31"+M->RA\_SITFOLH))  
  
3 - Campo **RA\_RESCRAI**: Retirar a validação: Vazio() .Or. If(Inclui,.F.,EXISTCPO("SX5","27"+M->RA\_RESCRAI))  
  
4 - Campo **RA\_OPCAO**: Retirar a validação: NaoVazio() .And. ChkDtOp(M->RA\_ADMISSA,M->RA\_OPCAO)  
  
5 - Campo **RA\_DESCCC**: Alterar a validação:

oDe:IF(Inclui,"",fDesc("SI3",SRA->RA\_CC,"I3\_DESC",,SRA->RA\_FILIAL))

oPara:IF(Inclui,"",fDesc("CTT",SRA->RA\_CC,"CTT\_DESC01",,SRA->RA\_FILIAL))  
  
- Para as implantações em que for realizada a migração do Ponto Logix para o Protheus, deve ser realizado o seguinte procedimento:

• **Criar manualmente a Regra de apontamento 01**, através do programa de PONA060, para que seja feita a inicialização de todos os funcionários com este código de regra. **Não haverá migração de Regras de Ponto entre os dois sistemas**  
  
• Por default, todos os funcionários também **serão incluídos com a sequência de turno 01**

- Antes de proceder com a migração de dados do Logix, toda a estrutura da tabela de empresas, tabelas do SIGAGPE, devem estar devidamente configuradas e criadas  
  
- O usuário deve fazer as compatibilizações do eSocial Protheus, através do programa RHUPDMOD para versão 11, opção 218  para os pacotes 1, 2 e 3, ou UPDDISTR para versão 12, assim o dicionário de dados ficara compatível para rodar o Migrador **RHIMP01**.
