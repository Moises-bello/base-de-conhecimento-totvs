---
content_hash: d75cbd2a360ca34f7045f0e766455ffa244e0c0e5c6bde66c07c4d61596ea2bd
fetched_at: '2026-06-29T00:05:55.333241+00:00'
page_id: '134153018'
product: rm
source: tdn-rm
title: Cálculo de Vale Transporte
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=134153018
version: 6
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Folha de Pagamento                      **Versão:**11.8X |
| **Processo** | **:** | Folha de Pagamento |
| **Subprocesso** | **:** | Cálculo de Vale Transporte |
| **Data da publicação** | **:** | 11/07/2013 |

#### **1- Introdução**

Neste documento você encontrará a parametrização e conferência a ser realizada no sistema para o cálculo de Vale Transporte.

#### **2- Configuração do Sindicato**

**2.1 – Acesso ao módulo**

Delphi: Acesse o menu “Cadastro | Sindicatos”

Nova MDI: Acesse o menu “Administração de Pessoal | Sindicatos”

**2.2 – Configuração da tela**

Edite o sindicato desejado e na aba “Identificação” determine o modo que será descontado o Vale-Transporte.

Visualização Delphi:

Visualização Nova MDI:

**2.3 – Campos**

• **"% desconto":** informe o percentual de desconto de vale-transporte definido para os funcionários ligados ao sindicato

• **"Desconto único no mês":** deverá ser habilitado para que seja feito o cálculo de desconto de vale-transporte considerando o valor encontrado nos lançamentos do acumulado mensal, ou seja, o somatório de todos os períodos. Não o habilitando, o sistema fará o cálculo para desconto de vale-transporte considerando somente o valor encontrado nos lançamentos do período

**• "Usa 30 dias":** deverá ser habilitado para que o percentual de desconto do vale-transporte seja aplicado sobre o salário do funcionário. Se o campo não estiver marcado, será aplicado o percentual de desconto sobre o número de dias úteis constantes no cadastro do funcionário

#### **3 – Configuração das Tarifas de Transporte**

**3.1 – Acesso o módulo**

Delphi: Acesse o menu “Cadastro | Tabelas auxiliares | Tarifas de transporte”

Nova MDI: Acesse o menu “Administração de Pessoal | Tarifas de Transporte”

**3.2 – Configuração**

Cadastre a(s) tarifa(s) a serem utilizada(s). Esteja atendo à vigência.

**3.3 – Outras informações**

Para outras informações sobre este módulo acesse o Wikihelp conforme link abaixo:

*• Cadastro de Tarifas de Transporte*

<http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.tarifasTransporte.aspx>

#### **4 – Configuração das Linhas de Transporte**

**4.1 – Acesso ao módulo**

Delphi: Acesse o menu “Cadastro | Tabelas auxiliares | Linhas de transporte”

 

Nova MDI: Acesse o menu “Administração de Pessoal | Linhas de Transporte”

**4.2 - Configuração**

Crie a(s) linha(s) de transporte, associando a ela(s) a(s) tarifa(s) cadastrada(s) no passo anterior.

**4.3 – Outras informações**

Para outras informações sobre este módulo acesse o Wikihelp conforme link abaixo:

*• Linhas de Transporte*

<http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.linhasTransporte.aspx>

#### **5 – Configuração no Funcionário**

**5.1 – Acesso ao módulo**

Acesse o cadastro de funcionários, edite o funcionário desejado e em seguida:

Delphi: Acesse a pasta “Registro | Vale Transporte”, informe os dias do mês atual e do próximo mês. Informe também a linha de transporte que o mesmo vai utilizar.

Nova MDI: Acesse a menu lateral “Informações para o cálculo | Parâmetros”

#### **6 – Lançamento do Vale Transporte**

**6.1 – Menu de Lançamento**

Delphi: Acesse o menu “Movimento | Folha de pagamento | Lançamentos automáticos | Vale transporte” e processe o lançamento de acordo com a seleção de funcionários

Nova MDI: Acesse o menu “Folha Mensal | Lançamentos | Grupo de Eventos”, crie um grupo mantendo marcado apenas o parâmetro “Lançar Vale Transporte”. Na aba “Eventos do grupo”, insira o evento de Vale Transporte.

#### **7 – Observações**

Ao acessar “Opções | Parâmetros | RM Labore” na “Pasta Parâm. Calculo | Parâmetros” você encontrará o parâmetro “Sal. nominal p/ vale-transporte”. Quando o mesmo estiver marcado, o valor da incidência de vale transporte, na pasta de incidências do envelope (Cadastros | Funcionários | Ícone Envelope | Pasta Incidências), mostrará o valor do salário base do funcionário. Caso contrário, o valor da incidência de vale transporte será a soma dos eventos que incidem em vale transporte no período.

Na nova MDI o parâmetro se encontra no menu “Configurações | Parametrizador”, item “06.01.03 – Folha Normal | Etapa 2: Vale Transporte”.

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)

**COMUNIDADE **[R@RH](https://totvs.byyou.com/?space=rrh)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 4 – (Recursos Humanos)

*Publicador: Joyce Nereu*

*Código: LAB-00001*
