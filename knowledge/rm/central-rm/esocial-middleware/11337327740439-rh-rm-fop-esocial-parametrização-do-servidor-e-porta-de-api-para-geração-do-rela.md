---
article_id: 11337327740439
category: eSocial - Middleware
content_hash: 5e2e09cd5dd72e15ab17c7ba2207d9d89416a33ccaadea8af621b628e19eeee7
fetched_at: '2026-06-28T22:47:05.542938+00:00'
product: rm
section_id: 1500000834541
source: central-rm
title: RH - RM - FOP - eSocial - Parametrização do Servidor e Porta de API para geração
  do Relatório de Conferência INSS/FGTS Middleware
type: support-article
updated_at: '2026-04-02T19:52:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11337327740439-RH-RM-FOP-eSocial-Parametriza%C3%A7%C3%A3o-do-Servidor-e-Porta-de-API-para-gera%C3%A7%C3%A3o-do-Relat%C3%B3rio-de-Confer%C3%AAncia-INSS-FGTS-Middleware
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24126939301015) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como parametrizar corretamente o servidor e porta de API do RM nas configurações do Middleware para geração do Relatório de Conferência INSS/FGTS?

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - A partir dos Patches 12.1.26.216, 12.1.27.172, 12.1.28.106 e superiores.  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
1. Acesse **Configurações | Parametrizador | eSocial | Integração Middleware | Outros Parâmetros**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11335898756887)

* No campo **Servidor**, será informado o IP da máquina onde está sendo executado o Serviço Host do **RM** (não inserir neste campo o endereço do Servidor de WebService do TAF), caso seja uma instalação local, será o IP da própria máquina (você pode conferir o IP através do Prompt de Comando do Windows, digitando *ipconfig*), Caso seja N Camadas, você deverá inserir o IP do servidor de Aplicação do RM;
* No campo **Porta**, você deverá informar a Porta definida nos arquivos **RM.Host.exe.config** e **RM.HostService.exe.config** localizados na pasta de instalação do RM, na tag '*ApiPort*':

![image.png](https://chat.google.com/u/0/api/get_attachment_url?url_type=FIFE_URL&content_type=image%2Fpng&attachment_token=AIGoCJlfaBQCJlLbqEbcW%2F2RIbSng%2BM%2BJgfYNQmbcs8UE4tIdcUDvGmn%2FJlWvfCQ6r9tKGJx0Em%2FaROEKBjBpqbioaVq%2FouVxJxhAZjgaImMrjHC5uzi%2B1vhhG%2FsInImm4MIMFtvawerg4iP4oTohzr%2FkUsY2VonBNQwCJX%2FMoGjFZm2h72z3Wzy4chnnhXl8x38iCh4I2T2i5lBGtu9nwICbwkAiWOREF%2BnTeQ8zXkIEpU2M%2F4gPha5VSBa9oSpi4VnLddHZ4%2B0qAbSECZuRj%2Fn1ASjhIOysJcJwtn0DyfyWz5O2ibD2J6Fe%2B2DhsLv6%2BG2%2FaLSxAhFzi9KQ7hgBPZnx8eyb1%2F2AUQKIwT4Qv16us%2FCC74gtBXbvUs1TH%2B9VYadZ86%2Fm73u%2Bd3WKuvl9VAlPlq%2FpTxHoEH0P7FtoiDN95ixSWf9ENtX5V1pS0x7Z9%2BMh7SF%2B1ZfBS0erfR7mgI%3D&sz=w512)

2. Após ter identificado o Servidor e Porta, será necessário reservar a Porta na rede, via **Prompt de Comando** no iniciar do **Windows** com o comando abaixo (executar como administrador):

```
netsh http add urlacl url=http://+:XXXX/ user=NetworkService
```

Substituir **XXXX** pela porta, por exemplo: 8053. Após execução do comando, será retornado a mensagem abaixo:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11336385564183)

3. Após realizar as alterações acima, será necessário parar o Host, e após inicializá-lo como **administrador**.

4. Ao finalizar as parametrizações, deverá testar a conexão com a API do RM no navegador, através do link: http://**servidor**:**porta**/api/swagger/ui/index#/

- Substituir **Servidor** e **Porta** pelo IP e Porta configurados anteriormente. Ao executar o *link* no navegador, deverá retornar a tela abaixo:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11336757299351)

7. Após execução do link anterior no navegador, retornando a página sinalizada acima, a geração do Relatório de **Conferência INSS/FGTS** poderá ser realizado normalmente.  
  
**Observações**1. Caso o teste com a conexão retorne com erro, o relatório não será gerado, podendo ser exibido mensagem de erro, ou o mesmo irá congelar em 1%. Um ponto importante, é verificar no *Firewall* da rede, se a porta utilizada como API não está com bloqueio.

2. É altamente recomendado que o processo acima seja feito pelo analista de TI da empresa devido ao nível de acesso administrador necessário para execução dos passos.
