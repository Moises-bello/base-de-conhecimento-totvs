---
content_hash: b32fa86b8b7ea095384e3f27f0fe546f489bb76c0c1cbb10bd95c3db839e1ed2
fetched_at: '2026-06-29T00:10:56.870663+00:00'
page_id: '593259892'
product: rm
source: tdn-rm
title: Substituição de Chefes e Supervisores
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=593259892
version: 10
---

## Objetivo

Este processo permite definir um ou vários substitutos para um chefe ou supervisor atual, informando a data de término da chefia e a data de término da chefia do substituto. O sistema substituirá automaticamente o chefe/supervisor pelos seus substitutos nas seções e equipes definidas.

---

### 1. Primeira etapa

* Selecione o chefe/supervisor a ser substituído.
* Informe a data em que a substituição será realizada.
* Selecione os papéis que serão substituídos.

### 2. Segunda etapa

* Escolha o substituto do chefe/supervisor definido na etapa anterior.
* Informe o período de substituição.

### 3. Terceira etapa – Seções

* O sistema apresenta as seções onde a substituição ocorrerá.
* É possível alterar o substituto para cada seção individualmente:

  + Selecione a seção desejada e clique em **Alterar Substituto**.
  + Na nova tela, preencha:

    - Data término do chefe/supervisor atual (definida na primeira etapa)
    - Novo chefe/supervisor (substituto)
    - Período de chefia do novo chefe/supervisor
  + Clique em **Definir Substituto** para confirmar a alteração.
* Caso o chefe/supervisor atue em mais de uma seção e queira alterar apenas algumas:

  + Selecione a(s) seção(ões) que **não deseja alterar** e clique em **Remover Substituto**.
  + Exemplo: Se o funcionário é chefe nas seções 01 e 02, e a substituição só deve ocorrer na seção 02, remova o substituto da seção 01. O sistema aplicará a substituição somente na seção 02.

### 4. Quarta etapa – Equipes

* O sistema apresenta as equipes onde ocorrerá a substituição.
* É possível alterar o substituto para cada equipe individualmente:

  + Selecione a equipe desejada e clique em **Alterar Substituto**.
  + Preencha os dados:

    - Data término do chefe/supervisor atual
    - Novo chefe/supervisor (substituto)
    - Período de chefia do novo chefe/supervisor
  + Clique em **Definir Substituto** para confirmar.
* Para alterações específicas em equipes:

  + Selecione as equipes que **não deseja alterar** e clique em **Remover Substituto**.
  + Exemplo: Se o funcionário é chefe nas equipes 01 e 02, e a substituição deve ocorrer apenas na equipe 02, remova o substituto da equipe 01. A substituição será aplicada somente na equipe 02.

---

falseObservações Importantes

💡Na rotina de substituição, o chefe deve ser substituído por outro chefe ou por uma pessoa que **não tenha cadastro como supervisor**, pois:

* O cadastro de chefe verifica o cadastro de seção do subordinado.
* O cadastro de supervisor verifica o código da equipe do subordinado.

Esses são comportamentos distintos que devem ser respeitados.

💡No portal RM, a visualização de funcionários subordinados nos menus *'Subordinados'* e *'Gestão de Férias'* **não estará disponível** para os gestores cuja **data de início de vínculo** seja **posterior** ao período da competência atual."

---

## Informações adicionais

* Disponível a partir das versões:

  + 12.1.2410.297
  + 12.1.2502.202
  + 12.1.2506.146  
    *(Necessário executar o RM.Atualizador para atualização dos scripts)*
* Quando a base estiver integrada com o **RM x Feedz**, ao cadastrar um substituto, o registro será criado com a flag **"Chefe/Supervisor Substituto"** ativada no cadastro de chefes e supervisores.

Para mais informações sobre o uso deste campo, consulte a documentação [**da Integração RM x Feedz.**](https://tdn.totvs.com/pages/releaseview.action?pageId=785614408#1-1)
