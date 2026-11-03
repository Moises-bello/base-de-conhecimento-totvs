---
article_id: 19634750285335
category: SIGAEST - CUSTOS
content_hash: 8fab3f8794516f1f08fa1c7d17566e883ca28be621a08883808e863804b7100e
fetched_at: '2026-06-28T22:39:02.416658+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST- MV_M330PR1 ativo com
  movimento RE5 e OP parcial não é custeada
type: support-article
updated_at: '2025-03-12T12:26:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19634750285335-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MV-M330PR1-ativo-com-movimento-RE5-e-OP-parcial-n%C3%A3o-%C3%A9-custeada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19634795781911) Tempo aproximado para leitura: **00:02:00** **Dúvida**Ao habilitar o parâmetro MV\_M330PR1 com apontamento parcial onde tem nota fiscal de beneficiamento não está sendo custeado ou levando o custo total no primeiro apontamento da OP, por que isso ocorre?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Implementado parâmetro MV\_M330PR1 tipo Lógico permite descarregar o custeio da produção no próximo apontamento de produção na rotina de recalculo do custo médio em conjunto com os parâmetros de sistema MV\_SEQ300 = .T., MV\_PRODPR0=1 e MV\_REQAUT=A.

De modo geral, para que os custos sejam equalizados no apontamento parcial, utiliza-se do parametro **MV\_M330PR1** habilitado.

Entretanto, para casos onde incide na existencia do movimento tipo "RE5 - Requisição informando OP na nota fiscal de entrada".

*Caso deseje que o custo seja equalizado com os tipos de movimentos RE5, é necessário que o parâmetro **MV\_M330PR1** esteja desabilitado.*

## **1º  Cenário**

Em um processo produtivo ao qual o cliente requisita proporcional ao que for apontado de produção, mesmo que seja parcial:

* Cadastrar um produto com o Tipo PA (produto acabado).
* Cadastrar um produto com o Tipo MP (Matéria prima).
* Saldo inicial da MP
* Criar uma estrutura de produto PA quantidade de Base1 para um MP quantidade base 1.
* Ordem de produção aberta com quantidade de 100 peças para produzir.
* 1º apontamento de produção para Op com 45 peças
  + Automaticamente será requisitado RE1 o Custo dessa produção será o Custo da requisição dividido pela quantidade produzida.
* 2º apontamento de produção para Op com 50 peças
  + Automaticamente será requisitado RE1 o Custo dessa produção será o saldo do custo da OP descarregado pela quantidade produzida.
* 3º apontamento de produção para Op com 5 peças realizando o mesmo processo com o saldo.

**Exemplo do processo :**

| Ord Produção | Produto | Tipo: RE/DE | Quantidade | Custo Unitario | Custo |
| --- | --- | --- | --- | --- | --- |
| 00000201001 | PRODRECAL06 | RE1 | 45,00 | 1,00 | 45,00 |
| 00000201001 | PRODRECAL05 | PR0 | 45,00 | 1,00 | 45,00 |
| 00000201001 | PRODRECAL06 | RE1 | 50,00 | 1,00 | 50,00 |
| 00000201001 | PRODRECAL05 | PR0 | 50,00 | 1,00 | 50,00 |
| 00000201001 | PRODRECAL06 | RE1 | 5,00 | 1,00 | 5,00 |
| 00000201001 | PRODRECAL06 | PR0 | 5,00 | 1,00 | 5,00 |

Como será apresentado no relatório MATR860 Relação por Ordem de produção:

![](https://tdn.totvs.com/download/attachments/401342835/image2018-9-4_17-55-53.png?version=1&modificationDate=1536094554000&api=v2)

 

## **2 º Cenário**

Em um processo produtivo ao qual o cliente realiza uma requisição manual do insumo necessário, o sistema vai se comportar descarregando todo o custo no primeiro apontamento de produção:

* Cadastrar um produto com o Tipo PA (produto acabado).
* Cadastrar um produto com o Tipo MP (Matéria prima).
* Criar uma estrutura de produto PA quantidade de Base1 para um MP quantidade base 1.
* Ordem de produção aberta com quantidade de 100 peças para produzir.
* Entrar com documento de entrada vinculando a ordem de produção na quantidade de 100 peças ao custo de 1,00.
* 4 apontamentos de produção com 25 peças cada apontamento.
* Todo o custo dessa produção será direcionado ao primeiro apontamento.

**Exemplo do processo:**

| Ord Produção | Produto | Tipo: RE/DE | Quantidade | Custo Unitario | Custo |
| --- | --- | --- | --- | --- | --- |
| 00000101001 | PRODRECAL04 | RE5 | 100,00 | 1,00 | 100,00 |
| 00000101001 | PRODRECAL05 | PR0 | 25,00 | 4,00 | 100,00 |
| 00000101001 | PRODRECAL06 | PR0 | 25,00 | 0,00 | 0,00 |
| 00000101001 | PRODRECAL05 | PR0 | 25,00 | 0,00 | 0,00 |
| 00000101001 | PRODRECAL06 | PR0 | 25,00 | 0,00 | 0,00 |

Como será apresentado no relatório MATR860 Relação por Ordem de produção:

![](https://tdn.totvs.com/download/attachments/401342835/image2018-9-4_17-43-44.png?version=1&modificationDate=1536093825000&api=v2)

**Saiba mais:**

*[MP - SIGAEST - Como fazer uma análise de Custos no Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020860771)*

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR860 - Interpretando Custos em Ordem de Produção (OP)*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012330641-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR860-Interpretando-Custos-em-Ordem-de-Produ%C3%A7%C3%A3o-OP-)

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
