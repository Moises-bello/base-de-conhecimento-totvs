---
article_id: 360029220131
category: Ferramentas
content_hash: 318ed70e6fb496997c7515e9187092a6b6f35ebf39331c103920470346324eb9
fetched_at: '2026-06-28T22:42:18.037931+00:00'
product: protheus
section_id: 360000075448
source: central-protheus
title: Framework - Linha Protheus - Incluir colunas no Browse
type: support-article
updated_at: '2024-05-09T11:12:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029220131-Framework-Linha-Protheus-Incluir-colunas-no-Browse
---

**Dúvida**  
Qual o procedimento para incluir uma nova coluna no Browse?  
  
**Ambiente**  
Protheus - SmartClient - A partir da versão 12  
  
**Solução**  
É possível incluir colunas do tipo Caracter, Numérico e Função. Os tipos Caracter e Numérico exibem apenas uma coluna com valor fixo. O tipo Função permite trazer outras informações, como registros de outra tabela por exemplo. Deve-se utilizar uma User Function compilada no RPO para efetuar este processo, conforme exemplo abaixo:  
  
**User Funcion compilada no RPO:**  
User function ColSCJ  
Return POSICIONE("SCJ", 1, xFilial("SCJ") + CJ\_NUM + CJ\_CLIENTE + CJ\_LOJA, "CJ\_NUM")  
  
**Incluir a coluna no Browse:**  
1. Na tela do Browse que deseja incluir a coluna, clique no botão em forma de engrenagem  
![2019-06-06_1050.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030369812)  
  
2. Clique em Incluir coluna  
  
3. Preencha os dados conforme exemplo abaixo:  
Título: Nome que aparecerá na coluna  
Dados: chamada da User Function criada  
Tipo: 3-Função  
Máscara: preencha se quiser uma máscara para os dados que serão exibidos  
Alinhamento: pode escolher o alinhamento do registro na coluna  
Imagem: indica se o campo é do tipo Imagem  
ID: define um identificador para esta coluna  
![CON_51.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030369892)
