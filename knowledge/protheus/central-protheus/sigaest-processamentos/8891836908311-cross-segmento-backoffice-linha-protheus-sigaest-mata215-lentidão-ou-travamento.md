---
article_id: 8891836908311
category: SIGAEST - PROCESSAMENTOS
content_hash: 9ec2a117a345f329343ae052d418ee84772e86ee60e52d63dc171878939eac89
fetched_at: '2026-06-28T22:39:04.931650+00:00'
product: protheus
section_id: 1500001538861
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA215 - Lentidão
  ou Travamento no Processamento Refaz Acumulados/Empenhos
type: support-article
updated_at: '2023-10-31T20:49:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8891836908311-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA215-Lentid%C3%A3o-ou-Travamento-no-Processamento-Refaz-Acumulados-Empenhos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18621095510551) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**

Ao processar a rotina **Refaz Acumulados (MATA215)** ocorre lentidão e/ou travamento na execução. **O que fazer para melhorar a performance ou impedir que a mesma conclua o processamento?**

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

**Importante conhecer o conceito do Processamento:**

O processamento do Refaz Empenhos tem como objetivo refazer os saldos de pedidos, solicitações e ordens de produção dos produtos com base nos seus respectivos movimentos.

Os arquivos refletirão os saldos empenhados, reservados e/ou esperando distribuição.

A rotina Refaz Acumulados deve ser utilizada para **checar/acertar dados que estejam indevidamente gravados nos arquivos**. Os campos a serem avaliados, recalculados e acertados são:

**• Saldos de pedidos e pedidos.**  
**• Quantidades empenhadas em pedidos de venda, não classificadas, reservadas e entradas previstas.**  
**• Quantidades do arquivo de reservas.**  
**• Entradas previstas de O.P. e solicitações de compras.**  
**• Saídas previstas e realizadas por pedidos de venda liberados.**  
**• Requisições empenhadas.**  
**• Movimentos com TES que atualize estoque (F4\_ESTOQUE=S).**

***Portanto*, tal processamento inviabiliza filtros, *o que faz com que seu processamento seja robusto*, normalmente levando mais tempo do que outros processamentos como por exemplo Refaz Salsos (MATA300), Refaz Poder de Terceiros (MATA216) e Refaz Custo de Entrada (MATA190).**

**Enfim, o que avaliar quando a rotina Refaz Empenhos (MATA215) começa a ficar lenta?**

O primeiro ponto fortemente recomendável é entender se houve algum fato relevante no Sistema entre a última vez que o processamento ocorreu em tempo aceitável e o novo processamento que houve queda drástica de performance. As causas mais comuns que começam a onerar este processamento são:

**▸** Fontes do Estoque desatualizados - É recomendável manter os fontes em suas atualizações homogêneas com a aplicação da **[Expedição Contínua do módulo](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/EST_expedicao_continua)**. Há cenários em que determinados clientes atualizam alguns fontes pontualmente enquanto outros ficam desatualizados, gerando este "desbalanceamento" e consequentemente perda de performance em algumas rotinas

**▸** Parâmetro **MV\_A215CHK** desabilitado;

**▸** Atualização de DBAcess e esquecimento da atualização do dbapi.dll da sua pasta para ser atualizado na pasta do AppServer (detalhes em: [MP - FRAME - Arquivo dbapi.dll do DBAccess no AppServer)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028710652-MP-FRAME-Arquivo-dbapi-dll-do-DBAccess-no-AppServer?source=search);

**▸** Artefatos de Framework desatualizados (LIB, Binários e DBAcess) - A recomendação é que eles estejam com sua atualização de até 6 meses do momento atual (sendo que o recomendável é sempre mantê-los atualizados) - Para atualizar estes artefatos, [clique aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=550332596);

**▸**Customizações influenciando no processo. Portanto, é sugestivo testar o ambiente padrão [desabilitando customizações](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021114292) para averiguação se o tempo de processamento cai;

**▸** Fragmentação de tabelas responsáveis durante o processamento (as tabelas que são cosumidas nos processamentos podem ser identificadas pelo **[DBTrace](MP%20-%20FIS%20-%20Como%20Gerar%20o%20Log%20DbTrace%20Para%20Monitorar%20Baixa%20Performance?)** - mas o processo de desfragmentação é de responsabilidade do DBA/Consultor DBA da empresa).

**▸** Recomendamos fortemente seguir [**estas dicas (clique aqui)**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017515552-MP-FRAME-Lentid%C3%A3o-no-Protheus-12) para ter um ganho de performance no processamento.

**▸** Avaliar se o ambiente esta configurado para utilização de Broker, recomendamos efetuar testes com e sem o Broker e validar se tem o mesmo comportamento. [**Clique aqui**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040589613-MP-FRAME-Como-realizar-uma-configura%C3%A7%C3%A3o-b%C3%A1sica-de-Broker-) e veja o artigo sobre o Broker.

**▸** Avaliar se o ambiente trabalha com produtos que controlam Lote e/ou Endereço e se constam registros com desbalanceamento de Saldos entre as tabelas. [**Clique aqui**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11594542049559-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Inconsist%C3%AAncia-de-saldos-gravados-Desbalanceamento-entre-Tabelas-de-Estoque) e veja detalhadamente como analisar.

**Caso,** **mesmo com as** **orientações acima** **não houver ganho de Performance, acione a Equipe de Suporte do módulo de Estoque/Custos encaminhando:**

**▸ Informações sobre tempo médio padrão do processamento e tempo médio atual;**

**[▸ LogProfiler](https://tdn.totvs.com/display/public/framework/LogProfiler+-+Como+executar) e [Trace](MP%20-%20FIS%20-%20Como%20Gerar%20o%20Log%20DbTrace%20Para%20Monitorar%20Baixa%20Performance?) do processamento da rotina MATA215.**

**▸ Filtrar pela APSDU na tabela CV8 pelo campo CV8\_PROC igual a MATA215 e exportar em .dtc (print abaixo), essa tabela é importante enviar devido conter o log de processamento da rotina, facilitando a identificação da lentidão ou até mesmo algum erro que pode estar impactando;**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18621363158295)**

**Com essas informações, nossos analistas avaliarão se há alguma função ou tabela/campo/query que esteja influenciando na queda de performance para melhor apoio.**

**Saiba mais:**

[*SIGAEST - Como habilitar e gerar o LogProfiler?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019902592-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-habilitar-e-gerar-o-LogProfiler-?source=search)

[*Clique aqui e veja mais artigos sobre Processamentos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538861-SIGAEST-PROCESSAMENTOS)
