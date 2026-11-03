---
article_id: 21457924310167
category: Banco de Horas
content_hash: 532e4cf0b13e3effe01067fdc4e088f6dbcb4ab1edf5715f14142913fcfff3bf
fetched_at: '2026-06-28T22:46:27.713951+00:00'
product: rm
section_id: 1500000835081
source: central-rm
title: RH - RM - PTO - Tabelas do banco de dados que salvam os valores do banco de
  horas
type: support-article
updated_at: '2024-06-12T18:22:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21457924310167-RH-RM-PTO-Tabelas-do-banco-de-dados-que-salvam-os-valores-do-banco-de-horas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21457924260759) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Quais são as tabelas dos bancos de dados envolvidas no processo de banco de horas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto – 11.82 e superiores.  
  
**Solução**Abaixo segue as tabelas envolvidas na rotina do banco de horas:

**ABANCOHORFUN**: Referente ao saldo do Banco de Horas Diário e Diário por Ocorrência  
**ACOMPFUN**: Referente ao saldo do Banco de Horas por Período

**ABANCOHORFUNDETALHE**: Nova tabela que armazena saldo tanto do banco de horas diário quanto banco de horas por período. Referente aos valores exibidos na guia Banco de Horas, na visão do espelho de ponto do funcionário.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21457967158039)

**ASALDOBANCOHOR**: Referente ao saldo exibido na guia Saldo do Banco de Horas sintético, na visão do espelho de ponto do funcionário.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21458015968663)

**ASALDOBANCOHORFUNDETALHE**: Referente ao saldo exibido na guia Saldo do Banco de Horas Analítico, na visão do espelho de ponto do funcionário.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21458015976727)

**AATUALFUN**: Esta tabela não é mais utilizada. Tratava-se de uma tabela que continha o saldo inicial do banco de horas inserido nos parâmetros do funcionário. O saldo nesta tabela é destinado apenas para fins de compensação e não pode ser lançado.

Para zerar o saldo, marcar o parâmetro "considerar saldo inicial" no processo de compensação/lançamento.  
  
**ADEFINICAOCOMPENSACAO**: Armazena o log da memória de cálculo da compensação do banco de horas. 

**Saiba Mais**:  
[RH - RM - PTO - Banco de Horas: Conceito e tipos de banco](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045694133)  
[RH - RM - PTO - Acessar a memória do processo compensação/lançamento do banco de horas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014004312)
