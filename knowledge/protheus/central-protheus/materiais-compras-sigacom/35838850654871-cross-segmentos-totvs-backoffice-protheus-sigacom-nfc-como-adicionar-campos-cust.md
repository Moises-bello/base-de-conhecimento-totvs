---
article_id: 35838850654871
category: Materiais - Compras (SIGACOM)
content_hash: 98ec6a8e54b85394471643b345d83ee0725fca73731ca714d95a1ce09fb79d5d
fetched_at: '2026-06-28T22:41:20.283406+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Como adicionar
  campos customizados nas telas e no formulário do Novo Fluxo de Compras?
type: support-article
updated_at: '2025-11-18T13:21:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35838850654871-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-Como-adicionar-campos-customizados-nas-telas-e-no-formul%C3%A1rio-do-Novo-Fluxo-de-Compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35838913913751) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Existe alguma possibilidade de adicionar Campos Customizados nas telas do Novo Fluxo de Compras? É possível adicionar campo customizado no HTML da cotação? Tem como adicionar campos customizados no formulário de preenchimento da cotação que é enviado ao email do fornecedor? Como exibir novos campos no e-mail do workflow que é enviado para o fornecedor?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - a partir da Release 12.1.2210  
  
**Solução**  
No Novo Fluxo de Compras temos várias telas, segue algumas delas: tela de Necessidade de Compra que lista as Solicitações, tela de Seleção dos fornecedores da cotação, tela de Envio do Workflow ao fornecedor, tela de Cotações, tela de visualização e edição das Propostas da cotação, telas de análise das cotações e formulário HTML que é enviado aos fornecedores.

Por padrão, a **única tela** que consegue carregar campos customizados é a **tela de Edição Manual da cotação** **na linha dos itens**. Na linha do item, campos customizados da tabela SC8 são apresentados e podem ser preenchidos. Para maiores informações consulte a documentação abaixo.

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Novo Fluxo de Compras - Como utilizar Campos Customizados - NFC (PGCA010)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19971094312599-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Novo-Fluxo-de-Compras-Como-utilizar-Campos-Customizados-NFC-PGCA010)

Nas outras telas Novo Fluxo de Compra **não é possível adicionar campos customizados**. Além disso, não existe nenhuma possibilidade de adicionar campos no formulário do NFC que é disparado ao e-mail do fornecedor. Seja campo customizado ou padrão, não é possível exibir mais campos. Também não é possível alterar a ordem dos campos do formulário.

**Atenção**

No mês de Dezembro, está prevista uma melhoria para que seja possível adicionar campos ao workflow do Novo Fluxo de Compras. Desse modo, será possível adicionar campos referente o Percentual dos Impostos.

**Obs1.** Não existe no formulário HTML padrão nenhuma forma de adicionar a imagem de logo da empresa.

**Obs2.** No Novo Fluxo de Compras, não é possível utilizar gatilhos customizados nos campos. Isso ocorre devido a limitação da tecnologia utilizada no desenvolvimento da rotina (POUI).

***Saiba Mais:***

[Novo Fluxo de Compras: Guia de Referência](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680260500)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
