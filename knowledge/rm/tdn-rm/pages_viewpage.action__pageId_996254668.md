---
content_hash: 0b02fd7648fb10cedf380c455119e5c82de837a82e2982722fed72dd74731730
fetched_at: '2026-06-29T00:12:16.645715+00:00'
page_id: '996254668'
product: rm
source: tdn-rm
title: Requisições Estoque Offline
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=996254668
version: 3
---

## **01. VISÃO GERAL**

Esse recurso está disponível na versão 12.1.2506 e superiores.

Essa funcionalidade consiste em permitir que uma requisição seja processada mesmo que a integração do estoque (EMS ou o Protheus) esteja offline (inativa).

Para que seja permitido, deve-se habilitar o parâmetro para indicar que a conexão (integração) esteja OFFLINE.

Ao processar uma requisição com o **Estoque OFFLINE**, o sistema realizará o lançamento na conta do paciente e  a liberação do aprazamento normalmente, marcará esta requisição como processada assim como seus itens.

É importante notar que não será alterado o saldo do produto enquanto o parâmetro de **Estoque OFFLINE** estiver ativo, Ao processar e confirmar os itens também não ocorrerá a validação do saldo.

Após as requisições serem processadas completamente, as que tiverem ao menos um item processado com estoque offline serão listas na grid **Apoio → Requisições Estoque Offline.** Importante ressaltar que,  para serem listadas no grid "Requisições Estoque Offline" as requisições não podem possuir itens pendentes de processamento.

Após desativar o parâmetro de **Estoque OFFLINE** é possível selecionar as requisições e processá-las, nesse momento o produto será movimentado e terá impacto em seu saldo.

O Estoque Offline afetará as requisições geradas na Movimentação de Estoques (exceto Devoluções), Painel de Dispensação e Painel de Cirurgias.
