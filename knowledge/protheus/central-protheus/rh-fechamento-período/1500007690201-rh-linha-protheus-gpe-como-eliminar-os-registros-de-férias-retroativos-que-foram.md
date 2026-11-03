---
article_id: 1500007690201
category: RH - Fechamento Período
content_hash: 8d1fa9d7e26acfdcf5de1b101212720a12ac255cce5eeff239aa4e24ef6052bc
fetched_at: '2026-06-28T22:43:24.418524+00:00'
product: protheus
section_id: 360011909793
source: central-protheus
title: RH - Linha Protheus - GPE - Como eliminar os registros de férias retroativos
  que foram gerados indevidamente
type: support-article
updated_at: '2025-04-17T17:13:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007690201-RH-Linha-Protheus-GPE-Como-eliminar-os-registros-de-f%C3%A9rias-retroativos-que-foram-gerados-indevidamente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26346809308695) Tempo aproximado para leitura: **00:04:00 min**  
**Dúvida**Como eliminar os registros de **férias retroativos que foram gerados indevidamente?**

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões   
  
**Solução**Devido a uma **não-conformidade na rotina de Fechamento - GPEM120**, que sob determinadas condições poderia gerar registros na tabela **Controle Dias de Direito (SRF)**, com dados retroativos desde a **data de Admissão** do funcionário, disponibilizado o *RDMAKE* **UPDSRF**.   
Esta situação ocorria geralmente em base de dados que foram **migradas de outros sistemas**, ou quando o funcionário **não possuía nenhum período ativo.**

**Exemplo**  
Funcionário 000001 **admitido em 01/01/2017**. Não há histórico de períodos anteriores, e em dezembro/2017 é feita a quitação das férias.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Data Ini. Férias** | **Data Fin. Férias** | **Dias Férias** | **Dias Vencidos** | **Dias Proporcionais** | **Status** |
| 01/01/2017 | 31/12/2017 | 30 | 30 | 0 | Pago |

Após fechar o período 01/01/2018 o sistema estava **criando períodos retroativos a admissão** com status de Ativo:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Data Ini. Férias** | **Data Fin. Férias** | **Dias Férias** | **Dias Vencidos** | **Dias Proporcionais** | **Status** |
| 01/01/2015 | 31/12/2015 | 30 | 30 | 0 | Ativo (indevido) |
| 01/01/2016 | 31/12/2016 | 30 | 30 | 0 | Ativo (indevido) |
| 01/01/2017 | 31/12/2017 | 30 | 30 | 0 | Pago |
| 01/01/2018 | 31/12/2018 | 30 | 0 | 2,5 | Ativo (correto) |

A **rotina** de **Fechamento** deve estar sempre devidamente **atualizada**.

Para que seja possível **eliminar** os **registros** de **férias** **retroativos** que foram **gerados** **indevidamente** está sendo disponibilizado o *RDMAKE* **UPDSRF**.   
Por meio desta rotina o sistema irá verificar todos os registros da tabela Controle dias de Direito (SRF) das Filiais selecionadas. A avaliação será feita a partir do registro mais recente para o mais antigo. Se houver ao menos um registro com o **Status** "Pago" (campo RF\_STATUS = 3), o sistema irá eliminar os registros anteriores que estiverem com Status Ativo.

Considerando o cenário descrito, após executar a rotina UPDSRF o sistema eliminará os registros retroativos do funcionário 000001:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Data Ini. Férias** | **Data Fin. Férias** | **Dias Férias** | **Dias Vencidos** | **Dias Proporcionais** | **Status** |
| 01/01/2017 | 31/12/2017 | 30 | 30 | 0 | Pago |
| 01/01/2018 | 31/12/2018 | 30 | 0 | 2,5 | Ativo |

**Configuração dos Menus**  
**1.** No **Configurador (SIGACFG),**acesse **Ambientes > Cadastro > Menu (CFGX013)**. Informe a nova opção de menu **SIGAGPE**, conforme instruções a seguir:

|  |  |
| --- | --- |
| **Menu** | SIGAGPE |
| **Submenu** | Fechamentos |
| **Nome da Rotina** | Atualiza SRF |
| **Programa** | UPDSRF |
| **Módulo** | Gestão de Pessoal |
| **Tipo** | Função de Usuário |

**Procedimento para Utilização  
  
2.** No módulo Gestão de Pessoal (SIGAGPE), acesse **Miscelânea > Fechamentos > Atualiza SRF (UPDSRF)**.

O sistema apresenta a rotina UPDSRF - Atualização dos dados da tabela SRF.  
  
![image2018-11-28_9-56-32.png](https://tdn.totvs.com/download/attachments/439684848/image2018-11-28_9-56-32.png?version=1&modificationDate=1543409792097&api=v2)  
  
**3.** Clique em **Avançar** para que o sistema apresente a tela para seleção das Filiais que serão processadas.

**![](https://tdn.totvs.com/download/attachments/439684848/image2018-11-28_9-57-37.png?version=1&modificationDate=1543409857287&api=v2)**

**4.** Clique em **Avançar** para iniciar o processamento.     
**5.** O sistema irá gerar **processar** os **funcionários** compreendidos nos parâmetros definidos pelo usuário, e irá apresentar um ***Log* dos registros** no final do processamento da rotina.

**Importante:**Serão **eliminados** os registros de férias ativos que estavam com **data inferior** a outros períodos que estavam quitados.

**Saiba Mais**Acesse o *link* a seguir para o pacote acumulado contendo as últimas atualizações dos fontes envolvidos e a pasta de ***Rdmake*** para compilação: [RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição continua (acumulado) do modulo Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-MP-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-continua-acumulado-do-modulo-Gest%C3%A3o-de-Pessoal?source=search)  
*Link* para boletim técnico: <https://tdn.totvs.com/pages/releaseview.action?pageId=439684848>

[RH - Fechamento Período](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011909793-RH-Fechamento-Per%C3%ADodo)
