---
content_hash: 982ac196b99b2081f065156d1801b8fc3bc8869e0924aaefdc7726bfc97d9049
fetched_at: '2026-06-29T00:08:09.095684+00:00'
page_id: '239024111'
product: rm
source: tdn-rm
title: Habilitar Esquema de Cores em Conexões Remotas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=239024111
version: 2
---

# Habilitar Esquema de Cores no RM, quando acessado através de conexões remotas

# 

|  |  |
| --- | --- |
| **Produto:** | Framework |
| **Versões:** | 11.XX; 12.1.XX |
| **Ocorrência:** | Habilitar esquema de cores no RM, quando acessado através de conexões remotas |
| **Ambiente:** | MDI |
| **Passo a passo:** | 1. Clique com o **botão direito** do mouse no ícone do **RM.exe** na sua área de trabalho.     **Imagem 1** – Botão direito do mouse acionado em cima do ícone do RM.     2. Clique em **Propriedades**. A tela abaixo será apresentada.    **Imagem 2** – Propriedades de RM.exe     3. Ao final do campo **Destino**, onde o caminho do **RM.exe** na máquina é apresentado, acrescentar [espaço + enableskin].  **EXEMPLO:** C:\totvs\CorporeRM\RM.Net\RM.exe enableskin  **Imagem 3 –** Adicionando [espaço + enableskin] ao final do campo Destino     4. Clique em **Aplicar**. |
| **Observações:** | **Essa configuração deve ser realizada para cada usuário do Windows.      Essa modificação poderá causar **queda de desempenho.**** |
