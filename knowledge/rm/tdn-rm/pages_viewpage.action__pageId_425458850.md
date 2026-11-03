---
content_hash: c4c0d80b3e82bd6855887781953385a5a99206f8be094c5ec955f6dfccfcb4cf
fetched_at: '2026-06-29T00:09:32.448473+00:00'
page_id: '425458850'
product: rm
source: tdn-rm
title: Tag para complemento de Histórico Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458850
version: 19
---

---

As tag's são recursos que permitem ao usuário adicionar alguma informação acadêmica ou financeira específica do TOTVS Gestão Educacional no complemento histórico da contabilização por competência ou por caixa no TOTVS Gestão Contábil.

Segue abaixo a listagem das tag's referente ao TOTVS Gestão Educacional com sua descrição e recurso onde pode ser utilizada.

|  |  |  |  |
| --- | --- | --- | --- |
| **Tag** | **Descrição** | **Contabilização por Competência** | **Contabilização por Caixa** |
| [ALU.C] | RA do Aluno | Usa | Usa |
| [ALU.D] | Nome do Aluno | Usa | Usa |
| [PRL.C] | Código do Período Letivo | Usa | Usa |
| [CNT.C] | Código do Contrato | Usa | Usa |
| [COM.D] | Competência | Usa | Não usa\* |
| [CUR.C] | Código do Curso | Usa | Usa |
| [CUR.D] | Nome do Curso | Usa | Usa |
| [SER.C] | Código da Série / Habilitação | Usa | Usa |
| [SER.D] | Nome da Série / Habilitação | Usa | Usa |
| [BOL.CX] | Código da Bolsa | Usa | Usa |
| [BOL.DX] | Nome da Bolsa | Usa | Usa |
| [BOL.VX] | Valor da Bolsa | Usa | Usa |
| [PAR.C] | Número da Parcela | Não usa | Usa |
| [COT.C] | Número da Cota | Não usa | Usa |

* Tag [CNT.C]  liberado nos patch's **12.1.32.315, 12.1.33.284, 12.1.34.185, 12.1.2205.124**
* Tag [ALU.D] caso o Nome Social esteja preenchido, a tag será preenchida com essa informação

**\***Na contabilização por *regime de caixa*, para informar a competência no complemento de histórico, use a variável [MDC], disponível no cadastro do evento contábil doTOTVS Gestão Financeira.

A letra 'X' das variáveis de Bolsa serve para indicar qual Bolsa será utilizada.

Vamos supor que no contrato do aluno existam 2 bolsas associadas. Para que as duas bolsas sejam referenciadas no complemento do histórico, inclua a variável duas vezes e substitua o 'X' número de ordem da bolsa.

**Exemplo:**   
Bolsas associadas no contrato do aluno: **'FIES'** e **'Aproveitamento'**Para que no lançamento contábil seja impresso o nome das duas Bolsas e seus respectivos valores, inclua no complemento uma variável para cada Bolsa e indique o número correspondente, assim: [BOL.D1] = [BOL.V1] - [BOL.D2] = [BOL.V2]

A ordem da Bolsa irá respeitar o código da Bolsa.   
As duas Bolsas associadas são:  
- Bolsa 'FIES' de código 5 com valor de 20,00  
- Bolsa 'Aproveitamento' de código 10 com valor de 30,00

Desta forma, no complemento do histórico onde o 'X' foi substituído por 1, serão apresentados os dados referentes à Bolsa 'FIES'. E onde o 'X' foi substituído por 2, serão apresentados os dados referentes à Bolsa 'Aproveitamento', assim:  
[BOL.D1] = [BOL.V1] - [BOL.D2] = [BOL.V2]   
FIES = 20,00 - Aproveitamento = 30,00
