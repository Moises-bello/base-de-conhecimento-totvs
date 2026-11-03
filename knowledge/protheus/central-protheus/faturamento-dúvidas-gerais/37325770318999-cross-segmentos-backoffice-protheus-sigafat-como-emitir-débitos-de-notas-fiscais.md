---
article_id: 37325770318999
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: b03fd1f5b9ce09ba9e9c69981cf884c0882cfa2e4e498f279f017356a25f6684
fetched_at: '2026-06-28T22:38:33.026186+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Como emitir débitos de notas
  fiscais não processadas na apuração (tpNFDebito = 03)
type: support-article
updated_at: '2025-12-29T20:11:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37325770318999-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-emitir-d%C3%A9bitos-de-notas-fiscais-n%C3%A3o-processadas-na-apura%C3%A7%C3%A3o-tpNFDebito-03
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37325739872407) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como emitir débitos de notas fiscais não processadas na apuração (**tpNFDebito = 03**)?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da versão 12.1.2210  
  
**Solução**  
A Nota Fiscal de débito do tipo “**Débitos de notas fiscais não processadas na apuração**” é um mecanismo de ajuste obrigatório para o Contribuinte (regime regular) garantir que todos os seus débitos de fornecimento (vendas) sejam devidamente processados na apuração. Ou seja, ao final de cada período de apuração, e após a disponibilização da prévia da apuração assistida, caberá ao contribuinte verificar a integridade das informações processadas, assegurando que todos os documentos fiscais de fornecimento tenham sido devidamente reconhecidos pelo sistema.

Se identificadas notas fiscais de fornecimento não processadas, o contribuinte deverá emitir uma nota fiscal de débito do tipo “03 – Débitos de Notas Fiscais Não Processadas na Apuração”, para garantir que o saldo final do período reflita corretamente o total de débitos devidos

**Importante:** Na Nota de Débito tipo 03 cada linha de item representa uma nota não processada na apuração, portanto cada linha terá obrigatoriamente uma nota referenciada.

**Processo**:

* Ao incluir o documento de débito deve ser informado no campo de tipo "**Tipo Compl.**" como “**3 - Débitos de notas fiscais não processadas na apuração**”;

(A numeração e série não são editáveis, pois serão geradas na confirmação.)

* Informe o **Cliente**e **Loja**, este deve ser o próprio emitente;
* Informe uma **Condição de Pagamento**(meramente informativa, pois não haverá geração de financeiro);
* Informe na grid:

  + **Produto**; Devidos as características Protheus para cálculos tributários e a forma com que a legislação define o processo de geração deste tipo de nota, o produto deve representar a totalidade da nota a ser referenciada.
  + **Quantidade** - Para este tipo de documento não deve ser informada quantidade.
* Informe o **Valor**. Será sobre este valor que haverá incidência do calculo de tributos;
* Informe uma **TES** que **não movimenta estoque** e **não gera financeiro**;
* Clique na opção **Vincular**;

  + Na parte superior, em **Filtros**, informe os dados para a busca do documento a ser referenciado nesta nota, ou seja, o documento de origem não processado;
  + Na seção **Itens**, serão listados os "produtos" informados no documento. A busca **não**será influenciada por estes, apenas pelos **Filtros**,esta seção deve ser usada para o relacionamento da linha com a nota referenciada.
  + Clique em **Buscar**. Serão listados até 300 linhas de itens de entrada de acordo com os filtros na seção **Resultado do filtro**
  + **Marque**o documento não processado na apuração. O registro marcado será listado na seção **Documentos Selecionados**;
  + Clique em **Confirmar**;
* Clique em **Confirmar**;
* Selecione a **Série**e **Numeração**para geração do documento.

**Saiba mais:**

* [Notas de Débito (NF-e: finNFe = 6 - NT 2025.002)](https://tdn.totvs.com/pages/viewpage.action?pageId=1013620273)
