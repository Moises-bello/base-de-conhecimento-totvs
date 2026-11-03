---
article_id: 37617078775831
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 3c9813b8d09dd5f14944e6e37ed8042e59735fcc17f5d3fdc94e8208286bc4a4
fetched_at: '2026-06-28T22:37:20.307063+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - "Erro de Gatilho CNE_VLTOT"
  ao Salvar a Medição no módulo Gestão de contratos. O que fazer?
type: support-article
updated_at: '2026-01-12T18:55:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37617078775831-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Erro-de-Gatilho-CNE-VLTOT-ao-Salvar-a-Medi%C3%A7%C3%A3o-no-m%C3%B3dulo-Gest%C3%A3o-de-contratos-O-que-fazer
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37617078753559) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
  
"Erro de Gatilho CNE\_VLTOT" ao Salvar a Medição no módulo Gestão de contratos. O que fazer?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37617070191767)

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de contratos - Todas as versões

**Solução**

Segue possibilidades do erro abaixo:

1. Verifique no configurador do sistema se os gatilhos estão conforme abaixo :

**CNE\_VLTOT Seq 001**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37617070192407)

**CNE\_VLTOT Seq 002**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37617070193047)

**CNE\_VLTOT Seq 003**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37617078758423)

**CNE\_VLTOT Seq 004**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/37617070193943)**

**CNE\_VLTOT Seq 005**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37617078758679)

**CNE\_VLTOT Seq 006**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37617078759703)

Demonstração resumida abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37617078760983)

Gatilhos **X7\_CDOMIN** = **CNE\_VLTOT**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37617078761239)

Caso possua alguma divergência de seu ambiente com as informações passadas acima, mediante a backup e em ambiente de teste realize um novo teste conforme padrão.

2. Caso o ambiente possua customizações relacionadas, peço por gentileza, que realize os testes desativando as customizações do ambiente através dos [3 métodos indicados nesta documentação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021114292), impreterivelmente.

1 - Através da chave IXBLOG no arquivo APPSERVER.ini

2 - Através do Configurador CFG - Catálogo de Personalizações

3 - Desabilitar customizações chamadas no dicionário de dados

Caso o problema persista , por gentileza abrir um ticket para equipe de suporte em um de nosso canais de atendimento.

***Saiba Mais:***

[Guia de Referencia - Gestão de Contratos - Protheus 12](https://tdn.totvs.com/pages/viewpage.action?pageId=224127467)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
