---
article_id: 360034679934
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: d36187a29fd923d169eef46bcb605410d9b0f550a43ba2af9233199af803428a
fetched_at: '2026-06-28T22:42:07.728066+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos  - GIA-SP - 3º
  Passo - Wizard de Configuração
type: support-article
updated_at: '2024-06-04T19:05:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034679934-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-GIA-SP-3%C2%BA-Passo-Wizard-de-Configura%C3%A7%C3%A3o
---

**Ocorrência**

Necessário atualizar o ambiente TAF para utilização da GIA-SP.

**Ambiente**Protheus - Livros Fiscais – A partir da versão 12.1.17]  
 **Causa**Necessidade das configurações para a geração do arquivo da **Nova GIA**através do **TAF.**  
 **Solução**A Wizard de Configuração tem como objetivo realizar a atualização do ambiente do TAF, será sempre executado no primeiro acesso do usuário, após a atualização do release ou pode também ser executada manualmente através do menu de opções do produto.  
  
Para realizar este procedimento acesse: **Atualizações -> Configs. TAF -> Wizard Config. TAF** e acione a opção **Avançar**.   
  
Marque a caixa de seleção e clique em **Avançar**.

![](https://tdn.totvs.com/download/attachments/379308197/image2018-7-4_13-13-9.png?version=1&modificationDate=1530720789000&api=v2)

Selecione a opção: Layout TOTVS ou Tabela Compartilhada no SGDB (Importação de arquivos ou integração via ODBC) e clique em Avançar.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045042674)

![](https://tdn.totvs.com/download/attachments/379308197/image2018-7-4_13-13-41.png?version=1&modificationDate=1530720822000&api=v2)

Na tela a seguir serão informados os dados para comunicação com o DBAccess. Os campos deverão ser preenchidos, conforme a seguir: 

![](https://tdn.totvs.com/download/attachments/379308197/image2018-7-4_13-13-52.png?version=1&modificationDate=1530720833000&api=v2)

Após o preenchimento das informações acima, serão alimentados os parâmetros   
  
**MV\_VAUTCON** = Versão das tabelas Autocontidas do TAF.  
**MV\_TAFTALI** = Deve ser informado no nome do TOPALIAS do seu ambiente dentro do appserver.ini.  
**MV\_TAFTDB** = Deve ser informado nome do banco do seu ambiente Exemplo MSSQL ou MSSQL7 informado no seu TOPBASE dentro do appserver.ini.  
**MV\_TAFPORT** = Indica o numero da porta do serviço do TopConnect.  
**MV\_TAFINT** = Indica se o cliente utiliza a integração banco a banco do TAF.  
  
Na tela seguinte, acione o botão “Processar as configurações realizadas neste assistente”. Ao término do Processamento será apresentado um resumo das configurações realizadas. 

![](https://tdn.totvs.com/download/attachments/379308197/image2018-7-4_13-14-57.png?version=1&modificationDate=1530720900000&api=v2)
