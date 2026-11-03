---
article_id: 41398667551255
category: eSocial
content_hash: 70dc5ddcfc54d46fa47601c9671a61a01955804e2fc80dfe9960685f7cbc3d51
fetched_at: '2026-06-28T22:47:15.273184+00:00'
product: rm
section_id: 11645725240471
source: central-rm
title: 'RH - RM - RHU - Processo Trabalhista - FGTS Digital: Multa do FGTS decorrente
  de Processo Trabalhista'
type: support-article
updated_at: '2026-06-22T14:57:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41398667551255-RH-RM-RHU-Processo-Trabalhista-FGTS-Digital-Multa-do-FGTS-decorrente-de-Processo-Trabalhista
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41398673196951) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Quais são as orientações quanto ao cadastro e envio de Multa (Indenização Compensatória) em reclamatórias trabalhistas a partir da implantação do FGTS Digital?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - **12.1.2506** e **superiores**.  
  
**Solução**  
Além do FGTS mensal apurado pelo evento S-2500, é comum que sentenças ou acordos trabalhistas reconheçam também o direito à indenização compensatória (a “multa de 40%” ou 20%, conforme o motivo de desligamento). O FGTS Digital trata esse cálculo em funcionalidade própria (Ou seja, não há cadastros no RM).

#### **Funcionalidade Gestão de Histórico de Remunerações de Processo Trabalhista**

Localizada dentro do módulo Remunerações para Fins Rescisórios, essa funcionalidade lista apenas os trabalhadores cujo motivo de desligamento, categoria e regime trabalhista tenham, por previsão legal, direito à indenização compensatória. Ela utiliza como base de cálculo os valores mensais de FGTS já informados no evento S-2500 (recuperados automaticamente pelo sistema) e permite ao empregador:

* Pesquisar o histórico por número do processo trabalhista;
* Visualizar as bases mensais de FGTS recuperadas do S-2500;
* Editar o cálculo quando necessário;
* Confirmar e enviar o débito ao módulo de Gestão de Guias, clicando em “Concluir e Enviar ao Gestão de Guias”.

O resultado desse procedimento gera o Tipo de Valor 991 (FGTS Indenização Compensatória — Processo Trabalhista), que passa a constar no módulo de Gestão de Guias para emissão e pagamento.

|  |
| --- |
| **Cuidado com duplicidade de bases de cálculo**  Essa funcionalidade NÃO se confunde com o cálculo da indenização compensatória ordinária (módulo principal de Gestão de Histórico de Remunerações).  O empregador deve ter atenção para não declarar a mesma base de cálculo nas duas funcionalidades, sob pena de duplicar — e majorar indevidamente — o valor da multa rescisória devida ao trabalhador. |

#### **Base de cálculo não declarada no evento S-2500**

Caso exista valor de indenização compensatória a recolher sobre bases de cálculo que não foram declaradas no evento S-2500, o recolhimento deve ser feito pela funcionalidade padrão de cálculo da multa rescisória (Edição do Histórico de Remunerações), editando os valores da base para fins rescisórios — sempre com atenção para não duplicar bases já lançadas na funcionalidade específica de processo trabalhista.

#### **Critérios legais para o cálculo automático**

O cálculo automático da indenização compensatória depende da categoria do trabalhador e do motivo de desligamento (ou de término, no caso de TSVE — Trabalhador Sem Vínculo de Emprego). As tabelas a seguir resumem as situações com direito ao cálculo automático pelo FGTS Digital.

| **Código** | **Motivo de desligamento** | **% Multa** |
| --- | --- | --- |
| 2 | Rescisão sem justa causa, por iniciativa do empregador | 40% |
| 3 | Rescisão antecipada do contrato a termo por iniciativa do empregador | 40% |
| 5 | Rescisão por culpa recíproca | 20% |
| 14\* | Encerramento da empresa / falecimento do empregador individual ou doméstico, sem continuidade | 40% |
| 17 | Rescisão indireta do contrato de trabalho | 40% |
| 26\* | Paralisação motivada por ato de autoridade pública | 40% |
| 27 | Força maior | 20% |
| 33 | Acordo entre as partes (art. 484-A da CLT) | 20% |
| 47\* | Encerramento da empresa / supressão de atividades | 40% |
| 48\* | Falecimento do empregador individual, sem continuidade | 40% |

*(\*) Motivos que permitem o arquivamento do cálculo automático da multa pelo empregador, sob sua conta e risco — o arquivamento não impede fiscalização e cobrança pela Secretaria de Inspeção do Trabalho.*

Categorias sem cálculo automático de multa: trabalhadores avulsos (201‑202), agentes públicos (301‑314), cessão (401 e 410), contribuintes individuais exceto diretor não empregado (701‑781, exceto 721) e bolsistas (901‑906).

#### **Reconstituição do histórico de remunerações**

Para apurar corretamente a multa, o FGTS Digital recompõe o histórico de depósitos devidos ao trabalhador a partir das remunerações já informadas ao eSocial — inclusive de competências anteriores ao início do sistema — considerando apenas a base de cálculo devida, independentemente de o depósito mensal ter sido efetivamente realizado. Quando o sistema não localizar a base ou justificativa de ausência de remuneração em alguma competência, o empregador pode:

* Preencher manualmente a remuneração devida em cada mês;
* Usar ferramentas de preenchimento em bloco (repetir valor ou usar o salário-mínimo);
* Importar arquivo em leiaute específico com as remunerações faltantes;
* Declarar diretamente o valor total atualizado da base de cálculo da indenização compensatória.

Desde março/2024, as informações e declarações do eSocial são consideradas base mínima obrigatória para o cálculo da indenização compensatória prevista no art. 18 da Lei nº 8.036/1990, e constituem confissão de débito e instrumento hábil para a cobrança do crédito de FGTS.

**Saiba Mais**  
Para maiores informações, acesse:

- [Manual de Orientação do FGTS DIGITAL](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/manual-de-orientacao-do-fgts-digital-versao-1-60-05-05-2026.pdf)

- [Recolhimentos de FGTS em processos trabalhistas serão efetuados via FGTS Digital a partir de maio/2026](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/comunicados/recolhimentos-de-fgts-em-processos-trabalhistas-serao-efetuados-via-fgts-digital-a-partir-de-maio-2026)

- [Em produção: recolhimentos de FGTS em processos trabalhistas devem ser efetuados via FGTS Digital](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/comunicados/em-producao-recolhimentos-de-fgts-em-processos-trabalhistas-devem-ser-efetuados-via-fgts-digital)

- [RH - RM - RHU - eSocial: S-2500 - Mapeamento dos campos para geração do evento S-2500](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18256276341783)

- [RH - RM - RHU - eSocial: S-2501 - Mapeamento dos campos para geração do evento S-2501](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18863423016855)
