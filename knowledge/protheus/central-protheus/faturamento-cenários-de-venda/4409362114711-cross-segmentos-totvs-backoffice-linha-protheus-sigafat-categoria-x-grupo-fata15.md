---
article_id: 4409362114711
category: Faturamento - Cenários de Venda
content_hash: 403f2f3b3fabce4b2f6a5e2682cfe3661c484a8e3d8adf5b7f693305f025c29c
fetched_at: '2026-06-28T22:38:34.059712+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Categoria x
  Grupo (FATA150) por Grade não salva
type: support-article
updated_at: '2021-09-24T15:01:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409362114711-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Categoria-x-Grupo-FATA150-por-Grade-n%C3%A3o-salva
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao acessar a rotina Amarração de **Categoria x Grupo (FATA150)** no Tipo de Interface "**Por Grade**", ao preencher os campos, na inclusão de um novo registro, o sistema não permite salvar o registro.  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Todas as versões  
  
**Causa**Esse incidente ocorre porque ao preencher o campo "**Ref Grad Cfg**" (**ACV\_REFGRD**) não é necessário preencher o campo "**Desc. Ref Gr**" (**ACV\_DESREF**), o sistema preencherá a descrição da grade automaticamente após salvar o registro.

Caso o campo "**Desc. Ref Gr**" (**ACV\_DESREF**) seja preenchido, o sistema identifica que há um erro e não realiza a gravação do registro.  
  
**Solução**Para solucionar este incidente, basta configurar o campo "**Desc. Ref Gr**" (**ACV\_DESREF**) para que o mesmo seja apenas visual, evitando que o usuário realize o preenchimento dele, para isso:

1. Acesse o Configurador do Sistema (SIGACFG);

2. Acesse as opções "Base de Dados", "Dicionário" e "Bases de Dados";

3. Selecione a opção "Dicionário de Dados" e localize a tabela "ACV";

4. Altere a tabela e localize o campo "Desc. Ref Gr" (ACV\_DESREF);

5. Altere o campo e informe a "Propriedade" dele como "Visualizar":

![ACV_DESREF.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4409367206679/ACV_DESREF.jpg)

6. Salve as alterações e atualize a Base de Dados;

Ao acessar a rotina, o campo "**Desc. Ref Gr**" (**ACV\_DESREF**) não poderá mais ser preenchido, mas será preenchido automaticamente pelo sistema ao preencher o campo "**Ref Grad Cfg**" (**ACV\_REFGRD**) e salvar o registro.
