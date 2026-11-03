---
article_id: 360013045611
category: Contabilidade Gerencial - Entidades
content_hash: d09756f72e1ac5d0ecb9c0ea9de53c3240a5af6ca4aa8e415af990970192dfae
fetched_at: '2026-06-28T22:40:49.797846+00:00'
product: protheus
section_id: 1500001537661
source: central-protheus
title: 'MP - SIGACTB - CTBA276/CTBA277: Cadastro de Grupo e Amarração dos Grupos'
type: support-article
updated_at: '2021-04-28T14:47:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013045611-MP-SIGACTB-CTBA276-CTBA277-Cadastro-de-Grupo-e-Amarra%C3%A7%C3%A3o-dos-Grupos
---

**Dúvida**Como criar **grupos de rateio** e **amarrá-los**?  
   
 **Ambiente**Microsiga Protheus - Contabilidade Gerencial - SIGACTB - Versões 11 e 12  
  
**Solução**Seguem abaixo, orientações para criação de **grupo de rateio** e a **amarração dos grupos**:

1. Criação de grupos de rateio (rotina ***CTBA276***)  
   Na criação de um **grupo**, no campo **Tipo**, defina se este será de **Origem** ou **Destino**;No campo **Entidade**, poderá selecionar se informará somente a ***conta contábil, centro de custos, item conta, classe de valor ou combinado***. Com esta última opção, o usuário poderá incluir um **grupo** informando mais de uma **entidade.**  
   É importante lembrar que neste processo, poderá incluir diversas sequências no cadastro**.** Porém, o **percentual das linhas** não pode ultrapassar 100% quando somados. **![Grupos.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360008969151/Grupos.jpg)**
2. Amarração dos grupos de rateio (rotina ***CTBA277***)  
   Para cadastrar uma **amarração** dos **grupos de rateio**, é necessário termos, ao menos, um ***grupo de origem*** e um de ***destino***;  
   Durante a criação desta amarração, na aba **Dados da Origem**, informe um grupo de origem cadastrado para o tipo de entidade correspondente (***conta contábil, centro de custos, item conta ou classe de valor***);  
   O mesmo processo pode ser aplicado na aba **Dados Contra Partida**;  
   Já na aba **Partida**, informe o código das entidades (***conta contábil, centro de custos, item conta ou classe de valor***) relacionadas a partida do lançamento rateado;  
   Caso preferir, nas abas **Dados Partida** e **Dados Contra Partida**, podem ser utilizadas fórmulas (função de usuário), onde terá a possibilidade de aplicar o tratamento desejado.  
     
   ![amarra_origem.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360008947612/amarra_origem.jpg)  
     
   ![Dados_Partida.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360008947952/Dados_Partida.jpg)  
     
   ![Dados_Destino.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360008948312/Dados_Destino.jpg)
