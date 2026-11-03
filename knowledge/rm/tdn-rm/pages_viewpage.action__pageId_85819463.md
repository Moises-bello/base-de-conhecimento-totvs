---
content_hash: c95fcb2bb418bf99c020fbe824e98a21323dac7a9a8c18136d599c8b12b95a43
fetched_at: '2026-06-29T00:11:54.852214+00:00'
page_id: '85819463'
product: rm
source: tdn-rm
title: Como Fazer- Integração com o TSA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=85819463
version: 11
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Automação de Ponto                      **Versão:**11.8X |
| **Processo** | **:** | Integração Com TSA |
| **Subprocesso** | **:** | Parametrização Para Integração |
| **Data da publicação** | **:** | 10/10/2013 |

#### Introdução

*Neste "Como Fazer" será apresentado todas as parametrizações necessárias nos produtos da linha RM para integração com o TSA.* 

#### Informações Gerais

*- O TSA possui integração com os seguintes dispositivos REP's: Dimep, Henry, Topdata, Madis Rodbel e telemática.*

#### Iniciando a parametrização da base

*- Copiar a pasta TSA (antiga TSA-TSREP)* *para unidade C.*

* *Abra a pasta TSA, edite o arquivo ALIAS.DAT e informe os dados da base de dados.*
* *Ainda na pasta TSA, edite o arquivo WEB.CONFIG, informe o nome do ALIAS criado no arquivo ALIAS.DAT , altere também a informação sobre o nome do servidor onde o TSA está instalado e a porta.*  
  *Por default o arquivo WEB.CONFIG virá com RM0005430:9595 substitua pelos dados do servidor e porta.*
* *Acessar IIS para inclusão de um diretório virtual (máquinas com Sistema Operacional XP) ou**Adicionar aplicativo (Máquinas com sistema**Operacional Vista e 7).*  
  *Obs.: Demonstração para Vista ou 7.*  
    
    
    
  *Clicar em OK.*  
    
    
  *Obs.: Demonstração para XP.*
* *Clicar em Sim.*  
    
    
  *Versão do APS.NET tem que ser 4.0.303.19.*  
    
  *- Copiar os scripts e o arquivo de fórmulas visuais para tua máquina. Os arquivos são:*  
  *Scripts : Para banco Oracle (xsltsEntidades11.40\_Oracle.sql)*  
  *Para banco Oracle (ImportacaoTabela\_TSA(Oracle.sql))*  
  *Para banco SQL (xsltsEntidades11.40\_SQL.sql)*  
  *Para banco SQL (ImportacaoTabela\_TSA(SQL).sql)*  
  *Fórmulas Visuais: TSA - Fórmula Visual 1140 22.12.2011.totvsWF*  
    
    
  *- Executar o script "xsltsEntidades11.40" na base de dados RM.*  
    
    
    
    
  *- Executar o script "ImportacaoTabela\_TSA" na base de dados RM.*  
    
    
    
    
  *- Toda a parametrização a seguir deverá ser realizada na nova MDI. Para acessar a nova MDI**localize a pasta RM. NET e execute o arquivo "RM.exe".*  
    
  *- Será apresentada a tela para login.Se necessário, crie um Alias para acesso a base de dados RM.*  
    
    
    
    
    
    
    
    
  *- Acessar o produto "Serviços Globais" para definir as permissões de acessos aos menus que serão utilizados durante o procedimento de parametrização dos produtos da linha RM.*  
    
    
  *- Verificar os perfis associados ao usuário logado.*  
    
    
    
    
  *- Acesse cada um dos perfis associados ao usuário e dê permissão ao item 02.01.02.*  
    
    
    
  *- Recolha tudo. Expanda os itens 02 e 02.01 e permita acesso ao item 02.01.02.*  
  *Visão Antes*  
    
  *Visão Depois*  
    
    
    
  *- À medida que forem encontrando itens sem permissão, acesse o módulo "Serviços Globais", e dê permissão ao menu desejado.*  
  ***- Configurar o WebService no Conector***  
  *Conector é o produto responsável por transformar as mensagens enviadas do RM para o padrão requerido pelo TSA, pra isto são necessárias algumas configurações gerais, que serão apresentadas no fluxo de telas abaixo.*  
    
    
    
    
    
    
    
  *- Preencha as informações conforme tela a seguir.*  
    
  *Dados da Url para cópia:*[*http://localhost/TSA/TSService.asmx*](http://localhost/TSA/TSService.asmx)  
    
    
    
    
    
    
  *- Acessar o sistema de Automação de Ponto.*  
    
    
    
    
    
    
    
    
    
    
    
    
  *- Antes de realizar importação de fórmulas visuais é preciso proceder à verificação da base para visualizar e acertar todos os erros relativos a horários, erros nos horários cadastrados na base impedirão a finalização do processo de importação/execução das fórmulas visuais.*  
    
    
    
    
    
    
    
    
  *- O resultado da verificação da base será apresentado conforme tela a seguir, veja o que foi listado e proceda com as correções.*  
    
    
  *- Acessar Automação de Ponto para importação das fórmulas visuais.*  
    
    
    
    
    
    
    
    
    
  *- Será aberta uma janela para buscar o arquivo já salvo em tua máquina contendo as fórmulas visuais.*  
    
    
    
    
    
    
    
    
  *- Editar a categoria criada para TSA/TSREP*  
    
    
    
  *- Acessar a guia "Perfis de Categoria da Fórmula Visual" e realizar a inclusão de todos os perfis associados ao usuário que está realizando a parametrização para a integração.*  
  *Exemplo: O usuário mestre possui s seguintes perfis marcados: Dba e Mestre.*  
  *Então nesta janela deverão ser incluídos os perfis Dba e Mestre (RM Chronus).*  
    
    
    
    
  *- Ao voltar na visão de Fórmula Visual, será possível visualizar todas as fórmulas importadas.*  
    
    
    
  *- Crie as seguintes pastas:*  
  *Na unidade C:, criar a pasta "LogTSATSREP"*  
  *No caminho C:, pasta**LogTSATSREP e Criar as pastas "TSA" e "TSAREP"*  
    
    
    
  *- Execução da fórmula visual de carga inicial.*  
  *A fórmula "Carga Inicial – TSA" é a responsável pela carga inicial da base do TSA com as informações presentes nos produtos da linha RM.*  
    
  *- Acessar RH -> Folha de Pagamento -> Administração de pessoal -> Seções*  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  *- Agora iremos associar todas as fórmulas visuais responsáveis por atualizar a base do TSA com qualquer alteração feita nos cadastros do RM e que sejam necessárias de replicação.*  
    
  ***Fórmula Visual: Empresa – TSA***  
  *Atualiza o TSA com qualquer alteração feita nas coligadas da Linha RM.*  
  *- Acessar Serviços Globais -> Coligadas*  
    
    
    
    
    
    
    
  ***Fórmula Visual: Seção – TSA/TSREP***  
  *Atualiza o TSA com qualquer alteração feita no Cadastro de Seção da Linha RM.*  
  *- Acessar RH -> Folha de Pagamento -> Administração de Pessoal -> Seções*  
    
    
    
    
    
    
    
  ***Fórmula Visual: Função Labore – TSA***  
  *Atualiza o TSA com qualquer alteração feita no Cadastro de Função do RM Labore*  
  *- Acessar RH -> Folha de Pagamento -> Administração de Pessoal -> Cargos/Funções -> Funções*  
    
    
    
    
    
  ***Fórmula Visual: Centro de Custo – TSA***  
  *Atualiza o TSA com qualquer alteração feita no Cadastro de Centro de Custo do RM Labore. Esta informação refletirá no TSA apenas para Centro de Custos que estejam associados à seção (pasta Dados Contábeis) que possuem funcionários que batem ponto.*  
  *Obs.: A Opção Centro de Custo RM Labore foi migrada a partir da versão 11.50.*  
  *A associação da fórmula visual se dará dentro do módulo Folha de Pagamento, Opção Centro de Custo, semelhante ao que foi feito com as demais fórmulas, ou seja, acessar Processos -> Fórmula Visual -> Gerenciar.*  
    
    
    
  ***Fórmula Visual: Afastamento – TSA***  
  *Atualiza o TSA com qualquer alteração feita na tela de Histórico de Afastamento do RM.*  
  *- Acessar**RH -> Folha de Pagamento -> Administração de Pessoal -> Funcionários -> Anexos -> Históricos - > Históricos de Afastamentos*  
  *Obs.: Ao cadastrar o afastamento no funcionário o campo "Observação" é de preenchimento obrigatório, pois sem esta informação o registro de afastamento não será atualizado no TSA.*  
    
    
    
    
    
    
    
    
  ***Fórmula Visual: Funcionário – TSA***  
  *Mantém atualizada a base do TSA com todas as informações alteradas na tela de Cadastro de Funcionário.*  
  *- Acessar RH -> Folha de Pagamento -> Administração de Pessoal -> Funcionários.*  
    
    
    
    
    
    
  ***Fórmula Visual:******Alteração Chapa Funcionário – TSA***  
  *Atualiza o TSA com as alterações de chapas.*  
  *- Acessar RH -> Folha de Pagamento -> Administração de Pessoal -> Funcionários.*  
    
    
    
    
    
  ***Fórmula Visual:******Alteração do Código da Seção - TSA/TSREP***  
  *Atualiza o TSA com as alterações nos códigos de seção.*  
  *- Acessar RH -> Folha de Pagamento -> Administração de Pessoal -> Seção.*  
    
    
    
    
    
    
    
  ***Fórmula Visual: Feriado – TSA***  
  *Atualiza o TSA com as alterações feitas no cadastro dos feriados da coligada.*  
  *- Acessar RH -> Automação de Ponto -> Cadastros -> Feriados.*  
    
    
    
    
    
    
    
    
    
    
  ***Fórmula Visual: Cópia de Feriado – TSA***  
  *Atualiza o TSA referente a cópia de Feriado entre calendários.*  
  *- Acessar RH -> Automação de Ponto -> Cadastros -> Feriados*  
    
    
    
    
    
    
  ***Fórmula Visual: Exceção Horário Alternativo – TSA***  
  *Atualiza o TSA com qualquer alteração no horário alternativo do funcionário feitas no RM.*  
  *- Acessar RH -> Automação de Ponto -> Funcionário -> Anexos -> Horário Planejado -> Horário Alternativo*  
    
    
    
    
    
    
  ***Fórmula Visual: Exceção Horário Programado – TSA***  
  *Atualiza o TSA com qualquer alteração no horário programado do funcionário feitas no RM.*  
  *- Acessar RH -> Automação de Ponto -> Funcionário -> Anexos -> Horário Planejado -> Horário Programado.*  
  *Obs.: Ao cadastrar um horário programado é preciso marcar a opção "Aprovado", pois sem esta informação o registro de afastamento não será atualizado no TSA.*  
    
    
    
    
    
    
    
    
  ***Fórmula Visual: Turno por Jornada – TSA***  
  *Atualiza o TSA com qualquer alteração feita na tela de Turno por Jornada do RM*  
  *- Acessar RH -> Automação de Ponto -> Horário por Jornada*  
    
    
    
    
  ***Fórmula Visual: Escala – TSA***  
  *Atualiza o TSA com quaisquer alterações realizadas nos índices dos horários por Jornada.*  
  *- Acessar RH -> Automação de Ponto -> Cadastros -> Horário por Jornada -> Anexos -> Índice da Jornada.*  
    
    
    
    
    
    
    
  ***Fórmula Visual: Turno por Intervalo – TSA***  
  *Atualiza o TSA com qualquer alteração feita na tela de Turno por Intervalo do RM*  
  *- Acessar RH -> Automação de Ponto -> Horário por Intervalo*  
    
    
    
    
    
    
    
    
  ***Fórmula Visual: Escala Intervalo – TSA***  
  *Atualiza o TSA com quaisquer alterações realizadas nas jornadas cadastradas no horário.*  
  *- Acessar RH -> Automação de Ponto -> Cadastros -> Horário por Intervalo -> Anexos -> Jornadas.*  
    
    
    
    
    
    
    
    
    
  ***Fórmula Visual: Histórico de Horário Intervalo***  
  *Atualiza o TSA com qualquer alteração feita na tela de Histórico de Horário por Intervalo do RM.*  
  *- Acessar RH -> Automação de Ponto -> Funcionários -> Anexos -> Horário planejado -> Histórico De Horários.*  
    
    
    
    
    
  ***Fórmula Visual: Histórico de Horário Jornada***  
  *Atualiza o TSA com qualquer alteração feita na tela de Histórico de Horário por Jornada do RM.*  
  *- Acessar RH -> Automação de Ponto -> Funcionários -> Anexos -> Horário planejado -> Histórico De Horários da Jornada.*  
    
    
    
    
    
    
    
  ***Fórmula Visual: Função – TSA***  
  *Atualiza o TSA com qualquer alteração na tela de Função feita no RM.*  
  *- Acessar RH -> Gestão de Pessoas -> Planejamento e Captação -> Funções*  
    
    
    
    
    
    
    
    
    
    
    
  *- Parametrização da Importação de batidas, temos duas possibilidades:*  
  *1º) Agendar o processo de importação de batidas. A tela de agendamento só estará disponível em ambiente 3 camadas.*  
  *Dúvidas sobre parametrização de ambiente 3 camadas consultar o link*[*http://totvsconnect.blogspot.com/2010/10/como-fazer-configuracao-do-jobserver-3.html*](http://totvsconnect.blogspot.com/2010/10/como-fazer-configuracao-do-jobserver-3.html)*.*  
  *2º) Importação iniciada pelo usuário.*  
  *- Acessar RH -> Automação de Ponto*  
    
    
    
    
    
    
    
  *Obs.: Em ambiente parametrizado para se trabalhar em 3 camadas, teremos na tela de Importação de batidas no lugar do botão Executar a opção "Avançar" , clicando em Avançar será apresentada a tela de agendamento da importação com várias opções.*

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)

**COMUNIDADE **[R@RH](https://totvs.byyou.com/?space=rrh)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 4 – (Recursos Humanos)

*Publicador: Joyce Nereu*

*Código: PTO-00001*
