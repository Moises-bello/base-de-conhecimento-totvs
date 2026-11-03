---
content_hash: cc1e197c526d1566eb76306b6971b47d91bee081e7b0d03760b48bc33112c68a
fetched_at: '2026-06-29T00:09:28.706908+00:00'
page_id: '423938763'
product: rm
source: tdn-rm
title: Previsão de Faturamento de Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938763
version: 4
---

O relatório de Previsão de Faturamento de Contratos, tem por finalidade, exibir as previsões de faturamento de contratos do tipo "PERIÓDICO" previamente cadastrados de um determinado período.  
 Esta funcionalidade está disponível em: BackOffice -> Gestão de Estoque, Compras e Faturamento | Contratos -> Previsão de Faturamento de Contrato.  
    
 **Parâmetros de entrada necessários para a geração do relatório**

**Filial:**Informar a filial na qual se deseja extrair os dados para o relatório de previsão  
 **Tipo de Movimento:**Deverá ser marcada essa opção caso o usuário deseje filtrar um determinado tipo de movimento para o relatório a ser gerado.  
 **Período:**Informar um determinado intervalo de meses, levando em consideração que o mês inicial deverá ser igual ou superior ao mês atual.  
 **Relatório:**Selecionar o tipo de relatório do RM Reports que será utilizado na geração do mesmo. Após informar os dados de entrada para geração do relatório, basta clicar em Executar que o relatório será gerado.

**Informações importantes na geração do relatório**

1. O campo filial informado pelo usuário no preenchimento dos parâmetros de tela;
2. Os valores de faturamentos devem ser maior que zero;
3. Período determinado pelo usuário (data inicial e data final). Caso o item não possua data fim de faturamento, ele será também exibido no relatório;
4. Os itens do contrato deverão estar com os status: "FATURAROUNAO = 1" e "ECANCELAMENTO = 0", a tabela que contém estes status é a TSTACNT e tem relacionamento com a TITMCNT e utiliza o campo CODSTACNT como chave estrangeira.
