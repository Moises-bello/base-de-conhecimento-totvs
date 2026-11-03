---
content_hash: d8fc0b8394d1ac16014a3ebbe5c3d62e03e10fee44ea4d1f7d06bf170943917c
fetched_at: '2026-06-29T00:09:24.500766+00:00'
page_id: '423937932'
product: rm
source: tdn-rm
title: Exportação/Importação Fabricantes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423937932
version: 7
---

O processo de exportação consiste em recuperar o cadastro de [Fabricantes](http://tdn.totvs.com/display/LRM/Fabricantes), gerando um arquivo texto conforme o layout definido. Para utilizar este recurso o usuário deve acessar o [TOTVS Business Conector](http://tdn.totvs.com/display/LRM/Novo+Conceito+TOTVS+Business+Conector) e importar os layouts através da aba Integração | [Gerador de Saídas](http://tdn.totvs.com/pages/viewpage.action?pageId=425459363) | Layout | Importar Layout.

***Atenção!*** No caso da importação, o processo é realizado pelo módulo Integração | Conceito. E para a exportação pelo módulo Integração | Gerador de Saídas para as exportações.

Existem dois tipos de layouts que se encontram-se disponíveis na pasta Objetos Gerencias no diretório de instalação do TOTVS RM. Abaixo estão as descrições referentes a cada layout::

**Layout 1**

   
 **Layout 2**  
    
   
 Para gerar o arquivo de exportação de fabricantes, selecione o layout desejado e execute o processo Geração de Saídas.

**Importação de Fabricantes**

Através da importação é possível inserir dados na tabela de Fabricantes ou atualizar os dados existentes a partir do arquivo texto criado na exportação.   
Para isto, é necessário importar o conceito através do TOTVS Business Conector| Integração |Conceito.   
Após a inclusão, edite o conceito e selecione o arquivo texto a ser importado através da opção Fabricantes, botão Editar.   
Após salvar as configurações, selecione o conceito e execute Processar Novo Conceito.   
Os dados serão atualizados para a tabela de Fabricantes.   
***Observações***: Ao importar o arquivo.txt os valores dos campos referentes ao Fabricante são copiados de acordo com a linha. Os valores copiados são salvos para a tabela **TFAB**

Informações Adicionais

* [Boletim Técnico - Importação/Exportação](http://tdn.totvs.com/download/attachments/185734021/MOV_BT_Importa%C3%A7%C3%A3o%20de%20Movimentos_BRA_PCREQ-2461.pdf?version=1&modificationDate=1424884082000&api=v2) [Lista de Fabricantes](http://tdn.totvs.com/download/attachments/192090512/EST_BT_Importa%C3%A7%C3%A3o_Exporta%C3%A7%C3%A3o_Fabricante_BRA_PCREQ-2441_PCREQ-2462.pdf?version=1&modificationDate=1436465173000&api=v2)
