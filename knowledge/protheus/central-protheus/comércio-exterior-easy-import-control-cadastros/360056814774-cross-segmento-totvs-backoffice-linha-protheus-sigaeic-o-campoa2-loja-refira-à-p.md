---
article_id: 360056814774
category: Comércio Exterior - Easy Import Control - Cadastros
content_hash: 4a5e7dd8bd189e5c1a137e42f6eb5557732e1abf49d5682c895f8c825cce2cbc
fetched_at: '2026-06-28T22:39:52.224321+00:00'
product: protheus
section_id: 1500001549382
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - O campoA2_LOJA
  refira à pasta:1, mas não existe. on FWFORMFIELD:PREPAREFIELDS(FWFORMFIELD.PRW)
type: support-article
updated_at: '2022-04-27T20:23:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056814774-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-O-campoA2-LOJA-refira-%C3%A0-pasta-1-mas-n%C3%A3o-existe-on-FWFORMFIELD-PREPAREFIELDS-FWFORMFIELD-PRW
---

**Ocorrência**Ao tentar incluir ou alterar um fabricante/fornecedor na rotina Fornecedores (**MATA020**) informa que o folder não existe do campo **A2\_COD**.  
  
**Causa**

```
O campo A2_LOJA refira à pasta:1, mas não existe. on FWFORMFIELD:PREPAREFIELDS(FWFORMFIELD.PRW) 05/03/2020 22:36:10 line : 408
```

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096440674/mceclip0.png)**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões  
  
**Solução**A tabela SX3 faz parte do dicionário de dados e é responsável pela estrutura e ordenação dos campos de uma tabela.  
Com isto, ao acessarmos a SX3 da tabela **SA2** campo **A2\_LOJA**e observarmos o campo **X3\_FOLDER**, o mesmo possui conteúdo 3. isto refere-se a pasta onde o campo será alocado para apresentação ao usuário em tela, ou seja, no cenário abaixo está sendo informado na SX3 a pasta 1 que refere-se a aba **Cadastrais** para o campo **A2\_LOJA**, mas esta pasta não existe pois não está sendo informada na tabela SXA que é responsável pela ordenação das pastas.  
Isto ocorre devido a falta de atualização do dicionário de dados do cliente e execução do **UPDDISTR**.  
  
SX3 do Campo filtrado na Tabela **SA2:**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098751153/mceclip1.png)**

Segue SXA filtrado na Tabela SA2:

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098751353/mceclip2.png)**

Ao acessar o cadastro de Fornecedores:  
- O erro informa que não existe a pasta 1 referente ao campo A2\_LOJA, pois no X3\_FOLDER foi informado que este campo se refere a pasta 1 mas se observarmos na tabela SXA que controla as pastas das rotinas do sistema, que só existem 8, sendo que o correto seria 9 pastas e a pasta "Cadastrais" onde fica o campo A2\_LOJA não esta criado no ambiente do cliente.  
  
**Para corrigir:**  
- Faça um *backup* da SXA e filtre a SA2 ao encontrar registros delete.

-Inclua um novo registro via APSDU com a descrição Cadastrais conforme print:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098752493/mceclip3.png)

Após a inclusão deste novo registro é só acessar a rotina de fornecedores que o erro não será mais exibido.
