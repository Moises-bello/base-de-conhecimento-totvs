---
article_id: 36290822157975
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: ae68eccfa7c21f60588655cf474d77ac3898785a886eee3c8ec2b0ac84697297
fetched_at: '2026-06-28T22:37:21.429095+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - CNTA121 - Lentidão
  na rotina de Medição de Contratos
type: support-article
updated_at: '2026-05-14T20:11:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36290822157975-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-CNTA121-Lentid%C3%A3o-na-rotina-de-Medi%C3%A7%C3%A3o-de-Contratos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36290822144663) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**

Na realização do Processo de Medição, na Inclusão, Encerramento ou Estorno, ao confirmar a execução da rotina apresenta lentidão ao confirmar a execução da operação. O que fazer?

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões]

**Solução**

Para dar inicio a validação da questão apresentada, deve-se primeiro validar se o ambiente em questão se encontra com as últimas atualizações disponibilizadas no portal do cliente, em relação aos módulos BACKOFFICE, SIGAGCT e artefatos:

- [Acumulado Compras/Backoffice conforme sua versão](https://tdn.totvs.com/pages/releaseview.action?pageId=522011099)

- [Acumulado Gestão de Contratos conforme sua versão](https://tdn.totvs.com/pages/viewpage.action?pageId=679961416)

- [LIB Atual](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/) - [Harpia](https://suporte.totvs.com/portal/p/10098/download?e=1050526) | [Onca](https://suporte.totvs.com/portal/p/10098/download?e=1168735)

- [Appserver](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/) - [Harpia R.33](https://suporte.totvs.com/portal/p/10098/download#detail/1112215) | [Onca](https://suporte.totvs.com/portal/p/10098/download?e=1168420)

- Smartclient WebApp - [Onca](https://suporte.totvs.com/portal/p/10098/download?e=1168455)

- DBAccess - [MP - FRAME - Atualização do DBAccess](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033789713-MP-FRAME-Atualiza%C3%A7%C3%A3o-do-DBAccess?source=search)

Não é comum a ocorrência de tempo elevado no processo de inclusão, no encerramento  ou mesmo no estorno do encerramento na rotina de medição de contratos, por isso a validação inicial das atualizações é o primeiro passo a ser efetuado.

Efetue a validação se o ambiente se encontra atualizado, mas se mesmo assim o processamento é lento:

- Aguardar até que seja carregado, ou esperar o tempo médio de carregamento que era feito antes.

- Reiniciar os serviços do ambiente, ou maquina em questão, pois possa ser um problema relacionado a infraestrutura.

Caso ainda assim se encontre lento o Processo, o Próximo passo é a realização do teste em um ambiente de sem customizações:

- Realize o teste com todas as customizações do ambiente desabilitadas **(não somente pelo IXBLOG, mas também pela XX7 com X7\_STATUS = 2 pra todos registros), impreterivelmente pelas 3 formas do artigo abaixo**:

Procedimentos para desativar as customizações:  
1 - [MP - Como ativar e desativar customizações no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021114292)

Retirar campos e gatilhos customizados:

    - Caso ainda reproduza, desabilitar também os campos e gatilhos customizados deletando do ambiente de homologação os registros da SX3 e SX7 com X3\_PROPRI e X7\_PROPRI = U

Após a reinicialização, o carregamento foi concluído, mas esta lento na sua opinião? Então devemos efetuar uma analise do Logprofiler + Dbtrace. Abaixo vídeo de como efetuar a coleta desses arquivos, para envio e analise do suporte. (sugestível ser efetuado o processo pelo seu departamento de T.I)

Além do seguinte arquivo importante para analise do Suporte:

**Habilitar TraceStack e Analisar Logs:**   
É necessário habilitar a chave TraceStack no arquivo appserver.ini em um ambiente isolado, conforme a documentação em [TraceStack](https://tdn.totvs.com/display/tec/TraceStack).

Após habilitar a chave TraceStack, faça um backup do arquivo console.log e reinicie o sistema para que seja gerado um novo arquivo.

Depois de reiniciar o sistema em mono usuário, acesse a rotina novamente e execute o processo que ocorre  a lentidão.

Durante esse período, verifique se algum erro é gerado no arquivo console.log e pode enviar o erro em txt, juntamente com os arquivos de LogProfiler e DbTrace ao fazer a abertura do ticket ao Suporte.

Videos para geração de LogProfiler: e DBTrace

**Obs:**

Em situações que gera a lentidão e depois trava e o sistema cai para que possamos analisar se é travamento ou  lentidão.

Realizar os procedimentos abaixo e abrir o ticket em um de nossos canais de atendimento para a equipe Protheus - Cestão de Contratos possa analisar junto com as informações abaixo:

1-)Vídeo do processo desde o ínicio até a ocorrência

2-)Por gentileza inserir a chave logprofiler=1 no ambiente, limpar o console e deixar rodar até cair, nos encaminhar o novo console gerado.  
   
Veja mais detalhes na documentação:LogProfiler:[LogProfiler pelo appserver](https://tdn.totvs.com/pages/viewpage.action?pageId=243638663)  
   
-Encaminhe também por gentileza o arquivo dbtrace - [OINF0001 - DBTrace - Como gerar o Log DbTrace para monitorar performance?](https://tdn.totvs.com/pages/releaseview.action?pageId=274851061)  
   
-O arquivo .csv contendo os dados dos fontes em uso (inspetor de objetos) para análise do suporte.  
Extrator de informações  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/25624035792151-RH-Linha-Protheus-TAF-eSocial-Central-de-Diagnostico-Como-enviar-o-extrato-das-Informa%C3%A7%C3%B5es>

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Documentação Gestão de Contratos do TDN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4441027145623)

[Guia de Referencia - Gestão de Contratos - Protheus 12](https://tdn.totvs.com/pages/viewpage.action?pageId=224127467)

[FAQs - Gestão de Contratos](https://tdn.totvs.com/x/O_tgDQ)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
