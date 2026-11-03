---
article_id: 360037766693
category: Relatórios e Workflows
content_hash: 8454d5aa16386600d610a871d391fd13a95dd940ca082064ff0473e180348ace
fetched_at: '2026-06-28T22:42:31.682038+00:00'
product: protheus
section_id: 360010992394
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Geração do relatório MNTR935
type: support-article
updated_at: '2021-06-17T19:40:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037766693-Manufatura-Linha-Protheus-MNT-Gera%C3%A7%C3%A3o-do-relat%C3%B3rio-MNTR935
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:02:15 min**  
**Dúvida**Como gerar o relatório **MNTR935 - Indicadores de Rendimento Combust.**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Relatórios e Workflows - Todas as versões  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:

1. Acesse o módulo **SIGAMNT - Manutenção de Ativos**.
2. Em **Atualizações - Controle de Oficina - Cadastros Básicos - Produtos** **- MATA010** inclua um produto.
3. Em **Atualizações - Controle de Oficina - Cadastros Básicos - Funcionários** **- GPEA010** inclua um funcionário.
4. Em **Atualizações - Controle de Oficina - Cadastros Básicos - Motoristas** **- OMSA040** inclua um motorista e não deixe de informar um número de **CPF - Cadastro de Pessoa Física**.
5. Em **Atualizações - Controle de Oficina - Cadastros Básicos - Fornecedores** **- MATA020** inclua um fornecedor.
6. Em **Atualizações - Controle de Combustíveis - Cadastros Postos - Tipos de Combustíveis - MNTA640** inclua um combustível.
7. Em **Atualizações - Controle de Combustíveis - Cadastros Postos - Postos - MNTA610** inclua dois postos com a negociação e o preço.
8. Em **Atualizações - Controle de Combustíveis - Cadastros Postos - Posto Interno - MNTA615** clique em **Tanques/Bombas**. Informe um tanque e relacione ao produto incluído anteriormente.
9. Em **Atualizações - Controle de Oficina - Bens - Veículos - MNTA084** inclua um veículo com campo **Categoria** igual **4 - Frota não Integrada ao TMS** e campo **Tem Contador**igual **S** - **Tem Contador Próprio**. Na aba **Complemento Veículo**, preencha os dados referente aos campos **Placa** e **Tipo Veiculo**. Em **Ações Relacionadas**, clique em **Tanque** e informe um tanque de combustível para o veículo, relacionando ao tipo de combustível informado no **passo 6**.
10. Em **Atualizações - Controle de Combustíveis - Abastecimento - Abastecimento Manual - MNTA655** inclua ao menos dois abastecimentos sendo um em cada posto.
11. Em **Relatórios - Controle de Combustíveis - Rel. Gerenciais - Indicadores de Rendimento Combust** **- MNTR935** informe os dados de forma que consigam abranger os abastecimentos cadastrados e selecione a opção **Imprimir**.
