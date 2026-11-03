---
article_id: 30098223824151
category: ACOMPANHA CUSTOS - JORNADA DE FECHAMENTO (NOVO)
content_hash: 07495797a4b49551f91b53c03150ba4b7e9f247e12f1ecfbc63d4bf20adb1eb0
fetched_at: '2026-06-28T22:38:48.077542+00:00'
product: protheus
section_id: 5367899706647
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como depurar a rotina
  Acompanha custos via browser?
type: support-article
updated_at: '2026-03-09T13:01:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30098223824151-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-depurar-a-rotina-Acompanha-custos-via-browser
---

O artigo explica como debugar a rotina Acompanha Custos via web no Protheus 12.1.33, utilizando ferramentas do navegador (como o console e a aba Network) para identificar erros de JavaScript e monitorar requisições HTTP. Destaca a importância de analisar códigos de status HTTP, como 500 (erro interno do servidor) e 400 (requisição malformada), para diagnosticar problemas e garantir a comunicação com APIs REST.

![relogio_tempo_leitura_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30098223790871) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como debugar o acompanha custos via web? e oque pode ser avaliado no debug da rotina?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Protheus Release 12.1.33  
  
**Solução**  
Apresentaremos detalhes técnicos sobre as inovações no framework Angular e a estilização PO UI do Backoffice Protheus. O conhecimento desses aspectos é fundamental para auxiliar na análise e solução de eventuais inconsistências na rotina de processamento Acompanha Custos.

**Debug - Aplicação web embarcada**

Valide a configuração da Multiprotocolport: <https://tdn.totvs.com/display/tec/Application+Server+-+Porta+Multiprotocolo>

O debug vai por meio da aplicação WEB para identificação de erros, aqui iremos dar o exemplo no navegador Google Chorme, através da tecla **F12**

**![Screenshot_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30098223792407)**

**Tipos de validação com a depuração que podem ser avaliados:**

**Console**

O console é utilizado, na maior parte do tempo, para visualizar erros e alertas de JavaScript, além das chamadas AJAX. Ele permite a análise de erros relacionados ao Front-End e falhas em consultas às APIs.

![Screenshot_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30098239599895)

**Network**

A guia **"Network"** funciona como um sniffer de proxy integrado, permitindo a monitoração do tráfego HTTP da página tanto durante o carregamento quanto após sua conclusão.

Todas as requisições às APIs, independentemente do verbo utilizado (**GET, POST, DELETE**, etc.), geram tráfego HTTP e são listadas nessa guia. Além disso, a ferramenta exibe diversas informações relevantes, como o endereço da requisição, o corpo da requisição, a resposta e seu status. Dessa forma, a guia **"Network"** torna-se uma excelente opção para a análise de erros e diagnóstico de falhas.

![Screenshot_3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30098223797399)

**Status da Requisição**

As APIs REST utilizam a parte **Status-Line** de uma mensagem de resposta HTTP para informar aos clientes o resultado geral da solicitação.

Para localizar o status da requisição, observe a **Status-Line** na resposta, que contém o código de status HTTP, o qual indica o sucesso ou a falha da operação solicitada.

![Screenshot_4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30098223798679)

**Status 500**

**Erro Interno do Servidor**

Esse pode ser o erro mais comum nas requisições, onde a grande maioria é em relação a problemas de conexão entre o sevidor de aplicação e o servidor REST. O servidor encontrou uma condição inesperada que o impediu de atender à solicitação. Para esses casos, é normalmente recomendado verificar a data de atualização do fonte da API, bem como a comunicação e estabilidade do serviço **REST**.

![Screenshot_5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30098239603351)

**Status 400**

A solicitação não pôde ser compreendida pelo servidor devido a uma sintaxe incorreta. O cliente **não deve** repetir o pedido sem modificações.

Normalmente, o serviço está preparado para esse tipo de situação e devolve uma mensagem explicativa sobre o que causou a inconsistência, além de orientar sobre como ajustar a solicitação. Caso essa mensagem não seja apresentada, o problema pode estar relacionado à configuração do ambiente ou até mesmo a um fonte desatualizado da API envolvida no processo.

![Screenshot_6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30098239604375)

Este resumo técnico é direcionado **ao analista técnico do cliente**, com conhecimentos em programação, para que possa avaliar e coletar dados relacionados a problemas no uso da rotina **MATA038,** caso não possuir, o processo podera ser feito via Consultoria, conforme preve escopo de atendimento [**Guia de Relacionamentos**](https://tdn.totvs.com/x/NOJeI)

**Saiba mais**:

[*Clique aqui e veja mais artigos sobre a Nova Jornada de Fechamento no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/5367899706647-ACOMPANHA-CUSTOS-JORNADA-DE-FECHAMENTO-NOVO-)
