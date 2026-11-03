---
article_id: 33876157924375
category: Materiais - Compras (SIGACOM)
content_hash: dffe5430d910f9d7c63ac4b1e5a0a7c0b6d6f900e87b79d3bcbd7e582d15ce01
fetched_at: '2026-06-28T22:41:19.907695+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: "Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador Xml - COM004\
  \ - \tTipo NF-e de ajustes não será tratado pelo Importador XML"
type: support-article
updated_at: '2025-08-01T15:07:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33876157924375-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-Xml-COM004-Tipo-NF-e-de-ajustes-n%C3%A3o-ser%C3%A1-tratado-pelo-Importador-XML
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33876132065687) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**

Ao importar XML ocorre o erro **COM004 - Tipo NF-e de ajustes não será tratado pelo Importador XML**

**Ambiente**

Cross Segmentos - TOTVS Backoffice Linha Protheus – Gestão de Compras – A partir da versão 12

**Causa**

O erro COM004 indica que a NF em questão se trata de uma NF de ajustes, porém esse tipo de XML não é importado/contemplado pelo Importador XML para dentro do Monitor. Por isso a nota não irá ser importada, se trata de um conceito padrão do sistema, não importar XMLs de NFE de ajustes.

Para saber se uma NFE é de ajustes, basta verificar a tag <finNfe> que consta no XML. Se a tag <finNfe> estiver com conteúdo 3 indica se tratar de uma NFE de ajustes.

Definição da TAG <finNFe> ( **Finalidade da NF-e )**

1=NF-e Normal;

2=NF-e Complementar;

3=NF-e Ajuste;

4=Devolução de mercadoria;

**Solução**

O lançamento de NFE de ajustes deve ser realizado manualmente através da rotina do Documento de entrada MATA103.

Caso tenha dúvidas no lançamento do documento de entrada, segue documentação abaixo.

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como realizar a inclusão de um Documento de Entrada - MATA103](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407604558615-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-realizar-a-inclus%C3%A3o-de-um-Documento-de-Entrada-MATA103)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como incluir Documento de Entrada com Solicitação de Compras e Pedido de Compras?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037447974-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-incluir-Documento-de-Entrada-com-Solicita%C3%A7%C3%A3o-de-Compras-e-Pedido-de-Compras)

***Saiba Mais :***

[Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Integração Importador XML x TOTVS Transmite](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7557934491159-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Integra%C3%A7%C3%A3o-Importador-XML-x-TOTVS-Transmite)

[IX02 - Pontos de Entrada Importador XML](https://tdn.totvs.com/display/PROT/IX02+-+Pontos+de+Entrada)

[TC06 - Erros (Códigos)](https://tdn.totvs.com/pages/viewpage.action?pageId=271663193)

[TOTVS Colaboração - Guia de Referencia (SIGACOM)](https://tdn.totvs.com/pages/releaseview.action?pageId=271661626)

[Importador XML - Guia de Referencia (SIGACOM)](https://tdn.totvs.com/pages/viewpage.action?pageId=485858148)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
