---
content_hash: 8684c131a499a5b183cfd20166fef7ed491b904cc8f49f6a38627bd85b2c5f3f
fetched_at: '2026-06-29T00:08:56.125238+00:00'
page_id: '351376245'
product: rm
source: tdn-rm
title: Evento S-2190
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-2190
version: 7
---

Leiautes1Leiaute 2.5.00

Mapeamento dos campos para o leiaute 2.5.00

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Registro eSocial** | **Campo eSocial** | **Tabela RM** | **Coluna RM** | **Informações do calculo** |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| infoRegPrelim | cpfTrab |  |  | PPESSOA.CPF |
| infoRegPrelim | dtNascto |  |  | PPESSOA.DTNASCIMENTO |
| infoRegPrelim | dtAdm |  |  | Recupera o valor do campo PFUNCPRELIMINAR.DATAADMISSAO |

true2Leiaute S-1.0

Mapeamento dos campos para o leiaute S-1.0

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Registro eSocial** | **Campo eSocial** | **Tabela RM** | **Coluna RM** | **Informações do calculo** |
| ideEvento | indRetif |  |  | Conforme manual |
| ideEvento | nrRecibo |  | PROTOCOLO |  |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| infoRegPrelim | cpfTrab |  |  | PPESSOA.CPF |
| infoRegPrelim | dtNascto |  |  | PPESSOA.DTNASCIMENTO |
| infoRegPrelim | dtAdm |  |  | Recupera o valor do campo PFUNCPRELIMINAR.DATAADMISSAO |
| infoRegPrelim | matricula | PFUNCPRELIMINAR | MATRICULAESOCIAL |  |
| infoRegPrelim | codCateg | PFUNCPRELIMINAR | CODCATEGORIAESOCIAL |  |
| infoRegPrelim | natAtividade |  |  | Caso PFUNCPRELIMINAR.ESOCIALNATATIVIDADE seja              1 - Trabalho Urbano, caso contrário             2 - Trabalho Rural |
| infoRegCTPS | CBOCargo |  |  |  |
| infoRegCTPS | vrSalFx | PFUNCPRELIMINAR | SALARIO |  |
| infoRegCTPS | undSalFixo |  |  | Caso PFUNCPRELIMINAR.CODRECEBIMENTO seja                             H - Horista; ou P - Professor Horista, retorna 1 - Por Hora;                            D - Diarista, retorna 2 - Por Dia;                            S - Semanalista, retorna 3 - Por Semana;                            Q - Quinzenalista, retorna 4 - Por Quinzena;                            M - Mensalista ou O - Outros, retorna 5 - Por Mês;                            T - Tarefeiro, retorna 6 - Por Tarefa;                            O - Outros, retorna 7 - Não se aplica; |
| infoRegCTPS | tpContr |  |  | Caso PFUNCPRELIMINAR.TPCONTR seja                                    1 - Prazo indeterminado;                                    2 - Prazo determinado, definido em dias;                                    3 - Prazo determinado, vinculado à ocorrência de um fato; |
| infoRegCTPS | dtTerm | PFUNCPRELIMINAR | FIMPRAZOCONTR |  |
