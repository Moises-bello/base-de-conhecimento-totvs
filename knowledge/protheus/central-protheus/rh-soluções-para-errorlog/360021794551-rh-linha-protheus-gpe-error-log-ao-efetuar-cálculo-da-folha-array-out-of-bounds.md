---
article_id: 360021794551
category: RH - Soluções para error.log
content_hash: 9ec59329ba35ef25bb7a33e873ee2de37614286f5379faa116a8c25233e50184
fetched_at: '2026-06-28T22:44:09.075359+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: RH - Linha Protheus - GPE - Error log ao efetuar cálculo da folha -  Array
  out of bounds [0] of [12] on F_ULTDIA(MATXFUNC.PRX)
type: support-article
updated_at: '2024-05-17T14:36:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021794551-RH-Linha-Protheus-GPE-Error-log-ao-efetuar-c%C3%A1lculo-da-folha-Array-out-of-bounds-0-of-12-on-F-ULTDIA-MATXFUNC-PRX
---

**Ocorrência**Ao efetuar o **cálculo da folha de pagamento** sistema gera o seguinte *log* de ocorrências: ***array out of bounds* [0] *of* [12] *on* F\_ULTDIA(MATXFUNC.PRX)**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para solucionar este erro será necessário efetuar o procedimento abaixo:  
  
1. Renomeie a pasta que contém o **repositório de fórmulas (rpofrm)**, que fica no diretório do RPO do Protheus (ele é gerado a partir das fórmulas e roteiros do SIGAGPE);  
  
2. Renomeie as tabelas de fórmulas e roteiros, para que o sistema recrie no padrão:  
-SRY;  
-SRM;  
-RCA;  
-RC2;  
-RC3.  
  
Acesse o **Configurador (SIGACFG)**, entre em Base de Dados> Dicionários> Base de Dados. Selecione no canto superior esquerdo **Dicionário de Dados** e depois selecione o ícone com o símbolo de lupa:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014191932/mceclip0.png)  
  
Será apresentada a tela abaixo. No campo de pesquisa, digite **SRY** e clique em **Buscar**. Depois selecione o ícone **Editar**:   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014192551/mceclip1.png)  
  
No exemplo abaixo, a tabela SRY possui o nome SRYT10, altere para um nome que não exista em seu ambiente, "SRYT10\_T" por exemplo:  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014193071/mceclip2.png)**Após a alteração, o campo Nome será alterado como SRYT10\_T. Clique em Confirmar:  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014193151/mceclip3.png)**Será apresentado o *browse*novamente. Clique no ícone com desenho Disquete. Será aberta uma nova janela, clique em Avançar em todas as janelas que forem mostradas:  
  
**Esta ação depende de acesso exclusivo:**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014193191/mceclip4.png)  
  
Será apresentada a janela abaixo ao fim do processamento. Verifique se será apresentada a mensagem: **Atualização finalizada com sucesso** e **Finalize**.  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014193211/mceclip5.png)**Após a execução do processo acima com todas as tabelas citadas, entre na rotina de roteiro de cálculo, localizada em Atualizações> Definições de Cálculo> Roteiro de Cálculo, para que as tabelas sejam recriadas. Este processo poderá demorar alguns minutos.   
  
3. Desabilite os pontos de entrada do sistema através da chave **IXBLOG=NORUN** no appserver.ini. Para mais detalhes acesse: <http://tdn.totvs.com/display/public/PROT/Chave+IXBLOG>**ATENÇÃO:** Este procedimento desabilitará os pontos de entrada de todos os módulos, por isso é **imprescindível a execução de todos os processos mencionados neste artigo em ambiente de testes.**   
  
**Observações Importantes:**Após a realização dos testes e análise dos cálculos, retornar os nomes das tabelas e pastas ao originais e desativar a chave IXBLOG.  
  
**Saiba mais**:  
Configuração do Repositório de Fórmulas para ambientes com Balance (balanceamento de carga): <http://tdn.totvs.com/pages/viewpage.action?pageId=208345362>
