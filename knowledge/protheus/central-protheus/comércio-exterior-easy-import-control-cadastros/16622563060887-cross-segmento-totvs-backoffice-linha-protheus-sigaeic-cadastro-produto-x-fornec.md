---
article_id: 16622563060887
category: Comércio Exterior - Easy Import Control - Cadastros
content_hash: f24b7a879d76e8d55b5041bf3b5c0aac657812f3cd01491a2463237dcd394a12
fetched_at: '2026-06-28T22:39:52.269108+00:00'
product: protheus
section_id: 1500001549382
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Cadastro Produto
  x Fornecedor "Valor atribuído difere do tamanho do campo (Descrição)".
type: support-article
updated_at: '2024-07-04T14:19:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16622563060887-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Cadastro-Produto-x-Fornecedor-Valor-atribu%C3%ADdo-difere-do-tamanho-do-campo-Descri%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16622598968215) Tempo aproximado para leitura: **04:00 min** **Dúvida**Como corrigir a mensagem ao inserir o Cadastro Produto x Fornecedor "Valor atribuído difere do tamanho do campo (Descrição)".  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16623094622743)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – A partir da versão12.1.33  
  
**Solução**Verifique dentro do Configurador o tamanho do campo "**A5\_NOMPROD"**, por padrão, tal campo possui o tamanho de 30 caracteres. Verifique também se este campo está com o mesmo tamanho do **"B1\_DESC".** Caso não esteja, efetue o ajuste via Configurador e após tal ação realize o procedimento novamente.

1. Acesse o módulo **SIGACFG** em Base de Dados, selecione Dicionário / Base de dados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16622562994967)

2. Selecione Dicionário de Dados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16622571149719)

3. Selecione a lupa.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16622614797591)

4. Selecione Procurar Por e informe a tabela **SA5** após selecione Buscar. 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16622340432407)

5. Posicione no campo "**A5\_NOMPROD",** selecione a folha com o lápis, verifique o tamanho do campo e iguale com o tamanho do campo "**B1\_DESC"**.

![](https://totvssuporte.zendesk.com/attachments/token/EVhzz6nLsw4dNbf3BA8BBS83g/?name=image.png)

6. Selecione Procurar Por e informe a tabela "**SB1"** após selecione Buscar. 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16622443628951)

7. Posicione no campo "**B1\_DESC",** selecione a folha com o lápis e verifique o tamanho do campo.

![](https://totvssuporte.zendesk.com/attachments/token/tOHeMbNN52c8o4GKje3HwzLvb/?name=image.png)
