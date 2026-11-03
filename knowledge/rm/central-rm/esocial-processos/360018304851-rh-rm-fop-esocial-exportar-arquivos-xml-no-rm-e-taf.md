---
article_id: 360018304851
category: esocial - Processos
content_hash: 9c8289e70ed236235a9600b10d3b67d7c5625ae829e06b15d0aab1efef83fd2b
fetched_at: '2026-06-28T22:47:08.366261+00:00'
product: rm
section_id: 1500000834441
source: central-rm
title: RH - RM - FOP - eSocial - Exportar arquivos XML no RM e TAF
type: support-article
updated_at: '2024-06-05T12:21:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018304851-RH-RM-FOP-eSocial-Exportar-arquivos-XML-no-RM-e-TAF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19111327926551)**Tempo aproximado para leitura: **00:02:20 min**

**Dúvida**Como realizar a exportação de arquivos XML gerados para o eSocial no RM e TAF?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para exportar o arquivo XML gerado pelo sistema para atender os eventos do eSocial, siga os passos abaixo:  
• **RM**1. Acesse o menu **eSocial | Fila de Eventos** (no caso de tabelas e não-periódicos) ou **eSocial | Eventos Periódicos;**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19111300008599)

2.Edite o evento que já tenha o XML gerado;  
 2.1 Para eventos de envio, acesse a sub-aba **Mensagem XML** clique no botão **Salvar XML**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19111327937943)

2.2. Para eventos totalizadores [CLIQUE AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6214979985175-RH-RM-FOP-eSocial-Middleware-Como-exportar-XML-de-retorno-do-Governo);

3. Salve o arquivo em um diretório da máquina.

**• TAF**1. Acesse **Atualizações | Eventos eSocial** e selecione o menu conforme o evento desejado. Exemplo: Extrair XML do S-2200 - Acesse **Atualizações | Eventos eSocial | Trabalhador | Cadastro Trabalhador**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013653992)

2. Após abrir o cadastro, selecione o registro em questão (no caso do exemplo acima, o funcionário desejado) e clique em **Outras ações | Gerar XML eSocial**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013675171)

3. Será exibida uma mensagem solicitando a seleção do tipo de evento desejado. Clique em **Confirmar**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013655092)

4. O arquivo será salvo na pasta **[diretório]/TAF/System** conforme mensagem apresentada na tela. O nome do arquivo também poderá ser verificado na mensagem.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013676331)

**Importante**Lembre-se que o processo deverá ser feito conforme o evento desejado. Caminhos no TAF a serem selecionados considerando os eventos abaixo:

* **S-1000:** Atualizações | Configs.TAF | Complemento cadastral
* **S-1005:** Atualizações | Eventos ESocial | Tabelas | Estab, Obras Ou...
* **S-1010:** Atualizações | Eventos Esocial | Tabelas | Rubricas
* **S-1020:** Atualizações | Eventos Esocial | Tabelas | Lotações Tributárias
* **S-1070:** Atualizações | Eventos Esocial | Tabelas | Processos Administrativos
* **S-1200:** Atualizações | Eventos Esocial | Periódicos | Folha de Pagamento
* **S-1210:** Atualizações | Eventos Esocial | Periódicos | Pgto Rend Trab
* **S-1260:** Atualizações | Eventos Esocial | Periódicos | Com.  Rural. Pf
* **S-1295:** Eventos Esocial | Periódicos | Totaliz. Pag. Contingência
* **S-1298:** Atualizações | Eventos Esocial | Periódicos | Reabertura Periódicos
* **S-1299:** Atualizações | Eventos Esocial | Periódicos | Fechamento Periódicos
* **S-2190:** Atualizações | Eventos Esocial | Trabalhador | Admissão Preliminar
* **S-2200:** Atualizações | Eventos Esocial | Trabalhador | Cadastro Trabalhador
* **S-2230:** Atualizações | Eventos Esocial | Não-Periódicos | Afastamento Temporário
* **S-2299:** Atualizações | Eventos Esocial | Não-Periódicos | Desligamento
* **S-2399:** Atualizações | Eventos Esocial | Trabalhador | Término Trabalhador Sem Vínculo
* **S-5001:** Atualizações | Eventos Esocial | Totalizadores | Cont.Social Por trabalhador
* **S-5002:** Atualizações | Eventos Esocial | Totalizadores | Irrf Por Trabalhador
* **S-5003:** Atualizações | Eventos Esocial | Totalizadores | Fgts Por Trabalhador
