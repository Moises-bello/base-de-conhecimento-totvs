---
article_id: 6172197751447
category: TAF - REINF
content_hash: f605cac7c8ea5f31c14a393a364702a49c4618291b3e990d607b2ca76eae3cdf
fetched_at: '2026-06-28T22:41:34.892366+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Wizard Configuração do
  TAF.
type: support-article
updated_at: '2024-11-11T19:44:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6172197751447-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Wizard-Configura%C3%A7%C3%A3o-do-TAF
---

**Dúvida**Como executar a Wizard de configuração do TAF?  
  
**Ambiente**

 A Wizard de Configuração tem como objetivo realizar a atualização do ambiente do TAF, será sempre executado no primeiro acesso do usuário, após a atualização do release ou pode também ser executada manualmente através do menu de opções do produto.  
  
Para realizar este procedimento acesse: **Atualizações -> Configs. TAF -> Wizard Config. TAF** e acione a opção **Avançar**.   
  
Marque a caixa de seleção e clique em **Avançar**.

![Wizard_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6171908825239)

Selecione a opção: **Tabela Compartilhada no SGDB** (Importação de arquivos ou integração via ODBC) e clique em Avançar.

Caso o ambiente seja Protheus com TAF como módulo, **não** selecione a opção **Web Service (Importação de arquivos ou integração via WS)**, pois esta opção é exclusiva para clientes que utilizam outros ERP's TOTVS e fará integração dos dados destes produtos para o TAF.  
  
Caso utilize o produto ERP Protheus e selecione está opção, será criado uma chave para JOB em seu appserver.ini que tentará fazer comunicação via Web Service e não obterá retorno, e por sua vez irá abrir um grande número de **Threads** no Monitor do TOP pelo fato não conseguir comunicação. Esta situação irá impactar no consumo de licenças.

![wizard_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6171931409559)

Na tela a seguir serão informados os dados para comunicação com o **DBAccess**. Informações devem ser coletadas do appserver.ini, os campos deverão ser preenchidos, conforme a seguir : 

![wizard_3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6171955790743)

Após o preenchimento das informações acima, serão alimentados os parâmetros:  
  
**MV\_VAUTCON** = Versão das tabelas Autocontidas do TAF.  
**MV\_TAFTALI** = Deve ser informado no nome do TOPALIAS do seu ambiente dentro do appserver.ini.  
**MV\_TAFTDB** = Deve ser informado nome do banco do seu ambiente Exemplo MSSQL ou MSSQL7 informado no seu TOPBASE dentro do appserver.ini.  
**MV\_TAFPORT** = Indica o numero da porta do serviço do TopConnect.  
**MV\_TAFINT** = Indica se o cliente utiliza a integração banco a banco do TAF.  
  
Na tela seguinte, acione o botão “Processar as configurações realizadas neste assistente”. Ao término do Processamento será apresentado um resumo das configurações realizadas. 

![wizard_4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6172020254231)
