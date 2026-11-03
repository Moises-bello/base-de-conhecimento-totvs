---
content_hash: 77a8e55709fadfe499e45bafcf78ae0564b34025e804e269bbf74d3291818dc2
fetched_at: '2026-06-29T00:09:25.421004+00:00'
page_id: '423938143'
product: rm
source: tdn-rm
title: Importação/Exportação de Movimentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938143
version: 7
---

Com a intenção de facilitar os processos de integração do ERP com bases e sistemas legados, ou mesmo a extração de dados do ERP, a TOTVS disponibilizou os layouts de importação e exportação de movimentos como objetos gerenciais padrões.  
    
 **Exportação**  
    
 O processo de Exportação de [Movimentos](http://tdn.totvs.com/pages/viewpage.action?pageId=423938113) permite copiar as informações de um movimento gerando um arquivo texto de acordo com um layout pré-definido. Deve-se primeiro importar o layout de exportação através do Módulo de Integração | [Gerador de Saídas](http://tdn.totvs.com/pages/viewpage.action?pageId=425459363) | Layouts | Processos | Importar Layout. Para Realizar a exportação dos movimentos utiliza-se a ferramenta Gerador de Saídas através do Módulo Integração |  Processos | Geração de Saídas.  
    
 **Importação**  
    
 Através da importação é possível inserir um movimento ou atualizar um movimento existente, a partir do arquivo texto criado na exportação. Para utilizar o processo de importação de Movimentos é necessário importar o layout através da aba [Conceito](http://tdn.totvs.com/display/LRM/Conceito+-+Como+parametrizar) no TOTVS Business Conector | Importar Conceito. Após a importação selecione o conceito na visão e execute o processo Processar Novo Conceito selecionando o arquivo desejado no mesmo formato do layout de exportação. Para a importação de Movimento existem as opções: Atualizar Movimentos Cadastrados e Cliente/Fornecedor identificado por CGCFO. Após a conclusão do processo os movimentos informados no arquivo de importação estarão atualizados no sistema.

***Atenção!*** No caso da importação, o processo é realizado pelo módulo Integração | Conceito. E para a exportação pelo módulo Integração | Gerador de Saídas para as exportações.

Informações Adicionais

* [Boletim Técnico - Importação/Exportação de Movimentos](http://tdn.totvs.com/download/attachments/185734021/MOV_BT_Importa%C3%A7%C3%A3o%20de%20Movimentos_BRA_PCREQ-2461.pdf?version=1&modificationDate=1424884082000&api=v2)
