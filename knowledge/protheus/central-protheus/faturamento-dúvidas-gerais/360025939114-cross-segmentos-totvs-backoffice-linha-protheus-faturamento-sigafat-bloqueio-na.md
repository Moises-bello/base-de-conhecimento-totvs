---
article_id: 360025939114
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 52aef6ca1d6e7b01a03fcc53a447a4b872fb11704a6c6dc0efbf691129685f3f
fetched_at: '2026-06-28T22:38:29.923079+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT)
  - Bloqueio na Tabela SB2
type: support-article
updated_at: '2026-03-24T12:09:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025939114-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Bloqueio-na-Tabela-SB2
---

**Ocorrência**

Ao incluir um pedido de vendas (**MATA410**), liberar o pedido (**MATA440**) ou Faturar o pedido de venda (**MATA461**), onde mais de um usuário esteja manipulando o mesmo produto é gerado um travamento na tabela **SB2**:

![](http://tdn.totvs.com/download/attachments/329024248/image2017-9-27_13-54-38.png?version=2&modificationDate=1515069621000&api=v2)  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-Faturamento (SIGAFAT)-  a partir da versão 12.

**Causa**

No passado a liberação do produto dentro dos processos de pedido de compra e venda, o geração de documento de entrada ou documento de saída, era efetuado por item e agora passou a ser efetuado por documento, causando o travamento na **SB2**.

**Solução**  
  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Verifique a possibilidade de o uso dos pontos de entradas:

**MT103TRV** - <http://tdn.totvs.com/pages/releaseview.action?pageId=45220976> ;

**MT410TRV** - <http://tdn.totvs.com/pages/releaseview.action?pageId=187531533>;

**M461TRV** - <http://tdn.totvs.com/display/public/PROT/M461TRV+-+Libera+a+trava+dos+registros+da+tabela+SB2>  ;

2. Utitlize o parâmetro **MV\_FATTRAV** (<http://tdn.totvs.com/pages/releaseview.action?pageId=233753699>) igual a 4;

3. Dentro da geração da nota de saída, deixe os parâmetros **MV\_GNRENF = .F.** (Ver [DOC0033\_Bloqueio\_Pedido\_de\_Venda\_x\_Tela\_GNRE\_Documento\_de\_Saída](http://tdn.totvs.com/pages/viewpage.action?pageId=235336214)) e **MV\_FISFRAS=.F.** (Ver documento <http://tdn.totvs.com/pages/releaseview.action?pageId=110431290>);

4. Verificar se o mata120 está desatualizado, caso esteja, solicite a equipe de suporte um pacote mais atualizado de acordo com a sua versão;

5. Caso os itens acima não auxiliem no problema de travamento, encaminhe o log profiler e o trace do dbacess para a avaliação da equipe de suporte, em caso de dúvida para extração dos logs, segue documentações:

Log Profiler -**[MP-FAT-Como-habilitar-e-gerar-o-LogProfiler-para-avaliação-de-desempenho-](%C2%A0https://centraldeatendimento.totvs.com/hc/pt-br/articles/115001427728-MP-FAT-Como-habilitar-e-gerar-o-LogProfiler-para-avalia%C3%A7%C3%A3o-de-desempenho-)**

Dbtrace - [**MP-SIGACOM-Como-gerar-o-Log-DbTrace-para-monitorar-baixa-performance-para-rotinas-ADVPL**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024300052-MP-SIGACOM-Como-gerar-o-Log-DbTrace-para-monitorar-baixa-performance-para-rotinas-ADVPL)

Maiores informações sobre bloqueios de registros podem ser obtidos através da FAQ: [**FAT0241 O registro encontra-se Bloqueado por outro usuário**](http://tdn.totvs.com/pages/releaseview.action?pageId=329024248)

Obs: Dentro do processo de Faturamento, uma forma para trabalhar o uso da tabela SB2 e evitar seu travamento é efetuar a atualização do estoque posterior a geração da nota com a opção de atualização de estoque tardia através de JOB, maiores informações, acesse: [**MP - FAT - Atualização de Estoque tardia na geração da NF de Saída MV\_NFS\_JOB**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020914632-MP-FAT-Atualiza%C3%A7%C3%A3o-de-Estoque-tardia-na-gera%C3%A7%C3%A3o-da-NF-de-Sa%C3%ADda-MV-NFS-JOB)
