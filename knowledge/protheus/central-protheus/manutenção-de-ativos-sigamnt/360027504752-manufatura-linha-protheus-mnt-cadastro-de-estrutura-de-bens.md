---
article_id: 360027504752
category: Manutenção de Ativos (SIGAMNT)
content_hash: d809590a66ef469eacf4df515769e3e71a3b41ebc5a5c82ebb434c148ece2b4d
fetched_at: '2026-06-28T22:42:32.830784+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Cadastro de Estrutura de Bens
type: support-article
updated_at: '2024-10-25T17:48:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027504752-Manufatura-Linha-Protheus-MNT-Cadastro-de-Estrutura-de-Bens
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como cadastrar **MNTA090 - Estrutura de Bens**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Versão 12  
  
**Solução**Para realização do cadastro da **Estrutura de Bens** no **SIGAMNT** é necessário a realização dos passos a seguir:  
  
**1. Cadastro de Bens - ST9**O **Bem CA001** pertence a família **VEIPES** e tipo modelo **AXOR**, temos também os Bens **PN001**, **PN002**, **PN003**, **PN004** com a família **PNEGRA** e modelo **0001**. Com base nas informações posteriores é criado o **Esquema padrão**.

|  |  |  |
| --- | --- | --- |
| **Bem** | **Família** | **Modelo** |
| CA001 | VEIPES | AXOR |
| PN001 | PNEGRA | 0001 |
| PN002 | PNEGRA | 0001 |
| PN003 | PNEGRA | 0001 |
| PN004 | PNEGRA | 0001 |

**2. Esquema Padrão - TQ0** / **TQ1**O objetivo do **Esquema padrão** é definir para uma **família** e **modelo** de um veículo, a quantidade de eixos, posição de cada componente na estrutura e principalmente a **Família de bens** a qual o componente que será inserido na estrutura pertencerá. Podemos identificar que o **Esquema padrão** criado corresponde a uma estrutura onde para **família/modelo** - **VEIPES** / **AXOR** existem dois eixos e para cada eixo dois pneus, os quais só permitirão ser adicionado pneus da família **PNEGRA**.

|  |  |  |
| --- | --- | --- |
| **Esquema** | **Modelo** | **Eixo** |
| VEIPES | AXOR | 2 |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Tipo de Eixo** | **Rodados** | **Loc Rod1** | **Família L1** | **Loc Rod2** | **Família L2** |
| DIRECIONAL | 2 | 1D | PNEGRA | 1E | PNEGRA |
| TRACIONADOR | 2 | 2D | PNEGRA | 2E | PNEGRA |

**3. Estruturas padrão - STC**Deve estar coerente com o **Esquema padrão**, que no caso do exemplo podemos identificar que os pneus pertencem a **família** **PNEGRA** e estão nas posições existentes no **Esquema padrão**, bem como o bem pai, também é da mesma **família/modelo** do **Esquema padrão**.

|  |  |  |
| --- | --- | --- |
| **Bem Pai** | **Componente** | **Localização** |
| VEIPES | PNEGRA | 1D |
| VEIPES | PNEGRA | 1E |
| VEIPES | PNEGRA | 2D |
| VEIPES | PNEGRA | 2E |

**4. Ordem de Serviço Corretiva - STJ**Incluir uma ordem de serviço para o bem pai da estrutura **CA001**, conforme o serviço no parâmetro de movimentação de pneus **MV\_NGSERPN - Indica o código de serviço utilizado para movimentação de pneus**.  
Após a inclusão, selecionar a **Ordem de Serviço** e no botão **Rodados**, incluir os pneus da família **PNEGRA**. Assim aparecem os componentes na Estrutura de Bens.  
  
**5. Estrutura de Bens -** **STC**Também deve estar coerente com o **Esquema padrão**, que no caso o exemplo podemos identificar que os pneus pertencem a família **PNEGRA** e estão nas posições existentes no **Esquema padrão**, bem como **CA001**, também é da mesma **família/modelo** do **Esquema padrão**.

|  |  |  |
| --- | --- | --- |
| **Bem Pai** | **Componente** | **Localização** |
| CA001 | PN001 | 1D |
| CA001 | PN003 | 1E |
| CA001 | PN002 | 2D |
| CA001 | PN004 | 2E |
