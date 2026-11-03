---
article_id: 35594764076055
category: eSocial
content_hash: 8df525dca45e851acee1f0e89af6cb315cfd5971eb9b8ae133889ac564bd8562
fetched_at: '2026-06-28T22:47:15.292637+00:00'
product: rm
section_id: 11645725240471
source: central-rm
title: 'RH - RM - RHU - Processo Trabalhista - FGTS Digital: Orientações consolidadas
  para recolhimento de FGTS em reclamatórias trabalhistas'
type: support-article
updated_at: '2026-06-22T16:59:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35594764076055-RH-RM-RHU-Processo-Trabalhista-FGTS-Digital-Orienta%C3%A7%C3%B5es-consolidadas-para-recolhimento-de-FGTS-em-reclamat%C3%B3rias-trabalhistas
---

⏱️ Tempo aproximado para leitura: 00:04:00 min

**Dúvida**  
Quais são as orientações quanto ao Recolhimento de FGTS em reclamatórias trabalhistas a partir da implantação do FGTS Digital?

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - **12.1.2506** e **superiores**.

**Solução**  
O FGTS Digital é o sistema, disponibilizado pelo Ministério do Trabalho e Emprego em conjunto com a Caixa Econômica Federal, responsável pela apuração, gestão e cobrança dos débitos de FGTS a partir das informações prestadas pelos empregadores no eSocial. A partir de sua implantação, o recolhimento do FGTS oriundo de Processos Trabalhistas — sejam sentenças proferidas pela Justiça do Trabalho, sejam acordos celebrados em Comissão de Conciliação Prévia (CCP) ou Núcleo Intersindical de Conciliação Trabalhista (NINTER) — passa a ter tratamento próprio dentro da plataforma.  
  
Esta documentação tem por objetivo consolidar, em linguagem orientativa, as regras e procedimentos gerais necessários para que o empregador cumpra corretamente suas obrigações de FGTS decorrentes de processos trabalhistas, evitando recolhimentos em duplicidade, autuações por descumprimento de obrigação acessória e prejuízos ao trabalhador.

|  |
| --- |
| **Marco temporal essencial**  Até 30/04/2026: sentenças e acordos (CCP/NINTER) seguem o modelo anterior — guias SEFIP/GFIP 660.  A partir de 01/05/2026: o recolhimento de FGTS de reclamatórias passa a ser feito obrigatoriamente pelo FGTS Digital.  Em ambos os casos, permanece a obrigação de transmitir o evento S-2500 ao eSocial. |

#### **Campos-chave do evento S-2500**

| **Campo** | **Finalidade** |
| --- | --- |
| dtSent / dtCCP | Data da sentença ou do acordo. Define a competência de apuração única em que todos os débitos do processo serão exibidos no FGTS Digital. |
| vrBcFGTSProcTrab | Base de cálculo de FGTS ainda não declarada em SEFIP ou no eSocial, inclusive de verba reconhecida no processo trabalhista. |
| vrBcFGTSSefip | Base de cálculo de FGTS declarada apenas em SEFIP (não informada no eSocial) e ainda não recolhida (campo opcional). |
| vrBcFGTSDecAnt | Base de cálculo de FGTS já declarada anteriormente no eSocial e ainda não recolhida (campo opcional). |

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41404310763415)  
  
**Importante**  
Os campos vrBcFGTSSefip e vrBcFGTSDecAnt somente podem receber valores referentes a competências de referência até 02/2024 (período anterior ao início do FGTS Digital). Bases de cálculo a partir de 03/2024 que não foram reconhecidas no processo, mas ainda estão em aberto, devem ser declaradas nos eventos normais de remuneração do eSocial (S-1200), e não nesses campos do S-2500.

#### **Competência de Apuração x Competência de Referência**

Um dos pontos de maior atenção no tratamento de processos trabalhistas é a distinção entre dois conceitos de período:

* Competência de Apuração: é única para todo o processo trabalhista e corresponde à data informada nos campos dtSent (sentença) ou dtCCP (acordo) do evento S-2500. É nessa competência que o débito aparecerá no módulo de Gestão de Guias.
* Competência de Referência: é cada mês com base de cálculo de FGTS informada dentro do processo (ou seja, o mês em que a verba seria originalmente devida). Pode haver dezenas de competências de referência dentro de uma única competência de apuração.

Na prática, o empregador deve selecionar, no FGTS Digital, o período de apuração do processo trabalhista; dentro dele, visualizará os débitos de todos os períodos de referência envolvidos. Os débitos sofrem incidência de encargos (juros e multa) desde cada período de referência até a data de vencimento da guia — e não apenas a partir da data da sentença.

|  |
| --- |
| **Exemplo**  Período de Apuração: 05/2026 (data da sentença/acordo)  Período de Referência 01/2024: base de R$ 1.000,00 (remFGTSProcTrab) + R$ 400,00 (remFGTSSefip) + R$ 300,00 (remFGTSDecAnt) = total agrupado de R$ 1.700,00 sob o Tipo de Valor 71  Período de Referência 02/2024: base de R$ 1.200,00 + R$ 120,00 + R$ 50,00 = total agrupado de R$ 1.370,00  Os dois valores aparecem no FGTS Digital sob a mesma competência de apuração (05/2026), com encargos calculados individualmente desde cada competência de referência. |

#### **Tipos de Valor de FGTS Gerados pelo Processo Trabalhista**

O eSocial classifica os débitos de FGTS oriundos de processos trabalhistas em tipos de valor específicos, distintos dos tipos de valor do FGTS mensal e rescisório “ordinário”. Esses tipos de valor são tratados, no FGTS Digital, como débitos do tipo “mensal”, ainda que se refiram ao mês da rescisão — isso simplifica o recolhimento em guia única de todo o débito apurado no processo.

| **Tipo de Valor** | **Descrição** | **Alíquota / Observação** |
| --- | --- | --- |
| 71 | FGTS Processo Trabalhista — Mensal | 8,0% — categorias gerais (101, 102, 104‑106, 111, 201‑202, 301‑304, 306‑307, 309‑310, 312, 721, entre outras) |
| 72 | FGTS Processo Trabalhista — Mensal Aprendiz / Contrato Verde e Amarelo | 2,0% — categorias 103, 107, 108 |
| 73 | FGTS Processo Trabalhista — Indenização compensatória do empregado doméstico | 3,2% — categoria 104; ainda em fase de implantação no FGTS Digital |
| 991 | FGTS Indenização Compensatória — Processo Trabalhista (Multa do FGTS) | Calculado diretamente pelo FGTS Digital, fora do eSocial — ver capítulo 6 deste guia |

Diferente dos tipos de valor 99 e 999 (indenização compensatória ordinária), os tipos 71, 72 e 73 chegam ao FGTS Digital diretamente pelo evento S-5503, enquanto o tipo 991 é calculado em funcionalidade própria do sistema.

#### **Regras de Recolhimento por Período**

* **Sentenças e acordos até 30/04/2026**

Para sentenças da Justiça do Trabalho ou acordos celebrados em CCP/NINTER ocorridos até 30/04/2026, o recolhimento do FGTS continua sendo feito pelas guias SEFIP/GFIP 660, conforme as orientações do Manual de Orientação ao Empregador — Recolhimentos Mensais e Rescisórios ao FGTS e das Contribuições Sociais, publicado pela Caixa Econômica Federal.

Mesmo nesses casos, permanece a obrigação de transmitir o evento S-2500 ao eSocial, nos termos do § 6º do art. 5º da Portaria MTE nº 240/2024.

* **Sentenças e acordos a partir de 01/05/2026**

Desde 01/05/2026, os empregadores devem utilizar obrigatoriamente o FGTS Digital para o recolhimento do FGTS previsto em sentenças da Justiça do Trabalho ou em acordos de CCP/NINTER. As bases de cálculo mensais têm como origem o evento S-2500 do eSocial e chegam ao sistema por meio do evento de retorno S-5503.

* **Regra específica para empregadores domésticos**

Os sistemas da Caixa ainda estavam, à data deste manual, em preparação para receber valores de FGTS de processos trabalhistas de empregados domésticos diretamente pelo FGTS Digital. Enquanto essa funcionalidade não estiver disponível, o empregador doméstico deve seguir as perguntas frequentes nº 25.01 e 25.02 do eSocial, que orientam a emissão de DAE (Documento de Arrecadação do eSocial). O procedimento envolve:

1. Acessar e reabrir cada uma das folhas de pagamento do período reclamado;
2. Clicar no nome do trabalhador na respectiva folha;
3. Editar manualmente a remuneração, incluindo a rubrica “Base de Cálculo do FGTS — Reclamatória Trabalhista”, com o valor estabelecido na ação judicial ou no acordo;
4. Seguir os demais procedimentos detalhados nas perguntas frequentes do eSocial sobre o tema.

|  |
| --- |
| **Atenção**  Verificar sempre, antes de declarar valores, se a competência de referência é anterior ou posterior a 03/2024 — isso determina se a regularização deve ocorrer pelos campos vrBcFGTSSefip/vrBcFGTSDecAnt do S-2500 (até 02/2024) ou pelos eventos normais de remuneração (S-1200) do eSocial (a partir de 03/2024). |

**Saiba Mais**  
Para maiores informações, acesse:

- [Manual de Orientação do FGTS DIGITAL](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/manual-de-orientacao-do-fgts-digital-versao-1-60-05-05-2026.pdf)

- [Recolhimentos de FGTS em processos trabalhistas serão efetuados via FGTS Digital a partir de maio/2026](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/comunicados/recolhimentos-de-fgts-em-processos-trabalhistas-serao-efetuados-via-fgts-digital-a-partir-de-maio-2026)

- [Em produção: recolhimentos de FGTS em processos trabalhistas devem ser efetuados via FGTS Digital](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/comunicados/em-producao-recolhimentos-de-fgts-em-processos-trabalhistas-devem-ser-efetuados-via-fgts-digital)

- [RH - RM - RHU - eSocial: S-2500 - Mapeamento dos campos para geração do evento S-2500](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18256276341783)

- [RH - RM - RHU - eSocial: S-2501 - Mapeamento dos campos para geração do evento S-2501](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18863423016855)
