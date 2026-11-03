---
article_id: 28930423763351
category: Financeiro - Conciliador Backoffice
content_hash: da964ac0097a6272c405b175f007bf17e1965bbcb3c983e1db472d3529cea526
fetched_at: '2026-06-28T22:37:47.249435+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940- Campos FK5_MSUIDT
  e IG_MSUIDT não são preenchidos
type: support-article
updated_at: '2025-06-02T21:29:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28930423763351-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Campos-FK5-MSUIDT-e-IG-MSUIDT-n%C3%A3o-s%C3%A3o-preenchidos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28930423740183) Tempo aproximado para leitura: **00:05:00 min****Dúvida**CTBA940- Campos FK5\_MSUIDT e IG\_MSUIDT não são preenchidos  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - Financeiro - Todas as versões

**Solução**

O erro "Não é possível a utilização desta configuração de conciliação porque não foram encontrados os seguintes campos de identificação única em seu ambiente: IG\_MSUIDT; FK5\_MSUIDT" ocorre devido à ausência da validação do Wizard do Conciliador. Para resolver, é necessário:

Caso não esteja atualizado, atualizar o BackOffice e dicionário, rodar o UPDDISTR

Executar o wizard WIZARDUUID do conciliador para a opção "gerar SDF com os campos de ID" para a criação do novos campos XXX\_MSUIDT

Para solucionar essa dúvida, realize os seguintes passos:

![Gravar_2025_01_02_17_45_21_436 (1).gif](https://centraldeatendimento.totvs.com/hc/article_attachments/28935201156759) 

### 01. POPULAR OS CAMPOS DE ID

O objetivo da opção Popular os campos de ID é preencher o código de ID único nos registros já gravados do sistema.

#### **01. RESUMO**

O objetivo da opção **Popular os campos de ID** é preencher o código de ID único nos registros já existentes do sistema. Essa opção é importante para que seja possível a utilização do conciliador nos registros do legado. 

Como os campos são novos, no momento da instalação/configuração da rotina eles estarão sem conteúdo.

Importante

Para popular os campos de ID da tabela, é necessário que mesma possua ao menos 1 campo do tipo data, este campo será utilizado para informar o intervalo de datas para o preenchimento do campo.

---

#### **02. PREENCHENDO OS IDS**

Escolher a opção **Popular os campos de ID** e clicar no botão Avançar:

![image2021-10-17_15-11-1.png](https://tdn.totvs.com/download/attachments/644712794/image2021-10-17_15-11-1.png?version=1&modificationDate=1634494261987&api=v2)

Será exibida a tela de apresentação da opção selecionada. No caso desta opção, será exibido um range de datas. 

Esse range representa o período retroativo que se deseja gravar os códigos de ID nos campos XXX\_MSUIDT

![image2022-6-27_10-35-1.png](https://tdn.totvs.com/download/attachments/644712794/image2022-6-27_10-35-1.png?version=1&modificationDate=1660943038193&api=v2)

Atenção

É importante selecionar somente o intervalo que se deseja trabalhar. 

Aconselhamos verificar com cautela essa informação, pois o tempo de processamento dessa rotina é proporcional ao tamanho do período escolhido.

Após clicar em avançar, o sistema exibira a tela com os campos que serão gravados "XXX\_MSUIDT".

Além disso, também serão exibidos os campos que serão utilizados na comparação do range de datas para filtrar os registros.

![image2022-8-19_18-16-46.png](https://tdn.totvs.com/download/attachments/644712794/image2022-8-19_18-16-46.png?version=1&modificationDate=1660943806603&api=v2)

Os campos utilizados para fazer o filtro podem ser editados pelo usuário.

Clicando duas vezes em cima do campo é exibida uma tela com os campos data disponíveis para alteração.

![image2022-8-19_18-16-19.png](https://tdn.totvs.com/download/attachments/644712794/image2022-8-19_18-16-19.png?version=1&modificationDate=1660943779390&api=v2)

Após a confirmação das tabelas selecionadas, o wizard realizará a gravação dos campos de ID

Campos gravados após processamento da rotina:

![image2022-8-19_18-12-31.png](https://tdn.totvs.com/download/attachments/644712794/image2022-8-19_18-12-31.png?version=1&modificationDate=1660943552150&api=v2)

Após o processamento da opção, a mensagem de Processamento Finalizado é exibida.

Ao confirmar, o wizard retornará ao menu de opções.

![image2021-10-17_14-36-41.png](https://tdn.totvs.com/download/attachments/644712794/image2021-10-17_14-36-41.png?version=1&modificationDate=1634495557717&api=v2)

Saiba mais

[Conciliador Backoffice - Configuração e Instalação](https://tdn.totvs.com/pages/viewpage.action?pageId=638741736%20)
