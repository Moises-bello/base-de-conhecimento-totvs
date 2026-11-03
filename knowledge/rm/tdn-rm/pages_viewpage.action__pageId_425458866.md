---
content_hash: c024f2684709081f2c388dc3ed868f28ef00233df868c24f2a4d86c3f6f07349
fetched_at: '2026-06-29T00:09:32.524135+00:00'
page_id: '425458866'
product: rm
source: tdn-rm
title: Layout do Arquivo Exportação de Candidatos para Gráfica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458866
version: 2
---

Este arquivo será gerado pelo sistema através do processo de exportação de candidato.

|  |  |  |
| --- | --- | --- |
| **Coluna** | **Descrição** | **Obrigatório?** |
| CODCOLIGADA | Código da coligada | Sim |
| IDPS | Código do processo seletivo | Sim |
| IDETAPA | Código da etapa | Sim |
| NUMERO\_CARTAO | Número do cartão resposta | Sim |
| NUMERO\_INSCRICAO | Número da inscrição | Sim |
| NOME | Nome do candidato | Sim |
| RG | Número da carteira de identidade | Sim |
| UF\_RG | Estado da carteira de identidade (MG, PR etc.) | Não |
| ORGAO\_RG | Órgão emissor da carteira de identidade | Não |
| LINGUA\_ESTRANGEIRA | Opção de língua estrangeira | Sim |
| SALA | Descrição da sala de prova | Sim |
| PRIMEIRA\_OPCAO | Área de interesse ofertada escolhida como primeira opção | Sim |
| TURNO\_PRIMEIRA\_OPCAO | Turno da área de interesse escolhida como primeira opção | Sim |
| SEGUNDA\_OPCAO | Área de interesse ofertada escolhida como segunda opção | Não |
| TURNO\_SEGUNDA\_OPCAO | Turno da área de interesse escolhida como segunda opção | Não |

Exemplo de uma linha do arquivo txt: CODCOLIGADA;IDPS;IDETAPA;NUMERO\_CARTAO;NUMERO\_INSCRICAO;NOME;RG;LINGUA\_ESTRANGEIRA;SALA;PRIMEIRA\_OPCAO;TURNO\_PRIMEIRA\_OPCAO 1;28;37;;13;CARLOS VICENTINO MORAES;;;2º Andar - Sala 01;Ciência da Computação;
