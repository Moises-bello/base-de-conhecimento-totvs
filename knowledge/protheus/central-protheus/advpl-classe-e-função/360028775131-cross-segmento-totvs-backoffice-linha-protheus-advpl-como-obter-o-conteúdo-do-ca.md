---
article_id: 360028775131
category: ADVPL - Classe e Função
content_hash: 76f735e154b6eb26e10bd71e131acc7f251157f4d7d0dc192612c7e6b7363bca
fetched_at: '2026-06-28T22:40:15.541111+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Como obter o conteúdo
  do campo D7_OBS
type: support-article
updated_at: '2022-01-05T14:53:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028775131-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-obter-o-conte%C3%BAdo-do-campo-D7-OBS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como obter o conteúdo do campo padrão do sistema **D7\_OBS?**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Existe dois tipos de contextos de campos no protheus, o primeiro é o **Real** que significa que o campo será gravado fisicamente, ou seja ele existe na tabela de banco de dados e existe o contexto  **Virtual**, ele é penas criado nas telas do sistema, não sendo gravado em lugar nenhum.

O campo **D7\_OBS** é de contexto Virtual ou seja não é gravado nenhuma informação em banco de dados. Por esse motivo não é possível buscar o valor do campo em tabelas, pois a informação não existe.

Quando preenchemos o campo **D7\_OBS**, a rotina grava os dados informados nesse campo em um arquivo **.txt** no diretório definido no parâmetro **MV\_DIRCQ**, que por padrão vem com os seguinte caminho **"C:\PROTHEUS\protheus\_data\relato\controle**". Quando visualizamos as informações do campo a rotina não faz busca em banco de dados, a rotina lê o arquivo .txt que contem as informações gravadas e apresenta dentro do campo **D7\_OBS.**

![Screenshot_12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029601771/Screenshot_12.png) 

**MV\_DIRCQ - Diretório controle de qualidade**Diretório destino onde são armazenados os certificados dos produtos aprovados no CQ - (Controle de Qualidade), pelo processo Skip-Lote.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029304132/mceclip1.png)

Para obter a informação desse campo, só será possível lendo o arquivo .txt, através de funções que tem essa finalidade, tais como **MemoRead**() e  **FRead**().  
  
**Saiba mais**[Mata175 - Instruções sobre Controle de Qualidade](http://tdn.totvs.com/pages/releaseview.action?pageId=6085107)  
[MV\_DIRCQ - Diretório controle de qualidade](http://tdn.totvs.com/pages/releaseview.action?pageId=6085209)  
[Manipulação de arquivos, discos e IO](http://tdn.totvs.com/pages/viewpage.action?pageId=6063692)  
[MemoRead](http://tdn.totvs.com/display/tec/MemoRead)**[FRead](http://tdn.totvs.com/display/tec/FRead)**
