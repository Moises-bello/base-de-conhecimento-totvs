---
content_hash: 6d442901ccefee70e6163d165e8ed3c66211334f089ae3901bee19d8cd5e033e
fetched_at: '2026-06-29T00:09:00.947017+00:00'
page_id: '370610931'
product: rm
source: tdn-rm
title: FINANCEIRO01-7431 Serviço Cálculo do Valor Líquido
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=370610931
version: 3
---

# Serviço Cálculo do Valor Líquido

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Serviço Cálculo do Valor Líquido |
| **Situação/Requisito:** | Necessidade de um serviço de cálculo do valor líquido seja exposto para ser utilizado pelas aplicações desenvolvidas pelo cliente. A necessidade do cliente é de que o serviço retorne o valor líquido para um lançamento em uma data qualquer, ou seja, que o serviço faça o cálculo de forma idêntica ao cálculo feito na visão ou edição de um lançamento. Para isso é necessário que o serviço receba a chave do lançamento (codcoligada, idlan) bem como uma data base para o cálculo do mesmo. |
| **Solução/Implementação:** | Serviço Cálculo do Valor Líquido disponibilizado no **wsPageIndex - RM\_IwsFin - ValorLiquido**  Formato de XML utilizado para realizar o serviço de buscar o **Cálculo do Valor Líquido**em lançamentos financeiros:    ***-> Cabeçalho do XML:***  <TOTVSMessage>  <MessageInformation>  <UUID>ValorLiquido</UUID>  <Type>BusinessMessage</Type>  <Transaction>ValorLiquido</Transaction>  <StandardVersion>1160</StandardVersion>  <SourceApplication>TOTVS SA</SourceApplication>  <CompanyId>21.867.387/0001-58</CompanyId>  <Product>RM</Product>  <GeneratedOn>2010-09-06T16:25:23Z</GeneratedOn>  <DeliveryType>Sync</DeliveryType>  <QUEUETYPE>1</QUEUETYPE>  </MessageInformation>  ***-> Configurações do XML:***  <BusinessMessage>  <BusinessEvent>  <Entity>ValorLiquido</Entity>  <Event>upsert</Event>  <Identification>  <key name="key1">IDFLAN</key>  <key name="key2">CODCOLIGADA</key>  </Identification>  </BusinessEvent>  ***-> Passando informações via XML:***  <BusinessContent>  <CompanyId>1</CompanyId>  <Code>6906</Code>  <CurrentDate>2011-04-07</CurrentDate>  <User>mestre</User>  </BusinessContent>  </BusinessMessage>  </TOTVSMessage>    **Referente a este bloco de tag´s, deve-se alterar os mesmos conforme suas descrições:**   * **CompanyId:**Código da Coligada. * **User:**Código do Usuário * **Code:**Numero do Lançamento Financeiro (Tabela: Flan – Campo: IDLan). * **CurrentDate:**Data Referência.   **Exemplo de como configurar Xml para Baixa:**  A busca do valor do Cálculo do Valor Líquido de um lançamento financeiro é feita quando é informado o Numero do lançamento referente na Tag <Code> e o tipo do evento da mensagem padrão enviada por parâmetro ao WebMethod. Exemplo:  ......  <BusinessEvent>  **<Event>upsert</Event>**  </BusinessEvent>  <BusinessContent>  ......  **<Code>1021</Code>**  ....  </BusinessContent>  ... |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | <http://fwrm-wiki:9999/WikiHelp/FIN/Fin.CrudWSLancamento.aspx> |
