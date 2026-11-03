---
article_id: 360035184194
category: Atualização
content_hash: f2011bb9d99a1147a941508fedbefe9a350c687a65309ea874dec4143755061c
fetched_at: '2026-06-28T22:42:21.295233+00:00'
product: protheus
section_id: 360000076747
source: central-protheus
title: Framework - Linha Protheus  - Visualizador do MPUPDLOG
type: support-article
updated_at: '2024-05-08T11:17:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035184194-Framework-Linha-Protheus-Visualizador-do-MPUPDLOG
---

**Dúvida**Como visualizar arquivo de log, pós lib de dezembro de 2017?  
   
 **Ambiente**Protheus - Servidor de Aplicação - Versão 12  
  
**Solução**A partir da LIB de dezembro de 2017, o arquivo de log de *update*(mpupdlog.log) não é mais criado na pasta System, mas sim, no banco de dados (exceto para bases exclusivamente sem banco, como PDV por exemplo).  
Desta forma, para que o log possa ser visualizado, deve-se utilizar a função **UPDVIEWLOG**, chamando a mesma através do **Programa Inicial** no Smartclient:  
  
![updviewlog.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045733454)  
  
Ao abrir a função, uma janela de **Log de atualização** será aberta, listando os erros detectados no *update*:  
  
![updviewlog2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045733494)  
  
Nesta tela é possível utilizar a funcionalidade de **Imprimir browse** para gerar um relatório dos erros, ou também criar um **Filtro** para listar apenas determinados tipos de avisos:  
  
![updviewlog3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046591033)  
  
Para utilizar um filtro, clique no botão **Filtrar**, depois selecione quais filtros deseja aplicar à tabela, e então clique em **Aplicar filtros selecionados**.  
  
![updviewlog4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046591073)
