---
content_hash: 3714ddebb1d7b43bbf9f4a30dc04e87c49431860d56ab888661bbab1642e3987
fetched_at: '2026-06-29T00:09:36.829522+00:00'
page_id: '425459529'
product: rm
source: tdn-rm
title: Backoffice RM x Protheus SigaMNT- Cancelar Ordem de Serviço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459529
version: 3
---

**Backoffice RM x Protheus SigaMNT- Cancelar Ordem de Serviço**

---

Através desta funcionalidade é possível efetuar o cancelamento das Ordens de Serviço no Protheus SigaMNT, efetuando um filtro de busca inicialmente através de seus parâmetros. Após o cancelamento da Ordem de serviço é enviada uma mensagem ao Backoffice RM cancelando a respectiva Ordem de manutenção. No final da execução do processo é apresentada uma mensagem informando o número de O.S. canceladas.

**Pré-condições**

**1:** Criar uma Ordem de Serviço

**Executando o Processo:**

**Passo 1:** Acesse: Protheus SigaMNT / Atualizações/Ordem de Serviço/Cancelamento O.S.

**Passo 2:** Informe os filtros de Ordem de Serviço conforme desejado e clique em Gerar Consulta.

**Passo 3:** Selecione as Ordens de Serviço conforme desejado e clique em Cancelar.

**Passo 4:** Informe o motivo do cancelamento.

**Passo 5:** O Protheus SigaMNT finaliza a Ordem de Serviço e envia uma mensagem ao Backoffice RM cancelando o Movimento de Ordem de Manutenção.

**Passo 6:** Acesse : RM / Backoffice / Gestão de Estoque, Compras e Faturamento / Outras Movimentações.

**Passo 7:** Informe o código do Tipo de Movimento criado para Ordem de Manutenção e a Filial.

**Passo 8:** Verificar que o Movimento de Ordem de Manutenção criado pela Ordem de serviço no Protheus SigaMNT é exibida com o Status "Cancelada".

**Observações:**

* Se a Ordem de Manutenção tiver sido Faturada no Backoffice RM , não deve ser permitido o cancelamento da Ordem de Serviço através do Protheus SigaMNT.
* Se  a Solicitação de Armazém (SA) gerada a partir da Ordem de serviço tiver em status diferente de "Pendente" no Backoffice RM , não deve ser permitido o cancelamento da Ordem de Serviço através do Protheus SigaMNT.
* Se o tipo de movimento de Solicitação de Armazém (SA) estiver parametrizado com a opção "Baixar para Movimento Default" (Etapa Compra/Venda - Outras Características) e a SA for recebida/faturada para um tipo de movimento que não estiver definido no parâmetro "Movimento Gerado (Default)", ao cancelar uma Solicitação de Armazém (a partir do processo de Cancelar Ordem de Serviço no SigaMNT) é consistido a existência de relacionamento entre a SA e o movimento gerado. Desta maneira não é permitido realizar o cancelamento da SA e da Ordem de Serviço, mesmo que o status da SA esteja como "Pendente".
