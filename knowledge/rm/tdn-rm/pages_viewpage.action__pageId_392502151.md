---
content_hash: 86cd0b3ff68ad8b37c61a945f0b579a6d7a343a904fc4b792a6866c12ed2ac4e
fetched_at: '2026-06-29T00:09:09.163789+00:00'
page_id: '392502151'
product: rm
source: tdn-rm
title: 3646783 FOPROTINAS01-5465 DT - Erro ao solicitar antecipação da 1ª parcela
  do 13º ao marcar férias via MDI
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=392502151
version: 1
---

# AJUSTE DE ERRO DE ASSEMBLY NÃO ENCONTRADO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Recursos Humanos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Cadastro de Período de Gozo |
| **Situação/Requisito:** | Ao tentar cadastrar período de gozo para funcionário marcando o parâmetro "Pagar 1ª Parcela 13º" no cadastro de período de gozo, é apresentado o erro "Assembly não encontrado: RM.Fop.FuFerias.Data.dll" após clicar em "Salvar". |
| **Solução/Implementação:** | Foi feito ajuste para chamar a função correta para criar conexão com o server ao validar o pagamento da 1ª parcela do 13º, quando este for solicitado. Desse modo, o assembly "RM.Fop.FuFerias.Data.dll", que pertence à camada server, pode ser encontrado. |
| **Tickets relacionados:** | 3646783 |
