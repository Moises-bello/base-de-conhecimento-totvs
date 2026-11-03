---
article_id: 17290088552215
category: Materiais - Compras (SIGACOM)
content_hash: 237af284fe10a886b564d8d08184523d35999c0b6b6c1b15e7d9ec236e667c24
fetched_at: '2026-06-28T22:41:18.701653+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Gera Cotação - Replica
  de Fornecedores.
type: support-article
updated_at: '2023-09-05T16:42:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17290088552215-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Gera-Cota%C3%A7%C3%A3o-Replica-de-Fornecedores
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17290034803223) Tempo aproximado para leitura: **00:03:SS min** **Dúvida**Como configurar a Replica de fornecedores ao Gerar a Cotação ?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - VERSÃO 12  
  
**Solução**

A replica de fornecedores na geração de cotação vai depender da configuração do parâmetro MV\_SELFOR (Indica se comprador pode fazer seleção dos fornecedores).

**MV\_SELFOR** = " N" -  Quando o parâmetro estiver N - Não, sera considerado o pergunte "Replicar fornecedores - MV\_PAR14" para que seja efetuado o processo.

**MV\_SELFOR** = "S" - Quando habilitado o parâmetro o pergunte "Replicar fornecedores - MV\_PAR14" sera **ignorado**, pois quando é apresentada a tela de seleção dos fornecedores, existe a opção **"Replicar p/ Grupo"** ou **"Replicar p/ TODOS".**

* **Replicar p/Grupo:**Fornecedor(es) sera(ão) replicado(s) para todos os itens pertencentes ao GRUPO em que estiver posicionado na tela.
* **Replicar p/Todos:**Fornecedor(es) sera(ão) replicado(s) para todos os itens pertencentes a cotação.

**Saiba mais em :**

**[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)**
