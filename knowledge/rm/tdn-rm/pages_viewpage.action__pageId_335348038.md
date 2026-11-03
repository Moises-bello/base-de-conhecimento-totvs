---
content_hash: 02127d1ed068cae7ee2cc8326f8733f62e1aa8725bf2501159fc73f5e6e411da
fetched_at: '2026-06-29T00:08:50.966483+00:00'
page_id: '335348038'
product: rm
source: tdn-rm
title: RMPAT00001_Exportação de Dados do Gestão Patrimonial.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=335348038
version: 8
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | Totvs Gestão Patrimonial |
| **Versões:** | 12.1.18 |
| **Ocorrência:** | Exportação de patrimônio |
| **Ambiente:** |  |
| **Passo a passo:** | **Introdução**  Através da execução deste processo, será possível exportar dados cadastrados no TOTVS Gestão Patrimonial*.*  **Desenvolvimento/Procedimento**  Primeiramente você deverá realizar a criação/importação do Conceito de exportação. Através da nova MDI:  a) Acessar o menu 'Integrações' / 'Conceito' / 'Processos' / 'Importar Conceito';  b) No caminho abaixo estão disponíveis todos os ICP's de exportação do TOTVS Gestão Patrimonial: C:\totvs\CorporeRM\objetosgerenciais\conceito\CONPAT0004 - Exportação de Patrimônio.icp  c) Selecione o ICP deseja e clique em **Executar**;  **Alteração do Conceito**  Com o Conceito criado será necessário realizar algumas modificações no mesmo conforme descrito abaixo:  Na aba 'Conexões de Origem' na linha **String de Conexão** substitua  **Data Source** = informe sua máquina da rede de sua empresa" **Initial Catalog**=nome da base no banco de dados **User ID**=nome do usuário do banco de dados **Password**=senha do usuário do banco de dados  No print abaixo veja um exemplo com estes campos já preenchidos.      Clique no botão **Testar,** para verificar se na conexão realmente existe, ou seja, se esta máquina, caminho e usuário existem para a conexão**.**      Antes de executar o conceito, será necessário crie um arquivo txt vazia, e informe o caminho no campo Arquivo; conforme print abaixo.      Sendo o processo efetuado com sucesso será apresentada a mensagem.  Após este processo o conceito poderá ser processado através do menu 'Processos' / 'Processar Conceito'. |
| **Observações:** |  |
