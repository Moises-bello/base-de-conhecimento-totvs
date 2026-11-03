---
content_hash: 8b91258e5208170469f0f01d9df1cd662870121045930e1da772d0a644f0a521
fetched_at: '2026-06-29T00:06:00.371966+00:00'
page_id: '196804779'
product: rm
source: tdn-rm
title: ER_Historico_Tabela_Vinculo_Salarial
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_Historico_Tabela_Vinculo_Salarial
version: 11
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Pessoas | **Módulo** | RHU |
| **Segmento Executor** |  | | |
| **Projeto1** | RHU – DESENVOLVIMENTO RHU007 | **IRM1** | PCREQ-6303 |
| **Requisito1** | PCREQ-6307 | **Subtarefa1** | PDR\_RHU\_RHU007-46 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** |  | **Réplica** |  |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Criação de histórico de vinculação de tabelas salarias por função ou lotação.

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Assistente de Vinculação de Tabela Salarial | Alteração | Valorização -> Vinculação | - |
| Histórico de Tabela Salarial | Criação | Planejamento e Captação -> Funções -> Histórico de Tabela Salarial | - |
| Histórico de Tabela Salarial | Criação | Planejamento e Captação -> Funções -> Quadro de Lotação ->Histórico de Tabela Salarial | - |

**Assistente de Vinculação de Tabela Salarial**

* Criar um novo campo na base de dados chamado "Data de Vínculo" para os agrupamentos de função e lotação. Este novo campo deve ser atualizado com a data atual do sistema sempre quando houver uma nova vinculação de tabela salarial.
* Criar nova estrutura na base de dados para armazenamento de histórico de vinculação de tabela salarial para os agrupamentos de função e lotação. A nova estrutura deverá conter os seguinte campos:  
  1. IDHISTORICO; - Chave Composta da Tabela
  2. CODCOLIGADA;  - Chave Composta da Tabela
  3. CODTABELA;  - Chave Composta da Tabela
  4. CODNIVEL;  - Chave Composta da Tabela
  5. CODFAIXA;  - Chave Composta da Tabela
  6. VALORSALARIO;
  7. CODSECAO (Para o caso de lotação);
  8. CODFUNCAO;
  9. DATAINICIOVINCULO;
  10. DATAFIMVINCULO;
* O novo histórico de vinculação de tabela salarial deve salvar o histórico de acordo com a inclusão/exclusão/atualização de vinculação de tabela salarial considerando a data de vinculo da inclusão de vinculação e data de exclusão/atualização da vinculação de uma tabela salarial. O histórico também deve considerar os níveis estabelecidos em cada vinculação, bem como todas as suas faixas.
* Criar um novo botão no Assistente de Vinculação de Tabela Salarial para excluir todos os vínculos da seleção atual. Também implementar nos níveis da treeview a opção de teclado "delete" para excluir os os vínculos da seleção bem como os vínculos dos itens filhos. Exibir mensagem de confirmação para exclusão na treeview.

**Anexo Histórico de Tabela Salarial**

* Criar um novo anexo para exibição do histórico de vinculação de tabela salarial. Este anexo deverá ser somente leitura, não permitindo inclusão/alteração/exclusão de registros
* O novo anexo deve ser adicionado as visões de Função e Lotação, e devem exibir o histórico de acordo com os agrupadores á época da vinculação. O novo anexo de histórico irá mostrar em sua visão o nome da tabela e as datas de vinculação da tabela salarial. Em sua edição, que será somente leitura, iremos mostrar o detalhe do histórico da tabela, mostrando nível, faixa e valor do salário da tabela.
  1. Ex.: Hoje o usuário realiza uma vinculação de tabela salarial considerando o agrupador por função. Amanhã o usuário realiza uma vinculação de tabela salarial considerando o agrupador por lotação.
  2. Este parâmetro está localizado no seguinte caminho: RH -> Gestão de Pessoas -> Configurações -> Parametrizador -> Validações -> Usar Seção e/ou Lotação na organização das Tabelas Salariais

***Tabelas Utilizadas***

* VNIVEISTABSALARIAISLOTACAO - Alteração com o novo campo "Data de Vínculo"
* VNIVEISTABSALARIAISFUNCAO - Alteração com o novo campo "Data de Vínculo"
* VHISTNIVEISTABSALARIAISLOTACAO - Nova tabela de histórico por lotação
* VHISTNIVEISTABSALARIAISFUNCAO - Nova tabela de histórico por função

## Protótipo de Tela

**Protótipo 01**

## **Protótipo 02**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
