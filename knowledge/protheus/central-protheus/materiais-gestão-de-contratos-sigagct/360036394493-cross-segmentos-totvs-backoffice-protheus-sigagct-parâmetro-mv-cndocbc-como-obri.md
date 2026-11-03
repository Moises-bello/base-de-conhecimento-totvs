---
article_id: 360036394493
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: d073da60730fa8e3b07d5fecab96920612537e4c4b29c81a3dd29e4f3527775d
fetched_at: '2026-06-28T22:37:23.995976+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Parâmetro MV_CNDOCBC
  - Como obrigar o vinculo de um documento no Banco de Conhecimento na alteração da
  situação do contrato ?
type: support-article
updated_at: '2022-05-19T21:27:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036394493-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Par%C3%A2metro-MV-CNDOCBC-Como-obrigar-o-vinculo-de-um-documento-no-Banco-de-Conhecimento-na-altera%C3%A7%C3%A3o-da-situa%C3%A7%C3%A3o-do-contrato
---

**Dúvida**Parâmetro MV\_CNDOCBC - Como obrigar o vinculo de um documento no Banco de Conhecimento na alteração da situação do contrato ?   
  
**Ambiente**Protheus – Gestão de Contratos – A partir da versão 12.1.17  
  
**Solução**

MV\_CNDOCBC = Informa se valida documentos do SIGAGCT, na alteração da situação do contrato, considerando o banco de conhecimento.

Exemplo de Uso:

No módulo Gestão de Contratos, quando é utilizada a rotina de "Documentos x Situação" (CNTA210) é feita uma amarração de "Tipo de Documento x Tipo de Contrato x Situação"

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046897074/mceclip3.png)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047767473/mceclip0.png)

Ao alterar a situação de um Contrato para a situação informada na Amarração realizada o sistema faz uma validação abrindo a tela de Check-list de Documentos abaixo.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047768213/mceclip4.png)

Se a tela for Confirmada a rotina valida que não houve a inclusão de um Documento para essa Mudança de Situação, podendo ou não continuar a mudança da Situação do Contrato.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047768353/mceclip5.png)

A Inclusão deste Documento poderá ser realizada na Rotina Atualizações>Contratos>Documentos (CNTA170) conforme abaixo:

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046898594/mceclip8.png)

Caso o Parâmetro MV\_CNDOCBC esteja ativado o sistema irá validar a inclusão do Documento para a Situação, mas também verificará se existe um Banco de Conhecimento cadastrado para este Documento incluído na rotina de Documentos (CNTA170) reportando a mensagem abaixo:

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046898854/mceclip9.png)

Assim deverá ser incluído um Banco de Conhecimento para este exemplo de Documento "TESTE" na rotina CNTA170 conforme abaixo:

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046899174/mceclip10.png)

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046899234/mceclip11.png)

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047769673/mceclip12.png)

Após essa inclusão, na mudança da situação já constará (checkbox) a inclusão realizada no Banco de Conhecimento do Documento inserido conforme abaixo:

![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047769813/mceclip13.png)

E ao confirmar a rotina passara para a confirmação final de alteração da situação:

![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046899534/mceclip14.png)

***Saiba Mais:***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
