---
article_id: 360041335034
category: Escrita Fiscal - Impostos - ICMS - Apuração e Livros Fiscais - Livro - Regime
  de Apuração
content_hash: a2565187d9b3534a90dfd8771ff0f706b45d053ae41510aca32c60ea9dea43cf
fetched_at: '2026-06-28T22:39:22.073108+00:00'
product: protheus
section_id: 1500001538681
source: central-protheus
title: ' CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Relatório MATRAPR
  em branco'
type: support-article
updated_at: '2022-11-17T14:26:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041335034--CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Relat%C3%B3rio-MATRAPR-em-branco
---

**Dúvida**

Relatório MATRAPR a partir das versões 12.1.25, 12.1.27 e 12.1.33 gerado em branco.

**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 12.1.25

Solução

Para correção, deverá baixar o fonte MATRAPR.PRX e também o include MATRAPR.CH.

Download do fonte MATRAPR.PRX. disponível no link abaixo:

RDMAKE compatível  da release  12.1.25 até 12.1.33

<https://suporte.totvs.com/portal/p/10098/download#detail/1083736>

**Importante:**

*Colocar o arquivo MATRAPR.CH no diretório de includes.*

Fonte customizável; Após efetuar este procedimento deverá compilar o fonte MATRAPR em seus projetos.

**Informação adicional:**

<https://tdn.totvs.com/pages/viewpage.action?pageId=636734315>
