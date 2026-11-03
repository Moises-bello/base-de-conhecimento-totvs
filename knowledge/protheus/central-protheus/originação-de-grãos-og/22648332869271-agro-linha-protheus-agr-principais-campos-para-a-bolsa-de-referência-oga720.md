---
article_id: 22648332869271
category: Originação de Grãos (OG)
content_hash: 9e258b775fabeab3a1bbfb66b2f07653037de3527d20b9b8c4c039873ee63f44
fetched_at: '2026-06-28T22:45:43.286628+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Principais Campos para a Bolsa de Referência
  OGA720
type: support-article
updated_at: '2025-06-21T16:04:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22648332869271-Agro-Linha-Protheus-AGR-Principais-Campos-para-a-Bolsa-de-Refer%C3%AAncia-OGA720
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22648325916567)** Tempo aproximado para leitura:**00:00:45 min****Dúvida**Quais são para a rotina **Principais Campos na Bolsa de Referência OGA720**?  
  
**Ambiente**TOTVS Agro – TOTVS Agro – Comercialização (Linha Protheus) - Originação de Grãos (OG) – Versão 12  
  
**Solução**Aqui abaixo estão apresentados os **principais campos** do cadastro da **Bolsa de Referência**. Alguns campos são exclusivo para integração com sistema de terceiro e que auxiliam no cadastro automático dos índices  servindo como valores de inicialização para os respectivos campos no cadastro de **Índices de Mercado**. Exemplos: **Código de Usuário, Grp. Usuário, Código futuro, Código do produto,** **Unid. Medida, Moeda e Tp Índice**.

|  |  |
| --- | --- |
| Campo | Descrição |
| --- | --- |
| Código | Código da bolsa de referência. |
| Bolsa de ref. | Descrição da bolsa de referência. |
| Preço bolsa | Indica se o preço para a bolsa é fixado ou oriunda de um índice. Caso seja índice, não permitirá a fixação de preço manualmente. Os valores aceitos são:  1 - Fixação;  2 - Índice. |
| URL Integração | URL de integração com API externa para atualização do índice de commodity de bolsa de referência.  Para obter essa funcionalidade é necessário ter os parâmetros [MV\_AGRO200](https://tdn.totvs.com/pages/viewpage.action?pageId=353276270), [MV\_AGRO201](https://tdn.totvs.com/pages/viewpage.action?pageId=353276354), [MV\_AGRO202](https://tdn.totvs.com/pages/viewpage.action?pageId=539531069)devidamente configurados para gerar o token de acesso e conseguir consumir a URL informada neste campo. |
| Código de Usuário | Código do usuário. Permite restringir a atualização de índice vinculados a bolsa de referência por usuário. |
| Grp. Usuário | Código do grupo de usuários. Permite restringir a atualização de índice vinculados a bolsa de referência por grupo de usuário. |
| Código futuro | Código do índice de commodity do sistema externo. Será utilizado para buscar o valores futuros para o índice, atualizando a cotação do índice no Protheus para as respectivas datas. |
| Código do produto | Código produto que estará vinculado a bolsa de referência. |
| Unid. Med. | Código da unidade de medida. |
| Moeda | Código da moeda. |
| Tp Índice | Define a regra que será utilizada para busca dos valores do índice. Os valores aceitos são:  **D - Diário** (Considera o índice do dia para pesquisa. Caso não encontre para a data específica, o valor do índice é zero);  **A - Mais atual** (Considera o índice com a data mais próxima com a data que foi passada para pesquisa);  **F - Fórmula** (Defina-se uma fórmula para busca);  **T - Tabelas** (Indica que a busca será feita em uma tabela de preço previamente cadastrada).  A bolsa de referência é utilizada como meio de integração para inclusão e atualização dos índices automaticamente. Dessa forma, este apenas é utilizado como valor inicial para o campo Tipo de Índice do programa Índices de Mercado na inclusão automática. Quando o tipo for fórmula, a mesma pode ser defina no cadastro de índices de mercado. |
| Integração | Indicador da situação da integração. Os valores aceitos são:  1 - Ativo;  2 - Inativo. |
| Form. Índice | Formato do código do índice. Na integração com a API será retornado um código de índice para ser gravado, porém o usuário poderá formatar este código do índice.  Neste campo use apenas números(0-9), vírgula(,) e hífen(-).  Os números representam a posição do caractere, e inicia na posição 1. A vírgula separa as posições dos caractere. O hífen representa uma sequencia de uma posição de um caractere até a posição de outro.  Por exemplo, considere que a API retornou o código 'CTD08M2018'. O usuário quer somente os 5 primeiros dígitos, então deverá informar: 1-5 ou 1,2,3,4,5 assim será salvo o índice CTD08.  Caso o usuário queira os 5 primeiros dígitos e os 2 últimos, então deverá informar: 1-5,9-10 ou 1-5,9,10 ou  1,2,3,4,5,9,10. |
| Qtd. p/ Ctr Futuro | Indica a quantidade que cada contrato deverá conter. Esta quantidade deve ser expressa na unidade de medida para o contrato.  Exemplo:  1 Contrato = 24 TN ou 1 Contrato = 24000 Kg |
| Unid. Med. Ctr | Unidade de medida para a quantidade do contrato. |
