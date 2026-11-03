---
article_id: 360007798631
category: RH - Cadastros
content_hash: 4838e7345d30a64cfd1f12cfddeaf70a43ba8046ad0f12e1d336af16d46b6e43
fetched_at: '2026-06-28T22:44:52.772947+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Como abonar um evento de forma Parcial
type: support-article
updated_at: '2026-02-24T20:42:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007798631-RH-Linha-Protheus-PON-Como-abonar-um-evento-de-forma-Parcial
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31649373265175)** Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida:**  
Como abonar um evento de forma Parcial?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico – todas as versões  
  
**Solução**  
No Protheus modulo Ponto Eletrônico permite o lançamento de mais que um abono por evento gerado, por exemplo: para um evento de Falta, o sistema permite o lançamento de um ou mais abonos para que seja possível que uma parte das horas seja abonada, outra seja lançada em Banco de Horas. Utilizando como exemplo uma Falta com dois abonos lançados, siga os passos abaixo:

**1 -** Cadastre os Motivos de Abono da seguinte maneira:

**- Opção 1:** irá abonar as horas e a falta não será exportada nem para folha e nem para Banco de Horas;

Para utilizar o motivo de abono sem o preenchimento do campo **'Cod. Evento'** necessita que os parâmetros **MV\_SUBABAP** e **MV\_ABOSEVE** abaixo estejam configurados da seguinte forma:

Acessar o modulo Configurador - **SIGACFG** em **Ambiente > Cadastros > Parâmetros:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31649373266967)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31649328766999)  
  
Após no modulo Ponto Eletrônico, realizar o cadastro do motivo de abono em **Atualizações > Cadastro do Ponto > Motivos Abono/justificativa**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31649373275159)

**-  Opção 2:** Não irá abonar a falta, porém, o restante das horas será descontado em Banco de Horas. Para isso, é necessário preencher o campo de Código de Evento, desta forma, sistema fará a substituição do evento gerado para o 015 que está configurado como FALTA BH, veja o cadastro do evento abaixo;  
  
Realizar o cadastro do motivo em **Atualizações > Cadastro do Ponto > Motivos Abono/justificativa**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31649373275927)

**2 -** Cadastrar o **evento** como exemplo abaixo;  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098695714)  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098695774)  
  
  
**3 -** Lançar os dois motivos de abono via rotina de **Integrados** ou **Apontamentos:**  
![1.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360008001831)  
  
  
**4 -** Executar o Cálculo Mensal para  funcionário, com isso, nada será levado aos Resultados e terá apenas as horas de desconto no Banco de Horas.

**Importante:** O exemplo acima é apenas uma falta com 5 horas, sendo apenas 01:00 abonada e as outras 04:00 sendo levadas ao Banco de Horas para compensação futura.  
  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Abonos MV\_ABOSEVE e MV\_SUBABAP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115009947187-RH-Linha-Protheus-PON-Abonos-MV-ABOSEVE-e-MV-SUBABAP)
