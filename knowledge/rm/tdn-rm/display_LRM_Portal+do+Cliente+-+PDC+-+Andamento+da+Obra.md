---
content_hash: 23c87c12d7ae348c30afeac0c972873005f3356f9094434f47066a9dafec1e94
fetched_at: '2026-06-29T00:09:47.955052+00:00'
page_id: '435105109'
product: rm
source: tdn-rm
title: Portal do Cliente - PDC - Andamento da Obra
type: documentation
url: https://tdn.totvs.com/display/LRM/Portal+do+Cliente+-+PDC+-+Andamento+da+Obra
version: 6
---

**Andamento da Obra**

Esta funcionalidade permite que a incorporadora, informe aos seus Clientes as etapas de construção do seu empreendimento, exibindo o percentual de completude para cada etapa cadastrada.

Ao acessar esta opção, o Cliente visualizará no topo da página um gráfico com o *Percentual Geral Concluído* e mais abaixo o percentual de andamento de cada uma das etapas que compõem o mesmo.

Cabe ressaltar que o cálculo deste *Percentual Geral Concluído* é obtido através da *S**o**ma de todos os PERCENTUAIS, Multiplicado pelo seu respectivo PESO*, tudo isso divido pela Soma de caba um destes PESOS, conforme exemplificado na consulta abaixo:

Andamento da Obra PDC

SELECT ROUND(SUM(X.PERCENTUAL\*X.PESO)/SUM(X.PESO),2) AS 'ANDAMENTO DA OBRA'  
FROM   (  
                 SELECT    XEMPREENDIMENTOMEDICAO.CODCOLIGADA,  
                           XEMPREENDIMENTOMEDICAO.COD\_PESS\_EMPR,  
                           XEMPREENDIMENTOMEDICAO.CODMEDICAO,  
                           XEMPREENDIMENTOMEDICAO.DESCRICAO,  
                           XEMPREENDIMENTOMEDICAO.PESO,  
                           SUM(XEMPREENDIMENTOMEDICAOVALOR.PERCENTUAL) PERCENTUAL  
                 FROM      XEMPREENDIMENTOMEDICAO (NOLOCK)  
                 LEFT JOIN XEMPREENDIMENTOMEDICAOVALOR(NOLOCK)  
                 ON        XEMPREENDIMENTOMEDICAO.CODCOLIGADA = XEMPREENDIMENTOMEDICAOVALOR.CODCOLIGADA  
                 AND       XEMPREENDIMENTOMEDICAO.COD\_PESS\_EMPR = XEMPREENDIMENTOMEDICAOVALOR.COD\_PESS\_EMPR  
                 AND       XEMPREENDIMENTOMEDICAO.CODMEDICAO = XEMPREENDIMENTOMEDICAOVALOR.CODMEDICAO  
                 WHERE     (  
                                     XEMPREENDIMENTOMEDICAO.MODULO = 2  
                           AND       ((  
                                                         XEMPREENDIMENTOMEDICAO.COD\_PESS\_EMPR = 1)))  
                GROUP BY   XEMPREENDIMENTOMEDICAO.CODCOLIGADA,  
                           XEMPREENDIMENTOMEDICAO.COD\_PESS\_EMPR,  
                           XEMPREENDIMENTOMEDICAO.CODMEDICAO,  
                           XEMPREENDIMENTOMEDICAO.PESO,  
                           XEMPREENDIMENTOMEDICAO.DESCRICAO) X

Cabe ao Administrador do PDC realizar o **cadastro** das informações sobre o *Andamento da Obra* através do menu ***Andamento da Obra*** no acesso da ***Gestão*** deste portal. O cadastro desta informação não é realizado na interface do TCGI.

Ao acessar o menu acima o portal apresenta uma página com a listagem com os andamentos de todos os Empreendimentos parametrizados para serem exibidos no PDC.

Ao editar um destes andamentos, o administrador será redirecionado para a página de cadastro das etapas de avanço de obra, sendo que estas etapas de duas formas diferentes:

* **Manual:** O cadastro de etapa manual é flexível para o administrador informar:
  + **Descrição:** Informe um nome para descrever a etapa cadastrada;
  + **Peso:** Informe o peso desta etapa no andamento da obra;
  + **Ordenação:** Informe a ordem na qual esta etapa será apresentada em relação às demais tarefas;
  + **% Avanço:** Informe o percentual de avança desta etapa.

* **TOTVS Obras e Projetos:** O sistema permite também a importação do cronograma do TOTVS Construção Obras e Projetos. Para realizar esta ação é necessário informar:
  + **Descrição:** Informe um nome para descrever a etapa cadastrada;
  + **Projeto:** Selecione o Projeto do TCOP pesquisando-o no campo destinado a este fim. O administrador precisa ter permissão de acesso ao projeto;
  + **Tarefa:** Selecione a tarefa da Planilha de Atividades, que será importada para o andamento

Adicione a Etapa criada.

Ao clicar no botão "*Importar Cronog. TOP*", o PDC consulta o *Cronograma Realizado* do Projeto selecionado, diretamente no *TOTVS Construção Obras e Projetos* e insere esta informação de acordo com as Etapas adicionadas.

Consegue consultar o Andamento da Obra. Essa tela do Novo PDC esta liberada na versão 12.1.2502 em diante.

Widget - Andamento da Obra

O PDC permite que o gráfico do *Percentual Geral Concluído* do Andamento da Obra seja exibido na página inicial deste portal, na forma de widget, através do menu [Personalizar](https://tdn.totvs.com/display/LRM/Portal+do+Cliente+-+PDC+-+Personalizar).
