---
content_hash: e873fb0d32e7bc6217d36f9a054f9b1a9cd7fa54e8b3b659e000a68e0aa2cf6c
fetched_at: '2026-06-29T00:09:34.591384+00:00'
page_id: '425459197'
product: rm
source: tdn-rm
title: Atividade de Integração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459197
version: 9
---

**Atividade de Integração**

---

A Atividade de Integração para Fórmula Visual disponibiliza uma forma de envio das informações obtidas na Fórmula Visual para um WebService de mensageria padrão, no modelo especificado.   
   
É fornecida também a opção de transformar o dado por XSL antes do envio do mesmo.  
   
**Observação:** Para que este compartilhamento da informação seja efetuado o WebService de destino deve disponibilizar um WebMethod com a seguinte assinatura:  
   
\[WebMethod(EnableSession = true)\]   
public string receiveMessage(string pInMsg)   
   
**Arquitetura**

A Atividade de Integração é consumida internamente a uma Fórmula Visual, obtendo como entrada o DataSet a ser trafegado e o código da transformação a ser efetuada no dado. Esta transformação é necessária para que a mensagem seja gerada no padrão de Mensageria Totvs.   
   
  
   
   
**Fluxo das Informações**  
   
A atividade pode ser inserida em qualquer ponto da Fórmula Visual, obtendo como parâmetros de entrada um DataSet, que pode ser manipulado ou obtido através de outras atividades, e o "TransactionID" referente a transformação a ser efetuada no DataSet de entrada. O dado transformado é enviado para o WebService de destino da mensageria padrão.  
  
**Configuração**  
   
Para fazer uso da Activity é necessário parametrizar a integração com a Mensageria Padrão.   
Para isso acesse o parametrizador do TBC: RM | Integração | Ferramentas | Parâmetros  
   
Selecione o pacote "Configurações Gerais ByYou ESB" e clique em avançar.

Os parâmetros disponíveis são:

* **Nº de Tentativas de Envio :** Número de tentativas de envio da mensagem pela fila de integração.
* **Ativar Log Debug:** Parâmetro que define se (quando ativo) o processo "Reprocessar Fila de Integração" considerará mensagens com qualquer status. Caso o mesmo esteja desmarcado o mesmo processo considera somente mensagens com status de erro.
* **URL do WebService:** Caminho do URL de destino.
* **Diagrama Síncrono:** Diagrama utilizado pelo ESB para esta mensagem, caso trafegada Sincronamente.
* **Diagrama Assíncrono:** Diagrama utilizado pelo ESB para esta mensagem, caso trafegada Assincronamente.
* **Padrão de Mensagem Síncrono:**Informa se a mensagem deve ser trafegada Síncrona ou Assincronamente.

**Notas:**

* Para a integração com Mensageria Padrão é necessário configurar somente os parâmetros "URL do WebService" e "Nº de Tentativas de Envio". Após, é só clicar em avançar e concluir a parametrização.
* A transformação do dado é feita através do XSL cadastrado na visão de Transformação que pode ser encontrada na aba "Ferramentas" do contexto TBC. A transformação é obtida a partir dos dados da "TransactionID" e "DataServer" passados pela Formula Visual.
