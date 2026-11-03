---
article_id: 13345491020951
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 330a7ee58a1d5819ebebbb96b51ca6e4d5816376197914c9209ad2307d4c5b6d
fetched_at: '2026-06-28T22:42:02.660189+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Como gerar o
  registro E115 para a tag cBenef?
type: support-article
updated_at: '2023-03-24T19:48:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13345491020951-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-o-registro-E115-para-a-tag-cBenef
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Dúvida**

Como gerar o registro **E115 - INFORMAÇÕES ADICIONAIS DA APURAÇÃO – VALORES**   
**DECLARATÓRIOS** para a tag cBenef?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**

**Solução**

Para solucionar essa dúvida, realize os seguintes passos:

A TAG **cBenef** é validada pela **UF do emitente**, sendo assim para **UF de transmissão de nota.**  
   
Para gerar a tabela **CDV** realize os seguintes passos:  
   
-  Configure os parâmetros;

* **MV\_ESTADO = SC**
* **MV\_GIAEFD = .F.**

O processo da tag é somente para emitentes dos estados **RS/SC/PR/RJ/DF/GO/SC.**

O processo irá utilizar a tabela 5.2 da SEFAZ alimentando a tabela **CDO** por possuir 8 caracteres, segue orientação do como efetuar importação:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026396974-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Atualiza%C3%A7%C3%A3o-tabela-CDO?source=search>

- Agora, deve acessar a rotina **FISA140 - Prod. x Cod.V.Decl** e crie a **amarração** na rotina.  
   
**Informar:**

* Produto
* CFOP da operação a ser aplicado aquele código
* Cod. Val. Decl (Tabela 5.2 da receita federal)
* CST
* Código de Reflexo conforme a sua necessidade
* Obs.Lan.Fis

Exemplo:  
![](https://totvssuporte.zendesk.com/attachments/token/2ymRuEZGTvdvpk118HmuajpRb/?name=image.png)

Após concluir, ir no **MATA410** - **Pedido de venda** e realizar inclusão do pedido de venda.  
   
Depois que anexar o cliente, produto, quantidade, valor unitário e total, informe a TES devidamente configurada. Vá em Outras ações >  Planilha >Aba lançamento de apuração e clicar em Valores Declaratórios.  
   
Neste momento irá apresentar as informações para tag cBenef  
   
![](https://totvssuporte.zendesk.com/attachments/token/0FvokhBITNlA9xOLJTpOBQCOl/?name=image.png)

Rode a **apuração - MATA953** e gere o **Sped Fiscal**.

Irá apresentar o registro mencionado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13344855980439)

Documentação complementar:

<https://tdn.totvs.com/display/public/PROT/3685244+DSERFIS1-8591+DT+Tratamento+para+preencher+tag+cBenef+com+tabela+da+receita+5.2>
