---
article_id: 1500004325941
category: SIGAEST - MOVIMENTAÇÕES
content_hash: c594df0e75d893436b903d9efe34d4346245bee64917f0d3c7927fe30bfeb3f6
fetched_at: '2026-06-28T22:38:55.783950+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA175 - Pontos de
  Entrada da rotina Baixa de CQ
type: support-article
updated_at: '2025-11-13T16:46:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004325941-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA175-Pontos-de-Entrada-da-rotina-Baixa-de-CQ
---

A rotina MATA175 - Baixa de CQ no TOTVS Protheus possui diversos pontos de entrada para personalização, incluindo:

**MT175BUT** (adiciona botões), **MT175ATU** (valida atualização do movimento), **A175CQ** e **A175GRV** (liberação/rejeição do material), **MT175LOK** e **MT175FOK** (valida linhas), MT175TOK (consistências adicionais), **M175VSLD** (validação do saldo disponível), **A175ALMO** (manipula armazém padrão) e **MTA175MNU** (adiciona botões no menu principal).

**Dúvida**  
Quais são os Pontos de Entrada da rotina Baixa de CQ - MATA175?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Veja abaixo os pontos de entrada relacionados à rotina MATA175- Baixa de CQ (Centro de Qualidade):

|  |  |  |
| --- | --- | --- |
| **Ponto de Entrada** | **Título:** | **Descrição:** |
| **[MA175BUT](https://tdn.totvs.com/pages/releaseview.action?pageId=6087604)** | Adiciona botões de usuário | Descrição: LOCALIZAÇÃO : Function A175LIBEST - Função que monta a tela com as opções do menu de liberação.    EM QUE PONTO : Antes da EnchoiceBar. Deve ser utilizado para adicionar botões do usuário, por meio do retorno de um Array, com a estrutura do botão a ser adicionado. |
| **[MT175ATU](https://tdn.totvs.com/pages/releaseview.action?pageId=6087712)** | Valida atualização do movimento | Descrição: LOCALIZAÇÃO : Function A175LibEst() - Exclusivo ao MatA175 para liberação.    EM QUE PONTO : É ativado na Confirmação da Liberação/Rejeição ou na Confirmação do Estorno.  Validar atualização do movimento. |
| **[A175CQ](https://tdn.totvs.com/pages/releaseview.action?pageId=235597762)** | Liberação/Rejeição do Material no CQ | Descrição: LOCALIZAÇÃO : Function A175Grava() - Responsável por realizar a Liberacao/Rejeicao do Material no CQ.    EM QUE PONTO : BAIXAS DO CQ |
| **[A175GRV](https://tdn.totvs.com/pages/releaseview.action?pageId=286518350)** | Grava Liberação/Rejeição no CQ. | Descrição: LOCALIZAÇÃO : Function A175Grava() - Responsável por realizar a Liberação/Rejeição do Material no CQ.    EM QUE PONTO : É chamado após a gravação de todos os dados (função FGRAVACQ), inclusive após gerar a requisição no arquivo de movimentos internos (SD3). |
| **[MT175LOK](https://tdn.totvs.com/pages/releaseview.action?pageId=6085784)** | Permite armazém destino que não esteja cadastrado no sistema | Descrição:  Localização.: Function A175LinOk - Critica se a linha digitada esta OK  Finalidade...: Permitir Armazém destino que não esteja cadastrado no sistema. |
| **[MT175FOK](https://tdn.totvs.com/display/public/PROT/MT175FOK+-+Valida+a+linha+do+baixas+do+CQ)** | Valida a linha das baixas do CQ | Este ponto de entrada tem o objetivo personalizar a validação da Linha.LOCALIZAÇÃO: Function A175linOk - No momento em que verifica a validação da linha no final do processo |
| **[MT175TOK](https://tdn.totvs.com/pages/releaseview.action?pageId=6085547)** | Efetua consistências adicionais | O Ponto de Entrada MT175TOK permite efetuar consistências adicionais, antes de efetuar a Liberação do CQ. |
| **[M175VSLD](https://tdn.totvs.com/pages/releaseview.action?pageId=6087993)** | Customização da Validação do Saldo Disponível | Este Ponto de Entrada permite customizar a validação do saldo disponível, para realizar o estorno na baixa do CQ. Está localizado na função A175GetDad, com a finalidade de verificar campo a campo da GetDados. |
| **[A175ALMO](https://tdn.totvs.com/pages/releaseview.action?pageId=49283605)** | Permite manipular o conteúdo do armazém padrão sugerido pela rotina durante aprovação | Permite manipular o conteúdo do armazém padrão sugerido pela rotina durante aprovação |
| **[MA175BUV](https://tdn.totvs.com/x/JSTzNQ)** | Criação do ponto de entrada MA175BUV que disponibiliza a funcionalidade de adicionar um botão de usuário na opção visualizar. | LOCALIZAÇÃO: Function A175Visual - Função que monta a tela com as opções do menu do botão Visualizar. EM QUE PONTO: Antes da EnchoiceBar que é criada ao clicar no botão "Visualizar". Deve ser utilizado para adicionar botões do usuário, por meio do retorno de um Array, com a estrutura do botão a ser adicionado. |
| **[MTA175MNU](https://tdn.totvs.com/pages/releaseview.action?pageId=6087794)** | Adiciona botões no menu principal da rotina | Descrição:  LOCALIZAÇÃO : Function MATA175- Rotina responsável pelas Baixas do Controle de Qualidade (CQ).  EM QUE PONTO : Antes de montar a tela do browse; Pode ser usado para adicionar botões no menu principal da rotina. |

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
