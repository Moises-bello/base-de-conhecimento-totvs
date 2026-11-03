---
article_id: 35314721022103
category: Escrita Fiscal - Configurador de Tributos
content_hash: 948edcd45009ed4ead9df149062f80b794610410c64a0e0447c7684e0827a937
fetched_at: '2026-06-28T22:39:17.537058+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Quais
  tabelas fazem parte do Configurador de Tributos?
type: support-article
updated_at: '2025-11-04T22:12:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35314721022103-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Quais-tabelas-fazem-parte-do-Configurador-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35314764801815) Tempo aproximado para leitura: **00:10 min**  
  
**Dúvida**  
Quais são as principais tabelas que compõem o Configurador de Tributos no Protheus?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - A partir da versão 12.1.2210  
  
**Solução**  
O Configurador de Tributos do Protheus utiliza diversas tabelas para controle de perfis tributários, regras de cálculo, apuração, e outras informações fiscais. Abaixo está a lista das principais tabelas utilizadas:

| Código | Descrição |
| --- | --- |
| F20 | Perfis Tributários |
| F21 | Perfil Tributário Orig./Dest. |
| F22 | Perfil Trib. de Participante |
| F23 | Perfil Tributário de Operação |
| F24 | Perfil Tributário de Produto |
| F25 | Perfil Produto x Origem |
| F26 | Perfil Tipo de Operação |
| F27 | Regra de Base de Calculo |
| F28 | Regra de Alíquota |
| F29 | Unidade de Referencia Fiscal |
| F2A | Valores da URF |
| F2B | Regra Tributária |
| F2C | Tributos De/Para |
| F2D | Tributos Genéricos Calculados |
| F2E | Cadastro de Tributo |
| F2F | Títulos de Tributos x NF |
| F2G | Regra de Apuração |
| F2H | Apuração Tributo Genérico |
| F2I | Saldos Apuração Trib. Genérico |
| F2J | Resumo Apuração por Regra |
| F2K | Resumo Analítico Trib Gen |
| F2L | Títulos Apuração Trib. Gen. |
| F2M | Ajustes Apuração Trib Gen |
| F2N | Regras de Título da Apuração |
| CIN | Cadastro de Fórmulas |
| CIO | Código de Serviço Municipal do perfil de operações |
| CIQ | Tabela Progressiva |
| CIR | Itens Tabela Progressiva |
| CIS | Cabeçalho da Regra de NCM |
| CIT | Tributo x Regra |
| CIU | Regra Adicional de Tributo por NCM |
| CIV | Regra por Dependentes |
| CIX | Cabeçalho da Regra de ISS |
| CIY | Alíquota de ISS por Município |
| CJ0 | CST - Cabeçalho |
| CJ1 | CST - Item |
| CJ2 | Regra Escrituração |
| CJ3 | Escrituração por item |
| CJ4 | Regra para Guia de Recolhimento |
| CJ5 | Regra de Código de Receita |
| CJ6 | Código de Receita por Estado |
| CJ7 | Mod. Documento Código Receita |
| CJ8 | Cadastro de Mensagem |
| CJ9 | Cabeçalho Regra de Ajuste de Lançamento |
| CJA | Itens - Regra de Ajuste de Lançamento |
| CJL | Controle de Mensagens Decodificadas |

## Observação importante

Antes de realizar o compartilhamento dessas tabelas, é necessário realizar uma análise detalhada na base de dados para garantir integridade e segurança das informações.

**Documentações relacionadas:**  
[CFGTRIB - Configurador de Tributos](https://tdn.totvs.com/display/PROT/CFGTRIB+-+Configurador+de+Tributos)

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Como compartilhar as regras dos perfis entre filias no FISA170?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23377972562455-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-compartilhar-as-regras-dos-perfis-entre-filias-no-FISA170)
