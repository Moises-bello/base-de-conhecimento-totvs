---
article_id: 36136468000407
category: Gestão organizacional
content_hash: 4e78852aa03da4d6937260a0901a7daf24755385f31f79512419924799dd22cc
fetched_at: '2026-06-28T22:47:22.176277+00:00'
product: rm
section_id: 1500000861422
source: central-rm
title: 'RH - RM - RHU - Processo Trabalhista: Tabelas responsáveis por armazenar os
  cadastros para criação de Relatórios'
type: support-article
updated_at: '2026-06-01T14:06:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36136468000407-RH-RM-RHU-Processo-Trabalhista-Tabelas-respons%C3%A1veis-por-armazenar-os-cadastros-para-cria%C3%A7%C3%A3o-de-Relat%C3%B3rios
---

![relogio_tempo_leitura_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36136472572183) Tempo aproximado para leitura: 00:02:00 min  
  
**Dúvida**  
Quais as tabelas armazenam os dados referente ao cadastro dos Processos Trabalhistas?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - **12.1.34**e **superiores**.  
  
**Solução**  
Segue abaixo relação das tabelas que armazenam os dados: 

|  |  |
| --- | --- |
| **Nome tabela** | **Descrição** |
| VPROCCALCTRIB | Calculo tributos trabalhistas - 2501 |
| VPROCCRCONTRIB | Contribuição Social - 2501 |
| VPROCESSOCOMPL | Campos Compl. Processos Trab. |
| VPROCESSOTRABALHISTA | Processo Trabalhista ESocial - 2500 |
| VPROCESSOTRIBUTOS | Tributos do Processo - 2501 |
| VPROCTRABABONO | Identificação do(s) ano(s)-base em que houve indenização substitutiva de abono salarial. |
| VPROCTRABDADOSCOMPL | Dados complementares Processo Trabalhista - 2500 |
| VPROCTRABDEPENDENTE | Dependente do Trabalhador - 2500 |
| VPROCTRABINFOCONTRATO | Informações do Contrato do Trabalhador - 2500 |
| VPROCTRABINFOCONTRATOCOMPL | Informações complementares do Processo Trabalhista - 2500 |
| VPROCTRABINFOVINC | Informações do Vínculo Trabalhista - 2500 |
| VPROCTRABMUDCATEGATIV | Tabela de mudança de categoria da atividade - 2500 |
| VPROCTRABOBSERVACOES | Observações do vínculo - 2500 |
| VPROCTRABPERIODO | Período das bases de cálculo - 2500 |
| VPROCTRABREMUNERACAO | Remuneração e periodicidade - 2500 |
| VPROCTRABTRABALHADOR | Trabalhador do Processo Trabalhista - 2500 |
| VPROCTRABUNICIDADECONTRATUAL | Unicidade Contratual - 2500 |
| VPROCTRIBBENEFPEN | Informação das deduções suspensas por dependentes e beneficiários da pensão alimentícia |
| VPROCTRIBDEDDEPEN | Dedução do rendimento tributável relativa a dependentes. |
| VPROCTRIBDEDSUSP | Detalhamento das deduções com exigibilidade suspensa. |
| VPROCTRIBIDEADV | Identificação dos advogados. |
| VPROCTRIBINFODEP | Informações de dependentes não cadastrados pelo S-2200/S-2205/S-2300. |
| VPROCTRIBINFOIRCOMPLEM | Informações relacionadas à retenção na fonte, aos rendimentos tributáveis e não tributáveis, deduções e/ou isenções, etc., de acordo |
| VPROCTRIBINFOPROCRET | Informações de processos relacionados a não retenção de tributos ou a depósitos judiciais. |
| VPROCTRIBINFORRA | Informações complementares relativas a Rendimentos Recebidos Acumuladamente - RRA. |
| VPROCTRIBINFOVALORES | Informações de valores relacionados a não retenção de tributos ou a depósitos judiciais. |
| VPROCTRIBIRRF | Tributo IRRF - 2501 |
| VPROCTRIBPENALIM | Informação dos beneficiários da pensão alimentícia. |
| VPROCTRIBTRABALHADOR | Tributos do trabalhador - 2501 |

No caso de telas que utilizam PO UI não é possível identificar o entidade e campo conforme ocorre com as demais telas (.Net) do sistema.   
   
**Importante**

Caso desejem consultar tabelas do sistema e campos, poderão realizar SELECT na entidade GDIC.

**Saiba Mais**

Para maiores informações, acesse:

- [RH - RM - RHU - eSocial: S-2500 - Mapeamento dos campos para geração do evento S-2500](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18256276341783)

- [RH - RM - RHU - eSocial: S-2501 - Mapeamento dos campos para geração do evento S-2501](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18863423016855)
