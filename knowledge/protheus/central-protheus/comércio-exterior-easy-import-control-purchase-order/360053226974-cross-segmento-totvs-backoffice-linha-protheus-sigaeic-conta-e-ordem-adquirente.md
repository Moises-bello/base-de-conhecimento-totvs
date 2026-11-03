---
article_id: 360053226974
category: Comércio Exterior - Easy Import Control - Purchase - Order
content_hash: c0df3de7e29560a86b06bdfe2f67ee8cf0d6714fcce349d7e8dcf0790d8334c1
fetched_at: '2026-06-28T22:39:41.123337+00:00'
product: protheus
section_id: 1500001538481
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Conta e Ordem
  Adquirente
type: support-article
updated_at: '2023-11-07T14:20:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053226974-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Conta-e-Ordem-Adquirente
---

**Dúvida**Como incluir o processo de conta e ordem por Adquirente?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**

Pré-Requisitos:

* É necessário habilitar os parâmetros com os seguintes conteúdos: MV\_PCOIMPO = F , MV\_PCOFOB = F , MV\_EIC\_PCO = T e MV\_EASY = S.
* Possuir um Solicitação de Importação cadastrada.

**Sequência 001:**

1. No Easy Import Control (SIGAEIC) acesse Atualizações/ Purchase Order/ Manutenção (EICPO400).
2. Clique em Incluir.
3. Preencha os campos obrigatórios. Na pasta Cadastrais informe a opção SIM no campo Import. C.O.? (W2\_IMPCO) e clique em Confirmar.
4. Na tela de Seleção de SI, informe a unidade requisitante e a SI cadastrada anteriormente. Clique em Confirmar.
5. Na tela de Seleção de Itens, selecione o item e clique em Confirmar. Clique em Confirmar novamente.
6. É apresentada a mensagem Confirma a gravação?. Clique em SIM.
7. É apresentado a mensagem informando que foi gerado o pedido. Clique em OK.

**Sequência 002:**

1. No Compras (SIGACOM) acesse Atualizações/ Pedidos/ Pedido de Compras (MATA121).
2. Visualize o pedido gerado.

**Sequencia 003:**

1. No Easy Import Control (SIGAEIC) acesse Atualizações/ Desembaraço/ Manutenção (EICDI502).
2. Clique em Incluir, preencha os campos obrigatórios.
3. Na pasta Cadastrais, o campo Import. C.O.? (W6\_IMPCO) esta preenchido.
4. Na pasta Outros, preencha os campos Tipo Consig.(W6\_PRO\_IMP) e CNPJ Consig.(W6\_CGC\_OUT).
5. Clique em Ações Relacionadas e clique em Itens. Dê um duplo clique no item e marque o mesmo.
6. Clique em Ações Relacionadas e clique em Invoice e clique em Incluir. Preencha os campos obrigatórios e vincule o item. Clique em Confirmar.
7. Clique em Ações Relacionadas e em Adições.
8. Clique em Ações Relacionadas novamente e clique em Gera. Confirme.
9. Clique em Confirmar na tela de Conferência Final é apresentada a mensagem: Confirma a Gravação?. Clique em SIM.

**Seqüência 004:**

1. No módulo Easy Import Control (SIGAEIC), acesse Atualizações / Desembaraço / NF Transferência (EICCO100).
2. Selecione o processo em análise e em seguida clique no botão Valores NFT.
3. Serão exibidos os valores correspondentes às despesas do processo e os itens que compõe o Embarque/Desembaraço. Clique em Des/Marca Todas Despesas e em seguida Des/Marca Todos Itens.
4. Clique em Digitação No. NFT Itens para informar o número da Nota Fiscal correspondente aos itens exibidos. Confirme. O número da Nota Fiscal e Série serão inseridos na capa do processo.
5. Clique em Gerar NFT.
6. Clique em Sim na seguinte mensagem exibida: Confirma Gravação dos Valores e Geração da NFT?.
7. É apresentada a mensagem Geração da Nota Fiscal Concluida. Clique em OK para gravar a geração da nota.

**Sequência 005:**

1. No módulo Easy Import Control (SIGAEIC), acesse Atualizações / Desembaraço / NF Transferência (EICCO100).
2. Posicione no processo desejado e clique na opção Ações Relacionadas e clique em Impressão val.
3. Clique na opção *Preview*.
4. Visualize a impressão do relatório.

Sequência 006:

1. No módulo Compras (SIGACOM), acesse Atualizações/ Movimentos/ Documento Entrada (MATA103).
2. Posicione no processo desejado e clique na opção Classificar. Observe que os campos Número e Série estão preenchidos.
3. Preencha os campos Tipo Entrada e Cod. Fiscal.
4. Clique em Confirmar para salvar.

**Saiba mais:**

[Conta e Ordem para Cliente Adquirente](https://tdn.totvs.com/display/public/mp/Conta+e+Ordem+para+Cliente+Adquirente+--+115792)

[Conta e Ordem para Cliente Adquirente (EICCO100)](https://tdn.totvs.com/pages/releaseview.action?pageId=397378615)
