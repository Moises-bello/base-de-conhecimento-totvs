---
content_hash: c8be1fc2e3d18bcbc1819401ff8537ad3c4d5e2e9fd766eb1e4dc1c8f60b625a
fetched_at: '2026-06-29T00:06:17.569287+00:00'
page_id: '213979816'
product: rm
source: tdn-rm
title: DT_Nova_Regra_de_Faturamento_por_Limite_de_Teto_e_Valor
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Nova_Regra_de_Faturamento_por_Limite_de_Teto_e_Valor
version: 1
---

# Nova Regra de Faturamento por Limite de Teto e Valor

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Condições Contratuais para Convênios, Faturamento para Convênios | |
| **Requisito (ISSUE):** | PCREQ-2295 |
| **Tabelas Utilizadas:** | SZCONDCONTRAT, SZFAIXAHEMOCOMP, SZFATHEMOCOMP, SZFATHEMOCOMPPCT, SZFATHEMOCOMPITEM |
| **Sistema(s) Operacional(is):** | Windows |
| **Versões/Release:** | 12.1.7 |

## Descrição

   Esta implementação consiste em prover, através das condições contratuais do convênio, os cadastros necessários para contemplar as quatro diferentes situações de Faturamento de Hemocomponentes e seus Itens associados, ou avulsos.

   Consiste também em prover, através do processo de faturamento para convênios a possibilidade de faturamento de Hemocomponentes.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

 O Patch 12.1.6 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.6.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Client.

**Para acesso siga as instruções abaixo:**

1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).
2. Faça o login, com seu E-mail e Senha.
3. Na barra de menu superior, clique em DOWNLOAD.
4. No boxe Central de Downloads aplique os filtros conforme campos abaixo:
   1. Linha: RM
   2. Versão: RM 12.1.6
   3. Tipo: Patch

Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

 Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

Importante: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

 Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

**Exemplo:**

1. No **TOTVS Gestão Hospitalar**, acesse o menu **Cadastros / Faturamento / Condições Contratuais com Convênios**.
2. Selecione o convênio e acesse a aba **Faturamento Hemocomponentes**.
3. Marque a opção **Fatura de Hemocomponentes** e selecione o tipo de faturamento desejado.
4. Crie um atendimento para este convênio e, conforme a parametrização realizada, lance os itens na conta. Caso a conta seja dos tipos 1 ou 2, se entende que essa conta deverá conter Hemocomponentes. Os Hemocomponentes serão entendidos como pacotes pelo sistema (RM Saúde), portanto, no cadastro da taxa ou serviço, o campo “pacote”, deverá estar marcado.
5. Após lançar o pacote na conta, o item ficará com uma faixa vermelha, conforme imagem.
6. A partir deste momento, esta conta é considerada uma conta do tipo “pacote” ou seja, todos os itens que não sejam pacotes, lançados nesta conta, constarão como pertencentes a algum pacote.
7. Caso seja necessário que o Item seja considerado como um “**Item Avulso**”, clique com o botão direito sobre ele e clique na opção Incluir Item na cobrança de pacote. Uma faixa vermelha será exibida sobre este item e ele passará a ter o campo “**INCLUIDOPACOTE” = T**, em sua respectiva tabela.
8. Encerre a conta do paciente.
9. Acesse o menu **Faturamento / Fatura para Convênios** e crie uma nova remessa para o convênio utilizado.
10. Gere esta fatura, contendo esta conta recém encerrada.
11. Os dados referentes ao faturamento de Hemocomponentes serão persistidos seguintes tabelas:

* **SZFATURAHEMOCOMP:** Tabela Pai, onde estarão as informações referentes à fatura recém-criada, como a soma do valor de todos os itens, informações sobre o convenio, unidade, etc.
* **SZFATURAHEMOCOMPPCT:** Tabela onde serão armazenados os dados referentes aos pacotes, onde constarão as informações como Descrição, quantidade, valor, valor total, entre outras.
* **SZFATURAHEMOCOMPITEM:** Tabela onde serão armazenados os dados referentes aos itens.

A comunicação entre as tabelas, que deverá ser levada em consideração na elaboração de relatório, obedece a seguinte estrutura:

divs
