---
article_id: 1500011971262
category: Gestão de Transportes (TMS)
content_hash: e704ecbde4ee084176e5c828e52312d745f287233c6a60f0b4e34ab7baee769d
fetched_at: '2026-06-28T22:45:27.464333+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Como gerar o TOTVS Replay
type: support-article
updated_at: '2025-08-15T12:55:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011971262-Log%C3%ADstica-Linha-Protheus-TMS-Como-gerar-o-TOTVS-Replay
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24682629546519)*** Tempo aproximado para leitura: **00:02:00 min**  
**Dúvida**Como gerar o **TOTVS Replay**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**A geração do TOTVS Replay ocorre através da opção **SHIFT+F6** da rotina, a qual pode apresentar um dos dois métodos para geração.

* **Primeiro método de geração:**Para gerar o **TOTVS Replay**, acesse o Sistema utilizando o **SIGAADV**, e, na rotina que estiver apresentando a inconsistência, pressione **SHIFT+F6**. Navegue até a quinta aba **TOTVS Replay**.

![Captura_de_tela_2021-05-24_173617.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019487821)

* Nesta tela, deixe a opção **Incluir fontes de lib** em branco, e então, clique em **Iniciar** e em seguida **Concluir.**
* Execute o processo até que seja reproduzido o incidente, em seguida, pressione **SHIFT+F6** novamente,  navegue até aba do **Totvs Replay**, clique em **Finalizar** e em seguida **Concluir.**
* Ao finalizar, será apresentado a tela abaixo informado o diretório onde será salvo o arquivo que por padrão é sempre a pasta do **smartclient**.

![3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019488761)

* Localizar o arquivo e enviar via **ticket** para que o analista da **TOTVS** analisar o conteúdo gerado.

**Segundo método de geração:**

* Para gerar o **TOTVS Replay**, acesse o Sistema utilizando o **SIGAADV**, e, na rotina que estiver apresentando a inconsistência, pressione **SHIFT+F6**. Caso esteja utilizando a nova tela de **Central de Diagnóstico**, clique em **Replay** no menu lateral esquerdo da tela:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24682629552279)

* Na próxima tela, escolha onde será salvo o arquivo gerado, deixe em branco a opção de **Incluir fontes da LIB,** e clique em **Iniciar**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24682629555479)

* Após iniciar a gravação, clique em **Sair** no canto inferior esquerdo da tela:

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/24682655889943)**

* Realize os processos desejados, e ao concluir, pressione **SHIFT+F6** novamente, vá em Replay e clique em **Finalizar:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/24682655891863)**

* O arquivo foi gerado na pasta selecionada, então, basta retornar ao atendimento para continuidade do ticket.

**Importante**

* Para gravar as informações, **NÃO é recomendado utilizar o SIGAMDI.**
* Deve-se chamar o módulo diretamente ou usar o **SIGAADV**.
* **O log é feito por thread.** O programa inicial **SIGAADV** e o programa inicial que chama diretamente os módulos, **SIGATMS** por exemplo, abre apenas uma thread, sem abas.
* Já o **SIGAMDI** abre uma **thread** por aba aberta. Desta forma, o log valerá apenas para a aba aberta em que for iniciado.

**Saiba mais**Para mais informações sobre **TOTVS Replay**, acesse o link: [TDS Replay](https://github.com/totvs/tds-vscode/wiki/TDS-Replay)
