---
article_id: 360047487694
category: Integrações Nativas
content_hash: b635f9326a5a037d98fb8c02d8fce1ed24e3ad9f7782c52e1d5a46bd396f434b
fetched_at: '2026-06-28T22:42:35.548785+00:00'
product: protheus
section_id: 360012117933
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Reporte de produtos em uma Ordem de Serviço
  finalizada
type: support-article
updated_at: '2024-08-28T18:40:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047487694-Manufatura-Linha-Protheus-MNT-Reporte-de-produtos-em-uma-Ordem-de-Servi%C3%A7o-finalizada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25974822727959) Tempo aproximado para leitura:**00:03:20 min**  
**Dúvida**Como realizar o reporte de produtos em uma ordem de serviço finalizada?  
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integrações Nativas - A partir da versão 12  
  
**Solução**O processo de reporte de insumos do tipo produto para ordens de serviço já finalizadas, pode ser realizado somente por aplicação direta por meio de rotinas do módulos **Estoque/Custo - SIGAEST**e**Compras - SIGACOM**. Sendo estas apresentadas a seguir:

* **Baixar Pré-Requisição - MATA185**

Ao acessar o módulo **Estoque/Custos - SIGAEST**no menu do módulo ir em: **Atualizações > Movimentações > Internas > Armazém > Baixar Pré-Requisição**. Realizar o processo de baixa sendo que ao informar os dados para este, os campos **Ordem de Serviço -** **CP\_NUMOS** e **Ordem de Produção -** **CP\_OP**já estarão preenchidos de forma automática conforme as informações da solicitação de armazém, assim não deveram ser alterados ou apagados para o correto reporte de insumos.  
  
Como não é possível incluir uma solicitação de armazém para um ordem de serviço finalizada, este processo somente é valido para a baixa de requisições já inclusas, antes da finalização da ordem que as originou.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069580714)

* **Documento de Entrada - MATA103**

Para esta rotina, acessar o módulo **Compras - SIGACOM**no menu do módulo ir em: **Atualizações > Movimentos > Documento Entrada**. Ao informar os dados do documento de entrada, não preencher o campo **Ordem de Produção - D1\_OP**pois este será gatilhado a partir do campo **Ordem de Serviço - D1\_ORDEM**.  
  
Ao pesquisar a ordem de serviço, marcar a opção **Incluir as ordens finalizadas** para que estas sejam listadas na consulta. Ao optar por uma ordem, automaticamente será preenchido o campo **Ordem de Produção - D1\_OP**.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069581034)

* **Movimentação Interna** **- MATA240**

Acessar o módulo **Estoque/Custos - SIGAEST** no menu do módulo ir em: **Atualizações > Movimentações > Internas > Movimentação Simples**. Informar os campos necessários para realização da movimentação, com a ressalva do campo **Ordem de Produção - D3\_OP** o qual não deverá ser informado, neste caso o preenchimento deve ser feito no campo **Ordem de Serviço - D3\_ORDEM.**   
  
Ao pesquisar a ordem de serviço, marcar a opção **Incluir as ordens finalizadas** para que estas sejam listadas na consulta. Ao optar por uma ordem, automaticamente será preenchido o campo **Ordem de Produção - D1\_OP**.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069581134)

* **Movimentação Múltipla - MATA241**

Acessar o módulo **Estoque/Custos - SIGAEST** no menu do módulo ir em: **Atualizações > Movimentações > Internas > Movimentação Múltipla**. Informar os campos necessários para realização da movimentação, com a ressalva do campo **Ordem de Produção - D3\_OP** o qual não deverá ser informado, neste caso o preenchimento deve ser feito no campo **Ordem de Serviço - D3\_ORDEM.**   
  
Ao pesquisar a ordem de serviço, marcar a opção **Incluir as ordens finalizadas** para que estas sejam listadas na consulta. Ao optar por uma ordem, automaticamente será preenchido o campo **Ordem de Produção - D1\_OP**.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070693353)

**Saiba mais**  
Para habilitar a consulta específica de **O.S. - Ordem de Serviço** verifique o artigo [Manufatura - Linha Protheus - MNT - Apresentação das Ordens de Serviço finalizadas na Consulta Padrão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048146893)
