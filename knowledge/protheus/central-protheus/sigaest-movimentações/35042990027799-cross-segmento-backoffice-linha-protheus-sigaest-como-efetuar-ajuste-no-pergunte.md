---
article_id: 35042990027799
category: SIGAEST - MOVIMENTAÇÕES
content_hash: c2aacd4c7dd65bd43d3b9a24d5c17b3a2e388fa92ffb516db0d16bc77ba921c1
fetched_at: '2026-06-28T22:38:54.388257+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como efetuar ajuste
  no Pergunte A311TES para corrigir a gravação da TES na opção Replicar TES da MATA311
type: support-article
updated_at: '2025-09-19T10:52:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35042990027799-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-efetuar-ajuste-no-Pergunte-A311TES-para-corrigir-a-grava%C3%A7%C3%A3o-da-TES-na-op%C3%A7%C3%A3o-Replicar-TES-da-MATA311
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35042990016151) Tempo aproximado para leitura: 00**:01:00 min**  
  
**Dúvida**  
Estamos colocando a **TES** no campo **NNT\_TE**, sendo que a TES existe no cadastro.  
Porém, o sistema retorna que a TES não existe.  
Identificamos que pode ser o **fonte A311TESEV** que está retornando essa negativa.

Esse comportamento é esperado?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Atualmente o Pergunte A311TES possui a pergunta Filial Destino com tamanho 8, entretanto, em ambientes onde o tamanho do campo Filial seja diferente, não ocorre o preenchimento da TES de entrada e saída ao confirmar a interface.

Além disso, para o campo TES de Entrada, tanto a consulta padrão como a validação verificam somente a filial corrente, onde deveria considerar a filial destino informada na mesma tela. Caso a Filial Destino esteja em branco, será considerada a filial atual.

As correções a seguir estarão disponíveis na expedição contínua a partir de Jun/22, entretanto, é possível realizar o ajuste manualmente.

## **AJUSTE DE DICIONÁRIO**

**1º Passo - Tamanho do campo Filial:**

Tenha em mãos o tamanho do campo Filial configurado em sua empresa. Caso não saiba o tamanho, verifique o passo a passo abaixo. Caso saiba, pode avançar para o **2º Passo**:

Acesse o módulo SIGACFG. Navegue pelo menu: Base de Dados / Dicionário / Base de Dados. No menu lateral, selecione Dicionário de Dados

![](https://tdn.totvs.com/download/thumbnails/687151348/image2022-5-18_11-51-4.png?version=1&modificationDate=1652885701160&api=v2)

Selecione qualquer tabela, por exemplo, A00 e clique em visualizar

![](https://tdn.totvs.com/download/attachments/687151348/image2022-5-18_11-51-39.png?version=1&modificationDate=1652885700967&api=v2)

No menu lateral, selecione Campos

![](https://tdn.totvs.com/download/thumbnails/687151348/image2022-5-18_11-52-2.png?version=1&modificationDate=1652885700767&api=v2)

Localize o campo A00\_FILIAL e clique em Visualizar

![](https://tdn.totvs.com/download/attachments/687151348/image2022-5-18_11-53-16.png?version=1&modificationDate=1652885700420&api=v2)

Será apresentada as informações do tamanho do campo, entre elas, o tamanho. Anote este valor (No exemplo abaixo, o tamanho 8)

![](https://tdn.totvs.com/download/attachments/687151348/image2022-5-18_11-53-35.png?version=1&modificationDate=1652885700217&api=v2)

**2º Passo - Ajuste do Pergunte A311TES**

Acesse o módulo SIGACFG. Navegue pelo menu: Base de Dados / Dicionário / Base de Dados. No menu lateral, selecione Perguntas

![](https://tdn.totvs.com/download/thumbnails/687151348/image2022-5-18_11-57-37.png?version=1&modificationDate=1652885857367&api=v2)

Localize o grupo de perguntas A311TES e clique em editar

![](https://tdn.totvs.com/download/attachments/687151348/image2022-5-18_13-39-43.png?version=1&modificationDate=1652891983850&api=v2)

Na primeira linha, que consta Filial Destino, localize o campo Tamanho e edite, informando o tamanho da filial de sua empresa

![](https://tdn.totvs.com/download/thumbnails/687151348/image2022-5-18_13-41-3.png?version=1&modificationDate=1652892063707&api=v2)

Na terceira linha, que consta TES de Entrada, localize o campo Validação e insira a seguinte regra:

| Vazio() .Or.( A311TESEV() .And. MaAvalTes("E",MV\_PAR03)) |
| --- |

![](https://tdn.totvs.com/download/attachments/687151348/image2022-5-18_13-42-33.png?version=1&modificationDate=1652892153723&api=v2)

Ainda na terceira linha, localize o campo Consulta Padrão (Edit) e substitua a consulta por NNTSF4

![](https://tdn.totvs.com/download/attachments/687151348/image2022-5-18_13-43-10.png?version=1&modificationDate=1652892190147&api=v2)

Para mais informações acesse:

[Como efetuar ajuste no Pergunte A311TES para corrigir a gravação da TES na opção Replicar TES da MATA311](https://tdn.totvs.com/pages/releaseview.action?pageId=687151348)

**Saiba mais:**

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA310 / MATA311 - Como configurar a Transferência entre Filiais (MATA310 / MATA311) no Protheus?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418209855639-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Como-configurar-a-Transfer%C3%AAncia-entre-Filiais-MATA310-MATA311-no-Protheus-?source=search)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA310/MATA311 - Como definir o Preço de Venda do Pedido de Venda derivado do processo de Transferência entre Filiais ?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021390332-MP-SIGAEST-Custo-do-produto-derivado-do-processo-de-transfer%C3%AAncia-via-MATA311-)

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
