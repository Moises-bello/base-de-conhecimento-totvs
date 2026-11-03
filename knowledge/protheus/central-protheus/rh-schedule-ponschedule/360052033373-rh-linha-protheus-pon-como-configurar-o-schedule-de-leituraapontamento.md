---
article_id: 360052033373
category: RH - Schedule (PONSCHEDULE)
content_hash: f530b8a67bce6ac4a6f76dec37e56f5fe99bb315c3514193edaf20b193641ea5
fetched_at: '2026-06-28T22:44:42.697018+00:00'
product: protheus
section_id: 32419396129943
source: central-protheus
title: RH - Linha Protheus - PON - Como configurar o Schedule de Leitura/Apontamento
type: support-article
updated_at: '2026-04-01T12:21:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052033373-RH-Linha-Protheus-PON-Como-configurar-o-Schedule-de-Leitura-Apontamento
---

**Dúvida**  
Como configurar o *Schedule* de Leitura/Apontamento?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
**1.** Por ser uma rotina customizável (RDMake) é necessário compilar o fonte **PONWORK.PRX** e os arquivos de tradução **.TRES** como o **PONWORK\_PT-BR.TRES** no ambiente, pois a rotina não está presente no repositório padrão. Para isto, baixe a expedição do RH e na pasta RDMAKEs baixe os arquivos correspondentes em seu projeto da ferramenta de compilação(VS CODE).   
[Pacote da expedição RH](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/rh_expedicao)  
  
Em caso de dúvidas sobre processo de compilação via VS CODE entre na comunidade do [GITHUB.](https://github.com/)  
  
Antes de executar a rotina **verifique no inspetor de objetos se estão compilados os arquivos de tradução dos idiomas utilizados**executar a rotina sem esses arquivos pode ocasionar erros.  
![](https://tdn.totvs.com/download/attachments/631321258/image-2025-6-25_10-52-42.png?version=1&modificationDate=1750859562724&api=v2&effects=drop-shadow)  
  
**2.** Configurar os **serviços** no **Appserver.ini** conforme exemplo abaixo:  
  
**[OnStart]**  
jobs=FWSCHDMANAG,FWSCHDQUEUE    
RefreshRate=180

**[FWSCHDMANAG]**  
Main=FWSCHDMANAG  
Environment=P1225(inserir o nome do seu ambiente)

**[FWSCHDQUEUE]**  
Main=FWSCHDQUEUE  
Environment=P1225(inserir o nome do seu ambiente)  
       
**3.** **Configurar** inicialmente os processadores de **Agendamento/*****Agents***. Para isso, siga os passos abaixo:  
- Acessar o **Configurador** na rotina **Ambiente>*****Schedule>Schedule***;  
- Acesse na aba lateral esquerda a opção ***Agents*****:**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/38160547378583)**  
  
- No menu superior, clique na opção **outras ações>Adicionar Agentes padrão.**   
\*\*Estes***agents*** serão os **responsáveis** por **executar** os **processos agendados**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38160531013271)  
  
**4.** Iniciar os Agents:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38160547382167)  
  
**5.** Após isso, será necessário configurar o **Agendamento** e sua **recorrência** (quantidade de vezes em que o *job* será executado durante o dia):  
- Acesse na aba lateral esquerda a opção **Agend.:**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/38160531015575)**  
  
- Clicar em **Novo** para incluir um novo agendamento:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38160531016727)  
  
**-** Na tela inclusão de agendamento, será necessário preencher com a função **U\_PONSCHEDULER** e os parâmetros desejados e após isso, clicar em avançar e cofigurar a recorrência. Segue um exemplo abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38160531018135)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38160531019927)  
  
Incluir as informações conforme seu ambiente e avançar para concluir a inclusão do agendamento:  
***Importante: Não é possível editar parâmetros no botão abaixo, pois os parâmetros são incluídos na inclusão da rotina de agendmamento:***![](https://centraldeatendimento.totvs.com/hc/article_attachments/38160531020951)  
  
**6. Sobre os parâmetros a serem utilizados, exemplo:**  
**U\_PONSCHEDULER("T1", "D MG 01", , .T., .T., .F., .T., .F., "3", "2",,, 1)**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18949474907159)  
  
Se os parâmetros que não são obrigatórios não forem preenchidos, o agendamento será executado da mesma forma, ou seja, é necessário apenas que sejam informados os códigos do Grupo de Empresas e da Filial.  
  
Abaixo, um detalhamento do funcionamento dos parâmetros:  
**-** **Efetuar a leitura e apontamento por filial?**  
-> Quando definido com **.T.** o sistema irá executar a função PONM010 para cada filial, preenchendo as perguntas Filial De? e Filial Até? com o mesmo conteúdo.  
-> Quando definido com **.F.** o sistema irá executar a função PONM010 apenas uma vez sem filtrar as filiais, deixando a pergunta Filial De? em branco e a pergunta Filial Até? com "ZZZZZ".  
  
**- Processa apenas a filial passada como parâmetro?**  
-> Quando definido com **.T.** o sistema irá executar a função PONM010 apenas para a filial enviada no parâmetro 02.  
-> Quando definido com **.F.** o sistema irá executar a função PONM010 para todas as filiais da empresa.  
  
O sistema busca o período definido nos parâmetros **MV\_PONMES e MV\_PAPONTA** e com base nas datas, define os períodos que serão processados até o período atual, de acordo com a data de execução. Exemplos:

Período definido nos parâmetros: **01/08/2023 - 31/08/2023**  
Data de execução do Schedule: 03/10/2023  
Parâmetro Limitar a data final do apontamento a data base do sistema?:  **.T.**  
Períodos que serão processados:

01/08/2023 - 31/08/2023  
01/09/2023 - 30/09/2023  
01/10/2023 - 03/10/2023

Período definido nos parâmetros: **16/08/2023 - 15/09/2023**  
Data de execução do Schedule: 14/10/2023  
Parâmetro Limitar a data final do apontamento a data base do sistema?: **.F.**  
Períodos que serão processados:

16/08/2023 - 15/09/2023  
16/09/2023 - 15/10/2023

Caso queira implementar uma regra diferente para definir os períodos de apontamento que serão processados pela rotina, pode-se customizar a função ***Monta\_Per*****presente na rotina PONWORK.**  
  
\*\****Importante: Para clientes que efetuarão a leitura/apontamento através do arquivo AFD (arquivo TXT):***  
***- esse arquivo deve estar dentro do diretório system e apontado corretamente no*** [***cadastro de relógio***](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004209412-RH-Linha-Protheus-PON-Como-efetuar-o-cadastro-do-Rel%C3%B3gio-de-Ponto)***;***  
***- Cliente que possuem o ambiente no CLOUD da TOTVS, devem solicitar que seja mapeado uma pasta dentro do diretório system com permissão para edição.***  
  
**Saiba mais,**  
[Leitura Automática das Marcações Utilizando o Schedule](https://tdn.totvs.com/pages/releaseview.action?pageId=631321258)  
[Manual do Ponto Protheus](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[PON-Rotina-Período-de-Apontamento-PONA290](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059188733-RH-Linha-Protheus-PON-Rotina-Per%C3%ADodo-de-Apontamento-PONA290)  
[PON-Como utilizar os parâmetros de Período MV\_PONMES e MV\_PAPONTA para Leitura e a tabela-SPO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045460153-RH-Linha-Protheus-PON-Como-utilizar-os-par%C3%A2metros-de-Leitura-e-a-tabela-SPO-respons%C3%A1vel-pelo-fechamento-mensal)
