---
article_id: 16194239222423
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: 4fcd6c733fed5d3ceaf9337e7b1ff7fd7d81d7c7e507c53bfeae0e355adbef44
fetched_at: '2026-06-28T22:45:21.016527+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Painel eSocial do Futuro (monitor) fica
  Carregando Informações do Ambiente.
type: support-article
updated_at: '2026-06-26T11:46:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16194239222423-RH-Linha-Protheus-TAF-eSocial-Painel-eSocial-do-Futuro-monitor-fica-Carregando-Informa%C3%A7%C3%B5es-do-Ambiente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16194229615255) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**Ao acessar o monitor Painel eSocial do Futuro, no TAF, a mensagem **"Carregando Informações do Ambiente"** é apresentada, e a rotina não carrega.

Exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16192329680023)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação Fiscal - e-Social - Rotinas Comuns - Monitor - Painel eSocial do Futuro (TAFA552A) - Á partir da versão 12.1.33  
  
**Causa**A mensagem pode ocorrer em diversas situações que estamos mapeando, elaboramos abaixo, alguns procedimentos que podem ser realizados para que o problema seja solucionado;  
  
**Solução**Abaixo alguns procedimento que podem ser executados para solucionar o problema, da mensagem **"Carregando Informações do Ambiente"** no monitor **Painel eSocial do Futuro**:

**1.** Verifique se o ambiente está atualizado, com a última expedição contínua e artefatos. Este ponto é essencial, para o correto funcionamento do novo monitor:

Expedição Contínua:

[Automação Fiscal - Atualização TAF - Expedição contínua no TAF (eSocial)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4484557005207)

Artefatos:

*LIB:*

[Automação Fiscal - Atualização - Como atualizar a LIB no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10486499915159)

*Binários:*

[Automação Fiscal - ATUALIZAÇÃO - Como atualizar o Binário no TAF?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034942753)

*DBAccess:*

[Automação Fiscal - ATUALIZAÇÃO - Como atualizar o DBAccess para o TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034522854)

**2.** Pare todos os serviços utilizados para o Protheus.

[Automação Fiscal - Configuração - Como parar os serviços do TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5519781139479)

Em seguida suba os serviços, seguindo a ordem abaixo:

1° Servidor de licenças  
2° Dbaccess  
3° Appserver  
4° Demais serviços 

**3.** Renomeie a pasta existe **http-root**, localizada dentro da pasta **Protheus Data**

Exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16192930538775)

Realize novamente o procedimento do **ITEM 2**desta documentação.

Acesse a rotina **Painel eSocial do Futuro**, para que a pasta **http-root** seja recriada.

**4.** Se seu ambiente já está configurado com a **Porta Multi Protocolo**, valide se as chaves dentro do **appserver.ini** (Master e Slaves se possuir) estão corretas:

[Automação Fiscal - Configuração - Como ativar a porta multi protocolo no TAF - MPP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4477439959063)

**5.**  Valide o nome inserido no **sys\_company (sigamat.emp)** para as filiais, se possuem o caractere barra **"\"**, caso possua, é necessário inverter a barra **"/" ou retira-la** do nome.

a) Abra o configurador para verificar: SIGACFG

[Automação Fiscal - CONFIGURADOR - Como acessar o configurador?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036108413)

b) Com o configurador aberto selecione no menu:

**Ambiente>Empresas>Filial**

c) Valide se alguma das filiais criadas, possui em seu nome a barra **"\"**, no campo **Descrição**:

*Exemplo:*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16424295081751)

d) Caso possua, altere o nome, inserindo a barra **"/"** ou **retirando** a barra do nome:

*Exemplo:*

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/16423750394519)**ou![](https://centraldeatendimento.totvs.com/hc/article_attachments/16423794425623)

\*\*Na tabela sys\_company (sigamat.emp) o campo correspondente é o M0\_FILIAL;

**6.** Caso o erro persista, realizar abertura de chamado junto do suporte TOTVS, informando:

a) Se o sistema está utilizando Porta Multi Protocolo ou  serviço REST;

b) Anexe o appserver.ini do Protheus (Master), Slaves e serviço REST se possuir;

c) Anexe os consoles (console.log) dos appserver´s;

**7. Se o erro na rotina Painel eSocial persistir:**

Abra um ticket para o suporte TOTVS TAF Esocial, e anexe as informações abaixo:

\*Print do erro;

\*Print da tela de diagnostico do TAF;

\*Extrato dos Fontes;

\*Cópia dos arquivos **appserver.ini** do Protheus Master (principal), REST e Slaves (balances), se possuir;

\*Cópia dos arquivos **console.log** do Protheus Master (principal), REST e Slaves (balances), se possuir;

\*Para gerar os arquivos do **console.log**, siga as orientações abaixo:

**a)** Habilite a chave **fwlogmsg\_debug=1** no(s) arquivo(s) **appserver.ini** dentro do grupo [**ENVIRONMENT]**(ambiente);

**b)** Após habilitar, **renomeie** o(s) **console.log** existente(s). **Gere o erro**na rotina Painel eSocial, e encaminhe para o suporte o(s)**novo(s) arquivo(s) console.log**
