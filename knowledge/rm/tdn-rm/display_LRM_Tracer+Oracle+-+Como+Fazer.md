---
content_hash: 8027683a941304eeb9625f7386203d86c01d8510a27c577050b37cafcf93a151
fetched_at: '2026-06-29T00:09:13.301907+00:00'
page_id: '419542240'
product: rm
source: tdn-rm
title: Tracer Oracle - Como Fazer
type: documentation
url: https://tdn.totvs.com/display/LRM/Tracer+Oracle+-+Como+Fazer
version: 1
---

#### **Utilizando trace em bases Oracle**

### **Utilizando trace em bases Oracle**

Neste artigo, explicaremos como realizar o trace em bases de dados Oracle utilizando o software Statment Tracer for Oracle.  
Trace é um conjunto de instruções SQL disparado pela aplicação durante a sua atividade. Esses comandos são importantes para facilitar o diagnóstico de determinados processos, ajudam na análise de desempenho do sistema, entre outras coisas.  
O download do software Statment Tracer for Oracle pode ser realizado no link a seguir: <http://www.aboves.com/Statement_Tracer_for_Oracle.exe>.  
Seguem os passos para a ativação do trace:

1. Feche todas as aplicações TOTVS linha RM que estiverem abertas na máquina;
2. Clique em Iniciar > Executar e digite services.msc;
3. Selecione o serviço RM.Host.Service
4. Clique com o botão direito sobre o serviço RM.Host.Service e selecione Parar.

1. Inicie o serviço do RM.Host através o executável RM.Host.exe que fica na pasta RM.Net. Por padrão, o diretório criado pela instalação é C:\totvs\CorporeRM\RM.Net, mas em alguns casos ele pode ser alterado pelo usuário;
2. Espere alguns minutos para que o serviço seja iniciado. Quando ativo, ele exibirá um ícone com um check "verde" ao lado do relógio do Windows, como mostra a figura a seguir;

1. Abra o sistema e posicione-se na tela a ser diagnosticada;
2. Execute o Statment Tracer for Oracle e clique Options > Settings, desmarque a opção Prepared SQL statments e clique em OK;

1. Clique no botão start (seta azul) para iniciar a coleta dos dados;
2. Inicie os procedimentos no sistema TOTVS da Lina RM. Exemplo: gere o relatório com problemas de lentidão ou inicie as interações na tela a ser diagnosticada;
3. Ao término do processo, clique no botão pause do Statment Tracer for Oracle para parar a coleta dos dados;
4. Por fim, exporte os dados coletados para um aquivo texto clicando em File > Save logs.

**TKPROF**  
Além do software Statment Tracer for Oracle, existe também o TKPROF, que analisa o trace gerado pela sessão em questão diretamente no Oracle.  
Em alguns casos mais específicos, esse procedimento é melhor que o Statment Tracer for Oracle. No entanto, ele é mais complexo e exige bons conhecimentos no ambiente Oracle. Segue um bom artigo sobre como utilizar a ferramenta TKPROF para o trace de sessões:  
<http://profissionaloracle.com.br/blogs/antognolli/2009/08/30/tkprof/>.  
FONTE: <https://totvs.byyou.com/artigos?&app_ByYouSocialArticle_articleId=495386162&space=rtecnologia-community>
