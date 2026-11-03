---
article_id: 35985241178391
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 2bcd5b76ffb0b854f22aa2062911d569236f244539a995f4d760d84bb062351d
fetched_at: '2026-06-28T22:39:30.635919+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 - Como calcular
  o FUST/FUNTTEL pelo Configurador de Tributos?
type: support-article
updated_at: '2025-11-03T17:34:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35985241178391-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-o-FUST-FUNTTEL-pelo-Configurador-de-Tributos
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

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985234098711)

**Perfil de Participante:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985234100759)

**Perfil de Operação:**

Nesse perfil, é importante validar que ambos os CFOPs estão vinculados (entrada e saída, se for utilizar para os dois casos), bem como se não há Código de Serviço na respectiva aba. Caso precise informar o Código de Serviço, o mesmo tem que estar vinculado também ao Produto.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985241156759)

**Perfil de Produto:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985234102551)

**Regra de cálculo:**

* FUST - ID Tributo 000071

**Regra de Base de Cálculo:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985241158167)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985234104087)

**Regra de Alíquota:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985241159447)![]()

**Regra de Escrituração:**

Nessa Regra, você irá informar a incidência pertinente de acordo com a sua operação. No exemplo foi utilizada a opção "Tributado" e sem CST, mas caso precise informar o CST preencha o campo devido.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985241160599)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985241161239)

**Regra de Cálculo:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985241161751)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985234106263)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985234106647)

* FUNTTEL - ID Tributo 000072:

**Regra de Base de Cálculo:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985234106903)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985241163031)

**Regra de Alíquota:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985234107799)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985241164055)

**Regra de Escrituração:**

Nessa Regra, você irá informar a incidência pertinente de acordo com a sua operação. No exemplo foi utilizada a opção "Tributado" e sem CST, mas caso precise informar o CST preencha o campo devido.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985241165847)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985234108951)

**Regra de Cálculo:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985234109847)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985234110103)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985241166871)

**EXEMPLO DE UTILIZAÇÃO - Pedido de Venda (MATA410):**

Inclusão de Nota no valor de R$ 1.000,00 - TES com CFOP 5101

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985234110871)

**EXEMPLO DE UTILIZAÇÃO - Documento de Entrada (MATA103):**

Inclusão de Nota no valor de R$ 1.000,00 - TES com CFOP 1101

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985241168407)

Após adequação do cálculo e devida escrituração, os detalhes serão gravados na F2D e CJ3 para que sejam alimentadas as informações no XML/DANFECOM.

Para geração do XML e DANFECOM, deverá ser validada a documentação abaixo do Protheus SPED/TSS:

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFCOM - FUST e FUNTTEL no XML/DANFECOM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35971113059095-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFCOM-FUST-e-FUNTTEL-no-XML-DANFECOM)

Documentação centralizada do Configurador de Tributos:

[CFGTRIB - Configurador de Tributos](https://tdn.totvs.com/display/public/PROT/CFGTRIB+-+Configurador+de+Tributos)
