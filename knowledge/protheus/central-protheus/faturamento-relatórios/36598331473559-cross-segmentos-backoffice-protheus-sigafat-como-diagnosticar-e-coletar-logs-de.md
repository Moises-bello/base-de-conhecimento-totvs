---
article_id: 36598331473559
category: FATURAMENTO - RELATÓRIOS
content_hash: 3f0c78b7076e23593d7fb7069136339dabb3433ef683ba3852dc17bcf6aa14ac
fetched_at: '2026-06-28T22:38:22.938830+00:00'
product: protheus
section_id: 1500001539381
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Como diagnosticar e coletar
  logs de erros no SmartView
type: support-article
updated_at: '2026-03-30T21:27:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36598331473559-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-diagnosticar-e-coletar-logs-de-erros-no-SmartView
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36598331460887) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**

Qual o procedimento correto para tratar e diagnosticar as ocorrências de erro apresentadas na tela ao gerar relatórios SmartView no módulo Faturamento?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

Caso um relatório do SmartView apresente erro em tela ou qualquer tipo de inconsistência durante a execução, é fundamental realizar a coleta dos *logs* do ambiente, a fim de possibilitar uma análise precisa e a identificação da causa do problema, considerando o uso de chaves importantes para corroborar com a análise.

**Importante**: As validações dos relatórios SmartView funcionam com linguagens avançadas. Por isso, é extremamente importante certificar-se das atualizações mais recentes em seu ambiente como um todo, antes de prosseguir com a coleta de logs:

- [Pacote de acumulados BackOffice - Conforme Release](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/Backoffice)  
- [LIB Atual](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/) - [Logo Guará](https://suporte.totvs.com/portal/p/10098/download?e=989259) | [Harpia](https://suporte.totvs.com/portal/p/10098/download?e=1050526)  
- [DBACCESS](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFDBA/search/searchAll)  
- [Appserver](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/)  
- [Smartclient](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFSC/search/searchAll) - [Lobo Guará](https://suporte.totvs.com/portal/p/10098/download#detail/947510) | [Harpia](https://suporte.totvs.com/portal/p/10098/download#detail/1112221)  
- [Central de Atualizações](https://suporte.totvs.com/portal/p/10098/download?e=946864#000006/368/TFSC/)

Ideal que todos os procedimentos devem ser realizados primeiro em ambiente de homologação atualizado.

**Configuração de Chaves para Mapeamento do Erro**

Antes da reprodução do erro, recomendamos configurar as seguintes chaves no ambiente. A ativação dessas chaves é crucial para mapear a origem e o fluxo do erro, fornecendo detalhes técnicos essenciais para a análise do suporte:

* **LogHttpFuncs=1**  
  Documentação: [TDN - LogHttpFuncs](https://tdn.totvs.com/x/MY5vI)
* **TraceStack=1**  
  Documentação: [TDN - TraceStack](https://tdn.totvs.com/x/jopc)
* **FWTRACELOG=1**  
  Documentação: [TDN - FWTRACELOG](https://tdn.totvs.com/x/Yc6qKg)

Essas chaves devem ser aplicadas no **AppServer.ini** do ambiente correspondente e estarão ativas durante a execução do serviço, após o processo de coleta, desative as chaves para evitar sobrecarga de logs desnecessários.

**Procedimento para Captura de Logs:**

1 - Após configurar as chaves acima no AppServer.ini, siga os passos a seguir imediatamente antes de reproduzir o erro:

2 - Apague o arquivo console.log da sessão atual do ambiente (presente na pasta log do AppServer ou onde você definiu para gravar o arquivo log).

3 - Reinicie o serviço do AppServer em modo exclusivo, se possível, para garantir integridade na coleta seja apenas nesse serviço. Caso não possa, certifique-se de que a coleta está sendo realizada no slave devido.

4 - Reproduza o erro novamente, executando o relatório que apresenta a falha.

5 - Envie o novo console.log gerado, juntamente com o log do SmartView (se possível)

6 - Capture uma imagem da rotina:

SIGACFG > Ambiente > Cadastros > Configuração TReports/Smart View (Opção: Token, no módulo Configurador).

7 - Informe se o problema ocorre em todos os relatórios ou apenas em um específico.

8 - Valide se o seu agent está atualizado e envie um print:

![Screenshot_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36598317798679)

**Onde é localizado os meus LOGS para coleta e envio?**

Os logs ficam nas pastas internas do seu ambiente. Você deve solicitar ao seu TIME de TI que pegue os logs caso você não tenha acesso.

**Meu ambiente é no T-CLOUD, como pego os logs?**

Se o seu ambiente é na **TOTVS** ***Cloud*** (T-CLOUD), a limpeza do console.log acaba não sendo muito viável de início, pois você precisa abrir uma solicitação para o time **CLOUD** realizar essa ação caso você não tenha acesso ao servidor.

No entanto, você pode efetuar a coleta dos *logs* no portal normalmente, ou via **FTP**. Isso também é um processo que pode ser efetuado por seu **time de T.I.**, ou por você, caso possua acesso ao portal do ambiente *Cloud:* [*CLOUD - MP - Download de logs (TCLOUD)*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408646347671-CLOUD-MP-Download-de-logs-TCLOUD)
