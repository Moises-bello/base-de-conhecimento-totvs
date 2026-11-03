---
article_id: 4405662700311
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 226cb69e153ee0184d286e10aa2dfc34bbb738468f6f77e12036a292a80c880b
fetched_at: '2026-06-28T22:38:44.083174+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Melhoria de Performance na
  geração do documento de saída
type: support-article
updated_at: '2024-02-23T17:38:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405662700311-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Melhoria-de-Performance-na-gera%C3%A7%C3%A3o-do-documento-de-sa%C3%ADda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21571933574935) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como se pode melhorar a performance da geração do documento de saída (MATA461)?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

Para o tratamento de baixa performance na geração da nota fiscal de saída, avalie:

**1** - Desabilitar os parâmetros abaixo:

* **MV\_FISFRAS** - Este parâmetro trata o **FCI** de produtos com rastreabilidade, sendo que uma vez que está habilitado deixará o processo moroso;
* **MV\_GNRENF**- Este parâmetro faz com que no momento da preparação da nota de saída, quando a pergunta Gera Guia? está igual a Sim, é aberto uma tela para preenchimento da **GNRE** **on line**, enquanto esta tela está aberta o processo de geração de nota não finaliza, gerando morosidade no processo. Uma vez desabilitado, o cliente pode gerar a **GNRE** via **Livros Fiscais**.
* **MV\_FINATFN-**realize um teste com conteúdo = 2) - Este parâmetro define se a atualização do fluxo de caixa será online ou offline.
* **MV\_LOGMOV -**Este parâmetro tem como função rastrear as divergências nas movimentações de lote e/ou endereço, uma vez habilitado gera morosidade no processo da geração da nota. Saiba mais: **[MP - SIGAEST - Este artigo tem como objetivo de explicar o uso do parâmetro MV\_LOGMOV.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011922091-MP-SIGAEST-Este-artigo-tem-como-objetivo-de-explicar-o-uso-do-par%C3%A2metro-MV-LOGMOV-)**

**2** - Ajustar a compatibilidade das tabelas de contábil: Se ao avaliar o logprofile ou mesmo for verificado muitas chamadas relacionadas as tabelas de CTB, como a tabela **CT1, CTV** ou **CQD, CTG**, com compartilhamentos diferentes. Para avaliação e tratamento das tabelas contábeis, consulte link a seguir, com a orientação do Módulo CTB:

**<http://tdn.totvs.com/display/public/PROT/CTB0012_Compartilhamento_de_tabelas_SIGACTB>**

**3 -** Desabilitar a Contabilização on line através dos parâmetros de preparação da nota abaixo. A contabilização poderá ser efetuada de forma off-line em Miscelâneas/Fechamento/Contabilização Off-line dos Documentos de Saída.

![](https://tdn.totvs.com/download/thumbnails/525797678/image2021-6-2_16-21-44.png?version=1&modificationDate=1622661705033&api=v2)

**4** - Atualizar de Binários, Dbaccess e Lib: Avalie no exportar dados se o Dbaccess,o Binário (Server e Smartclient) e as Libs estão atualizadas conforme o portal do cliente, caso não esteja, efetue a atualização os links do portal do cliente, é imprescindível que o ambiente esteja atualizado para uma performance adequada do sistema e para o caso do suporte precisar gerar uma avaliação de performance no desenvolvimento,

Link Geral:

AppServer: **<https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/>**

Smartcliente: **<https://suporte.totvs.com/portal/p/10098/download#000006/368/TFSC/>**

Libs: **<https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/>**

Dbaccess: [**https://suporte.totvs.com/portal/p/10098/download#000006/368/TFDBA**/](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFDBA/)

**5 -** Configurar a conexão do ambiente no **ODBC** conforme a imagem em abaixo.  
A orientação da equipe de tecnologia é de que seja criado com o ***SQL Server Native Client*** para melhor performance.

[![](https://lh3.googleusercontent.com/-AkwXzjw9An8/XhSOUWHrC-I/AAAAAAAAAk8/QxIYq6SK15sJnEiIGAasIJIHblMvfVdhwCK8BGAsYHg/s470/2020-01-07.png)](https://lh3.googleusercontent.com/-AkwXzjw9An8/XhSOUWHrC-I/AAAAAAAAAk8/QxIYq6SK15sJnEiIGAasIJIHblMvfVdhwCK8BGAsYHg/s0/2020-01-07.png)

**6 -** Atualização do ambiente Faturamento com o pacote de expedição contínua do módulo. A equipe de Desenvolvimento de produto efetuou tratamentos de melhoria na rotina  no final 2020 e inicio de 2021, portanto é importante a atualização para garantir o uso dessas melhorias no ambiente:

Link : **[SIGAFAT](https://tdn.totvs.com/pages/releaseview.action?pageId=521997859)**

O link encaminha para a página de atualização do desenvolvimento de produto Faturamento, onde contém as atualizações para as releases vigentes.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405661271447)

**7 -** Desabilitar pontos de entrada: caso possua chamada de ponto de entrada no ambiente, desabilite a chamada do ponto de entrada, podendo descompilar do RPO ou desabilitar via catálogo de personalizações do Configurador (XX7), para certificar que a customização por ponto de entrada não esteja influenciando no processo.

Importante: é necessário desabilitar os pontos de entradas, pois em caso de enviar a avaliação de performance para o desenvolvimento de produto , a avaliação poderá ser rejeitada se for constatado chamadas de ponto de entrada no processo.

Caso o processo seja efetuado via execauto e esse execauto estiver lento, neste caso a avaliação do processo será direcionada para a equipe de suporte de atendimento ADVPL.

**8 -** Avalie se a procedure do processo 14 está ativa, embora o faturamento não utilize procedures, existe uma chamada ao processo 14 que é efetuada pelo fonte **MATXFUNB**, que é um fonte genérico no sistema e que afeta o processamento da nota. Via configurador, Base de dados, Stored Procedures (**CFGX051**),opção instalar e habilite a procedure , a ativação deixará mais ágil o processamento de nota.

![](https://tdn.totvs.com/download/attachments/525797678/image2019-12-10_9-8-4.png?version=1&modificationDate=1575983284567&api=v2)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405661937047)

**9 - Campos virtuais utilizando a função Posicione?**

Verifique se a tabela que está sendo solicitada no processamento possui campos de usuários virtuais e que utilizem a chamada da função Posicione. 

Desabilite o campo ou retire a chamada do posicione do campo virtual.

 Para validar a função Posicione, efetue o procedimento da documentação: **[MP-ADVPL-Validar-função-Posicione?source=search](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029397891-MP-ADVPL-Validar-fun%C3%A7%C3%A3o-Posicione?source=search)**

**Importante**: Se mesmos efetuando os procedimentos acima, ainda houver baixa performance, acessar a FAQ **[OINF0004 - Avaliação de performance para rotinas do Protheus](https://tdn.totvs.com/pages/viewpage.action?pageId=274854325#1-PANEL2)**  e encaminhar para avaliação do suporte através de ticket de atendimento para baixa performance:

* Questionário de Performance Respondido;
* Evidência de teste (contemplando todas as configurações necessárias para chegar no mesmo cenário do problema);
* Envio de Logs( Profile, Dbtrace, TraceStack)
* Exportar dados
