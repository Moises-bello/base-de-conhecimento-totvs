---
article_id: 30095911670039
category: SIGAEST - CUSTOS
content_hash: 3724b10ad11040425320f2e529691d8827841f903ba7b992957e1feeb28063ed
fetched_at: '2026-06-28T22:39:00.696236+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como depurar a rotina
  Acompanha custos via browser?
type: support-article
updated_at: '2025-12-22T13:51:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30095911670039-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-depurar-a-rotina-Acompanha-custos-via-browser
---

![relogio_tempo_leitura_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30095894929175) Tempo aproximado para leitura: HH:MM:SS min  
  
**Dúvida**  
Como depurar a rotina Acompanha custos via browser?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Apresentaremos detalhes técnicos sobre as inovações no framework Angular e a estilização PO UI do Backoffice Protheus. O conhecimento desses aspectos é fundamental para auxiliar na análise e solução de eventuais inconsistências na rotina de processamento Acompanha Custos.

**Debug - Aplicação web embarcada**

Valide a configuração da Multiprotocolport: <https://tdn.totvs.com/display/tec/Application+Server+-+Porta+Multiprotocolo>

O debug vai por meio da aplicação WEB para identificação de erros, aqui iremos dar o exemplo no navegador Google Chrome, através da tecla **F12**

**![Screenshot_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30096746463255)**

**Tipos de validação com a depuração que podem ser avaliados:**

**Console**

O console é utilizado, na maior parte do tempo, para visualizar erros e alertas de JavaScript, além das chamadas AJAX. Ele permite a análise de erros relacionados ao Front-End e falhas em consultas às APIs.

![Screenshot_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30096807371159)

**Network**

A guia **"Network"** funciona como um sniffer de proxy integrado, permitindo a monitoração do tráfego HTTP da página tanto durante o carregamento quanto após sua conclusão.

Todas as requisições às APIs, independentemente do verbo utilizado (**GET, POST, DELETE**, etc.), geram tráfego HTTP e são listadas nessa guia. Além disso, a ferramenta exibe diversas informações relevantes, como o endereço da requisição, o corpo da requisição, a resposta e seu status. Dessa forma, a guia **"Network"** torna-se uma excelente opção para a análise de erros e diagnóstico de falhas.

![Screenshot_3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30096868364695)

**Status da Requisição**

As APIs REST utilizam a parte **Status-Line** de uma mensagem de resposta HTTP para informar aos clientes o resultado geral da solicitação.

Para localizar o status da requisição, observe a **Status-Line** na resposta, que contém o código de status HTTP, o qual indica o sucesso ou a falha da operação solicitada.

![Screenshot_4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30097056004119)

**Status 500**

**Erro Interno do Servidor**

Esse pode ser o erro mais comum nas requisições, onde a grande maioria é em relação a problemas de conexão entre o sevidor de aplicação e o servidor REST. O servidor encontrou uma condição inesperada que o impediu de atender à solicitação. Para esses casos, é normalmente recomendado verificar a data de atualização do fonte da API, bem como a comunicação e estabilidade do serviço **REST**.

![Screenshot_5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30097196148247)

**Status 400**

A solicitação não pôde ser compreendida pelo servidor devido a uma sintaxe incorreta. O cliente **não deve** repetir o pedido sem modificações.

Normalmente, o serviço está preparado para esse tipo de situação e devolve uma mensagem explicativa sobre o que causou a inconsistência, além de orientar sobre como ajustar a solicitação. Caso essa mensagem não seja apresentada, o problema pode estar relacionado à configuração do ambiente ou até mesmo a um fonte desatualizado da API envolvida no processo.

![Screenshot_6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30097196151191)

**Saiba mais**:

[*Clique aqui e veja mais artigos sobre a Nova Jornada de Fechamento no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/5367899706647-ACOMPANHA-CUSTOS-JORNADA-DE-FECHAMENTO-NOVO-)
