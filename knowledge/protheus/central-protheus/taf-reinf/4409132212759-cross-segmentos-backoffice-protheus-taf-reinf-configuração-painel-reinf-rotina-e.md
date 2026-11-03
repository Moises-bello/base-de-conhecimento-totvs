---
article_id: 4409132212759
category: TAF - REINF
content_hash: ec6c4ffe722047ba3a971464d05eba508f4b659eb9441e90bfb8b7b3646cf4f2
fetched_at: '2026-06-28T22:41:34.587544+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Configuração Painel Reinf
  - Rotina e Parâmetros
type: support-article
updated_at: '2023-10-06T12:55:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409132212759-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Configura%C3%A7%C3%A3o-Painel-Reinf-Rotina-e-Par%C3%A2metros
---

**Dúvida**

Como configurar o TAF do Futuro

**Ambiente**

TAF - A partir de 12.1.23

**Solução**

Após a conclusão da configuração do link [TAF – REINF - Configuração Painel Reinf - Appserver](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409133202199-TAF-REINF-Configura%C3%A7%C3%A3o-Painel-Reinf-Appserver?source=search),

efetuar a conclusão da configuração a seguir.

O Painel REINF tem como objetivo centralizar as tarefas referentes a entrega da obrigação Fiscal EFD-REINF. Anteriormente as mesmas eram realizadas em diversas rotinas dentro do TAF. A partir de agora com poucos cliques será possível realizar as principais tarefas como: apuração, transmissão e monitoramento de eventos, incluindo os eventos de fechamento e reabertura de período, de uma maneira muito mais intuitiva. Além de ter uma visão geral através de um painel de eventos que permite a extração dos relatórios das entregas.

Caso o ambiente esteja em Cloud Totvs, será informado as URLs do HTTP e REST para ser preenchida nos parâmetros abaixo.

Parâmetros

 O preenchimento dos parâmetros podem ser realizados na rotina ao acessar o menu Painel REINF, E-social do futuro ou pode ser preenchidos no configurador realizando o filtro por parâmetros.

![TAF_do_futuro.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409132170519)

Em casos aonde não consiga preencher na rotina ou no configurador será necessário criar os seguintes parâmetros para a instalação no configurador.

* Criar o parâmetro **MV\_GCTPURL** do tipo caractere, com o conteúdo http://{hostname-do-servidor}:{porta-http}
* Criar o parâmetro **MV\_BACKEND** do tipo caractere, com o conteúdo [http://{hostname-do-servidor}:{porta-rest}/rest](http://%7Bhostname-do-servidor%7D:%7Bporta-rest%7D/rest) . OBS: caso a URL da linha URI, da seção HTTPREST esteja diferente, por exemplo, URL = /app, o parâmetro deve ser preenchido com ip:porta/app.
* Criar o parâmetro **MV\_TAFPO** do tipo lógico, com .T. se possui mais módulos de Protheus além do TAF ou possui mais de uma placa de rede no servidor onde está sendo executado o serviço HTTP e com .F. se possui apenas o TAF e apenas uma placa de rede;

REINF

O parâmetro **MV\_TAFVLRE**precisa estar com o conteúdo **2\_01\_02**

[TAF - CONFIGURADOR - Como acessar os parâmetros do sistema?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036109233-TAF-CONFIGURADOR-Como-acessar-os-par%C3%A2metros-do-sistema-?source=search)
