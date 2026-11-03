---
content_hash: 4831b7d1513ace9c164a5ddafda3b1945363c3aecad5c6bcc60991a2509e0c03
fetched_at: '2026-06-29T00:09:37.256023+00:00'
page_id: '425459581'
product: rm
source: tdn-rm
title: Web Service Lançamento Financeiro (wsFin)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459581
version: 3
---

**Web Service Lançamento Financeiro (wsFin)**

---

**1. Inclusão e Exclusão**  
    
 Formato de XML utilizado para Incluir/Excluir lançamentos financeiros:  
 ***-> Cabeçalho do Xml:***  
 <TOTVSMessage>  
 <MessageInformation>  
 <UUID>Financial</UUID>  
 <Type>BusinessMessage</Type>  
 <Transaction>financial</Transaction>  
 <StandardVersion>1160</StandardVersion>  
 <SourceApplication>TOTVS SA</SourceApplication>  
 <CompanyId>21.867.387/0001-58</CompanyId>  
 <Product>RM</Product>  
 <GeneratedOn>2010-09-06T16:25:23Z</GeneratedOn>  
 <DeliveryType>Sync</DeliveryType>  
 <QUEUETYPE>1</QUEUETYPE>  
 </MessageInformation>  
 ***-> Configurações do Xml:***  
 <BusinessMessage>  
 <BusinessEvent>  
 <Entity>Financial</Entity>  
 **<Event>upsert</Event>**  
 <Identification>  
 <key name="key1">IDFLAN</key>  
 <key name="key2">CODCOLIGADA</key>  
 </Identification>  
 </BusinessEvent>  
 ***Nota:*** *A tag "<Event>" é responsável por indicar se a ação será de Inclusão (O comando a ser utilizado deve ser "upsert") ou de exclusão (Comando a ser utilizado deve ser "delete").*  
 ***-> Passando informações via Xml:***  
 <BusinessContent>  
 <CompanyId>1</CompanyId>   
 **<Code>0</Code>**  
 <CostCenterCode>01.1</CostCenterCode>  
 <CustomerCode>C00025</CustomerCode>  
 <BranchCode>1</BranchCode>  
 <DocumentTypeCode>01</DocumentTypeCode>  
 <CurrencyCode>R$</CurrencyCode>  
 <IssueDate>2011-04-01</IssueDate>  
 <ExpirationDate>2011-08-01</ExpirationDate>  
 <ExpectedDate>2011-04-05</ExpectedDate>  
 <CurrentDate>2011-04-01</CurrentDate>  
    
 ***Ação para INCLUIR (<Event>upsert</Event>):***  
 *Referente à tag "Code", o mesmo deve estar preenchido com valor igual a "0" (Zero).*  
    
 ***Ação para EXCLUIR (<Event>delete</Event>):***  
 *Referente à tag "Code", o mesmo deve estar preenchido com valor igual ao Numero do Lançamento Financeiro (Campo IdLan).*  
    
 <BankInformation>  
 <Code>001</Code>  
 <CashAccountCode>0001</CashAccountCode>  
 </BankInformation>  
 <Type>1</Type>  
 <Value>10</Value>  
 <ValueOfDiscount>0</ValueOfDiscount>  
 <ValueOfInterest>0</ValueOfInterest>  
 <ValueOfFine>0</ValueOfFine>  
 <ValueOfService>0</ValueOfService>  
 <ListOfOptionalValues>  
 <OptionalValues>  
 <Code>01</Code>  
 <Description>Correção Monetária</Description>  
 <Value>4.221</Value>  
 </OptionalValues>  
 <OptionalValues>  
 <Code>02</Code>  
 <Description>Correção2</Description>  
 <Value>4.221</Value>  
 </OptionalValues>  
 </ListOfOptionalValues>  
 </BusinessContent>  
 </BusinessMessage>  
 </TOTVSMessage>  
    
    
 **Referente a este bloco de tag´s, deve-se alterar os mesmos conforme suas descrições:**

* **CompanyId** = Código da Coligada.
* **Code** = Numero do Lançamento Financeiro (Tabela: Flan – Campo: IDLan, deixar zero quando a ação for de inclusão, para excluir esta tag deve ser preenchida com o Numero do Lançamento Financeiro).
* **CostCenterCode:** Centro de Custo.
* **CustomerCode:** Código do Cliente.
* **BranchCode:** Código da Filial.
* **DocumentTypeCode:** Código do Tipo de documento.
* **CurrencyCode:** Símbolo da moeda.
* **IssueDate:** Data de emissão.
* **ExpirationDate:** Data de vencimento.
* **ExpectedDate:** Data da previsão de baixa.
* **CurrentDate:** Data atual.
* **BankInformation:** Informações do banco.
* **Code (Tag Bank):** Código do Banco.
* **CashAccountCode:** Código do caixa a ser utilizado.
* **ValueOfDiscount:** Valor de desconto.
* **ValueOfInterest:** Valor de juros.
* **ValueOfFine:** Valor de multa.
* **ValueOfService:** Valor de serviço.

   
 **Exemplos de como configurar Xml para Inclusão e Exclusão**  
    
    
 **Inclusão:** A inclusão de um movimento é feita quando é informado 0 (zero) a Tag de <Code> e o tipo do evento da mensagem padrão enviada por parâmetro ao WebMethod. Exemplo:  
 ......  
 <BusinessEvent>   
 **<Event>upsert</Event>**  
 </BusinessEvent>  
 <BusinessContent>  
 ......  
 **<Code>0</Code>**  
 ....  
 </BusinessContent>  
 ...  
 **Exclusão:** A exclusão de um lançamento financeiro é feita quando é informado o numero do lançamento referente na Tag <Code> e o tipo do evento da mensagem padrão enviada por parâmetro ao WebMethod. Exemplo:  
 ......  
 <BusinessEvent>   
 **<Event>delete</Event>**  
 </BusinessEvent>  
 <BusinessContent>  
 ......  
 **<Code>1021</Code>**  
 ....  
 </BusinessContent>  
 ...  
    
 **2. Baixa**  
    
 Baixa (total ou parcial) de Lançamento Financeiro considerando o novo modelo de baixas do Gestão Financeira.  
 Formato de XML utilizado para realizar **Baixa** em lançamentos financeiros:  
 ***-> Cabeçalho do XML:***  
    
 <TOTVSMessage>  
 <MessageInformation>  
 <UUID>Baixa</UUID>  
 <Type>BusinessMessage</Type>  
 <Transaction>Baixa</Transaction>  
 <StandardVersion>1160</StandardVersion>  
 <SourceApplication>TOTVS SA</SourceApplication>  
 <CompanyId>21.867.387/0001-58</CompanyId>  
 <Product>RM</Product>  
 <GeneratedOn>2010-09-06T16:25:23Z</GeneratedOn>  
 <DeliveryType>Sync</DeliveryType>  
 <QUEUETYPE>1</QUEUETYPE>  
 </MessageInformation>  
 ***-> Configurações do XML:***  
 <BusinessMessage>  
 <BusinessEvent>  
 <Entity>Baixa</Entity>  
 <Event>upsert</Event>  
 <Identification>  
 <key name="key1">IDFLAN</key>  
 <key name="key2">CODCOLIGADA</key>  
 </Identification>  
 </BusinessEvent>  
 ***-> Passando informações via XML:***  
 <BusinessContent>  
 <CompanyId>1</CompanyId>  
 <Code>6906</Code>  
 <CurrentDate>2011-04-07</CurrentDate>  
 <User>mestre</User>  
 <ListOfConditionalPayment>  
 <ConditionalPayment>  
 <CompanyIdCashAccountCode>1</CompanyIdCashAccountCode>  
 <CashAccountCode>0001</CashAccountCode>  
 <Code>001</Code>  
 <Value>25</Value>  
 </ConditionalPayment>  
 <ConditionalPayment>  
 <CompanyIdCashAccountCode>1</CompanyIdCashAccountCode>  
 <CashAccountCode>0001</CashAccountCode>  
 <Code>2</Code>  
 <Value>25</Value>  
 </ConditionalPayment>  
 </ListOfConditionalPayment>  
 </BusinessContent>  
 </BusinessMessage>  
 </TOTVSMessage>  
    
    
 **Referente a este bloco de tag´s, deve-se alterar os mesmos conforme suas descrições:**

* **CompanyId:** Código da Coligada.
* **User:** Código do Usuário
* **Code:** Numero do Lançamento Financeiro (Tabela: Flan – Campo: IDLan).
* **CurrentDate:** Data atual.
* **CompanyIdCashAccountCode:** Cod. Coligada da conta caixa a ser utilizado.
* **CashAccountCode:** Código do caixa a ser utilizado.
* **Code:** Código referente à condição de pagamento.
* **Value:** Valor a ser baixado do Lançamento selecionado.

**Exemplo de como configurar Xml para Baixa:**  
    
 A baixa de um lançamento financeiro é feita quando é informado o Numero do lançamento referente na Tag <Code> e o tipo do evento da mensagem padrão enviada por parâmetro ao WebMethod. Exemplo:  
 ......  
 <BusinessEvent>   
 **<Event>upsert</Event>**  
 </BusinessEvent>  
 <BusinessContent>  
 ......  
 **<Code>1021</Code>**  
 ....  
 </BusinessContent>

---
