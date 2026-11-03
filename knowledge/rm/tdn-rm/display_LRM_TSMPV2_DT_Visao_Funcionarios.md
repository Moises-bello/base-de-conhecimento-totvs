---
content_hash: 4ffa25da66f5af439c612da1f20ada4f256e97e13fa4584f34b1745f5fa74640
fetched_at: '2026-06-29T00:06:02.068875+00:00'
page_id: '198943070'
product: rm
source: tdn-rm
title: TSMPV2_DT_Visao_Funcionarios
type: documentation
url: https://tdn.totvs.com/display/LRM/TSMPV2_DT_Visao_Funcionarios
version: 2
---

# VISÃO DE FUNCIONÁRIOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Visão de Funcionários* |
| **Situação/Requisito:** | Ao abrir a visão de funcionários pelo Folha de Pagamento, e em seguida alterar o contexto para outro sistema (ex: Gestão de Pessoas), deixando a visão de funcionários aberta, ao editar qualquer funcionário dessa visão o link de Anotações Pessoais não é exibido. |
| **Solução/Implementação:** | Foi alterada a action de Funcionários para guardar o código do sistema que originalmente abriu a action. |
| **Chamados relacionados:** | *TSMPV2* |
| **Versões/Release:** | *12.1.7* |
