---
content_hash: 349f70bd56b1ab81fef463ed6ccd2e9f8ae941e4dadbbda5624cac234314560a
fetched_at: '2026-06-29T00:09:11.699643+00:00'
page_id: '415701763'
product: rm
source: tdn-rm
title: 3797094 FISCAL01-6548 DT Nota Fiscal de Serviço - Migração para Layout Único
  do TSS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=415701763
version: 1
---

# Nota Fiscal Eletrônica de Serviço

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Notas Fiscal Eletrônica de Serviço |
| **Situação/Requisito:** | Migração do processo da NFS-e para o layout único do TSS |
| **Solução/Implementação:** | Todos os municípios passaram a utilizar o layout único do TSS para enviar notas eletrônicas de serviço.  Em contingência foi criado o recurso para que o usuário possa voltar o processo da nota para o layout próprio do TSS (antigo) do município que apresentar erro.  **Procedimento:**   1. Acessar os parâmetros do Gestão de Estoque, Compra e Faturamento 04.03 - Integrações | 04.03.03 - Fiscal | 04.03.03.01 - Dados Fiscais | Parâmetros por Filial | Etapa 2 - Ambiente de Operação da NF-e. Setar o valor do parâmetro TEMPO DE ESPERA P/ENTRAR EM CONTINGÊNCIA para o valor 99999 (cinco números 9). 2. Fechar o RM. 3. Parar o Host. 4. Carregar o Host e o RM novamente 5. Enviar a NFS-e, que agora será enviada no layout antigo. 6. Para retornar basta setar o mesmo parâmetro para o valor 0 (zero) e executar os passos 2, 3 e 4 novamente. |
