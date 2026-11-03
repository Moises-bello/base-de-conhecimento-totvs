---
article_id: 35070015212951
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: d3a2a57ceb03dbc58a56b29dd7ee300eaca9c9c912ef3a08a33c2a1b65c818f0
fetched_at: '2026-06-28T22:39:09.626806+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA180 - Quais são
  os Pontos de Entrada da rotina de Complemento de Produtos?
type: support-article
updated_at: '2025-10-01T13:50:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35070015212951-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA180-Quais-s%C3%A3o-os-Pontos-de-Entrada-da-rotina-de-Complemento-de-Produtos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35070037488023) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Quais são os Pontos de Entrada da rotina MATA180 - Complementos de Produtos?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Protheus Release 12.1.33 ou Superior.  
  
**Solução**  
Abaixo lista com todos os pontos de entrada disponíveis na rotina rotina MATA180 - Complementos de Produtos

|  |  |  |
| --- | --- | --- |
| **Ponto de Entrada:** | **Título:** | **Descrição:** |
| [MT180MEM](https://tdn.totvs.com/x/NVUbN) | Relação dos campos MEMOS | O Ponto de entrada é executado na função modeldef, após a abertura do tela de alteração, é utilizado para que o usuário monte um vetor contendo a relação dos campos virtuais do tipo MEMO que ele criou. |
| [MT180ROT](https://tdn.totvs.com/x/-F0bN) | Adiciona itens no menu browse | O Ponto de entrada é executado na função menudef, após a criação dos botões, é utilizado para chamar funções ao iniciar o browse ou criar/editar botões dentro do browse. |
| [MTA180MNU](https://tdn.totvs.com/x/W0MbN) | Executa funções e mensagens antes de abrir o browse | O Ponto de entrada é executado na função menudef, após a criação dos botões, é utilizado para chamar funções ao iniciar o browse ou criar/editar botões dentro do browse. |
| [MT180INC](https://tdn.totvs.com/x/S21qMw) | Salva as informações que estão sendo gravadas | O Ponto de entrada é executado no inicio da função de inclusão e de alteração, é utilizado para salvar informações que estão sendo gravadas dentro da SB5 na memoria. |
| [MA180TOK](https://tdn.totvs.com/x/qTgbN) | Validação da rotina de Dados complementares | O Ponto de entrada é executado na função de validação das informações, é utilizado para fazer a validação antes das alterações a serem feitas. |
| [MT180GRV](https://tdn.totvs.com/x/zVobN) | Validações pré gravação dos campos | O Ponto de entrada é executado durante a gravação do campo na tabela, é utilizado para que o usuário possa fazer validações para salvar o campo. |
| [MT180MEM](https://tdn.totvs.com/x/NVUbN) | Relação dos campos MEMOS | O Ponto de entrada é executado na função modeldef, após a abertura do tela de alteração, é utilizado para que o usuário monte um vetor contendo a relação dos campos virtuais do tipo MEMO que ele criou. |

**Saiba mais:**

[Complementos de Produtos - MATA180](https://tdn.totvs.com/x/CDpnF)

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
