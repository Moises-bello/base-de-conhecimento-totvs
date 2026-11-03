---
article_id: 360020640371
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 71fa6cd8e8274d7337404f37a0bdbea6b79a60456890d411087b3a023bead0fc
fetched_at: '2026-06-28T22:42:04.962318+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Como gerar o
  registro 0200 do EFD Contribuições
type: support-article
updated_at: '2023-11-08T12:48:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020640371-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-o-registro-0200-do-EFD-Contribui%C3%A7%C3%B5es
---

**Dúvida**Como gerar o registro **0200** do **EFD Contribuições**?  
  
**Ambiente**Microsiga Protheus  - Livros Fiscais - A partir da versão 11.80  
  
**Solução**Para gerar o registro 0200 - Tabela de identificação do Item (Produtos e Serviços), observe as seguintes orientações:  
  
1. Verifique os principais campos de preenchimento abaixo marcados em vermelho; Caminho: **Módulos Compras ou Faturamento >>Atualizações >>Cadastros >> Produto (Tabela SB1)**:  
  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18911652281239)  
  
  
2. No Cadastro de produtos **(SB1)**,preencha**:**Descrição**(B1\_DESC)**Pos.IPI/NCM**(B1\_POSIPI)****Grupo de Estoque,**para produtos que são combustíveis, medicamentos, armas de fogo ou veículos automotores **(B1\_GRUPO)**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18911636427927)  
  
**Importante:**a) A geração deste registro pode ser customizada a partir do **ponto de entrada SPEDPROD**. Neste ponto de entrada, podem-se alterar todos os campos do registro. Neste ponto são passados três parâmetros; a **variável cAliasSFT** que contém o filtro efetuado no**SFT**, de onde são lidas as informações do documento fiscal, **a cRegspd**que contém o nome do registro e a **cUnid** que contém o campo unidade de medida do produto.  
  
b) Para este registro existe também o **ponto de entrada** **SPDFIS001**, que permite ao usuário relacionar novos tipos de produto com a tabela descrita no campo **TIPO\_ITEM**deste registro.  
  
Para mais detalhes sobre este ponto de entrada, consulte o portal TDN:   
**SPDFIS001:**  
<https://tdn.totvs.com/display/public/PROT/PE+-+SPDFIS001+-+Trata+tipos+de+produtos>  
  
**SPEDPROD:**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=706922410>

c) Para o correto preenchimento do **campo 11 do registro 0200 - Tabela de Identificação do Item**verifique se a tabela de códigos utilizada no campo **Cód. ISS (B1\_CODISS)**é a tabela publicada no **Anexo I Lei Complementar Federal nº116/03**.Caso contrário relacione este código de ISS, utilizado no **SB1**, a um códigos publicados na **LC 116/03.**Isso é feito pela opção **Relac. Cód. ISS (MATA963),**disponível em **Atualização**->**Cadastros.**
