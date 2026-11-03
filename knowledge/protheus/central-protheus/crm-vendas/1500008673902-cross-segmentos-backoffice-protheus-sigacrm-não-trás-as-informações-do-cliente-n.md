---
article_id: 1500008673902
category: CRM - Vendas
content_hash: f88ed9a18d9739d18101cc514b8fb3446c5f8db31514e7ac23d5ac7c3483fc93
fetched_at: '2026-06-28T22:40:25.842060+00:00'
product: protheus
section_id: 1500001549102
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGACRM - Não trás as informações do
  cliente na proposta comercial
type: support-article
updated_at: '2024-03-28T21:37:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008673902-Cross-Segmentos-Backoffice-Protheus-SIGACRM-N%C3%A3o-tr%C3%A1s-as-informa%C3%A7%C3%B5es-do-cliente-na-proposta-comercial
---

**Ocorrência**Ao incluir uma Proposta comercial, o sistema não está trazendo as informações do cliente, informado na Oportunidade de venda.  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGACRM - A partir da release 12.1.17.  
  
**Causa**Esse incidente ocorre, pois a validação do campo **ADY\_DESOPO** está incorreta.

**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesse o módulo **Configurador** (**SIGACFG**).  
2. Acesse a rotina para a manutenção da Base de Dados.  
3. Selecione a opção de **Grupo de Campos** e clique em **Pesquisar**.  
4. Procure pela tabela **ADY**, e clique **Buscar** e depois em **Editar**.  
5. Procure pelo campo **ADY\_DESOPO**, e clique **Buscar** e depois em **Editar**.  
6. Acesse a aba Opções e altere o conteúdo do Inic. Padrão para **Iif(IsInCallStack("FATA300"),AD1->AD1\_DESCRI,Posicione('AD1',1,xFilial('AD1')+M->ADY\_OPORTU+M->ADY\_REVISA,'AD1\_DESCRI'))** e depois clique em **Salvar**.  
7. Clique em **Confirmar**.  
8. Clique em **Atualizar** as configurações dos **dicionários** e/ou **Base de Dados**.

Para mais informações segue a documentação da correção:

**<https://tdn.totvs.com/pages/releaseview.action?pageId=560639787>**
