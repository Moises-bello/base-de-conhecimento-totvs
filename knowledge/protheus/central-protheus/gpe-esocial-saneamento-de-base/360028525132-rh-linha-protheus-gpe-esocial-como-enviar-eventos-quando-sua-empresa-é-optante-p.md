---
article_id: 360028525132
category: GPE - eSocial - Saneamento de Base
content_hash: d80734c519a52e289a1ecd81c3f383e5ef1dde871b1ab7c19aa5f0d845cc0052
fetched_at: '2026-06-28T22:45:01.606455+00:00'
product: protheus
section_id: 360007319754
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - Como enviar eventos quando sua Empresa
  é optante pelo Simples Nacional?
type: support-article
updated_at: '2021-04-19T13:37:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028525132-RH-Linha-Protheus-GPE-eSocial-Como-enviar-eventos-quando-sua-Empresa-%C3%A9-optante-pelo-Simples-Nacional
---

**Dúvida**Como enviar eventos quando sua Empresa é optante pelo Simples Nacional?  
  
  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
  
  
**Solução** **1. S-1000:**Tudo começa pelo evento S-1000 que é gerado de acordo com o preenchimento do Complemento Cadastral do TAF.  
  
No evento S-1000 você deve informar a **Classificação Tributária** de sua Empresa de acordo com os Códigos previstos na tabela 08 do anexo I do leiaute do eSocial da versão vigente.  
  
**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029478071/mceclip3.png)**O RET (Governo) prevê três códigos diferentes de Optantes pelo Simples Nacional e a sua escolha influenciará tudo o que for enviado posteriormente e para saber qual código você deve utilizar consulte o seu departamento jurídico e contábil. **![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029481972/mceclip4.png)  
  
2. S-1005:**  
No GPE para o cálculo da Folha de Pagamento você deve informar a opção pelo **Simples Nacional** na tabela **S037** e essa informação também servirá para geração correta dos próximos eventos.  
 **![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029478451/mceclip5.png)**  
Na mesma tabela S037 você deve informar sobre a **Substituição de Contribuição Previdenciária**, para mais informações acesse a documentação abaixo. Essa informação influência no envio do evento do evento S-1200 e na alíquota de INSS Empresa calculada pelo RET (Governo).  
 **[MP - GPE - eSocial - S-1200/S-2299 - De onde o Sistema busca a informação de Contribuição Substituída](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027090412)**  
No caso do evento **S-1005** e do **RAT** e **FAP** o **GPE** se baseia na informação da tabela S037 para o cálculo, porém essa informação não pode ir EM BRANCO para o TAF devido exigência do leiaute do eSocial. Se sua Empresa não recolhe os encargos devido a algum beneficio fornecido por alguma lei, você deverá informar qual o **FAP** e **RAT** corretos através da Tabela **S129** do **GPE**, essa informação será exclusiva para o eSocial e não influenciará o cálculo do **GPE**.  
  
Segue o artigo sobre essa opção: [MP - GPE - eSocial - S-1005 - Preenchimento do RAT e FAP das empresas do Simples Nacional](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022874972-MP-GPE-eSocial-S-1005-Preenchimento-do-RAT-e-FAP-das-empresas-do-Simples-Nacional?source=search)  
  
![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029479051/mceclip10.png)  
  
**3. S-1020:**  
No caso do evento **S-1020** de Empresas optantes pelo Simples Nacional também há casos de FPAS e Códigos de terceiros específicos, os Códigos devem estar previstos e de acordo com as validações da tabela 04 do anexo I do leiaute do **eSocial** da versão vigente.  
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029478911/mceclip9.png)  
  
O código de **FPAS** é informado no cadastro da **Filial** através do **SIGACFG**.  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029482632/mceclip8.png)  
  
A informação de Código de **Terceiros** é preenchida na tabela **S038** do GPE. Importante, para o eSocial vai a informação do Código e não da Alíquota preenchida na tabela **S038**.  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029478791/mceclip7.png)  
  
Se você informar qualquer código divergente isso influenciará o cálculo da Contribuição Previdenciária apresentado no evento **S-5011** e na **DCTFWEB**.  
  
**4. S-1280:**

A informação de Substituição de Contribuição Previdenciária é enviada através do evento S-1280 que pode ser gerado na rotina de Eventos Periódicos do GPE.  
 **![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029478631/mceclip6.png)  
  
![](https://totvssuporte.zendesk.com/attachments/token/MFWOTQmhjNri1NJ8gYYsmHWmj/?name=inline-471045736.png)**

Em caso de dúvidas com relação aos códigos utilizados sugiro que também efetue um questionamento diretamente ao RET  (Governo) através dos canais de comunicação disponíveis através do portal do eSocial.

* [Fale Conosco](http://portal.esocial.gov.br/servicos/contato-1)
* [Central de Atendimento: 0800 730 0888](https://portal.esocial.gov.br/servicos/contato-1)

**Saiba Mais**Para saber mais consulte os links abaixo:   
[MP - GPE - eSocial - S-1200/S-2299 - De onde o Sistema busca a informação de Contribuição Substituída](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027090412)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)   
[Chatbot eSocial](https://chat-app.meudroz.com/#/prechat?header=false&token=dG90dnMtdXNlci0yOkFrVGllLDIwMTck&customerKey=totvs&openDelay=0&typingDelay=2500&watsontoken=false&watsonuser=false&watsonurl=false)
