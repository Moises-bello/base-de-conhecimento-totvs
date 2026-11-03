---
content_hash: f14ba73a71b3beaf6d9453b42314e519998484599a0d52ecdc6ed8ad0b0e49a3
fetched_at: '2026-06-29T00:12:13.346469+00:00'
page_id: '954083733'
product: rm
source: tdn-rm
title: Campos da API
type: documentation
url: https://tdn.totvs.com/display/LRM/Campos+da+API
version: 26
---

A partir das versão **12.1.2510**: A propriedade **CodCCT** foi adicionada, e as propriedades **numDirecaoAces**, **codIdFeder** e **codUnidExtChave** deixaram de ser obrigatórias.  
  
A API recordClockMarkings poderá receber no método POST os seguintes parâmetros: 

|  |  |  |  |
| --- | --- | --- | --- |
| Campo | Tipo | Obrigatório | Descrição |
| codIdPrevidSocial | string | Não | Código CTPS (Carteira de Trabalho e Previdência Social) |
| codRelogioExtChave | string | Sim | Código da coligada mais o código do Terminal de Coleta (utilizar o ; como separador) |
| numDirecaoAces | int | Não | Natureza da batida no Rep.  0-Entrada, 1-Saída do relógio de ponto.  1-Entrada e 2-Saída relógio do refeitório.  Observação: Na importação de batidas essa natureza é desconsidera. |
| codFuncMSA | string | Sim | Chapa/Matricula do Funcionário |
| codIdFeder | string | Não | Código da federação |
| codHash | string | Não | Código Hash |
| logImportProdut | int | Não | Indica se a batida foi importada. 0 - não importada, 1 - importada |
| codLote | string | Não | Código do lote |
| codNSR | int | Sim | Número Sequencial de Registro único por dispositivo  para Rep's do tipo C, P e A. Demais valor fixo 0. |
| codPisMSA | string | Sim para Rep's da portaria 1510 | Número do PIS do funcionário |
| valPerfAces | int | Não | Código Perfil de acesso. Valor fixo 0. |
| datMarcacAces | string | Sim utilizar o formato data | Data da batida |
| numHorarMarcacAces | int | Sim | Horário da marcação em segundos |
| codRep | string | Sim | Código de fabricação do relógio ou número de registro no INPI- REP-P |
| codUnidExtChave | string | Não | Código da coligada mais código da seção do funcionário (utilizar o ; como separador) |
| codUsuarExtChave | string | Sim | Código da coligada mais código da chapa do funcionário (utilizar o ; como separador) |
| codFuso | string | Sim | Fuso horário |
| codCPF | string | Sim para Rep's da portaria 671 | CPF do funcionário |
| numVersLayout | int | Não | REP's portaria 1510 valor - 1, REP's portaria 671 valor - 3. |
| InscrEmp | string | Não | CNPJ ou CPF do empregador |
| CodCCT | string | Não | Código do Acordo Coletivo |

**Alterações à partir da versão 12.1.2502.262:**

|  |  |  |  |
| --- | --- | --- | --- |
| codFuncMSA | string[] | Sim | Chapa(s)/Matrícula(s) do Funcionário |
| codUsuarExtChave | string[] | Sim | Código(s) de coligada(s) mais código(s) de chapa(s) do funcionário (utilizar o ; como separador) |

**Importante:**

Quando for REP-A o campo Codrep deve ter o CodCCT.
