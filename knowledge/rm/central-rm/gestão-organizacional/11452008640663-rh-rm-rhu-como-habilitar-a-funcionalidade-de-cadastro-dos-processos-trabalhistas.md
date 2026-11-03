---
article_id: 11452008640663
category: Gestão organizacional
content_hash: a3370046a3589fa8ece278ad7f087e568aaa1b78c98220d1782d56b3995d906b
fetched_at: '2026-06-28T22:47:22.280571+00:00'
product: rm
section_id: 1500000861422
source: central-rm
title: RH - RM - RHU - Como habilitar a funcionalidade de cadastro dos Processos Trabalhistas
type: support-article
updated_at: '2026-06-01T12:28:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11452008640663-RH-RM-RHU-Como-habilitar-a-funcionalidade-de-cadastro-dos-Processos-Trabalhistas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15863978016791) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como habilitar a funcionalidade de cadastro dos Processos Trabalhistas?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - **12.1.34.263**, **12.1.2205.211**, **12.1.2209.155** e superiores.  
  
**Solução**  
A funcionalidade de cadastro dos **Processos Trabalhistas** poderá ser utilizada nos patches citados acima e superiores.

O menu está disponível no módulo **Gestão de Pessoas |** **Gestão Organizacional** | **Processos Trabalhistas**, conforme imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26674532809111)

Para habilitar o menu, basta seguir os passos abaixo:  
  
1. Acesse o módulo **Folha de Pagamento |** **Configurações | Parametrizador | Etapa eSocial | Configurações Gerais 1/7:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26674516081815)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36442540255127)

Obs: Para atender as alterações feitas para envio dos eventos S-2500 e S-2501, atualmente, o Leiaute atual é o S-1.3 NT 04/2025, portanto deve alterar o campo Versão do Leiaute para S-1.3 NT 04/2025. Este Leiaute só está disponível para as seguintes versões:

* 12.1.2410.295
* 12.1.2502.199
* 12.1.2506.141 e superiores

Segue maiores informações: [RH - RM - FOP - eSocial - Leiaute S-1.3](https://tdn.totvs.com/pages/releaseview.action?pageId=981772609)

2. Clique em **Avançar |** **Integração com TAF | Outros Parâmetros** e preencha os campos referente a **Servidor API, Servidor APP** e **Portas**.   
 

Nos campos **Servidor API** e **Servidor APP** deve informar o **IP de Servidor** ou **Nome de uma máquina** cuja qual possua o RM instalado. Este servidor será utilizado para acesso a tela em questão, dessa forma informe IP de um servidor correspondente a sua instalação de Produção caso seja ambiente oficial ou servidor de homologação caso seja teste.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26674516085655)

No campo **Porta** do **Servidor API** informar a mesma porta definida nos arquivos **RM.Host.exe.config** e **RM.Host.Service.exe.config** para a tag **APIPORT**.

No campo **Porta** do **Servidor APP** informar a mesma porta definida nos arquivos **RM.Host.exe.config** e **RM.Host.Service.exe.config** para a tag **HTTPPORT**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26674516092311)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26674516095639)

3. É necessário executar o **RM.Atualizador.exe** para que a funcionalidade seja apresentada;

[RH - RM - FOP - RM Atualizador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5893403025687)

4. Por se tratar de uma implementação, assim como as demais esta ficará disponível na visão, porém estará desabilitada. Será necessário acessar o perfil associado ao usuário e liberar o acesso ao menu:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26674532833431)

**Importante**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11454686472087)

**Saiba Mais**  
Para maiores informações sobre os Processos Trabalhistas, acesse:

- [RH - RM - RHU - Dúvidas frequentes: geração dos eventos de Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17623656599575)

- [Processo Trabalhista - Cadastros dos eventos S-2500 e S-2501](https://tdn.totvs.com/display/public/LRM/Processo+Trabalhista+-+Cadastros+dos+eventos+S-2500+e+S-2501)

- [RH - RM - RHU - Erros de conexão ao acessar o menu de Processos Trabalhistas - Middleware](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11700201570583)

- [RH - RM - RHU - Erros de conexão ao acessar o menu de Processos Trabalhistas (TAF e Smart)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11571907280663)
