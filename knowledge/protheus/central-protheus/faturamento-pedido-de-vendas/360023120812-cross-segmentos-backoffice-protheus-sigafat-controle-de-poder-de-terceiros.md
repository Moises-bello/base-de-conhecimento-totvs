---
article_id: 360023120812
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 049942b74d41df0e41a7db6f5acd672723adc744d923f87be7da4cf109c82fd2
fetched_at: '2026-06-28T22:38:39.759015+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Controle de Poder de Terceiros
type: support-article
updated_at: '2026-02-11T20:45:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023120812-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Controle-de-Poder-de-Terceiros
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38337608497943)Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**  
Como é efetuado o Controle de Poder de Terceiros?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões.  
  
**Solução**

**I) Beneficiamento ou recebimento de material de cliente**

* **Entrada**

1) A entrada deve ser efetuada pelo **MATA103** (**Documento de Entrada**).

2) O Tipo da Nota Fiscal deve ser **"B - Beneficiamento"**, pois é obrigatório a informação do Cliente.

3) A pergunta "Poder Terc." (**F4\_PODER3**) deve estar preenchida como "R" ( Remessa ).

* **Saída**

1) A saída deve ser efetuada pelo **MATA410** (**Pedido de Venda**).

2) O Tipo do Pedido deve ser **"N - Normal"**, pois é obrigatório a informação do Cliente.

3) A Pergunta "Poder Terc." (**F4\_PODER3**) deve estar preenchida como "D" ( **Devoluçao** ).

4) Pressionar F4 na quantidade para selecionar a nota original.

**II) Recebimento de Material de fornecedor**

* **Entrada**

1) A entrada deve ser efetuada pelo **MATA103** (**Documento de Entrada**).

2) O Tipo da Nota Fiscal deve ser **"N - Normal"**, pois e obrigatório a informação do fornecedor.

3) A pergunta "Poder Terc." (**F4\_PODER3**) deve estar preenchida como "R" ( **Remessa** ).

* **Saída**

1) A saída deve ser efetuada pelo **MATA410** (**Pedido de Venda**).

2) O Tipo do Pedido deve ser **"B - Beneficiamento"**, pois eh obrigatório a informação do fornecedor.

3) A Pergunta "Poder Terc." (**F4\_PODER3**) deve estar preenchida como "D" ( **Devolução** ).

4) Utilizar F4 na quantidade para selecionar a nota original

**Observação:**

Se ao tentar selecionar a Nota de Origem, o sistema listar notas de lojas diferentes da informada no pedido:

1. No MATA410 (Pedido de Venda), antes de selecionar a nota, pressione a tecla F12.
2. Localize o parâmetro Operação Triangular?.

   * Se SIM: O sistema permite selecionar notas de qualquer loja do mesmo fornecedor/cliente (comportamento nativo para operações triangulares).
   * Se NÃO: O sistema restringe a busca apenas para a loja e código informados no cabeçalho do pedido.

**Saiba mais:**

[FAT0285 - Poder DE/EM Terceiro](https://tdn.totvs.com/x/xyCgGg)
