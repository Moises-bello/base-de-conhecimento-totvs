---
article_id: 11669998568087
category: ACOMPANHA CUSTOS - JORNADA DE FECHAMENTO (NOVO)
content_hash: 0e71715d9b76cc9d0264dcd003b01f316cf71264a9843d3e88d0d608e5e1c34e
fetched_at: '2026-06-28T22:38:48.219835+00:00'
product: protheus
section_id: 5367899706647
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA038 - Lentidão
  no carregamento da jornada de fechamento
type: support-article
updated_at: '2025-03-12T12:23:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11669998568087-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA038-Lentid%C3%A3o-no-carregamento-da-jornada-de-fechamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20028364759447) Tempo aproximado para leitura: **3min 15s****Dúvida**Durante a abertura da rotina Acompanha Custos, apresenta lentidão na tela inicial de carregamento, onde o GIF do boneco não processa mais nenhuma informação em tela. O que fazer?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - 12.1.33 e posterior.  
  
**Solução**Para dar inicio a validação da questão apresentada, deve-se primeiro validar se o ambiente em questão se encontra com as ultimas atualizações disponibilizadas no portal do cliente, em relação aos módulos SIGAEST, SIGACTB, SIGAFAT, SIGACOM, e artefatos:

- [Acumulado SIGAEST conforme sua versão](https://tdn.totvs.com/x/2hgdHw)  
- [LIB Harpia](https://suporte.totvs.com/portal/p/10098/download?e=1050526)  
 - [Appserver](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/)   
- [Smartclient](https://suporte.totvs.com/portal/p/10098/download?e=946864#000006/368/TFSC/)

- [DBAccess](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFDBA/)

Não é comum que a tela inicial tenha um tempo alto elevado de processamento, para exibir os fechamentos e reaberturas efetuados, por isso a validação inicial das atualizações é o primeiro passo a ser efetuado.

![carregamento_acompanha_custos.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11670005010967)

Efetue a validação se o ambiente se encontra atualizado, mas mesmo assim o carregamento é lento:

-Aguardar até que seja carregado, ou esperar o tempo médio de carregamento que era feito antes.

-Reiniciar os serviços do ambiente, ou maquina em questão, pois é um problema relacionado a infraestrutura.

Após a reinicialização, o carregamento foi concluído, mas esta lento na sua opinião? Então devemos efetuar uma analise do Logprofiler + Dbtrace. Abaixo vídeo de como efetuar a coleta desses arquivos, para envio e analise do suporte. (sugestível ser efetuado o processo pelo seu departamento de T.I)

Além do seguinte arquivo importante para analise do Suporte:

**Habilitar TraceStack e Analisar Logs:**   
É necessário habilitar a chave TraceStack no arquivo appserver.ini em um ambiente isolado, conforme a documentação em [TraceStack](https://tdn.totvs.com/display/tec/TraceStack).

Após habilitar a chave TraceStack, faça um backup do arquivo console.log e reinicie o sistema.

Depois de reiniciar o sistema, acesse a rotina "Acompanha Custos" e aguarde por cerca de 5 minutos. 

Durante esse período, verifique se algum erro é gerado no arquivo console.log e pode enviar o erro em txt e a fazer a abertura do ticket ao Suporte.

**Saiba Mais**

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Validação para inicia a rotina Acompanha Custos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5240908654999)*
