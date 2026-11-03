---
content_hash: 331d5e98f73055aeb97717787fd3ef06e05ffba8f1602d0b46fb3e2a03d9150d
fetched_at: '2026-06-29T00:10:18.897174+00:00'
page_id: '4812726'
product: rm
source: tdn-rm
title: Como Fazer - Importação Automática de Batidas Utilizando Layout AFD
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4812726
version: 10
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Automação de Ponto                    **Versão:**11.5X |
| **Processo** | **:** | Importação Automática de Batidas |
| **Subprocesso** | **:** | Utilizando Layout AFDT Em Ambiente 3 Camadas |
| **Data da publicação** | **:** | 15/10/2013 |

#### **1 – Introdução**

Este “Como Fazer” tem o objetivo de demonstrar como efetuar a importação de Importação Automáticas de Batidas Utilizando Arquivo no layout padrão AFD da nova portaria 1510.

Obs: Para utilizar a parametrização do novo layout AFD para importação automática de batidas deve ser feito os procedimentos abaixo pois essa funcionalidade só está disponível para ambiente em 3 camadas, então e necessário que estejam utilizando esse tipo de ambiente ou simular um ambiente de 3 camadas apontando para a própria máquina. Deve-se efetuar a parametrização dos arquivos .config caso NÃO possua ambiente 3 camadas:

#### **2 – Configuração dos Arquivos Configs**

1) Acessar a pasta C:\ TOTVS \ CorporeRM \ RM.Net;

2) Acessar TODOS os arquivos config e alterar os que possuam as tags abaixo,

 De:  
<add key="JobServer3Camadas" value="false" />

Para:  
<add key="JobServer3Camadas" value="true" />

3) Apontar todas as tags 3que possuam caminho setado para a máquina local:

<add key="ActionsPath" value="C:\TOTVS\CorporeRM\RM.Net;C:\TOTVS\CorporeRM\Corpore.Net\Bin" />  
<add key="LibPath" value="C:\TOTVS\CorporeRM\RM.Net" /> ;

4) Acessar o caminho "C:\TOTVS\CorporeRM \ RMChronus" e efetuar as alterações das tags acima no arquivo RMChronus.exe.config.  
**Atenção!** Essa alteração deve ser feita nos arquivos ".configs" das pastas dos aplicativos que se desejar utilizar o ambiente 3 camadas.

#### **3 – Processo de Importação**

Informar o caminho do arquivo a ser importado, o layout do relógio (O mesmo pode ser cadastrado em Cadastro / Tabelas Auxiliares / Terminais de Coleta / Layout) e o Terminal de Coleta (O mesmo pode ser cadastrado em Cadastro / Tabelas Auxiliares / Terminais de Coleta / Cadastro).

 

**Atenção!** No cadastro do Layout (Cadastro / Tabelas Auxiliares / Terminais de Coleta / Layout) deve estar marcada a Opção “Utiliza layout AFD para importação”

Ao avançar o processo de importação de batidas , irá abrir uma janela de agendamento de processo. Para que a mesma apareça deve-se estar em ambiente 3 camadas ou efetuar a configuração dos arquivos .config.

Configurar a data da primeira exceção assim como o horário e marcar as opções dos dias a serem gerado e o intervalo de cada importação. Assim o sistema ira importar o arquivo no intervalo e dias determinados.

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)

**COMUNIDADE **[R@RH](https://totvs.byyou.com/?space=rrh)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 4 – (Recursos Humanos)

*Publicador: Joyce Nereu*

*Código: PTO-00002*
