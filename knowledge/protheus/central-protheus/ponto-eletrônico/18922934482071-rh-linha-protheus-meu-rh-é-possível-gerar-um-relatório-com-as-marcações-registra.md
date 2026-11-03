---
article_id: 18922934482071
category: PONTO ELETRÔNICO
content_hash: 312c40802dff29610fd61dd2ad1cb46f309ca89207948fac088b69c09b25cee4
fetched_at: '2026-06-28T22:44:36.562091+00:00'
product: protheus
section_id: 10299685322391
source: central-protheus
title: RH - Linha Protheus - Meu RH - É possível gerar um relatório com as marcações
  registradas por Geolocalização
type: support-article
updated_at: '2026-06-16T18:55:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18922934482071-RH-Linha-Protheus-Meu-RH-%C3%89-poss%C3%ADvel-gerar-um-relat%C3%B3rio-com-as-marca%C3%A7%C3%B5es-registradas-por-Geolocaliza%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18922878026007) Tempo aproximado para leitura: **00:06:00 min**  
  
**Dúvida**  
É possível gerar um relatório com as marcações registradas por Geolocalização?  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**  
Não temos um relatório, que seja específico para listagem das marcações, feitas pelo App Meu RH, referente à Geolocalização.  
  
O único relatório que temos, via App Meu RH, para marcações, seria o [Espelho de Ponto](https://tdn.totvs.com/display/NPR/8.0++Consultar+Espelho+Ponto).  
  
No Protheus, há uma rotina em todos os módulos que é a **Consulta Genérica**, ou então a **Consulta Genérica Relacional**, que é possível realizar a extração de um relatório das tabelas envolvidas com este processo.  
  
No caso das marcações realizadas pelo **App Meu RH**, o Protheus possui **três tabelas principais**:  
- **SP8**: Marcações em período de apontamento aberto no Ponto Eletrônico;  
- **SPG**: Marcações em período de apontamento fechado no Ponto Eletrônico;  
- **RS3**: Marcações gravadas pelo App Meu RH, com incidência da Geolocalização.  
  
Inicialmente, é necessário **acessar o SIGACFG - Configurador**, e na rotina **Ambiente > Cadastros > Menus**, inserir as tabelas relacionadas na rotina **Consulta Genérica, no menu do módulo 18 - SIGATCF**, conforme exemplo:  
  
1 - abrir o menu do SIGATCF e em Adicionar, levar o menu para o quadrante direito:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18922925163031)  
  
2 - clicar na rotina Genéricos e em Detalhes:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18922909541143)  
  
3 - selecionar as três tabelas citadas e salvar:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18922939059223)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18922934424087)  
  
4 - salvar o menu com o nome SIGATCF e, reiniciar o Protheus.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18922909547415)  
  
5 - Confirmar a geração do Menu  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18922939067159)  
  
Assim, logar novamente no Protheus, acessar a **rotina de Consulta Genérica**, selecionando a tabela RS3:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18922934432151)  
  
Por fim, basta selecionar a tabela correspondente e, gerar o relatório, conforme necessidade.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18922893073559)  
  
Poderá então, ser gerado em planilha, com ou sem algum filtro, como o exemplo abaixo da RS3:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18922939078039)  
  
O mesmo procedimento, será para a rotina de **Consulta Genérica Relacional**, com a diferença que poderá utilizar uma relação de duas ou mais tabelas, na extração do relatório, com uma ordenação de campos definida.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18922925194903)  
  
Resultado:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18922909557783)  
  
Sendo possível, estas opções em Outras Ações:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18922878060439)  
  
**Saiba Mais**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
