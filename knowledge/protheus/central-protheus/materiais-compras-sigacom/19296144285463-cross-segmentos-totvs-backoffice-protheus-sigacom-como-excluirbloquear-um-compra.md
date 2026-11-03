---
article_id: 19296144285463
category: Materiais - Compras (SIGACOM)
content_hash: bf717410625c663fdbd40e8097fd1287a0e5bc13f1694b4a83774f48c3d19533
fetched_at: '2026-06-28T22:41:15.849363+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como Excluir/Bloquear
  um comprador (COMA087) '
type: support-article
updated_at: '2023-11-24T15:14:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19296144285463-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-Excluir-Bloquear-um-comprador-COMA087
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19296169557015) Tempo aproximado para leitura: **03:00 min****Ocorrência**  
No módulo Compras, é possível excluir um comprador ?  
**Ambiente**Protheus – Compras – A partir da versão 12.1.27  
  
**Solução**

No produto padrão não é possível excluir um comprador, porque o cadastro dele pode estar relacionado em outros registros. Exemplo: No caso da solicitação de compras possui vinculo com comprador, neste caso se excluir um registro que tem relação com outro pode gerar problemas de integridade entre eles. Existe um campo de bloqueio que pode ser inserido na tabela SY1 (cadastro de compradores). Esse campo deixará o registro INATIVO para uso.

Para realizar a inclusão do campo de bloqueio na tabela SY1, basta seguir o passo a passo dos prints a baixo:

1-) No modulo configurador( SIGACFG) , acesse a tabela SY1

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19296159541655)

2-) Clique em campos reservados, selecione e campo bloqueio automático e clica em finalizar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19296144264727)

3-) O sistema incluirá o campo Y1\_MSBLQ > Salve o dicionario clicando no icone "disquete"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19296189749655)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19297527831831)

4-) Acesse a rotina cadastro de compradores > Clique em alterar e mude o campo Bloqueado para "SIM"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19299016173719)

5-) O registo bloqueado será apresentado com a cor cinza, indicando seu bloqueio.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19296154885911)
