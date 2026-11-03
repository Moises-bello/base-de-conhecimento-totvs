---
article_id: 18713174729367
category: TAF - eSocial -TSS
content_hash: 719ada6a3eaea295053924d5291db94e23fab481d5a58336cb99cb86076c0600
fetched_at: '2026-06-28T22:45:21.885444+00:00'
product: protheus
section_id: 1500001536761
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial  - ATUALIZAÇÃO - Como atualizar o TSS do
  E-social?
type: support-article
updated_at: '2025-02-06T16:44:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18713174729367-RH-Linha-Protheus-TAF-eSocial-ATUALIZA%C3%87%C3%83O-Como-atualizar-o-TSS-do-E-social
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18713160299799) Tempo aproximado para leitura: 00:10:00 min**

**Dúvida**Automação Fiscal - ATUALIZAÇÃO - Como atualizar o TSS do E-social?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - ATUALIZAÇÃO - TSS - Como atualizar o TSS do E-social?

**Solução em vídeo:**

**\* As releases homologadas do TSS são 12.1.2310 ou superior;**

**\* Vídeo ilustrativo;**

**Solução (leitura):**

⚠ **Sempre realize um Backup da sua estrutura antes de realizar qualquer ação !** ⚠

Para atualização do TSS é necessário que você baixe os arquivos, links abaixo:

**OBS: Caso você queira migrar de Release, basta baixar os arquivos da Release desejada e substituir pela sua estrutura atual. Lembrando que o TSS é homologado apenas para a Release 12.1.2310 ou superior.**

Para saber qual é a sua release do TSS acesse a [tela de diagnóstico do TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17988545143063-Automa%C3%A7%C3%A3o-Fiscal-Rotinas-Comuns-Como-acessar-a-tela-de-diagn%C3%B3stico-no-TAF).

**Downloads:**

|  |  |  |
| --- | --- | --- |
| **Arquivos** | ``` Release 12.1.2310 ``` | ``` Release 12.1.2410 ``` |
| Binário do TSS (Appserver) - **Windows** | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1112215) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1168420) |
| URL do TSS | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/761864) | [Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025394911-Cross-Segmentos-TSS-Atualiza%C3%A7%C3%A3o-das-URLs-do-TSS) |
| Schemas do TSS | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=761857) | [Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552-Cross-Segmentos-TSS-Atualiza%C3%A7%C3%A3o-dos-SCHEMAS) |
| RPO do TSS | [Clique aqui](http://suporte.totvs.com/totvs-tdi-files-maps/mapeamentos/portal-anexos/anexos/zendesk/20240110/TTVFLGP1J001-1704916789657-344408.zip) | [Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-Cross-Segmentos-TSS-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS) |

**OBS: Para baixar os binários para Linux em qualquer versão, [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1112216)**

Após baixar todos os arquivos correspondentes a sua Release e versão do Sistema Operacional acima, extraia-os utilizando seu programa de extração da sua preferência.

![Extrair arquivo.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18728353284119)

Após descompactar os arquivos baixados iremos parar o serviço do TSS. Para isso basta acessar o gerenciador de tarefas clicando com o botão direito na barra de tarefas e depois acesse a opção "Gerenciador de Tarefas".

No Gerenciador de Tarefas você deve selecionar a aba "Serviços" e parar o serviço do TSS que normalmente é chamado de "APPSERVER-TSS". Clique com o botão direito em cima do mesmo e depois selecione a opção "Parar".

![Parar o serviço do TSS.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18736658148503)

Depois de parar os serviços, iremos atualizar primeiro o Binário do TSS.

Copie o conteúdo da pasta APPSERVER baixada e cole em sua pasta APPSERVER do TSS

```
Exemplo de caminho: C:\TSS\BIN\APPSERVER  
  
OBS: Lembrando que sua estrutura do TSS pode estar nomeada como SPED.
```

Caso não ache sua estrutura, valide com sua equipe de T.I ou com quem realizou a instalação do seu TSS. Lembrando que se o seu ambiente for **CLOUD TOTVS** deve [abrir uma solicitação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18029297135127-Automa%C3%A7%C3%A3o-Fiscal-ROTINA-Como-entrar-em-contato-com-o-suporte-do-TAF-) com a equipe do produto pedindo a atualização do TSS, caso não seja compartilhado.

![Binário Tss.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18736651235223)

Agora iremos atualizar a URL do TSS.

Copie o arquivo da pasta URL baixada (tssatuurl.json) e cole na pasta System do TSS

```
Exemplo de caminho: C:\TSS\system
```

![URL.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18736658169623)

O próximo passo é realizar a atualização do RPO do TSS.

Copie o arquivo da pasta RPO baixada, acesse a pasta apo, renomeie o seu arquivo do RPO atual e depois cole o RPO que foi baixado.

```
Exemplo de caminho: C:\TSS\APO
```

![RPO tss.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18736658193303)

Por ultimo iremos atualizar o Schemas do TSS.

Abra a pasta SCHEMAS\_TSS que foi baixada, copie todo o conteúdo dentro desta pasta e acesse sua estrutura do TSS. Na sua estrutura atual você perceberá que já contém uma pasta "Schemas"onde **recomendamos que você exclua ou renomeie a pasta da sua estrutura, recrie novamente com a mesma nomenclatura** e cole os arquivos da pasta SCHEMAS\_TSS baixada dentro da pasta recriada.

```
Exemplo de caminho: C:\TSS\Schemas
```

![Schemas.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18736651267095)

Após a atualização do TSS, vamos subir novamente o serviço do TSS e validar se a URL do TSS foi realmente atualizada.

Primeiro suba o serviço novamente do TSS acessando o Gerenciador de Tarefas.

![iniciar serviço do TSS.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18736658207511)

Com o serviço em execução, valide se o arquivo da URL (tssatuurl.json) some da pasta system do TSS após 30 á 60 segundos.

```
Exemplo de caminho: C:\TSS\system
```

![Validando arquivo json na system.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18736658213911)

Caso passe mais de 60 segundos e o arquivo continua na pasta system, acesse a pasta Semaforo do TSS, exclua o arquivo da mesma nomenclatura (tssatuurl.json) e depois reinicie o serviço do TSS.

![Exclusão do arquivo na pasta semaforo.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18736658219287)

Pronto, seu TSS já está atualizado !

Você não consegue validar se realmente foi atualizado via tela de diagnóstico, somente ver a Release do seu TSS.

Para validação, recomendamos que você veja se os arquivos da sua estrutura estão com a data de modificação atual.
