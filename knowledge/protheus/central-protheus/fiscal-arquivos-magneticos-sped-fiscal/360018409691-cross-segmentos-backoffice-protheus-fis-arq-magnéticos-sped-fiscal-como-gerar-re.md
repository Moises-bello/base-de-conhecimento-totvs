---
article_id: 360018409691
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 89202d3cee260af9692aa5ec755b67e5ebc0768fc2e80933f61435a485d7c1a7
fetched_at: '2026-06-28T22:42:02.284568+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Como gerar registro 0200
type: support-article
updated_at: '2025-02-11T21:17:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018409691-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Como-gerar-registro-0200
---

**Dúvida**Como gerar o registro **0200** do **SPED FISCAL?**  
  
**Ambiente**Microsiga Protheus  - Livros Fiscais - A partir da versão 11.80

**Solução**Registro 0200: Tabela de identificação do Item (Produtos e Serviços)  
1. Verifique os principais campos de preenchimento abaixo marcados em vermelho. Caminho: **Módulos Compras ou Faturamento >>Atualizações >>Cadastros >> Produto**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013754571/mceclip0.png)

2. No Cadastro de produtos **(SB1)** preencha**:**

Descrição **(B1\_DESC)**Pos.IPI/NCM **(B1\_POSIPI)****Grupo de Estoque,** para produtos que são combustíveis, medicamentos, armas de fogo ou veículos automotores **(B1\_GRUPO)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013754611/mceclip1.png)

**Importante:**

a) A geração deste registro pode ser customizada a partir do **ponto de entrada SPEDPROD**. Neste ponto de entrada, podem-se alterar todos os campos do registro. Neste ponto são passados três parâmetros; a **variável cAliasSFT** que contém o filtro efetuado no**SFT**, de onde são lidas as informações do documento fiscal, **a cRegspd**que contém o nome do registro e a **cUnid** que contém o campo unidade de medida do produto.

b) Para este registro existe também o **ponto de entrada** **SPDFIS001**, que permite ao usuário relacionar novos tipos de produto com a tabela descrita no campo **TIPO\_ITEM**deste registro.

Para mais detalhes sobre este ponto de entrada, consulte o portal

TDN: [SPDFIS001 - Trata tipos de produtos](http://tdn.totvs.com/display/PROT/SPDFIS001+-+Trata+tipos+de+produtos)

c) Para o correto preenchimento do **campo 11 do registro 0200 - Tabela de Identificação do Item**verifique se a tabela de códigos utilizada no campo **Cód. ISS (B1\_CODISS)**é a tabela publicada no **Anexo I Lei Complementar Federal nº116/03**.Caso contrário relacione este código de ISS, utilizado no **SB1**, a um códigos publicados na **LC 116/03.**Isso é feito pela opção **Relac. Cód. ISS (MATA963),**disponível em **Atualização** -> **Cadastros.**
