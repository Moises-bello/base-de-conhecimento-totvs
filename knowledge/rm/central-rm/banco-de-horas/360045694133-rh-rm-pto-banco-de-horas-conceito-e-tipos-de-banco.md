---
article_id: 360045694133
category: Banco de Horas
content_hash: 4cdf6feb2b76cc4f8cca08a3d478ed622cd52e81bc899fd6cb40d588f767c416
fetched_at: '2026-06-28T22:46:27.743049+00:00'
product: rm
section_id: 1500000835081
source: central-rm
title: 'RH - RM - PTO - Banco de Horas: Conceito e tipos de banco'
type: support-article
updated_at: '2024-06-20T20:49:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045694133-RH-RM-PTO-Banco-de-Horas-Conceito-e-tipos-de-banco
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16782096950295) Tempo aproximado para leitura: 00:01:30 min  
  
Dúvida**O que é banco de horas e os tipos de banco disponíveis no Automação de Ponto.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto – Todas as versões.  
  
**Solução**

O Banco de Horas tem como objetivo armazenar as horas extras, atrasos e faltas para futuras compensações ou pagamento. A forma de armazenamento e o período de disponibilidade das horas para compensação são definidos pela Legislação Trabalhista, Acordo Coletivo ou Convenção Coletiva de Trabalho. A seguir, apresento os tipos de banco de horas disponíveis:

1. **Banco de Horas Diário**: Nesse tipo de banco de horas, as horas extras e os atrasos/faltas são acumuladas diariamente e separados por faixas.
2. **Banco de Horas Diário por Ocorrência:** Nesse tipo de banco de horas diário, todas as ocorrências geradas são separadas diariamente. Esse tipo de banco permite pagar ou descontar uma ocorrência (atraso, falta ou hora extra) ao alterar a atitude da ocorrência coletada, sem a necessidade de passar pelo processo de compensação.
3. **Banco de Horas por Período:** Esse tipo de banco de horas registra as compensações do período agrupadas por evento.

Além disso, há a opção de utilizar **fórmulas** personalizadas caso os parâmetros disponíveis não atendam completamente às regras de negócio da empresa, convenção ou acordo coletivo.

Ao final de um período determinado é possível realizar a compensação do banco de horas ou o lançamento do banco de horas ou ambos em um único processo:

1. **Compensação do banco de horas**: Nessa opção, o sistema irá compensar os débitos e créditos do banco, e o saldo restante será mantido no banco de horas. Isso significa que as horas não serão lançadas para a movimentação do funcionário.
2. **Compensação e lançamento do banco de horas:** Nessa opção, o sistema irá compensar os débitos e créditos do banco, e o saldo restante será lançado para a movimentação do funcionário. Dessa forma, as horas serão pagas ou descontadas do funcionário.
3. **Lançamento do banco de horas:** Nessa opção, o sistema irá apenas lançar as horas do banco para a movimentação do funcionário, sem realizar a compensação dos débitos e créditos.

Portanto, esses processos só devem ser realizados após o fechamento do ponto do funcionário, pois o lançamento de horas para a movimentação travará o cálculo do funcionário.

Para obter mais detalhes sobre cada processo, recomendo consultar os documentos a seguir:

* [RH - RM - PTO - Como configurar o banco de Horas diário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045154114)
* [RH - RM - PTO - Como configurar o banco de horas por período](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017559512)
* [RH - RM - PTO - Como considerar percentual dos eventos no banco de horas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025275051)
* [RH - RM - PTO - Inserir horas no banco de horas do funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018470811)
* [RH - RM - PTO - Como lançar saldo parcial do banco de horas diário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20892682356119)
* [RH - RM - PTO - Zerar o saldo do banco de horas diário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012284812)
* [RH - RM - PTO - Zerar o saldo do banco de horas por período](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018164972)
* [RH - RM - PTO - Ordenação da compensação e do lançamento do banco de horas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025392891)
* [RH - RM - PTO - Compensação e lançamento do banco de horas considerando limite de dias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045162434)
* [RH - RM - PTO - Acessar a memória do processo compensação/lançamento do banco de horas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014004312)
* [RH - RM - PTO - Como desfazer o processo de compensação e/ou lançamento do banco de horas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21456970234391)
* [RH - RM - PTO - Conversor da compensação do banco de horas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000491987)
* [RH - RM - PTO - Quais são os relatórios que mostram o saldo do banco de horas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21461684191127)
* [RH - RM - PTO - Tabelas do banco de dados que salvam os valores do banco de horas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21457924310167)

**Saiba Mais:**  
Para maiores informações de como configurar, acesse os links:

[RH - RM - PTO - Alterar atitude de ocorrências coletadas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000585988)
