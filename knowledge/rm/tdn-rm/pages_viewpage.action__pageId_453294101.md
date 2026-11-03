---
content_hash: 5ec603d8f79b524223f2d628a88f667843d092a710208a32ee242ef1f454efcc
fetched_at: '2026-06-29T00:10:11.865245+00:00'
page_id: '453294101'
product: rm
source: tdn-rm
title: Portal do Cliente - PDC - Situação Financeira x Protheus
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=453294101
version: 10
---

**Situação Financeira**

---

**Descrição**

A funcionalidade de situação financeira integrada ao Protheus do PDC (Portal do Cliente) permite ao usuário selecionar um relatório default com layout de boleto único para impressão de segunda via de boleto.

Esta funcionalidade permite também, caso o usuário não utilize um layout de boleto único, a opção de associar um layout de boleto por banco específico através do Default de Banco. Neste caso o cliente deverá configurar nos parâmetros de integração TOTVS Incorporação x Protheus os parâmetros necessários para acesso aos serviços REST do Protheus para acesso ao serviço de consulta banco do título no Protheus.

A seguir serão apresentadas as duas funcionalidades de impressão de segunda via de boleto quando integrado ao back office Protheus.

|  |  |
| --- | --- |
|  | Como Fazer |

---

**Layout de boleto único**

Na opção de layout de boleto único o usuário informa nos parâmetros do TOTVS Incorporação qual o relatório com layout de boleto único que será utilizado para impressão de segunda via de boleto.

O Parâmetro está disponível no seguinte endereço: Projetos → Incorporação → Ambiente → Parâmetros → TOTVS Incorporação → Portal do Cliente → Relatórios

Com este relatório informado todos os boletos gerados pelo PDC utilizaram este layout para impressão de segunda via.

**Layout de boleto específico por banco**

Na opção de layout de boleto específico por banco o usuário não deverá informar o relatório de layout de boleto único conforme informado anteriormente. Assim o sistema irá procurar através do serviço do Protheus qual o banco associado ao título e depois procurar no respectivo banco do RM qual o relatório de layout de boleto associado ao banco para impressão da segunda via de boleto. Ou seja, O sistema trabalhará com um layout específico por banco. Desta forma o usuário poderá definir um layout específico por instituição financeira.

Observação: Caso o usuário mantenha o relatório de layout de boleto único informado, o sistema continuará a utilizar ele para impressão de todas as segundas via de boleto. Para que a funcionalidade de layout de boleto específico por banco seja utilizada o usuário deve remover o boleto default para que o sistema utiliza a outra opção.

Para que o titulo financeiro seja exibido no PDC ele deve ser enviado para Borderô no Protheus, desta forma o usuário pode imprimir a segunda via no PDC.

**Parâmetro de Integração TOTVS Incorporação x Protheus**

Para acesso ao serviço de consulta ao banco do titulo financeiro no Protheus o usuário deverá informar o endereço do serviço Protheus e um Usuário e Senha para autenticação, conforme apresentado a seguir. Todos os parâmetros devem ser da coligada global, independente de empresa.

PRJ\_URLAPIRESTPROTHEUS = Endereço do serviço Protheus  
PRJ\_USRAPIRESTPROTHEUS = Usuário para autenticação do serviço  
PRJ\_PASSAPIRESTPROTHEUS = Senha para autenticação do serviço

Após esta configuração o usuário precisará associar o relatório de layout do boleto por banco através do cadastro de banco, conforme apresentado na imagem a seguir:

O relatório associado receberá os parâmetros de chave do título e chave interna de integração conforme a seguir, caso o usuário crie estes parâmetros no relatório.

Caso contrário estes campos serão passados como filtro para o relatório de layout do boleto.

XXF\_INTVAL = Para acesso ao título pela tabela XXF e campo de valor integração (chave interna).

E1\_MSEMP, E1\_FILIAL, E1\_PREFIXO, E1\_NUM, E1\_PARCELA, E1\_TIPO = Para acesso direto a tabela SE1 e chave do titulo financeiro (chave primária).

Observação: O usuário na criação do relatório deverá fazer o acesso ao banco de dados do Protheus e a tabela de titulo a receber da respectiva empresa desejada.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

A funcionalidade de layout de boleto específico por banco esta disponível apenas a partir da versão 12.1.23

Esta funcionalidade depende da integração TIN x Protheus com EAI 1
