---
article_id: 360010377811
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: a057fb71e2b19e57a950cc20a9c16e91311393f31481124c6e7f3379631a7554
fetched_at: '2026-06-28T22:42:02.386133+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - REGISTRO 0300 E 0305
type: support-article
updated_at: '2025-02-11T21:25:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010377811-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-REGISTRO-0300-E-0305
---

**Dúvida**  
Como gerar o registro 0300 e 0305 - Cadastros de Bens ou Componentes do Ativo Imobilizado.  
  
**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80.  
  
**Solução**Para solucionar a dúvida acima, verifique as orientações:  
  
1. Se no cadastro de **Manutenção CIAP** “**MATA905**” (**Tabela SF9**) o campo **F9\_ROTINA** =  MATA103:- O item da nota virá do campo **FT\_ITEM**;  
- O modelo da Nota Fiscal dos campos **F1/F3/FT\_ESPECIE**;  
- O produto do campo **FT\_PRODUTO**.  
  
2. Se no cadastro de **Manutenção CIAP** “**MATA905**” (**Tabela SF9**) o campo **F9\_ROTINA** = MATA905:  
 - O item da nota deve ser informado no campo criado na **tabela SF9**, vincule o campo criado ao parâmetro **MV\_F9ITEM,**Exemplo: **MV\_F9ITEM** = **F9\_ITEMNFE**;  
 - A espécie da nota deve ser informada no campo criado na **tabela SF9**, vincule o campo criado ao parâmetro **MV\_F9ESP,**Exemplo: **MV\_F9ESP** = **F9\_ESPEC**; - O produto deve ser informado no campo criado na **tabela SF9**, vincule o campo criado ao parâmetro **MV\_F9PROD**. Exemplo: **MV\_F9PROD** = **F9\_PROD**.  
  
3. Campo **02\_COD\_CCUS** do **SPED FISCAL**:  
 - Se no cadastro de **Manutenção CIAP** “**MATA905**” (SF9) o campo **F9\_ROTINA** = MATA103, o campo **02\_COD\_CCUS** do registro 0305 será considerado do campo Centro de Custo **B1\_CC** do cadastro do produto Tabela SB1;  
 - Se no cadastro de **Manutenção CIAP** “**MATA905**” (SF9) o campo **F9\_ROTINA** = MATA905 o campo **02\_COD\_CCUS** do registro 0305 será considerado o campo **F9\_CC** o campo deve ser criado manualmente, preencha o mesmo com a informação da **Tabela CTT** no campo **C Custo**  (**CTT\_CUSTO**) e vincular ao parâmetro **MV\_F9CC**, Exemplo: **MV\_F9CC** = **F9\_CC**

Configuração para criar o campo:  
Campo: F9\_CC  
Tipo: Caracter  
Tamanho: 9  
Decimal: 0  
Formato: @!  
Contexto: Real  
Titulo: C. Custo     
Texto: Informa centro de custo  
Help: Informação do centro de custo para preenchimento do campo 02 COD\_CCUS registro 0305 SPED FISCAL.  
  
4. Campo **03\_FUNC do SPED FISCAL**:

- Deve ser preenchido o campo Função Bem (**F9\_FUNCIT**) da **tabela SF9** rotina **Manutenção CIAP** “**MATA905**”.  
  
![kcs1.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360013001192/kcs1.JPG)  
  
5. Campo **04\_VIDA\_UTIL do SPED FISCAL**:  
 - Deverá ser preenchido o campo **Vida Ultil** (**F9\_VIDUTIL**) da **tabela SF9** rotina **Manutenção CIAP** “**MATA905**”.  
  
![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-3%2022%3A6%3A9.png?version=1&modificationDate=1464998419000&api=v2)
