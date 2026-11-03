---
article_id: 360017553752
category: RH - Folha de Pagamento
content_hash: 3d5af6eb53dbede2604d174bb3d0cd8b5b3d8fdeb8259c893917f141be826b16
fetched_at: '2026-06-28T22:44:16.310526+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Salário Família - Forma de cálculo
type: support-article
updated_at: '2025-08-04T12:54:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017553752-RH-Linha-Protheus-GPE-Sal%C3%A1rio-Fam%C3%ADlia-Forma-de-c%C3%A1lculo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16282492610199)**Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**Salário Família - Forma de cálculo.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12  
  
**Solução****Cálculo de salário família para Mensalista**

Verifique o salário do funcionário no campo **RA\_SALARIO**e se o funcionário se enquadra na **faixa** cadastrada na tabela **S003** (Definições de cálculo / Manutenção Tabelas (GPE320)/ Tabela S003) . Em seguida faça o seguinte cálculo:  
**QtdeDepSF \* ValorFaixa / DiasBase \* DiasFamil**

**Cálculo de salário família para Horista**

Verifique o salário do funcionário através da seguinte conta ((**SalHora / HrMes) \* (HrNormal + HrDescanso)**) e se o funcionário se enquadra na **faixa** cadastrada na tabela S003. Depois, faça o seguinte cálculo:  
**QtdeDepSF \* ValorFaixa / DiasBase \* DiasFamil**

**Cálculo de salário família para Professor Mensalista**

Verifique o salário do funcionário no campo **RA\_SALARIO**. Caso não tenha, irá compor o salário de acordo com as tarefas cadastradas (Caso a tarefa seja **VARIÁVEL,** deverá ter incidência para Salário Família, se a mesma fizer parte da composição do salário do professor) se enquadra na faixa cadastrada na tabela S003 (Definições de cálculo / Manutenção Tabelas/ Tabela S003). Faça o seguinte cálculo:  
**QtdeDepSF \* ValorFaixa / DiasBase \* DiasFamil**

**Cálculo de salário família para Professor Aulista**

Verifique o salário de acordo com as **tarefas cadastradas** (caso a tarefa seja **VARIÁVEL,** deverá ter incidência para Salário Família, caso a mesma incida na composição do salário do professor) e se enquadra na faixa cadastrada na tabela S003 (Definições de cálculo / Manutenção Tabelas/ Tabela S003). Faz o seguinte cálculo:  
QtdeDepSF \* ValorFaixa / DiasBase \* DiasFamil

**Observação:**DiasFamil: se o conteúdo do parâmetro **MV\_SALFD** for **S**, buscará do último dia do mês, senão calculará com 30.  
DiasBase: se o conteúdo do parâmetro **MV\_SALFD** for **S**, buscará do último dia do mês, senão calculará com 30.

Para os adicionais padrões do sistema, é considerado o valor integral para a base de cálculo do salário família se ele estiver com SIM para Salário Família.

**Importante:** o parâmetro MV\_SALFD será preponderante ao parâmetro MV\_DIASPER no cálculo do salário família.

**Saiba Mais**

**<https://tdn.totvs.com/pages/releaseview.action?pageId=555868219>**

[RH - Linha Protheus - GPE - Calculo salário família para contrato intermitente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057788094-RH-Linha-Protheus-GPE-Calculo-sal%C3%A1rio-fam%C3%ADlia-para-contrato-intermitente?source=search)

[RH - Linha Protheus - GPE - Como calcular salario família para funcionário afastado por licença maternidade.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051164914-RH-Linha-Protheus-GPE-Como-calcular-salario-fam%C3%ADlia-para-funcion%C3%A1rio-afastado-por-licen%C3%A7a-maternidade-?source=search)

[RH - Linha Protheus - GPE - Como filtrar verbas com SIM para Salário Família?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049734353-RH-Linha-Protheus-GPE-Como-filtrar-verbas-com-SIM-para-Sal%C3%A1rio-Fam%C3%ADlia-?source=search)

[RH - Linha Protheus - GPE - Sistema não gera salário família na rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013018931-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-gera-sal%C3%A1rio-fam%C3%ADlia-na-rescis%C3%A3o?source=search)

[RH - Linha Protheus - GPE - Como configurar o sistema para que pague salario família para funcionário que teve afastamento dentro do mês](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058220214-RH-Linha-Protheus-GPE-Como-configurar-o-sistema-para-que-pague-salario-fam%C3%ADlia-para-funcion%C3%A1rio-que-teve-afastamento-dentro-do-m%C3%AAs?source=search)

[RH - Linha Protheus - GPE - Como alterar o valor do salário família - Tabela S003](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001654201-RH-Linha-Protheus-GPE-Como-alterar-o-valor-do-sal%C3%A1rio-fam%C3%ADlia-Tabela-S003?source=search)

[RH - Linha Protheus - GPE - Sistema não calcula Salário Família](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017957872-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-calcula-Sal%C3%A1rio-Fam%C3%ADlia?source=search)
