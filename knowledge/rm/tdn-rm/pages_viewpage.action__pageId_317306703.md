---
content_hash: 88d025c3f64629eaa8c139f376b0f2c0a6a68b6f56f020d2922d9ca86181fd5f
fetched_at: '2026-06-29T00:08:46.610124+00:00'
page_id: '317306703'
product: rm
source: tdn-rm
title: 1173827 MATFATCMPCRM01-1065 DT "Copiar Mensagem cadastrada na Natureza para
  o Histórico" e "Copiar Mensagens informadas no Movimento para o Histórico".
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=317306703
version: 2
---

# Processo de "Copiar Mensagem cadastrada na Natureza para o Histórico" e "Copiar Mensagens informadas no Movimento para o Histórico".

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção & Projetos. |
| **Módulo:** | **Totvs Gestão de Estoque Compras e Faturamento** |
| **Função:** | "Copiar Mensagem cadastrada na Natureza para o Histórico" e "Copiar Mensagens informadas no Movimento para o Histórico". |
| **Situação/Requisito:** | **Copiar Mensagem cadastrada na Natureza para o Histórico:** Copiar Mensagem cadastrada na Natureza para o Histórico sem que seja necessário preencher nos campos de Mensagens do Movimento.  **Copiar Mensagens informadas no Movimento para o Histórico:** Copiar todas as mensagens informadas nos Lookups de mensagem do movimento para o Histórico. |
| **Solução/Implementação:** | **Copiar Mensagem cadastrada na Natureza para o Histórico:**  Foi alterado o comportamento do botão "Copiar Mensagem Cadastrada na Natureza" para que se os parâmetros "Vincular Mensagens de Natureza ao Movimento" localizado em [Parâmetros | 04.03 - Integrações | 04.03.03 - Fiscal | 04.03.03.01 - Dados Ficais] e parâmetro do tipo de movimento "Usar Mensagens Definidas na Natureza" localizado em [Parâmetros do tipo de movimento | Etapa 62 - Fiscal - Dados Fiscais] estiverem marcados, o botão será habilitado na tela de "Observação" do movimento e quando acionado as mensagens cadastradas no anexo da natureza informada no movimento serão copiadas para o histórico independente dos Lookup de Mensagens do movimento estarem habilitados.  **Copiar Mensagens informadas no Movimento para o Histórico:**  Foi criado o botão "Copiar Mensagens Informadas no movimento para o Histórico".  Este botão será habilitado se alguma das mensagens do tipo de movimento (Mov - Valores Financeiros 1/4 "Frete, Despesa e Desconto" e Mov - Campos Livres 1/2 "Mensagem1 e Mensagem2") estiverem diferente de "Não Edita".  **Funcionalidade:** Copiar as mensagens informadas nos Lookups de mensagem do movimento para o histórico.  **Defaults:**  Por regra, se o parâmetro do tipo de movimento "Usar Mensagens Definidas na Natureza" e os Lookups de mensagem do movimento estivem habilitados, ao criar um novo movimento, todas as mensagens cadastradas no anexo da natureza serão carregadas com default para que sejam copiadas.  Se o parâmetro do tipo de movimento "Usar Mensagens Definidas na Natureza" estiver desabilitado e os Lookups de mensagem do movimento estivem habilitados, serão carregadas com default, as mensagens informadas nos parâmetros do tipo de movimento. |
| **Conversores e Parâmetros:** | Informe os conversores/parâmetros. |
| **Tickets relacionados:** | 1173827 |
| **Requisito:** | NA. |
| **Modelo:** |  |
