---
article_id: 360022341592
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 3f623792de5e0dbc78e4c5208ebf912a5d4ff79e3c3e5ad51811a5a25e279a43
fetched_at: '2026-06-28T22:38:39.711991+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Como fazer uma devolução
  de compras
type: support-article
updated_at: '2026-02-11T20:46:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022341592-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-fazer-uma-devolu%C3%A7%C3%A3o-de-compras
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22766156230295) Tempo aproximado para leitura: 00:04:30 min**

**Dúvida**  
Como fazer uma devolução de compras?

**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT – Todas as versões.

**Solução**

A devolução de compras no Protheus pode ser realizada de duas formas principais, garantindo a integridade fiscal e o vínculo com o documento de origem.

#### **Maneira 1: Manualmente pelo Pedido de Venda (MATA410)**

1. Acesse Atualizações > Pedidos > Pedidos de Venda.
2. Inclua um novo pedido e informe o campo Tipo (C5\_TIPO) = `D - Devolução de Compras`.
3. Preencha o Produto (C6\_PRODUTO), a TES (C6\_TES) (deve ser uma TES de saída que não controla poder de terceiros) e o Fornecedor/Loja idênticos à nota de entrada.
4. No campo N.F.Original (C6\_NFORI), pressione F4 para listar as notas de entrada disponíveis.
5. Selecione a nota desejada. O sistema carregará os itens e o valor unitário original (D1\_VUNIT).

#### **Maneira 2: Facilitador via Botão "Retornar"**

1. Em Pedidos de Venda, vá em Outras Ações > ReTornar.
2. Selecione o parâmetro Fornecedor, informe o código/loja e o intervalo de datas.
3. Na tela seguinte, marque a nota de entrada que deseja devolver e clique em Retorno. O pedido será gerado automaticamente com todos os vínculos.
4. TES de Devolução: É recomendado que a TES de entrada tenha o campo TES Devolução (F4\_TESDV) preenchido com o código da TES de saída correspondente para funcionar a opção retornar.

**Observação 1:**

* **Filtro de Loja/Fornecedor (F12):** Em operações de Beneficiamento, se ao pressionar F4 na quantidade do produto e o sistema trouxer notas de lojas diferentes da informada no cabeçalho, verifique os parâmetros da rotina (tecla F12). Se a opção "Op. Triangular ?" estiver como SIM, o sistema permitirá selecionar notas de outras lojas do mesmo fornecedor (comum em processos triangulares). Para restringir apenas à loja do cabeçalho, mantenha como NÃO.

**Observação 2:**

* Vínculo Fiscal: Para que a nota seja transmitida corretamente, a nota de origem deve ser do tipo "Normal", e o campo Nf. Original (C6\_NFORI) deve estar preenchido.

**Observação 3:**

* É possível realizar a devolução pela rotina "Nota fiscal manual de saída" (MATA920): Onde é feito manualmente o documento de saída sem pedido de venda.

  Em alguns casos a rotina Nota Fiscal Manual de Saída (MATA920) também pode ser utilizada para devolução de compras emitidas pelo fornecedor.

Assista nosso vídeo How To com o passo a passo detalhado:

**Saiba mais:**

* [Realizar uma Devolução de Compras](https://tdn.totvs.com/x/g0FtDQ)
* [Nota de Entrada não Aparece para Devolução](https://youtu.be/0GNdJIr-Ibs?si=cfODXuxkY3lkuiqm)
* [Cross Segmentos - Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Devolução de Compras emitida pelo fornecedor](https://centraldeatendimento.totvs.com/hc/pt-br/articles/24243183314711-Cross-Segmentos-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Devolu%C3%A7%C3%A3o-de-Compras-emitida-pelo-fornecedor)
