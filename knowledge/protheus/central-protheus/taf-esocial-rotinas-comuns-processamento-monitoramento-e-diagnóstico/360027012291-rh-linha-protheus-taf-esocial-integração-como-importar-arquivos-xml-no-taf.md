---
article_id: 360027012291
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: 58db9a95220bfa95fed7650ac2dc026f023af4fecbc9f33b1318edd6091f40d6
fetched_at: '2026-06-28T22:45:21.170104+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Integração - Como importar arquivos XML
  no TAF
type: support-article
updated_at: '2024-05-24T19:08:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027012291-RH-Linha-Protheus-TAF-eSocial-Integra%C3%A7%C3%A3o-Como-importar-arquivos-XML-no-TAF
---

**Dúvida**Como realizar a Importação de arquivos XML gerado por softwares terceiros para o TAF?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF - Todas as versões  
  
**Solução**

1 - Quando o arquivo XML estiver pronto para a importação no TAF, devemos nos atentar com a nomenclatura dos arquivos. Devemos saber o código da filial da empresa no ERP, qual tipo de evento, e uma chave que possa identificar o evento no sistema.

Os arquivos XML´s devem ser ajustados individualmente, um arquivo XML por evento/colaborador, esta rotina não integra XML em lote.

**Formato:** Codigo\_Filial\_TipoDoEvento\_Chave  
**Exemplo:** 99\_01\_S-1010\_9901000001S101020191001.xml

2 - Caso não lembre qual o código de filial no TAF, acesse o complemento cadastral da sua empresa no TAF:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048480233)

3 - Verifica qual código de filial é o da sua empresa que deseja realizar a importação do arquivo:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047598234)

4 - Devemos criar uma pasta para realizar a importação dos arquivos para o sistema TAF. vamos mostrar criando o diretório, na pasta raiz de instalação do TAF como exemplo, mas você pode criar a pasta em outro local. Crie a pasta **xml** na pasta de instalação do TAF:

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047598294)**

5 - Acesse o TAF e clique em Miscelânea -> Integração -> Importação de Arquivos:  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048480393)

6 - Clique em **avançar**:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047598334)

7 - Clique no botão "..." para deixar selecionar o diretório para importar o arquivos:  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047598414)

8 - Localize o diretório que foi criado para importação dos arquivos XML's:  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048480473)

9 - Após selecionar o diretório, clique em Finalizar para importar os arquivos criados.   
No item **"Método de Importação"**, deixa selecionado o item **"3-Importa XML - Layout eSocial"**:  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047598454)

10 - Caso queira validar o processo, basta clicar em "**sim**", caso não queira validar, clique em "**não**":

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047620234)

11 - Se quiser visualizar se os XML's foram integrados com sucesso, clique em **"sim":**

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048501253)

12 - Selecione a data referente ao dia que integrou os eventos para o TAF:

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048501313)

13 - Verifique se os eventos foram incluídos com sucesso para o sistema:

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047620354)

14 - Tendo sucesso na integração, basta acessar o monitoramento para transmitir os eventos para o eSocial.
