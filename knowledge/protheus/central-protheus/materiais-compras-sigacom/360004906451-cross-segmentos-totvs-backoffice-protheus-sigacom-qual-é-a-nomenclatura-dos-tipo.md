---
article_id: 360004906451
category: Materiais - Compras (SIGACOM)
content_hash: fa908302a79e98c2a12b1573663bc909b67e1eefce4530b123ab1a190a39e6f0
fetched_at: '2026-06-28T22:41:10.396390+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Qual é a nomenclatura
  dos Tipos de Documento definidos no campo CR_TIPO ?
type: support-article
updated_at: '2026-04-09T14:59:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004906451-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-%C3%A9-a-nomenclatura-dos-Tipos-de-Documento-definidos-no-campo-CR-TIPO
---

**Dúvida**  
Qual é a nomenclatura dos tipos de documento definidos no campo CR\_TIPO ?

**Ambiente**  
Protheus – Compras – A partir da versão 12.17  
  
  
**Solução**

O campo CR\_TIPO possui os tipos de documentos para que o sistema possa comparar com a permissão do grupo de aprovador definido na aba tipo de documentos.

Segue abaixo os tipos de siglas e nomenclatura do campo CR\_TIPO dos documentos bloqueados:

Compras:

IP = Item de pedido

PC = pedido de compras

SC = Solicitação de compras

NF = Nota Fiscal (Tolerância de Recebimento)

CP = Contrato de parceria

 AE = Autorização de Entrega

Estoque:

 SA = Solicitação Armazém

Gestão de Contratos:

IM = Itens medição de Contrato

IC = Itens do contrato

IR = Itens da revisão

MD = Medição

CT = Contrato

RV = Revisão.

Segue exemplo abaixo da funcionalidade da Aba Tipos de documento utilizado no Grupo de aprovação - MATA114:

![Capturar.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360006280451)

Como exemplo acima o Grupo de Aprovadores em questão pode receber aprovação apenas dos tipos de documentos como Nota Fiscal (Tolerância de Recebimento) e Solicitação de Compras conforme "flegados" na aba “Tipo de Documentos”, ou seja, demais documentos que gerariam registros na tabela SCR com o campo diferente do CR\_TIPO = "NF"  ou CR\_TIPO = "SC", este grupo de aprovação não está habilitado para receber a alçada de aprovação.

***Obs:***

Para habilitar a aba “Tipo de documentos” no cadastro de grupo de aprovação basta ativar o parâmetro MV\_ALTPDOC = T

***Saiba Mais :***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como utilizar a Tolerância de Recebimento no módulo de Compras ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006558892-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-utilizar-a-Toler%C3%A2ncia-de-Recebimento-no-m%C3%B3dulo-de-Compras)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
