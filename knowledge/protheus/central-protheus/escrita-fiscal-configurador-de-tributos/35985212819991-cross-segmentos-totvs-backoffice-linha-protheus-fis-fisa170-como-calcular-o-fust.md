---
article_id: 35985212819991
category: Escrita Fiscal - Configurador de Tributos
content_hash: dba92539d9add55b1b9f90430d99d1fe0be7aeb998322a6e31e2c682b553d66a
fetched_at: '2026-06-28T22:39:17.750220+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 - Como calcular
  o FUST/FUNTTEL pelo Configurador de Tributos?
type: support-article
updated_at: '2025-11-03T17:34:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35985212819991-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-o-FUST-FUNTTEL-pelo-Configurador-de-Tributos
---

**Dúvida**  
Como calcular o FUST/FUNTTEL pelo Configurador de Tributos (FISA170)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Abaixo será apresentado um exemplo de parametrização/cálculo dos tributos FUST e FUNTTEL utilizando o Configurador de Tributos.

Para o exemplo em questão iremos efetuar uma Venda e uma Compra com os respectivos CFOPs 5101 e 1101, sendo que na implantação deverá adequar esses parâmetros a sua operação.

1. Venda SP x SP (MV\_ESTADO = SP  e Cliente = SP).
2. Compra SP x SP (MV\_ESTADO = SP e Forncedor = SP).

Em ambos os casos serão utilizados os mesmos Perfis citados abaixo:

**Perfil de Origem/Destino:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985219947799)

**Perfil de Participante:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985212799511)

**Perfil de Operação:**

Nesse perfil, é importante validar que ambos os CFOPs estão vinculados (entrada e saída, se for utilizar para os dois casos), bem como se não há Código de Serviço na respectiva aba. Caso precise informar o Código de Serviço, o mesmo tem que estar vinculado também ao Produto.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985212799767)

**Perfil de Produto:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985212800791)

**Regra de cálculo:**

* FUST - ID Tributo 000071

**Regra de Base de Cálculo:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985219949207)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985212802327)

**Regra de Alíquota:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985212803351)![]()

**Regra de Escrituração:**

Nessa Regra, você irá informar a incidência pertinente de acordo com a sua operação. No exemplo foi utilizada a opção "Tributado" e sem CST, mas caso precise informar o CST preencha o campo devido.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985219953559)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985219954327)

**Regra de Cálculo:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985212805655)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985219956119)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985219957271)

* FUNTTEL - ID Tributo 000072:

**Regra de Base de Cálculo:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985219958423)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985219959063)

**Regra de Alíquota:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985219960983)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985212808855)

**Regra de Escrituração:**

Nessa Regra, você irá informar a incidência pertinente de acordo com a sua operação. No exemplo foi utilizada a opção "Tributado" e sem CST, mas caso precise informar o CST preencha o campo devido.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985219961239)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985212809623)

**Regra de Cálculo:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985212810263)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985212810775)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985219963415)

**EXEMPLO DE UTILIZAÇÃO - Pedido de Venda (MATA410):**

Inclusão de Nota no valor de R$ 1.000,00 - TES com CFOP 5101

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985212811031)

**EXEMPLO DE UTILIZAÇÃO - Documento de Entrada (MATA103):**

Inclusão de Nota no valor de R$ 1.000,00 - TES com CFOP 1101

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985212811415)

Após adequação do cálculo e devida escrituração, os detalhes serão gravados na F2D e CJ3 para que sejam alimentadas as informações no XML/DANFECOM.

Para geração do XML e DANFECOM, deverá ser validada a documentação abaixo do Protheus SPED/TSS:

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFCOM - FUST e FUNTTEL no XML/DANFECOM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35971113059095-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFCOM-FUST-e-FUNTTEL-no-XML-DANFECOM)

Documentação centralizada do Configurador de Tributos:

[CFGTRIB - Configurador de Tributos](https://tdn.totvs.com/display/public/PROT/CFGTRIB+-+Configurador+de+Tributos)
