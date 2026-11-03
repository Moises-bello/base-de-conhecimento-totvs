---
article_id: 360028663471
category: RH - Folha de Pagamento
content_hash: 57ba701f8d369f6541eead84523cee8b8f0eeca95fb9b860315ebed96d3c2336
fetched_at: '2026-06-28T22:44:13.528147+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como funciona o salário família para funcionários
  Horistas
type: support-article
updated_at: '2025-04-23T12:01:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028663471-RH-Linha-Protheus-GPE-Como-funciona-o-sal%C3%A1rio-fam%C3%ADlia-para-funcion%C3%A1rios-Horistas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15940185046039) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como funciona o salário família para funcionários Horistas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

O cálculo do Salário Família para funcionários horistas pode ser realizado de duas formas:

* Verificação do conteúdo dos campos **Salário (RA\_SALARIO) e Hrs. Mensais (RA\_HRSMES)** no cadastro do funcionário em **Atualizações > Funcionários > Funcionários (GPEA010)**, para enquadramento de acordo com o conteúdo da tabela **S003 - Tabela de Salário Família**, localizada em **Atualizações > Definições de Cálculo > Manutenção de Tabelas (GPEA320)**.

![](https://i.imgur.com/5xJk6bL.png)

* Verificação das verbas com os identificadores **0032** - Salário Horista e **0033** - DRS Horista, para o enquadramento informando anteriormente.

Para esta validação foi implementado o Mnemônico **P\_SALFHOR**, cujo conteúdo pode ser .F. ou .T.

**P\_SALFHOR = .F.**

**Atualizações / Definições de Cálculo / Mnemônicos (GPEA300)**: utilizando com conteúdo .F.  
  
![](http://tdn.totvs.com/download/attachments/343638421/image2018-3-7_21-11-35.png?version=1&modificationDate=1520470184000&api=v2)  
  
Pode-se verificar na imagem abaixo que a verba atrelada ao Identificador de cálculo 0034 - Salário Família foi gerada para o funcionário, pois a soma das verbas 003 (id 0032) + 005 (id 0033) se enquadraram no teto do salário Família, uma vez que no respectivo mês o funcionário tinha apenas 205,33 horas trabalhadas.

Nos meses com 30 ou 31 dias este funcionário já não recebe, pois ultrapassaria o limite para o recebimento deste benefício.

![](http://tdn.totvs.com/download/attachments/343638421/image2018-3-7_21-32-45.png?version=1&modificationDate=1520470184000&api=v2)

**P\_SALFHOR = .T.**

**Atualizações / Definições de Cálculo / Mnemônico****s (GPEA300)**: utilizando com conteúdo .T.  
![](http://tdn.totvs.com/download/attachments/343638421/image2018-3-7_21-18-7.png?version=1&modificationDate=1520470184000&api=v2)  
Utilizando o Mnemônico com conteúdo igual a T, o sistema efetua a verificação do **Salário (RA\_SALARIO**) do funcionário multiplicando pela quantidade de horas mês definido no campo **Hrs. Mensais (RA\_HRSMES)**, neste exemplo 220, portanto R$6,27 X 220 = R$1.379,40, cujo valor ultrapassa o teto do salário família desta competência, que é de R$1.319,18.

![](http://tdn.totvs.com/download/attachments/343638421/image2018-3-7_21-21-39.png?version=1&modificationDate=1520470183000&api=v2)  
**Obs.:** ressaltamos que as verbas com os identificadores 0032 - Salario Horista, 0033 - DSR Horista e 0034 - Salário Família no campo Salário Família (RV\_SALFAMI) devem estar com conteúdo igual a N- Não para que a verba de salário família possa ser gerada.  
  
**Saiba Mais**  
Veja como buscar esse documento através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://totvssuporte.zendesk.com/knowledge/articles/1500008685602/pt-br?brand_id=1509248&return_to=%2Fhc%2Fpt-br%2Farticles%2F1500008685602)

[RH - Linha Protheus - GPE - Como alterar o valor do salário família - Tabela S003](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001654201-RH-Linha-Protheus-GPE-Como-alterar-o-valor-do-sal%C3%A1rio-fam%C3%ADlia-Tabela-S003?source=search)

[RH - Linha Protheus - GPE - Sistema não calcula Salário Família](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017957872-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-calcula-Sal%C3%A1rio-Fam%C3%ADlia?source=search)

[RH - Linha Protheus - GPE - Salário Família - Forma de cálculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017553752-RH-Linha-Protheus-GPE-Sal%C3%A1rio-Fam%C3%ADlia-Forma-de-c%C3%A1lculo?source=search)

[RH - Linha Protheus - GPE - Como filtrar verbas com SIM para Salário Família?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049734353-RH-Linha-Protheus-GPE-Como-filtrar-verbas-com-SIM-para-Sal%C3%A1rio-Fam%C3%ADlia-?source=search)

[RH - Linha Protheus - GPE - Calculo salário família para contrato intermitente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057788094-RH-Linha-Protheus-GPE-Calculo-sal%C3%A1rio-fam%C3%ADlia-para-contrato-intermitente?source=search)

[RH - Linha Protheus - GPE - Cálculo de salário família nas férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12330801635607-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-sal%C3%A1rio-fam%C3%ADlia-nas-f%C3%A9rias?source=search)

[RH - Linha Protheus - GPE - Como configurar o sistema para que pague salario família para funcionário que teve afastamento dentro do mês](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058220214-RH-Linha-Protheus-GPE-Como-configurar-o-sistema-para-que-pague-salario-fam%C3%ADlia-para-funcion%C3%A1rio-que-teve-afastamento-dentro-do-m%C3%AAs?source=search)

[RH - Linha Protheus - GPE - Como calcular salario família para funcionário afastado por licença maternidade.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051164914-RH-Linha-Protheus-GPE-Como-calcular-salario-fam%C3%ADlia-para-funcion%C3%A1rio-afastado-por-licen%C3%A7a-maternidade-?source=search).
