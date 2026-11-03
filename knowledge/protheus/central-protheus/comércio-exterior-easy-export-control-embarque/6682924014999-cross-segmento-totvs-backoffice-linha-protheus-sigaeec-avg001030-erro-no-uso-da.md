---
article_id: 6682924014999
category: Comércio Exterior - Easy Export Control - Embarque
content_hash: e778f6ab1c63d42281af639f70b198cfee304e330619e97dd7cef7d92c4c11f1
fetched_at: '2026-06-28T22:36:39.111239+00:00'
product: protheus
section_id: 1500001549322
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - AVG001030: Erro
  no uso da função avkey'
type: support-article
updated_at: '2022-06-10T20:24:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6682924014999-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-AVG001030-Erro-no-uso-da-fun%C3%A7%C3%A3o-avkey
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Ao atualizar do ambiente com a issue **DTRADE-7677**, ao gerar devolução de exportação na rotina de Documento de Entrada **(****MATA103****)** está apresentando a mensagem abaixo, teria alguma procedure no EEC ou parâmetro para validar esta mensagem?**"AVG001030 - Erro no uso da função AVKey: Função não compatível com o tipo de dado! Procedure TXDEVOLUCAO, linha 3536"**

![ERRO_DEVOLU__O.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/6676502541591/ERRO_DEVOLU__O.PNG)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões  
  
**Solução**Erro ocasionado pois o campo EEQ\_IMLOJA não estava marcado como a opção usado,  browser e a  
opção todos os módulos estava demarcado.  
Acessar o configurador - Base Dados - Dicionário - Base de Dados:

![BASE_DE_DADOS.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6682250603799/BASE_DE_DADOS.png)

1. Clique na opção Dicionário de Dados.
2. Pesquise pela Tabela **EEQ (Valor das Parcelas do Embarque)** .
3. Clique na opção Campos.
4. Pesquise pelo campos **EEQ\_IMLOJA**.
5. Clique no botão alterar.
6. Na aba **Uso** marque as opções Usado e Browser.
7. Na aba **Módulos marque todos os módulos**![EEQ_IMLOJA_-_USO.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/6682619290903/EEQ_IMLOJA_-_USO.PNG)

![EEQ_IMLOJA_-_MODULO.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/6682699977367/EEQ_IMLOJA_-_MODULO.PNG)  
Salve as alterações na configurador e ao efetuar um teste na geração da devolução na rotina de documento de entrada e mensagem não será mais exibida.  
  
**Saiba mais**[DTRADE-7677 - Devolução de Nota Fiscal de Exportação](https://tdn.totvs.com/pages/releaseview.action?pageId=686485640)
