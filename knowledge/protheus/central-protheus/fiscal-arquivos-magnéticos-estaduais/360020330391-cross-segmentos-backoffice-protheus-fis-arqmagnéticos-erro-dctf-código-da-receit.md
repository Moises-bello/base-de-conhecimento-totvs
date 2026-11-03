---
article_id: 360020330391
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 7b39acb49f4e696a17c49924719aae535af89b862599c3665c96b6c01617c137
fetched_at: '2026-06-28T22:42:10.864594+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Erro DCTF "Código
  da Receita inválido"
type: support-article
updated_at: '2022-08-17T19:37:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020330391-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Erro-DCTF-C%C3%B3digo-da-Receita-inv%C3%A1lido
---

**Ocorrência**Ao validar o arquivo da **DCTF** é apresentado o seguinte erro de validação "Código da Receita não pertence ao Grupo de Tributo"   
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Causa**Esse incidente ocorre, pois o código do tributo não pertence ou não está atualizado de acordo com a tabela de código de Sistema da **Receita Federal**.   
  
O Sistema carrega esta informação para o arquivo de acordo com o campo **E2\_CODRET** da Tabela **SE2** (Contas a pagar).  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Consulte a Tabela atual de **Códigos da Receita Federal**, no próprio validador da **DCTF**;

2. Consulte o **Código da Receita** + **Variação** + **Periodicidade** que aceito pela **DCTF**;

![DCTF_c_digo.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360016075972/DCTF_c_digo.PNG)

A composição do conteúdo é WWWW=XXXXYYZ, em que:  
WWWW: Código de receita utilizado no sistema Protheus.  
XXXX: Código de receita na **DCTF** com a mesma característica do código do sistema.  
YY: Variação de acordo com a **DCTF**.  
Z: Periodicidade de acordo com o código da receita na **DCTF**. Deve ser informado:  
D: para periodicidade Diária;  
S: para periodicidade Semanal;  
X: para periodicidade Decendial;  
Q: para periodicidade Quinzenal;  
M: para periodicidade Mensal;  
B: para periodicidade Bimestral  
T: para periodicidade Trimestral;  
U: para periodicidade Quadrimestral;  
E: para periodicidade Semestral;  
A: para periodicidade Anual.  
  
3. Acesse o **Configurador** e informe o código no parâmetro **MV\_DCTF000**;  
Para separar grupos de relacionamento, utilize sempre o ponto e vírgula ( ; ). O ponto-e-vírgula é obrigatório sempre no final, como último carácter, mesmo quando houver apenas 1 item.  
Exemplo: **5952=595202Q**;

4. Dúvidas no preenchimento do Parâmetro? Consulte o link abaixo:

<https://tdn.totvs.com/pages/releaseview.action?pageId=655865674>
