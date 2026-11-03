---
content_hash: 4251b5fb08c3b1beba39aaa13be63dd6dedfae8ff1190c43281cd96fd87bea04
fetched_at: '2026-06-29T00:09:35.345262+00:00'
page_id: '425459319'
product: rm
source: tdn-rm
title: Web Service Financeiro - XML Baixa
type: documentation
url: https://tdn.totvs.com/display/LRM/Web+Service+Financeiro+-+XML+Baixa
version: 3
---

**Web Service Financeiro - XML Baixa**

---

Formato de Xml utilizado para realizar Baixa:  
  
**1 - Cabeçalho do Xml:**  
   
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

**2 - Configurações do Xml:**

<BusinessMessage>  
<BusinessEvent>  
<Entity>Baixa</Entity>  
<Event>upsert</Event>  
<Identification>  
<key name="key1">IDFLAN</key>  
<key name="key2">CODCOLIGADA</key>  
</Identification>  
</BusinessEvent>  
**3 - Passando informações via Xml:**  
   
<BusinessContent>  
<CompanyId>1</CompanyId>  
<Code>6906</Code>  
<CurrentDate>2011-04-07</CurrentDate>  
<User>mestre</User>  
<StatementDocumentNumber></StatementDocumentNumber>  
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
</TOTVSMessage>]]

**4** - Referente a este bloco de tag´s, deve-se alterar os mesmos conforme suas descrições:

**CompanyId**: Código da Coligada.  
**User**: Código do Usuário  
**Code**: Numero do Lançamento Financeiro (Tabela: Flan – Campo: IDLan).  
**CurrentDate**: Data atual.  
**StatementDocumentNumber**: Número Documento do Extrato (Campo opcional, caso seja informado, o valor será gravado no campo de Número Documento do Extrato da baixa do lançamento).  
**CompanyIdCashAccountCode**: Cod. Coligada da conta caixa a ser utilizado.  
**CashAccountCode**: Código do caixa a ser utilizado.  
**Code**: Código referente à condição de pagamento.  
**Value**: Valor a ser baixado do Lançamento selecionado.  
    
**Exemplo de como configurar Xml para Baixa:**  
   
A baixa de um lançamento financeiro é feita quando é informado o Numero do lançamento referente na Tag <Code> e o tipo do evento da mensagem padrão enviada por parâmetro ao WebMethod. Exemplo:  
  
<BusinessEvent>   
**<Event>upsert</Event>**  
</BusinessEvent>  
<BusinessContent>  
......  
**<Code>1021</Code>**  
</BusinessContent>
