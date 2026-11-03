---
content_hash: 244bc1a40045468c179919a168cf5287f32e5d31e7092341bcbc99d818c0d9bc
fetched_at: '2026-06-29T00:09:37.277779+00:00'
page_id: '425459584'
product: rm
source: tdn-rm
title: Web Sevice Movimento (wsMov)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459584
version: 2
---

**Web Sevice Movimento (wsMov)**

---

Formato do Xml utilizado para Incluir/Alterar/Excluir movimentos:  
     
 **1 - Cabeçalho do Xml:**  
    
 <TOTVSMessage>

<MessageInformation>  
 <UUID>Moviment</UUID>  
 <Type>BusinessMessage</Type>  
 <Transaction>Moviment</Transaction>  
 <StandardVersion>1160</StandardVersion>  
 <SourceApplication>TOTVS SA</SourceApplication>  
 <CompanyId>1</CompanyId>  
 <Product>RM</Product>  
 <GeneratedOn>2011-06-02</GeneratedOn>  
 <DeliveryType>Sync</DeliveryType>  
 <QUEUETYPE>1</QUEUETYPE>

</MessageInformation>

**2 - Configurações do Xml:**

<BusinessMessage>

<BusinessEvent>

<Entity>Moviment</Entity>  
 **<Event>upsert</Event>**  
 <Identification>

<key name="key1">IDMOV</key>  
 <key name="key2">CODCOLIGADA</key>

</Identification>

</BusinessEvent>

**Observação:**

A tag "<Event>" é responsável por indicar se a ação será de Inclusão ou alteração (O comando a ser utilizado deve ser "upsert") ou de exclusão (Comando a ser utilizado deve ser "delete").

**3 - Passando informações via Xml:**

<BusinessContent>

<CompanyId>1</CompanyId>  
 **<Code>0</Code>**  
 <CodeTypeMov>1.1.01</CodeTypeMov>  
 <BranchCode>1</BranchCode>  
 <CodeLoc>01</CodeLoc>  
 <Type>P</Type>  
 <Status>A</Status>  
 <CostCenterCode>02.1.1.1</CostCenterCode>  
 <LanDate>2011-07-05</LanDate>  
 <IssueDate>2011-07-05</IssueDate>  
 <CancelDate>2011-07-05</CancelDate>  
 <PaymentCodition>001</PaymentCodition>  
 <ValueDiscount>0</ValueDiscount>  
 <ValueExpenditure>0</ValueExpenditure>  
 <ValueGross>70</ValueGross>  
 <Value>70</Value>

**Ação para INCLUIR e ALTERAR(<Event>upsert</Event>):**  
 **Referente à tag "Code", o mesmo deve estar preenchido com valor igual a "0" (Zero – Incluir) ou com o valor referente ao numero do Movimento (Alterar).**  
    
 **Ação para EXCLUIR (<Event>delete</Event>):**  
 **Referente à tag "Code", o mesmo deve estar preenchido com valor igual ao Numero do Movimento.**

<ListItems>

<Items>

<CompanyId>1</CompanyId>  
 <Code>0</Code>  
 <CodePrd>7</CodePrd>  
 <Amount>10</Amount>   
 <CodeUnd>UN</CodeUnd>  
 <ValueUnit>7</ValueUnit>  
 <ValueDiscount>0</ValueDiscount>  
 <ValueExpenditure>0</ValueExpenditure>  
 <ValueTotal>70</ValueTotal>  
 <Value>70</Value>

</Items>  
    
 **(Para adicionar mais itens, deve incluir o conjunto da tag "Items" novamente, ver abaixo:**  
    
 **<Items>**  
 **<CompanyId>?</CompanyId>**  
 **(………)**  
 **<Value>?</Value>**  
 **</Items> )**  
 </ListItems>  
 </BusinessContent>  
 </BusinessMessage>  
 </TOTVSMessage>  
    
 **Exemplo de Xml, para consumir o Web Method, clique no Link abaixo:**  
    
 [Exemplo Web Method Movimento](http://tdn.totvs.com/kbm#113698)  
     
 **4 - Referente a este bloco de tag´s, deve-se alterar os mesmos conforme suas descrições:**

* **CompanyId** = Código da Coligada.
* **Code** = Numero do movimento (Tabela: TMov – Campo: IDMov, deixar zero quando a ação for de inclusão, para excluir ou alterar o movimento, esta tag deve ser preenchida com o Numero do Lançamento Financeiro).
* **CodeTypeMov:** Código do Tipo de Movimento.
* **BranchCode:** Código da Filial.
* **CodeLoc:** Código do Local de Estoque.
* **Type:** Tipo.
* **Status:** Status do Movimento.
* **CostCenterCode:** Centro de Custo.
* **LanDate:** Data de Lançamento.
* **IssueDate:** Data de emissão.
* **CancelDate:** Data de Cancelamento.
* **PaymentCodition** = Código da condição de pagamento.
* **ValueDiscount:** Valor de desconto.
* **ValueExpenditure:** Valor da Despesa.
* \*\* ValueGross:\* Valor Bruto.
* \*\* Value:\* Valor Liquido.

Informação referente aos itens do Movimento:

* **CompanyId:** Código da Coligada.
* **Code** = Numero do movimento (Tabela: TMov – Campo: IDMov, deixar zero quando a ação for de inclusão, para excluir ou alterar o movimento, esta tag deve ser preenchida com o Numero do Lançamento Financeiro).
* **CodePrd:** Código do Produto.
* **Amount:** Quantidade do Item.
* **CodeUnd:** Código da unidade medida.
* \*\*\* ValueUnit:\* Valor unitário.
* **ValueDiscount:** Valor de desconto.
* **ValueExpenditure:** Valor da Despesa.
* \*\*\* ValueTotal:\* Valor Total do item.
* \*\*\* Value:\* Valor liquido.

({**}**{\*}) Estes campos devem conter a soma de todos os valores totais dos itens.  
 ({**}****{**}) Estes campos são obrigatórios seu preenchimento.

***Observação:***

A informação referente à quantidade, valor total, valor liquido deve ser informado de maneira correta, pois o Web Method de Financeiro não realiza consistência se os valores informados estão incorretos.  
    
 **Exemplos de como configurar Xml para Inclusão, Alteração e Baixa**   
    
  
 **Inclusão:** A inclusão de um movimento é feita quando é informado 0 (zero) a Tag de <Code> e o tipo do evento da mensagem padrão enviada por parâmetro ao WebMethod. Exemplo:  
 (....)  
 <BusinessEvent>   
 **<Event>upsert</Event>**  
 </BusinessEvent>  
 <BusinessContent>  
 (....)  
 **<Code>0</Code> (Código do Movimento)**  
 (....)  
 </BusinessContent>  
 (....)  
    
 <ListItems>   
 <Items>  
    
 (....)  
    
 **<Code>0</Code> (Código do Movimento referente ao item) -  Obrigatório**  
    
 **Observação: Para que a inclusão seja realizada, o valor desta tag Code deve estar igual ao valor da tag Code acima (referente ao Código de Movimento). Caso esteja diferente ocorrerá atualização.**   
    
 (....)  
    
 </Items>  
 </ListItems>  
 (....)  
    
 **Alteração:** A alteração de um movimento é feita quando é informado o numero do lançamento referente na Tag <Code> e o tipo do evento da mensagem padrão enviada por parâmetro ao WebMethod. Exemplo:  
 (....)  
 <BusinessEvent>   
 **<Event>upsert</Event>**  
 </BusinessEvent>  
 <BusinessContent>  
 (....)  
 **<Code>1021</Code> (Código do Movimento)**  
 (....)  
 </BusinessContent>  
 (....)  
    
 <ListItems>   
 <Items>  
 (....)  
 **<Code>0</Code> (Código do Movimento referente ao item) - Obrigatório**  
 **Observação: Para que a inclusão seja realizada, o valor desta tag Code deve estar igual ao valor da tag Code acima (referente ao Código de Movimento). Caso esteja diferente ocorrerá atualização.**   
 (....)  
 </Items>  
 </ListItems>  
 (....)  
 **Exclusão:** A exclusão de um movimento é feita quando é informado o numero do lançamento referente na Tag <Code> e o tipo do evento da mensagem padrão enviada por parâmetro ao WebMethod. Exemplo:  
 (....)  
 <BusinessEvent>   
 **<Event>delete</Event>**  
 </BusinessEvent>  
 <BusinessContent>  
 (....)  
 **<Code>1021</Code> (Código do Movimento)**  
 (....)  
 </BusinessContent>  
 (....)  
    
 <ListItems>   
 <Items>  
 (....)  
 **<Code>0</Code> (Código do Movimento referente ao item) - Obrigatório**  
 **Observação: Para que a inclusão seja realizada, o valor desta tag Code deve estar igual ao valor da tag Code acima (referente ao Código de Movimento). Caso esteja diferente ocorrerá atualização.**   
 (....)  
 </Items>  
 </ListItems>  
 (....)
